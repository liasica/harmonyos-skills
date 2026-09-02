---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/avscreencapture-screen-recording-arkts
title: 基于AVScreenCapture实现屏幕录制（ArkTS）
breadcrumb: 指南 > 媒体 > Media Kit（媒体服务） > 媒体开发指导(ArkTS) > 媒体开发实践 > 基于AVScreenCapture实现屏幕录制（ArkTS）
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:47+08:00
doc_updated_at: 2026-08-24
content_hash: sha256:3753bdfabc00acccd5898509da091bd462812fd6f043e6949a39e2e7db5bfad8
---

## 概述

[AVScreenCapture](media-kit-intro.md#avscreencapture)是系统提供的用于实现屏幕录制功能的核心模块，属于媒体的核心能力之一。本文主要针对ArkTS开发场景，详细讲解使用AVScreenCaptureRecorder模块实现录屏写文件的原理和开发流程；如需更底层的数据控制和更优的性能表现，请参考[《基于 AVScreenCapture 实现屏幕录制（C/C++）》](avscreencapture-screen-recording-c.md)。

| 实现方案 | 优点 | 缺点 | 适用场景 |
| --- | --- | --- | --- |
| **使用AVScreenCaptureRecorder模块录屏写文件（ArkTS）** | - 开发逻辑简单，代码维护成本低，无需具备Native相关知识，开发效率相对较高。  - 内存管理相对安全，无需手动释放资源，GC自动回收。  - 与UI界面无缝联动，可以实时更新界面元素。 | - 功能缺失，仅支持文件输出模式（OH\_CAPTURE\_FILE），无法获取原始数据码流。  - 受JS运行时限制，高负载场景下性能相对较差。  - 实时性不佳，不适用于延迟敏感场景。  - 格式受限，仅支持输出MP4格式。  - CPU占用率高。 | 该方案适用于重视开发交互效率和UI界面交互，同时对实时性要求不高的常规场景，例如在线教育课程录制、简单屏幕录制等文件录制场景。 |

**说明** 

在进行屏幕录制开发前需要申请相应权限：麦克风权限（**ohos.permission.MICROPHONE**）、后台长时任务权限（**ohos.permission.KEEP\_BACKGROUND\_RUNNING**）。其他权限可根据需要申请，例如：若需访问公共目录，则应申请公共目录的读写权限。

开发者如果想要了解音视频编码相关内容，可以参考：[音频编码](audio-encoding.md)和[视频编码](video-encoding.md)。

## 场景描述

HarmonyOS 提供了用于实现录屏功能的ArkTS接口，能够支持屏幕录制及音频数据采集。然而，ArkTS侧的实现方案仅能通过文件形式将数据流转至其他模块进行播放或处理。

本章将通过一个案例介绍如何在ArkTS侧实现录屏存文件。在该案例中，用户点击屏幕录制按钮即可启动屏幕录制，期间可以切换至后台录制桌面或其他应用页面。当用户点击停止按钮或屏幕左上角录屏胶囊中的停止按钮时，屏幕录制将停止。录屏内容将保存至应用沙箱文件中，点击结束录屏后出现的播放按钮，即可播放录制的视频文件。

**案例展示图：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/BQWHb_W9RZ-TL2zXVwbL4w/zh-cn_image_0000002736313697.gif)

## 实现原理

**调用流程图**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/QMhVrXRaTFS6mmu7ljJRSA/zh-cn_image_0000002706674654.png)

当点击录制按钮时，会调用异步方法进行屏幕录制。关键过程如下：

1. 等到异步任务得到调度后，会先获取文件信息，用于保存录屏视频。
2. 接着会通过createAVScreenCaptureRecorder()方法构建出AVScreenCaptureRecorder的实例化对象。
3. 然后为该实例对象绑定状态变化监听函数和异常监听函数。
4. 接着还需要配置屏幕录制参数，然后根据参数配置对实例化对象进行初始化。
5. 初始化完成之后即可调用startRecording()方法开启屏幕录制。

当点击停止按钮时，同样系统会调用异步方法来停止录制。等到异步任务被调度后，将调用stopRecording()方法停止屏幕录制，随后关闭文件fd。

**说明** 

