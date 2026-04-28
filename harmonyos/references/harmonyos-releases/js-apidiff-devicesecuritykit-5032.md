---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-devicesecuritykit-5032
title: Device Security Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.3(15) > OS平台能力 > API变更清单 > HarmonyOS 5.0.3(15) Beta2引入的API > Device Security Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:35:34+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:3c06d79a73c80e798a12e24bdb84e83d4863ea1923ebbac6f412ea29992c1020
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：global；  API声明： declare namespace antifraudPicker  差异内容： declare namespace antifraudPicker | api/@hms.security.antifraudPicker.d.ts |
| 新增API | NA | 类名：antifraudPicker；  API声明： interface AntifraudMessageOptions  差异内容： interface AntifraudMessageOptions | api/@hms.security.antifraudPicker.d.ts |
| 新增API | NA | 类名：AntifraudMessageOptions；  API声明：maxSelectNumber?: number;  差异内容：maxSelectNumber?: number; | api/@hms.security.antifraudPicker.d.ts |
| 新增API | NA | 类名：antifraudPicker；  API声明： interface SingleAntifraudMessageInfo  差异内容： interface SingleAntifraudMessageInfo | api/@hms.security.antifraudPicker.d.ts |
| 新增API | NA | 类名：SingleAntifraudMessageInfo；  API声明：senderNumber: string;  差异内容：senderNumber: string; | api/@hms.security.antifraudPicker.d.ts |
| 新增API | NA | 类名：SingleAntifraudMessageInfo；  API声明：receivingTime: number;  差异内容：receivingTime: number; | api/@hms.security.antifraudPicker.d.ts |
| 新增API | NA | 类名：SingleAntifraudMessageInfo；  API声明：messageContent: string;  差异内容：messageContent: string; | api/@hms.security.antifraudPicker.d.ts |
| 新增API | NA | 类名：SingleAntifraudMessageInfo；  API声明：senderName: string;  差异内容：senderName: string; | api/@hms.security.antifraudPicker.d.ts |
| 新增API | NA | 类名：SingleAntifraudMessageInfo；  API声明：senderPlace: string;  差异内容：senderPlace: string; | api/@hms.security.antifraudPicker.d.ts |
| 新增API | NA | 类名：SingleAntifraudMessageInfo；  API声明：messageType: string;  差异内容：messageType: string; | api/@hms.security.antifraudPicker.d.ts |
| 新增API | NA | 类名：SingleAntifraudMessageInfo；  API声明：mmsSubject?: string;  差异内容：mmsSubject?: string; | api/@hms.security.antifraudPicker.d.ts |
| 新增API | NA | 类名：SingleAntifraudMessageInfo；  API声明：mmsAttachments?: MmsAttachmentInfo[];  差异内容：mmsAttachments?: MmsAttachmentInfo[]; | api/@hms.security.antifraudPicker.d.ts |
| 新增API | NA | 类名：antifraudPicker；  API声明： interface MmsAttachmentInfo  差异内容： interface MmsAttachmentInfo | api/@hms.security.antifraudPicker.d.ts |
| 新增API | NA | 类名：MmsAttachmentInfo；  API声明：attachmentType: number;  差异内容：attachmentType: number; | api/@hms.security.antifraudPicker.d.ts |
| 新增API | NA | 类名：MmsAttachmentInfo；  API声明：uri: string;  差异内容：uri: string; | api/@hms.security.antifraudPicker.d.ts |
| 新增API | NA | 类名：antifraudPicker；  API声明： interface AntifraudMessageResult  差异内容： interface AntifraudMessageResult | api/@hms.security.antifraudPicker.d.ts |
| 新增API | NA | 类名：AntifraudMessageResult；  API声明：messageInfo: SingleAntifraudMessageInfo[];  差异内容：messageInfo: SingleAntifraudMessageInfo[]; | api/@hms.security.antifraudPicker.d.ts |
| 新增API | NA | 类名：antifraudPicker；  API声明： interface SingleAntifraudCallLogInfo  差异内容： interface SingleAntifraudCallLogInfo | api/@hms.security.antifraudPicker.d.ts |
| 新增API | NA | 类名：SingleAntifraudCallLogInfo；  API声明：callerNumber: string;  差异内容：callerNumber: string; | api/@hms.security.antifraudPicker.d.ts |
| 新增API | NA | 类名：SingleAntifraudCallLogInfo；  API声明：receivingTime: number;  差异内容：receivingTime: number; | api/@hms.security.antifraudPicker.d.ts |
| 新增API | NA | 类名：SingleAntifraudCallLogInfo；  API声明：callLogType: number;  差异内容：callLogType: number; | api/@hms.security.antifraudPicker.d.ts |
| 新增API | NA | 类名：SingleAntifraudCallLogInfo；  API声明：callerName: string;  差异内容：callerName: string; | api/@hms.security.antifraudPicker.d.ts |
| 新增API | NA | 类名：SingleAntifraudCallLogInfo；  API声明：callDuration: number;  差异内容：callDuration: number; | api/@hms.security.antifraudPicker.d.ts |
| 新增API | NA | 类名：antifraudPicker；  API声明： interface AntifraudCallLogResult  差异内容： interface AntifraudCallLogResult | api/@hms.security.antifraudPicker.d.ts |
| 新增API | NA | 类名：AntifraudCallLogResult；  API声明：callLogInfo: SingleAntifraudCallLogInfo[];  差异内容：callLogInfo: SingleAntifraudCallLogInfo[]; | api/@hms.security.antifraudPicker.d.ts |
| 新增API | NA | 类名：antifraudPicker；  API声明： interface AntifraudCallLogOptions  差异内容： interface AntifraudCallLogOptions | api/@hms.security.antifraudPicker.d.ts |
| 新增API | NA | 类名：AntifraudCallLogOptions；  API声明：maxSelectNumber?: number;  差异内容：maxSelectNumber?: number; | api/@hms.security.antifraudPicker.d.ts |
| 新增API | NA | 类名：antifraudPicker；  API声明：function selectFraudMessage(context: common.Context, options?: AntifraudMessageOptions): Promise<AntifraudMessageResult>;  差异内容：function selectFraudMessage(context: common.Context, options?: AntifraudMessageOptions): Promise<AntifraudMessageResult>; | api/@hms.security.antifraudPicker.d.ts |
| 新增API | NA | 类名：antifraudPicker；  API声明：function selectFraudCallLog(context: common.Context, options?: AntifraudCallLogOptions): Promise<AntifraudCallLogResult>;  差异内容：function selectFraudCallLog(context: common.Context, options?: AntifraudCallLogOptions): Promise<AntifraudCallLogResult>; | api/@hms.security.antifraudPicker.d.ts |
| kit变更 | NA | DeviceSecurityKit | api/@hms.security.antifraudPicker.d.ts |
