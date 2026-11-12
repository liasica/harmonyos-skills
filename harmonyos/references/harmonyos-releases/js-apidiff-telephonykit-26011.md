---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-telephonykit-26011
title: Telephony Kit
breadcrumb: 版本说明 > 最新版本(26.0.1) > 26.0.1 > OS平台能力 > API变更清单 > Telephony Kit
category: harmonyos-releases
scraped_at: 2026-11-12T09:49:54+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:e0720ca4abda92a7d803a7b838f88a9dce8309dd257f4dbcca40c2d05450c030
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增错误码 | 类名：sim；  API声明：function getSimAccountInfo(slotId: number, callback: AsyncCallback<IccAccountInfo>): void;  差异内容：NA | 类名：sim；  API声明：function getSimAccountInfo(slotId: number, callback: AsyncCallback<IccAccountInfo>): void;  差异内容：201 | api/@ohos.telephony.sim.d.ts |
| 新增错误码 | 类名：sim；  API声明：function getSimAccountInfo(slotId: number): Promise<IccAccountInfo>;  差异内容：NA | 类名：sim；  API声明：function getSimAccountInfo(slotId: number): Promise<IccAccountInfo>;  差异内容：201 | api/@ohos.telephony.sim.d.ts |
| 新增API | NA | 类名：call；  API声明：function makeDirectCall(phoneNumber: string): Promise<void>;  差异内容：function makeDirectCall(phoneNumber: string): Promise<void>; | api/@ohos.telephony.call.d.ts |
| 新增API | NA | 类名：observer；  API声明：function onVoIPStateChange(callback: Callback<VoIPCallStateInfo>): void;  差异内容：function onVoIPStateChange(callback: Callback<VoIPCallStateInfo>): void; | api/@ohos.telephony.observer.d.ts |
| 新增API | NA | 类名：observer；  API声明：function offVoIPStateChange(callback?: Callback<VoIPCallStateInfo>): void;  差异内容：function offVoIPStateChange(callback?: Callback<VoIPCallStateInfo>): void; | api/@ohos.telephony.observer.d.ts |
| 新增API | NA | 类名：observer；  API声明：export interface VoIPCallStateInfo  差异内容：export interface VoIPCallStateInfo | api/@ohos.telephony.observer.d.ts |
| 新增API | NA | 类名：VoIPCallStateInfo；  API声明：appName: string;  差异内容：appName: string; | api/@ohos.telephony.observer.d.ts |
| 新增API | NA | 类名：VoIPCallStateInfo；  API声明：contactName: string;  差异内容：contactName: string; | api/@ohos.telephony.observer.d.ts |
| 新增API | NA | 类名：VoIPCallStateInfo；  API声明：callType: VoIPCallType;  差异内容：callType: VoIPCallType; | api/@ohos.telephony.observer.d.ts |
| 新增API | NA | 类名：VoIPCallStateInfo；  API声明：callState: VoIPCallState;  差异内容：callState: VoIPCallState; | api/@ohos.telephony.observer.d.ts |
| 新增API | NA | 类名：VoIPCallStateInfo；  API声明：isVoiceAnswerSupported: boolean;  差异内容：isVoiceAnswerSupported: boolean; | api/@ohos.telephony.observer.d.ts |
| 新增API | NA | 类名：observer；  API声明：export enum VoIPCallType  差异内容：export enum VoIPCallType | api/@ohos.telephony.observer.d.ts |
| 新增API | NA | 类名：VoIPCallType；  API声明：VOICE = 0  差异内容：VOICE = 0 | api/@ohos.telephony.observer.d.ts |
| 新增API | NA | 类名：VoIPCallType；  API声明：VIDEO = 1  差异内容：VIDEO = 1 | api/@ohos.telephony.observer.d.ts |
| 新增API | NA | 类名：observer；  API声明：export enum VoIPCallState  差异内容：export enum VoIPCallState | api/@ohos.telephony.observer.d.ts |
| 新增API | NA | 类名：VoIPCallState；  API声明：IDLE = 0  差异内容：IDLE = 0 | api/@ohos.telephony.observer.d.ts |
| 新增API | NA | 类名：VoIPCallState；  API声明：INCOMING = 1  差异内容：INCOMING = 1 | api/@ohos.telephony.observer.d.ts |
| 新增API | NA | 类名：VoIPCallState；  API声明：OUTGOING = 2  差异内容：OUTGOING = 2 | api/@ohos.telephony.observer.d.ts |
| 新增API | NA | 类名：VoIPCallState；  API声明：DIALING = 3  差异内容：DIALING = 3 | api/@ohos.telephony.observer.d.ts |
| 新增API | NA | 类名：VoIPCallState；  API声明：ANSWERED = 4  差异内容：ANSWERED = 4 | api/@ohos.telephony.observer.d.ts |
| 新增API | NA | 类名：VoIPCallState；  API声明：ACTIVE = 5  差异内容：ACTIVE = 5 | api/@ohos.telephony.observer.d.ts |
| 新增API | NA | 类名：VoIPCallState；  API声明：HOLDING = 6  差异内容：HOLDING = 6 | api/@ohos.telephony.observer.d.ts |
| 新增API | NA | 类名：VoIPCallState；  API声明：DISCONNECTING = 7  差异内容：DISCONNECTING = 7 | api/@ohos.telephony.observer.d.ts |
| 新增API | NA | 类名：VoIPCallState；  API声明：DISCONNECTED = 8  差异内容：DISCONNECTED = 8 | api/@ohos.telephony.observer.d.ts |
