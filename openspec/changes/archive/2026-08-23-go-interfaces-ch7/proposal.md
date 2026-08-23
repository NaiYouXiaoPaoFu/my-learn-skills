## Why

用户已完成第 6 章方法学习，下一步指定《Go 语言圣经》第 7 章“接口”。现有学习记录显示接口方法集仅达到 level 2、confidence 0.65，且明确需要继续巩固 `nil` 接口、类型断言、接口嵌套与组合；现在需要把第 7 章组织成一条可恢复、可检验的主线，而不是一次性浏览术语。

## What Changes

- 建立 Go 接口章节的分阶段学习方案，先衔接方法集、静态类型/动态类型/动态值，再进入接口的合约与隐式实现。
- 学习如何从调用方需求设计小接口，并用 `io.Writer`、`fmt.Stringer`、`sort.Interface`、`http.Handler` 等标准库场景理解可替换性。
- 学习接口值的类型和值、`nil` 接口与携带 `nil` 指针的区别，以及接口组合和嵌套。
- 学习接口断言、类型开关和 `any` 的适用边界，区分普通接口值与泛型约束；泛型基础不重复展开。
- 每个阶段加入短 checkpoint，章节末用综合题验证方法集、接口值、实现关系、类型断言和工程取舍之间的连接。
- 仅在综合 checkpoint 通过或用户明确确认后，回写长期学习状态；未稳定结论保留为待复习项。

## Capabilities

### New Capabilities

- `go-interface-contracts`: 用最小方法集合表达行为合约，并判断具体类型是否隐式满足接口。
- `go-interface-values`: 解释接口值的静态类型、动态类型、动态值，以及 `nil` 边界和方法集规则。
- `go-interface-composition`: 使用接口嵌套、组合和标准库接口完成可替换设计。
- `go-interface-type-inspection`: 使用安全的类型断言和类型开关处理接口中的不同具体类型，并理解 `any` 的边界。

### Modified Capabilities

- 无

## Impact

- 学习过程文件：`openspec/changes/go-interfaces-ch7/` 下的 proposal、design、specs 和 tasks。
- 长期状态：`.learning/learning-state.sqlite3` 中新增或更新 Go 接口主题、阶段 checkpoint、来源和知识状态；只有通过检验的结论才会升级。
- 学习总结：若章节结论稳定，新增 `docs/learning/go-interfaces/summary.md`；本轮不修改 Go 代码仓库，也不引入运行时依赖。
- 外部资料：用户指定的《Go 语言圣经》第 7 章与 Go 官方规范、Effective Go、官方 Tour；教学回答中保留实际使用的链接。
\n+## Approval
\n+用户已明确批准本方案，进入正式教学阶段。
