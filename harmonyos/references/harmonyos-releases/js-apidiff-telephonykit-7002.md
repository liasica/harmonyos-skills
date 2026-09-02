---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-telephonykit-7002
title: Telephony Kit
breadcrumb: 版本说明 > 最新版本(26.0.0) > 26.0.0 > OS平台能力 > API变更清单 > 26.0.0 Beta2引入的API > Telephony Kit
category: harmonyos-releases
scraped_at: 2026-09-02T14:49:04+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:4b355b739b3826e8f94d28bde204c7295fec3b74382707d254d451272a962bf8
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：call；  API声明：function makeCallWithToken(phoneNumber: string, options?: MakeCallOptions): Promise<string>;  差异内容：function makeCallWithToken(phoneNumber: string, options?: MakeCallOptions): Promise<string>; | api/@ohos.telephony.call.d.ts |
| 新增API | NA | 类名：call；  API声明：export enum CallTransferType  差异内容：export enum CallTransferType | api/@ohos.telephony.call.d.ts |
| 新增API | NA | 类名：CallTransferType；  API声明：TRANSFER\_TYPE\_UNCONDITIONAL = 0  差异内容：TRANSFER\_TYPE\_UNCONDITIONAL = 0 | api/@ohos.telephony.call.d.ts |
| 新增API | NA | 类名：CallTransferType；  API声明：TRANSFER\_TYPE\_BUSY = 1  差异内容：TRANSFER\_TYPE\_BUSY = 1 | api/@ohos.telephony.call.d.ts |
| 新增API | NA | 类名：CallTransferType；  API声明：TRANSFER\_TYPE\_NO\_REPLY = 2  差异内容：TRANSFER\_TYPE\_NO\_REPLY = 2 | api/@ohos.telephony.call.d.ts |
| 新增API | NA | 类名：CallTransferType；  API声明：TRANSFER\_TYPE\_NOT\_REACHABLE = 3  差异内容：TRANSFER\_TYPE\_NOT\_REACHABLE = 3 | api/@ohos.telephony.call.d.ts |
| 新增API | NA | 类名：MakeCallOptions；  API声明：isCustomAccessibility?: boolean;  差异内容：isCustomAccessibility?: boolean; | api/@ohos.telephony.call.d.ts |
| 新增API | NA | 类名：call；  API声明：export interface CallTransferResult  差异内容：export interface CallTransferResult | api/@ohos.telephony.call.d.ts |
| 新增API | NA | 类名：CallTransferResult；  API声明：status: TransferStatus;  差异内容：status: TransferStatus; | api/@ohos.telephony.call.d.ts |
| 新增API | NA | 类名：CallTransferResult；  API声明：startHour: number;  差异内容：startHour: number; | api/@ohos.telephony.call.d.ts |
| 新增API | NA | 类名：CallTransferResult；  API声明：startMinute: number;  差异内容：startMinute: number; | api/@ohos.telephony.call.d.ts |
| 新增API | NA | 类名：CallTransferResult；  API声明：endHour: number;  差异内容：endHour: number; | api/@ohos.telephony.call.d.ts |
| 新增API | NA | 类名：CallTransferResult；  API声明：endMinute: number;  差异内容：endMinute: number; | api/@ohos.telephony.call.d.ts |
| 新增API | NA | 类名：call；  API声明：export enum TransferStatus  差异内容：export enum TransferStatus | api/@ohos.telephony.call.d.ts |
| 新增API | NA | 类名：TransferStatus；  API声明：TRANSFER\_DISABLE = 0  差异内容：TRANSFER\_DISABLE = 0 | api/@ohos.telephony.call.d.ts |
| 新增API | NA | 类名：TransferStatus；  API声明：TRANSFER\_ENABLE = 1  差异内容：TRANSFER\_ENABLE = 1 | api/@ohos.telephony.call.d.ts |
| 新增API | NA | 类名：data；  API声明：function showSystemApnSettings(context: Context): Promise<void>;  差异内容：function showSystemApnSettings(context: Context): Promise<void>; | api/@ohos.telephony.data.d.ts |
| 新增API | NA | 类名：observer；  API声明：function onCommunicationStateChange(callback: Callback<boolean>, options?: ObserverOptions): void;  差异内容：function onCommunicationStateChange(callback: Callback<boolean>, options?: ObserverOptions): void; | api/@ohos.telephony.observer.d.ts |
| 新增API | NA | 类名：observer；  API声明：function offCommunicationStateChange(callback: Callback<boolean>, options?: ObserverOptions): void;  差异内容：function offCommunicationStateChange(callback: Callback<boolean>, options?: ObserverOptions): void; | api/@ohos.telephony.observer.d.ts |
