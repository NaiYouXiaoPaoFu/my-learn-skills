---
name: code-path-tracer
description: "代码执行链路追踪。Use when the user asks to 看懂一个接口、追请求链路、追数据流、handler service repository 怎么串起来、Gin 中间件执行顺序、HTTP 请求如何进入业务代码、定位某个功能入口。Actions: trace, follow call path, map data flow, explain execution path."
---

# Code Path Tracer

IRON LAW: 只追一条明确链路，不扩散成全项目讲解。

## 职责

把一个请求、命令、函数或页面动作的执行路径讲清楚。

## 工作流

- [ ] Step 1: 读取 `learn-context` 产出的入口文件和目标行为
- [ ] Step 2: 找入口：route、handler、command、component event 或 test
- [ ] Step 3: 逐层追踪：输入 -> 校验 -> 编排 -> 查询/写入 -> DTO/响应
- [ ] Step 4: 标出横切逻辑：middleware、auth、transaction、cache、error handling
- [ ] Step 5: 输出链路图和 1 到 3 个后续知识点
- [ ] Step 6: 如果出现架构边界问题，交给 `architecture-lens`

## 输出格式

- 入口：
- 调用顺序：
- 数据如何变化：
- 错误如何返回：
- 横切逻辑：
- 需要补的知识点：

## 反模式

- 不要用“这里大概会调用”代替实际文件证据。
- 不要同时追多条入口。
- 不要跳过错误分支和中间件。
