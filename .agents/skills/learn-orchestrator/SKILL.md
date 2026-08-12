---
name: learn-orchestrator
description: "学习技能编排与路由。Use when the user asks to 学习一个项目、拆解仓库、粘贴 issue/PR、安装或合并学习 skills、组装 skills、安排学习路线、决定先用哪个 skill、把代码库学习拆成阶段、从业务链路回到知识点。Actions: route, orchestrate, plan, compose, sequence, split learning workflow."
---

# Learn Orchestrator

IRON LAW: 只编排，不代替子 skill 做教学、Review、实现或文档回写。

## 职责

把用户的学习请求拆成一组可组合的原子 skill 调用顺序，并说明每一步的输入、输出和停止条件。

## 工作流

- [ ] Step 1: 判断请求类型
  - 粘贴 issue/PR/link/review comments -> `issue-pr-intake`
  - 安装/合并到已有仓库 -> `repo-skill-integrator`
  - 项目/模块学习 -> `learn-context` -> `project-deep-dive`
  - 代码链路理解 -> `learn-context` -> `code-path-tracer`
  - 概念讲解 -> `source-researcher` -> `concept-teacher`
  - 架构/设计取舍 -> `learn-context` -> `architecture-lens`
  - 代码/方案审核 -> `learn-context` -> `review-coach`
  - 讲后确认 -> `learning-checkpoint`
  - 稳定结论沉淀 -> `learning-note-writer`
- [ ] Step 2: 读取 `.agents/skills/references/composition-recipes.md`
- [ ] Step 3: 输出一个最小 skill 流程
- [ ] Step 4: 标明每个 skill 只需要读哪些上下文
- [ ] Step 5: 如果流程超过 5 步，拆成阶段，不一次执行完

## 输出格式

- 目标：这轮学习要达成什么。
- Skill 顺序：按执行顺序列出，不超过当前阶段需要的步骤。
- 每步输入：代码、文档、issue、用户问题或外部资料。
- 每步输出：链路图、概念卡、检查题、Review 结论或回写草稿。
- 停止条件：用户完成检验、问题进入 Review、或结论需要回写。

## 反模式

- 不要把所有学习任务塞进一个大回答。
- 不要跳过上下文装载直接讲抽象概念。
- 不要在 issue/PR 已经给出精准上下文时重新扫全仓库。
- 不要让 Review skill 代替教学主链路。
- 不要把一次性讨论直接沉淀成长期规则。
