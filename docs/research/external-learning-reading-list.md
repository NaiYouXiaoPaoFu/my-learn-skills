# 外部学习资料阅读清单

这份清单记录本仓库设计时参考的外部资料。用途是帮助学习，不作为规则来源直接照搬。

## Skills / Agent 编排

- GitHub Copilot coding agent skills 文档  
  https://docs.github.com/en/copilot/how-tos/agents/copilot-coding-agent/extending-copilot-coding-agent-with-skills  
  重点看：项目级 `.agents/skills` 结构、`SKILL.md` 触发方式。

- addyosmani/agent-skills  
  https://github.com/addyosmani/agent-skills  
  重点看：多个 workflow skills 如何拆分，meta-skill 如何做发现和组合。

- awesome-claude-code  
  https://github.com/hesreallyhim/awesome-claude-code  
  重点看：社区里 hooks、agents、commands、skills 的组合形态。

- awesome-claude-code-workflows  
  https://github.com/ithiria894/awesome-claude-code-workflows  
  重点看：workflow recipes 如何把规则、hooks、skills、agents 串起来。

## 面试式追问 / 项目深挖

- DeepWiki Project Deep Dive  
  https://deepwiki.com/taocao/ai-engineering-field-guide/3.5-project-deep-dive  
  重点看：项目经历如何从背景、角色、决策、结果继续追问。

- JavaGuide 后端面试准备计划  
  https://javaguide.cn/interview-preparation/backend-interview-plan.html  
  重点看：项目经历、八股、场景题如何组合准备。

- Cornell AppDev Backend Interview Guide  
  https://www.cornellappdev.com/apply/interview-guides/backend  
  重点看：后端面试如何贴近真实工作流和系统设计。

- PrepPilot Project Walkthrough Interview Guide  
  https://usepreppilot.com/blog/project-walkthrough-interview-guide  
  重点看：如何讲项目上下文、个人贡献、技术取舍和后续追问。

## Go Web / 后端基础

- Go `net/http` package  
  https://pkg.go.dev/net/http  
  重点看：`Server`、`Handler`、`ServeMux`、请求响应模型。

- Go by Example: HTTP Servers  
  https://gobyexample.com/http-servers  
  重点看：最小 HTTP server 和 handler 写法。

- Gin 官方文档  
  https://gin-gonic.com/en/docs/  
  重点看：routing、middleware、binding、error handling。

- MDN HTTP Overview  
  https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Overview  
  重点看：HTTP 请求/响应、headers、状态码和 Web 架构背景。

## 阅读建议

1. 先看 Skills / Agent 编排，理解为什么本仓库拆成小 skill。
2. 再看面试式追问资料，只学提问方式，不背题。
3. 做 Go Web issue 时，优先回到 `net/http`、Gin、MDN 这些基础资料。
4. 每次只带着一个 issue 或一个代码链路去读，不做泛泛阅读。
