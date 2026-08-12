---
name: learn-context
description: "学习任务上下文装载。Use when the user asks to 先看项目、加载 issue/PR、理解仓库、找相关文档、进入某个模块学习、开始代码链路分析、开始 Review 前收集证据。Actions: gather, load, inspect, collect context, find docs, find code, prepare learning context."
---

# Learn Context

IRON LAW: 只收集最小必要上下文，不提前教学、不提前下结论。

## 职责

为后续 skill 提供干净、可验证、低噪音的输入。

## 工作流

- [ ] Step 1: 确认学习对象：仓库、模块、issue、PR、文件、函数或概念
- [ ] Step 2: 如果输入来自 issue/PR，先读取 `issue-pr-intake` 的上下文包
- [ ] Step 3: 读取索引文件：README、docs、AGENTS、OpenSpec、issue 或任务说明
- [ ] Step 4: 只搜索 issue/PR、任务说明或用户问题点名的代码和测试
- [ ] Step 5: 输出上下文包，最多包含 5 类证据
- [ ] Step 6: 推荐下一步 skill，不直接执行它

## 输出格式

- 学习目标：
- 已读文档：
- 相关代码入口：
- 关键约束：
- 未确认问题：
- 推荐下一步：

## 反模式

- 不要扫完整仓库后输出长清单。
- 不要越过 issue/PR 上下文去加载无关知识。
- 不要把猜测写成事实。
- 不要把无关文件塞给后续 skill。
