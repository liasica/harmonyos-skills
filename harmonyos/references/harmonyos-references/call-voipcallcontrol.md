---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/call-voipcallcontrol
title: voipCallControl (VoIP通话控制)
breadcrumb: API参考 > 应用服务 > Call Service Kit（通话服务） > ArkTS API > voipCallControl (VoIP通话控制)
category: harmonyos-references
scraped_at: 2026-11-12T09:57:14+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:ec2c9e36082d784f99e545ed4db74bf8051e1a98fb03bcafef602d62daa8944d
---

本模块提供面向第三方穿戴等外设设备的VoIP通话控制功能，包括接听来电、拒接来电以及挂断通话等。由系统选择待控制的VoIP通话，因此无需指定callId。

**起始版本：** 26.0.1

## 导入模块

```typescript
import { voipCallControl } from '@kit.CallServiceKit';
```

## VideoStateType

表示接听VoIP通话时视频状态的枚举。

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Telephony.VoipCallManager

**起始版本：** 26.0.1

| 名称 | 值 | 说明 |
| --- | --- | --- |
| TYPE\_VOICE | 0 | 语音状态。 |
| TYPE\_VIDEO | 1 | 视频状态。 |

## voipCallControl.answerCall

answerCall(videoState?: VideoStateType): Promise<void>

接听当前VoIP来电。由系统选择待接听的来电，因此无需指定callId。可通过可选参数videoState区分语音接听和视频接听；不传入该参数时，默认为语音接听。使用Promise异步回调。

**需要权限**：ohos.permission.MANAGE\_CALL\_FOR\_DEVICES

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Telephony.VoipCallManager

**起始版本：** 26.0.1

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| videoState | [VideoStateType](call-voipcallcontrol.md#videostatetype) | 否 | 接听VoIP通话的通话类型：TYPE\_VOICE表示语音接听，TYPE\_VIDEO表示视频接听。默认值为TYPE\_VOICE。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](call-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 1007200002 | Operation failed. Cannot connect to service. |
| 1007200003 | System internal error. |
| 1007200004 | No VoIP call is available for control. |
| 1007200999 | Unknown error code. |

**示例：**

```typescript
import { voipCallControl } from '@kit.CallServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

// 语音接听当前来电
voipCallControl.answerCall().then(() => {
  hilog.info(0x0000, 'testTag', 'Succeeded in answering the voice call.');
}).catch((err: BusinessError) => {
  hilog.error(0x0000, 'testTag', 'Failed to answer the voice call: %{public}d %{public}s', err.code, err.message);
});

// 视频接听当前来电
voipCallControl.answerCall(voipCallControl.VideoStateType.TYPE_VIDEO).then(() => {
  hilog.info(0x0000, 'testTag', 'Succeeded in answering the video call.');
}).catch((err: BusinessError) => {
  hilog.error(0x0000, 'testTag', 'Failed to answer the video call: %{public}d %{public}s', err.code, err.message);
});
```

## voipCallControl.rejectCall

rejectCall(): Promise<void>

拒接当前VoIP来电。由系统选择待拒接的来电，因此无需指定callId。使用Promise异步回调。

**需要权限**：ohos.permission.MANAGE\_CALL\_FOR\_DEVICES

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Telephony.VoipCallManager

**起始版本：** 26.0.1

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](call-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 1007200002 | Operation failed. Cannot connect to service. |
| 1007200003 | System internal error. |
| 1007200004 | No VoIP call is available for control. |
| 1007200999 | Unknown error code. |

**示例：**

```typescript
import { voipCallControl } from '@kit.CallServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

// 拒接当前来电
voipCallControl.rejectCall().then(() => {
  hilog.info(0x0000, 'testTag', 'Succeeded in rejecting the call.');
}).catch((err: BusinessError) => {
  hilog.error(0x0000, 'testTag', 'Failed to reject the call: %{public}d %{public}s', err.code, err.message);
});
```

## voipCallControl.hangUpCall

hangUpCall(): Promise<void>

挂断当前VoIP通话。由系统选择待挂断的通话：优先挂断激活态通话，若来电中不存在激活态通话，则挂断来电。使用Promise异步回调。

**需要权限**：ohos.permission.MANAGE\_CALL\_FOR\_DEVICES

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Telephony.VoipCallManager

**起始版本：** 26.0.1

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](call-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 1007200002 | Operation failed. Cannot connect to service. |
| 1007200003 | System internal error. |
| 1007200004 | No VoIP call is available for control. |
| 1007200999 | Unknown error code. |

**示例：**

```typescript
import { voipCallControl } from '@kit.CallServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

// 挂断当前通话
voipCallControl.hangUpCall().then(() => {
  hilog.info(0x0000, 'testTag', 'Succeeded in hanging up the call.');
}).catch((err: BusinessError) => {
  hilog.error(0x0000, 'testTag', 'Failed to hang up the call: %{public}d %{public}s', err.code, err.message);
});
```
