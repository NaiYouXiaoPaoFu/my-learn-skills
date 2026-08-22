# Go 泛型学习总结

## 学习范围

本阶段围绕 Go 泛型基础、类型约束、类型集、泛型类型和泛型接口展开，资料来源包括用户指定文章与 Go 官方文档。

## 目录

1. [泛型解决的问题](#1-泛型解决的问题)
2. [泛型函数语法](#2-泛型函数语法)
3. [类型形参、类型实参和类型推断](#3-类型形参类型实参和类型推断)
4. [类型约束](#4-类型约束)
5. [`any`、`comparable` 和 `~`](#5-any-comparable-和-)
6. [泛型类型](#6-泛型类型)
7. [接口作为泛型约束](#7-接口作为泛型约束)
8. [泛型接口](#8-泛型接口)
9. [泛型接口实例化与实现接口的值](#9-泛型接口实例化与实现接口的值)
10. [接口变量、接口约束和类型集的区别](#10-接口变量接口约束和类型集的区别)
11. [泛型的工程边界](#11-泛型的工程边界)
12. [本阶段检验结论](#12-本阶段检验结论)
13. [参考资料](#13-参考资料)

---

## 1. 泛型解决的问题

泛型适合解决：**执行逻辑相同，但数据类型不同**的问题。

没有泛型时，可能需要重复编写：

```go
func SumInt(a, b int) int {
	return a + b
}

func SumFloat64(a, b float64) float64 {
	return a + b
}
```

使用泛型后可以合并为：

```go
func Sum[T int | float64](a, b T) T {
	return a + b
}
```

泛型相比 `any + reflect` 的主要价值：

- 保留编译期类型检查。
- 避免运行时反射和类型判断。
- 避免为相同逻辑重复编写多份代码。
- 返回值可以保留调用时的具体类型。

泛型不是为了让所有代码都抽象化，而是为了复用**类型不同、逻辑相同**的代码。

## 2. 泛型函数语法

```go
func Sum[T int | float64](a, b T) T {
	return a + b
}
```

拆解：

- `Sum`：函数名。
- `T`：类型形参，是一个类型占位符。
- `int | float64`：类型约束，规定 `T` 允许的类型范围。
- `a, b T`：参数类型都是 `T`。
- 最后的 `T`：返回值类型是 `T`。

可以自动推断类型：

```go
Sum(1, 2)       // T 推断为 int
Sum(1.2, 2.3)   // T 推断为 float64
```

也可以显式指定类型实参：

```go
Sum[int](1, 2)
Sum[float64](1.2, 2.3)
```

## 3. 类型形参、类型实参和类型推断

```go
func Sum[T int | float64](a, b T) T
```

这里的 `T` 是**类型形参**：定义函数时的类型占位符。

```go
Sum[int](1, 2)
```

这里的 `int` 是**类型实参**：调用时填入的具体类型。

```go
Sum(1, 2)
```

这里由编译器根据参数类型推断 `T = int`。

心智模型：

```text
普通参数：占位数据
类型参数：占位类型
类型约束：允许哪些类型，以及这些类型共同支持什么操作
类型实参：调用时填入的具体类型
```

## 4. 类型约束

类型约束决定两件事：

1. `T` 可以是什么类型。
2. 函数体内可以对 `T` 做什么操作。

```go
func Sum[T int | float64](a, b T) T {
	return a + b
}
```

因为 `T` 被限制为数字类型，所以可以使用 `+`。

```go
func Contains[T comparable](items []T, target T) bool {
	for _, item := range items {
		if item == target {
			return true
		}
	}
	return false
}
```

因为函数体使用了 `==`，所以约束选择 `comparable`。

选择约束的原则：

> 看函数体实际需要什么能力，再选择能准确表达该能力的最小约束。

## 5. `any`、`comparable` 和 `~`

### `any`

```go
func Print[T any](value T) {
	fmt.Println(value)
}
```

`any` 允许任意类型，但不保证所有类型都支持特定操作。

因此可以：

```go
fmt.Println(value)
```

但不能直接假设：

```go
value + value
value == other
```

因为任意类型中可能包含切片、Map、函数等不支持这些操作的类型。

### `comparable`

```go
func Contains[T comparable](items []T, target T) bool
```

`comparable` 表示 `T` 支持 `==` 和 `!=`，适合比较、查找、去重等场景。

```go
type UserID int64

ids := []UserID{101, 102}
Contains(ids, UserID(102)) // 合法，T 推断为 UserID
```

### `~`

```go
type UserID int64

type Number interface {
	~int64
}
```

- `int64`：只允许精确的 `int64` 类型。
- `~int64`：允许底层类型为 `int64` 的自定义类型，例如 `UserID`。

```go
func NextID[T ~int64](id T) T {
	return id + 1
}
```

这里 `comparable` 不够，因为“可比较”不等于“可以做加法”；`~int64` 同时表达了底层类型和数值运算需求。

## 6. 泛型类型

泛型可以用于切片、Map、结构体等类型。

### 泛型切片

```go
type NumberSlice[T int | int32 | int64] []T

numbers := NumberSlice[int]{1, 2, 3}
```

### 泛型 Map

```go
type GenericMap[K comparable, V int | string | byte] map[K]V

m := GenericMap[int, string]{
	1: "hello",
}
```

- `K` 必须是 `comparable`，因为 Map 需要比较 key。
- `V` 只能是约束列出的类型。

### 泛型结构体

```go
type Box[T any] struct {
	Value T
}

box := Box[string]{Value: "hello"}
```

区分：

```go
Box[string]                 // 泛型结构体实例化后的具体类型
Box[string]{Value: "hello"} // 创建具体结构体值
```

## 7. 接口作为泛型约束

普通接口可以作为泛型参数的约束：

```go
func PrintObject[T fmt.Stringer](value T) {
	fmt.Println(value.String())
}
```

含义：

```text
T 是具体类型，但 T 必须实现 String() string。
```

例如：

```go
type Person struct {
	Name string
}

func (p Person) String() string {
	return "Person: " + p.Name
}

PrintObject(Person{Name: "Alice"})
```

普通接口参数也可以实现相同的行为：

```go
func PrintObject(value fmt.Stringer) {
	fmt.Println(value.String())
}
```

如果函数只需要调用接口方法，且不需要保留具体类型，普通接口通常更简单；如果返回值或后续逻辑需要保留具体类型，泛型更有价值。

## 8. 泛型接口

```go
type Provider[T any] interface {
	Get() T
}
```

它是一个带类型参数的接口模板。

不同类型实参会产生不同的具体接口类型：

```go
Provider[string] // 要求 Get() string
Provider[int]    // 要求 Get() int
```

实现者：

```go
type UserProvider struct{}

func (UserProvider) Get() string {
	return "Alice"
}
```

使用：

```go
var p Provider[string] = UserProvider{}
```

合法，因为 `UserProvider` 有 `Get() string` 方法。

下面不合法：

```go
var p Provider[int] = UserProvider{}
```

因为 `Provider[int]` 要求 `Get() int`，而 `UserProvider` 提供 `Get() string`。

Go 接口实现要求方法签名完全匹配：方法名、参数类型、返回值类型都必须一致。

## 9. 泛型接口实例化与实现接口的值

这两个概念必须分开：

### 泛型接口实例化

```go
Provider[string]
```

含义是把 `T` 固定为 `string`，得到具体接口类型：

```go
interface {
	Get() string
}
```

它不是创建对象。

### 创建实现接口的值

```go
UserProvider{}
```

这是创建一个 `UserProvider` 类型的结构体值。

如果它有：

```go
Get() string
```

那么这个值就满足 `Provider[string]`。

准确表述：

> `UserProvider{}` 是 `UserProvider` 类型的对象实例，并且实现了 `Provider[string]` 接口。

不要说：

> `UserProvider` 是 `Provider[string]` 的实例。

最终过程：

```text
Provider[T]
    ↓ 固定 T = string
Provider[string]
    ↓ 要求 Get() string
UserProvider{}
    ↓ 检查方法
实现 Get() string，赋值合法
```

## 10. 接口变量、接口约束和类型集的区别

### 接口作为变量类型

```go
var writer io.Writer
```

它可以保存任意实现了 `Write([]byte) (int, error)` 的值，并在运行时通过接口调用方法。

### 接口作为泛型约束

```go
func Write[T io.Writer](w T, data []byte) error {
	_, err := w.Write(data)
	return err
}
```

这里 `io.Writer` 用来限制 `T`，不是用来声明一个接口变量。

如果函数不需要保留具体类型，这个泛型版本通常可以简化为：

```go
func Write(w io.Writer, data []byte) error
```

### 类型集约束

```go
type SignedInt interface {
	int8 | int16 | int32 | int64
}
```

它描述允许的类型集合，只用于泛型约束：

```go
func Add[T SignedInt](a, b T) T {
	return a + b
}
```

不能用来声明普通接口变量：

```go
var n SignedInt // 不允许
```

区分原则：

```text
方法集合：描述类型会什么，可以作为普通接口类型
类型元素集合：描述 T 可以是什么，只能作为泛型约束
```

## 11. 复杂类型集与 `~`

类型集可以用并集、交集和底层类型约束组合。

### 并集

```go
type A interface {
	~int | ~string
}
```

`A` 表示：底层类型是 `int` 或 `string` 的所有类型。

因此下面都满足：

```go
type MyInt int
type MyString string

F[int](1)
F[MyInt](1)
F[MyString]("x")
```

### 交集

接口中多个元素同时出现时，取的是交集：

```go
type B interface {
	~int
	fmt.Stringer
}
```

`B` 表示：底层类型是 `int`，并且实现 `String() string` 的类型。

```go
type MyInt int

func (m MyInt) String() string {
	return "x"
}
```

此时：

```go
G[int](1)   // 不允许：int 没有 String() string 方法
G[MyInt](1) // 允许：MyInt 底层类型是 int，且实现 fmt.Stringer
```

注意：`fmt.Stringer` 是普通接口，声明的方法是 `String() string`。作为泛型约束时，它代表“所有实现该方法的非接口类型”的类型集。

### 空类型集与空接口

空类型集和空接口不是一回事。

```go
type Impossible interface {
	int
	string
}
```

这里要求一个类型既是 `int` 又是 `string`，不存在这样的类型，所以类型集为空。

```go
func Print[T any](v T) {}
```

`any` / `interface{}` 表示所有非接口类型，是全集，不是空集。

### `~` 的判断模型

```text
int  ：只允许精确的 int 类型
~int ：允许 int，也允许 type MyInt int 这类底层类型为 int 的命名类型
```

使用 `~` 时，核心问题是：这个自定义类型的底层类型是否落在约束允许范围内。

## 12. 泛型语言边界

泛型不是类型万能开关。Go 对泛型有几个重要边界。

### 带类型集的接口不能作为普通变量类型

```go
type Number interface {
	~int | ~float64
}

var x Number // 不允许
```

`Number` 是约束接口，只能用于限制类型参数：

```go
func Add[T Number](a, b T) T {
	return a + b
}
```

### 方法不能声明自己的新类型参数

```go
type Box[T any] struct {
	Value T
}

func (b Box[T]) Get() T {
	return b.Value
}

func (b Box[T]) Convert[U any](fn func(T) U) U { // 不允许
	return fn(b.Value)
}
```

receiver 可以使用类型参数 `T`，但方法不能再单独声明新的 `[U any]`。需要新类型参数时，通常改成普通函数。

### 不要用泛型模拟大量类型分支

如果不同类型要走完全不同业务逻辑，泛型通常不是合适抽象。

```go
func Handle(v any) {
	switch x := v.(type) {
	case int:
		fmt.Println(x + 1)
	case string:
		fmt.Println(strings.ToUpper(x))
	case User:
		SaveUser(x)
	}
}
```

这类代码的核心不是“相同逻辑作用于不同类型”，而是运行时分发或业务分支。

## 13. 泛型数据结构

泛型适合实现容器，因为容器逻辑相同，但元素类型不同。

```go
type Queue[T any] []T

func (q *Queue[T]) Push(v T) {
	*q = append(*q, v)
}

func (q *Queue[T]) Pop() (T, bool) {
	var zero T

	if len(*q) == 0 {
		return zero, false
	}

	v := (*q)[0]
	*q = (*q)[1:]
	return v, true
}
```

使用：

```go
var q Queue[int]

q.Push(1)
q.Push("hello") // 不允许：Queue[int] 的 Push 参数类型是 int

v, ok := q.Pop() // v 的类型是 int
```

`Pop` 没有做类型断言。`Queue[int]` 实例化后，本质上就是从 `[]int` 中取出 `int`。

`Pop` 返回 `(T, bool)`，因为空队列时没有元素可返回，而 `T` 可能是 `int`、`string` 或指针。只返回 `T` 会分不清零值到底是真实元素还是空队列结果。

## 14. 泛型性能与工程取舍

泛型不是反射，也不是天然零成本保证。

优先使用泛型的场景：

```go
func Contains[T comparable](items []T, target T) bool {
	for _, item := range items {
		if item == target {
			return true
		}
	}
	return false
}
```

这里逻辑与类型无关，只要求元素支持 `==`，所以 `T comparable` 正好表达最小能力。

不优先使用泛型的场景：

```go
func WriteJSON(w io.Writer, v any) error {
	return json.NewEncoder(w).Encode(v)
}
```

`io.Writer` 是普通行为接口，`json.Encoder.Encode` 本来接收 `any`。这里没有对 `v` 做类型相关操作，也不需要保留具体返回类型，引入泛型没有收益。

工程判断标准：

```text
泛型能否表达更强的编译期约束，或保留输入输出之间的具体类型关系？
```

如果答案是否定的，普通接口、具体类型或 `any` 可能更简单。

## 15. 本阶段检验结论

用户已通过以下场景检验：

- 能解释 `T` 是类型形参。
- 能解释 `~int` 允许底层类型为 `int` 的自定义类型。
- 能根据 `==` 选择 `comparable`。
- 能将 `Contains` 迁移到 `UserID` 自定义类型。
- 能解释 `Provider[string]` 和 `Provider[int]` 是不同的具体接口类型。
- 能区分泛型接口实例化和创建实现接口的结构体值。
- 能判断 `ConfigLoader{}` 是否满足 `Loader[string]`。
- 能判断泛型是否真正保留了调用者的具体类型。
- 能计算复杂类型集中的并集、交集和空类型集。
- 能解释 `~int` 与 `fmt.Stringer` 组合时为什么 `MyInt` 需要实现 `String() string`。
- 能区分带类型集的约束接口和普通行为接口。
- 能判断泛型方法限制、带类型集接口变量限制和类型分支滥用问题。
- 能解释 `Queue[T]` 相比 `[]any` 的编译期类型安全，以及 `Pop() (T, bool)` 的必要性。
- 能判断 `Contains[T comparable]` 适合泛型，而类型分支处理和 `WriteJSON(io.Writer, any)` 不适合泛型。

掌握边界：已完成泛型核心语法、泛型接口、复杂类型集、语言边界、简单泛型数据结构和工程取舍检验。尚未深入验证 Go 泛型底层实现细节、gcshape/dictionary 性能模型和大型泛型容器设计。

## 16. Interface 方法集复习结论

本轮综合检验表明，接口方法集已经建立基本判断能力，但还不够熟练，后续需要通过更多场景巩固。

### 值接收者与指针接收者

```go
type Runner interface { Run() error }
type Job struct{}
func (j *Job) Run() error { return nil }
```

此时 `Job` 的方法集不包含 `Run`，`*Job` 的方法集包含 `Run`。因此 `Job{}` 不能赋给 `Runner`，`&Job{}` 可以。若 `Run` 使用值接收者，则 `Job` 和 `*Job` 都满足接口。

### 自动取址不等于接口实现

可寻址变量调用指针接收者方法时可以自动取址：

```go
j := Job{}
j.Run() // 等价于 (&j).Run()
```

但接口赋值或函数传参不会自动取址：`Execute(j)` 不允许，`Execute(&j)` 允许。临时值 `Job{}.Run()` 不能依赖自动取址，因为临时值不可寻址。

### nil 接口与 nil 指针

接口值可理解为“动态类型 + 动态值”。`var r Runner = (*Job)(nil)` 时，动态类型是 `*Job`，动态值是 `nil`，所以 `r == nil` 为 `false`。只有动态类型和动态值都为空时，接口才等于 `nil`。nil 指针的方法是否 panic，取决于方法体是否解引用 receiver。

### 调用方定义最小接口

调用方只需要创建用户时，应依赖最小接口：

```go
type UserCreator interface { CreateUser(name string) error }
func Register(repo UserCreator, name string) error { return repo.CreateUser(name) }
```

接口通常定义在调用方包，因为调用方最清楚当前用例需要哪些能力；一个具体实现可以同时满足多个调用方的小接口。

### 本轮卡点与掌握边界

- 已能判断值接收者和指针接收者的基本方法集。
- 已能判断可寻址变量调用指针方法时的自动取址。
- 已能区分接口传参不会自动取址。
- 已能基本判断 nil 接口与接口中 nil 指针的差异。
- 仍需巩固：静态类型、动态类型、动态值三个术语，以及复杂场景中的方法集迁移。

## 17. 后续拓展清单

以下内容已登记为泛型主题的后续学习范围，当前未教学或未检验，不计入已掌握结论。

1. **接口巩固题**：nil 接口、类型断言、接口嵌套和组合场景。
2. **泛型实现细节**：gcshape stenciling、dictionary 传递和二进制体积/运行时开销。
3. **大型泛型容器**：堆、集合、比较器注入和对象池的设计取舍。

建议学习顺序：接口巩固题 -> 泛型实现细节 -> 大型泛型容器。
 
## 18. 参考资料

- [Go 官方泛型教程](https://go.dev/doc/tutorial/generics)
- [Go 语言规范：Interface types 与 type set](https://go.dev/ref/spec#Interface_types)
- [用户指定文章：泛型](https://golang.halfiisland.com/essential/senior/90.generic.html)
