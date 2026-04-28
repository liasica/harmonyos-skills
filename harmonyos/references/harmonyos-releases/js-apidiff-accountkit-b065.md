---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-accountkit-b065
title: Account Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.0(12) > OS平台能力 > API变更清单 > HarmonyOS NEXT Beta引入的API > Account Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:36:14+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:6bc87f1fc4038e552cebe9168c01233c9d55adb1777726f4559a188d3e379bff
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 错误码变更 | 类名：minorsProtection；  API声明：function leadToTurnOnMinorsMode(context: common.Context): Promise<void>;  差异内容：1001502009,1009900003,1009900005,1009900007,401 | 类名：minorsProtection；  API声明：function leadToTurnOnMinorsMode(context: common.Context): Promise<void>;  差异内容：1001502009,1009900003,1009900005,1009900007,1009900011,401 | api/@hms.core.account.minorsProtection.d.ts |
| 错误码变更 | 类名：minorsProtection；  API声明：function leadToTurnOffMinorsMode(context: common.Context): Promise<void>;  差异内容：1001502009,1009900003,1009900006,401 | 类名：minorsProtection；  API声明：function leadToTurnOffMinorsMode(context: common.Context): Promise<void>;  差异内容：1001502009,1009900003,1009900006,1009900011,401 | api/@hms.core.account.minorsProtection.d.ts |
| 新增API | NA | 类名：minorsProtection；  API声明：function supportMinorsMode(): boolean;  差异内容：function supportMinorsMode(): boolean; | api/@hms.core.account.minorsProtection.d.ts |
| 新增API | NA | 类名：MinorsModeErrorCode；  API声明：SERVICE\_NOT\_AVAILABLE = 1009900011  差异内容：SERVICE\_NOT\_AVAILABLE = 1009900011 | api/@hms.core.account.minorsProtection.d.ts |
| 新增API | NA | 类名：LoginWithHuaweiIDButtonParams；  API声明：loginButtonTextType?: LoginButtonTextType;  差异内容：loginButtonTextType?: LoginButtonTextType; | api/@hms.core.account.LoginComponent.d.ets |
| 新增API | NA | 类名：loginComponentManager；  API声明： export enum LoginButtonTextType  差异内容： export enum LoginButtonTextType | api/@hms.core.account.LoginComponent.d.ets |
| 新增API | NA | 类名：LoginButtonTextType；  API声明：QUICK\_LOGIN = 0  差异内容：QUICK\_LOGIN = 0 | api/@hms.core.account.LoginComponent.d.ets |
| 新增API | NA | 类名：LoginButtonTextType；  API声明：QUICK\_REGISTRATION = 1  差异内容：QUICK\_REGISTRATION = 1 | api/@hms.core.account.LoginComponent.d.ets |
| 新增API | NA | 类名：RealNameErrorCode；  API声明：REAL\_NAME\_VERIFICATION\_ERROR = 1002500009  差异内容：REAL\_NAME\_VERIFICATION\_ERROR = 1002500009 | api/@hms.core.account.realname.d.ts |
