# Go 接口学习总结

## 学习范围

本阶段围绕《Go 语言圣经》第 7 章接口，学习接口合约、隐式实现、方法集、接口值、`nil` 边界、接口组合、标准库适配、类型断言、类型开关，以及普通接口与泛型约束的边界。

非目标：反射、`unsafe`、接口运行时内部布局、性能基准、泛型基础语法和完整标准库接口清单。

## 1. 接口是行为合约

接口描述调用方需要的行为，不描述具体实现：

```go
type Writer interface {
    Write([]byte) (int, error)
}
```

Go 通过方法集隐式实现接口，不需要显式 `implements` 声明。只要具体类型的方法签名满足接口，就能作为该接口使用。

接口通常应由消费者根据实际调用需求定义，并尽量只保留最小方法集合。函数只需要写入能力时，应依赖 `io.Writer`，而不是 `*os.File` 或包含无关方法的大接口。

参考：[Go 语言圣经 7.1：接口是合约](https://gopl-zh.github.io/ch7/ch7-01.html)、[Effective Go：Interfaces](https://go.dev/doc/effective_go#interfaces)。

## 2. 方法集决定接口赋值

值接收器方法同时出现在值类型和对应指针类型的方法集中：

```go
func (Job) Run() {}
```

因此 `Job` 和 `*Job` 都可能满足只要求 `Run()` 的接口。

指针接收器方法只出现在指针类型的方法集中：

```go
func (c *Counter) Write([]byte) (int, error) {}
```

因此 `Counter` 不满足只要求 `Write` 的接口，而 `*Counter` 满足。

可寻址变量的直接方法调用可能触发编译器自动取地址：

```go
job.Stop() // 可能按 (&job).Stop() 处理
```

但这不会修改方法集，也不会让接口传参自动取地址。接口赋值必须根据静态方法集判断。

参考：[Go 官方规范：Method sets](https://go.dev/ref/spec#Method_sets)。

## 3. 接口值与 nil

接口值需要区分：

```text
静态类型：变量声明时的接口类型
动态类型：接口当前保存的具体类型
动态值：接口当前保存的具体值
```

真正的 nil 接口：

```text
动态类型 = nil
动态值   = nil
接口 == nil 为 true
```

携带 nil 指针的接口：

```go
var p *Job = nil
var r Runner = p
```

此时：

```text
r 的静态类型：Runner
r 的动态类型：*Job
r 的动态值：nil
r == nil：false
```

类型断言 `r.(*Job)` 可以成功，但返回的 `*Job` 值仍然是 nil。接口不等于 nil 不能保证动态值非 nil，也不能保证调用方法安全；是否 panic 取决于方法体是否解引用 nil 接收器。

## 4. 接口组合与标准库适配

接口嵌入是方法要求的组合，不是继承，也不保存字段：

```go
type ReadWriter interface {
    io.Reader
    io.Writer
}
```

具体类型必须同时满足嵌入接口的全部方法。函数参数仍应使用实际需要的最小接口：只读就用 `io.Reader`，确实需要读写才用 `io.ReadWriter`。

`http.Handler` 通过 `ServeHTTP(http.ResponseWriter, *http.Request)` 表达 HTTP 处理行为。任意拥有匹配方法的类型都能作为 handler 使用，调用方不依赖其内部实现。

## 5. 类型断言与类型开关

不确定接口动态类型时，优先使用双返回值断言：

```go
text, ok := value.(string)
```

断言失败时 `ok == false`，不会像单返回值断言那样直接 panic。断言目标也可以是接口，用于检查动态值是否具备某种额外行为：

```go
s, ok := value.(fmt.Stringer)
```

类型开关适合运行时混合多种类型，并且每种类型需要不同处理逻辑的场景。它会显式依赖处理的动态类型集合。

## 6. 普通接口、泛型与 any

选择依据：

```text
只需要某种行为，不需要保留具体类型：普通接口
编译期知道类型，并需要返回/继续使用 T：泛型
运行时才知道动态类型，且需要按类型分支：any + 类型断言/类型开关
```

例如只需要 `String()` 时，普通接口语义更直接：

```go
func Print(v fmt.Stringer) {
    fmt.Println(v.String())
}
```

如果需要返回调用者传入的原始具体类型，泛型可以保留 `T`：

```go
func LogAndKeep[T fmt.Stringer](v T) T {
    fmt.Println(v.String())
    return v
}
```

`any` 不是“可以直接执行任意操作”；它只是允许保存任意类型，具体操作仍需类型断言、类型开关或更准确的泛型约束。

本阶段特别纠正：不能笼统地说“需要具体类型就使用 any + 类型断言”。如果具体类型在编译期已知且需要保留，应优先考虑泛型；只有运行时动态类型检查才使用 `any` 和类型断言。

## 检验结果与掌握程度

用户通过了：

- 接口合约、隐式实现和最小接口 checkpoint；
- nil 接口与携带 nil 指针 checkpoint；
- 接口组合、`http.Handler` 和最小接口 checkpoint；
- 类型断言、类型开关、`any` 与泛型边界 checkpoint；
- 章节综合 checkpoint。

综合证据：用户能判断值/指针方法集、接口赋值、nil 接口、动态类型/动态值、接口组合和类型断言，并能根据具体场景选择普通接口、泛型或 `any` + 类型开关。

掌握程度：**level 4/6：能解释取舍和边界。**

尚未评为 level 5 或 6：尚未通过真实项目代码中的独立接口设计、排错和跨模块迁移验证。

## 仍需复习

- 继续强化“直接方法调用的自动取地址”与“接口赋值不自动取地址”的区别。
- 保持谨慎：不能无场景地断言泛型一定带来更多或更少运行时开销；本章主要依据语义需求选择抽象，不以未经基准验证的性能判断作为结论。
- 后续可在真实 Gin handler/service 或 repository 场景中验证消费者定义小接口的边界。

## 参考资料

- [Go 语言圣经第 7 章：接口](https://gopl-zh.github.io/ch7/ch7.html)
- [Go 语言圣经 7.1：接口是合约](https://gopl-zh.github.io/ch7/ch7-01.html)
- [Go 官方规范：Interface types](https://go.dev/ref/spec#Interface_types)
- [Go 官方规范：Method sets](https://go.dev/ref/spec#Method_sets)
- [Effective Go：Interfaces](https://go.dev/doc/effective_go#interfaces)
