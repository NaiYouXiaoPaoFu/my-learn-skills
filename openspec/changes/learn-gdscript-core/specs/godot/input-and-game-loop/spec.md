## Purpose

掌握 Godot 输入与帧循环边界，使学习者能实现稳定、可调试的角色控制与实时行为。

## ADDED Requirements

### Requirement: 学习者能处理动作输入

学习者 MUST 能配置 InputMap，使用动作输入和输入回调，并能区分轮询输入与事件输入的适用场景。

#### Scenario: 支持多设备同一动作
- **WHEN** 移动动作需要同时支持键盘与手柄
- **THEN** 学习者能通过动作名处理输入，而不是把设备按键散落在业务代码中

### Requirement: 学习者能区分帧更新

学习者 MUST 能解释 `_process`、`_physics_process`、`delta` 与物理更新的边界，并实现不依赖帧率的基础移动。

#### Scenario: 改变运行帧率
- **WHEN** 游戏帧率发生变化
- **THEN** 角色速度和计时逻辑仍按时间推进，物理相关行为位于合适的更新回调
