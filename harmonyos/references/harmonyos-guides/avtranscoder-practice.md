---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/avtranscoder-practice
title: 创建异步线程执行AVTranscoder视频转码(ArkTS)
breadcrumb: 指南 > 媒体 > Media Kit（媒体服务） > 媒体开发指导(ArkTS) > 视频转码 > 创建异步线程执行AVTranscoder视频转码(ArkTS)
category: harmonyos-guides
scraped_at: 2026-04-28T07:46:29+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:0eb452abb2820ccd4216d76c9117650d3396f0a830220a7dcacf166aaf087a82
---

在开发过程中，应用经常会创建异步线程执行视频转码任务以满足不同诉求，主要包括：

* 节省存储空间。

  高清视频文件通常存储空间占用大，几分钟的视频就可能占用数GB的存储空间。视频压缩可以显著减小文件大小，节省存储空间。
* 提高设备兼容性。

  不同设备所支持播放的视频格式各不相同。视频转码可以将源视频格式转换成设备支持的常用格式，以满足不同设备的播放需求，从而提高视频文件的设备兼容性。

## 基础概念

视频的码率（Bitrate）和分辨率（宽×高）是影响视频画质和文件大小的两个关键因素。它们之间的关系并非简单的线性对应，而是受到编码效率、内容复杂度等多种因素的共同影响。

* **码率（Bitrate）和分辨率（宽×高）的基本概念**

  + 码率：指的是单位时间内视频流的数据量（单位：Kbps 或 Mbps）。1 Mbps = 1,000,000 bit/s（1,000,000比特每秒）。

    码率越高，单位时间内传输的数据越多，潜在画质更高，但文件体积也更大。
  + 分辨率：指视频画面的像素数量（例如 1920×1080）。

    分辨率越高，像素数量越多，画面细节更加清晰，但需要处理的数据量也更大。
* **码率和分辨率的关系**

  + 直观关系

    在相同编码效率和内容复杂度的情况下，分辨率越大，则需要分配越高的码率以保持画质。如果所分配的码率不足，编码器会通过压缩（如丢弃细节、增加块效应）来降低数据量。
  + 公式参考（经验法则）

    - 码率正比于 分辨率宽×分辨率高×帧率×复杂度系数
    - 复杂度系数与视频内容的动态程度相关，例如静态画面（例如讲座视频）低复杂度系数，可以较低码率保持清晰，动态画面（例如体育比赛）高复杂度系数，需要更高的码率。
* **编码效率的影响**

  不同的编码标准（如 H.264、H.265、AV1）具有不同的压缩效率：

  + 高效编码器（如 H.265）在相同分辨率和画质下，码率可比 H.264 降低约50%。
  + 低效编码器（如 MJPEG）需要更高的码率以避免画质损失。

## 选择合适的码率和分辨率

* **码率转换**

  输入：源视频的宽wref、高href、帧率fpsref、码率Rref；目标视频的宽wtar、高htar、帧率fpstar。

  输出：目标视频的码率Rtar。

  计算过程：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/QxIOby11RcKRLHHd-WNEyQ/zh-cn_image_0000002552798948.png?HW-CC-KV=V1&HW-CC-Date=20260427T234627Z&HW-CC-Expire=86400&HW-CC-Sign=E03E65677DA5A16E003B6D4AD39EC9440DA5DB1A35D5632B99D80387B1F37F52)

  分辨率和帧率的系数由以下经验公式计算可得。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/O-JtU-JzQc2nVRI46zn8Ag/zh-cn_image_0000002583438643.png?HW-CC-KV=V1&HW-CC-Date=20260427T234627Z&HW-CC-Expire=86400&HW-CC-Sign=25E2531231600A877974F125DE62E1FC412AFCAA95DEB99450EDDBDEFD7649D3)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a7/v3/Qvq3gqgJToGf91V8TgGpDg/zh-cn_image_0000002552958598.png?HW-CC-KV=V1&HW-CC-Date=20260427T234627Z&HW-CC-Expire=86400&HW-CC-Sign=6CACBF728CE2A8A1F88B63A245FF5FEE61722AF00E1B57A3D1C661EEEA8687D3)

  上述计算帧率的公式y=clip(0.5, 2, x)表示：如果x∈[0.5, 2.0]，取y=x；如果x＜0.5，取y=0.5；如果x＞2.0，取y=2.0。
* **码率计算**

  选定一个baseline的码率，例如720P/30fps的视频，码率默认3Mbps，记为V0。

  如果要对视频V1做转码，输出视频为V2，可以按如下过程计算：

  1. 代入(V0,V2)，得到估计码率为R2。
  2. 代入(V1,V2)，得到估计码率为R2'。

  取二者最小值，以确保目标码率比源视频有所降低。
