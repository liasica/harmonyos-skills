---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/camera-recording
title: 录像(ArkTS)
breadcrumb: 指南 > 媒体 > Camera Kit（相机服务） > 开发相机应用基础能力(ArkTS) > 录像(ArkTS)
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:44+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:0a092f63713d3f1c9ad6db024b528a4a211f8ace68e8bc78f3bca70480df0bbf
---

在开发相机应用时，需要先[申请相关权限](camera-preparation.md)。

相机应用可通过调用和控制相机设备，完成预览、拍照和录像等基础操作。

录像也是相机应用的最重要功能之一，录像是循环帧的捕获。对于录像的自定义配置，开发者可以参考[拍照](camera-shooting.md)中的步骤4，设置分辨率、闪光灯、焦距、照片质量及旋转角度等信息。

## 开发步骤

详细的API说明请参考[@ohos.multimedia.camera (相机管理)](../harmonyos-references/arkts-apis-camera.md)。

1. 导入media模块。

   创建录像输出流的SurfaceId以及录像输出的数据，都需要用到系统提供的media接口[@ohos.multimedia.media (媒体服务)](../harmonyos-references/arkts-apis-media.md)能力，导入media接口的方法如下。

   ```ts
   import { BusinessError } from '@kit.BasicServicesKit';
   import { camera } from '@kit.CameraKit';
   import { media } from '@kit.MediaKit';
   ```
