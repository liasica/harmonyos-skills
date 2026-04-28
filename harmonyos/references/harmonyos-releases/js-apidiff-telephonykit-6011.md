---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-telephonykit-6011
title: Telephony Kit
breadcrumb: 版本说明 > HarmonyOS 6.0.1(21) > OS平台能力 > API变更清单 > 6.0.1(21) Beta1引入的API > Telephony Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:34:03+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:d7f7ef002ab90c47473e9f0d09c1071c0bcbef68fa4eef6e79b3ae6e6953950d
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：call；  API声明：export enum TelCallState  差异内容：export enum TelCallState | api/@ohos.telephony.call.d.ts |
| 新增API | NA | 类名：TelCallState；  API声明：TEL\_CALL\_STATE\_UNKNOWN = -1  差异内容：TEL\_CALL\_STATE\_UNKNOWN = -1 | api/@ohos.telephony.call.d.ts |
| 新增API | NA | 类名：TelCallState；  API声明：TEL\_CALL\_STATE\_IDLE = 0  差异内容：TEL\_CALL\_STATE\_IDLE = 0 | api/@ohos.telephony.call.d.ts |
| 新增API | NA | 类名：TelCallState；  API声明：TEL\_CALL\_STATE\_RINGING = 1  差异内容：TEL\_CALL\_STATE\_RINGING = 1 | api/@ohos.telephony.call.d.ts |
| 新增API | NA | 类名：TelCallState；  API声明：TEL\_CALL\_STATE\_OFFHOOK = 2  差异内容：TEL\_CALL\_STATE\_OFFHOOK = 2 | api/@ohos.telephony.call.d.ts |
| 新增API | NA | 类名：TelCallState；  API声明：TEL\_CALL\_STATE\_ANSWERED = 3  差异内容：TEL\_CALL\_STATE\_ANSWERED = 3 | api/@ohos.telephony.call.d.ts |
| 新增API | NA | 类名：TelCallState；  API声明：TEL\_CALL\_STATE\_CONNECTED = 4  差异内容：TEL\_CALL\_STATE\_CONNECTED = 4 | api/@ohos.telephony.call.d.ts |
| 新增API | NA | 类名：observer；  API声明：type TelCallState = call.TelCallState;  差异内容：type TelCallState = call.TelCallState; | api/@ohos.telephony.observer.d.ts |
| 新增API | NA | 类名：observer；  API声明：function on(type: 'callStateChangeEx', callback: Callback<TelCallState>, options?: ObserverOptions): void;  差异内容：function on(type: 'callStateChangeEx', callback: Callback<TelCallState>, options?: ObserverOptions): void; | api/@ohos.telephony.observer.d.ts |
| 新增API | NA | 类名：observer；  API声明：function off(type: 'callStateChangeEx', callback?: Callback<TelCallState>): void;  差异内容：function off(type: 'callStateChangeEx', callback?: Callback<TelCallState>): void; | api/@ohos.telephony.observer.d.ts |
