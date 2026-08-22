#!/usr/bin/env python3
"""Manage durable state for the personalized learning tutor."""
from __future__ import annotations
import argparse, json, sqlite3
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
DB = ROOT / ".learning" / "learning-state.sqlite3"
SCHEMA = ROOT / ".learning" / "schema.sql"

def connection():
    DB.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(DB); conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON"); return conn

def initialize():
    with connection() as conn: conn.executescript(SCHEMA.read_text(encoding="utf-8"))

def emit(row): print(json.dumps(dict(row) if row else {}, ensure_ascii=False, indent=2))
def require(conn, table, value):
    row = conn.execute(f"SELECT id FROM {table} WHERE id=?", (value,)).fetchone()
    if not row: raise SystemExit(f"unknown {table}: {value}")

def topic_start(a):
    with connection() as c:
        c.execute("""INSERT INTO learning_topics(slug,title,source_context,summary_dir,summary_path,target_level,status) VALUES(?,?,?,?,?,?,'active')
        ON CONFLICT(slug) DO UPDATE SET title=excluded.title,source_context=excluded.source_context,summary_dir=excluded.summary_dir,summary_path=excluded.summary_path,target_level=excluded.target_level,status='active',updated_at=CURRENT_TIMESTAMP""", (a.slug,a.title,a.source_context,a.summary_dir,a.summary_path,a.target_level))
        emit(c.execute("SELECT * FROM learning_topics WHERE slug=?",(a.slug,)).fetchone())
def plan_start(a):
    plan={k:getattr(a,k.replace('-','_')) for k in ('goal','scope','non-goals','prerequisites','stages','evidence','stop-condition')}
    with connection() as c:
        t=c.execute("SELECT id FROM learning_topics WHERE slug=?",(a.topic,)).fetchone()
        if not t: raise SystemExit(f"unknown topic: {a.topic}")
        cur=c.execute("INSERT INTO learning_sessions(topic_id,mode,goal,target_level,plan_json) VALUES(?,?,?, ?,?)",(t['id'],'teaching',a.goal,a.target_level,json.dumps(plan,ensure_ascii=False)))
        c.execute("INSERT INTO learning_plans(session_id,scope,non_goals,prerequisites,stages,evidence,stop_condition) VALUES(?,?,?,?,?,?,?)",(cur.lastrowid,a.scope,a.non_goals,a.prerequisites,a.stages,a.evidence,a.stop_condition))
        emit(c.execute("SELECT * FROM learning_sessions WHERE id=?",(cur.lastrowid,)).fetchone())
def source_add(a):
    with connection() as c:
        tid=c.execute("SELECT id FROM learning_topics WHERE slug=?",(a.topic,)).fetchone()['id'] if a.topic else None
        c.execute("INSERT OR IGNORE INTO source_references(session_id,topic_id,url,source_type,title,version,confidence,notes) VALUES(?,?,?,?,?,?,?,?)",(a.session,tid,a.url,a.type,a.title,a.version,a.confidence,a.notes))
        emit(c.execute("SELECT * FROM source_references WHERE url=? AND session_id IS ?",(a.url,a.session)).fetchone())
def checkpoint_add(a):
    with connection() as c:
        require(c,'learning_sessions',a.session); c.execute("INSERT INTO checkpoints(session_id,question,answer,result,evidence,tags) VALUES(?,?,?,?,?,?)",(a.session,a.question,a.answer,a.result,a.evidence,a.tags)); emit(c.execute("SELECT * FROM checkpoints WHERE id=last_insert_rowid()").fetchone())
def knowledge_set(a):
    with connection() as c:
        t=c.execute("SELECT id FROM learning_topics WHERE slug=?",(a.topic,)).fetchone()
        if not t: raise SystemExit(f"unknown topic: {a.topic}")
        c.execute("""INSERT INTO knowledge_states(topic_id,skill_key,level,confidence,evidence,next_action) VALUES(?,?,?,?,?,?)
        ON CONFLICT(topic_id,skill_key) DO UPDATE SET level=excluded.level,confidence=excluded.confidence,evidence=excluded.evidence,next_action=excluded.next_action,assessed_at=CURRENT_TIMESTAMP""",(t['id'],a.skill,a.level,a.confidence,a.evidence,a.next_action)); emit(c.execute("SELECT * FROM knowledge_states WHERE topic_id=? AND skill_key=?",(t['id'],a.skill)).fetchone())
def misconception_add(a):
    with connection() as c:
        tid=c.execute("SELECT id FROM learning_topics WHERE slug=?",(a.topic,)).fetchone()['id'] if a.topic else None
        c.execute("INSERT INTO misconceptions(topic_id,session_id,skill_key,tag,description,severity,evidence) VALUES(?,?,?,?,?,?,?)",(tid,a.session,a.skill,a.tag,a.description,a.severity,a.evidence)); emit(c.execute("SELECT * FROM misconceptions WHERE id=last_insert_rowid()").fetchone())
def interview_start(a):
    with connection() as c:
        tid=c.execute("SELECT id FROM learning_topics WHERE slug=?",(a.topic,)).fetchone()['id'] if a.topic else None
        cur=c.execute("INSERT INTO learning_sessions(topic_id,mode,goal,plan_json) VALUES(?,?,?,?)",(tid,'interview',a.goal,json.dumps({'dimensions':a.dimensions,'stop_condition':a.stop_condition},ensure_ascii=False)))
        c.execute("INSERT INTO interview_sessions(session_id,target_role,target_level,mode) VALUES(?,?,?,?)",(cur.lastrowid,a.role,a.level,a.mode)); emit(c.execute("SELECT * FROM interview_sessions WHERE session_id=?",(cur.lastrowid,)).fetchone())
