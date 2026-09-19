# Learn GDScript Core — 系统教学方案

## Why

用户希望系统、完整地学习 GDScript；当前长期学习状态没有 GDScript 主题、知识状态或 checkpoint 记录，也不应预设任何编程前置知识。需要一条以 Godot 4.7 stable 官方文档为依据、可恢复、可检验的主线，把语言本身与 Godot 的节点/场景运行模型连接起来，而不是把 GDScript 当作脱离引擎的 Python 方言。

## What Changes

- 建立从零基础到能独立设计、实现、调试中小型 Godot 游戏脚本的 GDScript 教学 change。
- 覆盖 GDScript 4.x 语言核心：语法、值与引用、类型系统、函数、集合、面向对象、脚本生命周期、错误处理、异步、信号、资源与工具脚本。
- 覆盖完成实际游戏脚本所需的 Godot 运行模型：节点、场景、场景树、输入、帧循环、生命周期、信号、资源、实例化与场景组织。
- 采用小节练习、可运行功能和 checkpoint；每章综合检验通过前不视为掌握。
- 以一个逐步扩展的 2D 小游戏作为贯穿项目，要求用户解释代码、修改行为、定位错误，而不是只复制代码。
- 主线结束且用户确认后，回写稳定学习结论与实际使用的来源链接；未经批准不开始正式教学或写入掌握状态。

## Capabilities

### New Capabilities

- `gdscript/foundations`: 编辑器环境、脚本结构、语法、变量、常量、基本类型与表达式。
- `gdscript/control-flow-functions`: 条件、循环、模式匹配、函数、作用域、返回值与参数。
- `gdscript/collections`: Array、Dictionary、 typed collections、字符串处理、可变性与引用语义。
- `gdscript/typing-and-errors`: 渐进式静态类型、类型推断、注解、警告、断言、运行时错误与调试。
- `gdscript/object-model`: 类、继承、组合、class_name、静态成员、内部类、Callable 与 lambda。
- `godot/nodes-scenes-lifecycle`: Node、Scene、SceneTree、实例化、生命周期回调与节点引用。
- `godot/input-and-game-loop`: 输入映射、_process、_physics_process、delta、运动与物理更新边界。
- `godot/signals-and-async`: signal、连接/断开、Callable、await、协作式异步与解耦通信。
- `godot/resources-and-editor`: Resource、预加载/加载、导出变量、资源化数据、工具脚本与编辑器可见性。
- `gdscript/architecture-and-quality`: 脚本职责、场景组织、Autoload、数据与逻辑边界、风格、性能意识与版本控制。
- `gdscript/capstone`: 综合项目、需求拆解、实现、调试、重构、解释与迁移能力考核。

### Modified Capabilities

无（本 change 仅新增 GDScript 学习主题）。

## Goal / Scope / Non-goals

**Goal（目标能力）：** 在 Godot 4.x 环境下（当前实测 Godot 4.6），用户能不依赖逐行跟写，独立阅读和编写结构清晰的 GDScript，构建一个可运行的 2D 小游戏核心闭环：节点与场景组织、输入、状态、帧更新、信号、资源、异步、错误处理和调试；能说明关键语言与引擎行为的因果关系，并能定位常见错误。

**Scope（本轮讲授）：**

1. GDScript 的身份与语法：脚本即类、extends、注释、缩进、标识符、变量/常量/枚举、基本值类型、运算符与表达式。
2. 控制流与函数：if/elif/else、for/while、match、break/continue、函数、默认参数、返回值、作用域和递归边界。
3. 数据建模：Array/Dictionary、typed collections、字符串、Vector2/Vector3、值与引用、复制与别名、可变数据。
4. 渐进式类型系统：显式类型、:= 推断、Variant、类型转换、is/as、返回类型、警告和静态检查。
5. 对象模型：类与实例、继承与组合、覆盖、super、class_name、static、内部类、Callable 和匿名函数。
6. Godot 基础运行模型：节点、场景、场景树、脚本附加、_init/_ready/_process/_physics_process/_exit_tree、节点路径与生命周期安全。
7. 游戏循环与输入：InputMap、_input/_unhandled_input、动作输入、delta、运动、CharacterBody2D 的职责边界和基础碰撞反馈。
8. 信号与异步：声明和发射 signal、代码/编辑器连接、Callable、断开、一次性连接、await 信号/协程、取消与生命周期风险。
9. 资源与编辑器集成：Resource、preload/load、导出属性、资源数据与场景数据、tool 脚本的适用边界。
10. 错误处理与调试：解析/类型/运行时错误、assert、错误返回、断点、远程调试、最小复现和日志策略。
11. 可维护性：命名和格式风格、场景与脚本边界、Autoload 的适用条件、依赖方向、避免过度耦合、基础性能判断与项目组织。
12. 综合项目：从需求到场景树、脚本协作、状态、UI/信号、存档或配置资源、调试、重构和口头解释。

**Non-goals（本轮不展开，登记为后续候选）：**

- GDScript 之外的其他编程语言、GDExtension、Shader、VisualScript 或完整游戏美术/音频制作。
- 3D 渲染、动画树、导航、多人联机、着色器编程和平台发布细节；仅在综合项目确实需要时做最小接口说明。
- Godot 全部类库 API 背诵；以查阅 Class Reference、理解抽象和完成需求为目标。
- 高级性能工程（线程安全、服务器权威网络、底层渲染、内存布局）与大型团队生产流程。
- 将未通过 checkpoint 的内容写成“已掌握”，或在用户未确认章节结束前自动进入下一章。

**Prerequisites：** 不预设编程基础。需要安装 Godot 4.x 和一个编辑器；环境安装与最小项目创建会作为第一阶段实操。当前用户实测版本为 Godot 4.6，后续遇到版本差异时先查对应官方文档再调整。

## Evidence and Checkpoints

- 每小节：用户先预测行为，再完成一个最小可运行改动，并用自己的话解释关键因果。
- 每章：至少一个边界题（生命周期/类型/引用/异步等）和一个迁移题（改需求而非照抄）。
- 综合考核：独立完成一个可运行 2D 小游戏核心功能；随机抽取需求变更；解释节点生命周期、数据流、信号连接、类型选择和错误定位；修复一个预置缺陷。
- 掌握判定以实际回答与运行结果为证据；未稳或低置信度内容回退到更小概念，不跳过补课。

## Sources

- Godot GDScript 文档索引（Godot Engine stable，当前用户使用 4.6）：https://docs.godotengine.org/en/stable/tutorials/scripting/gdscript/index.html
- GDScript reference：https://docs.godotengine.org/en/stable/tutorials/scripting/gdscript/gdscript_basics.html
- GDScript dynamic language introduction：https://docs.godotengine.org/en/stable/tutorials/scripting/gdscript/gdscript_advanced.html
- Static typing in GDScript：https://docs.godotengine.org/en/stable/tutorials/scripting/gdscript/static_typing.html
- GDScript style guide：https://docs.godotengine.org/en/stable/tutorials/scripting/gdscript/gdscript_styleguide.html
- Using signals：https://docs.godotengine.org/en/stable/getting_started/step_by_step/signals.html
- Godot best practices：https://docs.godotengine.org/en/stable/tutorials/best_practices/index.html

## Review Status

- 状态：**approved，用户已明确批准**。
- 已进入正式教学；每个阶段仍需通过 checkpoint，未验证内容不写成已掌握。
