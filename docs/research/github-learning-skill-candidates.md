# GitHub 学习型 Skill 候选记录

本文件记录外部候选的可借鉴点，不代表直接采用。

## 当前结论

- 没找到完全等价于“真实项目拆解 -> 场景化概念教学 -> 检验 -> 文档回写”的现成 skill 包。
- 值得借鉴的是模式，不是直接复制目录。
- 本仓库采用小 skill 编排，而不是单个万能导师 skill。

## 候选模式

### addyosmani/agent-skills

- 来源：https://github.com/addyosmani/agent-skills
- 可借鉴点：按工程阶段拆成多个 workflow skills，并用 meta-skill 做发现和调用。
- 适合吸收：`learn-orchestrator` 只做路由，子 skill 保持单职责；共享 references 统一放在根级 reference 区。
- 不直接采用：它偏生产级工程流程，本仓库偏个人学习闭环。

### GitHub Agent Skills 文档

- 来源：https://docs.github.com/en/copilot/how-tos/agents/copilot-coding-agent/extending-copilot-coding-agent-with-skills
- 可借鉴点：项目级 skill 可放在 `.agents/skills`，每个 skill 一个目录和一个 `SKILL.md`。
- 适合吸收：本仓库直接使用 `.agents/skills/<skill-name>/SKILL.md` 结构。
- 不直接采用：文档只规定形态，不提供学习型流程。

### Awesome Claude Skills / Everything Claude Code 类索引

- 来源：https://github.com/piebald-ai/awesome-claude-skills
- 来源：https://github.com/hesreallyhim/awesome-claude-code
- 可借鉴点：持续发现社区 skills、hooks、agents、commands 和 workflow 组合方式。
- 适合吸收：后续维护候选库。
- 不直接采用：索引范围过宽，需要二次筛选。

### awesome-claude-code-workflows

- 来源：https://github.com/ithiria894/awesome-claude-code-workflows
- 可借鉴点：把 hooks、MCP、skills、agents 和项目规则组合成 workflow recipes。
- 适合吸收：后续进入多 agent / webhook 阶段时参考组合形态。
- 不直接采用：当前版本先做 skill 编排，不引入执行自动化。

## 下一步筛选标准

- 是否支持按真实代码链路学习。
- 是否能把知识点回收到项目场景。
- 是否有理解检验，而不是只生成解释。
- 是否能分层回写稳定结论。
- 是否保持单职责，可被 orchestrator 组合。
