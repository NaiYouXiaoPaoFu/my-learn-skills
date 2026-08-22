# Go 第 6 章：方法学习总结

## 学习范围

本阶段学习《Go 语言圣经》第 6 章，覆盖方法声明、指针接收器、嵌入结构体、方法值与方法表达式、Bit 数组和封装。

## 核心主线

```text
命名类型
  -> 方法与接收器
  -> 值接收器 / 指针接收器
  -> 嵌入字段与方法提升
  -> 方法值 / 方法表达式
  -> Bit 数组实践
  -> 封装与 API 边界
```

## 1. 方法与接收器

方法是在函数名之前增加接收器声明：

```go
func (p Point) Distance(q Point) float64 {
    return math.Hypot(q.X-p.X, q.Y-p.Y)
}
```

- `(p Point)` 是接收器。
- 调用 `p.Distance(q)` 时，`p` 已作为接收器隐含传入。
- 括号内只传普通参数，不能再次传入接收器。
- 方法绑定到命名类型；不同类型可以拥有同名方法。
- 命名的 slice 等非结构体类型也可以定义方法。

## 2. 值接收器与指针接收器

```go
func (a Account) Balance() int
func (a *Account) Deposit(amount int)
```

- 值接收器接收副本，适合只读、值语义和较小对象。
- 指针接收器操作原对象，适合修改状态或避免复制较大对象。
- 可寻址变量调用指针方法时，Go 可以隐式取地址：`p.ScaleBy(2)` 近似为 `(&p).ScaleBy(2)`。
- 临时字面量不可寻址，不能直接调用需要指针接收器的方法。
- 同一类型通常保持接收器风格一致，但不是语言强制规则。
- 结构体值复制只复制字段本身；slice、map、指针等字段可能继续共享底层数据。slice 的 `append` 扩容还可能让副本指向新底层数组。

## 3. 嵌入结构体

```go
type ColoredPoint struct {
    Point
    Color string
}
```

嵌入字段会提升字段和方法：

```go
cp.X       // 近似 cp.Point.X
cp.Move(1, 2) // 通过 Point 提升的方法
```

关键边界：嵌入是组合，不是继承。

- `ColoredPoint` 拥有一个 `Point`，但不是 `Point`。
- 需要 `Point` 参数时，不能把 `ColoredPoint` 自动当成 `Point`，要显式使用 `q.Point`。
- 调用提升的指针方法时，外层可寻址变量可以让编译器完成隐式取地址。

## 4. 方法值与方法表达式

方法值绑定具体接收器：

```go
f1 := p.Add
f1(q)
```

方法表达式从类型取得方法，接收器成为第一个参数：

```go
f2 := Point.Add
f2(p, q)
```

判断口诀：

```text
方法值：对象已绑定，调用时不再传接收器。
方法表达式：对象未绑定，接收器作为第一个参数。
```

## 5. Bit 数组

`IntSet` 用 `[]uint64` 表示非负整数集合：

```go
type IntSet struct {
    words []uint64
}
```

对元素 `x`：

```go
word := x / 64
bit := x % 64
```

因此：

```text
1   -> words[0]
65  -> words[1]
130 -> words[2]
```

添加元素：

```go
s.words[word] |= 1 << bit
```

- `1 << bit` 生成目标位掩码。
- `|=` 将目标位设置为 `1`，不影响其他位。
- 按位或对应集合并集。
- `0010 | 0100 = 0110` 表示集合 `{1, 2}`，新增的是 `2`，不是 `3`。
- `Add`、`UnionWith` 等修改集合的方法需要指针接收器。
- 零值 `IntSet` 可以作为空集合直接使用。

## 6. 封装

Go 通过标识符首字母控制包外可见性：

- 大写首字母：导出。
- 小写首字母：未导出。
- 可见性边界是包，不是类型内部。

```go
type Account struct {
    balance int
}

func (a *Account) Balance() int {
    return a.balance
}
```

隐藏字段并通过方法操作，可以：

- 防止外部写入非法状态，例如负余额；
- 维护类型不变量；
- 隐藏底层表示；
- 允许未来替换实现而不破坏调用方。

封装不是机械地隐藏所有字段。`Path []Point` 的底层序列可能就是类型本质，适合保留 slice 语义；`IntSet` 的 `[]uint64` 只是实现细节，更适合隐藏。

## 已掌握与未稳定点

### 已掌握

- 方法声明、接收器和方法调用。
- 值接收器与指针接收器的修改语义。
- 可寻址变量的隐式取地址。
- 嵌入字段、字段提升、方法提升和组合关系。
- 方法值与方法表达式的参数差异。
- Bit 数组的 word/bit 定位和按位运算基础。
- 封装对不变量、API 稳定性和实现替换的价值。

### 未稳定点

- 复杂结构体复制时，slice、map、指针字段的共享与扩容边界需要继续通过独立排错巩固。
- 尚未通过完整迁移场景证明能独立设计一组方法和封装 API。
- Bit 数组还未实现完整的 `Remove`、`Clear`、`Copy`、交集和差集方法。

## 掌握程度

**4/6：能解释取舍和边界。**

证据：用户能独立回答方法声明、指针接收器、嵌入结构体、方法值/表达式和封装综合题，并能从底层共享、扩容、API 稳定性和不变量角度解释原因。

暂未评为 5/6 或 6/6：复杂引用字段复制、完整 API 设计、独立排错和跨场景迁移尚未充分验证。

## 下次衔接

下一阶段候选：第 7 章接口。进入前先保留本章的未稳定点，不重复整章教学；必要时用一个小型综合排错题复查值复制、指针接收器和封装边界。

## 参考资料

- [Go语言圣经第 6 章：方法](https://gopl-zh.github.io/ch6/ch6.html)
- [6.1 方法声明](https://gopl-zh.github.io/ch6/ch6-01.html)
- [6.2 基于指针对象的方法](https://gopl-zh.github.io/ch6/ch6-02.html)
- [6.3 通过嵌入结构体来扩展类型](https://gopl-zh.github.io/ch6/ch6-03.html)
- [6.4 方法值和方法表达式](https://gopl-zh.github.io/ch6/ch6-04.html)
- [6.5 示例：Bit 数组](https://gopl-zh.github.io/ch6/ch6-05.html)
- [6.6 封装](https://gopl-zh.github.io/ch6/ch6-06.html)
- [Go 官方规范：Method declarations](https://go.dev/ref/spec#Method_declarations)
- [Go 官方规范：Struct types](https://go.dev/ref/spec#Struct_types)
- [Go 官方规范：Exported identifiers](https://go.dev/ref/spec#Exported_identifiers)
