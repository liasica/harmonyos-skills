---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-callservice-1
title: 应用内发起通话，已经接通后通话状态显示错误
breadcrumb: FAQ > 应用服务开发 > VoIP通话服务（Call Service Kit） > 应用内发起通话，已经接通后通话状态显示错误
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:47+08:00
doc_updated_at: 2026-08-12
content_hash: sha256:fa853e8d5ce563813aad46a4d463899d6695c67e2849ad6f8e5d505edeb5028d
---

## 问题现象

应用内主动发起通话，已经接通了，但是页面上通话状态还是显示“正在等待对方接听”。

## 背景知识

* [Call Service Kit](../harmonyos-guides/call-introduction.md)：通话服务是HarmonyOS为开发者提供的应用内通话管理服务。应用内通话，主要分为来电场景、去电场景两类。
  + 来电场景：应用接收到来自网络的音/视频通话，称为来电场景。
  + 去电场景：应用主动发起音/视频通话，称为去电场景。
* [voipCall.on('voipCallUiEvent')](../harmonyos-references/call-voipcall.md#voipcallonvoipcalluievent)：订阅[voipCallUiEvent](../harmonyos-references/call-voipcall.md#voipcalluievent)事件。
  + VOIP\_CALL\_EVENT\_VOICE\_ANSWER：通话语音接听事件。
  + VOIP\_CALL\_EVENT\_VIDEO\_ANSWER：通话视频接听事件。
* [voipCall.reportCallStateChange](../harmonyos-references/call-voipcall.md#voipcallreportcallstatechange-1)：通知应用内通话状态变化，并指定通话类型。
  + 通话状态可以参考[VoipCallState](../harmonyos-references/call-voipcall.md#voipcallstate)。
  + 通话类型可以参考[VoipCallType](../harmonyos-references/call-voipcall.md#voipcalltype)。

## 问题定位

1. 检查应用的通话方式：通过"voip"关键词搜索日志，得到如下日志，发现应用使用了Call Service Kit通话服务，还有音视频流、输入输出设备等一些信息的显示。

   ```txt
   02-09 18:06:43.923  1392 11037 I C02560/audio_host/audio_hw_primary: [reset_input_route_for_noise_reduction:143]: voip scene: 1, need noise reduction: 0, input route: communication-bt-sco-mic
   02-09 18:06:43.925  1392 11037 I C02560/audio_host/audio_capture_multimic: [multi_mic_voip:131]: voip 
   02-09 18:06:44.016  1392 11037 I C02562/audio_host/CustAudio: AlgoLib::Init:400: AlgoLib stream 14: to init algo for voipprocessing_module_voip_tx,in_device=0x80000008,out_device=0x10,source=7
   02-09 18:07:18.163  1456  2662 I C02B2E/media_service/ScreenCaptureServer: #2351 OnVoIPStatusChanged, isInVoIPCall:1
   02-09 18:07:18.222   805  2358 I C02B87/audio_server/AudioStreamCollector: [ChangeVoipCapturerStreamToNormal]Has capture stream count: 2
   02-09 18:07:18.222   805  2358 W C02B8B/audio_server/AudioPolicyService: [GetPreferredInputStreamTypeInner]Voip Change To Normal
   02-09 18:07:18.225   805 32577 I C02B89/audio_server/AudioRendererSinkInner: [SetAudioParameter]SetAudioParameter: key 0, condition: , value: VOIP_APPSCENE=0;
   ```
2. 搜索"VOIP\_CALL\_EVENT\_VIDEO\_ANSWER"、"VOIP\_CALL\_VIDEO"、"VoipCallState"、"reportCallStateChange"等日志关键词，发现日志中并没有关于应用视频通话接听事件、通话状态变化的信息打印，判断该应用未监听通话状态。

## 分析结论

应用在发起通话和接听通话后都没有监听通话状态，导致页面一直显示“正在等待对方接听”。

## 修改建议

* 建议在应用内通话中调用[voipCall.on('voipCallUiEvent')](../harmonyos-references/call-voipcall.md#voipcallonvoipcalluievent)监听通话事件，当监听到通话视频接听事件时，调用[voipCall.reportCallStateChange](../harmonyos-references/call-voipcall.md#voipcallreportcallstatechange-1)通知通话状态变化，并更新页面UI通话状态显示“通话中。
* 构建上报去电的参数，向Call Service Kit上报去电，参考[voipCall.reportOutgoingCall](../harmonyos-references/call-voipcall.md#voipcallreportoutgoingcall)。
