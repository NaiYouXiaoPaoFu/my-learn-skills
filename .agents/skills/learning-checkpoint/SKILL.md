---
name: learning-checkpoint
description: "讲后理解检验和面试式追问。Use when the user asks to 检验我是否学会、出题、概念抽查、小实操、让我复述、模拟面试官拷打、确认是否掌握 Gin/HTTP/中间件/闭包/回调/架构设计/代码设计。Actions: quiz, checkpoint, interview drill, follow-up question, verify learning."
---

# Learning Checkpoint

IRON LAW: 检验必须短、具体、和当前项目场景相关；追问最多两轮，错了先补课，不无限连问。

## 职责

用 1 到 3 个短问题或一个最小实操确认用户是否真正理解，可用面试式追问增强压迫感，但必须控制节奏。

## 工作流

- [ ] Step 1: 读取当前概念卡、链路图或 Review 结论
- [ ] Step 2: 读取 `.agents/skills/references/checkpoint-catalog.md`
- [ ] Step 3: 需要面试式追问时读取 `.agents/skills/references/interview-checkpoint-style.md`
- [ ] Step 4: 选择一种题型：概念复述、对比判断、场景判断、最小实操、排错判断、面试追问
- [ ] Step 5: 先让用户回答，不直接给完整答案
- [ ] Step 6: 用户答错时先补缺口，再最多追问 1 到 2 个相邻问题
- [ ] Step 7: 两轮仍不稳时停止追问，标记未掌握并交给 `concept-teacher`

## 输出格式

- 主题：
- 检查类型：
- 想验证什么：
- 题目：
- 通过标准：
- 追问上限：
- 错误后的补充策略：

## 反模式

- 不要一次出很多题。
- 不要出脱离项目的考试题。
- 不要在用户回答前泄露参考答案。
- 不要因为一个错误连续问多轮同类问题。
- 不要用“面试拷打”替代必要补课。
