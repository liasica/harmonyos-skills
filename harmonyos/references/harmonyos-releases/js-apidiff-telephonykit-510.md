---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-telephonykit-510
title: Telephony Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.1.0(18) > OS平台能力 > API变更清单 > Telephony Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:35:16+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:d777569bce12c2f3de10bf84e2549c36d29529725074157bd9c9ff2a0f1a7778
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：global；  API声明：declare namespace eSIM  差异内容：declare namespace eSIM | api/@ohos.telephony.esim.d.ts |
| 新增API | NA | 类名：eSIM；  API声明：function isSupported(slotId: number): boolean;  差异内容：function isSupported(slotId: number): boolean; | api/@ohos.telephony.esim.d.ts |
| 新增API | NA | 类名：eSIM；  API声明：function addProfile(profile: DownloadableProfile): Promise<boolean>;  差异内容：function addProfile(profile: DownloadableProfile): Promise<boolean>; | api/@ohos.telephony.esim.d.ts |
| 新增API | NA | 类名：eSIM；  API声明：export interface DownloadableProfile  差异内容：export interface DownloadableProfile | api/@ohos.telephony.esim.d.ts |
| 新增API | NA | 类名：DownloadableProfile；  API声明：activationCode: string;  差异内容：activationCode: string; | api/@ohos.telephony.esim.d.ts |
| 新增API | NA | 类名：DownloadableProfile；  API声明：confirmationCode?: string;  差异内容：confirmationCode?: string; | api/@ohos.telephony.esim.d.ts |
| 新增API | NA | 类名：DownloadableProfile；  API声明：carrierName?: string;  差异内容：carrierName?: string; | api/@ohos.telephony.esim.d.ts |
| 新增API | NA | 类名：DownloadableProfile；  API声明：accessRules?: Array<AccessRule>;  差异内容：accessRules?: Array<AccessRule>; | api/@ohos.telephony.esim.d.ts |
| 新增API | NA | 类名：radio；  API声明：function getRadioTechSync(slotId: number): NetworkRadioTech;  差异内容：function getRadioTechSync(slotId: number): NetworkRadioTech; | api/@ohos.telephony.radio.d.ts |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：api@ohos.telephony.esim.d.ts  差异内容：TelephonyKit | api/@ohos.telephony.esim.d.ts |
