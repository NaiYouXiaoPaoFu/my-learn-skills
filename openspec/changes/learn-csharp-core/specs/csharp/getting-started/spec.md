## Purpose

让零基础学习者装好 .NET SDK、用 dotnet CLI 创建并运行第一个控制台程序，建立"编写 → 运行 → 看输出"的最小闭环。

## ADDED Requirements

### Requirement: 环境安装与验证

学习者在指导下安装 .NET SDK（Windows），并通过 `dotnet --version` 验证安装成功。

#### Scenario: 安装后验证

- **WHEN** 学习者执行 `dotnet --version`
- **THEN** 输出 SDK 版本号，且能说明 .NET 运行时与 SDK 的关系（SDK 含编译器与运行时，发布运行只需运行时）

### Requirement: 创建并运行控制台程序

学习者用 `dotnet new console` 创建项目、`dotnet run` 运行，并理解 Program.cs 与 Main 入口的作用。

#### Scenario: Hello World

- **WHEN** 学习者新建 console 项目、修改 Program.cs 输出自定义文本并 `dotnet run`
- **THEN** 终端打印出修改后的文本，且学习者能指出 `Console.WriteLine` 的作用与字符串字面量的写法

### Requirement: 输出与编译运行流程

学习者能区分"编译"与"运行"，知道代码修改后需重新编译/运行才生效。

#### Scenario: 修改后重跑

- **WHEN** 学习者修改输出文本后再次运行
- **THEN** 输出反映最新修改，学习者能说出"先编译后运行"的流程（`dotnet build` / `dotnet run` 隐含编译）
