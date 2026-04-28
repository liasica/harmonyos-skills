---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-audio-record-base-on-audiocapturer
title: 基于AudioCapturer录制PCM音频（ArkTS）
breadcrumb: 最佳实践 > 媒体 > 音频和视频 > 音频录制系列开发实践 > 基于AudioCapturer录制PCM音频（ArkTS）
category: best-practices
scraped_at: 2026-04-28T08:20:39+08:00
doc_updated_at: 2026-03-17
content_hash: sha256:e97c0e290855b7b84000a39ee86cbdef663c6bde8a4e35c56bf8f3afc77489a4
---

## 概述

AudioCapturer是用于音频录制的ArkTS API，仅支持录制PCM格式，可以用于录制音频母带。本文适用于音频录制类应用的开发，针对市场上主流音频录制类应用的常见场景，介绍了基于AudioCapturer如何录制PCM音频，指导开发者基于不同的业务场景，使用AudioCapturer实现音频录制功能。

基于AudioCapturer录制PCM音频（ArkTS）实现的功能效果如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/UlDyp8Q5TKixpxvKRY409Q/zh-cn_image_0000002524061072.gif?HW-CC-KV=V1&HW-CC-Date=20260428T002033Z&HW-CC-Expire=86400&HW-CC-Sign=331B690D132AC2984B03DCBAF5542D0F94AFBF4E1A119FEF88783A2E00C1BE3C "点击放大")

本文的主要内容如下：

[基础录制](bpta-audio-record-base-on-audiocapturer.md#section20569101215108)：介绍了基于AudioCapturer录制PCM音频，包括开始录制、结束录制。

## 基础录制

### 实现原理

AudioCapturer可以录制PCM（Pulse Code Modulation）音频数据，能够快速实现PCM的基础录制，支持设置静音打断和回声消除。在创建完AudioCapturer后，需要设置对应的回调函数、音频录制的参数配置，通过readData的回调函数将采集的数据写入到文件中。

**图1** AudioCapturer状态变化示意图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0c/v3/i11zL9JzT368OISEwfV9Xw/zh-cn_image_0000002555220981.jpg?HW-CC-KV=V1&HW-CC-Date=20260428T002033Z&HW-CC-Expire=86400&HW-CC-Sign=22D240D9066EAC71D492518D50D11E11E31EFE7368C4AB789F8338DFD35F5D5E "点击放大")

### 开发步骤

1.配置音频采集参数。

