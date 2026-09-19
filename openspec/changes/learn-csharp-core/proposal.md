# Learn C# Core — 教学方案

## Why

用户为零基础、未选具体应用方向，明确要求先定目标再选资料。需要一份可恢复、资料驱动、待审核的 C#/.NET 语言核心教学方案，避免凭记忆讲解或预设固定路线。

## What Changes

- 建立「C#/.NET 语言核心」主线教学方案，目标等级：零基础 → 可独立编写、运行、调试控制台程序（等级 2-3）。
- 以 Microsoft Learn 官方 Get started with C# 路径（Part 1-6）为教学主线，每节教学前由 `source-researcher` 核对具体模块链接（版本相关）。
- 分 7 个教学小节 + 1 个跨章综合考核，每节含小节 checkpoint；综合考核通过前不视为完成。
- 主线完成后回写长期学习笔记到 `docs/learning/` 并更新 SQLite 状态。

## Capabilities

### New Capabilities

- `csharp/getting-started`: 环境搭建与第一个控制台程序（.NET SDK、dotnet CLI、Hello World）
- `csharp/values-and-types`: 变量、内置类型、类型推断与转换
- `csharp/control-flow`: 条件分支与循环
- `csharp/methods`: 方法定义/调用、参数、返回值与作用域
- `csharp/classes-basics`: 类、字段/属性、构造器、对象与静态成员
- `csharp/arrays-collections`: 数组、List<T> 与 foreach 遍历
- `csharp/exceptions-debugging`: 异常处理与调试器基本使用

### Modified Capabilities

无（新仓库，无既有 spec）。

## 范围

**Goal（目标能力）：** 零基础者掌握 C#/.NET 语言核心，能独立完成"编写 → 运行 → 调试"控制台程序闭环：正确使用变量与类型、控制流、方法、类与对象、数组与集合、异常处理，并能用调试器定位常见错误。

**Scope（本轮讲授）：**

1. 环境与第一个程序：.NET SDK、dotnet CLI（`dotnet new console` / `dotnet run`）、Program.cs、`Console.WriteLine`、Main 入口
2. 值与类型：变量/常量、内置类型（int、double、bool、char、string）、`var`、类型转换
3. 控制流：if/else、switch、for、while、do-while、foreach、break/continue
4. 方法与作用域：定义/调用、参数、返回值、局部作用域
5. 类与对象基础：class、字段、属性、构造器、`new`、`this`、静态成员
6. 数组与集合基础：数组、`List<T>`、遍历、常用字符串处理
7. 异常与调试：try/catch/finally、常见异常类型、断点与单步调试

**Non-goals（本轮不讲，登记为后续候选）：**

- ASP.NET Core / Web 后端、Unity、桌面 UI（WinForms/WPF）——目标未定，不锁定方向
- 继承、接口、多态深挖——OOP 本轮只到 class 基础
- 泛型高级、LINQ 深入、async/await、委托/事件
- 内存管理/GC 深入、unsafe、反射/元编程
- 数据库、EF Core、依赖注入、测试框架

理由：零基础第一闭环以"可运行、可调试"为核心；每个被排除概念都回答不了"它如何帮助当前 Goal"，只登记为后续候选。

**Prerequisites：** 无编程前置知识（用户已确认零基础）；需要一台可安装 .NET SDK 的 Windows 机器与一个编辑器（VS Code 优先，免费轻量）。环境搭建本身是第 0 步实操教学内容。

## 审核状态

- 状态：**draft，待用户批准或修改**
- 未经用户明确批准，不开始正式教学、不推进 tasks、不调用 apply。
- 用户提出修改时更新本 proposal 与 design/tasks，保持未批准状态。
