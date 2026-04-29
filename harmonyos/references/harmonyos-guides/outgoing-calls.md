---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/outgoing-calls
title: 去电场景
breadcrumb: 指南 > 应用服务 > Call Service Kit（通话服务） > 去电场景
category: harmonyos-guides
scraped_at: 2026-04-29T13:37:38+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:00f4ae4512be16aa2f3b19db70294e9e47dbd11550106f7b9efc7fbdc466daf7
---

## 场景介绍

应用主动发起音/视频通话，称为去电场景。

去电场景，由于应用在前台，不需要横幅通知，只在屏幕左上角，展示通话胶囊。去电场景的效果图展示如下：

| **语音去电(正在呼叫)** | **语音去电（通话中）** | **视频去电（正在呼叫）** | **视频去电（通话中）** |
| --- | --- | --- | --- |
|  |  |  |  |

去电场景，用户也可以拉起通知中心面板，在实况窗横幅上做静音与解除静音、挂断通话等操作。

| **去电实况窗通知（正在呼叫）** | **去电实况窗通知（通话中）** |
| --- | --- |
|  |  |

## 约束与限制

去电场景支持Phone、Tablet设备，并从6.0(20)版本开始支持Wearable设备。

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/sWyPEyMJTK-8KLisbAbhCA/zh-cn_image_0000002589245141.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T053737Z&HW-CC-Expire=86400&HW-CC-Sign=01FCCD4C371576FC66A2DC828BDC23C5B8FC742538CB6E7686B641DB1548EB94)

## 接口说明

去电场景的接口，由[voipCall](../harmonyos-references/call-voipcall.md)提供。更多接口信息详见[接口文档](../harmonyos-references/call-voipcall.md)。

| 接口名 | 描述 |
| --- | --- |
| on(type: 'voipCallUiEvent', callback: Callback<VoipCallUiEventInfo>): void | 订阅voipCallUiEvent事件。 |
| off(type: 'voipCallUiEvent', callback?: Callback<VoipCallUiEventInfo>): void | 取消订阅voipCallUiEvent事件。 |
| reportOutgoingCall(voipCallAttribute: VoipCallAttribute): Promise<ErrorReason> | 上报去电。 |
| reportCallAudioEventChange(callId: string, callAudioEvent: CallAudioEvent): Promise<void> | 上报音频事件。 |
| reportCallStateChange(callId: string, callState: VoipCallState): Promise<void> | 上报通话状态改变。 |
| reportCallStateChange(callId: string, callState: VoipCallState, callType: VoipCallType): Promise<void> | 上报通话状态改变，并指定通话类型。 |

## 开发步骤

去电场景的开发步骤与来电场景相似。

1. 导入相关依赖。

   ```
   1. import { voipCall } from '@kit.CallServiceKit';
   2. import { image } from '@kit.ImageKit';
   3. import { hilog } from '@kit.PerformanceAnalysisKit';
   ```
2. 为了感知到用户在实况窗上做的静音与解除静音、挂断通话等操作，应用需要注册voipCallUiEvent事件。建议在上报去电之前注册。

   示例代码如下：

   ```
   1. // 注册voipCallUiEvent事件
   2. voipCall.on('voipCallUiEvent', callback => {
   3. hilog.info(0x0000, 'CallDemo', 'Succeeded in registering voipCallUiEvent');
   4. });
   ```
3. 应用内部建立通话连接之后，需要向Call Service Kit上报去电，并携带通话信息，详见[VoipCallAttribute](../harmonyos-references/call-voipcall.md#voipcallattribute)。

   系统会在屏幕左上角，展示通话胶囊。

   以语音去电为例，示例代码如下：

   ```
   1. // 构建上报去电的参数
   2. let voipCallAttribute: voipCall.VoipCallAttribute = {
   3. callId: '1234567890',
   4. voipCallType: voipCall.VoipCallType.VOIP_CALL_VOICE,
   5. userName: 'Jack',
   6. userProfile: image.createPixelMapSync(new ArrayBuffer(100), { size: { width: 90, height: 90 } }),
   7. abilityName: 'VoipCallAbility',
   8. voipCallState: voipCall.VoipCallState.VOIP_CALL_STATE_DIALING,  // 去电的状态必须是DIALING
   9. showBannerForIncomingCall: true
   10. };

   12. // 向Call Service Kit上报去电
   13. voipCall.reportOutgoingCall(voipCallAttribute).then(errorReason => {
   14. if (errorReason == voipCall.ErrorReason.ERROR_NONE) {
   15. hilog.info(0x0000, 'CallDemo', 'Succeeded in reporting the outgoing call');
   16. } else {
   17. hilog.error(0x0000, 'CallDemo', 'Failed to report the outgoing call: %{public}d', errorReason);
   18. }
   19. });
   ```

   注意

   上报去电时，通话状态必须是VOIP\_CALL\_STATE\_DIALING，否则Call Service Kit会认为参数不合法而返回[1007200001错误码](../harmonyos-references/call-error-code.md#section1007200001-参数无效)。
4. 如果对端接听，应用需要向Call Service Kit上报通话状态[VOIP\_CALL\_STATE\_ACTIVE](../harmonyos-references/call-voipcall.md#voipcallstate)。系统会更新通话胶囊，开始展示通话计时。

   示例代码如下：

   ```
   1. // ...应用服务器收到对端接听的消息
   2. let answeredCallId = '123456'; //与reportOutgoingCall携带callId一致，应用内通话唯一ID。

   4. // 向Call Service Kit上报通话状态
   5. voipCall.reportCallStateChange(answeredCallId, voipCall.VoipCallState.VOIP_CALL_STATE_ACTIVE);
   ```
5. 去电场景，用户也可以拉起通知中心面板，在实况窗通知上执行静音或解除静音。

   开发方法与来电场景相同，详见[来电场景：静音与解除静音](incoming-calls.md#开发步骤)。
6. 去电场景，用户也可以拉起通知中心面板，在实况窗通知上点击挂断。

   开发方式与来电场景相同，详见[来电场景：用户点击挂断](incoming-calls.md#开发步骤)。
7. 通话结束后，可以解除voipCallUiEvent事件。

   示例代码如下：

   ```
   1. // 解除voipCallUiEvent事件
   2. voipCall.off('voipCallUiEvent', callback => {
   3. hilog.info(0x0000, 'CallDemo', `Succeeded in unRegistering voipCallUiEvent, callId: ${callback.callId}`);
   4. });
   ```