2. 创建Surface。

   系统提供的media接口可以创建一个录像[AVRecorder](../harmonyos-references/arkts-apis-media-avrecorder.md)实例，通过该实例的[getInputSurface](../harmonyos-references/arkts-apis-media-avrecorder.md#getinputsurface9)方法获取SurfaceId，与录像输出流做关联，处理录像输出流输出的数据。

   ```typescript
   this.avRecorder = await this.createAVRecorder();
   if (this.avRecorder === undefined) {
     Logger.error(TAG, 'Failed to create the avRecorder.');
     return;
   }
   await this.prepareAVRecorder();
   let videoSurfaceId = await this.avRecorder.getInputSurface();
   ```
3. 创建录像输出流。

   通过[CameraOutputCapability](../harmonyos-references/arkts-apis-camera-i.md#cameraoutputcapability)中的videoProfiles属性，可获取当前设备支持的录像输出流。然后，定义创建录像的参数，通过[createVideoOutput](../harmonyos-references/arkts-apis-camera-cameramanager.md#createvideooutput)方法创建录像输出流。

   **说明** 

   1.预览流与录像输出流的分辨率的宽高比要保持一致，如示例代码中宽高比为640:480 = 4:3，则需要预览流中的分辨率的宽高比也为4:3，如分辨率选择640:480，或960:720，或1440:1080，以此类推。

   2.在设置预览输出流的分辨率宽高前，需要先通过[AVRecorderProfile](../harmonyos-references/arkts-apis-media-i.md#avrecorderprofile9)查询视频帧支持可配置的宽高范围。

   3.获取录像旋转角度的方法：通过[VideoOutput](../harmonyos-references/arkts-apis-camera-videooutput.md)中的[getVideoRotation](../harmonyos-references/arkts-apis-camera-videooutput.md#getvideorotation12)方法获取rotation实际的值。

   4.录像输出流帧率通过[CameraOutputCapability](../harmonyos-references/arkts-apis-camera-i.md#cameraoutputcapability)中的videoProfiles属性，选择[VideoProfile](../harmonyos-references/arkts-apis-camera-i.md#videoprofile)中[frameRateRange](../harmonyos-references/arkts-apis-camera-i.md#frameraterange)满足实际业务需求的录像输出流videoProfile。

   ```typescript
   createVideoOutputFn(cameraManager: camera.CameraManager, videoProfileObj: camera.VideoProfile,
     surfaceId: string): camera.VideoOutput | undefined {
     let videoOutput: camera.VideoOutput | undefined = undefined;
     try {
       videoOutput = cameraManager.createVideoOutput(videoProfileObj, surfaceId);
       Logger.info(TAG, `createVideoOutputFn success: ${videoOutput}`);
     } catch (error) {
       let err = error as BusinessError;
       Logger.error(TAG, `createVideoOutputFn failed: ${err.code}`);
     }
     return videoOutput;
   }
   ```
4. 开始录像。

   **说明** 

   * 在设置预览流帧率时，需要先通过[getActiveFrameRate](../harmonyos-references/arkts-apis-camera-previewoutput.md#getactiveframerate12)查询当前录像流的帧率。
   * 当录像流已设置过范围帧率时，预览流帧率必须设置与其相同的范围帧率。
   * 当录像流已设置过固定帧率时，预览流帧率要设置成录像帧率的约数，且必须也为固定帧率。
   * 部分设备前置镜头录像分辨率若选择3280\*2160，录像模式下可能会出现视频倒置的情况，建议在[commitConfig](../harmonyos-references/arkts-apis-camera-session.md#commitconfig11)后设置视频防抖[setVideoStabilizationMode](../harmonyos-references/arkts-apis-camera-stabilization.md#setvideostabilizationmode11)，避免该问题发生。

   先通过videoOutput的[start](../harmonyos-references/arkts-apis-camera-videooutput.md#start-1)方法启动录像输出流，再通过avRecorder的[start](../harmonyos-references/arkts-apis-media-avrecorder.md#start9)方法开始录像。

   ```typescript
   async startVideo(): Promise<void> {
     Logger.info(TAG, 'startVideo is called');
     try {
       await this.videoOutput?.start();
       await this.avRecorder?.start();
       this.isRecording = true;
     } catch (error) {
       let err = error as BusinessError;
       Logger.error(TAG, `startVideo err: ${err.code}`);
     }
     Logger.info(TAG, 'startVideo End of call');
   }
   ```
5. 停止录像。

   先通过avRecorder的[stop](../harmonyos-references/arkts-apis-media-avrecorder.md#stop9-1)方法停止录像，再通过videoOutput的[stop](../harmonyos-references/arkts-apis-camera-videooutput.md#stop-1)方法停止录像输出流。

   ```typescript
   async stopVideo(): Promise<void> {
     Logger.info(TAG, 'stopVideo is called');
     if (!this.isRecording) {
       Logger.info(TAG, 'not in recording');
       return;
     }
     try {
       if (this.avRecorder) {
         await this.avRecorder.stop();
       }
       if (this.videoOutput) {
         await this.videoOutput.stop();
       }
       this.isRecording = false;
     } catch (error) {
       let err = error as BusinessError;
       Logger.error(TAG, `stopVideo err: ${err.code}`);
     }
     Logger.info(TAG, 'stopVideo End of call');
   }
   ```

## 状态监听

在相机应用开发过程中，可以随时监听录像输出流状态，包括录像开始、录像结束、录像流输出的错误。

* 通过注册固定的frameStart回调函数获取监听录像开始结果，videoOutput创建成功时即可监听，录像第一次曝光时触发，有该事件返回结果则认为录像开始。

  ```typescript
  videoOutput.on('frameStart', (err: BusinessError) => {
    if (err !== undefined && err.code !== 0) {
      return;
    }
    console.info('Video frame started');
  });
  ```
* 通过注册固定的frameEnd回调函数获取监听录像结束结果，videoOutput创建成功时即可监听，录像完成最后一帧时触发，有该事件返回结果则认为录像流已结束。

  ```typescript
  videoOutput.on('frameEnd', (err: BusinessError) => {
    if (err !== undefined && err.code !== 0) {
      return;
    }
    console.info('Video frame ended');
  });
  ```
* 通过注册固定的error回调函数获取监听录像输出错误结果，callback返回预览输出接口使用错误时对应的错误码，错误码类型参见[CameraErrorCode](../harmonyos-references/arkts-apis-camera-e.md#cameraerrorcode)。

  ```typescript
  videoOutput.on('error', (error: BusinessError) => {
    console.error(`Video output error code: ${error.code}`);
  });
  ```

## 示例代码

* [基于CameraKit通过AVRecorder录像](https://gitcode.com/HarmonyOS_Samples/camera-kit-avrecorder)
