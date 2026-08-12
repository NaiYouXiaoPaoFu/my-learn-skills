---
name: project-deep-dive
description: "项目学习切片拆解。Use when the user asks to 拆解项目、拆解模块、制定学习路线、从业务功能提炼知识点、把仓库拆成学习 issue、分析优雅架构和代码设计。Actions: decompose project, slice module, map learning topics, create learning backlog."
---

# Project Deep Dive

IRON LAW: 只拆学习切片，不直接讲完整课程，也不替用户实现代码。

## 职责

把真实项目或模块拆成可学习、可验证、可组合的小切片。

## 工作流

- [ ] Step 1: 先读取 `learn-context` 产出的上下文包
- [ ] Step 2: 读取 `.agents/skills/references/learning-system-gate.md`
- [ ] Step 3: 找出业务链路：入口、核心操作、数据流、失败分支、验证方式
- [ ] Step 4: 把链路拆成 3 到 7 个学习切片
- [ ] Step 5: 每个切片绑定一个主知识点和一个最小验证
- [ ] Step 6: 标出后续应调用的 skill

## 输出格式

- 切片名：
- 服务的业务链路：
- 主知识点：
- 相关文件：
- 应理解的设计点：
- 最小实操或检验：
- 推荐下一步 skill：

## 反模式

- 不要把 HTTP、Gin、GORM、部署等纯技术点机械拆成孤立课程。
- 不要让一个切片覆盖多个互不依赖的主题。
- 不要没有验证方式就输出学习路线。