* **分辨率设置参考（以H.264为例）**

  | 分辨率 | 动态内容（如游戏） | 中等动态（如电影） | 静态内容（如幻灯片） |
  | --- | --- | --- | --- |
  | 720p(1280 × 720) | 3.5–5 Mbps | 2.5–4 Mbps | 1–2 Mbps |
  | 1080p(1920 × 1080) | 6–8 Mbps | 4–6 Mbps | 2–3 Mbps |
  | 4K(3840 × 2160) | 25–35 Mbps | 15–25 Mbps | 10–15 Mbps |
* **转换样例**

  场景一：假设要转码一个分辨率1280×720，30fps的视频，码率为1Mbps，这是画质相对比较良好的视频。需要将视频转码为分辨率640×480，30fps的视频，码率应该设置为463,463bps。计算如下：

  Resolution\_factor = 0.463463

  fps\_factor = 1

  Rtar = 463,463bps

  场景二：假设要转码一个分辨率1280×720，30fps的视频，码率为1Mbps的视频。需要将视频转码为码率为600,000bps，30fps的视频，分辨率应该设置为888×500。计算如下：

  fps\_factor = 1

  Rtar = 600,000bps

  Resolution\_factor = 0.482029

## 视频转码压缩开发样例

```
1. import { media } from '@kit.MediaKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { fileIo } from '@kit.CoreFileKit';
4. export class AVTranscoderDemo {
5. private avTranscoder: media.AVTranscoder | undefined = undefined;
6. private context: Context | undefined;
7. constructor(context: Context) {
8. this.context = context;
9. }
10. private avConfig: media.AVTranscoderConfig = {
11. // audioBitrate: 100000, // 音频比特率。
12. // audioCodec: media.CodecMimeType.AUDIO_AAC, // 音频编码格式。
13. fileFormat: media.ContainerFormatType.CFT_MPEG_4, // 封装格式。
14. videoBitrate: 1000000, // 视频比特率。
15. videoCodec: media.CodecMimeType.VIDEO_AVC, // 视频编码格式。
16. videoFrameWidth: 1280, // 视频分辨率的宽。
17. videoFrameHeight: 720  // 视频分辨率的高。
18. };
19. // 注册avTranscoder回调函数。
20. setAVTranscoderCallback() {
21. if (canIUse("SystemCapability.Multimedia.Media.AVTranscoder")) {
22. if (this.avTranscoder != undefined) {
23. // 转码完成回调函数。
24. this.avTranscoder.on('complete', async () => {
25. console.info(`AVTranscoder is completed`);
26. await this.releaseTranscoderingProcess();
27. });
28. // 错误上报回调函数。
29. this.avTranscoder.on('error', (err: BusinessError) => {
30. console.error(`AVTranscoder failed, code is ${err.code}, message is ${err.message}`);
31. });
32. }
33. }
34. }
35. // 开始转码对应的流程。
36. async startTranscoderingProcess() {
37. if (canIUse("SystemCapability.Multimedia.Media.AVTranscoder") && this.context != undefined) {
38. if (this.avTranscoder != undefined) {
39. await this.avTranscoder.release();
40. this.avTranscoder = undefined;
41. }
42. // 1.创建转码实例。
43. this.avTranscoder = await media.createAVTranscoder();
44. this.setAVTranscoderCallback();
45. // 2.获取转码源文件fd和目标文件fd赋予avTranscoder；参考FilePicker文档。
46. let fileDescriptor = await this.context.resourceManager.getRawFd('H264_AAC.mp4');
47. this.avTranscoder.fdSrc = fileDescriptor;
48. let outputFilePath = this.context.filesDir + "/output.mp4";
49. let file = fileIo.openSync(outputFilePath, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
50. this.avTranscoder.fdDst = file.fd;
51. // 3.配置转码参数完成准备工作。
52. await this.avTranscoder.prepare(this.avConfig);
53. // 4.开始转码。
54. await this.avTranscoder.start();
55. }
56. }
57. // 暂停转码对应的流程。
58. async pauseTranscoderingProcess() {
59. if (canIUse("SystemCapability.Multimedia.Media.AVTranscoder")) {
60. if (this.avTranscoder != undefined) { // 仅在调用start返回后调用pause为合理调用。
61. await this.avTranscoder.pause();
62. }
63. }
64. }
65. // 恢复对应的转码流程。
66. async resumeTranscoderingProcess() {
67. if (canIUse("SystemCapability.Multimedia.Media.AVTranscoder")) {
68. if (this.avTranscoder != undefined) { // 仅在调用pause返回后调用resume为合理调用。
69. await this.avTranscoder.resume();
70. }
71. }
72. }
73. // 释放转码流程。
74. async releaseTranscoderingProcess() {
75. if (canIUse("SystemCapability.Multimedia.Media.AVTranscoder")) {
76. if (this.avTranscoder != undefined) {
77. // 1.释放转码实例。
78. await this.avTranscoder.release();
79. this.avTranscoder = undefined;
80. // 2.关闭转码目标文件fd。
81. }
82. }
83. }
84. // 一个完整的【开始转码-暂停转码-恢复转码-转码完成】示例。
85. async avTranscoderDemo() {
86. await this.startTranscoderingProcess(); // 开始转码。
87. await this.pauseTranscoderingProcess(); // 暂停转码。
88. await this.resumeTranscoderingProcess(); // 恢复转码。
89. await this.releaseTranscoderingProcess(); // 释放转码。
90. }
91. }
```

