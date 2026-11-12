---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-callservicekit-26011
title: Call Service Kit
breadcrumb: 版本说明 > 最新版本(26.0.1) > 26.0.1 > OS平台能力 > API变更清单 > Call Service Kit
category: harmonyos-releases
scraped_at: 2026-11-12T09:49:53+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:9199e6f53d62b9fb7ac55ab6c920d87979a151ec4049f1e56224b9fdabe128af
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：global；  API声明：declare namespace voipCallControl  差异内容：declare namespace voipCallControl | api/@hms.telephony.voipCallControl.d.ts |
| 新增API | NA | 类名：voipCallControl；  API声明：export enum VideoStateType  差异内容：export enum VideoStateType | api/@hms.telephony.voipCallControl.d.ts |
| 新增API | NA | 类名：VideoStateType；  API声明：TYPE\_VOICE = 0  差异内容：TYPE\_VOICE = 0 | api/@hms.telephony.voipCallControl.d.ts |
| 新增API | NA | 类名：VideoStateType；  API声明：TYPE\_VIDEO = 1  差异内容：TYPE\_VIDEO = 1 | api/@hms.telephony.voipCallControl.d.ts |
| 新增API | NA | 类名：voipCallControl；  API声明：function answerCall(videoState?: VideoStateType): Promise<void>;  差异内容：function answerCall(videoState?: VideoStateType): Promise<void>; | api/@hms.telephony.voipCallControl.d.ts |
| 新增API | NA | 类名：voipCallControl；  API声明：function rejectCall(): Promise<void>;  差异内容：function rejectCall(): Promise<void>; | api/@hms.telephony.voipCallControl.d.ts |
| 新增API | NA | 类名：voipCallControl；  API声明：function hangUpCall(): Promise<void>;  差异内容：function hangUpCall(): Promise<void>; | api/@hms.telephony.voipCallControl.d.ts |
| 新增API | NA | 类名：CallerInfoQueryExtensionAbility；  API声明：onQueryBusinessServiceDataWithProtocol(privacyPhoneNumber: Uint8Array, privacyProtocol: PrivacyProtocol): Promise<PrivacySearchResult>;  差异内容：onQueryBusinessServiceDataWithProtocol(privacyPhoneNumber: Uint8Array, privacyProtocol: PrivacyProtocol): Promise<PrivacySearchResult>; | api/@hms.telephony.CallerInfoQueryExtensionAbility.d.ts |
| 新增API | NA | 类名：BusinessServiceData；  API声明：carryout?: CarryoutData;  差异内容：carryout?: CarryoutData; | api/@hms.telephony.numberIdentify.d.ts |
| 新增API | NA | 类名：BusinessServiceType；  API声明：CARRYOUT = 1  差异内容：CARRYOUT = 1 | api/@hms.telephony.numberIdentify.d.ts |
| 新增API | NA | 类名：numberIdentify；  API声明：export interface CarryoutData  差异内容：export interface CarryoutData | api/@hms.telephony.numberIdentify.d.ts |
| 新增API | NA | 类名：CarryoutData；  API声明：customerName: string;  差异内容：customerName: string; | api/@hms.telephony.numberIdentify.d.ts |
| 新增API | NA | 类名：CarryoutData；  API声明：carryoutNumber: string;  差异内容：carryoutNumber: string; | api/@hms.telephony.numberIdentify.d.ts |
| 新增API | NA | 类名：CarryoutData；  API声明：carryoutMerchant: string;  差异内容：carryoutMerchant: string; | api/@hms.telephony.numberIdentify.d.ts |
| 新增API | NA | 类名：CarryoutData；  API声明：carryoutStatus: string;  差异内容：carryoutStatus: string; | api/@hms.telephony.numberIdentify.d.ts |
| 新增API | NA | 类名：CarryoutData；  API声明：carryoutStatusColor: StatusColor;  差异内容：carryoutStatusColor: StatusColor; | api/@hms.telephony.numberIdentify.d.ts |
| 新增API | NA | 类名：CarryoutData；  API声明：carryoutAddress: string;  差异内容：carryoutAddress: string; | api/@hms.telephony.numberIdentify.d.ts |
| 新增API | NA | 类名：CarryoutData；  API声明：carryoutTimeoutDescription: string;  差异内容：carryoutTimeoutDescription: string; | api/@hms.telephony.numberIdentify.d.ts |
| 新增API | NA | 类名：CarryoutData；  API声明：deepLinking: string;  差异内容：deepLinking: string; | api/@hms.telephony.numberIdentify.d.ts |
| 新增API | NA | 类名：numberIdentify；  API声明：export enum StatusColor  差异内容：export enum StatusColor | api/@hms.telephony.numberIdentify.d.ts |
| 新增API | NA | 类名：StatusColor；  API声明：BLUE = 0  差异内容：BLUE = 0 | api/@hms.telephony.numberIdentify.d.ts |
| 新增API | NA | 类名：StatusColor；  API声明：GREEN = 1  差异内容：GREEN = 1 | api/@hms.telephony.numberIdentify.d.ts |
| 新增API | NA | 类名：StatusColor；  API声明：RED = 2  差异内容：RED = 2 | api/@hms.telephony.numberIdentify.d.ts |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：api@hms.telephony.voipCallControl.d.ts  差异内容：CallServiceKit | api/@hms.telephony.voipCallControl.d.ts |
