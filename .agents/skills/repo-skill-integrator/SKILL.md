---
name: repo-skill-integrator
description: "仓库级 skill 和 AGENTS.md 集成合并。Use when installing this learning skill kit into a repo that already has AGENTS.md or .agents/skills, scanning existing project skills, resolving conflicts, merging similar skills, synthesizing repo-specific rules, and avoiding duplicate skills that make agents spin."
---

# Repo Skill Integrator

IRON LAW: 不覆盖目标仓库已有 AGENTS.md 或 skills；先扫描、分类、合成，再只添加无冲突内容。

## 职责

把本学习 skill kit 集成到已有项目仓库时，保留目标仓库原有规则，合并相似职责，避免重复 skill 造成 agent 空转。

## 工作流

- [ ] Step 1: 读取 `.agents/skills/references/repo-integration-workflow.md`
- [ ] Step 2: 扫描目标仓库 `AGENTS.md`、`.agents/skills/*/SKILL.md`、已有模板和校验脚本
- [ ] Step 3: 按职责分类：同名冲突、相似职责、完全缺失、可直接复用
- [ ] Step 4: 对同名或相似 skill，输出“综合重塑版”建议，不保留两份相似 skill
- [ ] Step 5: 对 `AGENTS.md`，提炼已有项目硬规则，再合入学习规则，去重并标出冲突
- [ ] Step 6: 只把无冲突缺失项加入目标仓库；有冲突项输出合并方案给用户确认

## 输出格式

- 目标仓库：
- 已有 AGENTS.md 结论：
- 已有 skills：
- 可直接新增：
- 需要合并重塑：
- 不建议加入：
- AGENTS.md 合并建议：
- 用户确认点：

## 反模式

- 不要用本仓库的 `AGENTS.md` 直接覆盖目标仓库。
- 不要把职责相近的两个 skill 都留下。
- 不要因为目标仓库已有规则就完全跳过学习规则。
- 不要把项目特定规则抽象掉；学习规则只能补充，不能吞掉项目约束。
