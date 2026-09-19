# C# 语言核心教学 — Tasks

> 状态约定：`[ ]` 待做，`[x]` 已完成。每个小节 = 教学 → 用户实操 → 小节 checkpoint → 记录证据。综合考核通过前不视为完成。

## 1. 环境与第一个程序

- [ ] 1.1 教学：.NET 是什么、C# 与 .NET 关系、SDK vs 运行时（配 Microsoft Learn Part 1/2 链接）
- [ ] 1.2 实操：安装 .NET SDK，`dotnet --version` 验证；VS Code 安装 C# 扩展
- [ ] 1.3 实操：`dotnet new console` 创建项目，修改 Program.cs 输出自定义文本，`dotnet run` 运行
- [ ] 1.4 小节 checkpoint：说出编译 vs 运行的流程；修改后重跑程序看到新输出

## 2. 值与类型

- [ ] 2.1 教学：变量/常量、int/double/bool/char/string、var 推断（配官方模块链接）
- [ ] 2.2 教学：隐式 vs 显式转换、精度丢失、常见类型错误
- [ ] 2.3 实操：用户先写一个"声明多类型变量并打印"的小程序，我 review
- [ ] 2.4 小节 checkpoint：类型不匹配错误修复 + 转换精度丢失解释

## 3. 控制流

- [ ] 3.1 教学：if/else if/else、switch、比较与逻辑运算符
- [ ] 3.2 教学：for/while/do-while/foreach、break/continue、死循环识别
- [ ] 3.3 实操：用户先写"分数分档 + 求和循环"小程序，我 review
- [ ] 3.4 小节 checkpoint：多分支逻辑正确性 + break/continue 差异口头说明

## 4. 方法与作用域

- [ ] 4.1 教学：方法定义/调用、形参实参、返回值、可选/命名参数
- [ ] 4.2 教学：作用域与变量遮蔽
- [ ] 4.3 实操：用户先写"带参数和返回值的方法 + 复用"小程序，我 review
- [ ] 4.4 小节 checkpoint：方法拆分正确 + 作用域错误预判

## 5. 类与对象基础

- [ ] 5.1 教学：class 是模板、new 创建实例、字段/属性/构造器/静态成员
- [ ] 5.2 实操：用户先写"Student 类（姓名+分数）+ 构造器初始化"小程序，我 review
- [ ] 5.3 小节 checkpoint：实例 vs 类成员访问差异 + 构造器作用解释

## 6. 数组与集合

- [ ] 6.1 教学：数组声明/索引/越界、List<T> 增删、foreach、常用字符串方法
- [ ] 6.2 实操：用户先写"逗号分隔数字解析 + 求和"小程序，我 review
- [ ] 6.3 小节 checkpoint：越界异常解释 + 数组 vs List 适用差异

## 7. 异常与调试

- [ ] 7.1 教学：try/catch/finally 执行时机、常见异常类型、throw 主动抛错
- [ ] 7.2 教学：VS Code 断点、单步、变量面板（配 Part 6 调试模块链接）
- [ ] 7.3 实操：用户先写"非法输入捕获 + 断点定位 bug"小程序，我 review
- [ ] 7.4 小节 checkpoint：非法输入不崩溃 + 用调试器定位一处逻辑错误

## 8. 综合考核（跨章）

- [ ] 8.1 设计并实现一个小项目（如成绩统计 + 温度换算 + 简单记账），要求覆盖：类型、控制流、方法、类、集合、异常六块
- [ ] 8.2 综合考核点评：边界（越界/非法输入）、取舍（数组 vs List、static vs 实例）、调试能力
- [ ] 8.3 评估掌握等级（目标 2-3）；不稳项回退补课，连续两轮不稳则缩小范围重教

## 9. 回写

- [ ] 9.1 经用户确认后 `learning-note-writer` 回写 `docs/learning/csharp-core.md`（含官方链接）
- [ ] 9.2 更新 SQLite：learning_topics、knowledge_states、checkpoints、source_references、misconceptions
- [ ] 9.3 用户确认后归档本 change；未确认不自动 archive
