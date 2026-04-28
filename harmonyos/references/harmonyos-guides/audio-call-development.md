---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/audio-call-development
title: 开发音频通话功能
breadcrumb: 指南 > 媒体 > Audio Kit（音频服务） > 音频通话 > 开发音频通话功能
category: harmonyos-guides
scraped_at: 2026-04-28T07:45:38+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:20eff933ee53572e12936d9d1731bbd115d50736f8695bfd501358f74ade0f50
---

在音频通话场景下，音频输出（播放对端声音）和音频输入（录制本端声音）会同时进行，应用可以通过使用AudioRenderer来实现音频输出，通过使用AudioCapturer来实现音频输入，同时使用AudioRenderer和AudioCapturer即可实现音频通话功能。

在音频通话开始和结束时，应用可以自行检查当前的[音频场景模式](audio-call-overview.md#音频场景模式)和[铃声模式](audio-call-overview.md#铃声模式)，以便采取合适的音频管理及提示策略。

以下代码示范了同时使用AudioRenderer和AudioCapturer实现音频通话功能的基本过程，其中未包含音频通话数据的传输过程，实际开发中，需要将网络传输来的对端通话数据解码播放，此处仅以读取音频文件的数据代替；同时需要将本端录制的通话数据编码打包，通过网络发送给对端，此处仅以将数据写入音频文件代替。

示例为片段代码，可通过点击示例代码右下方的链接获取[完整示例](https://gitcode.com/openharmony/applications_app_samples/blob/master/code/DocsSample/Media/Audio/VoipCallSampleJS)。

## 使用AudioRenderer播放对端的通话声音

该过程与[使用AudioRenderer开发音频播放功能(ArkTs)](using-audiorenderer-for-playback.md)过程相似，关键区别在于audioRendererInfo参数和音频数据来源。audioRendererInfo参数中，音频流使用类型usage需设置为VoIP通话：STREAM\_USAGE\_VOICE\_COMMUNICATION。

```
1. import { audio } from '@kit.AudioKit'; // 导入audio模块。
2. import { BusinessError } from '@kit.BasicServicesKit'; // 导入BusinessError。
3. import { fileIo as fs } from '@kit.CoreFileKit'; // 导入文件操作模块。
4. import { common } from '@kit.AbilityKit'; // 导入UIAbilityContext。

6. // 与使用AudioRenderer开发音频播放功能过程相似,关键区别在于audioRendererInfo参数和音频数据来源。
7. const TAG = 'VoIPDemoForAudioRenderer';

9. class Options {
10. public offset?: number;
11. public length?: number;
12. }

14. let bufferSize: number = 0;
15. let audioRenderer: audio.AudioRenderer | undefined = undefined;
16. let audioStreamInfo: audio.AudioStreamInfo = {
17. samplingRate: audio.AudioSamplingRate.SAMPLE_RATE_48000, // 采样率。
18. channels: audio.AudioChannel.CHANNEL_2, // 通道。
19. sampleFormat: audio.AudioSampleFormat.SAMPLE_FORMAT_S16LE, // 采样格式。
20. encodingType: audio.AudioEncodingType.ENCODING_TYPE_RAW // 编码格式。
21. };
22. let audioRendererInfo: audio.AudioRendererInfo = {
23. // 需使用通话场景相应的参数。
24. usage: audio.StreamUsage.STREAM_USAGE_VOICE_COMMUNICATION, // 音频流使用类型:VoIP通话。
25. rendererFlags: 0 // 音频渲染器标志:默认为0即可。
26. };
27. let audioRendererOptions: audio.AudioRendererOptions = {
28. streamInfo: audioStreamInfo,
29. rendererInfo: audioRendererInfo
30. };
31. let file: fs.File;
32. let writeDataCallback: audio.AudioRendererWriteDataCallback;
33. // ...
34. async function initArguments(context: common.UIAbilityContext) {
35. let path = context.cacheDir;
36. // 此处仅作示例,实际使用时需要将文件替换为应用要播放的PCM文件。
37. let filePath = path + '/StarWars10s-2C-48000-4SW.pcm';
38. file = fs.openSync(filePath, fs.OpenMode.READ_ONLY);
39. writeDataCallback = (buffer: ArrayBuffer) => {
40. let options: Options = {
41. offset: bufferSize,
42. length: buffer.byteLength
43. };

45. try {
46. let bufferLength = fs.readSync(file.fd, buffer, options);
47. bufferSize += buffer.byteLength;
48. // 如果当前回调传入的数据不足一帧,空白区域需要使用静音数据填充,否则会导致播放出现杂音。
49. if (bufferLength < buffer.byteLength) {
50. let view = new DataView(buffer);
51. for (let i = bufferLength; i < buffer.byteLength; i++) {
52. // 空白区域填充静音数据。当使用音频采样格式为SAMPLE_FORMAT_U8时0x7F为静音数据,使用其他采样格式时0为静音数据。
53. view.setUint8(i, 0);
54. }
55. }
56. // API version 11不支持返回回调结果,从API version 12开始支持返回回调结果。
57. // 如果开发者不希望播放某段buffer,返回audio.AudioDataCallbackResult.INVALID即可。
58. return audio.AudioDataCallbackResult.VALID;
59. } catch (error) {
60. console.error('Error reading file:', error);

62. if (globalLogUpdate) {
63. globalLogUpdate(`Error reading file: ${error}`, true);
64. }
65. // API version 11不支持返回回调结果,从API version 12开始支持返回回调结果。
66. return audio.AudioDataCallbackResult.INVALID;
67. }
68. };
69. }

71. // 初始化,创建实例,设置监听事件。
72. async function init() {
73. audio.createAudioRenderer(audioRendererOptions, (err, renderer) => { // 创建AudioRenderer实例。
74. if (!err) {
75. console.info(`${TAG}: creating AudioRenderer success`);
76. // ...
77. audioRenderer = renderer;
78. if (audioRenderer !== undefined) {
79. audioRenderer.on('writeData', writeDataCallback);
80. }
81. } else {
82. console.info(`${TAG}: creating AudioRenderer failed, error: ${err.message}`);
83. // ...
84. }
85. });
86. }

88. // 开始一次音频渲染。
89. async function start() {
90. if (audioRenderer !== undefined) {
91. let stateGroup = [audio.AudioState.STATE_PREPARED, audio.AudioState.STATE_PAUSED, audio.AudioState.STATE_STOPPED];
92. if (stateGroup.indexOf(audioRenderer.state.valueOf()) === -1) { // 当且仅当状态为prepared、paused和stopped之一时才能启动渲染。
93. console.error(TAG + 'start failed');
94. // ...
95. return;
96. }
97. // 启动渲染。
98. audioRenderer.start((err: BusinessError) => {
99. if (err) {
100. console.error('Renderer start failed.');
101. // ...
102. } else {
103. console.info('Renderer start success.');
104. // ...
105. }
106. });
107. }
108. }

110. // 暂停渲染。
111. async function pause() {
112. if (audioRenderer !== undefined) {
113. // 只有渲染器状态为running的时候才能暂停。
114. if (audioRenderer.state.valueOf() !== audio.AudioState.STATE_RUNNING) {
115. console.info('Renderer is not running');
116. // ...
117. return;
118. }
119. // 暂停渲染。
120. audioRenderer.pause((err: BusinessError) => {
121. if (err) {
122. console.error('Renderer pause failed.');
123. // ...
124. } else {
125. console.info('Renderer pause success.');
126. // ...
127. }
128. });
129. }
130. }

132. // 停止渲染。
133. async function stop() {
134. if (audioRenderer !== undefined) {
135. // 只有渲染器状态为running或paused的时候才可以停止。
136. if (audioRenderer.state.valueOf() !== audio.AudioState.STATE_RUNNING &&
137. audioRenderer.state.valueOf() !== audio.AudioState.STATE_PAUSED) {
138. console.info('Renderer is not running or paused.');
139. // ...
140. return;
141. }
142. // 停止渲染。
143. audioRenderer.stop((err: BusinessError) => {
144. if (err) {
145. console.error('Renderer stop failed.');
146. // ...
147. } else {
148. fs.close(file);
149. console.info('Renderer stop success.');
150. // ...
151. }
152. });
153. }
154. }

156. // 销毁实例,释放资源。
157. async function release() {
158. if (audioRenderer !== undefined) {
159. // 渲染器状态不是released状态,才能release。
160. if (audioRenderer.state.valueOf() === audio.AudioState.STATE_RELEASED) {
161. console.info('Renderer already released');
162. // ...
163. return;
164. }
165. // 释放资源。
166. audioRenderer.release((err: BusinessError) => {
167. if (err) {
168. console.error('Renderer release failed.');
169. // ...
170. } else {
171. console.info('Renderer release success.');
172. // ...
173. }
174. });
175. }
176. }
```

## 使用AudioCapturer录制本端的通话声音

该过程与[使用AudioCapturer开发音频录制功能(ArkTs)](using-audiocapturer-for-recording.md)过程相似，关键区别在于audioCapturerInfo参数和音频数据流向。audioCapturerInfo参数中音源类型source需设置为语音通话：SOURCE\_TYPE\_VOICE\_COMMUNICATION。

所有录制均需要申请麦克风权限：ohos.permission.MICROPHONE，申请方式请参考[向用户申请授权](request-user-authorization.md)。

```
1. import { audio } from '@kit.AudioKit'; // 导入audio模块。
2. import { BusinessError } from '@kit.BasicServicesKit'; // 导入BusinessError。
3. import { fileIo as fs } from '@kit.CoreFileKit'; // 导入文件操作模块。
4. import { common, abilityAccessCtrl, PermissionRequestResult } from '@kit.AbilityKit'; // 导入UIAbilityContext。
5. // 与使用AudioCapturer开发音频录制功能过程相似,关键区别在于audioCapturerInfo参数和音频数据流向。
6. const TAG = 'VoIPDemoForAudioCapturer';

8. class Options {
9. public offset?: number;
10. public length?: number;
11. }

13. let bufferSize: number = 0;
14. let audioCapturer: audio.AudioCapturer | undefined = undefined;
15. let audioStreamInfo: audio.AudioStreamInfo = {
16. samplingRate: audio.AudioSamplingRate.SAMPLE_RATE_48000, // 采样率。
17. channels: audio.AudioChannel.CHANNEL_2, // 通道。
18. sampleFormat: audio.AudioSampleFormat.SAMPLE_FORMAT_S16LE, // 采样格式。
19. encodingType: audio.AudioEncodingType.ENCODING_TYPE_RAW // 编码格式。
20. };
21. let audioCapturerInfo: audio.AudioCapturerInfo = {
22. // 需使用通话场景相应的参数。
23. source: audio.SourceType.SOURCE_TYPE_VOICE_COMMUNICATION, // 音源类型:语音通话。
24. capturerFlags: 0 // 音频采集器标志:默认为0即可。
25. };
26. let audioCapturerOptions: audio.AudioCapturerOptions = {
27. streamInfo: audioStreamInfo,
28. capturerInfo: audioCapturerInfo
29. };
30. let file: fs.File;
31. let readDataCallback: Callback<ArrayBuffer>;

33. // ...

35. async function initArguments(context: common.UIAbilityContext) {
36. let path = context.cacheDir;
37. let filePath = path + '/StarWars10s-2C-48000-4SW.pcm';
38. file = fs.openSync(filePath, fs.OpenMode.READ_WRITE | fs.OpenMode.CREATE);
39. console.info(`File opened: ${filePath}`);

41. readDataCallback = (buffer: ArrayBuffer) => {
42. let options: Options = {
43. offset: bufferSize,
44. length: buffer.byteLength
45. }
46. fs.writeSync(file.fd, buffer, options);
47. bufferSize += buffer.byteLength;
48. }
49. }

51. // 初始化,创建实例,设置监听事件。
52. async function init() {
53. audio.createAudioCapturer(audioCapturerOptions, (err, capturer) => { // 创建AudioCapturer实例。
54. if (err) {
55. console.error(`Invoke createAudioCapturer failed, code is ${err.code}, message is ${err.message}`);
56. // ...
57. return;
58. }
59. console.info(`${TAG}: create AudioCapturer success`);
60. // ...
61. audioCapturer = capturer;
62. if (audioCapturer !== undefined) {
63. audioCapturer.on('readData', readDataCallback);
64. }
65. });
66. }

68. // 开始一次音频采集。
69. async function start() {
70. if (audioCapturer !== undefined) {
71. let stateGroup = [audio.AudioState.STATE_PREPARED, audio.AudioState.STATE_PAUSED, audio.AudioState.STATE_STOPPED];
72. if (stateGroup.indexOf(audioCapturer.state.valueOf()) === -1) {
73. // 当且仅当状态为STATE_PREPARED、STATE_PAUSED和STATE_STOPPED之一时才能启动采集。
74. console.error(`${TAG}: start failed`);
75. // ...
76. return;
77. }

79. // 启动采集。
80. audioCapturer.start((err: BusinessError) => {
81. if (err) {
82. console.error('Capturer start failed.');
83. // ...
84. } else {
85. console.info('Capturer start success.');
86. // ...
87. }
88. });
89. }
90. }

92. // 停止采集。
93. async function stop() {
94. if (audioCapturer !== undefined) {
95. // 只有采集器状态为STATE_RUNNING或STATE_PAUSED的时候才可以停止。
96. if (audioCapturer.state.valueOf() !== audio.AudioState.STATE_RUNNING &&
97. audioCapturer.state.valueOf() !== audio.AudioState.STATE_PAUSED) {
98. console.info('Capturer is not running or paused');
99. // ...
100. return;
101. }

103. // 停止采集。
104. audioCapturer.stop((err: BusinessError) => {
105. if (err) {
106. console.error('Capturer stop failed.');
107. // ...
108. } else {
109. fs.close(file);
110. console.info('Capturer stop success.');
111. // ...
112. }
113. });
114. }
115. }

117. // 销毁实例,释放资源。
118. async function release() {
119. if (audioCapturer !== undefined) {
120. // 采集器状态不是STATE_RELEASED或STATE_NEW状态,才能release。
121. if (audioCapturer.state.valueOf() === audio.AudioState.STATE_RELEASED ||
122. audioCapturer.state.valueOf() === audio.AudioState.STATE_NEW) {
123. console.info('Capturer already released');
124. // ...
125. return;
126. }

128. // 释放资源。
129. audioCapturer.release((err: BusinessError) => {
130. if (err) {
131. console.error('Capturer release failed.');
132. // ...
133. } else {
134. console.info('Capturer release success.');
135. // ...
136. }
137. });
138. }
139. }
```
