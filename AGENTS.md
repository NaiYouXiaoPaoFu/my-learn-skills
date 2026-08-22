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

## 常见错误与操作门禁

- 不得重复输出同一条完整回答、教学内容、题目或总结；发送前检查标题、段落和代码块是否重复。
- 发生重复投递时，不得再次粘贴全文“修复”；只发送简短更正或新增内容。
- 章节或小节结束后，不得未经用户确认自动进入下一阶段；先完成当前总结和 checkpoint，再询问是否继续或是否有反问。
- 掌握程度评分必须由既定 skill 按职责负责；修改规则前先检查 skill chain 和职责边界，不把职责重复塞进其他 skill。
- 未经用户明确同意，不得执行 `git commit`、`git push` 或其他会改变版本历史/远程状态的操作；可以先修改工作区并报告待提交内容。
- 用户要求“提交”时，先确认提交范围；不得顺手纳入无关的已有修改、学习状态数据库或未请求的新文件。
- 用户指出重复错误时，先修正根因和对应规则，再继续主任务；不得只口头承诺而不更新适用的规则。

## OpenSpec 工作流门禁

- OpenSpec 已接入本仓库，负责跨消息恢复的当前工作流状态；SQLite 负责长期学习状态。两者不得重复承载同一字段。
- 每次学习请求开始前，先运行 `openspec list --json`；若有相关 active change，必须读取其 proposal/design/specs/tasks 后恢复，不得另起一套方案或凭当前对话猜阶段。
- 教学方案使用 OpenSpec change 持久化：`proposal.md` 记录目标、范围、非目标和审核状态；`design.md` 记录教学编排与取舍；`tasks.md` 记录小节、checkpoint、综合考核和回写步骤。
- 教学方案的 `proposal.md` 未获用户明确批准前，不得开始正式教学；用户提出修改时更新 artifacts，并保持未批准状态。
- OpenSpec 的 `apply` 在本仓库学习场景只推进教学任务和 checkpoint，不得把教学任务误当成代码实现；代码变更仍需遵守普通工程验证规则。
- 被用户插话、切换主题或中断后，先保存/更新当前 change 状态，再处理插话；插话结束后先恢复原 change 的下一项任务，不得丢失主线。
- `docs/learning/` 存放稳定学习总结，`.learning/learning-state.sqlite3` 存放长期状态；`openspec/changes/` 存放当前方案与进度，`openspec/changes/archive/` 存放已结束方案。
- 未经用户明确同意，不得自动 archive 教学 change、推进下一章节或把 draft 标记为 approved。

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

## 自适应教学与持久状态

- 当用户显露知识缺口时，先用 `source-researcher` 查官方或权威资料；不得按默认前置知识继续推进。
- 对单一概念、资料或项目切片，先用 `adaptive-tutor` 输出 Goal、Scope、Non-goals、Prerequisites、Stages、Evidence 和 Stop Condition，再进入教学。
- 相关概念只能在明确服务当前 Goal 时展开；否则登记为后续候选，主线完成或用户切换前不得继续扩展。
- 用 `.learning/learning-state.sqlite3` 持久记录主题、学习计划、来源、检验、误区、面试和稳定偏好；未通过检验或未经用户确认的结论不得写成掌握状态。
- 用户明确进入模拟面试时使用 `interview-simulator`。面试期间不教学、不提示；结束后必须复盘并写入数据库。`learning-checkpoint` 的两轮上限只适用于教学后的短检验，不限制独立模拟面试的计划范围。
- 不要让 `review-coach` 代替教学主链路。
