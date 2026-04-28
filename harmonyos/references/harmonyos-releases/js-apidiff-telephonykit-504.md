---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-telephonykit-504
title: Telephony Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.4(16) > OS平台能力 > API变更清单 > Telephony Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:35:28+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:a2db4560d24def9292e83738a9d520c5abd3b0168d60aac96f205cca170718f1
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：data；  API声明：function queryAllApns(): Promise<Array<ApnInfo>>;  差异内容：function queryAllApns(): Promise<Array<ApnInfo>>; | api/@ohos.telephony.data.d.ts |
| 新增API | NA | 类名：data；  API声明：function queryApnIds(apnInfo: ApnInfo): Promise<Array<number>>;  差异内容：function queryApnIds(apnInfo: ApnInfo): Promise<Array<number>>; | api/@ohos.telephony.data.d.ts |
| 新增API | NA | 类名：data；  API声明：function setPreferredApn(apnId: number): Promise<boolean>;  差异内容：function setPreferredApn(apnId: number): Promise<boolean>; | api/@ohos.telephony.data.d.ts |
| 新增API | NA | 类名：data；  API声明： interface ApnInfo  差异内容： interface ApnInfo | api/@ohos.telephony.data.d.ts |
| 新增API | NA | 类名：ApnInfo；  API声明：apnName: string;  差异内容：apnName: string; | api/@ohos.telephony.data.d.ts |
| 新增API | NA | 类名：ApnInfo；  API声明：apn: string;  差异内容：apn: string; | api/@ohos.telephony.data.d.ts |
| 新增API | NA | 类名：ApnInfo；  API声明：mcc: string;  差异内容：mcc: string; | api/@ohos.telephony.data.d.ts |
| 新增API | NA | 类名：ApnInfo；  API声明：mnc: string;  差异内容：mnc: string; | api/@ohos.telephony.data.d.ts |
| 新增API | NA | 类名：ApnInfo；  API声明：user?: string;  差异内容：user?: string; | api/@ohos.telephony.data.d.ts |
| 新增API | NA | 类名：ApnInfo；  API声明：type?: string;  差异内容：type?: string; | api/@ohos.telephony.data.d.ts |
| 新增API | NA | 类名：ApnInfo；  API声明：proxy?: string;  差异内容：proxy?: string; | api/@ohos.telephony.data.d.ts |
| 新增API | NA | 类名：ApnInfo；  API声明：mmsproxy?: string;  差异内容：mmsproxy?: string; | api/@ohos.telephony.data.d.ts |
| 删除API | 类名：global；  API声明： declare namespace eSIM  差异内容： declare namespace eSIM | NA | api/@ohos.telephony.esim.d.ts |
| 删除API | 类名：eSIM；  API声明：function isSupported(slotId: number): boolean;  差异内容：function isSupported(slotId: number): boolean; | NA | api/@ohos.telephony.esim.d.ts |
| 删除API | 类名：eSIM；  API声明：function addProfile(profile: DownloadableProfile): Promise<boolean>;  差异内容：function addProfile(profile: DownloadableProfile): Promise<boolean>; | NA | api/@ohos.telephony.esim.d.ts |
| kit变更 | TelephonyKit | NA | api/@ohos.telephony.esim.d.ts |
