---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-accountkit-6101
title: Account Kit
breadcrumb: 版本说明 > HarmonyOS 6.1.0(23) > OS平台能力 > API变更清单 > 6.1.0(23) Beta1引入的变更 > Account Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:33:22+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:3e01942a9ec81cd40785b7e9d225c09fdaf80675b24cbe0501a8d9a56ed8a089
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增错误码 | 类名：extendService；  API声明：function startAccountCenter(context: common.Context, callback: AsyncCallback<void>): void;  差异内容：NA | 类名：extendService；  API声明：function startAccountCenter(context: common.Context, callback: AsyncCallback<void>): void;  差异内容：1001600011 | api/@hms.core.account.extendservice.d.ts |
| 新增错误码 | 类名：extendService；  API声明：function startAccountCenter(context: common.Context): Promise<void>;  差异内容：NA | 类名：extendService；  API声明：function startAccountCenter(context: common.Context): Promise<void>;  差异内容：1001600011 | api/@hms.core.account.extendservice.d.ts |
| 新增API | NA | 类名：ExtendErrorCode；  API声明：DEVICE\_NOT\_SUPPORTED = 1001600011  差异内容：DEVICE\_NOT\_SUPPORTED = 1001600011 | api/@hms.core.account.extendservice.d.ts |
