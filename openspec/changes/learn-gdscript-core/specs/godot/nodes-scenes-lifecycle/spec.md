## Purpose

把 GDScript 语言实例连接到 Godot 的节点、场景和 SceneTree 运行模型，建立生命周期安全的脚本执行链路。

## ADDED Requirements

### Requirement: 学习者能解释节点与场景关系

学习者 MUST 能区分 Node、Scene、SceneTree、脚本和场景实例，能创建、保存、实例化场景并使用稳定的节点引用。

#### Scenario: 组合可复用游戏场景
- **WHEN** 主场景需要放入一个可复用玩家场景
- **THEN** 学习者能实例化玩家场景并指出脚本实例与节点树位置

### Requirement: 学习者能安全使用生命周期

学习者 MUST 能解释 `_init`、`_ready`、`_process`、`_physics_process` 和 `_exit_tree` 的职责与调用时机，并避免在节点未就绪或已退出后访问它。

#### Scenario: 处理动态生成节点
- **WHEN** 敌人运行时加入或移出场景树
- **THEN** 学习者能选择初始化、清理和引用时机，且不依赖偶然的节点顺序
