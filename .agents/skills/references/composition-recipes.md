# Skill 组合配方

用于 `learn-orchestrator` 选择最小可执行 skill 序列。

## 项目第一次学习

1. `learn-context`：读取 README、docs、入口结构和当前目标。
2. `project-deep-dive`：拆 3 到 7 个学习切片。
3. `learning-checkpoint`：确认用户能复述项目主链路。
4. `learning-note-writer`：只在阶段结论稳定后回写。

## 接入已有项目仓库

1. `repo-skill-integrator`：扫描目标 `AGENTS.md` 和已有 skills。
2. 生成集成计划：同名冲突、相似职责、缺失 skill、AGENTS.md 合并建议。
3. 只复制无冲突缺失项；相似 skill 先合成，不并排保留。
4. 目标仓库通过 `validate_skills.py` 后再开始学习任务。

## 用户粘贴 issue 或 PR

1. `issue-pr-intake`：提取目标、非目标、任务树、验收标准、评论约束和粒度判断。
2. `learn-context`：只读取 issue/PR 指向的文件、接口、模块、测试和文档。
3. 根据任务类型选择：
   - 理解链路 -> `code-path-tracer`
   - 拆学习切片 -> `project-deep-dive`
   - 审核 PR / 评论 -> `review-coach`
   - 概念补课 -> `concept-teacher`
4. `learning-checkpoint`：用 issue/PR 场景做短检验。
5. `learning-note-writer`：只有通过检验或形成稳定结论后回写。

## 看懂一个接口或功能

1. `learn-context`：定位目标接口、测试、文档。
2. `code-path-tracer`：沿入口追到响应或副作用。
3. `architecture-lens`：分析分层和边界。
4. `concept-teacher`：讲 1 到 2 个卡住的概念。
5. `learning-checkpoint`：出一道场景题或最小实操。

## 学一个技术概念

1. `source-researcher`：查官方资料或权威来源。
2. `concept-teacher`：结合项目场景讲清概念。
3. `learning-checkpoint`：检验理解。
4. `learning-note-writer`：反复出现或通过检验后再沉淀。

## Review 用户代码

1. `learn-context`：确认目标行为、代码范围和验证方式。
2. `review-coach`：按严重度输出问题。
3. `concept-teacher`：只讲暴露出的概念误区。
4. `learning-checkpoint`：让用户解释最小修复思路。

## 找 GitHub 上可借鉴的 learning skill

1. `source-researcher`：找候选仓库和模式。
2. `architecture-lens`：判断候选是否适合本系统。
3. `project-deep-dive`：把可借鉴模式转成原子 skill 或 reference。
4. `learning-note-writer`：记录采用/不采用理由。

## 组合上限

- 单轮最多执行 5 个 skill。
- 超过 5 个时按阶段拆分。
- 每阶段必须有一个可验证产物：上下文包、切片列表、链路图、概念卡、检验题或回写草稿。
- 如果 issue/PR 已经是强粒度，只执行当前必要链路，不重新拆任务。