EventLoop事件循环是ArkTS异步编程模型的核心（单线程+任务队列），其在JS/TS的基础上结合了HarmonyOS的UI框架和任务调度特性，主要用于管理代码执行顺序、处理异步操作（如网络请求、定时器、用户交互、I/O）以及更新UI等。

## 开发步骤

1. 获取文件信息。

   首先，通过时间戳和应用沙箱目录拼接出文件路径，然后利用文件管理模块的openSync()接口获取文件信息。后续的录屏文件将存储在该文件中。

   获取沙箱路径。

   ```typescript
   private filesDir = this.getUIContext().getHostContext()?.filesDir;
   ```

   拼接文件路径并获取文件信息。

   ```typescript
   public updateFileFd(filesDir: string) {
     this.fileName = systemDateTime.getTime(true).toString() + '.mp4';
     this.path = filesDir + '/' + this.fileName;
     try {
       this.file = fileIo.openSync(this.path, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
       this.captureConfig.fd = this.file.fd;
     } catch (error) {
       let err = error as BusinessError;
       hilog.error(0x0000, 'testTag', `openSync fail. code = ${err.code}, message = ${err.message}`);
     }
   }
   ```
2. 创建AVScreenCaptureRecorder实例化对象并绑定监听函数。

   通过MediaKit提供的createAVScreenCaptureRecorder()接口构建实例对象，然后使用.on接口为其绑定可选的监听回调函数。在以下示例中，订阅了两个回调事件：stateChange（状态切换事件回调）和error（错误事件回调）。对于同一个回调事件，用户只能订阅一次，若重复订阅，则以最后一次订阅的回调接口为准。已订阅的回调事件还可以通过off接口取消订阅。

   ```typescript
   public async startRecording(filesDir: string) {
     this.updateFileFd(filesDir);

     try {
       this.screenCapture = await media.createAVScreenCaptureRecorder();
     } catch (error) {
       let err = error as BusinessError;
       hilog.error(0x0000, 'testTag', `createAVScreenCaptureRecorder fail. code = ${err.code}, message = ${err.message}`);
     }

     if (this.screenCapture != undefined) {
       hilog.info(0xFF00, CommonConstants.LOG_TAG, 'ScreenCapture has been created successfully.');
     } else {
       hilog.info(0xFF00, CommonConstants.LOG_TAG, 'ScreenCapture creation failed.');
       return;
     }

     this.screenCapture?.on('stateChange', async (infoType: media.AVScreenCaptureStateCode) => {
       switch (infoType) {
         case media.AVScreenCaptureStateCode.SCREENCAPTURE_STATE_STARTED:
           hilog.info(0xFF00, CommonConstants.LOG_TAG, 'Callback received after screen recording starts successfully.');
           break;
         case media.AVScreenCaptureStateCode.SCREENCAPTURE_STATE_CANCELED:
           this.screenCapture?.release();
           this.screenCapture = undefined;
           hilog.info(0xFF00, CommonConstants.LOG_TAG, 'The screen recording function is not allowed.');
           break;
         case media.AVScreenCaptureStateCode.SCREENCAPTURE_STATE_STOPPED_BY_USER:
           this.screenCapture?.release();
           this.screenCapture = undefined;
           AppStorage.setOrCreate('isRecordOne', false);
           AppStorage.setOrCreate('fileNameOne', this.fileName);
           hilog.info(0xFF00, CommonConstants.LOG_TAG,
             'End screen recording via the screen recording capsule, and the underlying recording stops.');
           break;
         case media.AVScreenCaptureStateCode.SCREENCAPTURE_STATE_INTERRUPTED_BY_OTHER:
           hilog.info(0xFF00, CommonConstants.LOG_TAG, 'Screen recording stopped due to other interruptions.');
           break;
         case media.AVScreenCaptureStateCode.SCREENCAPTURE_STATE_STOPPED_BY_CALL:
           hilog.info(0xFF00, CommonConstants.LOG_TAG, 'Screen recording was interrupted by a call.');
           break;
         case media.AVScreenCaptureStateCode.SCREENCAPTURE_STATE_MIC_UNAVAILABLE:
           hilog.info(0xFF00, CommonConstants.LOG_TAG, 'The screen recording microphone is unavailable.');
           break;
         case media.AVScreenCaptureStateCode.SCREENCAPTURE_STATE_MIC_MUTED_BY_USER:
           hilog.info(0xFF00, CommonConstants.LOG_TAG, 'The screen recording microphone has been muted by the user.');
           break;
         case media.AVScreenCaptureStateCode.SCREENCAPTURE_STATE_MIC_UNMUTED_BY_USER:
           hilog.info(0xFF00, CommonConstants.LOG_TAG, 'The screen recording microphone has been unmuted by the user.');
           break;
         case media.AVScreenCaptureStateCode.SCREENCAPTURE_STATE_ENTER_PRIVATE_SCENE:
           hilog.info(0xFF00, CommonConstants.LOG_TAG, 'Screen recording enters a privacy scenario.');
           break;
         case media.AVScreenCaptureStateCode.SCREENCAPTURE_STATE_EXIT_PRIVATE_SCENE:
           hilog.info(0xFF00, CommonConstants.LOG_TAG, 'Screen recording exits the privacy scenario.');
           break;
         case media.AVScreenCaptureStateCode.SCREENCAPTURE_STATE_STOPPED_BY_USER_SWITCHES:
           hilog.info(0xFF00, CommonConstants.LOG_TAG,
             'The user account is switched, and the underlying recording stops.');
           break;
         default:
           break;
       }
     })

     this.screenCapture?.on('error', (err) => {
       hilog.info(0xFF00, CommonConstants.LOG_TAG, 'Handle exception cases.');
     })
   ```
