## Purpose

掌握 GDScript 集合与引用语义，使学习者能为游戏状态选择合适的数据结构，并避免隐式共享导致的错误。

## ADDED Requirements

### Requirement: 学习者能操作集合

学习者 MUST 能使用 Array、Dictionary、字符串和向量，完成创建、索引、遍历、增删改、查找与基本转换；能区分 typed 与 untyped collection 的约束。

#### Scenario: 建模收集物状态
- **WHEN** 游戏需要保存多个物品及其数量
- **THEN** 学习者能解释选择 Array 或 Dictionary 的理由，并实现读写和遍历

### Requirement: 学习者能解释值与引用

学习者 MUST 能预测赋值、函数传参、浅复制和修改嵌套数据时的别名行为。

#### Scenario: 修复共享状态污染
- **WHEN** 修改一个对象后另一个变量的集合也变化
- **THEN** 学习者能定位共享引用并选择合适的复制或数据设计
