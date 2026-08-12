# Go Web 学习主题图谱

这个图谱供 `concept-teacher` 把知识点回收到项目链路里。

## 请求与协议

- HTTP 请求/响应：方法、路径、Header、Body、状态码。
- TCP 三次握手：建立可靠连接的前置过程；讲 HTTP 前可作为网络背景，不要喧宾夺主。
- TLS/HTTPS：证书、加密、反向代理和 Cookie Secure 的关系。
- CORS：浏览器跨源策略；必须和 credentials、Cookie、服务端响应头一起讲。

## Gin / Web 框架

- 路由：URL 和 handler 的映射。
- Handler：解析输入、调用 service、返回响应，不承载业务细节。
- Middleware：鉴权、日志、CORS、恢复、限流等横切逻辑。
- Context：请求级状态、超时、取消、参数传递；不要把它当全局容器。

## Go 语言基础

- 闭包：函数捕获外部变量；常见于 middleware、handler factory、回调封装。
- 回调：把行为作为参数交给另一个函数；常见于遍历、异步、钩子、框架扩展点。
- interface：面向行为抽象；先看调用方需要什么，不先造大接口。
- error：显式错误返回；要讲错误在哪一层转换成业务响应。
- goroutine/channel：并发工具；先讲生命周期、取消、背压，再讲写法。

## 数据与持久化

- DTO：接口传输对象，服务页面/API 场景，不等同数据库实体。
- Entity/Model：持久化结构，服务数据库映射。
- Repository：显式查询和写入，不放业务流程。
- Transaction：多个写操作的一致性边界。
- Index：围绕过滤、排序、join 设计，不是“慢就加索引”。

## 登录与安全

- session + cookie：服务端保存登录态，客户端保存会话标识。
- HttpOnly / Secure / SameSite：分别约束脚本读取、明文传输、跨站携带。
- CSRF：状态变更接口要关注。
- 权限：公开接口和管理接口分层，服务端必须再次校验。

## 性能与部署

- 缓存：先判断读写模式、失效策略和一致性代价。
- 降级/重试/超时：先定义失败结果，不盲目加中间件。
- Docker / Compose：统一环境，不替代部署设计。
- Nginx/反代：HTTPS、静态资源、转发头、Cookie 域要一起看。
