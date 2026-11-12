---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/remote-voip-call-control
title: 外设VoIP通话控制
breadcrumb: 指南 > 应用服务 > Call Service Kit（通话服务） > 外设VoIP通话控制
category: harmonyos-guides
scraped_at: 2026-11-12T09:52:21+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:95f2452d6d555a486cbbd222a55c6667fa4e27ea39eaed051dd138722eaf2675
---

## 场景介绍

从API26.0.1版本开始，新增外设VoIP通话控制。

用户在远端设备（如第三方穿戴设备）上控制本设备的VoIP通话，称为外设VoIP通话控制场景。在该场景中，运行在远端设备上的应用可以接听、拒接当前来电，或者挂断当前通话。由系统选择待控制的VoIP通话，优先选择第一路通话，无需应用指定callId。

当前支持的操作如下：

* 接听来电：支持语音接听和视频接听两种方式，默认为语音接听。
* 拒接来电：拒接当前来电。
* 挂断通话：优先挂断激活态通话，如来电中不存在激活态通话，则挂断来电。

## 约束与限制

* 需要申请权限ohos.permission.MANAGE\_CALL\_FOR\_DEVICES，申请方式请参见[声明权限](declare-permissions.md)。
* 本设备上需存在可控制的VoIP通话（来电或通话中），否则调用会返回1007200004错误码。

### 使用限制

本端和远端设备需要打开蓝牙或WLAN开关，并确保本端与远端设备已配对并连接成功。

### 设备限制

本端设备：支持HarmonyOS 7及以上的Phone、Tablet、PC/2in1、Wearable设备。

## 接口说明

外设VoIP通话控制场景的接口，由[voipCallControl](../harmonyos-references/call-voipcallcontrol.md)提供。更多接口信息详见[接口文档](../harmonyos-references/call-voipcallcontrol.md)。

| 接口名 | 描述 |
| --- | --- |
| answerCall(videoState?: VideoStateType): Promise<void> | 接听当前来电，可通过videoState指定语音接听或视频接听。 |
| rejectCall(): Promise<void> | 拒接当前来电。 |
| hangUpCall(): Promise<void> | 挂断当前通话。 |

## 开发步骤

1. 在开发前，需要在应用的配置文件中声明权限ohos.permission.MANAGE\_CALL\_FOR\_DEVICES，申请方式请参见[声明权限](declare-permissions.md)。
2. 导入相关依赖。

   ```typescript
   import { voipCallControl } from '@kit.CallServiceKit';
   import { BusinessError } from '@kit.BasicServicesKit';
   import { hilog } from '@kit.PerformanceAnalysisKit';
   import { observer } from '@kit.TelephonyKit';
   ```
3. 调用[observer.onVoIPStateChange](../doccenter-references/api/js-apis-observer.md#observeronvoipstatechange)，监听voip通话状态。
4. 接听当前来电。

   语音接听：传入[TYPE\_VOICE](../harmonyos-references/call-voipcallcontrol.md#videostatetype)。

   示例代码如下：

   ```typescript
   // 语音接听当前来电
   voipCallControl.answerCall().then(() => {
     hilog.info(0x0000, 'CallDemo', 'Succeeded in answering the voice call.');
   }).catch((err: BusinessError) => {
     hilog.error(0x0000, 'CallDemo', 'Failed to answer the voice call: %{public}d %{public}s', err.code, err.message);
   });
   ```

   视频接听：传入[TYPE\_VIDEO](../harmonyos-references/call-voipcallcontrol.md#videostatetype)。

   示例代码如下：

   ```typescript
   // 视频接听当前来电
   voipCallControl.answerCall(voipCallControl.VideoStateType.TYPE_VIDEO).then(() => {
     hilog.info(0x0000, 'CallDemo', 'Succeeded in answering the video call.');
   }).catch((err: BusinessError) => {
     hilog.error(0x0000, 'CallDemo', 'Failed to answer the video call: %{public}d %{public}s', err.code, err.message);
   });
   ```
5. 拒接当前来电。

   示例代码如下：

   ```typescript
   // 拒接当前来电
   voipCallControl.rejectCall().then(() => {
     hilog.info(0x0000, 'CallDemo', 'Succeeded in rejecting the call.');
   }).catch((err: BusinessError) => {
     hilog.error(0x0000, 'CallDemo', 'Failed to reject the call: %{public}d %{public}s', err.code, err.message);
   });
   ```
6. 挂断当前通话。

   系统会选择待挂断的通话：优先挂断激活态通话，如来电中不存在激活态通话，则挂断来电。

   示例代码如下：

   ```typescript
   // 挂断当前通话
   voipCallControl.hangUpCall().then(() => {
     hilog.info(0x0000, 'CallDemo', 'Succeeded in hanging up the call.');
   }).catch((err: BusinessError) => {
     hilog.error(0x0000, 'CallDemo', 'Failed to hang up the call: %{public}d %{public}s', err.code, err.message);
   });
   ```
