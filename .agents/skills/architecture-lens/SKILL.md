---
name: architecture-lens
description: "架构与代码设计分析。Use when the user asks to 分析优雅架构设计、代码设计、分层边界、handler service repository、DTO、模块职责、可维护性、耦合、抽象是否过度、为什么这样设计。Actions: analyze architecture, compare designs, explain tradeoffs, find boundary risks."
---

# Architecture Lens

IRON LAW: 先讲变化原因和边界，再评价架构好坏。

## 职责

分析一个模块、方案或链路的职责边界、取舍和长期维护风险。

## 工作流

- [ ] Step 1: 读取 `learn-context` 或 `code-path-tracer` 的结果
- [ ] Step 2: 读取 `.agents/skills/references/learning-system-gate.md`
- [ ] Step 3: 回答：这个模块有哪些变化原因？
- [ ] Step 4: 回答：哪些边界是业务、数据、协议、权限或横切逻辑？
- [ ] Step 5: 比较当前方案、简单替代方案、过度设计方案
- [ ] Step 6: 输出设计判断和需要交给 `concept-teacher` 的知识点

## 输出格式

- 设计问题：
- 当前边界：
- 变化原因：
- 当前方案优点：
- 当前方案风险：
- 替代方案：
- 推荐学习点：

## 反模式

- 不要一上来套 DDD、微服务、Clean Architecture 等大词。
- 不要只说“这样更优雅”，必须说明维护和验证收益。
- 不要把 DTO、实体、接口响应和数据库表混成一层。
