---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-audio-58
title: AudioCapturer录音失败
breadcrumb: FAQ > 媒体开发 > 音频和视频 > 音频（Audio） > AudioCapturer录音失败
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:44+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:322871822395090198b20256554dbcbf1bb6c6998b6d87c41588dcf45e7c667c
---

## 问题现象

AudioCapturer录音失败，如何定位？

## 背景知识

* [AudioCapturer](../harmonyos-guides/using-audiocapturer-for-recording.md)是音频采集器，用于录制PCM（Pulse Code Modulation）音频数据，适合有音频开发经验的开发者实现更灵活的录制功能。
* [OHAudio](../harmonyos-guides/using-ohaudio-for-recording.md)是系统在API version 10中引入的一套C API，此API在设计上实现归一，同时支持普通音频通路和低时延通路。仅支持PCM格式，适用于依赖Native层实现音频输入功能的场景。

## 问题定位

1. 检查麦克风权限是否申请成功：
   * module.json5配置文件中是否已[声明麦克风权限](../harmonyos-guides/declare-permissions.md)：ohos.permission.MICROPHONE。
   * 代码中是否已主动[向用户申请权限](../harmonyos-guides/request-user-authorization.md)。
   * 用户是否已同意麦克风权限。当权限未申请成功时，调用audio.createAudioCapturer时会失败，报错信息如下：

   ```txt
   17:02:44.042   55177-55177   C02B8B/com.exa...AudioCapturer  com.examp...udiodemo  E     [CreateAudioCapturerNativeObject]Capturer Create failed
   17:02:44.042   55177-55177   C02B8B/com.exa...AudioCapturer  com.examp...udiodemo  E     [Construct]failed to CreateAudioCapturerNativeObject
   17:02:44.042   55177-55177   C01320/com.exa...diodemo/JsEnv  com.examp...udiodemo  W     [source_map145]the stack without line info
   17:02:44.043   55177-55177   A03D00/com.exa...diodemo/JSAPP  com.examp...udiodemo  E     Invoke createAudioCapturer failed, code is 6800301, message is system error
   ```
2. 确认权限申请成功后，需要调用audioCapturer.start起录音流开始录音，具体可参考[使用AudioCapturer开发音频录制功能](../harmonyos-guides/using-audiocapturer-for-recording.md)。
3. 音频录制需要在前台启动，启动后可以退后台（需要申请[长时任务](../harmonyos-guides/continuous-task.md)）。在后台启动录制将会失败。因焦点打断被暂停的录音流，后台重新启动录制也会失败，但是可以[设置静音打断模式](../harmonyos-guides/using-audiocapturer-for-recording.md#设置静音打断模式)，将打断策略从停止录音切换为静音录制。

## 分析结论

调用麦克风录音，属于隐私敏感功能，需要遵循系统的安全规范以及开发步骤。

## 修改建议

针对以上问题，排查并修复对应的功能。

## 常见FAQ

Q：AudioCapturer录制音频过程中，麦克风权限被禁止，此时AudioState状态为多少？

A：AudioState状态仍然是STATE\_RUNNING，但是后续录到的是静音数据。

Q：SOURCE\_TYPE\_VOICE\_RECOGNITION语音识别源类型为什么在连接车载蓝牙时候无法录音了？

A：SOURCE\_TYPE\_VOICE\_RECOGNITION语音识别源暂时不支持车载蓝牙。
