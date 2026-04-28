---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-telephonykit-6101
title: Telephony Kit
breadcrumb: 版本说明 > HarmonyOS 6.1.0(23) > OS平台能力 > API变更清单 > 6.1.0(23) Beta1引入的变更 > Telephony Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:33:36+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:adb1cb2392d785eed99ea1fe499f035d964265174d8a1368c64184ac4fc56431
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增错误码 | 类名：radio；  API声明：function getRadioTechSync(slotId: number): NetworkRadioTech;  差异内容：NA | 类名：radio；  API声明：function getRadioTechSync(slotId: number): NetworkRadioTech;  差异内容：201,401,8300001,8300002,8300003,8300999 | api/@ohos.telephony.radio.d.ts |
| 新增API | NA | 类名：call；  API声明：function answerCall(callback: AsyncCallback<void>): void;  差异内容：function answerCall(callback: AsyncCallback<void>): void; | api/@ohos.telephony.call.d.ts |
| 新增API | NA | 类名：call；  API声明：function hangUpCall(callback: AsyncCallback<void>): void;  差异内容：function hangUpCall(callback: AsyncCallback<void>): void; | api/@ohos.telephony.call.d.ts |
| 新增API | NA | 类名：call；  API声明：function rejectCall(callback: AsyncCallback<void>): void;  差异内容：function rejectCall(callback: AsyncCallback<void>): void; | api/@ohos.telephony.call.d.ts |
| 新增API | NA | 类名：call；  API声明：export enum CCallState  差异内容：export enum CCallState | api/@ohos.telephony.call.d.ts |
| 新增API | NA | 类名：CCallState；  API声明：CCALL\_STATE\_UNKNOWN = -1  差异内容：CCALL\_STATE\_UNKNOWN = -1 | api/@ohos.telephony.call.d.ts |
| 新增API | NA | 类名：CCallState；  API声明：CCALL\_STATE\_ACTIVE = 0  差异内容：CCALL\_STATE\_ACTIVE = 0 | api/@ohos.telephony.call.d.ts |
| 新增API | NA | 类名：CCallState；  API声明：CCALL\_STATE\_HOLDING = 1  差异内容：CCALL\_STATE\_HOLDING = 1 | api/@ohos.telephony.call.d.ts |
| 新增API | NA | 类名：CCallState；  API声明：CCALL\_STATE\_DIALING = 2  差异内容：CCALL\_STATE\_DIALING = 2 | api/@ohos.telephony.call.d.ts |
| 新增API | NA | 类名：CCallState；  API声明：CCALL\_STATE\_ALERTING = 3  差异内容：CCALL\_STATE\_ALERTING = 3 | api/@ohos.telephony.call.d.ts |
| 新增API | NA | 类名：CCallState；  API声明：CCALL\_STATE\_INCOMING = 4  差异内容：CCALL\_STATE\_INCOMING = 4 | api/@ohos.telephony.call.d.ts |
| 新增API | NA | 类名：CCallState；  API声明：CCALL\_STATE\_WAITING = 5  差异内容：CCALL\_STATE\_WAITING = 5 | api/@ohos.telephony.call.d.ts |
| 新增API | NA | 类名：CCallState；  API声明：CCALL\_STATE\_DISCONNECTED = 6  差异内容：CCALL\_STATE\_DISCONNECTED = 6 | api/@ohos.telephony.call.d.ts |
| 新增API | NA | 类名：CCallState；  API声明：CCALL\_STATE\_DISCONNECTING = 7  差异内容：CCALL\_STATE\_DISCONNECTING = 7 | api/@ohos.telephony.call.d.ts |
| 新增API | NA | 类名：CCallState；  API声明：CCALL\_STATE\_IDLE = 8  差异内容：CCALL\_STATE\_IDLE = 8 | api/@ohos.telephony.call.d.ts |
| 新增API | NA | 类名：CCallState；  API声明：CCALL\_STATE\_ANSWERED = 9  差异内容：CCALL\_STATE\_ANSWERED = 9 | api/@ohos.telephony.call.d.ts |
| 新增API | NA | 类名：observer；  API声明：type CCallState = call.CCallState;  差异内容：type CCallState = call.CCallState; | api/@ohos.telephony.observer.d.ts |
| 新增API | NA | 类名：observer；  API声明：function onCCallStateChange(callback: Callback<CCallStateInfo>, options?: ObserverOptions): void;  差异内容：function onCCallStateChange(callback: Callback<CCallStateInfo>, options?: ObserverOptions): void; | api/@ohos.telephony.observer.d.ts |
| 新增API | NA | 类名：observer；  API声明：function offCCallStateChange(callback?: Callback<CCallStateInfo>): void;  差异内容：function offCCallStateChange(callback?: Callback<CCallStateInfo>): void; | api/@ohos.telephony.observer.d.ts |
| 新增API | NA | 类名：observer；  API声明：export interface CCallStateInfo  差异内容：export interface CCallStateInfo | api/@ohos.telephony.observer.d.ts |
| 新增API | NA | 类名：CCallStateInfo；  API声明：state: CCallState;  差异内容：state: CCallState; | api/@ohos.telephony.observer.d.ts |
| 新增API | NA | 类名：CCallStateInfo；  API声明：teleNumber: string;  差异内容：teleNumber: string; | api/@ohos.telephony.observer.d.ts |
| 新增API | NA | 类名：observer；  API声明：function onGetSimActiveState(slotId: number, callback: Callback<boolean>): void;  差异内容：function onGetSimActiveState(slotId: number, callback: Callback<boolean>): void; | api/@ohos.telephony.observer.d.ts |
| 新增API | NA | 类名：observer；  API声明：function offGetSimActiveState(callback?: Callback<boolean>): void;  差异内容：function offGetSimActiveState(callback?: Callback<boolean>): void; | api/@ohos.telephony.observer.d.ts |
| 新增API | NA | 类名：vcard；  API声明：function importVCard(context: Context, filePath: string, accountId: number, callback: AsyncCallback<void>): void;  差异内容：function importVCard(context: Context, filePath: string, accountId: number, callback: AsyncCallback<void>): void; | api/@ohos.telephony.vcard.d.ts |
| 新增API | NA | 类名：vcard；  API声明：function importVCard(context: Context, filePath: string, accountId?: number): Promise<void>;  差异内容：function importVCard(context: Context, filePath: string, accountId?: number): Promise<void>; | api/@ohos.telephony.vcard.d.ts |
| 新增API | NA | 类名：vcard；  API声明：function importVCard(context: Context, filePath: string, callback: AsyncCallback<void>): void;  差异内容：function importVCard(context: Context, filePath: string, callback: AsyncCallback<void>): void; | api/@ohos.telephony.vcard.d.ts |
| 新增API | NA | 类名：vcard；  API声明：function exportVCard(context: Context, predicates: dataSharePredicates.DataSharePredicates, options: VCardBuilderOptions, callback: AsyncCallback<string>): void;  差异内容：function exportVCard(context: Context, predicates: dataSharePredicates.DataSharePredicates, options: VCardBuilderOptions, callback: AsyncCallback<string>): void; | api/@ohos.telephony.vcard.d.ts |
| 新增API | NA | 类名：vcard；  API声明：function exportVCard(context: Context, predicates: dataSharePredicates.DataSharePredicates, options?: VCardBuilderOptions): Promise<string>;  差异内容：function exportVCard(context: Context, predicates: dataSharePredicates.DataSharePredicates, options?: VCardBuilderOptions): Promise<string>; | api/@ohos.telephony.vcard.d.ts |
| 新增API | NA | 类名：vcard；  API声明：function exportVCard(context: Context, predicates: dataSharePredicates.DataSharePredicates, callback: AsyncCallback<string>): void;  差异内容：function exportVCard(context: Context, predicates: dataSharePredicates.DataSharePredicates, callback: AsyncCallback<string>): void; | api/@ohos.telephony.vcard.d.ts |
