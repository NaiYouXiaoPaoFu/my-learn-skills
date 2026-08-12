---
name: issue-pr-intake
description: "Issue/PR 精准上下文提取。Use when the user pastes GitHub issue, PR, issue link, PR link, task body, review comments, acceptance criteria, reproduction steps, labels, or checklist and wants learning, implementation, review, or context loading. Actions: extract context, classify granularity, identify files, build skill chain."
---

# Issue PR Intake

IRON LAW: issue/PR 是内部精准上下文源；默认消化给后续 skill，不把正文或完整 Context Pack 复述给用户。

## 职责

把用户粘贴的 issue、PR、评论或链接整理成后续 skill 能直接消费的内部最小上下文包。

## 工作流

- [ ] Step 1: 判断输入类型：issue、PR、评论串、diff 摘要、验收标准或链接
- [ ] Step 2: 读取 `.agents/skills/references/issue-pr-workflow.md`
- [ ] Step 3: 提取问题边界、目标、非目标、任务树、验收标准和相关文件
- [ ] Step 4: 判断粒度：强粒度、正常粒度、过粗、过碎
- [ ] Step 5: 只保留当前任务必需的知识点和代码入口
- [ ] Step 6: 内部保留 `Issue/PR Context Pack`，只向用户输出执行摘要和推荐 `Skill Chain`

## 输出格式

默认只输出：

- Skill Chain：
- Current Stage：`issue-pr-intake`
- Stop Condition：
- 粒度判断：强粒度 / 正常粒度 / 过粗 / 过碎
- 下一步只加载：
- 本轮不加载：
- 未确认问题：

内部 Context Pack，不默认展示：

- 类型：issue / PR / review comments / link only / pasted excerpt
- 粒度判断：强粒度 / 正常粒度 / 过粗 / 过碎
- 当前目标：
- 非目标：
- 关键上下文：
- 相关文件或入口：
- 必要知识点：
- 验收标准：
- 未确认问题：
- 推荐 Skill Chain：
- Stop Condition：

## 反模式

- 不要因为看到 issue 链接就扫描全仓库。
- 不要把 issue 里没提到的技术点扩展成学习路线。
- 不要把 PR review 当成重新设计整个功能。
- 不要在只有链接且无法访问时猜内容；要求用户粘贴正文或评论。
