---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/using-audiocapturer-for-recording
title: 使用AudioCapturer开发音频录制功能(ArkTs)
breadcrumb: 指南 > 媒体 > Audio Kit（音频服务） > 音频录制 > 使用AudioCapturer开发音频录制功能(ArkTs)
category: harmonyos-guides
scraped_at: 2026-04-29T13:34:32+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:bdae4455a5d8ee33a61835b5d836f7d1f81564fef7004cf05ca6d64f28134702
---

AudioCapturer是音频采集器，用于录制PCM（Pulse Code Modulation）音频数据，适合有音频开发经验的开发者实现更灵活的录制功能。

## 开发指导

使用AudioCapturer录制音频涉及到AudioCapturer实例的创建、音频采集参数的配置、采集的开始与停止、资源的释放等。本开发指导将以一次录制音频数据的过程为例，向开发者讲解如何使用AudioCapturer进行音频录制，建议搭配[AudioCapturer](../harmonyos-references/arkts-apis-audio-audiocapturer.md)的API说明阅读。

下图展示了AudioCapturer的状态变化，在创建实例后，调用对应的方法可以进入指定的状态实现对应的行为。需要注意的是在确定的状态执行不合适的方法可能导致AudioCapturer发生错误，建议开发者在调用状态转换的方法前进行状态检查，避免程序运行产生预期以外的结果。

**图1** AudioCapturer状态变化示意图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/RXYWBJi1RtSpCIT2lnZT_w/zh-cn_image_0000002558605374.png?HW-CC-KV=V1&HW-CC-Date=20260429T053430Z&HW-CC-Expire=86400&HW-CC-Sign=66DCDD1BEA7BA276B64995E84C55D79EBC01D28DEE59E8B425AB377202A256C9)

