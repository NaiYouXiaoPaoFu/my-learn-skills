# 教学方案目录

当前教学方案的唯一过程状态由 OpenSpec 管理，不在此目录另建第二套 draft/approved 状态机。

## OpenSpec 位置

```text
openspec/changes/<topic>/
├── proposal.md  # 目标、范围、非目标、历史状态与用户审核
├── design.md    # 教学编排、取舍、资料和恢复说明
├── specs/       # 可验证的学习要求与场景
└── tasks.md     # 小节、checkpoint、综合考核和回写任务
```

## 状态边界

- `openspec/changes/`：当前教学方案、审核状态和过程进度。
- `openspec/changes/archive/`：用户确认结束后归档的历史方案。
- `.learning/learning-state.sqlite3`：长期学习等级、checkpoint 证据、误区、资料和偏好。
- `docs/learning/`：稳定的学习总结，不作为当前工作流状态源。


OpenSpec 相关 agent skills 统一位于 `.agents/skills/openspec-*`，因此所有 agent 都可按仓库默认技能发现机制读取。
用户明确批准 `proposal.md` 后才能开始正式教学。被其他问题打断时，先更新 `tasks.md`，恢复时从 OpenSpec 状态继续。
