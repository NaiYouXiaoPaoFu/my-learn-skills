## Purpose

让零基础学习者掌握数组与 List<T> 的声明、访问与遍历，理解集合长度可变与固定的差异，能处理简单字符串数据。

## ADDED Requirements

### Requirement: 数组与索引

学习者能声明数组、通过索引读写元素，理解索引从 0 开始与越界风险。

#### Scenario: 索引越界

- **WHEN** 访问索引等于数组长度的元素
- **THEN** 运行时报 IndexOutOfRangeException，学习者能解释索引范围 [0, Length-1] 并修复

### Requirement: List<T> 与动态长度

学习者能用 List<T> 增删元素，理解其长度可变的优势。

#### Scenario: 动态收集

- **WHEN** 需要不断往集合添加数据直到某个条件结束
- **THEN** 学习者用 List<T> 与 Add 实现，能说出数组（定长）与 List（变长）的适用差异

### Requirement: foreach 遍历

学习者用 foreach 遍历数组/List 并理解其只读、顺序访问的特性。

#### Scenario: 遍历求和

- **WHEN** 需要计算集合元素之和
- **THEN** 学习者用 foreach 遍历累加，能说出 foreach 与 for 下标遍历的差异及各自适用场景

### Requirement: 字符串处理基础

学习者能使用常用字符串方法（Length、Contains、Split、Trim 等）完成简单文本处理。

#### Scenario: 分割输入

- **WHEN** 用户输入用逗号分隔的一串数字
- **THEN** 学习者用 Split 拆分成数组、Trim 清理空白并转换为数字，完成简单解析
