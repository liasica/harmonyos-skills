---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-audio-record-base-on-avrecorder-arkts
title: 基于AVRecorder录制格式化音频（ArkTS）
breadcrumb: 最佳实践 > 媒体 > 音频和视频 > 音频录制系列开发实践 > 基于AVRecorder录制格式化音频（ArkTS）
category: best-practices
scraped_at: 2026-04-28T08:20:39+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:c0aea27812800465d7d67661f6dcc467f30b5a22a7eabdb41896880005bdd3e5
---

## 概述

AVRecorder集成了音频输入录制、音频编码和媒体封装的功能，可以快速实现音频录制，输出文件格式支持m4a、mp3等格式。本文适用于音频录制类应用的开发，针对市场上主流音频录制类应用的常见场景，介绍了在ArkTS侧基于AVRecorder如何录制格式化音频，指导开发者实现基础录制。

基于AVRecorder录制格式化音频（ArkTS）实现的功能效果如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/RIYVxnGXSAi80mE_vqXkew/zh-cn_image_0000002524061074.gif?HW-CC-KV=V1&HW-CC-Date=20260428T002038Z&HW-CC-Expire=86400&HW-CC-Sign=FBF2B2F7758C8E5C02CFC81286DDB0EF46985CDED91E81A081B0D1E381D568CD "点击放大")

本文的主要内容如下：

[基础录制](bpta-audio-record-base-on-avrecorder-arkts.md#section20569101215108)：介绍了在ArkTS侧基于AVRecorder录制格式化音频，包括开始录制、暂停录制、结束录制。

## 基础录制

### 实现原理

为了方便开发者录制并输出格式化音频文件，HarmonyOS提供了AVRecorder录制器，用于音频数据采集、音频编码以及音频文件封装等端到端一体化音频录制。AVRecorder输出文件格式支持m4a、mp3等格式，支持设置静音打断和回声消除，便于快速实现音频录制的功能。例如，开发者可以直接调用设备硬件如麦克风录音，并生成m4a音频文件。

AVRecorder提供了开始录制、暂停录制、恢复录制、停止录制、释放资源等功能。其整个开发流程可以概括为：AVRecorder实例创建、采集回调注册（各类事件监听）、音频采集参数配置、采集的开始与停止以及资源的释放等。其中，事件监听主要包括音频焦点中断事件监听和音频录制流状态监听。在创建完实例后，开发者可以调用相关方法使得音频录制流进入对应的状态。如果在确定的状态调用不合适的方法，则可能导致不可预期的错误，所以开发过程中应该严格遵循状态机要求，如只能在paused状态下调用resume()接口。

**图1** 录制状态变化示意图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/Q4g4KXTRS-ms-9R358kvkA/zh-cn_image_0000002555220983.png?HW-CC-KV=V1&HW-CC-Date=20260428T002038Z&HW-CC-Expire=86400&HW-CC-Sign=3224073E114A3074453FBC97D1BC3316BA6815D33D6D1005323A2802906BA66A "点击放大")

### 开发步骤

1.创建AVRecorder对象。

```
1. private avRecorder: media.AVRecorder | undefined = undefined;

3. // Create an avRecorder instance
4. public async initAVRecorder() {
5. try {
6. this.avRecorder = await media.createAVRecorder();
7. // Set if recorder want to be muted
8. this.avRecorder.setWillMuteWhenInterrupted(true).catch((error: BusinessError) => {
9. Logger.error(`Failed to setWillMuteWhenInterrupted, error code: ${error.code}, message: ${error.message}`);
10. });
11. } catch (err) {
12. let error: BusinessError = err as BusinessError;
13. Logger.error(`Failed to create avRecorder, error code: ${error.code}, message: ${error.message}`);
14. }
15. }
```