def interview_question(a):
    with connection() as c:
        require(c,'interview_sessions',a.interview); c.execute("INSERT INTO interview_questions(interview_id,sequence_no,question,answer,followups,score,result,evidence,tags) VALUES(?,?,?,?,?,?,?,?,?)",(a.interview,a.sequence,a.question,a.answer,a.followups,a.score,a.result,a.evidence,a.tags)); emit(c.execute("SELECT * FROM interview_questions WHERE id=last_insert_rowid()").fetchone())
def interview_finish(a):
    with connection() as c:
        row=c.execute("SELECT session_id FROM interview_sessions WHERE id=?",(a.interview,)).fetchone()
        if not row: raise SystemExit(f"unknown interview: {a.interview}")
        c.execute("UPDATE interview_sessions SET overall_result=?,scores_json=?,strengths=?,gaps=?,next_actions=?,debriefed_at=CURRENT_TIMESTAMP WHERE id=?",(a.result,a.scores,a.strengths,a.gaps,a.next_actions,a.interview)); c.execute("UPDATE learning_sessions SET status='completed',ended_at=CURRENT_TIMESTAMP WHERE id=?",(row['session_id'],)); emit(c.execute("SELECT * FROM interview_sessions WHERE id=?",(a.interview,)).fetchone())
def preference_set(a):
    with connection() as c:
        c.execute("""INSERT INTO learner_preferences(key,value,evidence,confirmed) VALUES(?,?,?,?) ON CONFLICT(key) DO UPDATE SET value=excluded.value,evidence=excluded.evidence,confirmed=excluded.confirmed,updated_at=CURRENT_TIMESTAMP""",(a.key,a.value,a.evidence,int(a.confirmed))); emit(c.execute("SELECT * FROM learner_preferences WHERE key=?",(a.key,)).fetchone())
def next_actions(a):
    with connection() as c: print(json.dumps([dict(r) for r in c.execute("""SELECT t.slug,t.title,k.skill_key,k.level,k.next_action,k.evidence FROM knowledge_states k JOIN learning_topics t ON t.id=k.topic_id WHERE t.status='active' AND (k.next_action IS NOT NULL OR k.level<t.target_level) ORDER BY k.level,k.assessed_at""")],ensure_ascii=False,indent=2))
def parser():
    p=argparse.ArgumentParser(); s=p.add_subparsers(dest='command',required=True)
    def cmd(n,f): q=s.add_parser(n); q.set_defaults(func=f); return q
    cmd('init',lambda a:initialize())
    q=cmd('topic-start',topic_start); q.add_argument('slug');q.add_argument('title');q.add_argument('--source-context');q.add_argument('--summary-dir',default='docs/learning');q.add_argument('--summary-path');q.add_argument('--target-level',type=int,default=2)
    q=cmd('plan-start',plan_start); q.add_argument('--topic',required=True);q.add_argument('--goal',required=True);q.add_argument('--scope',required=True);q.add_argument('--non-goals',required=True);q.add_argument('--prerequisites',required=True);q.add_argument('--stages',required=True);q.add_argument('--evidence',required=True);q.add_argument('--stop-condition',required=True);q.add_argument('--target-level',type=int,default=2)
    q=cmd('source-add',source_add);q.add_argument('url');q.add_argument('--session',type=int);q.add_argument('--topic');q.add_argument('--type',required=True,choices=['official','documentation','blog','interview','repository','other']);q.add_argument('--title');q.add_argument('--version');q.add_argument('--confidence',default='medium',choices=['low','medium','high']);q.add_argument('--notes')
    q=cmd('checkpoint-add',checkpoint_add);q.add_argument('--session',required=True,type=int);q.add_argument('--question',required=True);q.add_argument('--answer');q.add_argument('--result',required=True,choices=['pass','partial','fail','not_answered']);q.add_argument('--evidence');q.add_argument('--tags')
    q=cmd('knowledge-set',knowledge_set);q.add_argument('--topic',required=True);q.add_argument('--skill',required=True);q.add_argument('--level',type=int,required=True);q.add_argument('--confidence',type=float,required=True);q.add_argument('--evidence',required=True);q.add_argument('--next-action')
    q=cmd('misconception-add',misconception_add);q.add_argument('--skill',required=True);q.add_argument('--tag',required=True);q.add_argument('--description',required=True);q.add_argument('--topic');q.add_argument('--session',type=int);q.add_argument('--severity',default='medium',choices=['low','medium','high','critical']);q.add_argument('--evidence')
    q=cmd('interview-start',interview_start);q.add_argument('--goal',required=True);q.add_argument('--mode',required=True);q.add_argument('--topic');q.add_argument('--role');q.add_argument('--level');q.add_argument('--dimensions',required=True);q.add_argument('--stop-condition',required=True)
    q=cmd('interview-question',interview_question);q.add_argument('--interview',type=int,required=True);q.add_argument('--sequence',type=int,required=True);q.add_argument('--question',required=True);q.add_argument('--answer');q.add_argument('--followups');q.add_argument('--score',type=int);q.add_argument('--result',required=True,choices=['strong','pass','partial','weak','unknown']);q.add_argument('--evidence');q.add_argument('--tags')
    q=cmd('interview-finish',interview_finish);q.add_argument('--interview',type=int,required=True);q.add_argument('--result',required=True);q.add_argument('--scores',required=True);q.add_argument('--strengths',required=True);q.add_argument('--gaps',required=True);q.add_argument('--next-actions',required=True)
    q=cmd('preference-set',preference_set);q.add_argument('key');q.add_argument('value');q.add_argument('--evidence',required=True);q.add_argument('--confirmed',action='store_true')
    cmd('next',next_actions); return p
if __name__=='__main__':
    a=parser().parse_args(); a.func(a)