具体如何使用转码能力对视频进行转码，可以参见文档：[用AVTranscoder实现视频转码](using-avtranscoder-for-transcodering.md)。

## 使用异步线程的方式进行转码

本示例使用的是worker线程的方式来实现异步线程进行转码，worker线程的详细使用方式，可以参见文档:

* [Worker线程使用说明](../harmonyos-references/js-apis-worker.md)
* [Worker简介](worker-introduction.md)

### 开发步骤

1. 引入头文件，创建worker线程，并注册回调。

   ```
   1. import { ErrorEvent, MessageEvents, worker } from '@kit.ArkTS'
   2. import { SendableObject } from '../util/SendableObject';
   3. import { common, sendableContextManager } from '@kit.AbilityKit';
   ```

   ```
   1. // 创建Worker对象。
   2. private workerInstance?: worker.ThreadWorker;
   3. @State currentProgress: number = 0;

   5. this.workerInstance = new worker.ThreadWorker('entry/ets/workers/task.ets');

   7. // 注册onmessage回调，当宿主线程接收到来自其创建的Worker通过workerPort.postMessage接口发送的消息时被调用，在宿主线程执行。
   8. this.workerInstance.onmessage = (e: MessageEvents) => {
   9. let data: string | number = e.data;
   10. if (typeof data === 'string') { // complete事件。
   11. console.info('workerInstance onmessage is: ', data);
   12. if (data === 'complete') {
   13. console.info('complete: ', data);
   14. this.workerInstance?.terminate();
   15. }
   16. } else if (typeof data === 'number') {
   17. this.currentProgress = data; // 当前进度。
   18. }
   19. }

   21. // 注册onErrors回调，可以捕获Worker线程的onmessage回调、timer回调以及文件执行等流程产生的全局异常，在宿主线程执行。
   22. this.workerInstance.onerror = (err: ErrorEvent) => {
   23. console.info("workerInstance onerror message is: " + err.message);
   24. }

   26. // 注册onmessageerror回调，当Worker对象接收到一条无法被序列化的消息时被调用，在宿主线程执行。
   27. this.workerInstance.onmessageerror = () => {
   28. console.info('workerInstance onmessageerror');
   29. }

   31. // 注册onexit回调，当Worker销毁时被调用，在宿主线程执行。
   32. this.workerInstance.onexit = (e: number) => {
   33. // 当Worker正常退出时code为0，异常退出时code为1。
   34. console.info("workerInstance onexit code is: ", e);
   35. }
   ```
2. 创建参数对象，向worker线程发送参数对象。

   如下是参数对象模型：

   ```
   1. import { sendableContextManager } from '@kit.AbilityKit';

   3. // 发送的参数必须加上@Sendable标注。
   4. @Sendable
   5. export class SendableObject {
   6. constructor(sendableContext: sendableContextManager.SendableContext, data: string = '') {
   7. this.sendableContext = sendableContext;
   8. this.data = data;
   9. }

   11. private sendableContext: sendableContextManager.SendableContext;
   12. private data: string;

   15. public getSendableContext() {
   16. return this.sendableContext;
   17. }

   19. public getData() {
   20. return this.data;
   21. }
   22. }
   ```

   如下是发送参数的逻辑：

   ```
   1. private context: Context | undefined;
   2. // 向Worker线程发送消息。
   3. this.context = this.getUIContext().getHostContext(); // 获取当前组件所在Ability的Context。
   4. if (this.context != undefined) {
   5. const sendableContext: sendableContextManager.SendableContext = sendableContextManager.convertFromContext(
   6. this.context);
   7. const sendableObject: SendableObject = new SendableObject(sendableContext, 'some information');
   8. this.workerInstance.postMessageWithSharedSendable(sendableObject);
   9. }
   ```
