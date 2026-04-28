---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-callkit-b065
title: Call Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.0(12) > OS平台能力 > API变更清单 > HarmonyOS NEXT Beta引入的API > Call Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:36:16+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:5ebb6223d8c97f9157fe023332a24efa1982fbf1b45ffbf759cfb04cd2e62c4e
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：voipCall；  API声明：function reportCallStateChange(callId: string, callState: VoipCallState, callType: VoipCallType): Promise<void>;  差异内容：function reportCallStateChange(callId: string, callState: VoipCallState, callType: VoipCallType): Promise<void>; | api/@hms.telephony.voipCall.d.ts |
| 新增API | NA | 类名：VoipCallAttribute；  API声明：isConferenceCall?: boolean;  差异内容：isConferenceCall?: boolean; | api/@hms.telephony.voipCall.d.ts |
| 新增API | NA | 类名：VoipCallAttribute；  API声明：isVoiceAnswerSupported?: boolean;  差异内容：isVoiceAnswerSupported?: boolean; | api/@hms.telephony.voipCall.d.ts |
| 新增API | NA | 类名：VoipCallState；  API声明：VOIP\_CALL\_STATE\_ANSWERED = 6  差异内容：VOIP\_CALL\_STATE\_ANSWERED = 6 | api/@hms.telephony.voipCall.d.ts |
| 新增API | NA | 类名：VoipCallState；  API声明：VOIP\_CALL\_STATE\_DISCONNECTING = 7  差异内容：VOIP\_CALL\_STATE\_DISCONNECTING = 7 | api/@hms.telephony.voipCall.d.ts |