* 音频采集参数分为2类：音频流信息[AudioStreamInfo](../harmonyos-references/arkts-apis-audio-i.md#audiostreaminfo8)（主要包括采样率、通道数、采样格式、编码格式等）和音频采集器信息[AudioCapturerInfo](../harmonyos-references/arkts-apis-audio-i.md#audiocapturerinfo8)（音频流类型，即录制业务场景和采集器标志）。
* 将配置好的参数audioCapturerOptions传入createAudioCapturer接口中，以创建音频采集器实例。
* 设置readData回调函数。该回调用于系统向PCM文件中写入采集到的音频数据。其中，Options用来标记每次写入的数据在文件中偏移量和大小。

```
1. async initCapturer(): Promise<void> {
2. try {
3. // Config AudioStreamInfo
4. let audioStreamInfo: audio.AudioStreamInfo = {
5. channels: audio.AudioChannel.CHANNEL_1, // Set channel
6. samplingRate: audio.AudioSamplingRate.SAMPLE_RATE_48000,  // Set samplingRate
7. sampleFormat: audio.AudioSampleFormat.SAMPLE_FORMAT_S16LE,  // Set sampleFormat
8. encodingType: audio.AudioEncodingType.ENCODING_TYPE_RAW,  // Set encodingType
9. };
10. // Config AudioCapturerInfo
11. let audioCapturerInfo: audio.AudioCapturerInfo = {
12. capturerFlags: 0,
13. source: audio.SourceType.SOURCE_TYPE_VOICE_COMMUNICATION,
14. };
15. // Config AudioCapturerOptions
16. let audioCapturerOptions: audio.AudioCapturerOptions = {
17. streamInfo: audioStreamInfo,
18. capturerInfo: audioCapturerInfo,
19. };

21. this.capturer = await audio.createAudioCapturer(audioCapturerOptions);
22. // Set if capturer want to be muted
23. this.capturer.setWillMuteWhenInterrupted(true).catch((error: BusinessError) => {
24. Logger.error(TAG, `setWillMuteWhenInterrupted error. message:${error.message}`);
25. });
26. // Set stateChange callback
27. this.capturer.on('stateChange', (state: audio.AudioState) => {
28. Logger.info(TAG, `Audio capturer state changed: ${state}`);
29. });
30. // Set readData callback
31. this.capturer.on('readData', (buffer: ArrayBuffer) => {
32. let options: WriteOptions = { offset: this.writeOffset, length: buffer.byteLength };
33. fileIo.writeSync(this.recordFile?.fd, buffer, options);
34. this.writeOffset += buffer.byteLength;
35. });
36. } catch (error) {
37. Logger.error(TAG, `initCapturer error. message:${(error as BusinessError).message}`);
38. }
39. }
```

[AudioCapturerController.ets](https://gitcode.com/HarmonyOS_Samples/audio-capturer-record-pcm/blob/master/entry/src/main/ets/controller/AudioCapturerController.ets#L39-L79)

2.开始音频录制。

```
1. async startCapturer(): Promise<void> {
2. if (this.capturer === undefined) {
3. throw new Error(`Release AudioCapturer at undefined state`);
4. }
5. let state = this.capturer.state;
6. if (state === audio.AudioState.STATE_INVALID) {
7. this.capturer = undefined;
8. throw new Error(`AudioCapturer at invalid state.`);
9. }
10. if (state !== audio.AudioState.STATE_PREPARED && state !== audio.AudioState.STATE_STOPPED) {
11. throw new Error(`Release AudioCapturer at wrong state, ${state}`);
12. }
13. try {
14. this.tmpPath = this.context?.filesDir + '/example.pcm';
15. let openMode = fileIo.OpenMode.WRITE_ONLY | fileIo.OpenMode.CREATE | fileIo.OpenMode.TRUNC;
16. this.recordFile = fileIo.openSync(this.tmpPath, openMode);
17. this.writeOffset = 0;
18. await this.capturer.start();
19. } catch (error) {
20. Logger.error(TAG, `startCapturer error. message:${(error as BusinessError).message}`);
21. }
22. }
```

[AudioCapturerController.ets](https://gitcode.com/HarmonyOS_Samples/audio-capturer-record-pcm/blob/master/entry/src/main/ets/controller/AudioCapturerController.ets#L87-L108)

3.停止音频录制。

```
1. async stopCapturer(): Promise<void> {
2. if (this.capturer === undefined) {
3. throw new Error(`Release AudioCapturer at undefined state`);
4. }
5. let state = this.capturer.state;
6. if (state === audio.AudioState.STATE_INVALID) {
7. this.capturer = undefined;
8. throw new Error(`AudioCapturer at invalid state.`);
9. }
10. if (state !== audio.AudioState.STATE_RUNNING) {
11. return;
12. }
13. try {
14. await this.capturer.stop();
15. fileIo.closeSync(this.recordFile?.fd);
16. } catch (error) {
17. Logger.error(TAG, `stopCapturer error. message:${(error as BusinessError).message}`);
18. }
19. }
```

[AudioCapturerController.ets](https://gitcode.com/HarmonyOS_Samples/audio-capturer-record-pcm/blob/master/entry/src/main/ets/controller/AudioCapturerController.ets#L116-L134)

4.取消监听事件，并释放资源。

```
1. async releaseCapturer(): Promise<void> {
2. if (this.capturer === undefined) {
3. throw new Error(`Release AudioCapturer at undefined state`);
4. }
5. let state = this.capturer.state;
6. if (state === audio.AudioState.STATE_INVALID) {
7. this.capturer = undefined;
8. throw new Error(`AudioCapturer at invalid state.`);
9. }
10. if (state !== audio.AudioState.STATE_PREPARED && state !== audio.AudioState.STATE_STOPPED) {
11. throw new Error(`Release AudioCapturer at wrong state, ${state}`);
12. }
13. try {
14. this.capturer.off('readData');
15. await this.capturer.release();
16. this.capturer = undefined;
17. } catch (error) {
18. Logger.error(TAG, `releaseCapturer error. message:${(error as BusinessError).message}`);
19. }
20. }
```

[AudioCapturerController.ets](https://gitcode.com/HarmonyOS_Samples/audio-capturer-record-pcm/blob/master/entry/src/main/ets/controller/AudioCapturerController.ets#L142-L161)

## 常见问题

### 设置静音打断模式

开发者在创建AudioCapturer实例时，调用[setWillMuteWhenInterrupted()](../harmonyos-references/arkts-apis-audio-audiocapturer.md#setwillmutewheninterrupted20)接口设置当前录制音频流是否启用静音打断模式。

```
1. // Set if capturer want to be muted
2. this.capturer.setWillMuteWhenInterrupted(true).catch((error: BusinessError) => {
3. Logger.error(TAG, `setWillMuteWhenInterrupted error. message:${error.message}`);
4. });
```

[AudioCapturerController.ets](https://gitcode.com/HarmonyOS_Samples/audio-capturer-record-pcm/blob/master/entry/src/main/ets/controller/AudioCapturerController.ets#L61-L64)

### 设置回声消除

开发者在设置audio.AudioCapturerInfo时，将[SourceType](../harmonyos-references/arkts-apis-audio-e.md#sourcetype8)值指定为SOURCE\_TYPE\_VOICE\_COMMUNICATION或SOURCE\_TYPE\_LIVE即可。

### 获取音频振幅

开发者在开发通讯软件的语音录制发送、音乐录制等场景时，为了体现当前录制音量的大小，需要实现音频录制波形。关于音频录制波形可以参考[基于AudioRenderer和AudioCapturer实现音频波形动画](bpta-audio-ripple-animation.md)。

## 示例代码

* [基于AudioCapturer录制音频(ArkTS)](https://gitcode.com/HarmonyOS_Samples/audio-capturer-record-pcm)
