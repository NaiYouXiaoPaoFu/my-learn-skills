---
name: openspec-explore
description: 探索教学主题和方案取舍，结合学习状态形成可审核的 OpenSpec 教学方案，不开始正式教学或推进未批准任务。
---

# OpenSpec Explore

## IRON LAW
探索可以发散，正式教学必须回到已审核的 OpenSpec change。

## 职责
读取相关学习状态和 active change，澄清目标、边界、前置知识和取舍；只更新用户同意的方案 artifacts，不执行正式教学。

## 工作流
1. 运行 `openspec list --json`。
2. 若有相关 change，读取 proposal、design、specs、tasks；否则先讨论是否创建 change。
3. 查询 SQLite 相关知识状态、checkpoint、误区和偏好。
4. 比较讲与不讲的内容，说明每个取舍如何服务当前目标。
5. 将稳定决定写入对应 artifact，但不擅自批准方案。

## 输出格式
- 当前问题：
- 已知证据：
- 方案选项与取舍：
- 未决问题：
- 建议更新的 artifact：

## 反模式
- 不在 explore 中开始正式教学。
- 不自动捕获未经用户确认的决定。
- 不忽略已有 active change。
