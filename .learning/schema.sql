PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS learning_topics (
  id INTEGER PRIMARY KEY,
  slug TEXT NOT NULL UNIQUE,
  title TEXT NOT NULL,
  source_context TEXT,
  target_level INTEGER NOT NULL DEFAULT 2 CHECK (target_level BETWEEN 0 AND 6),
  status TEXT NOT NULL DEFAULT 'active' CHECK (status IN ('active','paused','completed')),
  created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS knowledge_states (
  id INTEGER PRIMARY KEY,
  topic_id INTEGER NOT NULL REFERENCES learning_topics(id) ON DELETE CASCADE,
  skill_key TEXT NOT NULL,
  level INTEGER NOT NULL DEFAULT 0 CHECK (level BETWEEN 0 AND 6),
  confidence REAL NOT NULL DEFAULT 0 CHECK (confidence BETWEEN 0 AND 1),
  evidence TEXT NOT NULL,
  next_action TEXT,
  assessed_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
  UNIQUE(topic_id, skill_key)
);

CREATE TABLE IF NOT EXISTS learning_sessions (
  id INTEGER PRIMARY KEY,
  topic_id INTEGER REFERENCES learning_topics(id) ON DELETE SET NULL,
  mode TEXT NOT NULL CHECK (mode IN ('teaching','practice','review','interview','debrief')),
  goal TEXT NOT NULL,
  target_level INTEGER CHECK (target_level BETWEEN 0 AND 6),
  status TEXT NOT NULL DEFAULT 'active' CHECK (status IN ('active','completed','stopped','blocked')),
  plan_json TEXT NOT NULL,
  started_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
  ended_at TEXT
);

CREATE TABLE IF NOT EXISTS checkpoints (
  id INTEGER PRIMARY KEY,
  session_id INTEGER NOT NULL REFERENCES learning_sessions(id) ON DELETE CASCADE,
  question TEXT NOT NULL,
  answer TEXT,
  result TEXT CHECK (result IN ('pass','partial','fail','not_answered')),
  evidence TEXT,
  tags TEXT,
  created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS source_references (
  id INTEGER PRIMARY KEY,
  session_id INTEGER REFERENCES learning_sessions(id) ON DELETE SET NULL,
  topic_id INTEGER REFERENCES learning_topics(id) ON DELETE SET NULL,
  url TEXT NOT NULL,
  source_type TEXT NOT NULL CHECK (source_type IN ('official','documentation','blog','interview','repository','other')),
  title TEXT,
  version TEXT,
  confidence TEXT NOT NULL DEFAULT 'medium' CHECK (confidence IN ('low','medium','high')),
  notes TEXT,
  accessed_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
  UNIQUE(url, session_id)
);

CREATE TABLE IF NOT EXISTS misconceptions (
  id INTEGER PRIMARY KEY,
  topic_id INTEGER REFERENCES learning_topics(id) ON DELETE SET NULL,
  session_id INTEGER REFERENCES learning_sessions(id) ON DELETE SET NULL,
  skill_key TEXT NOT NULL,
  tag TEXT NOT NULL,
  description TEXT NOT NULL,
  severity TEXT NOT NULL DEFAULT 'medium' CHECK (severity IN ('low','medium','high','critical')),
  resolved INTEGER NOT NULL DEFAULT 0 CHECK (resolved IN (0,1)),
  evidence TEXT,
  created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
  resolved_at TEXT
);

CREATE TABLE IF NOT EXISTS interview_sessions (
  id INTEGER PRIMARY KEY,
  session_id INTEGER NOT NULL UNIQUE REFERENCES learning_sessions(id) ON DELETE CASCADE,
  target_role TEXT,
  target_level TEXT,
  mode TEXT NOT NULL,
  overall_result TEXT,
  scores_json TEXT,
  strengths TEXT,
  gaps TEXT,
  next_actions TEXT,
  debriefed_at TEXT
);

CREATE TABLE IF NOT EXISTS interview_questions (
  id INTEGER PRIMARY KEY,
  interview_id INTEGER NOT NULL REFERENCES interview_sessions(id) ON DELETE CASCADE,
  sequence_no INTEGER NOT NULL,
  question TEXT NOT NULL,
  answer TEXT,
  followups TEXT,
  score INTEGER CHECK (score BETWEEN 0 AND 5),
  result TEXT CHECK (result IN ('strong','pass','partial','weak','unknown')),
  evidence TEXT,
  tags TEXT,
  source_reference_id INTEGER REFERENCES source_references(id) ON DELETE SET NULL,
  UNIQUE(interview_id, sequence_no)
);

CREATE TABLE IF NOT EXISTS learner_preferences (
  key TEXT PRIMARY KEY,
  value TEXT NOT NULL,
  evidence TEXT,
  confirmed INTEGER NOT NULL DEFAULT 0 CHECK (confirmed IN (0,1)),
  updated_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX IF NOT EXISTS idx_knowledge_topic ON knowledge_states(topic_id);
CREATE INDEX IF NOT EXISTS idx_checkpoint_session ON checkpoints(session_id);
CREATE INDEX IF NOT EXISTS idx_misconception_open ON misconceptions(resolved, skill_key);
CREATE INDEX IF NOT EXISTS idx_interview_question_tags ON interview_questions(tags);
