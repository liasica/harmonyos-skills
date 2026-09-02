---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-agentframeworkkit-7003
title: Agent Framework Kit
breadcrumb: 版本说明 > 最新版本(26.0.0) > 26.0.0 > OS平台能力 > API变更清单 > 26.0.0 Release引入的API > Agent Framework Kit
category: harmonyos-releases
scraped_at: 2026-09-02T14:49:02+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:638ffedb61b6bcc6d9e9648cc3ff93ab6f84ec1794cb76f8ee9570ef79163e0d
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 删除API | 类名：global；  API声明：export enum AgentOperation  差异内容：export enum AgentOperation | NA | api/@hms.ai.A2A.d.ts |
| 删除API | 类名：AgentOperation；  API声明：EXECUTE = 0  差异内容：EXECUTE = 0 | NA | api/@hms.ai.A2A.d.ts |
| 删除API | 类名：AgentOperation；  API声明：CANCEL = 1  差异内容：CANCEL = 1 | NA | api/@hms.ai.A2A.d.ts |
| 删除API | 类名：AgentOperation；  API声明：CLEAR\_CONTEXT = 2  差异内容：CLEAR\_CONTEXT = 2 | NA | api/@hms.ai.A2A.d.ts |
| 删除API | 类名：AgentOperation；  API声明：PERCEPTION\_SUGGEST = 3  差异内容：PERCEPTION\_SUGGEST = 3 | NA | api/@hms.ai.A2A.d.ts |
| 删除API | 类名：RequestContext；  API声明：getClientSessionId(): string | undefined;  差异内容：getClientSessionId(): string | undefined; | NA | api/@hms.ai.A2A.d.ts |
| 函数变更 | 类名：global；  API声明：export type OnDataCallback = (method: AgentOperation, context: RequestContext) => void;  差异内容：method: AgentOperation | 类名：global；  API声明：export type OnDataCallback = (method: string, context: RequestContext) => void;  差异内容：method: string | api/@hms.ai.A2A.d.ts |
