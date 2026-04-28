---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-avscreencapture-for-screen-recording
title: 基于AVScreenCapture实现屏幕录制
breadcrumb: 最佳实践 > 媒体 > 音频和视频 > 基于AVScreenCapture实现屏幕录制
category: best-practices
scraped_at: 2026-04-28T08:20:48+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:9ebc4159498e18fa03cb75c99c366230855abbaeba984fba7c96b0e7771a1762
---

## 概述

[AVScreenCapture](../harmonyos-guides-V5/media-kit-intro-V5.md#avscreencapture)是系统提供的用于实现屏幕录制功能的模块，属于媒体子系统的核心能力之一。AVScreenCapture主要应用于需要捕获屏幕内容的场景，例如在线教育录课、游戏直播、会议录制、远程协作等。AVScreenCapture主要工作是捕获音频信号、视频信号，并通过音视频编码保存屏幕信息，提供录屏写文件和录屏转码流两套接口，能够输出原始码流和文件两种不同形式的信息。该模块允许调用者指定屏幕录制的编码格式、封装格式和文件路径等参数，同时支持全屏录制、指定窗口录制或指定物理屏录制的配置。

* 转码流形式：连续的二进制数据包（如：01001011 01100101...），无边界标记，不区分数据块。其存在形式为内存/网络传输中的瞬时状态，类似网络传输中的TCP流、摄像头实时视频流。其生命周期为实时生成、实时消费、立即销毁。
* 写文件形式：静态的存储容器，结构化存储单元（如：文件头 + 数据区 + 文件尾）， 具有明确的边界，通过文件系统标记起始和结束位置。其存在形式为存储介质中的持久实体，其生命周期包括创建、写入、关闭和长期存储。

原始码流

本文主要针对以下几种实现方案详细讲解其实现原理和开发流程。

* [使用AVScreenCaptureRecorder模块录屏写文件（ArkTS）](bpta-avscreencapture-for-screen-recording.md#section162864319340)
* [使用AVScreenCapture模块录屏写文件（C/C++）](bpta-avscreencapture-for-screen-recording.md#section6121629163710)
* [使用AVScreenCapture模块录屏转码流（C/C++）](bpta-avscreencapture-for-screen-recording.md#section15553154512379)

三种实现方案对比情况如下：

|  | 优点 | 缺点 | 适用场景 |
| --- | --- | --- | --- |
| 使用AVScreenCaptureRecorder模块录屏写文件（ArkTS） | * 开发逻辑简单，代码维护成本低，无需具备Native相关知识，开发效率相对较高。 * 内存管理相对安全，无需手动释放资源，GC自动回收。 * 与UI界面无缝联动，可以实时更新界面元素。 | * 功能缺失，仅支持文件输出模式（OH\_CAPTURE\_FILE），无法获取原始数据码流。 * 受JS运行时限制，高负载场景下性能相对较差。 * 实时性不佳，不适用于延迟敏感场景。 * 格式受限，仅支持输出MP4格式。 * CPU占用率高。 | 该方案适用于重视开发交互效率和UI界面交互，同时对实时性要求不高的常规场景，例如在线教育课程录制、简单屏幕录制等文件录制场景。 |
| 使用AVScreenCapture模块录屏写文件（C/C++） | * 开发逻辑简单，开发效率适中。 * 实时性表现一般，延迟低于ArkTS方法，但高于C/C++转码流方法。 * 支持动态音频切换。 * CPU占用率相对较低 | * 开发逻辑较为复杂，需要掌握C++/NDK相关知识。 * 需要手动释放资源。 * 仍依赖系统封装器，仅支持MP4视频格式。 * 无法获取原始数据码流，对数据进行相关操作。 | 该方案适用于对实时性、视频画质有较高要求，且需要动态音频切换的高性能场景，例如游戏高帧率录制、会议录制等文件录制场合。 |
| 使用AVScreenCapture模块录屏转码流（C/C++） | * 极致性能，实时性强，延迟极低。 * 可以自由掌控数据，支持自定义编码、多源合成及逐帧处理等。 * 资源优化，内存占用率极低。 | * 开发成本极高，需要具备音视频编码的专业知识。 * 风险较高，需要自行管理线程和内存安全风险。 * 容易出现编码器碎片化问题。 * 维护和调试都较为困难。 | 该方案适用于对实时性要求极高、需要多源合成及逐帧处理的专业场景，例如游戏直播、远程桌面控制和定制格式输出等。 |

开发者可以对比三种方式的优缺点及其适用场景，自行选择最适合的实现方案。

说明

在进行屏幕录制开发前需要申请相应权限：麦克风权限（**ohos.permission.MICROPHONE**）、后台长时任务权限（**ohos.permission.KEEP\_BACKGROUND\_RUNNING**）。其他权限可根据需要申请，例如：若需访问公共目录，则应申请公共目录的读写权限。

开发者如果想要了解音视频编码相关内容，可以参考：[音频编码](../harmonyos-guides/audio-encoding.md)和[视频编码](../harmonyos-guides/video-encoding.md)。

## 使用AVScreenCaptureRecorder模块录屏写文件（ArkTS）

### 场景描述

HarmonyOS 提供了用于实现录屏功能的ArkTS接口，能够支持屏幕录制及音频数据采集。然而，ArkTS侧的实现方案仅能通过文件形式将数据流转至其他模块进行播放或处理。

本节将通过一个案例介绍如何在ArkTS侧实现录屏存文件。在该案例中，用户点击屏幕录制按钮即可启动屏幕录制，期间可以切换至后台录制桌面或其他应用页面。当用户点击停止按钮或屏幕左上角录屏胶囊中的停止按钮时，屏幕录制将停止。录屏内容将保存至应用沙箱文件中，点击结束录屏后出现的播放按钮，即可播放录制的视频文件。

**案例展示图：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/GLz7oxkvSI2-VqCQHZUWNA/zh-cn_image_0000002358208918.gif?HW-CC-KV=V1&HW-CC-Date=20260428T002045Z&HW-CC-Expire=86400&HW-CC-Sign=597F5172AF0372A4C245465A88F7DA8E08E58DC3185E88F55099797494359400 "点击放大")

### 实现原理

**调用流程图**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/pEhryRo9Ro2Gv6lMYWeiDg/zh-cn_image_0000002439565978.png?HW-CC-KV=V1&HW-CC-Date=20260428T002045Z&HW-CC-Expire=86400&HW-CC-Sign=1C528A6B051ABCAC5C9788BA4EFF7EA509C1B175733E9DBF2DB3B116D68B0874)

当点击录制按钮时，会调用异步方法进行屏幕录制。关键过程如下：

1. 等到异步任务得到调度后，会先获取文件信息，用于保存录屏视频。
2. 接着会通过createAVScreenCaptureRecorder()方法构建出AVScreenCaptureRecorder的实例化对象。
3. 然后为该实例对象绑定状态变化监听函数和异常监听函数。
4. 接着还需要配置屏幕录制参数，然后根据参数配置对实例化对象进行初始化。
5. 初始化完成之后即可调用startRecording()方法开启屏幕录制。

当点击停止按钮时，同样系统会调用异步方法来停止录制。等到异步任务被调度后，将调用stopRecording()方法停止屏幕录制，随后关闭文件fd。

说明

EventLoop事件循环是ArkTS异步编程模型的核心（单线程+任务队列），其在JS/TS的基础上结合了HarmonyOS的UI框架和任务调度特性，主要用于管理代码执行顺序、处理异步操作（如网络请求、定时器、用户交互、I/O）以及更新UI等。

### 开发步骤

1. 获取文件信息。

   首先，通过时间戳和应用沙箱目录拼接出文件路径，然后利用文件管理模块的openSync()接口获取文件信息。后续的录屏文件将存储在该文件中。

   获取沙箱路径。

   ```
   1. private filesDir = this.getUIContext().getHostContext()?.filesDir;
   ```

   [ArkTSAVScreenCapture.ets](https://gitcode.com/HarmonyOS_Samples/BestPracticeSnippets/blob/master/avscreen-capture-screen-record-master/entry/src/main/ets/pages/ArkTSAVScreenCapture.ets#L27-L27)

   拼接文件路径并获取文件信息。

   ```
   1. public updateFileFd(filesDir: string) {
   2. // 获取文件fd
   3. this.fileName = systemDateTime.getTime(true).toString() + '.mp4';
   4. this.path = filesDir + '/' + this.fileName;
   5. try {
   6. this.file = fs.openSync(this.path, fs.OpenMode.READ_WRITE | fs.OpenMode.CREATE);
   7. } catch (error) {
   8. let err = error as BusinessError;
   9. hilog.error(0x0000, 'testTag', `openSync fail. code = ${err.code}, message = ${err.message}`);
   10. }
   11. }
   ```

   [MyAVScreenCapture.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/avscreen-capture-screen-record-master/entry/src/main/ets/model/MyAVScreenCapture.ets#L160-L171)
2. 创建AVScreenCaptureRecorder实例化对象并绑定监听函数。

   通过MediaKit提供的createAVScreenCaptureRecorder()接口构建实例对象，然后使用.on接口为其绑定可选的监听回调函数。在以下示例中，订阅了两个回调事件：stateChange（状态切换事件回调）和error（错误事件回调）。对于同一个回调事件，用户只能订阅一次，若重复订阅，则以最后一次订阅的回调接口为准。已订阅的回调事件还可以通过off接口取消订阅。

   ```
   1. // 获取fd
   2. this.updateFileFd(filesDir);
   3. // 实例化对象
   4. try {
   5. this.screenCapture = await media.createAVScreenCaptureRecorder();
   6. } catch (error) {
   7. let err = error as BusinessError;
   8. hilog.error(0x0000, 'testTag',
   9. `createAVScreenCaptureRecorder fail. code = ${err.code}, message = ${err.message}`);
   10. }
   11. if (this.screenCapture != undefined) {
   12. hilog.info(0xFF00, CommonConstants.LOG_TAG, 'ScreenCapture has been created successfully.');
   13. } else {
   14. hilog.info(0xFF00, CommonConstants.LOG_TAG, 'ScreenCapture creation failed.');
   15. return;
   16. }

   18. // 监听屏幕捕获的状态更改
   19. this.screenCapture?.on('stateChange', async (infoType: media.AVScreenCaptureStateCode) => {
   20. switch (infoType) {
   21. case media.AVScreenCaptureStateCode.SCREENCAPTURE_STATE_STARTED:
   22. hilog.info(0xFF00, CommonConstants.LOG_TAG, '录屏成功开始后会收到的回调.');
   23. break;
   24. case media.AVScreenCaptureStateCode.SCREENCAPTURE_STATE_CANCELED:
   25. this.screenCapture?.release();
   26. this.screenCapture = undefined;
   27. hilog.info(0xFF00, CommonConstants.LOG_TAG, '不允许使用录屏功能.');
   28. break;
   29. case media.AVScreenCaptureStateCode.SCREENCAPTURE_STATE_STOPPED_BY_USER:
   30. this.screenCapture?.release();
   31. this.screenCapture = undefined;
   32. AppStorage.setOrCreate('isRecordOne', false);
   33. AppStorage.setOrCreate('fileNameOne', this.fileName);
   34. hilog.info(0xFF00, CommonConstants.LOG_TAG,
   35. '通过屏幕录制胶囊结束屏幕录制，底层录制停止');
   36. break;
   37. case media.AVScreenCaptureStateCode.SCREENCAPTURE_STATE_INTERRUPTED_BY_OTHER:
   38. hilog.info(0xFF00, CommonConstants.LOG_TAG, '屏幕录制因其他中断而停止');
   39. break;
   40. case media.AVScreenCaptureStateCode.SCREENCAPTURE_STATE_STOPPED_BY_CALL:
   41. hilog.info(0xFF00, CommonConstants.LOG_TAG, '屏幕录制被电话打断');
   42. break;
   43. case media.AVScreenCaptureStateCode.SCREENCAPTURE_STATE_MIC_UNAVAILABLE:
   44. hilog.info(0xFF00, CommonConstants.LOG_TAG, '录屏麦克风不可用');
   45. break;
   46. case media.AVScreenCaptureStateCode.SCREENCAPTURE_STATE_MIC_MUTED_BY_USER:
   47. hilog.info(0xFF00, CommonConstants.LOG_TAG, '录屏麦克风被用户静音');
   48. break;
   49. case media.AVScreenCaptureStateCode.SCREENCAPTURE_STATE_MIC_UNMUTED_BY_USER:
   50. hilog.info(0xFF00, CommonConstants.LOG_TAG, '录屏麦克风被用户取消静音');
   51. break;
   52. case media.AVScreenCaptureStateCode.SCREENCAPTURE_STATE_ENTER_PRIVATE_SCENE:
   53. hilog.info(0xFF00, CommonConstants.LOG_TAG, '录屏进入隐私场景');
   54. break;
   55. case media.AVScreenCaptureStateCode.SCREENCAPTURE_STATE_EXIT_PRIVATE_SCENE:
   56. hilog.info(0xFF00, CommonConstants.LOG_TAG, '录屏退出隐私场景');
   57. break;
   58. case media.AVScreenCaptureStateCode.SCREENCAPTURE_STATE_STOPPED_BY_USER_SWITCHES:
   59. hilog.info(0xFF00, CommonConstants.LOG_TAG, '用户账号切换，底层录制会停止');
   60. break;
   61. default:
   62. break;
   63. }
   64. })

   66. // 监听异常
   67. this.screenCapture?.on('error', (err) => {
   68. hilog.info(0xFF00, CommonConstants.LOG_TAG, 'Handle exception cases.');
   69. })
   ```

   [MyAVScreenCapture.ets](https://gitcode.com/HarmonyOS_Samples/BestPracticeSnippets/blob/master/avscreen-capture-screen-record-master/entry/src/main/ets/model/MyAVScreenCapture.ets#L34-L102)
3. 配置录制参数并初始化AVScreenCaptureRecorder对象。

   示例中通过 getDefaultDisplaySync() 方法获取屏幕宽高。开发者也可以自定义屏幕宽高，但需注意，若设置不当，可能会导致录制的视频界面出现黑边。

   ```
   1. let displayInfo = display.getDefaultDisplaySync();
   ```

   [EntryAbility.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/avscreen-capture-screen-record-master/entry/src/main/ets/entryability/EntryAbility.ets#L112-L112)

   以下配置了屏幕录制参数，除了fd配置外，其余配置均为可选。未配置时，将采用默认值。默认值可参考：[AVScreenCaptureRecordConfig](../harmonyos-references/arkts-apis-media-i.md#avscreencapturerecordconfig12)。

   ```
   1. // 配置屏幕录制参数
   2. let captureConfig: media.AVScreenCaptureRecordConfig = {
   3. // 开发者可以根据自己的需要设置宽度和高度
   4. frameWidth: this.displayInfo.width,
   5. frameHeight: this.displayInfo.height,
   6. // 用于写入文件的文件描述符（fd）
   7. fd: (this.file as fs.File).fd,
   8. // 可选参数及其默认值
   9. videoBitrate: 10000000,
   10. audioSampleRate: 48000,
   11. audioChannelCount: 2,
   12. audioBitrate: 96000,
   13. displayId: 0,
   14. };
   ```

   [MyAVScreenCapture.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/avscreen-capture-screen-record-master/entry/src/main/ets/model/MyAVScreenCapture.ets#L106-L119)

   基于上述配置信息初始化screenCapture实例对象。

   ```
   1. await this.screenCapture?.init(captureConfig);
   ```

   [MyAVScreenCapture.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/avscreen-capture-screen-record-master/entry/src/main/ets/model/MyAVScreenCapture.ets#L123-L123)
4. 通过startRecording()接口开启录制。

   startRecording()接口以异步方式启动录屏，启动后录屏不会影响页面操作。

   ```
   1. await this.screenCapture?.startRecording();
   ```

   [MyAVScreenCapture.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/avscreen-capture-screen-record-master/entry/src/main/ets/model/MyAVScreenCapture.ets#L127-L127)
5. 通过stopRecording()停止录制并关闭文件。

   同样的，stopRecording()接口也是异步接口，示例中首先通过stopRecording()接口停止录制，然后调用release()方法销毁实例，释放资源。

   ```
   1. // 停止录屏
   2. public async stopRecording() {
   3. if (this.screenCapture == undefined) {
   4. hilog.info(0xFF00, CommonConstants.LOG_TAG, 'ScreenCapture exception.');
   5. return;
   6. }

   8. try {
   9. await this.screenCapture?.stopRecording();

   11. // 调用release()方法来销毁实例并释放资源
   12. await this.screenCapture?.release();

   14. // 关闭文件
   15. fs.close((this.file as fs.File).fd);
   16. } catch (error) {
   17. let err = error as BusinessError;
   18. hilog.error(0x0000, 'testTag', `stop fail. code = ${err.code}, message = ${err.message}`);
   19. }
   20. }
   ```

   [MyAVScreenCapture.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/avscreen-capture-screen-record-master/entry/src/main/ets/model/MyAVScreenCapture.ets#L136-L156)

说明

除了通过主动点击按钮调用stopRecording()来停止录屏外，还可以通过点击录屏胶囊中的结束按钮来停止录制。该方案主要依赖于回调函数实现，当用户点击胶囊中的停止按钮时，录屏对象实例screenCapture会触发SCREENCAPTURE\_STATE\_STOPPED\_BY\_USER的回调，通知应用录屏已停止，无需开发者主动调用stopRecording()方法。在C/C++方法中，对应的回调是OH\_SCREEN\_CAPTURE\_STATE\_STOPPED\_BY\_USER。

## 使用AVScreenCapture模块录屏写文件（C/C++）

### 场景描述

除了ArkTS侧接口，系统还提供实现录屏功能相应的C语言版本的API接口。该API接口支持文件和码流两种格式，本小节主要介绍其进行屏幕录制时，直接存文件的实现方案，该方案需要配置录屏的数据类型为OH\_CAPTURE\_FILE。

案例实现的页面效果与上一章节一致，主要区别在于代码层面。同样的，在该案例中用户点击屏幕录制按钮会开启屏幕录制，当用户点击停止按钮或者点击屏幕左上角录屏胶囊中的停止按钮会停止屏幕录制并将录屏信息保存到应用沙箱文件中。点击播放按钮会播放录制的视频文件。

**案例展示图：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/OrUye0qwTS-sf6qOW0ytgg/zh-cn_image_0000002358368862.gif?HW-CC-KV=V1&HW-CC-Date=20260428T002045Z&HW-CC-Expire=86400&HW-CC-Sign=7460A8799D92037F465F8D7940143C9429BC91539004E68FD1FF67A2B9132B5F "点击放大")

### 实现原理

**调用流程图**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/4dpGfiyHTqqvD4v8AMd_pw/zh-cn_image_0000002473046625.png?HW-CC-KV=V1&HW-CC-Date=20260428T002045Z&HW-CC-Expire=86400&HW-CC-Sign=036CC1F1F778A32ACE1DDAE44B523CB617BE17AA741535FB0DD147A74DA0C530 "点击放大")

当点击录制按钮时，会调用异步方法进行屏幕录制。关键过程如下：

1. 当异步任务被调度，会先获取一个文件信息，用于保存录屏视频。
2. 然后调用Native侧的方法，并传递文件fd、设备宽高等参数至Native侧。
3. 在Native侧，首先创建一个AVScreenCapture实例对象，并使用从ArkTS传递过来的参数（文件fd、设备宽高等）配置屏幕录制参数并进行初始化。
4. 初始化完成后，还需为该实例对象绑定可选的回调函数，如状态变更和数据处理等。
5. 最后，在完成所有配置后，调用OH\_AVScreenCapture\_StartScreenRecording()方法开始屏幕录制。

当点击停止按钮时，会调用相应的Native方法，Native侧通过调用OH\_AVScreenCapture\_StopScreenRecording()方法来停止屏幕录制；随后，控制权返回到ArkTS侧，在此调用异步方法以关闭文件fd。

### 开发步骤

1. 获取文件信息并调用Native侧方法传递参数。

   与上述方案类似，通过时间戳和应用沙箱目录拼接生成文件路径，然后利用文件管理模块提供的openSync()接口获取文件信息。该文件的fd将传递到Native侧，用于配置录屏数据的最终存储位置。在以下示例中，可以看到通过调用Native方法startScreenCaptureToFile()，将文件fd和屏幕的宽度及高度三个参数传递到Native侧。

   ```
   1. // 获取保存文件信息并调用Native方法
   2. async createVideoFd(): Promise<void> {
   3. // 拼接文件路径
   4. this.tmpFileNameTwo = systemDateTime.getTime(true) + '.mp4';
   5. // ...
   6. this.filepath = this.getUIContext().getHostContext()?.filesDir + '/' + this.tmpFileNameTwo;
   7. hilog.info(0xFF00, CommonConstants.LOG_TAG, 'filepath uri: %{public}s', this.filepath);

   9. try {
   10. // 获取文件信息
   11. this.file = fs.openSync(this.filepath, fs.OpenMode.READ_WRITE | fs.OpenMode.CREATE);
   12. // ...

   14. // 调用native方法开启录制并传递fd、宽高
   15. avScreenCapture.startScreenCaptureToFile(this.file.fd, this.displayInfo.width, this.displayInfo.height);

   17. // ...
   18. } catch (error) {
   19. let err = error as BusinessError;
   20. hilog.error(0x0000, 'testTag', `startScreenCaptureToFile fail. code = ${err.code}, message = ${err.message}`);
   21. }
   22. }
   ```

   [CAVScreenCaptureToFile.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/avscreen-capture-screen-record-master/entry/src/main/ets/pages/CAVScreenCaptureToFile.ets#L44-L73)

   这里获取屏幕宽高的实现代码与上述内容一致，都是通过ArkTS接口获取的。开发者也可以选择在Native侧获取，参考：[oh\_display\_manager.h](../harmonyos-references/capi-oh-display-manager-h.md)。

   ```
   1. let displayInfo = display.getDefaultDisplaySync();
   ```

   [EntryAbility.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/avscreen-capture-screen-record-master/entry/src/main/ets/entryability/EntryAbility.ets#L112-L112)
2. 创建AVScreenCapture实例化对象并初始化。

   首先，获取了ArkTS侧的参数信息，这些参数在配置录屏参数时将被使用。接着，调用OH\_AVScreenCapture\_Create()创建实例对象，随后配置录制参数并初始化AVScreenCapture对象。

   创建实例化对象。

   ```
   1. napi_value CAVScreenCaptureToFile::StartScreenCaptureToFile(napi_env env, napi_callback_info info) {
   2. size_t argc = 3;
   3. napi_value args[3] = {nullptr};
   4. napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);

   6. int32_t outputFd, videoWidth, videoHeight;
   7. // 获取参数：文件fd和宽高
   8. napi_get_value_int32(env, args[0], &outputFd);
   9. napi_get_value_int32(env, args[1], &videoWidth);
   10. napi_get_value_int32(env, args[2], &videoHeight);
   11. OH_LOG_INFO(LOG_APP, "文件FD为 %{public}d", outputFd);
   12. if (outputFd <= 0) {
   13. OH_LOG_ERROR(LOG_APP, "FD ERROR: %{public}d", outputFd);
   14. napi_value res;
   15. napi_create_int32(env, -1, &res);
   16. return res;
   17. }

   19. if (g_avCapture_ != nullptr) {
   20. StopScreenCaptureRecording(g_avCapture_);
   21. OH_AVScreenCapture_Release(g_avCapture_);
   22. }
   23. // 创建实例化对象
   24. g_avCapture_ = OH_AVScreenCapture_Create();
   25. if (g_avCapture_ == nullptr) {
   26. OH_LOG_ERROR(LOG_APP, "CAVScreenCaptureToFile create screen capture failed");
   27. }

   29. // ...
   30. }
   ```

   [CAVScreenCaptureToFile.cpp](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/avscreen-capture-screen-record-master/entry/src/main/cpp/CAVScreenCaptureToFile/CAVScreenCaptureToFile.cpp#L205-L287)

   录屏模式，录屏流数据类型以及录屏文件参数配置。

   上面获取的文件fd信息也是在此处配置的。直接将录屏保存到文件时，需要将dataType值设置为OH\_CAPTURE\_FILE。当数据格式为OH\_CAPTURE\_FILE时，必须配置录制文件参数（recorderInfo），其中包含文件保存的路径信息。在将录屏保存为文件时，默认录制内部音频，但也可以同时录制内外音频，且麦克风可以动态开启或关闭。可以使用OH\_AVScreenCapture\_SetMicrophoneEnabled()函数动态控制麦克风的开关。

   ```
   1. OH_AVScreenCaptureConfig config_;
   2. OH_RecorderInfo recorderInfo;

   4. // 转文件fd为url
   5. std::string fileUrl = "fd://" + std::to_string(outputFd);
   6. recorderInfo.url = const_cast<char *>(fileUrl.c_str());
   7. // 文件格式MP4
   8. recorderInfo.fileFormat = OH_ContainerFormatType::CFT_MPEG_4;
   9. OH_LOG_INFO(LOG_APP, "CAVScreenCaptureToFile ScreenCapture fileUrl %{public}s", fileUrl.c_str());

   11. // 调用音视频录制参数配置函数
   12. SetConfigAsFile(config_, videoWidth, videoHeight);
   13. config_.captureMode = OH_CAPTURE_HOME_SCREEN;
   14. config_.dataType = OH_CAPTURE_FILE;
   15. config_.recorderInfo = recorderInfo;

   17. // 设置麦克风开关
   18. bool isMicrophone = true;
   19. OH_AVScreenCapture_SetMicrophoneEnabled(g_avCapture_, isMicrophone);

   21. OH_AVScreenCapture_SetCanvasRotation(g_avCapture_, true);
   ```

   [CAVScreenCaptureToFile.cpp](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/avscreen-capture-screen-record-master/entry/src/main/cpp/CAVScreenCaptureToFile/CAVScreenCaptureToFile.cpp#L235-L255)

   音视频录制参数配置。

   上面获取到的屏幕宽高数据是在这里配置的。请注意，内录参数为必填项。如果同时设置了内录和外录参数，内录和麦克风（即外录）的参数设置需要保持一致。

   ```
   1. void CAVScreenCaptureToFile::SetConfigAsFile(OH_AVScreenCaptureConfig &config, int32_t videoWidth,
   2. int32_t videoHeight) {
   3. // 音频配置
   4. OH_AudioCaptureInfo micCapInfo = {.audioSampleRate = 48000, .audioChannels = 2, .audioSource = OH_SOURCE_DEFAULT};
   5. OH_AudioCaptureInfo innerCapInfo = {.audioSampleRate = 48000, .audioChannels = 2, .audioSource = OH_ALL_PLAYBACK};
   6. OH_AudioEncInfo audioEncInfo = {.audioBitrate = 96000, .audioCodecformat = OH_AudioCodecFormat::OH_AAC_LC};
   7. OH_AudioInfo audioInfo = {.micCapInfo = micCapInfo, .innerCapInfo = innerCapInfo, .audioEncInfo = audioEncInfo};

   9. // 视频配置
   10. OH_VideoCaptureInfo videoCapInfo = {
   11. .videoFrameWidth = videoWidth, .videoFrameHeight = videoHeight, .videoSource = OH_VIDEO_SOURCE_SURFACE_RGBA};
   12. OH_VideoEncInfo videoEncInfo = {
   13. .videoCodec = OH_VideoCodecFormat::OH_H264, .videoBitrate = 10000000, .videoFrameRate = 30};
   14. OH_VideoInfo videoInfo = {.videoCapInfo = videoCapInfo, .videoEncInfo = videoEncInfo};

   16. config = {
   17. .captureMode = OH_CAPTURE_HOME_SCREEN,
   18. .dataType = OH_ORIGINAL_STREAM,
   19. .audioInfo = audioInfo,
   20. .videoInfo = videoInfo,
   21. .recorderInfo = {},
   22. };
   23. }
   ```

   [CAVScreenCaptureToFile.cpp](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/avscreen-capture-screen-record-master/entry/src/main/cpp/CAVScreenCaptureToFile/CAVScreenCaptureToFile.cpp#L143-L165)

   根据配置初始化AVScreenCapture实例对象。

   ```
   1. OH_AVSCREEN_CAPTURE_ErrCode result = OH_AVScreenCapture_Init(g_avCapture_, config_);
   ```

   [CAVScreenCaptureToFile.cpp](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/avscreen-capture-screen-record-master/entry/src/main/cpp/CAVScreenCaptureToFile/CAVScreenCaptureToFile.cpp#L259-L259)
3. 绑定回调函数

   这里设置了 stateChange（状态切换事件回调）和 error（错误事件回调）。

   ```
   1. // 设置回调
   2. OH_AVScreenCapture_SetErrorCallback(g_avCapture_, OnErrorSaveFile, nullptr);
   3. OH_AVScreenCapture_SetStateCallback(g_avCapture_, OnStateChangeSaveFile, nullptr);
   ```

   [CAVScreenCaptureToFile.cpp](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/avscreen-capture-screen-record-master/entry/src/main/cpp/CAVScreenCaptureToFile/CAVScreenCaptureToFile.cpp#L268-L270)

   回调具体实现如下：

   状态变化回调。

   ```
   1. void CAVScreenCaptureToFile::OnStateChangeSaveFile(struct OH_AVScreenCapture *capture,
   2. OH_AVScreenCaptureStateCode stateCode, void *userData) {
   3. (void)capture;
   4. switch (stateCode) {
   5. case OH_SCREEN_CAPTURE_STATE_STARTED: {
   6. OH_LOG_INFO(LOG_APP, "录屏开始状态变更");
   7. break;
   8. }

   10. case OH_SCREEN_CAPTURE_STATE_CANCELED: {
   11. OH_LOG_INFO(LOG_APP, "录屏取消状态变更 ");
   12. StopScreenCaptureRecording(capture);
   13. break;
   14. }
   15. case OH_SCREEN_CAPTURE_STATE_STOPPED_BY_CALL: {
   16. OH_LOG_INFO(LOG_APP,
   17. "录屏被电话打断状态处理");
   18. break;
   19. }
   20. case OH_SCREEN_CAPTURE_STATE_MIC_UNAVAILABLE: {
   21. OH_LOG_INFO(LOG_APP,
   22. "录屏中途麦克风无法获取状态");
   23. break;
   24. }
   25. case OH_SCREEN_CAPTURE_STATE_INTERRUPTED_BY_OTHER: {
   26. OH_LOG_INFO(LOG_APP,
   27. "录屏状态被打断");
   28. break;
   29. }
   30. case OH_SCREEN_CAPTURE_STATE_MIC_MUTED_BY_USER: {
   31. OH_LOG_INFO(LOG_APP,
   32. "录屏中途用户将麦克风禁音");
   33. break;
   34. }

   36. case OH_SCREEN_CAPTURE_STATE_MIC_UNMUTED_BY_USER: {
   37. OH_LOG_INFO(LOG_APP,
   38. "录屏中途用户将麦克风解除禁音");
   39. break;
   40. }

   42. case OH_SCREEN_CAPTURE_STATE_ENTER_PRIVATE_SCENE: {
   43. OH_LOG_INFO(LOG_APP,
   44. "录屏进入隐私状态");
   45. std::thread releaseSCInstanceThread(ReleaseSCWorker, capture);
   46. releaseSCInstanceThread.detach();
   47. break;
   48. }

   50. case OH_SCREEN_CAPTURE_STATE_EXIT_PRIVATE_SCENE: {
   51. OH_LOG_INFO(LOG_APP,
   52. "录屏退出隐私模式状态");
   53. break;
   54. }

   56. case OH_SCREEN_CAPTURE_STATE_STOPPED_BY_USER: {
   57. napi_acquire_threadsafe_function(tsFn);
   58. napi_call_threadsafe_function(tsFn, nullptr, napi_tsfn_nonblocking);
   59. napi_release_threadsafe_function(tsFn, napi_tsfn_release);
   60. tsFn = nullptr;
   61. OH_LOG_INFO(LOG_APP,
   62. "录屏被用户切换打断");
   63. std::thread releaseSCInstanceThread(ReleaseSCWorker, capture);
   64. releaseSCInstanceThread.detach();
   65. break;
   66. }

   68. default:
   69. break;
   70. }

   72. (void)userData;
   73. }
   ```

   [CAVScreenCaptureToFile.cpp](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/avscreen-capture-screen-record-master/entry/src/main/cpp/CAVScreenCaptureToFile/CAVScreenCaptureToFile.cpp#L64-L136)

   错误监听回调。

   ```
   1. void CAVScreenCaptureToFile::OnErrorSaveFile(OH_AVScreenCapture *capture, int32_t errorCode, void *userData) {
   2. (void)capture;
   3. OH_LOG_INFO(LOG_APP, "录屏发生错误，错误码为 %{public}d", errorCode);
   4. (void)userData;
   5. }
   ```

   [CAVScreenCaptureToFile.cpp](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/avscreen-capture-screen-record-master/entry/src/main/cpp/CAVScreenCaptureToFile/CAVScreenCaptureToFile.cpp#L45-L49)
4. 通过OH\_AVScreenCapture\_StartScreenRecording()开启录制。

   ```
   1. result = OH_AVScreenCapture_StartScreenRecording(g_avCapture_);
   ```

   [CAVScreenCaptureToFile.cpp](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/avscreen-capture-screen-record-master/entry/src/main/cpp/CAVScreenCaptureToFile/CAVScreenCaptureToFile.cpp#L274-L274)
5. 通过调用OH\_AVScreenCapture\_StopScreenRecording()停止录制，然后释放ScreenCapture实例。

   ```
   1. napi_value CAVScreenCaptureToFile::StopScreenCaptureToFile(napi_env env, napi_callback_info info) {
   2. // ...

   4. OH_LOG_INFO(LOG_APP, "停止屏幕录制");
   5. result = OH_AVScreenCapture_StopScreenRecording(g_avCapture_);
   6. if (result != AV_SCREEN_CAPTURE_ERR_BASE) {
   7. OH_LOG_ERROR(
   8. LOG_APP,
   9. "停止屏幕录制错误，结果为：%{public}d",
   10. result);
   11. } else {
   12. OH_LOG_INFO(LOG_APP, "停止屏幕录制成功");
   13. }
   14. result = OH_AVScreenCapture_Release(g_avCapture_);
   15. if (result != AV_SCREEN_CAPTURE_ERR_BASE) {
   16. OH_LOG_ERROR(LOG_APP, "释放实例化对象异常，错误为: %{public}d",
   17. result);
   18. } else {
   19. OH_LOG_INFO(LOG_APP, "释放实例化对象成功");
   20. }
   21. // ...
   22. }
   ```

   [CAVScreenCaptureToFile.cpp](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/avscreen-capture-screen-record-master/entry/src/main/cpp/CAVScreenCaptureToFile/CAVScreenCaptureToFile.cpp#L169-L201)

   然后在ArkTS侧关闭文件。

   ```
   1. async releaseFD() {
   2. if (this.file?.fd != undefined && this.file.fd?.valueOf() > 0) {
   3. // 关闭文件
   4. try {
   5. fs.close(this.file.fd);
   6. } catch (error) {
   7. let err = error as BusinessError;
   8. hilog.error(0x0000, 'testTag', `close fail. code = ${err.code}, message = ${err.message}`);
   9. }
   10. }
   11. }
   ```

   [CAVScreenCaptureToFile.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/avscreen-capture-screen-record-master/entry/src/main/ets/pages/CAVScreenCaptureToFile.ets#L77-L88)

## 使用AVScreenCapture模块录屏转码流（C/C++）

### 场景描述

本小节主要介绍通过C语言版本的API实现屏幕录制的另一种方法，即将录屏数据提取为码流，然后通过该码流合成视频文件。此方案需要将录屏的数据类型配置为OH\_ORIGINAL\_STREAM，实现过程较为复杂，涉及绑定音频和视频编码器以及封装器对数据进行处理。

说明

本案例中，屏幕录制使用的是AVScreenCapture框架能力，音频流使用的是AudioCapturer创建的音频采集器录制，如需对音频流进行操作，需要修改AudioCapturer对应的相关配置。

案例实现的页面效果与前两个章节一致，通过点击对应按钮开启/关闭录屏，录屏结束后可以播放录屏视频。

**案例展示图：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0d/v3/MYLwNYkjTj24EMEQPsgpCw/zh-cn_image_0000002358208954.gif?HW-CC-KV=V1&HW-CC-Date=20260428T002045Z&HW-CC-Expire=86400&HW-CC-Sign=F65285A1EA41BC6DD877EFEF561C737FFA7D8AB13BA3D341BB5154B5F5AB3860 "点击放大")

### 实现原理

**调用流程图**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/jtQCI3y2SwGCRPdZGnaUew/zh-cn_image_0000002472889049.png?HW-CC-KV=V1&HW-CC-Date=20260428T002045Z&HW-CC-Expire=86400&HW-CC-Sign=0AAD100B954FC54177F8C3342AF5ADAD27D12E322C16B853B0B47B3F8BF6B40D "点击放大")

当点击录制按钮时，系统会调用异步方法来执行屏幕录制。关键过程如下：

1. 当异步任务被调度后，系统会先获取文件信息，用于保存录屏视频。
2. 然后调用Native侧方法，并传递文件fd、设备宽度等参数至Native侧。
3. Native侧首先会创建音频编码器、视频编码器以及封装器对应的实例对象并绑定相应的数据处理回调函数。
4. 然后配置音频录制参数并初始化音频录制实例对象（OH\_AudioCapturer类型），同时配置屏幕录制参数并初始化屏幕录制实例对象（OH\_AVScreenCapture类型）。
5. 最后，启动音视频录制，并创建音视频编码器及封装器的子线程，这些子线程主要用于处理采集的音视频码流数据并进行封装。

当点击停止按钮时，会调用相应的Native方法。Native侧首先等待数据写入完成，随后启动子线程来释放音视频编码器及封装器的相关资源。此时，Native主线程将等待这些资源释放完毕，然后调用OH\_AVScreenCapture\_StopScreenRecording()方法停止屏幕录制。之后，控制权返回到ArkTS侧，在ArkTS侧调用异步方法关闭文件fd。

### 开发步骤

1. 获取文件信息并调用Native侧方法传递参数。

   这一步与C/C++侧录屏存文件的方法一致。通过时间戳和应用沙箱目录拼接出文件路径，然后获取文件信息。接着调用Native方法startScreenCaptureToStream()并传递参数。

   ```
   1. // 获取保存文件信息并调用Native方法
   2. async createVideoFd(): Promise<void> {
   3. // 拼接文件路径
   4. this.tmpFileNameThree = systemDateTime.getTime(true) + '.mp4';
   5. // ...
   6. this.filepath = this.getUIContext().getHostContext()?.filesDir + '/' + this.tmpFileNameThree;
   7. hilog.info(0xFF00, CommonConstants.LOG_TAG, 'filepath uri: %{public}s', this.filepath);
   8. try {
   9. // 获取文件信息
   10. this.file = fs.openSync(this.filepath, fs.OpenMode.READ_WRITE | fs.OpenMode.CREATE);

   12. // ...

   14. // 调用native方法开启录制并传递fd、宽高
   15. avScreenCapture.startScreenCaptureToStream(this.file.fd, this.displayInfo.width, this.displayInfo.height)

   17. // ...
   18. } catch (error) {
   19. let err = error as BusinessError;
   20. hilog.error(0x0000, 'testTag', `startScreenCaptureToStream fail. code = ${err.code}, message = ${err.message}`);
   21. }
   22. }
   ```

   [CAVScreenCaptureToStream.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/avscreen-capture-screen-record-master/entry/src/main/ets/pages/CAVScreenCaptureToStream.ets#L44-L73)

   通过ArkTS侧接口获取屏幕宽高，Native侧获取方法参考：[oh\_display\_manager.h](../harmonyos-references/capi-oh-display-manager-h.md)。

   ```
   1. let displayInfo = display.getDefaultDisplaySync();
   ```

   [EntryAbility.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/avscreen-capture-screen-record-master/entry/src/main/ets/entryability/EntryAbility.ets#L112-L112)
2. 初始化音频编码器、视频编码器以及封装器。

   首先，也需要获取ArkTS侧的参数，这部分内容在前面已经介绍过，这里不再赘述。具体可参考使用AVScreenCapture模块进行录屏存文件的章节。

   音视频编码器的相关配置中，sampleInfo用于存储参数配置信息，这些信息将在后续配置音频编码器、视频编码器及封装器配置项时使用。

   ```
   1. void CAVScreenCaptureToStream::InitConfig(int32_t outputFd, int32_t videoWidth, int32_t videoHeight) {
   2. sampleInfo_.outputFd = outputFd;

   4. // 视频编码器配置
   5. sampleInfo_.videoWidth = videoWidth;
   6. sampleInfo_.videoHeight = videoHeight;
   7. sampleInfo_.frameRate = 30;
   8. sampleInfo_.bitrate = 10000000;
   9. sampleInfo_.videoCodecMime = "video/avc";

   11. // 音频编码器配置
   12. sampleInfo_.audioCodecMime = OH_AVCODEC_MIMETYPE_AUDIO_AAC;
   13. sampleInfo_.audioSampleFormat = OH_BitsPerSample::SAMPLE_S16LE;
   14. sampleInfo_.audioSampleRate = 48000;
   15. sampleInfo_.audioChannelCount = 2;
   16. sampleInfo_.audioBitRate = 96000;
   17. sampleInfo_.audioChannelLayout = OH_AudioChannelLayout::CH_LAYOUT_STEREO;
   18. sampleInfo_.audioMaxInputSize = sampleInfo_.audioSampleRate * 0.02 * sampleInfo_.audioChannelCount * sizeof(short);

   20. std::lock_guard<std::mutex> lock(mutex_);

   22. // 声明音视频编码器、音频采集器及封装器类对象
   23. audioEncoder_ = std::make_unique<AudioEncoder>();
   24. audioCapturer_ = std::make_unique<AudioCapturer>();
   25. videoEncoder_ = std::make_unique<VideoEncoder>();
   26. muxer_ = std::make_unique<Muxer>();

   28. // 根据文件fd创建封装器并初始化
   29. muxer_->Create(sampleInfo_.outputFd);
   30. muxer_->Config(sampleInfo_);

   32. // 创建音视频编码器
   33. CreateEncoder();

   35. // 初始化音频采集器对象
   36. audioCapturer_->AudioCapturerInit(sampleInfo_, audioEncContext_);

   38. // ...
   39. }
   ```

   [CAVScreenCaptureToStream.cpp](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/avscreen-capture-screen-record-master/entry/src/main/cpp/CAVScreenCaptureToStream/CAVScreenCaptureToStream.cpp#L234-L274)

   创建封装器对象。

   需要提供文件fd及封装器的输出格式，此处配置为MP4格式。

   ```
   1. int32_t Muxer::Create(int32_t fd) {
   2. muxer_ = OH_AVMuxer_Create(fd, AV_OUTPUT_FORMAT_MPEG_4);
   3. return 0;
   4. }
   ```

   [Muxer.cpp](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/avscreen-capture-screen-record-master/entry/src/main/cpp/CAVScreenCaptureToStream/Muxer.cpp#L30-L33)

   配置封装器配置项。

   通过调用OH\_AVFormat\_CreateVideoFormat()创建视频格式来添加视频轨道。

   配置完成后，即可调用OH\_AVMuxer\_Start()开始封装音视频数据。

   ```
   1. int32_t Muxer::Config(SampleInfo &sampleInfo) {
   2. // 创建并添加音频轨
   3. OH_AVFormat *formatAudio = OH_AVFormat_CreateAudioFormat(sampleInfo.audioCodecMime.data(),
   4. sampleInfo.audioSampleRate, sampleInfo.audioChannelCount);
   5. // 设置相关参数
   6. OH_AVFormat_SetIntValue(formatAudio, OH_MD_KEY_PROFILE, AAC_PROFILE_LC);

   8. int32_t ret = OH_AVMuxer_AddTrack(muxer_, &audioTrackId_, formatAudio);
   9. OH_AVFormat_Destroy(formatAudio);

   11. // 创建并添加视频轨
   12. OH_AVFormat *formatVideo =
   13. OH_AVFormat_CreateVideoFormat(sampleInfo.videoCodecMime.data(), sampleInfo.videoWidth, sampleInfo.videoHeight);

   15. // 设置相关参数
   16. OH_AVFormat_SetDoubleValue(formatVideo, OH_MD_KEY_FRAME_RATE, sampleInfo.frameRate);
   17. OH_AVFormat_SetIntValue(formatVideo, OH_MD_KEY_WIDTH, sampleInfo.videoWidth);
   18. OH_AVFormat_SetIntValue(formatVideo, OH_MD_KEY_HEIGHT, sampleInfo.videoHeight);
   19. OH_AVFormat_SetStringValue(formatVideo, OH_MD_KEY_CODEC_MIME, sampleInfo.videoCodecMime.data());

   21. ret = OH_AVMuxer_AddTrack(muxer_, &videoTrackId_, formatVideo);
   22. if (ret != AV_ERR_OK) {
   23. OH_LOG_ERROR(LOG_APP, "AddTrack failed");
   24. }
   25. OH_AVFormat_Destroy(formatVideo);
   26. formatVideo = nullptr;
   27. return ret;
   28. }
   ```

   [Muxer.cpp](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/avscreen-capture-screen-record-master/entry/src/main/cpp/CAVScreenCaptureToStream/Muxer.cpp#L37-L64)

   创建音频编码器。

   从mime类型创建音频编码器实例。

   ```
   1. // 创建音频编码器
   2. int32_t AudioEncoder::Create(const std::string &codecMime) {
   3. encoder_ = OH_AudioCodec_CreateByMime(codecMime.c_str(), true);
   4. return 0;
   5. }
   ```

   [AudioEncoder.cpp](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/avscreen-capture-screen-record-master/entry/src/main/cpp/CAVScreenCaptureToStream/AudioEncoder.cpp#L24-L28)

   配置音频编码器。

   首先，将配置信息写入format，然后通过OH\_AudioCodec\_Configure()接口配置编码器。接下来，使用OH\_AudioCodec\_RegisterCallback()方法注册回调函数。这些回调函数包括：监控编解码器操作错误、监控编解码器流变化、监控编解码器需要输入数据、监控编解码器已生成输出数据。请注意，音频编码器目前不支持监控编解码器流变化的回调。

   ```
   1. int32_t AudioEncoder::Config(SampleInfo &sampleInfo, CodecUserData *codecUserData) {
   2. OH_AVFormat *format = OH_AVFormat_Create();
   3. if (format == nullptr) {
   4. OH_LOG_ERROR(LOG_APP, "AVFormat create failed");
   5. }

   7. // 配置相关参数
   8. OH_AVFormat_SetIntValue(format, OH_MD_KEY_AUDIO_SAMPLE_FORMAT, sampleInfo.audioSampleFormat);
   9. OH_AVFormat_SetIntValue(format, OH_MD_KEY_AUD_CHANNEL_COUNT, sampleInfo.audioChannelCount);
   10. OH_AVFormat_SetIntValue(format, OH_MD_KEY_AUD_SAMPLE_RATE, sampleInfo.audioSampleRate);
   11. OH_AVFormat_SetLongValue(format, OH_MD_KEY_BITRATE, sampleInfo.audioBitRate);
   12. OH_AVFormat_SetLongValue(format, OH_MD_KEY_CHANNEL_LAYOUT, sampleInfo.audioChannelLayout);
   13. OH_AVFormat_SetIntValue(format, OH_MD_KEY_MAX_INPUT_SIZE, sampleInfo.audioMaxInputSize);
   14. int ret = OH_AudioCodec_Configure(encoder_, format);
   15. if (ret != AV_ERR_OK) {
   16. OH_LOG_ERROR(LOG_APP, "Config failed, ret: %{public}d", ret);
   17. }
   18. OH_AVFormat_Destroy(format);
   19. format = nullptr;

   21. // 设置音频编码器处理回调
   22. OH_AudioCodec_RegisterCallback(encoder_,
   23. {AudioEncoder::OnCodecError, AudioEncoder::OnCodecFormatChange,
   24. AudioEncoder::OnNeedInputBuffer, AudioEncoder::OnNewOutputBuffer},
   25. codecUserData);
   26. // 准备编码器内部资源，必须在调用此接口之前调用配置接口
   27. ret = OH_AudioCodec_Prepare(encoder_);
   28. if (ret != AV_ERR_OK) {
   29. OH_LOG_ERROR(LOG_APP, "Prepare failed, ret: %{public}d", ret);
   30. }
   31. return 0;
   32. }
   ```

   [AudioEncoder.cpp](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/avscreen-capture-screen-record-master/entry/src/main/cpp/CAVScreenCaptureToStream/AudioEncoder.cpp#L35-L66)

   创建视频编码器。

   同样从mime类型创建视频编码器实例。

   ```
   1. void VideoEncoder::Create(const std::string &videoCodecMime) {
   2. encoder_ = OH_VideoEncoder_CreateByMime(videoCodecMime.c_str());
   3. }
   ```

   [VideoEncoder.cpp](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/avscreen-capture-screen-record-master/entry/src/main/cpp/CAVScreenCaptureToStream/VideoEncoder.cpp#L20-L22)

   配置视频编码器。

   与音频编码器配置方法相同，将配置信息写入format，然后通过OH\_VideoEncoder\_Configure()接口进行编码器配置。接下来，使用OH\_VideoEncoder\_RegisterCallback()方法注册回调函数。这些回调函数用于监控编解码器操作错误、编解码器流变化、编解码器需要输入数据以及编解码器已生成输出数据。

   ```
   1. int32_t VideoEncoder::Config(SampleInfo &sampleInfo, CodecUserData *codecUserData) {
   2. OH_AVFormat *format = OH_AVFormat_Create();

   4. // 配置相关参数
   5. OH_AVFormat_SetIntValue(format, OH_MD_KEY_WIDTH, sampleInfo.videoWidth);
   6. OH_AVFormat_SetIntValue(format, OH_MD_KEY_HEIGHT, sampleInfo.videoHeight);
   7. OH_AVFormat_SetDoubleValue(format, OH_MD_KEY_FRAME_RATE, sampleInfo.frameRate);
   8. OH_AVFormat_SetIntValue(format, OH_MD_KEY_PIXEL_FORMAT, sampleInfo.pixelFormat);
   9. OH_AVFormat_SetIntValue(format, OH_MD_KEY_VIDEO_ENCODE_BITRATE_MODE, sampleInfo.bitrateMode);
   10. OH_AVFormat_SetLongValue(format, OH_MD_KEY_BITRATE, sampleInfo.bitrate);
   11. OH_AVFormat_SetIntValue(format, OH_MD_KEY_PROFILE, sampleInfo.hevcProfile);

   13. int ret = OH_VideoEncoder_Configure(encoder_, format);
   14. if (ret != AV_ERR_OK) {
   15. OH_LOG_ERROR(LOG_APP, "Config failed, ret: %{public}d", ret);
   16. }
   17. OH_AVFormat_Destroy(format);
   18. format = nullptr;

   20. // 根据视频编码器获取Surface
   21. OH_VideoEncoder_GetSurface(encoder_, &sampleInfo.window);

   23. // 设置视频编码器处理回调
   24. OH_VideoEncoder_RegisterCallback(encoder_,
   25. {VideoEncoder::OnCodecError, VideoEncoder::OnCodecFormatChange,
   26. VideoEncoder::OnNeedInputBuffer, VideoEncoder::OnNewOutputBuffer},
   27. codecUserData);
   28. // 准备编码器内部资源，必须在调用此接口之前调用配置接口
   29. OH_VideoEncoder_Prepare(encoder_);

   31. return 0;
   32. }
   ```

   [VideoEncoder.cpp](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/avscreen-capture-screen-record-master/entry/src/main/cpp/CAVScreenCaptureToStream/VideoEncoder.cpp#L26-L57)
3. 初始化音频采集（音频录制）器。

   首先，创建一个音频流构造器，然后设置其相关属性值，并设置输入音频流的回调。OnReadData回调用于读取音频数据。接着，通过OH\_AudioStreamBuilder\_GenerateCapturer()方法，根据音频流构造器创建音频流实例。

   ```
   1. // 初始化音频采集器
   2. void AudioCapturer::AudioCapturerInit(SampleInfo &sampleInfo, CodecUserData *audioEncContext)
   3. {
   4. AudioCapturerRelease();

   6. // 创建builder
   7. OH_AudioStream_Type type = AUDIOSTREAM_TYPE_CAPTURER;
   8. OH_AudioStreamBuilder_Create(&builder_, type);
   9. // 设置参数和回调
   10. OH_AudioStreamBuilder_SetSamplingRate(builder_, sampleInfo.audioSampleRate);
   11. OH_AudioStreamBuilder_SetChannelCount(builder_, sampleInfo.audioChannelCount);
   12. OH_AudioStreamBuilder_SetSampleFormat(builder_, AUDIOSTREAM_SAMPLE_S16LE);
   13. OH_AudioStreamBuilder_SetLatencyMode(builder_, AUDIOSTREAM_LATENCY_MODE_NORMAL);
   14. OH_AudioStreamBuilder_SetEncodingType(builder_, AUDIOSTREAM_ENCODING_TYPE_RAW);
   15. OH_AudioCapturer_Callbacks callbacks;
   16. callbacks.OH_AudioCapturer_OnReadData = AudioCapturerOnReadData;
   17. OH_AudioStreamBuilder_SetCapturerCallback(builder_, callbacks, audioEncContext);
   18. // 创建 OH_AudioCapturer对象
   19. OH_AudioStreamBuilder_GenerateCapturer(builder_, &audioCapturer_);
   20. }
   ```

   [AudioCapturer.cpp](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/avscreen-capture-screen-record-master/entry/src/main/cpp/CAVScreenCaptureToStream/AudioCapturer.cpp#L43-L62)
4. 初始化视频采集（视频录制）器。

   类似于上述C/C+文件存储方法，首先创建实例化对象，接着配置相关回调函数及参数。随后，调用OH\_AVScreenCapture\_Init()方法初始化视频采集器。

   ```
   1. void CAVScreenCaptureToStream::StartScreenCapture(int32_t outputFd, int32_t videoWidth, int32_t videoHeight) {
   2. // ...

   4. if (g_avCapture != nullptr) {
   5. StopScreenCaptureRecording(g_avCapture);
   6. }

   8. // 创建实例化对象
   9. g_avCapture = OH_AVScreenCapture_Create();
   10. if (g_avCapture == nullptr) {
   11. OH_LOG_ERROR(LOG_APP, "create screen capture failed");
   12. }
   13. OH_LOG_INFO(LOG_APP, "ScreenCapture after create sc");

   15. // 设置回调
   16. OH_AVScreenCapture_SetErrorCallback(g_avCapture, OnErrorToStream, nullptr);
   17. OH_AVScreenCapture_SetStateCallback(g_avCapture, OnSurfaceStateChangeToStream, nullptr);

   19. OH_AVScreenCapture_SetCanvasRotation(g_avCapture, true);

   21. // 初始化配置
   22. OH_AVScreenCaptureConfig config_;
   23. SetConfigToStream(config_, videoWidth, videoHeight);
   24. int result = OH_AVScreenCapture_Init(g_avCapture, config_);
   25. if (result != AV_SCREEN_CAPTURE_ERR_OK) {
   26. OH_LOG_INFO(LOG_APP, "ScreenCapture OH_AVScreenCapture_Init failed %{public}d", result);
   27. }
   28. OH_LOG_INFO(LOG_APP, "ScreenCapture OH_AVScreenCapture_Init %{public}d", result);

   30. // ...
   31. }
   ```

   [CAVScreenCaptureToStream.cpp](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/avscreen-capture-screen-record-master/entry/src/main/cpp/CAVScreenCaptureToStream/CAVScreenCaptureToStream.cpp#L278-L363)
5. 通过OH\_AVScreenCapture\_StartScreenCaptureWithSurface()接口开启屏幕录制。

   这里使用Surface模式启动录屏。通过OH\_AVScreenCapture\_StartScreenCaptureWithSurface()方法指定Surface并启动录屏。同时启动封装器。

   ```
   1. result = OH_AVScreenCapture_StartScreenCaptureWithSurface(g_avCapture, sampleInfo_.window);
   2. OH_LOG_INFO(LOG_APP, "OH_VideoEncoder_Start Started 2 %{public}d", result);
   3. if (result != AV_SCREEN_CAPTURE_ERR_OK) {
   4. OH_LOG_INFO(LOG_APP, "ScreenCapture Started failed %{public}d", result);
   5. OH_AVScreenCapture_Release(g_avCapture);
   6. }
   ```

   [CAVScreenCaptureToStream.cpp](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/avscreen-capture-screen-record-master/entry/src/main/cpp/CAVScreenCaptureToStream/CAVScreenCaptureToStream.cpp#L311-L316)
6. 拆分音视频编码器以及封装器子线程。

   启动音视频编码器和封装器，并将音视频编码器及封装器的数据处理子线程分离以进行数据处理。详细处理逻辑请参见示例代码。

   ```
   1. // 开启封装器
   2. int32_t ret = muxer_->Start();
   3. // 开启视频编码器
   4. ret = videoEncoder_->Start();

   6. // ...

   8. // 启动视频输出线程
   9. encOutputThread_ = std::make_unique<std::thread>(&CAVScreenCaptureToStream::EncOutputThread, this);
   10. if (encOutputThread_ == nullptr) {
   11. StartRelease();
   12. return;
   13. }

   15. if (audioEncContext_) {
   16. // 开启音频采集器
   17. audioCapturer_->AudioCapturerStart();

   19. // 开启音频编码器
   20. audioEncoder_->Start();

   22. // ...

   24. // 启动音频输入输出线程
   25. audioEncInputThread_ = std::make_unique<std::thread>(&CAVScreenCaptureToStream::AudioEncInputThread, this);
   26. audioEncOutputThread_ = std::make_unique<std::thread>(&CAVScreenCaptureToStream::AudioEncOutputThread, this);
   27. if (audioEncInputThread_ == nullptr || audioEncOutputThread_ == nullptr) {
   28. StartRelease();
   29. return;
   30. }

   32. // 清空播放缓存队列
   33. if (audioEncContext_ != nullptr) {
   34. audioEncContext_->ClearCache();
   35. }
   36. }
   ```

   [CAVScreenCaptureToStream.cpp](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/avscreen-capture-screen-record-master/entry/src/main/cpp/CAVScreenCaptureToStream/CAVScreenCaptureToStream.cpp#L321-L360)
7. 停止屏幕录制并释放相应资源。

   首先，等待数据写入完成，然后启动子线程以释放音视频编码器及封装器的相关资源。在资源完全释放后，调用OH\_AVScreenCapture\_StopScreenRecording()方法停止屏幕录制，最后释放ScreenCapture实例。

   ```
   1. // 停止屏幕录制
   2. void CAVScreenCaptureToStream::StopScreenCapture() {
   3. int32_t ret = videoEncoder_->NotifyEndOfStream();

   5. // 等待数据写入
   6. std::unique_lock<std::mutex> lock(mutex_);
   7. doneCond_.wait(lock);
   8. // 等待资源释放
   9. if (releaseThread_ && releaseThread_->joinable()) {
   10. releaseThread_->join();
   11. releaseThread_.reset();
   12. }

   14. // ...

   16. // 停止录屏
   17. ret = OH_AVScreenCapture_StopScreenCapture(g_avCapture);
   18. if (ret != AV_SCREEN_CAPTURE_ERR_BASE) {
   19. OH_LOG_ERROR(LOG_APP, "StopScreenCapture OH_AVScreenCapture_StopScreenCapture Result: %{public}d", ret);
   20. } else {
   21. OH_LOG_INFO(LOG_APP, "StopScreenCapture OH_AVScreenCapture_StopScreenCapture");
   22. }
   23. // 释放实例对象
   24. ret = OH_AVScreenCapture_Release(g_avCapture);
   25. if (ret != AV_SCREEN_CAPTURE_ERR_BASE) {
   26. OH_LOG_ERROR(LOG_APP, "StopScreenCapture OH_AVScreenCapture_Release: %{public}d", ret);
   27. } else {
   28. OH_LOG_INFO(LOG_APP, "OH_AVScreenCapture_Release success");
   29. }

   31. // ...
   32. }
   ```

   [CAVScreenCaptureToStream.cpp](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/avscreen-capture-screen-record-master/entry/src/main/cpp/CAVScreenCaptureToStream/CAVScreenCaptureToStream.cpp#L370-L407)

   音视频编码器及封装器资源释放。

   ```
   1. // 释放线程
   2. void CAVScreenCaptureToStream::Release() {
   3. std::lock_guard<std::mutex> lock(mutex_);
   4. isStarted_ = false;
   5. // 视频输出线程
   6. if (encOutputThread_ && encOutputThread_->joinable()) {
   7. encOutputThread_->join();
   8. encOutputThread_.reset();
   9. }
   10. // 音频输入线程
   11. if (audioEncInputThread_ && audioEncInputThread_->joinable()) {
   12. audioEncContext_->inputCond.notify_all();
   13. audioEncInputThread_->join();
   14. audioEncInputThread_.reset();
   15. }
   16. // 音频输出线程
   17. if (audioEncOutputThread_ && audioEncOutputThread_->joinable()) {
   18. audioEncContext_->outputCond.notify_all();
   19. audioEncOutputThread_->join();
   20. audioEncOutputThread_.reset();
   21. }

   23. // 释放封装器
   24. if (muxer_ != nullptr) {
   25. muxer_->Release();
   26. muxer_.reset();
   27. OH_LOG_INFO(LOG_APP, "Muxer release successful");
   28. }
   29. // 释放编码器
   30. if (videoEncoder_ != nullptr) {
   31. videoEncoder_->Stop();
   32. if (sampleInfo_.window != nullptr) {
   33. OH_NativeWindow_DestroyNativeWindow(sampleInfo_.window);
   34. sampleInfo_.window = nullptr;
   35. }
   36. videoEncoder_->Release();
   37. videoEncoder_.reset();
   38. OH_LOG_INFO(LOG_APP, "Video encoder release successful");
   39. }
   40. if (audioEncoder_ != nullptr) {
   41. audioEncoder_->Stop();
   42. audioEncoder_->Release();
   43. audioEncoder_.reset();
   44. OH_LOG_INFO(LOG_APP, "Audio encoder release successful");
   45. }

   47. // 释放资源
   48. if (audioCapturer_ != nullptr) {
   49. audioCapturer_->AudioCapturerRelease();
   50. audioCapturer_.reset();
   51. OH_LOG_INFO(LOG_APP, "Audio Capturer release successful");
   52. }
   53. if (audioEncContext_ != nullptr) {
   54. delete audioEncContext_;
   55. audioEncContext_ = nullptr;
   56. }
   57. if (videoEncContext_ != nullptr) {
   58. delete videoEncContext_;
   59. videoEncContext_ = nullptr;
   60. }
   61. doneCond_.notify_all();
   62. OH_LOG_INFO(LOG_APP, "Release successful");
   63. }
   ```

   [CAVScreenCaptureToStream.cpp](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/avscreen-capture-screen-record-master/entry/src/main/cpp/CAVScreenCaptureToStream/CAVScreenCaptureToStream.cpp#L445-L507)

   最后在ArkTS侧关闭文件。

   ```
   1. async releaseFD() {
   2. if (this.file?.fd != undefined && this.file.fd?.valueOf() > 0) {
   3. // 关闭文件
   4. try {
   5. fs.close(this.file.fd);
   6. } catch (error) {
   7. let err = error as BusinessError;
   8. hilog.error(0x0000, 'testTag', `close fail. code = ${err.code}, message = ${err.message}`);
   9. }
   10. }
   11. }
   ```

   [CAVScreenCaptureToStream.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/avscreen-capture-screen-record-master/entry/src/main/ets/pages/CAVScreenCaptureToStream.ets#L77-L88)

说明

AVScreenCapture在屏幕录制过程中无法动态调整参数。 若要实现动态调整参数，可以通过配置编码器来完成。

## 常见问题

### 如何配置音频内录和音频外录

内录和外录是指在录音设备中进行录音的两种不同方式。内录是使用设备内部的音频输入接口来录制声音，而外录则是通过外部麦克风或其他音频源连接到设备来录制声音。

配置内录外录的代码如下：

其中micCapInfo对应外录（麦克风）配置，innerCapInfo对应内录配置。

```
1. void CAVScreenCaptureToFile::SetConfigAsFile(OH_AVScreenCaptureConfig &config, int32_t videoWidth,
2. int32_t videoHeight) {
3. // 音频配置
4. OH_AudioCaptureInfo micCapInfo = {.audioSampleRate = 48000, .audioChannels = 2, .audioSource = OH_SOURCE_DEFAULT};
5. OH_AudioCaptureInfo innerCapInfo = {.audioSampleRate = 48000, .audioChannels = 2, .audioSource = OH_ALL_PLAYBACK};
6. OH_AudioEncInfo audioEncInfo = {.audioBitrate = 96000, .audioCodecformat = OH_AudioCodecFormat::OH_AAC_LC};
7. OH_AudioInfo audioInfo = {.micCapInfo = micCapInfo, .innerCapInfo = innerCapInfo, .audioEncInfo = audioEncInfo};

9. // 视频配置
10. OH_VideoCaptureInfo videoCapInfo = {
11. .videoFrameWidth = videoWidth, .videoFrameHeight = videoHeight, .videoSource = OH_VIDEO_SOURCE_SURFACE_RGBA};
12. OH_VideoEncInfo videoEncInfo = {
13. .videoCodec = OH_VideoCodecFormat::OH_H264, .videoBitrate = 10000000, .videoFrameRate = 30};
14. OH_VideoInfo videoInfo = {.videoCapInfo = videoCapInfo, .videoEncInfo = videoEncInfo};

16. config = {
17. .captureMode = OH_CAPTURE_HOME_SCREEN,
18. .dataType = OH_ORIGINAL_STREAM,
19. .audioInfo = audioInfo,
20. .videoInfo = videoInfo,
21. .recorderInfo = {},
22. };
23. }
```

[CAVScreenCaptureToFile.cpp](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/avscreen-capture-screen-record-master/entry/src/main/cpp/CAVScreenCaptureToFile/CAVScreenCaptureToFile.cpp#L143-L165)

### 如何减少录制文件的大小

可以通过修改视频压缩标准或者降低屏幕录制的帧率来实现。

具体方法如下：

* 使用H265（HEVC）替代H264（AVC）。H265（HEVC）的压缩效率更高。
* 通过调用OH\_AVScreenCapture\_SetMaxVideoFrameRate()将最高帧率设置为30，以降低录制的帧率。

### 如何单独录制视频或者音频

屏幕录制时，涉及的[OH\_AVScreenCaptureConfig](../harmonyos-references/capi-avscreencapture-oh-avscreencaptureconfig.md)相关配置项包括录制模式（[OH\_CaptureMode](../harmonyos-references/capi-native-avscreen-capture-base-h.md#oh_capturemode) ）、数据格式（[OH\_DataType](../harmonyos-references/capi-native-avscreen-capture-base-h.md#oh_datatype)）、音频参数（[OH\_AudioInfo](../harmonyos-references/capi-avscreencapture-oh-audioinfo.md)）、视频参数（[OH\_VideoInfo](../harmonyos-references/capi-avscreencapture-oh-videoinfo.md)）以及录制文件参数（[OH\_RecorderInfo](../harmonyos-references/capi-avscreencapture-oh-recorderinfo.md)）。

其中包含了音频录制参数与视频录制参数。如果单录音频，只需配置OH\_AudioInfo即可，如果单录视频，只需配置OH\_VideoInfo即可。

## 示例代码

* [基于AVScreenCapture实现录屏功能](https://gitcode.com/harmonyos_samples/avscreen-capture-screen-record)