3. worker线程接收参数，并且执行转码的逻辑。

   worker线程接收参数：

   ```
   1. //worker线程接收参数。
   2. const sendableObject: SendableObject = event.data;
   3. const sendableContext: sendableContextManager.SendableContext =
   4. sendableObject.getSendableContext() as sendableContextManager.SendableContext;
   5. const context: common.Context =
   6. sendableContextManager.convertToContext(sendableContext) as common.Context;
   7. // 执行转码逻辑。
   8. await doSome(context);
   9. // 向主线程发送消息。
   10. workerPort.postMessage('start end');
   ```

   执行转码逻辑：

   ```
   1. async function doSome(context: common.Context) {
   2. console.info(`doSome in`);
   3. try {
   4. let transcoder = await media.createAVTranscoder();
   5. // 转码完成回调函数。
   6. transcoder.on('complete', async () => {
   7. console.info(`transcode complete`);
   8. fileIo.closeSync(transcoder.fdDst); // 关闭fdDst。
   9. await transcoder?.release()
   10. workerPort.postMessage('complete');
   11. })
   12. // 转码错误回调函数。
   13. transcoder.on('error', async (err: BusinessError) => {
   14. fileIo.closeSync(transcoder.fdDst);
   15. await transcoder?.release();
   16. })
   17. // 转码进度更新回调函数。
   18. transcoder.on('progressUpdate', (progress: number) => {
   19. console.info(`AVTranscoder progressUpdate = ${progress}`);
   20. workerPort.postMessage(progress);
   21. })

   23. try {
   24. // 获取输入文件fd，H264_AAC.mp4为rawfile目录下的预置资源，需要开发者根据实际情况进行替换。
   25. let fileDescriptor = await context.resourceManager.getRawFd('H264_AAC.mp4');
   26. transcoder.fdSrc = fileDescriptor; // 设置fdSrc。
   27. } catch (error) {
   28. console.error('Failed to get the file descriptor, please check the resource and path.');
   29. }
   30. // 设置输出文件路径，context.filesDir为应用的沙箱路径。
   31. let fdPath = context.filesDir + "/" + "VID_" + Date.parse(new Date().toString()) + ".mp4";
   32. let file = fileIo.openSync(fdPath, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
   33. let fd = file.fd;
   34. console.info(`file fd ${fd}`);
   35. transcoder.fdDst = file.fd;

   37. let config: media.AVTranscoderConfig = {
   38. fileFormat: media.ContainerFormatType.CFT_MPEG_4, // 封装格式。
   39. audioCodec: media.CodecMimeType.AUDIO_AAC, // 音频编码格式。
   40. videoCodec: media.CodecMimeType.VIDEO_AVC, // 视频编码格式。
   41. videoBitrate: 200000, // 视频比特率。
   42. }
   43. await transcoder?.prepare(config);
   44. await transcoder?.start();
   45. } catch (e) {
   46. console.error(`transcode error: code = ` + e.code.toString() + `, message = ${JSON.stringify(e.message)}`);
   47. }
   48. }
   ```
4. 监听转码的Complete回调，在转码结束的时候向主线程发送消息。

   ```
   1. // 转码完成回调函数。
   2. transcoder.on('complete', async () => {
   3. console.info(`transcode complete`);
   4. fileIo.closeSync(transcoder.fdDst); // 关闭fdDst。
   5. await transcoder?.release()
   6. workerPort.postMessage('complete');
   7. })
   ```
5. 主线程接收到worker线程转码结束的信息，销毁worker线程。

   ```
   1. // 注册onmessage回调，当宿主线程接收到来自其创建的Worker通过workerPort.postMessage接口发送的消息时被调用，在宿主线程执行。
   2. this.workerInstance.onmessage = (e: MessageEvents) => {
   3. let data: string | number = e.data;
   4. if (typeof data === 'string') {
   5. console.info('workerInstance onmessage is: ', data);
   6. if (data === 'complete') {
   7. console.info('complete: ', data);
   8. this.workerInstance?.terminate();
   9. }
   10. } else if (typeof data === 'number') {
   11. this.currentProgress = data;
   12. }
   13. }
   ```

## 运行示例工程

参考以下示例，使用worker线程的方式来实现异步线程进行转码。

1. 新建工程，下载[完整示例工程](https://gitcode.com/openharmony/applications_app_samples/tree/master/code/DocsSample/Media/AVTranscoder/AsyncTranscoder)，并将示例工程的资源复制到对应目录。

   ```
   1. AsyncTranscoder
   2. entry/build-profile.json5 (配置字段信息将Worker线程文件打包到应用)
   3. entry/src/main/ets/
   4. ├── pages
   5. │    └── Index.ets (转码界面)
   6. ├── util
   7. │    └── SendableObject.ets (Sendable对象)
   8. │
   9. └── workers
   10. └── task.ets (转码任务)

   12. entry/src/main/resources/
   13. ├── base
   14. │   ├── element
   15. │   │   ├── color.json
   16. │   │   ├── float.json
   17. │   │   └── string.json
   18. │   └── media
   19. │
   20. └── rawfile
   21. └── H264_AAC.mp4 (视频资源)
   ```
2. 编译新建工程并运行。
