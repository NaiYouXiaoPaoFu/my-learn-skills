## Purpose

让零基础学习者掌握 try/catch/finally 异常处理与调试器基本操作，能主动捕获运行时错误并用断点、单步定位 bug。

## ADDED Requirements

### Requirement: 异常捕获

学习者用 try/catch/finally 处理可能失败的代码，理解各块执行时机。

#### Scenario: 非法输入

- **WHEN** 用户输入无法转换为数字导致 FormatException
- **THEN** 学习者用 try/catch 捕获并给出友好提示而非程序崩溃，能说出 catch 后程序继续执行、finally 无论是否异常都执行

### Requirement: 异常类型与抛出

学习者能区分常见异常类型（FormatException、IndexOutOfRangeException、DivideByZeroException、NullReferenceException），并能用 throw 主动抛异常。

#### Scenario: 主动校验

- **WHEN** 方法收到非法参数（如负数分数）
- **THEN** 学习者用 throw new ArgumentException(...) 主动拒绝，并说明主动抛 vs 静默错误的取舍

### Requirement: 调试器基本使用

学习者能在 IDE（VS Code）中设置断点、单步执行并观察变量值，用调试器而非 print 定位问题。

#### Scenario: 断点定位

- **WHEN** 程序结果不符合预期但无明显报错
- **THEN** 学习者打断点、单步（Step Over/Into）、查看变量面板，指出出错的语句与变量值
