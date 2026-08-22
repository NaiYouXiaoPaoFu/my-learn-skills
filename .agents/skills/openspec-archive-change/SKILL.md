---
name: openspec-archive-change
description: 在用户确认章节或教学方案结束后，检查并归档 OpenSpec 教学 change。
---

# OpenSpec Archive Change

## IRON LAW
未经用户明确确认，不得归档教学 change。

## 职责
检查教学方案、tasks、checkpoint、综合考核和学习回写是否完成，在用户确认后归档历史 change。

## 工作流
1. 运行 `openspec list --json`，明确选择 change，不凭猜测归档。
2. 运行 `openspec status --change <topic> --json`，检查 artifacts 和 tasks。
3. 检查章节综合 checkpoint、掌握度评估和 learning-note-writer 回写状态。
4. 展示未完成项和归档影响，等待用户确认。
5. 仅在确认后运行 OpenSpec archive 流程。

## 输出格式
- Change：
- 完成状态：
- 未完成项：
- 回写状态：
- 用户确认：
- 归档位置：

## 反模式
- 不自动选择有歧义的 change。
- 不把未完成任务隐藏成完成。
- 不未经确认 archive 或推进下一章。
