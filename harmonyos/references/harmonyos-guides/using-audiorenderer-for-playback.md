---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/using-audiorenderer-for-playback
title: 使用AudioRenderer开发音频播放功能(ArkTs)
breadcrumb: 指南 > 媒体 > Audio Kit（音频服务） > 音频播放 > 使用AudioRenderer开发音频播放功能(ArkTs)
category: harmonyos-guides
scraped_at: 2026-04-29T13:34:28+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:6d15087a841efbc425b8b558be82d546ba599d62aff4423a03659a5b5055c706
---

AudioRenderer是音频渲染器，用于播放PCM（Pulse Code Modulation）音频数据，相比[AVPlayer](using-avplayer-for-playback.md)而言，可以在输入前添加数据预处理，更适合有音频开发经验的开发者，以实现更灵活的播放功能。

## 开发指导

使用AudioRenderer播放音频涉及到AudioRenderer实例的创建、音频渲染参数的配置、渲染的开始与停止、资源的释放等。本开发指导将以一次渲染音频数据的过程为例，向开发者讲解如何使用AudioRenderer进行音频渲染，建议搭配[AudioRenderer](../harmonyos-references/arkts-apis-audio-audiorenderer.md)的API说明阅读。

下图展示了AudioRenderer的状态变化，在创建实例后，调用对应的方法可以进入指定的状态实现对应的行为。需要注意的是在确定的状态执行不合适的方法可能导致AudioRenderer发生错误，建议开发者在调用状态转换的方法前进行状态检查，避免程序运行产生预期以外的结果。

为保证UI线程不被阻塞，大部分AudioRenderer调用都是异步的。对于每个API均提供了callback函数和Promise函数，以下示例均采用callback函数。

**图1** AudioRenderer状态变化示意图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/AvxulecERGqyAKdQI4u-KA/zh-cn_image_0000002589244833.png?HW-CC-KV=V1&HW-CC-Date=20260429T053427Z&HW-CC-Expire=86400&HW-CC-Sign=73DD1A929D667149E1B74A4E38259AD9D5AA9C4361820B226DCBBACE44DF1DB1)