使用[on('stateChange')](../harmonyos-references/arkts-apis-audio-audiocapturer.md#onstatechange8)方法可以监听AudioCapturer的状态变化，每个状态对应值与说明见[AudioState](../harmonyos-references/arkts-apis-audio-e.md#audiostate8)。

### 开发步骤及注意事项

以下各步骤示例为片段代码，可通过示例代码右下方链接获取[完整示例](https://gitcode.com/openharmony/applications_app_samples/blob/master/code/DocsSample/Media/Audio/AudioCaptureSampleJS)。

1. 配置音频采集参数并创建AudioCapturer实例，音频采集参数的详细信息可以查看[AudioCapturerOptions](../harmonyos-references/arkts-apis-audio-i.md#audiocaptureroptions8)。

   说明

   当设置Mic音频源（即[SourceType](../harmonyos-references/arkts-apis-audio-e.md#sourcetype8)为SOURCE\_TYPE\_MIC、SOURCE\_TYPE\_VOICE\_RECOGNITION、SOURCE\_TYPE\_VOICE\_COMMUNICATION、SOURCE\_TYPE\_VOICE\_MESSAGE、SOURCE\_TYPE\_LIVE（从API version 20开始支持））时，需要申请麦克风权限ohos.permission.MICROPHONE，申请方式参考：[向用户申请授权](request-user-authorization.md)。

   ```
   1. import { audio } from '@kit.AudioKit';
   2. // ...
   3. let audioStreamInfo: audio.AudioStreamInfo = {
   4. samplingRate: audio.AudioSamplingRate.SAMPLE_RATE_48000, // 采样率。
   5. channels: audio.AudioChannel.CHANNEL_2, // 通道。
   6. sampleFormat: audio.AudioSampleFormat.SAMPLE_FORMAT_S16LE, // 采样格式。
   7. encodingType: audio.AudioEncodingType.ENCODING_TYPE_RAW // 编码格式。
   8. };
   9. let audioCapturerInfo: audio.AudioCapturerInfo = {
   10. source: audio.SourceType.SOURCE_TYPE_MIC, // 音源类型:Mic音频源。根据业务场景配置,参考SourceType。
   11. capturerFlags: 0 // 音频采集器标志。
   12. };
   13. let audioCapturerOptions: audio.AudioCapturerOptions = {
   14. streamInfo: audioStreamInfo,
   15. capturerInfo: audioCapturerInfo
   16. };
   17. // ...
   18. audio.createAudioCapturer(audioCapturerOptions, (err, capturer) => { // 创建AudioCapturer实例。
   19. if (err) {
   20. console.error(`Invoke createAudioCapturer failed, code is ${err.code}, message is ${err.message}`);
   21. // ...
   22. return;
   23. }
   24. console.info(`${TAG}: create AudioCapturer success`);
   25. // ...
   26. audioCapturer = capturer;
   27. if (audioCapturer !== undefined) {
   28. audioCapturer.on('readData', readDataCallback);
   29. // ...
   30. }
   31. });
   ```
2. 调用[on('readData')](../harmonyos-references/arkts-apis-audio-audiocapturer.md#onreaddata11)方法，订阅监听音频数据读入回调。

   注意

   * **线程管理**：不建议使用多线程来处理数据读取。若需使用多线程读取数据，需要做好线程管理。
   * **线程耗时**：readData 方法所在的线程中，不建议执行耗时任务。否则可能会导致数据处理线程响应回调延迟，进而引发录音数据缺失、卡顿、杂音等音频效果问题。
   * **注册回调**：开发者应避免在主线程中注册回调，以免被其他业务阻塞导致响应回调不及时造成卡顿。建议使用独立的异步线程池处理回调。

   ```
   1. import { BusinessError } from '@kit.BasicServicesKit';
   2. import { fileIo as fs } from '@kit.CoreFileKit';
   3. import { common, abilityAccessCtrl, PermissionRequestResult } from '@kit.AbilityKit';
   4. // ...
   5. class Options {
   6. public offset?: number;
   7. public length?: number;
   8. }
   9. // ...
   10. let bufferSize: number = 0;
   11. let path = context.cacheDir;
   12. let filePath = path + '/StarWars10s-2C-48000-4SW.pcm';
   13. file = fs.openSync(filePath, fs.OpenMode.READ_WRITE | fs.OpenMode.CREATE);
   14. readDataCallback = (buffer: ArrayBuffer) => {
   15. let options: Options = {
   16. offset: bufferSize,
   17. length: buffer.byteLength
   18. }
   19. fs.writeSync(file.fd, buffer, options);
   20. bufferSize += buffer.byteLength;
   21. };
   22. // ...
   23. audioCapturer.on('readData', readDataCallback);
   ```
3. 调用[start](../harmonyos-references/arkts-apis-audio-audiocapturer.md#start8)方法进入running状态，开始录制音频。

   ```
   1. import { BusinessError } from '@kit.BasicServicesKit';
   2. // ...
   3. audioCapturer.start((err: BusinessError) => {
   4. if (err) {
   5. // ...
   6. console.error('Capturer start failed.');
   7. } else {
   8. // ...
   9. console.info('Capturer start success.');
   10. }
   11. });
   ```
4. 调用[stop](../harmonyos-references/arkts-apis-audio-audiocapturer.md#stop8)方法停止录制。

   ```
   1. import { BusinessError } from '@kit.BasicServicesKit';
   2. // ...
   3. audioCapturer.stop((err: BusinessError) => {
   4. if (err) {
   5. // ...
   6. console.error('Capturer stop failed.');
   7. } else {
   8. // ...
   9. console.info('Capturer stop success.');
   10. }
   11. });
   ```
5. 调用[release](../harmonyos-references/arkts-apis-audio-audiocapturer.md#release8)方法销毁实例，释放资源。

   ```
   1. import { BusinessError } from '@kit.BasicServicesKit';
   2. // ...
   3. audioCapturer.release((err: BusinessError) => {
   4. if (err) {
   5. // ...
   6. console.error('Capturer release failed.');
   7. } else {
   8. fs.closeSync(file);
   9. console.info('Capturer release success.');
   10. // ...
   11. }
   12. });
   ```

### 完整示例

下面展示了使用AudioCapturer录制音频的完整示例代码。

```
1. import { audio } from '@kit.AudioKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { fileIo as fs } from '@kit.CoreFileKit';
4. import { common, abilityAccessCtrl, PermissionRequestResult } from '@kit.AbilityKit';
5. const TAG = 'AudioCapturerDemo';
6. class Options {
7. public offset?: number;
8. public length?: number;
9. }

11. let audioCapturer: audio.AudioCapturer | undefined = undefined;
12. let audioStreamInfo: audio.AudioStreamInfo = {
13. samplingRate: audio.AudioSamplingRate.SAMPLE_RATE_48000, // 采样率。
14. channels: audio.AudioChannel.CHANNEL_2, // 通道。
15. sampleFormat: audio.AudioSampleFormat.SAMPLE_FORMAT_S16LE, // 采样格式。
16. encodingType: audio.AudioEncodingType.ENCODING_TYPE_RAW // 编码格式。
17. };
18. let audioCapturerInfo: audio.AudioCapturerInfo = {
19. source: audio.SourceType.SOURCE_TYPE_MIC, // 音源类型:Mic音频源。根据业务场景配置,参考SourceType。
20. capturerFlags: 0 // 音频采集器标志。
21. };
22. let audioCapturerOptions: audio.AudioCapturerOptions = {
23. streamInfo: audioStreamInfo,
24. capturerInfo: audioCapturerInfo
25. };
26. let file: fs.File;
27. let readDataCallback: Callback<ArrayBuffer>;

29. // ...

31. async function initArguments(context: common.UIAbilityContext): Promise<void> {
32. let bufferSize: number = 0;
33. let path = context.cacheDir;
34. let filePath = path + '/StarWars10s-2C-48000-4SW.pcm';
35. file = fs.openSync(filePath, fs.OpenMode.READ_WRITE | fs.OpenMode.CREATE);
36. readDataCallback = (buffer: ArrayBuffer) => {
37. let options: Options = {
38. offset: bufferSize,
39. length: buffer.byteLength
40. }
41. fs.writeSync(file.fd, buffer, options);
42. bufferSize += buffer.byteLength;
43. };
44. }

46. // 初始化,创建实例,设置监听事件。
47. async function init(updateCallback?: (msg: string, isError: boolean) => void, stateCallback?:
48. (msg: string) => void): Promise<void> {
49. audio.createAudioCapturer(audioCapturerOptions, (err, capturer) => { // 创建AudioCapturer实例。
50. if (err) {
51. console.error(`Invoke createAudioCapturer failed, code is ${err.code}, message is ${err.message}`);
52. // ...
53. return;
54. }
55. console.info(`${TAG}: create AudioCapturer success`);
56. // ...
57. audioCapturer = capturer;
58. if (audioCapturer !== undefined) {
59. audioCapturer.on('readData', readDataCallback);
60. // ...
61. }
62. });
63. }

65. // 开始一次音频采集。
66. async function start(updateCallback?: (msg: string, isError: boolean) => void): Promise<void> {
67. if (audioCapturer !== undefined) {
68. let stateGroup = [audio.AudioState.STATE_PREPARED,
69. audio.AudioState.STATE_PAUSED, audio.AudioState.STATE_STOPPED];
70. // 当且仅当状态为STATE_PREPARED、STATE_PAUSED和STATE_STOPPED之一时才能启动采集。
71. if (stateGroup.indexOf(audioCapturer.state.valueOf()) === -1) {
72. console.error(`${TAG}: start failed`);
73. // ...
74. return;
75. }

77. // 启动采集。
78. audioCapturer.start((err: BusinessError) => {
79. if (err) {
80. // ...
81. console.error('Capturer start failed.');
82. } else {
83. // ...
84. console.info('Capturer start success.');
85. }
86. });
87. }
88. }

90. // 停止采集。
91. async function stop(updateCallback?: (msg: string, isError: boolean) => void): Promise<void> {
92. if (audioCapturer !== undefined) {
93. // 只有采集器状态为STATE_RUNNING或STATE_PAUSED的时候才可以停止。
94. if (audioCapturer.state.valueOf() !== audio.AudioState.STATE_RUNNING &&
95. audioCapturer.state.valueOf() !== audio.AudioState.STATE_PAUSED) {
96. console.info('Capturer is not running or paused');
97. // ...
98. return;
99. }

101. // 停止采集。
102. audioCapturer.stop((err: BusinessError) => {
103. if (err) {
104. // ...
105. console.error('Capturer stop failed.');
106. } else {
107. // ...
108. console.info('Capturer stop success.');
109. }
110. });
111. }
112. }

114. // 销毁实例,释放资源。
115. async function release(updateCallback?: (msg: string, isError: boolean) => void): Promise<void> {
116. if (audioCapturer !== undefined) {
117. // 采集器状态不是STATE_RELEASED或STATE_NEW状态,才能release。
118. if (audioCapturer.state.valueOf() === audio.AudioState.STATE_RELEASED ||
119. audioCapturer.state.valueOf() === audio.AudioState.STATE_NEW) {
120. console.info('Capturer already released');
121. // ...
122. return;
123. }

125. // 释放资源。
126. audioCapturer.release((err: BusinessError) => {
127. if (err) {
128. // ...
129. console.error('Capturer release failed.');
130. } else {
131. fs.closeSync(file);
132. console.info('Capturer release success.');
133. // ...
134. }
135. });
136. }
137. }

139. // ...

141. // ...
```

### 设置静音打断模式

如果需要实现录音全程不被系统基于焦点并发规则打断的效果，提供将打断策略从停止录音切换为静音录制的功能，录音过程中也不影响其他应用启动录音。开发者在创建AudioCapturer实例时，调用[setWillMuteWhenInterrupted](../harmonyos-references/arkts-apis-audio-audiocapturer.md#setwillmutewheninterrupted20)接口设置是否开启静音打断模式。默认不开启，此时由音频焦点策略管理并发音频流的执行顺序。开启后，被其他应用打断导致停止或暂停录制时会进入静音录制状态，在此状态下录制的音频没有声音。

### 回声消除功能

回声消除功能可在支持的设备上有效消除录音过程中的回声干扰，提升音频采集质量。开发者可通过指定特定的Mic音频源[SourceType](../harmonyos-references/arkts-apis-audio-e.md#sourcetype8)（SOURCE\_TYPE\_VOICE\_COMMUNICATION、SOURCE\_TYPE\_LIVE）来启用该功能，系统将会自动对采集的音频信号进行回声消除处理。

在启用前，建议先调用[isAcousticEchoCancelerSupported](../harmonyos-references/arkts-apis-audio-audiostreammanager.md#isacousticechocancelersupported20)接口（从API version 20开始支持）查询当前设备对音频输入源类型[SourceType](../harmonyos-references/arkts-apis-audio-e.md#sourcetype8)是否支持回声消除功能，以确保功能的可用性。若支持，则可在创建音频录制构造器时设置相应的Mic音频源，从而激活回声消除处理流程。
