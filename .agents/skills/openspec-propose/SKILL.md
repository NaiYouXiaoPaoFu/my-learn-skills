---
name: openspec-propose
description: 创建并完善可恢复的 OpenSpec 教学方案，记录目标范围、学习证据、取舍和审核门禁，等待用户批准后再开始正式教学。
---

# OpenSpec Propose

## IRON LAW
先创建可恢复的教学方案，未经用户明确批准不得开始正式教学。

## 职责
创建 OpenSpec change 的 proposal、design、specs 和 tasks，记录教学目标、范围、取舍、checkpoint 与恢复状态。

## 工作流
1. 运行 `openspec list --json`，确认没有重复的 active change。
2. 运行 `openspec new change <topic>`。
3. 读取 `openspec status --change <topic> --json` 和 artifact instructions。
4. 按依赖顺序创建 artifacts；方案必须说明讲什么、为什么讲、不讲什么、为什么不讲，以及综合考核如何覆盖相关边界。
5. 展示 draft 方案，等待用户明确批准或修改；未经批准不得调用 apply。

## 输出格式
- Change：路径和状态
- Goal / Scope / Non-goals：
- 历史学习证据：
- 教学取舍：
- Checkpoint 与综合考核：
- 等待用户：批准或修改

## 反模式
- 不把 draft 当 approved。
- 不创建第二套平行方案状态。
- 不因用户插话而创建重复 change。