在进行应用开发的过程中，建议开发者通过[on('stateChange')](../harmonyos-references/arkts-apis-audio-audiorenderer.md#onstatechange8)方法订阅AudioRenderer的状态变更。因为针对AudioRenderer的某些操作，仅在音频播放器在固定状态时才能执行。如果应用在音频播放器处于错误状态时执行操作，系统可能会抛出异常或生成其他未定义的行为。

* prepared状态：通过调用[audio.createAudioRenderer](../harmonyos-references/arkts-apis-audio-f.md#audiocreateaudiorenderer8)方法进入到该状态。
* running状态：正在进行音频数据播放，可以在prepared状态通过调用[start](../harmonyos-references/arkts-apis-audio-audiorenderer.md#start8)方法进入此状态，也可以在paused状态和stopped状态通过调用[start](../harmonyos-references/arkts-apis-audio-audiorenderer.md#start8)方法进入此状态。
* paused状态：在running状态可以通过调用[pause](../harmonyos-references/arkts-apis-audio-audiorenderer.md#pause8)方法暂停音频数据的播放并进入paused状态，暂停播放之后可以通过调用[start](../harmonyos-references/arkts-apis-audio-audiorenderer.md#start8)方法继续音频数据播放。
* stopped状态：在paused/running状态可以通过[stop](../harmonyos-references/arkts-apis-audio-audiorenderer.md#stop8)方法停止音频数据的播放。
* released状态：在prepared、paused、stopped等状态，用户均可通过[release](../harmonyos-references/arkts-apis-audio-audiorenderer.md#release8)方法释放掉所有占用的硬件和软件资源，并且不会再进入到其他的任何一种状态了。

### 开发步骤及注意事项

以下各步骤示例为片段代码，可通过示例代码右下方链接获取[完整示例](https://gitcode.com/openharmony/applications_app_samples/blob/master/code/DocsSample/Media/Audio/AudioRendererSampleJS)。

1. 配置音频渲染参数并创建AudioRenderer实例，音频渲染参数的详细信息可以查看[AudioRendererOptions](../harmonyos-references/arkts-apis-audio-i.md#audiorendereroptions8)。

   ```
   1. import { audio } from '@kit.AudioKit';
   2. // ...
   3. let audioStreamInfo: audio.AudioStreamInfo = {
   4. samplingRate: audio.AudioSamplingRate.SAMPLE_RATE_48000, // 采样率。
   5. channels: audio.AudioChannel.CHANNEL_2, // 通道。
   6. sampleFormat: audio.AudioSampleFormat.SAMPLE_FORMAT_S16LE, // 采样格式。
   7. encodingType: audio.AudioEncodingType.ENCODING_TYPE_RAW // 编码格式。
   8. };
   9. let audioRendererInfo: audio.AudioRendererInfo = {
   10. usage: audio.StreamUsage.STREAM_USAGE_MUSIC, // 音频流使用类型：音乐。根据业务场景配置，参考StreamUsage。
   11. rendererFlags: 0 // 音频渲染器标志。
   12. };
   13. let audioRendererOptions: audio.AudioRendererOptions = {
   14. streamInfo: audioStreamInfo,
   15. rendererInfo: audioRendererInfo
   16. };
   17. // ...
   18. audio.createAudioRenderer(audioRendererOptions, (err, renderer) => { // 创建AudioRenderer实例。
   19. if (!err) {
   20. console.info(`${TAG}: creating AudioRenderer success`);
   21. // ...
   22. audioRenderer = renderer;
   23. if (audioRenderer !== undefined) {
   24. audioRenderer.on('writeData', writeDataCallback);
   25. // ...
   26. }
   27. } else {
   28. console.info(`${TAG}: creating AudioRenderer failed, error: ${err.message}`);
   29. globalLogUpdate(`${TAG}: creating AudioRenderer failed, error: ${err.message}`, false);
   30. }
   31. });
   ```
2. 调用[on('writeData')](../harmonyos-references/arkts-apis-audio-audiorenderer.md#onwritedata11)方法，订阅监听音频数据写入回调，推荐使用API version 12支持返回回调结果的方式。

   * API version 12开始该方法支持返回回调结果，系统可以根据开发者返回的值来决定此次回调中的数据是否播放。

     注意

     + 能填满回调所需长度数据的情况下，返回audio.AudioDataCallbackResult.VALID，系统会取用完整长度的数据缓冲进行播放。请不要在未填满数据的情况下返回audio.AudioDataCallbackResult.VALID，否则会导致杂音、卡顿等现象。
     + 在无法填满回调所需长度数据的情况下，建议开发者返回audio.AudioDataCallbackResult.INVALID，系统不会处理该段音频数据，然后会再次向应用请求数据，确认数据填满后返回audio.AudioDataCallbackResult.VALID。
     + 回调函数结束后，音频服务会把缓冲中数据放入队列里等待播放，因此请勿在回调外再次更改缓冲中的数据。对于最后一帧，如果数据不够填满缓冲长度，开发者需要使用剩余数据拼接空数据的方式，将缓冲填满，避免缓冲内的历史脏数据对播放效果产生不良的影响。

     ```
     1. import { audio } from '@kit.AudioKit';
     2. import { BusinessError } from '@kit.BasicServicesKit';
     3. import { fileIo as fs } from '@kit.CoreFileKit';
     4. import { common } from '@kit.AbilityKit';
     5. // ...
     6. class Options {
     7. public offset?: number;
     8. public length?: number;
     9. }
     10. // ...
     11. let bufferSize: number = 0;
     12. let file = await context.resourceManager.getRawFd('32_xiyouji.pcm');
     13. writeDataCallback = (buffer: ArrayBuffer) => {
     14. let options: Options = {
     15. offset: bufferSize,
     16. length: buffer.byteLength
     17. };
     18. // ...
     19. audioRenderer.on('writeData', writeDataCallback);
     ```
   * API version 11该方法不支持返回回调结果，系统默认回调中的数据均为有效数据。

     注意

     + 开发者应避免在主线程中注册回调，以免被其他业务阻塞导致响应回调不及时造成卡顿。建议使用独立的异步线程池处理回调。
     + 请确保填满回调所需长度数据，否则会导致杂音、卡顿等现象。
     + 在无法填满回调所需长度数据的情况下，建议开发者选择暂时停止写入数据（不暂停音频流），阻塞回调函数，等待数据充足时，再继续写入数据，确保数据填满。在阻塞回调函数后，如需调用AudioRenderer相关接口，需先解阻塞。
     + 开发者如果不希望播放本次回调中的音频数据，可以主动将回调中的数据块置空（置空后，也会被系统统计到已写入的数据，播放静音帧）。
     + 回调函数结束后，音频服务会把缓冲中数据放入队列里等待播放，因此请勿在回调外再次更改缓冲中的数据。对于最后一帧，如果数据不够填满缓冲长度，开发者需要使用剩余数据拼接空数据的方式，将缓冲填满，避免缓冲内的历史脏数据对播放效果产生不良的影响。
     + 在写数据回调中，避免与耗时业务耦合或等待其他业务操作，例如写数据时不要等待UI绘制。否则，可能会导致数据传输不及时，从而产生卡顿现象。

     ```
     1. import { audio } from '@kit.AudioKit';
     2. import { BusinessError } from '@kit.BasicServicesKit';
     3. import { fileIo as fs } from '@kit.CoreFileKit';
     4. import { common } from '@kit.AbilityKit';
     5. // ...
     6. class Options {
     7. public offset?: number;
     8. public length?: number;
     9. }
     10. // ...
     11. let bufferSize: number = 0;
     12. let file = await context.resourceManager.getRawFd('32_xiyouji.pcm');
     13. writeDataCallback = (buffer: ArrayBuffer) => {
     14. let options: Options = {
     15. offset: bufferSize,
     16. length: buffer.byteLength
     17. };
     18. // ...
     19. audioRenderer.on('writeData', writeDataCallback);
     ```
3. 调用[start](../harmonyos-references/arkts-apis-audio-audiorenderer.md#start8)方法进入running状态，开始渲染音频。

   ```
   1. import { BusinessError } from '@kit.BasicServicesKit';
   2. // ...
   3. audioRenderer.start((err: BusinessError) => {
   4. if (err) {
   5. console.error('Renderer start failed.');
   6. // ...
   7. } else {
   8. console.info('Renderer start success.');
   9. // ...
   10. }
   11. });
   ```
4. 调用[stop](../harmonyos-references/arkts-apis-audio-audiorenderer.md#stop8)方法停止渲染。

   ```
   1. import { BusinessError } from '@kit.BasicServicesKit';
   2. // ...
   3. audioRenderer.stop((err: BusinessError) => {
   4. if (err) {
   5. console.error('Renderer stop failed.');
   6. // ...
   7. } else {
   8. console.info('Renderer stop success.');
   9. // ...
   10. }
   11. });
   ```
5. 调用[release](../harmonyos-references/arkts-apis-audio-audiorenderer.md#release8)方法销毁实例，释放资源。

   应用需根据实际业务需求合理使用AudioRenderer实例，按需创建并及时释放，避免占用过多音频资源导致异常。

   ```
   1. import { BusinessError } from '@kit.BasicServicesKit';
   2. // ...
   3. audioRenderer.release((err: BusinessError) => {
   4. if (err) {
   5. console.error('Renderer release failed.');
   6. // ...
   7. } else {
   8. // 关闭沙箱文件
   9. console.info('Renderer release success.');
   10. // ...
   11. }
   12. });
   ```

### 选择正确的StreamUsage

创建播放器时候，开发者需要根据应用场景指定播放器的StreamUsage，选择正确的StreamUsage可以避免用户遇到不符合预期的行为。

在音频API文档[StreamUsage](../harmonyos-references/arkts-apis-audio-e.md#streamusage)介绍中，列举了每一种类型推荐的应用场景。例如音乐场景推荐使用STREAM\_USAGE\_MUSIC，电影或者视频场景推荐使用STREAM\_USAGE\_MOVIE，游戏场景推荐使用STREAM\_USAGE\_GAME，等等。

如果开发者配置了不正确的StreamUsage，可能带来一些不符合预期的行为。例如以下场景。

* 游戏场景错误使用STREAM\_USAGE\_MUSIC类型，游戏应用将无法和其他音乐应用并发播放，而游戏场景通常可以与其他音乐应用并发播放。
* 导航场景错误使用STREAM\_USAGE\_MUSIC类型，导航应用播报时候会导致正在播放的音乐停止播放，而导航场景我们通常期望正在播放的音乐仅降低音量播放。

### 配置合适的音频采样率

采样率：指音频每秒单个声道样点数，单位为Hz。

重采样：根据输入输出音频采样率的差异，进行上采样（通过插值增加样点数）或下采样（通过抽取减少样点数）。

AudioRenderer支持枚举类型[AudioSamplingRate](../harmonyos-references/arkts-apis-audio-e.md#audiosamplingrate8)中定义的所有采样率。

若通过AudioRenderer设置的输入音频采样率与设备输出采样率不一致，系统会将输入音频重采样为设备输出采样率。

若为减少重采样功耗，可使用采样率与输出设备采样率一致的输入音频。推荐使用48k采样率。

### 完整示例

下面展示了使用AudioRenderer渲染音频文件的示例代码。

```
1. import { audio } from '@kit.AudioKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { fileIo as fs } from '@kit.CoreFileKit';
4. import { common } from '@kit.AbilityKit';
5. // ...
6. const TAG = 'AudioRendererDemo';
7. class Options {
8. public offset?: number;
9. public length?: number;
10. }
11. // ...

13. let audioRenderer: audio.AudioRenderer | undefined = undefined;
14. let audioStreamInfo: audio.AudioStreamInfo = {
15. samplingRate: audio.AudioSamplingRate.SAMPLE_RATE_48000, // 采样率。
16. channels: audio.AudioChannel.CHANNEL_2, // 通道。
17. sampleFormat: audio.AudioSampleFormat.SAMPLE_FORMAT_S16LE, // 采样格式。
18. encodingType: audio.AudioEncodingType.ENCODING_TYPE_RAW // 编码格式。
19. };
20. let audioRendererInfo: audio.AudioRendererInfo = {
21. usage: audio.StreamUsage.STREAM_USAGE_MUSIC, // 音频流使用类型：音乐。根据业务场景配置，参考StreamUsage。
22. rendererFlags: 0 // 音频渲染器标志。
23. };
24. let audioRendererOptions: audio.AudioRendererOptions = {
25. streamInfo: audioStreamInfo,
26. rendererInfo: audioRendererInfo
27. };
28. let writeDataCallback: audio.AudioRendererWriteDataCallback;

30. async function initArguments(context: common.UIAbilityContext) {
31. let bufferSize: number = 0;
32. let file = await context.resourceManager.getRawFd('32_xiyouji.pcm');
33. writeDataCallback = (buffer: ArrayBuffer) => {
34. let options: Options = {
35. offset: bufferSize,
36. length: buffer.byteLength
37. };

39. try {
40. let bufferLength = fs.readSync(file.fd, buffer, options);
41. bufferSize += buffer.byteLength;
42. // 如果当前回调传入的数据不足一帧，空白区域需要使用静音数据填充，否则会导致播放出现杂音。
43. if (bufferLength < buffer.byteLength) {
44. let view = new DataView(buffer);
45. for (let i = bufferLength; i < buffer.byteLength; i++) {
46. // 空白区域填充静音数据。当使用音频采样格式为SAMPLE_FORMAT_U8时0x7F为静音数据，使用其他采样格式时0为静音数据。
47. view.setUint8(i, 0);
48. }
49. }
50. // API version 11不支持返回回调结果，从API version 12开始支持返回回调结果。
51. // 如果开发者不希望播放某段buffer，返回audio.AudioDataCallbackResult.INVALID即可。
52. return audio.AudioDataCallbackResult.VALID;
53. } catch (error) {
54. console.error('Error reading file:', error);
55. // ...
56. // API version 11不支持返回回调结果，从API version 12开始支持返回回调结果。
57. return audio.AudioDataCallbackResult.INVALID;
58. }
59. };
60. }

62. // 初始化，创建实例，设置监听事件。
63. async function init() {
64. audio.createAudioRenderer(audioRendererOptions, (err, renderer) => { // 创建AudioRenderer实例。
65. if (!err) {
66. console.info(`${TAG}: creating AudioRenderer success`);
67. // ...
68. audioRenderer = renderer;
69. if (audioRenderer !== undefined) {
70. audioRenderer.on('writeData', writeDataCallback);
71. // ...
72. }
73. } else {
74. console.info(`${TAG}: creating AudioRenderer failed, error: ${err.message}`);
75. // ...
76. }
77. });
78. }

80. // 开始一次音频渲染。
81. async function start() {
82. if (audioRenderer !== undefined) {
83. let stateGroup = [audio.AudioState.STATE_PREPARED, audio.AudioState.STATE_PAUSED, audio.AudioState.STATE_STOPPED];
84. if (stateGroup.indexOf(audioRenderer.state.valueOf()) === -1) { // 当且仅当状态为prepared、paused和stopped之一时才能启动渲染。
85. console.error(TAG + 'start failed');
86. // ...
87. return;
88. }
89. // 启动渲染。
90. audioRenderer.start((err: BusinessError) => {
91. if (err) {
92. console.error('Renderer start failed.');
93. // ...
94. } else {
95. console.info('Renderer start success.');
96. // ...
97. }
98. });
99. }
100. }

102. async function pause() {
103. // 暂停渲染。
104. if (audioRenderer !== undefined) {
105. // 只有渲染器状态为running的时候才能暂停。
106. if (audioRenderer.state.valueOf() !== audio.AudioState.STATE_RUNNING) {
107. console.info('Renderer is not running');
108. // ...
109. return;
110. }
111. // 暂停渲染。
112. audioRenderer.pause((err: BusinessError) => {
113. if (err) {
114. console.error('Renderer pause failed.');
115. // ...
116. } else {
117. console.info('Renderer pause success.');
118. // ...
119. }
120. });
121. }
122. }

124. // 停止渲染。
125. async function stop() {
126. if (audioRenderer !== undefined) {
127. // 只有渲染器状态为running或paused的时候才可以停止。
128. if (audioRenderer.state.valueOf() !== audio.AudioState.STATE_RUNNING &&
129. audioRenderer.state.valueOf() !== audio.AudioState.STATE_PAUSED) {
130. console.info('Renderer is not running or paused.');
131. // ...
132. return;
133. }
134. // 停止渲染。
135. audioRenderer.stop((err: BusinessError) => {
136. if (err) {
137. console.error('Renderer stop failed.');
138. // ...
139. } else {
140. console.info('Renderer stop success.');
141. // ...
142. }
143. });
144. }
145. }

147. // 销毁实例，释放资源。
148. async function release() {
149. if (audioRenderer !== undefined) {
150. // 渲染器状态不是released状态，才能release。
151. if (audioRenderer.state.valueOf() === audio.AudioState.STATE_RELEASED) {
152. console.info('Renderer already released');
153. // ...
154. return;
155. }

157. // ...

159. // 释放资源。
160. audioRenderer.release((err: BusinessError) => {
161. if (err) {
162. console.error('Renderer release failed.');
163. // ...
164. } else {
165. // 关闭沙箱文件
166. console.info('Renderer release success.');
167. // ...
168. }
169. });
170. }
171. }
```

当同优先级或高优先级音频流要使用输出设备时，当前音频流会被中断，应用可以自行响应中断事件并做出处理。具体的音频并发处理方式可参考[处理音频焦点事件](audio-playback-concurrency.md)。