3. 配置录制参数并初始化AVScreenCaptureRecorder对象。

   示例中通过 getDefaultDisplaySync() 方法获取屏幕宽高。开发者也可以自定义屏幕宽高，但需注意，若设置不当，可能会导致录制的视频界面出现黑边。

   ```typescript
   let displayInfo = display.getDefaultDisplaySync();
   ```

   以下配置了屏幕录制参数，除了fd配置外，其余配置均为可选。未配置时，将采用默认值。默认值可参考：[AVScreenCaptureRecordConfig](../harmonyos-references/arkts-apis-media-i.md#avscreencapturerecordconfig12)。

   ```typescript
   private captureConfig: media.AVScreenCaptureRecordConfig = {
     frameWidth: this.displayInfo.width,
     frameHeight: this.displayInfo.height,
     fd: 0,
     videoBitrate: 10000000,
     audioSampleRate: 48000,
     audioChannelCount: 2,
     audioBitrate: 96000,
     displayId: 0,
   };
   ```

   基于上述配置信息初始化screenCapture实例对象。

   ```typescript
   await this.screenCapture?.init(this.captureConfig);
   ```
4. 通过startRecording()接口开启录制。

   startRecording()接口以异步方式启动录屏，启动后录屏不会影响页面操作。

   ```typescript
   await this.screenCapture?.startRecording();
   ```
5. 通过stopRecording()停止录制并关闭文件。

   同样的，stopRecording()接口也是异步接口，示例中首先通过stopRecording()接口停止录制，然后调用release()方法销毁实例，释放资源。

   ```typescript
   public async stopRecording() {
     if (this.screenCapture == undefined) {
       hilog.info(0xFF00, CommonConstants.LOG_TAG, 'ScreenCapture exception.');
       return;
     }

     try {
       await this.screenCapture?.stopRecording();

       await this.screenCapture?.release();

       fileIo.close((this.file as fileIo.File).fd);
     } catch (error) {
       let err = error as BusinessError;
       hilog.error(0x0000, 'testTag', `stop fail. code = ${err.code}, message = ${err.message}`);
     }
   }
   ```

**说明** 

除了通过主动点击按钮调用stopRecording()来停止录屏外，还可以通过点击录屏胶囊中的结束按钮来停止录制。该方案主要依赖于回调函数实现，当用户点击胶囊中的停止按钮时，录屏对象实例screenCapture会触发SCREENCAPTURE\_STATE\_STOPPED\_BY\_USER的回调，通知应用录屏已停止，无需开发者主动调用stopRecording()方法。在C/C++方法中，对应的回调是OH\_SCREEN\_CAPTURE\_STATE\_STOPPED\_BY\_USER。

## 示例代码

* [基于AVScreenCapture实现录屏功能](https://gitcode.com/HarmonyOS_Samples/avscreen-capture-screen-record/tree/master)
