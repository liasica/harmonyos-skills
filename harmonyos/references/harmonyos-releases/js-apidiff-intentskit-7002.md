---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-intentskit-7002
title: Intents Kit
breadcrumb: 版本说明 > 最新版本(26.0.0) > 26.0.0 > OS平台能力 > API变更清单 > 26.0.0 Beta2引入的API > Intents Kit
category: harmonyos-releases
scraped_at: 2026-09-02T14:49:03+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:1a4d43240db2a2772210f3ef5bb5c22069bf911dcbb94f19a55ec44914e9a991
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增错误码 | 类名：insightIntent；  API声明：function shareIntent(context: common.BaseContext, intents: InsightIntent[], callback: AsyncCallback<void>): void;  差异内容：NA | 类名：insightIntent；  API声明：function shareIntent(context: common.BaseContext, intents: InsightIntent[], callback: AsyncCallback<void>): void;  差异内容：1000101102,1000101103 | api/@hms.ai.insightIntent.d.ts |
| 新增错误码 | 类名：insightIntent；  API声明：function shareIntent(context: common.BaseContext, intents: InsightIntent[]): Promise<void>;  差异内容：NA | 类名：insightIntent；  API声明：function shareIntent(context: common.BaseContext, intents: InsightIntent[]): Promise<void>;  差异内容：1000101102,1000101103 | api/@hms.ai.insightIntent.d.ts |
| 新增错误码 | 类名：insightIntent；  API声明：function getSid(context: common.BaseContext, renew: boolean): Promise<string>;  差异内容：NA | 类名：insightIntent；  API声明：function getSid(context: common.BaseContext, renew: boolean): Promise<string>;  差异内容：1000101103 | api/@hms.ai.insightIntent.d.ts |
