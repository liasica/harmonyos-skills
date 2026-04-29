---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/using-avrecorder-for-recording
title: 使用AVRecorder录制音频(ArkTS)
breadcrumb: 指南 > 媒体 > Media Kit（媒体服务） > 媒体开发指导(ArkTS) > 录制 > 使用AVRecorder录制音频(ArkTS)
category: harmonyos-guides
scraped_at: 2026-04-29T13:35:25+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:c54e5c3c8832d4d5390375f2e176bd36ca58a58872c990c0ead57314d6da8427
---

使用[AVRecorder](media-kit-intro.md#avrecorder)可以实现音频录制功能，本开发指导将以“开始录制-暂停录制-恢复录制-停止录制”的一次流程为例，向开发者讲解AVRecorder音频录制相关功能。

在进行应用开发的过程中，开发者可以通过AVRecorder的state属性，主动获取当前状态或使用[on('stateChange')](../harmonyos-references/arkts-apis-media-avrecorder.md#onstatechange9)方法监听状态变化。开发过程中必须严格遵循状态机要求，例如只能在started状态下调用[pause](../harmonyos-references/arkts-apis-media-avrecorder.md#pause9-1)接口，只能在paused状态下调用[resume](../harmonyos-references/arkts-apis-media-avrecorder.md#resume9-1)接口。

**图1** 录制状态变化示意图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/KHo0dCPrQUyIYXl8xHo-RA/zh-cn_image_0000002558765096.png?HW-CC-KV=V1&HW-CC-Date=20260429T053524Z&HW-CC-Expire=86400&HW-CC-Sign=7255A2112E8899932C37EAFA2FE2DAC5742AB2AFE0485932C08E840787404980)

状态的详细说明请参考[AVRecorderState](../harmonyos-references/arkts-apis-media-t.md#avrecorderstate9)。

## 申请权限

在开发此功能前，开发者应根据实际需求申请相关权限：

* 当需要使用麦克风时，需要申请**ohos.permission.MICROPHONE**麦克风权限。申请方式请参考：[向用户申请授权](request-user-authorization.md)。
* 当需要读取和保存音频文件时，请优先使用[AudioViewPicker音频选择器对象](../harmonyos-references/js-apis-file-picker.md#audioviewpicker)。

说明

仅应用需要克隆、备份或同步用户公共目录的音频类文件时，可申请ohos.permission.READ\_AUDIO、ohos.permission.WRITE\_AUDIO权限来读写音频文件，申请方式请参考[申请受控权限](declare-permissions-in-acl.md)，通过AGC审核后才能使用。为避免应用的上架申请被驳回，开发者应优先使用Picker/控件等替代方案，仅少量符合[特殊场景](restricted-permissions.md#ohospermissionread_audio)的应用被允许申请受限权限。

## 开发音频录制应用须知

* 如果需要持续录制或后台录制，请申请长时任务避免进入挂起（Suspend）状态。具体参考[长时任务开发指导](continuous-task.md)。
* 录制需要在前台启动，启动后可以退后台。在后台启动录制将会失败。
* 应用录制音频时需要使用合适的录制流类型，请参考[使用合适的音频流类型](using-right-streamusage-and-sourcetype.md)。
* 应用录制音频时需要切换输入设备路由，请参考[实现音频输入设备路由切换](audio-input-device-switcher.md)。

## 开发步骤及注意事项

详细的API说明请参考[AVRecorder](../harmonyos-references/arkts-apis-media-avrecorder.md)。

1. 创建AVRecorder实例，实例创建完成进入idle状态。

   说明

   需要在avRecorder完成赋值后，再进行剩余操作。

   ```
   1. import { media } from '@kit.MediaKit';
   2. import { BusinessError } from '@kit.BasicServicesKit';

   4. private avRecorder: media.AVRecorder | undefined = undefined;

   6. try {
   7. this.avRecorder = await media.createAVRecorder();
   8. } catch (err) {
   9. let error: BusinessError = err as BusinessError;
   10. console.error(`Failed to create avRecorder, error code: ${error.code}, message: ${error.message}`);
   11. }
   ```
2. 设置业务需要的监听事件，监听状态变化及错误上报。

   | 事件类型 | 说明 |
   | --- | --- |
   | stateChange | 必要事件，监听AVRecorder的state属性改变。 |
   | error | 必要事件，监听AVRecorder的错误信息。 |

   ```
   1. import { BusinessError } from '@kit.BasicServicesKit';

   3. // 状态上报回调函数。
   4. this.avRecorder?.on('stateChange', (state: media.AVRecorderState, reason: media.StateChangeReason) => {
   5. console.info(`AVRecorder state is changed to ${state}, reason: ${reason}`);
   6. // 用户可以在此补充状态发生切换后想要进行的动作。
   7. });

   9. // 错误上报回调函数。
   10. this.avRecorder?.on('error', (error) => {
   11. console.error(`Error occurred in avRecorder, error code: ${error.code}, message: ${error.message}`);
   12. });
   ```
3. 配置音频录制参数，调用[prepare](../harmonyos-references/arkts-apis-media-avrecorder.md#prepare9-1)接口，此时进入prepared状态。

   说明

   配置参数需要注意：

   * 配置参数之前需要确保完成对应权限的申请，请参考[申请权限](using-avrecorder-for-recording.md#申请权限)。
   * prepare接口的入参avConfig中仅设置音频相关的配置参数，如示例代码所示。

     如果只需要录制音频，请不要设置视频相关配置参数；如果需要录制视频，可以参考[视频录制开发指导](video-recording.md)进行开发。直接设置视频相关参数会导致后续步骤报错。
   * 需要使用支持的[录制规格](media-kit-intro.md#支持的格式)，具体录制参数需严格契合既定的[录制参数配置](../harmonyos-references/arkts-apis-media-i.md#avrecorderprofile9)。
   * 录制输出的url地址（即示例里avConfig中的url），形式为fd://xx (fd number)。需要基础文件操作接口（[Core File Kit的ohos.file.fs](../harmonyos-references/js-apis-file-fs.md)）实现应用文件访问能力，获取方式参考[应用文件访问与管理](app-file-access.md)。
   * 示例中配置的audioCodec音频编码格式、aacProfile音频编码扩展格式、fileFormat封装格式请参考[AVRecorderProfile](../harmonyos-references/arkts-apis-media-i.md#avrecorderprofile9)。

   ```
   1. import { media } from '@kit.MediaKit';
   2. import { BusinessError } from '@kit.BasicServicesKit';
   3. import fileIo from '@ohos.file.fs';

   5. let avProfile: media.AVRecorderProfile = {
   6. audioBitrate: 112000, // 音频比特率。
   7. audioChannels: 2, // 音频声道数。
   8. audioCodec: media.CodecMimeType.AUDIO_AAC, // 音频编码格式。
   9. aacProfile: media.AacProfile.AAC_HE, // 音频编码扩展格式。
   10. audioSampleRate: 48000, // 音频采样率。
   11. fileFormat: media.ContainerFormatType.CFT_MPEG_4A, // 封装格式。
   12. };

   14. const context: Context = this.getUIContext().getHostContext()!; // 参考应用文件访问与管理。
   15. let filePath: string = context.filesDir + '/example.mp3';
   16. let audioFile: fileIo.File = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
   17. let fileFd: number = audioFile.fd; // 获取文件fd。

   19. let avConfig: media.AVRecorderConfig = {
   20. audioSourceType: media.AudioSourceType.AUDIO_SOURCE_TYPE_MIC, // 音频输入源，这里设置为麦克风。
   21. profile: avProfile,
   22. url: 'fd://' + fileFd.toString(), // 参考应用文件访问与管理中的开发示例获取创建的音频文件fd填入此处。
   23. };

   25. try {
   26. await this.avRecorder?.prepare(avConfig);
   27. console.info('Succeeded in preparing avRecorder');
   28. } catch (err) {
   29. let error: BusinessError = err as BusinessError;
   30. console.error(`Failed to prepare avRecorder, error code: ${error.code}, message: ${error.message}`);
   31. }
   ```
4. 开始录制，调用[start](../harmonyos-references/arkts-apis-media-avrecorder.md#start9-1)接口，此时进入started状态。

   ```
   1. // 开始录制。
   2. await this.avRecorder?.start();
   ```
5. 暂停录制，调用[pause](../harmonyos-references/arkts-apis-media-avrecorder.md#pause9-1)接口，此时进入paused状态。

   ```
   1. // 暂停录制。
   2. await this.avRecorder?.pause();
   ```
6. 恢复录制，调用[resume](../harmonyos-references/arkts-apis-media-avrecorder.md#resume9-1)接口，此时再次进入started状态。

   ```
   1. // 恢复录制。
   2. await this.avRecorder?.resume();
   ```
7. 停止录制，调用[stop](../harmonyos-references/arkts-apis-media-avrecorder.md#stop9-1)接口，此时进入stopped状态。

   ```
   1. // 停止录制。
   2. await this.avRecorder?.stop();
   ```
8. 重置资源，调用[reset](../harmonyos-references/arkts-apis-media-avrecorder.md#reset9-1)接口，重新进入idle状态，允许重新配置录制参数。

   ```
   1. // 重置资源。
   2. await this.avRecorder?.reset();
   ```
9. 销毁实例，调用[release](../harmonyos-references/arkts-apis-media-avrecorder.md#release9-1)接口，进入released状态，退出录制。

   ```
   1. // 销毁实例。
   2. await this.avRecorder?.release();
   ```

## 完整示例

参考以下示例，完成“开始录制-暂停录制-恢复录制-停止录制”的完整流程。

使用当前示例代码时，需要申请**ohos.permission.MICROPHONE**麦克风权限。申请方式请参考：[向用户申请授权](request-user-authorization.md)。

```
1. import { common } from '@kit.AbilityKit';
2. import { media } from '@kit.MediaKit';
3. import { BusinessError } from '@kit.BasicServicesKit';
4. import fileIo from '@ohos.file.fs';

6. async function audioRecording(context: common.Context): Promise<void> {
7. // 创建avRecorder对象。
8. let avRecorder: media.AVRecorder | undefined = undefined;
9. try {
10. avRecorder = await media.createAVRecorder();
11. } catch (error) {
12. let err = error as BusinessError;
13. console.error(`Failed to create avRecorder, error code: ${err.code}, message: ${err.message}`);
14. return;
15. }

17. // 注册avRecorder回调函数。
18. try {
19. // 状态机变化回调函数。
20. avRecorder.on('stateChange', (state: media.AVRecorderState, reason: media.StateChangeReason) => {
21. console.info(`AVRecorder state is changed to ${state}, reason: ${reason}`);
22. });
23. // 错误上报回调函数。
24. avRecorder.on('error', (error: BusinessError) => {
25. console.error(`Error occurred in avRecorder, error code: ${error.code}, message: ${error.message}`);
26. });
27. } catch (error) {
28. let err = error as BusinessError;
29. console.error(`Failed to set avRecorder callback, error code: ${err.code}, message: ${err.message}`);
30. }

32. let avProfile: media.AVRecorderProfile = {
33. audioBitrate: 112000, // 音频比特率。
34. audioChannels: 2, // 音频声道数。
35. audioCodec: media.CodecMimeType.AUDIO_AAC, // 音频编码格式。
36. aacProfile: media.AacProfile.AAC_HE, // 音频编码扩展格式。
37. audioSampleRate: 48000, // 音频采样率。
38. fileFormat: media.ContainerFormatType.CFT_MPEG_4A, // 封装格式。
39. };
40. let avConfig: media.AVRecorderConfig = {
41. audioSourceType: media.AudioSourceType.AUDIO_SOURCE_TYPE_MIC, // 音频输入源，这里设置为麦克风。
42. profile: avProfile,
43. url: 'fd://35', // 参考应用文件访问与管理开发示例新建并读写一个文件。
44. };

46. // 创建文件以及设置avConfig.url。
47. let audioFile: fileIo.File | undefined = undefined;
48. try {
49. let path: string = context.filesDir + '/example.mp3'; // 文件沙箱路径，文件后缀名应与封装格式对应。
50. audioFile = fileIo.openSync(path, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE); // 打开文件。
51. } catch (error) {
52. let err = error as BusinessError;
53. console.error(`Failed to open file, error code: ${err.code}, message: ${err.message}`);
54. }
55. if (audioFile !== undefined) {
56. avConfig.url = 'fd://' + audioFile.fd; // 更新url。
57. }

59. // 配置录制参数完成准备工作。
60. try {
61. if (avRecorder.state === 'idle' || avRecorder.state === 'stopped') { // 仅在idle或者stopped状态下调用prepare为合理状态切换。
62. await avRecorder.prepare(avConfig);
63. }
64. } catch (error) {
65. let err = error as BusinessError;
66. console.error(`Failed to prepare avRecorder, error code: ${err.code}, message: ${err.message}`);
67. }

69. // 开始录制。
70. try {
71. if (avRecorder.state === 'prepared') { // 仅在prepared状态下调用start为合理状态切换。
72. await avRecorder.start();
73. }
74. } catch (error) {
75. let err = error as BusinessError;
76. console.error(`Failed to start avRecorder, error code: ${err.code}, message: ${err.message}`);
77. }

79. // 暂停录制。
80. try {
81. if (avRecorder.state === 'started') { // 仅在started状态下调用pause为合理状态切换。
82. await avRecorder.pause();
83. }
84. } catch (error) {
85. let err = error as BusinessError;
86. console.error(`Failed to pause avRecorder, error code: ${err.code}, message: ${err.message}`);
87. }

89. // 恢复录制。
90. try {
91. if (avRecorder.state === 'paused') { // 仅在paused状态下调用resume为合理状态切换。
92. await avRecorder.resume();
93. }
94. } catch (error) {
95. let err = error as BusinessError;
96. console.error(`Failed to resume avRecorder, error code: ${err.code}, message: ${err.message}`);
97. }

99. // 停止录制。
100. try {
101. if (avRecorder.state === 'started' || avRecorder.state === 'paused') { // 仅在started或者paused状态下调用stop为合理状态切换。
102. await avRecorder.stop();
103. }
104. } catch (error) {
105. let err = error as BusinessError;
106. console.error(`Failed to stop avRecorder, error code: ${err.code}, message: ${err.message}`);
107. }

109. // 重置。
110. try {
111. await avRecorder.reset();
112. } catch (error) {
113. let err = error as BusinessError;
114. console.error(`Failed to reset avRecorder, error code: ${err.code}, message: ${err.message}`);
115. }

117. // 释放录制实例。
118. try {
119. await avRecorder.release();
120. avRecorder = undefined;
121. } catch (error) {
122. let err = error as BusinessError;
123. console.error(`Failed to release avRecorder, error code: ${err.code}, message: ${err.message}`);
124. }

126. // 关闭录制文件fd。
127. try {
128. if (audioFile !== undefined) {
129. await fileIo.close(audioFile.fd);
130. }
131. } catch (error) {
132. let err = error as BusinessError;
133. console.error(`Failed to close fd, error code: ${err.code}, message: ${err.message}`);
134. }
135. }
```
