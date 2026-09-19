## Purpose

让零基础学习者掌握 C# 条件分支与循环结构，能根据条件与重复需求选择正确的控制流并理解其执行顺序。

## ADDED Requirements

### Requirement: 条件分支

学习者能用 if/else if/else 与 switch 实现多分支逻辑，理解条件表达式求值为 bool。

#### Scenario: 多分支判断

- **WHEN** 输入分数需要分为优/良/及格/不及格四档
- **THEN** 学习者用 if/else if/else 或 switch 实现，能解释分支的执行顺序与首个匹配分支生效的规则

### Requirement: 循环结构

学习者能区分 for、while、do-while、foreach 的适用场景，正确使用 break/continue。

#### Scenario: 计数循环

- **WHEN** 需要打印 1 到 N 的平方
- **THEN** 学习者用 for 循环实现，能说出循环三要素（初始化、条件、步进）各起什么作用

#### Scenario: 条件循环

- **WHEN** 需要持续读取输入直到用户输入特定值（如 "quit"）
- **THEN** 学习者用 while 或 do-while 实现，并能解释两者先判断后执行与先执行后判断的区别

#### Scenario: 提前跳出

- **WHEN** 循环内满足特定条件需要停止整个循环或跳过本次迭代
- **THEN** 学习者正确使用 break（退出循环）与 continue（跳过本次），且能说出两者差异

### Requirement: 死循环识别

学习者能识别死循环并解释原因与规避方式。

#### Scenario: 条件永不变化

- **WHEN** while 循环条件依赖的变量在循环体内从未改变
- **THEN** 学习者指出这是死循环，说明变量更新或退出条件缺失是根因
