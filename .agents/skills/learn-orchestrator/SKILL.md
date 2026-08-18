---
name: learn-orchestrator
description: "学习技能编排与路由。Use when the user asks to 学习项目、拆解仓库、粘贴 issue/PR、安排资料驱动教学、组装 skills、安排学习路线、决定先用哪个 skill，或进行自适应模拟面试。Actions: route, orchestrate, plan, compose, sequence, split learning workflow, interview."
---

# Learn Orchestrator

IRON LAW: 只编排，不代替子 skill 做教学、Review、实现、面试或文档回写。

## 职责

把用户的学习请求拆成最小、可组合的 skill 顺序，并明确输入、输出和停止条件；具体知识教学由子 skill 完成。

## 工作流

- [ ] Step 1: 判断请求类型：
  - issue/PR/link/review comments -> `issue-pr-intake`
  - 项目/模块学习 -> `learn-context` -> `project-deep-dive`
  - 代码链路 -> `learn-context` -> `code-path-tracer`
  - 概念讲解或知识缺口 -> `source-researcher` -> `adaptive-tutor` -> `concept-teacher`
  - 架构/设计取舍 -> `learn-context` -> `architecture-lens`
  - 代码/方案审核 -> `learn-context` -> `review-coach`
  - 模拟面试/拷打 -> `learn-context`（如有项目）-> `source-researcher`（如需面经）-> `interview-simulator`
  - 讲后确认 -> `learning-checkpoint`
  - 稳定结论或面试复盘 -> `learning-note-writer`
- [ ] Step 2: 读取 `.agents/skills/references/composition-recipes.md`，并读取 SQLite 当前学习状态。
- [ ] Step 3: 对概念缺口先输出 OpenSpec 风格的 Goal / Scope / Non-goals / Evidence / Stop condition，再开始教学。
- [ ] Step 4: 输出当前阶段的最小 skill 流程和每步输入/输出；不超过 5 个 skill，超出则分阶段。
- [ ] Step 5: 主线完成检验前，相关拓展只登记为后续候选，不切换主目标。

## 输出格式

- `目标：` 本轮可验证能力
- `Skill Chain：` 实际顺序
- `Current Stage：` 当前 skill
- `每步输入/输出：` 精简说明
- `Stop Condition：` checkpoint、面试结束复盘、稳定回写或阻塞问题

## 反模式

- 不把所有学习任务塞进一个大回答。
- 不跳过资料查证、计划或 checkpoint。
- 不把相关拓展当作主线，不默认用户掌握前置知识。
- 不让 Review 或面试 skill 代替教学。
- 不把一次性讨论直接沉淀成长期规则。
