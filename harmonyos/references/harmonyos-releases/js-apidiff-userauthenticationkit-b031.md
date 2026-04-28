---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-userauthenticationkit-b031
title: User Authentication Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.0(12) > OS平台能力 > API变更清单 > HarmonyOS NEXT Developer Beta2引入的API > User Authentication Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:36:47+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:e1ca8b7cae1e5d55fe22a2fb0026420dacf721bc772798ff8a20a89e2e5aea69
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 错误码变更 | 类名：userAuth；  API声明：function getAvailableStatus(authType: UserAuthType, authTrustLevel: AuthTrustLevel): void;  差异内容：12500002,12500005,12500006,12500010,201,401 | 类名：userAuth；  API声明：function getAvailableStatus(authType: UserAuthType, authTrustLevel: AuthTrustLevel): void;  差异内容：12500002,12500005,12500006,12500010,12500013,201,401 | api/@ohos.userIAM.userAuth.d.ts |
| 错误码变更 | 类名：UserAuthInstance；  API声明：start(): void;  差异内容：12500001,12500002,12500003,12500004,12500005,12500006,12500007,12500009,12500010,12500011,201,401 | 类名：UserAuthInstance；  API声明：start(): void;  差异内容：12500001,12500002,12500003,12500004,12500005,12500006,12500007,12500009,12500010,12500011,12500013,201,401 | api/@ohos.userIAM.userAuth.d.ts |
| 新增API | NA | 类名：UserAuthResultCode；  API声明：PIN\_EXPIRED = 12500013  差异内容：PIN\_EXPIRED = 12500013 | api/@ohos.userIAM.userAuth.d.ts |
