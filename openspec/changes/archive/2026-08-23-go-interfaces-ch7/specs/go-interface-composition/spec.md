## ADDED Requirements

### Requirement: 接口组合与标准库适配

教学方案 MUST 让学习者能使用接口嵌套/组合表达复合行为，并把标准库接口用于不同具体实现之间的替换。

#### Scenario: 组合接口
- **WHEN** 一个新接口嵌入两个已有接口
- **THEN** 学习者能列出新接口所需的完整方法集合，并判断一个具体类型是否满足全部方法

#### Scenario: HTTP handler 适配
- **WHEN** 一个 HTTP 组件需要 `ServeHTTP(http.ResponseWriter, *http.Request)` 行为
- **THEN** 学习者能识别 `http.Handler` 是行为合约，并区分满足接口的具体 handler 与 handler 的内部实现

#### Scenario: 避免过度抽象
- **WHEN** 调用方只使用一个方法但候选接口还包含多个无关方法
- **THEN** 学习者能缩小调用方依赖的接口，而不是为了复用类型定义而接受大接口
