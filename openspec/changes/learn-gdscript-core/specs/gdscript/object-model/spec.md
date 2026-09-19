## Purpose

掌握 GDScript 的对象模型和可调用对象，使学习者能将数据与行为组织成可复用脚本，而不依赖全局变量堆叠。

## ADDED Requirements

### Requirement: 学习者能组织类与对象

学习者 MUST 能定义类、实例化对象、使用成员、构造函数、继承、覆盖、`super`、`class_name`、静态成员和内部类，并能比较继承与组合。

#### Scenario: 扩展不同类型的收集物
- **WHEN** 收集物共享位置和拾取接口但奖励规则不同
- **THEN** 学习者能选择继承或组合并说明依赖方向

### Requirement: 学习者能使用Callable与匿名函数

学习者 MUST 能理解 Callable、lambda、回调和方法引用在信号、排序或延迟行为中的作用。

#### Scenario: 延后执行一个行为
- **WHEN** 一个节点需要把行为交给另一个节点在未来调用
- **THEN** 学习者能传递可调用对象并说明其目标实例与生命周期风险
