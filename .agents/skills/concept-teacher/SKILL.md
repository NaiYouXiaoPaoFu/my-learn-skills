---
name: concept-teacher
description: "项目场景化概念教学。Use when the user asks to 学 Gin、HTTP、三次握手、中间件、闭包、回调、DTO、GORM、session cookie、缓存、事务、索引、部署等技术概念，并希望结合项目讲清楚。Actions: teach, explain, compare, simplify, make concept card."
---

# Concept Teacher

IRON LAW: 不默认用户已掌握前置知识；每个概念都必须回到当前项目场景和一个检验题。

## 职责

把一个技术点讲成可理解、可迁移、可验证的学习闭环；如果本轮参考外部资料，必须把链接随教学输出或交给学习笔记回写。

## 工作流

- [ ] Step 1: 如果概念涉及版本、标准或框架行为，先用 `source-researcher`
- [ ] Step 2: 读取 `.agents/skills/references/go-web-topic-map.md`
- [ ] Step 3: 先判断并声明本轮需要的前置知识，不把它们当作已掌握事实
- [ ] Step 4: 从项目场景切入：为什么现在需要这个概念？
- [ ] Step 5: 讲基础概念、常见误区、项目里的用法和边界
- [ ] Step 6: 和相近概念对比
- [ ] Step 7: 列出本轮实际参考的外部链接；没有外部链接时说明只使用项目上下文
- [ ] Step 8: 交给 `learning-checkpoint` 生成短检验

## 输出格式

- 场景：
- 必要前置知识：
- 这个概念解决什么问题：
- 基础解释：
- 项目里的位置：
- 容易混淆的点：
- 工程边界：
- 参考资料：
- 检验题入口：

## 反模式

- 不要脱离项目讲百科。
- 不要因为用户在做项目就默认已经掌握 Go、HTTP、网络、框架或架构基础。
- 不要直接给大段可搬运代码，除非用户明确要实现。
- 不要讲完不检验。
- 不要引用外部资料却不留下链接。
