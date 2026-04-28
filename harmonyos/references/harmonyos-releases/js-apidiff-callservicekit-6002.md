---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-callservicekit-6002
title: Call Service Kit
breadcrumb: 版本说明 > HarmonyOS 6.0.0(20) > OS平台能力 > API变更清单 > 6.0.0(20) Beta2引入的API > Call Service Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:34:27+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:06e8fb42d9de852d54324e70c2d3e0b6b29581415aa501ed940df15ecc264030
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| syscap变更 | 类名：global；  API声明：export interface CallerInfo  差异内容：SystemCapability.Telephony.CallManager | 类名：global；  API声明：export interface CallerInfo  差异内容：SystemCapability.Telephony.NumberIdentifyService | api/@hms.telephony.CallerInfoQueryExtensionAbility.d.ts |
| syscap变更 | 类名：CallerInfo；  API声明：contactName: string;  差异内容：SystemCapability.Telephony.CallManager | 类名：CallerInfo；  API声明：contactName: string;  差异内容：SystemCapability.Telephony.NumberIdentifyService | api/@hms.telephony.CallerInfoQueryExtensionAbility.d.ts |
| syscap变更 | 类名：CallerInfo；  API声明：employeeId?: string;  差异内容：SystemCapability.Telephony.CallManager | 类名：CallerInfo；  API声明：employeeId?: string;  差异内容：SystemCapability.Telephony.NumberIdentifyService | api/@hms.telephony.CallerInfoQueryExtensionAbility.d.ts |
| syscap变更 | 类名：CallerInfo；  API声明：department?: string;  差异内容：SystemCapability.Telephony.CallManager | 类名：CallerInfo；  API声明：department?: string;  差异内容：SystemCapability.Telephony.NumberIdentifyService | api/@hms.telephony.CallerInfoQueryExtensionAbility.d.ts |
| syscap变更 | 类名：CallerInfo；  API声明：position?: string;  差异内容：SystemCapability.Telephony.CallManager | 类名：CallerInfo；  API声明：position?: string;  差异内容：SystemCapability.Telephony.NumberIdentifyService | api/@hms.telephony.CallerInfoQueryExtensionAbility.d.ts |
| syscap变更 | 类名：global；  API声明：export default class CallerInfoQueryExtensionAbility  差异内容：SystemCapability.Telephony.CallManager | 类名：global；  API声明：export default class CallerInfoQueryExtensionAbility  差异内容：SystemCapability.Telephony.NumberIdentifyService | api/@hms.telephony.CallerInfoQueryExtensionAbility.d.ts |
| syscap变更 | 类名：CallerInfoQueryExtensionAbility；  API声明：context: CallerInfoQueryExtensionContext;  差异内容：SystemCapability.Telephony.CallManager | 类名：CallerInfoQueryExtensionAbility；  API声明：context: CallerInfoQueryExtensionContext;  差异内容：SystemCapability.Telephony.NumberIdentifyService | api/@hms.telephony.CallerInfoQueryExtensionAbility.d.ts |
| syscap变更 | 类名：CallerInfoQueryExtensionAbility；  API声明：onQueryCallerInfo(phoneNumber: string): Promise<CallerInfo>;  差异内容：SystemCapability.Telephony.CallManager | 类名：CallerInfoQueryExtensionAbility；  API声明：onQueryCallerInfo(phoneNumber: string): Promise<CallerInfo>;  差异内容：SystemCapability.Telephony.NumberIdentifyService | api/@hms.telephony.CallerInfoQueryExtensionAbility.d.ts |
| syscap变更 | 类名：global；  API声明：export default class CallerInfoQueryExtensionContext  差异内容：SystemCapability.Telephony.CallManager | 类名：global；  API声明：export default class CallerInfoQueryExtensionContext  差异内容：SystemCapability.Telephony.NumberIdentifyService | api/@hms.telephony.CallerInfoQueryExtensionContext.d.ts |
