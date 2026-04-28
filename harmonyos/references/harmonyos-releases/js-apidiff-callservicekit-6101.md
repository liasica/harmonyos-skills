---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-callservicekit-6101
title: Call Service Kit
breadcrumb: 版本说明 > HarmonyOS 6.1.0(23) > OS平台能力 > API变更清单 > 6.1.0(23) Beta1引入的变更 > Call Service Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:33:27+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:7c7eee368328095e11464f17d754864304b2386443e27326444c3e7a69dcc537
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：global；  API声明：declare namespace numberIdentify  差异内容：declare namespace numberIdentify | api/@hms.telephony.numberIdentify.d.ts |
| 新增API | NA | 类名：numberIdentify；  API声明：function isSupportEnterpriseNumberIdentify(context: Context): Promise<boolean>;  差异内容：function isSupportEnterpriseNumberIdentify(context: Context): Promise<boolean>; | api/@hms.telephony.numberIdentify.d.ts |
| 新增API | NA | 类名：numberIdentify；  API声明：function queryNumberIdentifySwitchState(context: Context): SwitchState;  差异内容：function queryNumberIdentifySwitchState(context: Context): SwitchState; | api/@hms.telephony.numberIdentify.d.ts |
| 新增API | NA | 类名：numberIdentify；  API声明：interface SwitchState  差异内容：interface SwitchState | api/@hms.telephony.numberIdentify.d.ts |
| 新增API | NA | 类名：SwitchState；  API声明：isNumberIdentifyEnabled: boolean;  差异内容：isNumberIdentifyEnabled: boolean; | api/@hms.telephony.numberIdentify.d.ts |
| 新增API | NA | 类名：SwitchState；  API声明：isApplicationNumberIdentifyEnabled: boolean;  差异内容：isApplicationNumberIdentifyEnabled: boolean; | api/@hms.telephony.numberIdentify.d.ts |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：api@hms.telephony.numberIdentify.d.ts  差异内容：CallServiceKit | api/@hms.telephony.numberIdentify.d.ts |
