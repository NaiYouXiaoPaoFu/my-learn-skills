## ADDED Requirements

### Requirement: 接口合约与隐式实现

教学方案 MUST 让学习者能从调用方需要的行为定义最小接口，并根据方法签名和方法集判断具体类型是否隐式满足接口。

#### Scenario: 判断标准库接口实现
- **WHEN** 学习者看到 `io.Writer` 的 `Write([]byte) (int, error)` 约定以及一个具体类型的方法声明
- **THEN** 学习者能判断该类型是否可作为 `io.Writer` 传入，并说明 Go 不需要显式 implements 声明

#### Scenario: 选择最小接口
- **WHEN** 一个函数只需要调用 `Write` 而不需要文件、缓冲区或其他具体能力
- **THEN** 学习者能选择 `io.Writer` 而不是具体类型或包含无关方法的大接口，并解释可替换性
