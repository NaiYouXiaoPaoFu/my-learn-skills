# Repository Agent Rules

本仓库用于个人学习型 skills 编排。所有 agent 进入本仓库后先遵守这里，再读取具体 skill。

## 硬规则

- 学习、拆解、教学、Review、issue/PR 接入类请求，必须先走 `learn-orchestrator` 或说明为什么只调用单个 skill。
- 用户粘贴 issue、PR、review comments 或链接时，先走 `issue-pr-intake`，把它当作内部精准上下文入口。
- 回答学习任务时必须显式输出 `Skill Chain`、`Current Stage` 和 `Stop Condition`，但不要复述完整 issue/PR 内容。
- 没有 `learning-checkpoint`，不把一次教学视为完成。
- 没有通过检验或形成稳定结论，不调用 `learning-note-writer` 回写长期文档。
- 不默认用户已经掌握未教学、未检验的前置知识。
- 面试式追问最多两轮；用户不会时先补课，不连续问同类问题。
- 教学时实际参考外部资料，必须在回答里给出链接，或在总结文档的对应知识点下写入链接。
- 把本 kit 接入已有仓库时，必须先用 `repo-skill-integrator` 扫描现有 `AGENTS.md` 和 skills，不直接覆盖。
- 强粒度 issue 不重新拆任务；只加载 issue 指向的必要代码、测试、文档和知识点。
- 正常粒度 issue 可以补少量子任务和风险，但不能重写整个 issue。
- 过粗 issue 先拆分；过碎 issue 先补业务场景和验收标准。

## 默认输出协议

```text
Skill Chain: <skill-a> -> <skill-b> -> <skill-c>
Current Stage: <current-skill>
Stop Condition: <checkpoint / review done / stable note / blocked question>
```

## Issue / PR 输入协议

如果用户只粘贴链接且无法访问，要求用户补充以下最小内容：

- 标题
- 正文或任务树
- 验收标准
- 关键评论或 review comments
- 已知相关文件、接口或模块

如果用户已经粘贴正文，不要再索要全量仓库背景，也不要把正文整理后重复输出给用户。

## 不要做

- 不要先扫全仓库再理解 issue。
- 不要默认展示完整 Context Pack；它是内部工作产物。
- 不要把技术点讲成脱离项目的百科。
- 不要跳过 checkpoint 直接给“已掌握”的结论。
- 不要还没教学就默认用户已掌握。
- 不要无限追问；两轮不稳就回到更小概念。
- 不要用“参考官方文档”代替具体链接。
- 不要用本仓库的规则覆盖目标仓库原有项目规则。
- 不要把临时 workaround 写入长期文档。
- 不要让 `review-coach` 代替教学主链路。
