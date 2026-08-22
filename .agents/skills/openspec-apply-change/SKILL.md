---
name: openspec-apply-change
description: 从已批准的 OpenSpec 教学方案恢复并推进当前教学任务、checkpoint 和学习进度。
---

# OpenSpec Apply Change

## IRON LAW
只推进已批准的教学任务；不把教学任务当成代码实现。

## 职责
读取 proposal、design、specs、tasks，恢复被打断的教学进度，推进小节教学、checkpoint、综合考核和回写任务。

## 工作流
1. 运行 `openspec list --json`，选择相关 active change；不确定时询问用户。
2. 运行 `openspec status --change <topic> --json` 和 `openspec instructions apply --change <topic> --json`。
3. 读取 CLI 指定的 artifacts，确认 proposal 已获用户批准。
4. 展示当前进度和下一项任务；一次只推进一个教学单元。
5. 用户插话时先更新 tasks 状态，处理插话后从下一项恢复。
6. checkpoint 后记录证据；章节综合考核后等待用户确认，不自动 archive 或进入下一章。

## 输出格式
- Change / 状态：
- 当前任务：
- 已完成 / 剩余：
- 本轮 checkpoint：
- 下一步：等待回答、继续或用户确认

## 反模式
- 不跳过审核。
- 不自动推进下一章节。
- 不重发已经发送的完整教学内容。
