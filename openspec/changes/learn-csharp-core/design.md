# C# 语言核心教学方案 — Design

## Context

- 用户零基础、未选应用方向，确认「先定目标再选资料」。SQLite 中无任何 C# 学习记录，无 active change（首次学习）。
- 已确认的学习偏好：不预设固定路线（由目标驱动）、不默认掌握任何前置知识、优先官方权威资料、混合教学格式（讲解/类比/图示/对比/最小代码/实验/检验）、可给示例代码但默认不直接给最终实现、面试式严格追问后复盘。
- 机器：Windows 11，可用 Visual Studio Code + .NET SDK（需安装）。

## Goals / Non-Goals

**Goals:**
- 建立零基础可执行的 7 小节 + 综合考核的 C#/.NET 语言核心教学主线，每节可独立检验。
- 全程资料驱动：每节教学前 `source-researcher` 核对 Microsoft Learn 官方模块链接（版本相关，避免凭记忆）。
- 结束时学习者能独立完成"编写 → 运行 → 调试"控制台程序闭环，目标等级 2-3。

**Non-Goals:**
- 不锁定应用方向（后端/Unity/桌面均非本轮主线）。
- 不覆盖继承/接口/多态、LINQ、async/await、泛型高级、数据库等（登记为下一阶段候选）。
- 不做代码实现（本仓库是学习仓库，教学产出是学习状态与笔记，不写业务代码）。

## Decisions

### 1. 主线定为「C#/.NET 语言核心」
零基础且未选方向时，语言核心是所有后续方向（后端/Unity/桌面）的公共底子。相比直接选 ASP.NET Core 或 Unity，语言核心不依赖领域知识，可验证性最强（控制台程序即可检验）。替代方案（直接教后端/游戏）因目标未定而排除。

### 2. 资料主线：Microsoft Learn「Get started with C#」官方路径
已核对官方链接：
- Part 1 编写第一个 C# 程序：https://learn.microsoft.com/en-us/training/paths/get-started-c-sharp-part-1/
- Part 2 创建并运行控制台程序（含 VS Code 环境配置）：https://learn.microsoft.com/en-us/training/paths/get-started-c-sharp-part-2/
- Part 3 为控制台程序添加逻辑：https://learn.microsoft.com/en-us/training/paths/get-started-c-sharp-part-3/
- Part 6 调试控制台程序（异常与调试）：https://learn.microsoft.com/en-us/training/paths/get-started-c-sharp-part-6/
- 中文 C# 文档入口（A tour of C#）：https://learn.microsoft.com/zh-cn/dotnet/csharp/tour-of-csharp/
- .NET 官方学习入口：https://dotnet.microsoft.com/en-us/learn/csharp

Part 4/5（数据、构建应用）与语言核心章节映射在对应小节教学前再次核对链接。每节教学给出具体模块链接，不用"参考官方文档"笼统带过。

### 3. 章节顺序按"最小可运行闭环"推进
环境与 Hello World → 值/类型 → 控制流 → 方法 → 类 → 集合 → 异常与调试。每个概念都立刻放进可运行的控制台程序里验证，避免纯语法灌输。

### 4. 教学法：最小示例 → 类比/图示 → 用户先写 → 我 review
符合 code_boundary 偏好：提供帮助理解的示例代码，但练习由用户先写，我 review 后给反馈；不直接交付最终实现。

### 5. Checkpoint 分层
小节 checkpoint 只验本节（题目或最小实操）；综合考核跨 Scope 设计（小项目：如"成绩统计 + 温度换算 + 简单记账"），覆盖类型、控制流、方法、类、集合、异常六块。综合考核通过前不视为完成、不写长期笔记。

### 6. 环境搭建是第 0 步实操
零基础最常见首个卡点是 SDK 安装与编辑器配置。正式教学第一件事：装 .NET SDK → `dotnet --version` → VS Code 装 C# 扩展 → 跑通 Hello World。

### 7. 状态与回写
OpenSpec 承载过程状态（当前小节、checkpoint、审核状态）；SQLite 承载长期状态（topic、level、confidence、misconception）。每节 checkpoint 后立即更新阶段证据；综合考核通过并经用户确认后才 `learning-note-writer` 回写 `docs/learning/` 并更新 SQLite。

## Risks / Trade-offs

- **环境安装失败风险**（防火墙、磁盘权限、SDK 版本）：预案为官方安装器 + 手动检查 `dotnet --version`；VS Code 扩展安装失败时降级用 `dotnet run` 命令行演示（内容不变，体验略降）。
- **零基础抽象概念理解风险**（值/引用、对象、编译 vs 运行）：用类比（模板/实例、类型=容器规格、编译=翻译）与图示 + 最小实验对冲；连续两轮 checkpoint 不稳则回退到更小概念补课。
- **中文资料与官方英文模块混杂**：官方链接以英文路径为准（版本最新），讲解用中文；名词首次出现给中英对照，避免工具界面与术语断层。
- **语言版本差异（C# 9-13 特性）**：教学以 LTS 稳定特性为准（.NET 8/9 的默认模板 `Top-level statements` 等），教学前核对目标版本行为，不教非 LTS 实验特性。
