# my-learn-skills

这是一个个人学习型 skills 仓库，目标是把“项目拆解、概念教学、代码链路理解、带学 Review、讲后检验、文档回写”拆成小 skill 后组合使用。另外hys最帅了

## 设计原则

- 小 skill 优先：一个 skill 只负责一类动作。
- 编排和执行分离：`learn-orchestrator` 只决定顺序，不代替子 skill 工作。
- 项目场景优先：技术点必须回到真实业务链路。
- 讲后必须检验：没有 checkpoint，不算完成学习闭环。
- 稳定结论才回写：临时讨论不进入长期文档。
- issue/PR 优先：用户粘贴 issue、PR 或 review comments 时，先抽取精准上下文，不扫全仓库。
- 参考资料留痕：教学时用到的外部文档链接，要随回答输出或写入总结文档对应知识点。

- `learn-orchestrator`：学习流程路由和组合。
- `adaptive-tutor`：不预设前置知识，生成可验证的 OpenSpec 风格教学计划并控制主线。
- `interview-simulator`：真实模拟面试、连续追问和逐题复盘。
- `issue-pr-intake`：从 issue、PR、评论或链接提取精准上下文。
- `learn-context`：收集最小必要项目上下文。
- `project-deep-dive`：把项目或模块拆成学习切片。
- `source-researcher`：查官方资料和外部候选。
- `code-path-tracer`：追一条代码执行链路。
- `architecture-lens`：分析架构边界和设计取舍。
- `concept-teacher`：结合项目讲概念。
- `review-coach`：带学式代码和设计 Review。
- `learning-checkpoint`：出短题或最小实操检验理解。
- `learning-note-writer`：把稳定结论分层回写。

通用系统提示词：`docs/tutor-system-prompt.md`。

## 典型组合

- 学项目：`learn-context` -> `project-deep-dive` -> `learning-checkpoint`
- 接 issue/PR：`issue-pr-intake` -> `learn-context` -> 对应处理 skill -> `learning-checkpoint`
- 看接口：`learn-context` -> `code-path-tracer` -> `architecture-lens` -> `concept-teacher` -> `learning-checkpoint`
- 学概念：`source-researcher` -> `concept-teacher` -> `learning-checkpoint`
- 做 Review：`learn-context` -> `review-coach` -> `concept-teacher` -> `learning-checkpoint`
- 写沉淀：`learning-checkpoint` -> `learning-note-writer`


## 持久化工作流

数据库位于 `.learning/learning-state.sqlite3`，通过 `scripts/learning_state.py` 操作：

```bash
python3 scripts/learning_state.py init
python3 scripts/learning_state.py topic-start <slug> <title> --target-level 3
python3 scripts/learning_state.py plan-start --topic <slug> --goal <goal> --scope <scope> --non-goals <non-goals> --prerequisites <prerequisites> --stages <stages> --evidence <evidence> --stop-condition <stop-condition>
python3 scripts/learning_state.py checkpoint-add --session <id> --question <question> --result partial --evidence <evidence>
python3 scripts/learning_state.py knowledge-set --topic <slug> --skill <skill> --level 2 --confidence 0.5 --evidence <evidence> --next-action <action>
python3 scripts/learning_state.py interview-start --goal <goal> --mode project-deep-dive --dimensions <dimensions> --stop-condition <condition>
python3 scripts/learning_state.py interview-question --interview <id> --sequence 1 --question <question> --result partial --score 2 --evidence <evidence>
python3 scripts/learning_state.py interview-finish --interview <id> --result <result> --scores <json> --strengths <text> --gaps <text> --next-actions <text>
python3 scripts/learning_state.py next
```

通用导师系统提示词位于 `docs/tutor-system-prompt.md`。
## 来源约束

本仓库的规则抽象自本地 `blog` 仓库里的学习型项目要求：真实业务链路、工程门禁、单主题 issue、讲后检验、分层回写。外部 GitHub 候选只吸收可借鉴模式，不直接照搬。

## 在其它仓库生效

推荐使用项目级集成：先扫描目标仓库已有 `.agents/skills` 和 `AGENTS.md`，再只复制无冲突缺失项。已有规则和相似 skill 不覆盖，改由 `repo-skill-integrator` 给出综合重塑建议。

先 dry-run 看会复制什么：

```bash
python3 scripts/sync_to_repo.py /path/to/target-repo
```

确认无误后写入安全缺失项，并在需要时生成 `docs/learning-skill-integration-plan.md`：

```bash
python3 scripts/sync_to_repo.py /path/to/target-repo --apply
```

如果报告提示同名或相似 skill，不要并排保留；让当次会话的 agent 使用 `repo-skill-integrator` 合成目标仓库版本。

同步后进入目标仓库运行：

```bash
python3 scripts/validate_skills.py
```

## 校验

```bash
python3 scripts/validate_skills.py
find .agents/skills -mindepth 1 -maxdepth 1 -type d ! -name references -exec python3 /home/xxs/.codex/skills/.system/skill-creator/scripts/quick_validate.py {} \;
```
