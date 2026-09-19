## Purpose

掌握程序执行顺序和函数抽象，使学习者能把游戏规则拆成可调用、可验证的行为。

## ADDED Requirements

### Requirement: 学习者能控制执行流

学习者 MUST 能使用 `if/elif/else`、`for`、`while`、`match`、`break` 和 `continue`，并说明边界条件与可能的无限循环。

#### Scenario: 依据状态选择行为
- **WHEN** 角色状态或输入条件变化
- **THEN** 学习者能选择合适的分支或匹配结构，并预测每条路径

### Requirement: 学习者能设计函数接口

学习者 MUST 能定义带参数、默认值和返回类型的函数，理解局部作用域、返回值和副作用。

#### Scenario: 把重复规则提取为函数
- **WHEN** 收集物计分规则在两个位置重复
- **THEN** 学习者能提取函数并迁移调用方，行为保持一致
