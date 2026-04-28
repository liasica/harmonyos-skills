---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/call-voipcall
title: voipCall (应用内通话管理)
breadcrumb: API参考 > 应用服务 > Call Service Kit（通话服务） > ArkTS API > voipCall (应用内通话管理)
category: harmonyos-references
scraped_at: 2026-04-28T08:16:29+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:2537ae6712868941103b7b465e56434912fd0da86200638f63016729eaa3b295
---

本模块提供应用内通话管理功能，包括向系统上报来电、上报去电、上报通话状态以及获取用户点击事件等。

获取用户点击事件需使用[voipCall.on](call-voipcall.md#voipcallonvoipcalluievent)在业务流程开始时提前订阅voipCallUiEvent事件，可于业务流程结束后使用[voipCall.off](call-voipcall.md#voipcalloffvoipcalluievent)结束订阅。

**起始版本：** 4.1.0(11)

## 导入模块

PhoneTabletWearable

```
1. import { voipCall } from '@kit.CallServiceKit';
```

## VoipCallType

PhoneTabletWearable

表示通话类型的枚举。

**系统能力**：SystemCapability.Telephony.VoipCallManager

**起始版本：** 4.1.0(11)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| VOIP\_CALL\_VOICE | 0 | 语音通话。 |
| VOIP\_CALL\_VIDEO | 1 | 视频通话。 |

## VoipCallState

PhoneTabletWearable

表示通话状态的枚举。

**系统能力**：SystemCapability.Telephony.VoipCallManager

**起始版本：** 4.1.0(11)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| VOIP\_CALL\_STATE\_IDLE | 0 | 呼叫状态空闲。 |
| VOIP\_CALL\_STATE\_RINGING | 1 | 呼叫传入状态。 |
| VOIP\_CALL\_STATE\_ACTIVE | 2 | 激活呼叫状态。 |
| VOIP\_CALL\_STATE\_HOLDING | 3 | 保持呼叫状态。 |
| VOIP\_CALL\_STATE\_DISCONNECTED | 4 | 呼叫状态已断开。 |
| VOIP\_CALL\_STATE\_DIALING | 5 | 拨号中。  **起始版本**: 5.0.0(12) |
| VOIP\_CALL\_STATE\_ANSWERED | 6 | 正在接听。  **起始版本**: 5.0.0(12) |
| VOIP\_CALL\_STATE\_DISCONNECTING | 7 | 正在断开。  **起始版本**: 5.0.0(12) |

## VoipCallUiEvent

PhoneTabletWearable

表示通话事件的枚举。

**系统能力**：SystemCapability.Telephony.VoipCallManager

**起始版本：** 4.1.0(11)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| VOIP\_CALL\_EVENT\_NONE | 0 | 无任何事件。 |
| VOIP\_CALL\_EVENT\_VOICE\_ANSWER | 1 | 通话语音接听事件。 |
| VOIP\_CALL\_EVENT\_VIDEO\_ANSWER | 2 | 通话视频接听事件。 |
| VOIP\_CALL\_EVENT\_REJECT | 3 | 通话拒接事件。 |
| VOIP\_CALL\_EVENT\_HANGUP | 4 | 通话挂断事件。 |
| VOIP\_CALL\_EVENT\_MUTED | 5 | 静音事件。  **起始版本**: 5.0.0(12) |
| VOIP\_CALL\_EVENT\_UNMUTED | 6 | 取消静音事件。  **起始版本**: 5.0.0(12) |
| VOIP\_CALL\_EVENT\_SPEAKER\_ON | 7 | 开启扬声器事件。  **起始版本**: 5.0.0(12)  （预留事件，暂未支持） |
| VOIP\_CALL\_EVENT\_SPEAKER\_OFF | 8 | 关闭扬声器事件。  **起始版本**: 5.0.0(12)  （预留事件，暂未支持） |
| VOIP\_CALL\_EVENT\_MUTE\_RINGTONE | 9 | 用户按键静音铃声事件。  **起始版本**: 6.0.2(22) |

## ErrorReason

PhoneTabletWearable

表示错误码类型的枚举。

**系统能力**：SystemCapability.Telephony.VoipCallManager

**起始版本：** 4.1.0(11)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| ERROR\_NONE | 0 | 无错误出现。 |
| CELLULAR\_CALL\_EXISTS | 1 | 当前已存在蜂窝通话。 |
| VOIP\_CALL\_EXISTS | 2 | 当前已存在其他应用内通话。 |
| INVALID\_CALL | 3 | 通话无效，比如传入的callId未通过校验等。 |
| USER\_ANSWER\_CELLULAR\_FIRST | 4 | 用户选择接听蜂窝。 |

## VoipCallUiEventInfo

PhoneTabletWearable

通话事件详细信息。

**系统能力**：SystemCapability.Telephony.VoipCallManager

**起始版本：** 4.1.0(11)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| callId | string | 否 | 否 | 应用内通话唯一ID。 |
| voipCallUiEvent | [VoipCallUiEvent](call-voipcall.md#voipcalluievent) | 否 | 否 | 应用内通话事件。 |
| errorReason | [ErrorReason](call-voipcall.md#errorreason) | 否 | 否 | 应用内通话错误码。 |

## VoipCallFailureCause

PhoneTabletWearable

表示来电消息建立失败原因的枚举。

**系统能力**：SystemCapability.Telephony.VoipCallManager

**起始版本：** 4.1.0(11)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| OTHER | 0 | 其他失败原因。 |
| ROUTE\_BUSY | 1 | 应用线路忙。 |
| CONNECTION\_FAILED | 2 | 通话连接建立失败。 |

## VoipCallAttribute

PhoneTabletWearable

通话属性选项。

**系统能力**：SystemCapability.Telephony.VoipCallManager

**起始版本：** 4.1.0(11)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| callId | string | 否 | 否 | 应用内通话唯一ID。 |
| voipCallType | [VoipCallType](call-voipcall.md#voipcalltype) | 否 | 否 | 应用内通话类型。 |
| userName | string | 否 | 否 | 应用内通话用户昵称。 |
| userProfile | image.[PixelMap](arkts-apis-image-pixelmap.md) | 否 | 否 | 用户头像图片，需导入图像处理模块，详情见[PixelMap](arkts-apis-image-pixelmap.md)。  支持传入的最大图片大小为221x221像素，推荐传入的图片大小为112x112像素。通过 [PixelMap](arkts-apis-image-pixelmap.md)的[getPixelBytesNumber](arkts-apis-image-pixelmap.md#getpixelbytesnumber7)接口获取到的图片大小要小于196608bit。 |
| abilityName | string | 否 | 否 | 接听后需加载的应用界面ability名称。 |
| voipCallState | [VoipCallState](call-voipcall.md#voipcallstate) | 否 | 否 | 应用内通话状态。 |
| showBannerForIncomingCall | boolean | 否 | 是 | 支持应用上报来电/去电是否显示横幅通知。  true：应用设置来电显示横幅通知。  false：应用设置来电不显示横幅通知。  默认值为true。  **起始版本**: 5.0.0(12) |
| isConferenceCall | boolean | 否 | 是 | 通话是否为会议。  true：来电是会议。  false：来电不是会议。  默认值为false。  **起始版本**: 5.0.0(12) |
| isVoiceAnswerSupported | boolean | 否 | 是 | 视频来电/去电是否支持语音接听。  true：支持。  false：不支持。  默认值为true。  **起始版本**: 5.0.0(12) |
| isUserMuteRingToneAllowed | boolean | 否 | 是 | 是否支持用户按键静音来电铃声。  true：支持。  false：不支持。  默认值为false。  **起始版本**: 6.0.2(22) |
| isDialingAllowedDuringCarrierCall | boolean | 否 | 是 | 是否允许运营商通话中发起VoIP主叫。  true：允许。  false：不允许。  默认值为false。  **起始版本**: 6.0.2(22) |

## CallAudioEvent

PhoneTabletWearable

表示静音、扬声器事件的枚举。

**系统能力**：SystemCapability.Telephony.VoipCallManager

**起始版本：** 5.0.0(12)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| AUDIO\_EVENT\_MUTED | 0 | 静音。 |
| AUDIO\_EVENT\_UNMUTED | 1 | 取消静音。 |
| AUDIO\_EVENT\_SPEAKER\_ON | 2 | 开启扬声器。 |
| AUDIO\_EVENT\_SPEAKER\_OFF | 3 | 关闭扬声器。 |

## voipCall.on('voipCallUiEvent')

PhoneTabletWearable

on(type: 'voipCallUiEvent', callback: Callback<VoipCallUiEventInfo>): void

订阅voipCallUiEvent事件。使用Callback的方式获取订阅voipCallUiEvent事件的结果。

**系统能力**：SystemCapability.Telephony.VoipCallManager

**起始版本：** 4.1.0(11)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 通话事件类型，参数固定为“voipCallUiEvent”。 |
| callback | Callback<[VoipCallUiEventInfo](call-voipcall.md#voipcalluieventinfo)> | 是 | 回调函数，返回通话事件详细信息对象。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](call-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 1007200001 | Invalid parameter value. |
| 1007200002 | Operation failed. Cannot connect to service. |
| 1007200003 | System internal error. |
| 1007200999 | Unknown error code. |

**示例：**

```
1. import { voipCall } from '@kit.CallServiceKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. voipCall.on('voipCallUiEvent', (data: voipCall.VoipCallUiEventInfo) => {
5. hilog.info(0x0000, 'testTag', `Succeeded in reading callback. CallId: ${data.callId}, voipCallUiEvent: ${data.voipCallUiEvent}`);
6. });
```

## voipCall.off('voipCallUiEvent')

PhoneTabletWearable

off(type: 'voipCallUiEvent', callback?: Callback<VoipCallUiEventInfo>): void

取消订阅voipCallUiEvent事件。使用Callback的方式获取取消订阅voipCallUiEvent事件的结果。

**系统能力**：SystemCapability.Telephony.VoipCallManager

**起始版本：** 4.1.0(11)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 通话事件类型，参数固定为“voipCallUiEvent”。 |
| callback | Callback<[VoipCallUiEventInfo](call-voipcall.md#voipcalluieventinfo)> | 否 | 需要取消监听的回调函数，返回通话事件详细信息对象。若不填，则取消当前应用监听该事件的所有回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](call-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 1007200001 | Invalid parameter value. |
| 1007200002 | Operation failed. Cannot connect to service. |
| 1007200003 | System internal error. |
| 1007200999 | Unknown error code. |

**示例：**

```
1. import { voipCall } from '@kit.CallServiceKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. voipCall.off('voipCallUiEvent', (data: voipCall.VoipCallUiEventInfo) => {
5. hilog.info(0x0000, 'testTag', `Succeeded in reading callback. CallId: ${data.callId}, voipCallUiEvent: ${data.voipCallUiEvent}`);
6. });
```

## voipCall.reportIncomingCall

PhoneTabletWearable

reportIncomingCall(voipCallAttribute: VoipCallAttribute): Promise<ErrorReason>

通知来电消息，如果应用来电消息建立失败，需调用[reportIncomingCallError](call-voipcall.md#voipcallreportincomingcallerror)通知来电建立失败。需设置通话详细信息，见[VoipCallAttribute](call-voipcall.md#voipcallattribute)。使用Promise异步回调。

**系统能力**：SystemCapability.Telephony.VoipCallManager

**起始版本：** 4.1.0(11)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| voipCallAttribute | [VoipCallAttribute](call-voipcall.md#voipcallattribute) | 是 | 应用内通话详细信息如用户头像、用户昵称、通话唯一标识等，详情请参见[VoipCallAttribute](call-voipcall.md#voipcallattribute)。（应用上报去电时，VoipCallAttribute中的voipCallState属性必须为VOIP\_CALL\_STATE\_DIALING。） |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[ErrorReason](call-voipcall.md#errorreason)> | Promise对象，返回错误码类型。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](call-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 1007200001 | Invalid parameter value. |
| 1007200002 | Operation failed. Cannot connect to service. |
| 1007200003 | System internal error. |
| 1007200999 | Unknown error code. |

**示例：**

```
1. import { image } from '@kit.ImageKit';
2. import { voipCall } from '@kit.CallServiceKit';
3. import { resourceManager } from '@kit.LocalizationKit';
4. import { hilog } from '@kit.PerformanceAnalysisKit';
5. import { UIAbility } from '@kit.AbilityKit';
6. import { pushService } from '@kit.PushKit';

8. interface Content {
9. data: string;
10. callId: string;
11. }

13. export default class VoipAbility extends UIAbility {
14. onCreate(): void {
15. hilog.info(0x0000, 'testTag', 'VoipExtAbility onCreate.');
16. pushService.receiveMessage('VoIP', this, async (data) => {
17. let content: Content = JSON.parse(data.data);
18. let callId: string = content.callId;

20. hilog.info(0x0000, 'testTag', 'Get voip message successfully: %{public}s', callId);

22. // 此处为用户头像，需要创建PixelMap类型
23. const resourceMgr : resourceManager.ResourceManager = this.context.resourceManager;
24. const fileData : Uint8Array = await resourceMgr.getRawFileContent('example.png');
25. const buffer = fileData.buffer;
26. const imageSource : image.ImageSource = image.createImageSource(buffer);
27. const pixelMap : image.PixelMap = await imageSource.createPixelMap();
28. if (pixelMap) {
29. pixelMap.getImageInfo((err, imageInfo) => {
30. if (imageInfo) {
31. hilog.info(0x0000, 'testTag', `DemoPushMessageAbility imageInfo: ${imageInfo.size.width} * ${imageInfo.size.height}.`);
32. }
33. });
34. }

36. // 构建通话详细信息的对象
37. let callInfo: voipCall.VoipCallAttribute = {
38. callId: callId,
39. voipCallType: voipCall.VoipCallType.VOIP_CALL_VOICE,
40. userName: "name",
41. userProfile: pixelMap,
42. abilityName: 'ability',
43. voipCallState: voipCall.VoipCallState.VOIP_CALL_STATE_RINGING
44. };

46. // 通知来电消息
47. let error = await voipCall.reportIncomingCall(callInfo);
48. if (error != voipCall.ErrorReason.ERROR_NONE) {
49. hilog.error(0x0000, 'testTag', 'Failed to report incoming call: %{public}d', error);
50. return;
51. }

53. hilog.info(0x0000, 'testTag', 'Get voip message end.');
54. });
55. hilog.info(0x0000, 'testTag', 'Succeeded in registering VoIP.');
56. }
57. }
```

## voipCall.reportOutgoingCall

PhoneTabletWearable

reportOutgoingCall(voipCallAttribute: VoipCallAttribute): Promise<ErrorReason>

应用上报去电。需设置通话详细信息，见[VoipCallAttribute](call-voipcall.md#voipcallattribute)。使用Promise异步回调。

**系统能力**：SystemCapability.Telephony.VoipCallManager

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| voipCallAttribute | [VoipCallAttribute](call-voipcall.md#voipcallattribute) | 是 | 应用内通话详细信息如用户头像、用户昵称、通话唯一标识等，详情请参见[VoipCallAttribute](call-voipcall.md#voipcallattribute)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[ErrorReason](call-voipcall.md#errorreason)> | Promise对象，返回错误码类型。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](call-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 1007200001 | Invalid parameter value. |
| 1007200002 | Operation failed. Cannot connect to service. |
| 1007200003 | System internal error. |
| 1007200999 | Unknown error code. |

**示例：**

```
1. import { image } from '@kit.ImageKit';
2. import { voipCall } from '@kit.CallServiceKit';
3. import { resourceManager } from '@kit.LocalizationKit';
4. import { hilog } from '@kit.PerformanceAnalysisKit';
5. import { UIAbility } from '@kit.AbilityKit';
6. import { pushService } from '@kit.PushKit';

8. interface Content {
9. data: string;
10. callId: string;
11. }

13. export default class VoipExtAbility extends UIAbility {
14. onCreate(): void {
15. hilog.info(0x0000, 'testTag', 'VoipExtAbility onCreate.');
16. pushService.receiveMessage('VoIP', this, async (data) => {
17. let content: Content = JSON.parse(data.data);
18. let callId: string = content.callId;

20. hilog.info(0x0000, 'testTag', 'Get voip message successfully: %{public}s', callId);

22. // 此处为用户头像，需要创建PixelMap类型
23. const resourceMgr : resourceManager.ResourceManager = this.context.resourceManager;
24. const fileData : Uint8Array = await resourceMgr.getRawFileContent('example.png');
25. const buffer = fileData.buffer;
26. const imageSource : image.ImageSource = image.createImageSource(buffer);
27. const pixelMap : image.PixelMap = await imageSource.createPixelMap();
28. if (pixelMap) {
29. pixelMap.getImageInfo((err, imageInfo) => {
30. if (imageInfo) {
31. hilog.info(0x0000, 'testTag', `DemoPushMessageAbility imageInfo: ${imageInfo.size.width} * ${imageInfo.size.height}.`);
32. }
33. });
34. }

36. // 构建通话详细信息的对象
37. let callInfo: voipCall.VoipCallAttribute = {
38. callId: callId,
39. voipCallType: voipCall.VoipCallType.VOIP_CALL_VOICE,
40. userName: "name",
41. userProfile: pixelMap,
42. abilityName: 'ability',
43. voipCallState: voipCall.VoipCallState.VOIP_CALL_STATE_DIALING
44. };

46. // 通知去电消息
47. let error = await voipCall.reportOutgoingCall(callInfo);
48. if (error != voipCall.ErrorReason.ERROR_NONE) {
49. hilog.error(0x0000, 'testTag', 'Failed to report outgoing call: %{public}d', error);
50. return;
51. }
52. hilog.info(0x0000, 'testTag', 'Get voip message end.');
53. });
54. hilog.info(0x0000, 'testTag', 'Succeeded in registering VoIP.');
55. }
56. }
```

## voipCall.reportCallAudioEventChange

PhoneTabletWearable

reportCallAudioEventChange(callId: string, callAudioEvent: CallAudioEvent): Promise<void>

应用上报通话中的静音、扬声器事件。使用Promise异步回调。

**系统能力**：SystemCapability.Telephony.VoipCallManager

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callId | string | 是 | 应用内通话唯一ID。 |
| callAudioEvent | [CallAudioEvent](call-voipcall.md#callaudioevent) | 是 | VoIP开/关静音、扬声器事件，详情请参见[CallAudioEvent](call-voipcall.md#callaudioevent)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](call-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 1007200001 | Invalid parameter value. |
| 1007200002 | Operation failed. Cannot connect to service. |
| 1007200003 | System internal error. |
| 1007200999 | Unknown error code. |

**示例：**

```
1. import { voipCall } from '@kit.CallServiceKit';
2. import { UIAbility } from '@kit.AbilityKit';
3. import { pushService } from '@kit.PushKit';
4. import { hilog } from '@kit.PerformanceAnalysisKit';

6. interface Content {
7. data: string;
8. callId: string;
9. }

11. export default class VoipExtAbility extends UIAbility {
12. onCreate(): void {
13. hilog.info(0x0000, 'testTag', 'VoipExtAbility onCreate.');
14. pushService.receiveMessage('VoIP', this, async (data) => {
15. let content: Content = JSON.parse(data.data);
16. let callId: string = content.callId;

18. let callAudioEvent : voipCall.CallAudioEvent = voipCall.CallAudioEvent.AUDIO_EVENT_MUTED;

20. // 上报通话中静音、扬声器事件
21. voipCall.reportCallAudioEventChange(callId, callAudioEvent).then(() => {
22. hilog.info(0x0000, 'testTag', `Succeeded in reporting call audio event change.`);
23. });
24. });
25. hilog.info(0x0000, 'testTag', 'Succeeded in registering VoIP.');
26. }
27. }
```

## voipCall.reportCallStateChange

PhoneTabletWearable

reportCallStateChange(callId: string, callState: VoipCallState): Promise<void>

通知应用内通话状态变化，使用Promise异步回调。

该接口不能改变通话类型，例如，语音通话不能升级为视频通话，视频通话也不能降级为语音通话，如需上述升降级操作，请调用[voipCall.reportCallStateChange](call-voipcall.md#voipcallreportcallstatechange-1)。

**系统能力**：SystemCapability.Telephony.VoipCallManager

**起始版本：** 4.1.0(11)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callId | string | 是 | 呼叫ID。 |
| callState | [VoipCallState](call-voipcall.md#voipcallstate) | 是 | 通话状态，参考[VoipCallState](call-voipcall.md#voipcallstate)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](call-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 1007200001 | Invalid parameter value. |
| 1007200002 | Operation failed. Cannot connect to service. |
| 1007200003 | System internal error. |
| 1007200999 | Unknown error code. |

**示例：**

```
1. import { voipCall } from '@kit.CallServiceKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. voipCall.reportCallStateChange("callId123", voipCall.VoipCallState.VOIP_CALL_STATE_ACTIVE).then(() => {
5. hilog.info(0x0000, 'testTag', `Succeeded in reporting call state change.`);
6. });
```

## voipCall.reportCallStateChange

PhoneTabletWearable

reportCallStateChange(callId: string, callState: VoipCallState, callType: VoipCallType): Promise<void>

通知应用内通话状态变化，并指定通话类型，使用Promise异步回调。

对于视频来电语音接听、通话中视频降语音或者语音升视频，需要调用该接口，并传入正确的callType。

**系统能力**：SystemCapability.Telephony.VoipCallManager

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callId | string | 是 | 呼叫ID。 |
| callState | [VoipCallState](call-voipcall.md#voipcallstate) | 是 | 通话状态，参考[VoipCallState](call-voipcall.md#voipcallstate)。 |
| callType | [VoipCallType](call-voipcall.md#voipcalltype) | 是 | 通话类型，参考[VoipCallType](call-voipcall.md#voipcalltype)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](call-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 1007200001 | Invalid parameter value. |
| 1007200002 | Operation failed. Cannot connect to service. |
| 1007200003 | System internal error. |
| 1007200999 | Unknown error code. |

**示例：**

```
1. import { voipCall } from '@kit.CallServiceKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. voipCall.reportCallStateChange("callId123", voipCall.VoipCallState.VOIP_CALL_STATE_ACTIVE, voipCall.VoipCallType.VOIP_CALL_VOICE).then(() => {
5. hilog.info(0x0000, 'testTag', `Succeeded in reporting call state change.`);
6. });
```

## voipCall.reportIncomingCallError

PhoneTabletWearable

reportIncomingCallError(callId: string, voipCallFailureCause: VoipCallFailureCause): Promise<void>

通知来电消息建立失败的原因，使用Promise异步回调。

**系统能力**：SystemCapability.Telephony.VoipCallManager

**起始版本：** 4.1.0(11)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callId | string | 是 | 应用内通话唯一ID。 |
| voipCallFailureCause | [VoipCallFailureCause](call-voipcall.md#voipcallfailurecause) | 是 | 来电消息建立失败原因。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](call-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 1007200001 | Invalid parameter value. |
| 1007200002 | Operation failed. Cannot connect to service. |
| 1007200003 | System internal error. |
| 1007200999 | Unknown error code. |

**示例：**

```
1. import { voipCall } from '@kit.CallServiceKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. voipCall.reportIncomingCallError("callId123", voipCall.VoipCallFailureCause.OTHER).then(() => {
5. hilog.info(0x0000, 'testTag', `Succeeded in reporting incoming call error.`);
6. });
```
