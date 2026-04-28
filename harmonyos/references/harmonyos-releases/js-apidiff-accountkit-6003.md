---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-accountkit-6003
title: Account Kit
breadcrumb: 版本说明 > HarmonyOS 6.0.0(20) > OS平台能力 > API变更清单 > 6.0.0(20) Beta3引入的API > Account Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:34:11+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:567cdc285ce88386a736bdfb28524c1474cd207bfd01c87adb294877f8c0437a
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| API从不支持元服务到支持元服务 | 类名：AuthorizationWithHuaweiIDCredential；  API声明：readonly avatarUri?: string;  差异内容：NA | 类名：AuthorizationWithHuaweiIDCredential；  API声明：readonly avatarUri?: string;  差异内容：atomicservice | api/@hms.core.authentication.d.ts |
| API从不支持元服务到支持元服务 | 类名：AuthorizationWithHuaweiIDCredential；  API声明：readonly nickName?: string;  差异内容：NA | 类名：AuthorizationWithHuaweiIDCredential；  API声明：readonly nickName?: string;  差异内容：atomicservice | api/@hms.core.authentication.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：LoginPanelParams；  API声明：securityVerification?: boolean;  差异内容：securityVerification?: boolean; | api/@hms.core.account.LoginComponent.d.ets |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：HuaweiIDCredential；  API声明：readonly enableSecurityVerification?: boolean;  差异内容：readonly enableSecurityVerification?: boolean; | api/@hms.core.account.LoginComponent.d.ets |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：LoginWithHuaweiIDButtonParams；  API声明：securityVerification?: boolean;  差异内容：securityVerification?: boolean; | api/@hms.core.account.LoginComponent.d.ets |