[RecorderController.ets](https://gitcode.com/HarmonyOS_Samples/avrecorder-record-formatted-audio-arkts/blob/master/entry/src/main/ets/controller/RecorderController.ets#L23-L37)

2.设置AVRecorder的相关参数，在进入prepare状态后，开启音频录制。

* 设置音频录制AVRecorderProfile的参数配置，包括采样率、采样通道、音频格式等。
* 设置音频录制AVRecorderConfig的参数配置，包括音频源类型、录制输出的URL等。
* 调用prepare()接口，进入prepare状态。在进入prepare状态后，调用startRecorder()接口。

```
1. // Configure audio recording parameters
2. public prepareAVRecorder(uiContext: Context | undefined) {
3. if (!uiContext) {
4. return;
5. }
6. // Audio recording configuration file
7. let avProfile: media.AVRecorderProfile = {
8. audioBitrate: 112000, // Audio Bit Rate
9. audioChannels: 2, // Number of audio channels
10. audioCodec: media.CodecMimeType.AUDIO_MP3, // Audio encoding format
11. audioSampleRate: 48000, // Audio sampling rate
12. fileFormat: media.ContainerFormatType.CFT_MP3, // Container format
13. };

15. let filePath: string = uiContext.filesDir + '/example.mp3';
16. try {
17. let audioFile: fs.File = fs.openSync(filePath, fs.OpenMode.READ_WRITE | fs.OpenMode.CREATE | fs.OpenMode.TRUNC);
18. let fileFd: number = audioFile?.fd as number;
19. // Parameter settings for audio recording
20. let avConfig: media.AVRecorderConfig = {
21. audioSourceType: media.AudioSourceType.AUDIO_SOURCE_TYPE_VOICE_COMMUNICATION, // Audio input source, set as microphone here
22. profile: avProfile,
23. url: 'fd://' + fileFd.toString(),
24. };
25. if (this.avRecorder?.state === 'idle' || this.avRecorder?.state === 'stopped') {
26. this.avRecorder?.prepare(avConfig, (err: BusinessError) => {
27. if (!err) {
28. this.startRecorder();
29. }
30. });
31. }
32. } catch (error) {
33. let err: BusinessError = error as BusinessError;
34. Logger.error(`Failed to open file, error code: ${err.code}, message: ${err.message}`);
35. }
36. }
```

[RecorderController.ets](https://gitcode.com/HarmonyOS_Samples/avrecorder-record-formatted-audio-arkts/blob/master/entry/src/main/ets/controller/RecorderController.ets#L41-L76)

3.调用start()接口，开始音频录制。

```
1. // Start recording
2. public startRecorder() {
3. this.avRecorder?.start((err: BusinessError) => {
4. if (!err) {
5. Logger.info('Succeeded in start avRecorder');
6. }
7. });
8. }
```

[RecorderController.ets](https://gitcode.com/HarmonyOS_Samples/avrecorder-record-formatted-audio-arkts/blob/master/entry/src/main/ets/controller/RecorderController.ets#L80-L87)

4.暂停音频录制。

```
1. // Pause recording
2. public pauseRecorder() {
3. this.avRecorder?.pause((err: BusinessError) => {
4. if (!err) {
5. Logger.info('Succeeded in pause avRecorder');
6. }
7. });
8. }
```

[RecorderController.ets](https://gitcode.com/HarmonyOS_Samples/avrecorder-record-formatted-audio-arkts/blob/master/entry/src/main/ets/controller/RecorderController.ets#L91-L98)

5.恢复音频录制。

```
1. // Resume recording
2. public resumeRecorder() {
3. this.avRecorder?.resume((err: BusinessError) => {
4. if (!err) {
5. Logger.info('Succeeded in resume avRecorder');
6. }
7. });
8. }
```

[RecorderController.ets](https://gitcode.com/HarmonyOS_Samples/avrecorder-record-formatted-audio-arkts/blob/master/entry/src/main/ets/controller/RecorderController.ets#L102-L109)

6.停止音频录制。

```
1. // Stop recording
2. public stopRecorder() {
3. this.avRecorder?.stop((err: BusinessError) => {
4. if (!err) {
5. Logger.info('Succeeded in stop avRecorder');
6. }
7. });
8. }
```

[RecorderController.ets](https://gitcode.com/HarmonyOS_Samples/avrecorder-record-formatted-audio-arkts/blob/master/entry/src/main/ets/controller/RecorderController.ets#L113-L120)

7.释放音频录制资源。

```
1. // Release audio recording resources
2. public releaseRecorder() {
3. this.avRecorder?.release((err: BusinessError) => {
4. if (!err) {
5. Logger.info('Succeeded in release avRecorder');
6. }
7. });
8. }
```

[RecorderController.ets](https://gitcode.com/HarmonyOS_Samples/avrecorder-record-formatted-audio-arkts/blob/master/entry/src/main/ets/controller/RecorderController.ets#L124-L131)

## 常见问题

### 设置静音打断模式

通过调用[setWillMuteWhenInterrupted()](../harmonyos-references/arkts-apis-media-avrecorder.md#setwillmutewheninterrupted20)接口设置是否开启静音打断模式。

### 设置回声消除

通过将AudioSourceType值指定为AUDIO\_SOURCE\_TYPE\_VOICE\_COMMUNICATION即可。

## 示例代码

* [基于AVRecorder录制音频（ArkTS）](https://gitcode.com/HarmonyOS_Samples/avrecorder-record-formatted-audio-arkts)
