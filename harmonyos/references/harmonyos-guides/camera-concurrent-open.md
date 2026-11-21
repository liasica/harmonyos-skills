---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/camera-concurrent-open
title: 多摄同开(ArkTS)
breadcrumb: 指南 > 媒体 > Camera Kit（相机服务） > 开发相机应用基础能力(ArkTS) > 多摄同开(ArkTS)
category: harmonyos-guides
scraped_at: 2026-11-21T09:12:02+08:00
doc_updated_at: 2026-11-20
content_hash: sha256:8f42e2ba3174979fa4d3003794afe4c7a58210f8ab8fbcbcde1e9fc302554db3
---

从API version 18开始支持多摄同开，即应用同时开启前置/后置相机进行预览和录像（前置/后置相机同时拍照功能待开放）。

**说明** 

由于多摄同开需要前置/后置相机同时运行，所以对于相机功能有较大限制。当前版本仅支持以下七项基础功能，请勿对多摄同开开启的相机进行超出以下七种基础功能范围之外的查询、设置和使能。

1. 闪光灯。
2. 曝光。
3. 变焦。
4. 曝光补偿。
5. 对焦。
6. 防抖。
7. 色彩空间。

## 开发步骤

详细的API说明请参考[Camera](../harmonyos-references/arkts-apis-camera.md)。

Context获取方式请参考：[获取UIAbility的上下文信息](uiability-usage.md#获取uiability的上下文信息)。

1. 需要导入相机框架、媒体库、图片等相关领域依赖。

   ```ts
   import { photoAccessHelper } from '@kit.MediaLibraryKit';
   import { camera } from '@kit.CameraKit';
   import { media } from '@kit.MediaKit';
   import { fileIo } from '@kit.CoreFileKit';
   import { common } from '@kit.AbilityKit';
   import { colorSpaceManager } from '@kit.ArkGraphics2D';
   import { BusinessError } from '@kit.BasicServicesKit';
   ```
2. 通过[getCameraDevice](../harmonyos-references/arkts-apis-camera-cameramanager.md#getcameradevice18)获取对应的前置和后置相机。如果接口返回undefined，基于示例中的配置信息，表示当前设备不支持指定位置（前置/后置）的默认类型相机，无法实现多摄同开功能。

   ```typescript
   getSupportedCamerasForConcurrentFn(cameraManager: camera.CameraManager) {
     let cameras = cameraManager.getSupportedCameras();

     // 如果相机数量少于2，说明只存在单侧相机，返回。
     if (cameras.length < 2) {
       return;
     }

     // 获取逻辑后置和逻辑前置。
     let curCameraDeviceBack = cameraManager.getCameraDevice(camera.CameraPosition.CAMERA_POSITION_BACK,
       camera.CameraType.CAMERA_TYPE_DEFAULT);
     let curCameraDeviceFront = cameraManager.getCameraDevice(camera.CameraPosition.CAMERA_POSITION_FRONT,
       camera.CameraType.CAMERA_TYPE_DEFAULT);
   }
   ```
3. 获取对应的并发能力集。通过[getCameraConcurrentInfos](../harmonyos-references/arkts-apis-camera-cameramanager.md#getcameraconcurrentinfos18)获取相机的输出并发能力信息数组[CameraConcurrentInfo](../harmonyos-references/arkts-apis-camera-i.md#cameraconcurrentinfo18)，数组内部包含相机在对应并发模式下支持的模式和输出能力，**在多摄同开场景下设置的模式和输出能力必须在并发能力集的范围之内**。若[getCameraConcurrentInfos](../harmonyos-references/arkts-apis-camera-cameramanager.md#getcameraconcurrentinfos18)接口返回空数组，则表明当前设备不支持并发功能。

   ```typescript
   getSupportedOutputCapabilityForConcurrentFn(cameraManager: camera.CameraManager,
     curCameraDeviceFront: camera.CameraDevice,
     curCameraDeviceBack: camera.CameraDevice): camera.CameraOutputCapability | undefined {
     // 检查当前相机是否支持拍照模式，获取原始能力集。
     let sceneModes = cameraManager.getSupportedSceneModes(curCameraDeviceFront);
     if (sceneModes === undefined) {
       return undefined;
     }
     let isSupported: boolean = sceneModes.includes(camera.SceneMode.NORMAL_PHOTO);
     if (!isSupported) {
       return undefined;
     }
     let cameraOutputCapability = cameraManager.getSupportedOutputCapability(curCameraDeviceFront,
       camera.SceneMode.NORMAL_PHOTO);

     let deviceArray: camera.CameraDevice[] = [curCameraDeviceFront, curCameraDeviceBack];

     // 获取并发能力集。
     let concurrentInfo: camera.CameraConcurrentInfo[] = cameraManager.getCameraConcurrentInfos(deviceArray);

     if (concurrentInfo.length === 0) {
       return undefined;
     }

     // 用并发能力集替换原始能力集。
     for (let i = 0; i < concurrentInfo.length; i++) {
       if (concurrentInfo[i].device.cameraPosition == camera.CameraPosition.CAMERA_POSITION_FRONT) {
         cameraOutputCapability = concurrentInfo[i].outputCapabilities[0];
         break;
       }
     }
     return cameraOutputCapability;
   }
   ```
4. 确定预览输出流。

   ```typescript
   getPreviewOutputForConcurrentFn(cameraManager: camera.CameraManager,
     cameraOutputCapability: camera.CameraOutputCapability, surfaceId: string): camera.PreviewOutput | undefined {
     // 此处创建预览输出流以format：1003，size：1920*1080的previewProfile为例。
     let previewProfileObj: camera.Profile = {
       format: 1003,
       size: {
         width: 1920,
         height: 1080
       }
     };
     // 查询对应previewProfile是否存在，对应的previewProfile必须在getCameraConcurrentInfos获取到的并发能力信息数组范围内。
     let previewProfiles = cameraOutputCapability.previewProfiles;
     if (previewProfiles.length < 1) {
       return undefined;
     }
     let index = previewProfiles.findIndex((previewProfile: camera.Profile) => {
       return previewProfile.size.width === previewProfileObj.size.width &&
         previewProfile.size.height === previewProfileObj.size.height &&
         previewProfile.format === previewProfileObj.format;
     });
     if (index === -1) {
       return undefined;
     }

     // 创建previewOutput对象。
     let previewOutput = cameraManager.createPreviewOutput(previewProfileObj, surfaceId);
     if (previewOutput === undefined) {
       return undefined;
     }
     return previewOutput;
   }
   ```
5. 确定拍照输出流。

   ```typescript
   getPhotoOutputForConcurrentFn(cameraManager: camera.CameraManager,
     cameraOutputCapability: camera.CameraOutputCapability): camera.PhotoOutput | undefined {
     // 此处创建拍照输出流以format：2000，size：1920*1080的photoProfile为例。
     let photoProfileObj: camera.Profile = {
       format: 2000,
       size: {
         width: 1920,
         height: 1080
       }
     };
     // 查询对应photoProfile是否存在，对应的photoProfile必须在getCameraConcurrentInfos获取到的并发能力信息数组范围内。
     let photoProfiles = cameraOutputCapability.photoProfiles;
     if (photoProfiles.length < 1) {
       return undefined;
     }
     let index = photoProfiles.findIndex((photoProfile: camera.Profile) => {
       return photoProfile.size.width === photoProfileObj.size.width &&
         photoProfile.size.height === photoProfileObj.size.height &&
         photoProfile.format === photoProfileObj.format;
     });
     if (index === -1) {
       return undefined;
     }
     let photoOutput = cameraManager.createPhotoOutput(photoProfileObj);
     if (photoOutput === undefined) {
       return undefined;
     }
     return photoOutput;
   }
   ```
6. 确定录像输出流。

   ```typescript
   async createAVRecorderForConcurrent(): Promise<media.AVRecorder | undefined> {
     let avRecorder: media.AVRecorder | undefined = undefined;
     try {
       avRecorder = await media.createAVRecorder();
     } catch (error) {
       console.error(`createAVRecorder error`)
     }
     return avRecorder;
   }

   initFdForConcurrent(context: common.Context): number {
     let filesDir = context.filesDir;
     let filePath = filesDir + `/${Date.now()}.mp4`;
     AppStorage.setOrCreate<string>('filePath', filePath);
     try {
       let file: fileIo.File = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
       return file.fd;
     } catch (error) {
       let err = error as BusinessError;
       console.error(`openSync failed, err code: ${err.code}.`);
       return -1;
     }
   }

   async prepareAVRecorderForConcurrent(videoProfileObj: camera.VideoProfile, curCameraDevice: camera.CameraDevice,
     avRecorder: media.AVRecorder, context: common.Context): Promise<void> {
     let fd = this.initFdForConcurrent(context);
     let videoConfig: media.AVRecorderConfig = {
       audioSourceType: media.AudioSourceType.AUDIO_SOURCE_TYPE_MIC,
       videoSourceType: media.VideoSourceType.VIDEO_SOURCE_TYPE_SURFACE_YUV,
       profile: {
         audioBitrate: 48000,
         audioChannels: 2,
         audioCodec: media.CodecMimeType.AUDIO_AAC,
         audioSampleRate: 48000,
         fileFormat: media.ContainerFormatType.CFT_MPEG_4,
         videoBitrate: 512000,
         videoCodec: media.CodecMimeType.VIDEO_AVC,
         videoFrameWidth: videoProfileObj.size.width,
         videoFrameHeight: videoProfileObj.size.height,
         videoFrameRate: videoProfileObj.frameRateRange.min
       },
       url: `fd://${fd.toString()}`,
       rotation: curCameraDevice?.cameraOrientation
     };
     await avRecorder?.prepare(videoConfig).catch((err: BusinessError): void => {
       console.error(`prepareAVRecorder prepare err code: ${err.code}.`);
     });
   }

   async getVideoOutputFn(cameraManager: camera.CameraManager, cameraOutputCapability: camera.CameraOutputCapability,
     concurrentInfo: camera.CameraConcurrentInfo[], curCameraDeviceFront: camera.CameraDevice,
     context: common.Context): Promise<camera.VideoOutput | undefined> {
     // 此处创建录像输出流以format：1003，size：1920*1080的录像配置项为例。
     // 对应的录像配置项必须在getCameraConcurrentInfos获取到的并发能力信息数组范围内。
     let videoProfileObj: camera.VideoProfile = {
       format: 1003,
       size: {
         width: 1920,
         height: 1080
       },
       frameRateRange: {
         min: 30,
         max: 60
       }
     };

     // 替换相应能力集。
     for (let i = 0; i < concurrentInfo.length; i++) {
       if (concurrentInfo[i].device.cameraPosition == camera.CameraPosition.CAMERA_POSITION_FRONT) {
         cameraOutputCapability = concurrentInfo[i].outputCapabilities[1];
         break;
       }
     }
     let videoProfiles = cameraOutputCapability.videoProfiles;
     if (videoProfiles.length < 1) {
       return undefined;
     }
     let index = videoProfiles.findIndex((videoProfile: camera.VideoProfile) => {
       return videoProfile.size.width === videoProfileObj.size.width &&
         videoProfile.size.height === videoProfileObj.size.height &&
         videoProfile.format === videoProfileObj.format &&
         videoProfile.frameRateRange.min <= 60 &&
         videoProfile.frameRateRange.max <= 60;
     });
     if (index === -1) {
       return undefined;
     }
     videoProfileObj = videoProfiles[index];
     let avRecorder = await this.createAVRecorderForConcurrent();
     if (avRecorder === undefined) {
       return undefined;
     }
     // 保存avRecorder，供停止录制和释放时使用。
     this.avRecorder = avRecorder;
     await this.prepareAVRecorderForConcurrent(videoProfileObj, curCameraDeviceFront, avRecorder, context);
     let videoSurfaceId = await avRecorder.getInputSurface();
     let videoOutput = cameraManager.createVideoOutput(videoProfileObj, videoSurfaceId);
     if (videoOutput === undefined) {
       return undefined;
     }
     return videoOutput;
   }
   ```
7. 打开相机。通过[open](../harmonyos-references/arkts-apis-camera-camerainput.md#open18)以多摄同开状态打开指定相机。在使用[open](../harmonyos-references/arkts-apis-camera-camerainput.md#open18)接口前，请先查询接口是否支持并发能力集，并优先调用[getCameraConcurrentInfos](../harmonyos-references/arkts-apis-camera-cameramanager.md#getcameraconcurrentinfos18)方法，获取多摄同开状态下的相机并发能力集。请勿在未查询并发能力集的情况下使用[open](../harmonyos-references/arkts-apis-camera-camerainput.md#open18)，否则会导致打开相机失败。

   ```typescript
   async openCameraForConcurrent(cameraManager: camera.CameraManager, cameraDevice: camera.CameraDevice) {
     let cameraInput: camera.CameraInput | undefined = undefined;
     try {
       cameraInput = cameraManager.createCameraInput(cameraDevice);
       console.info(`createCameraInputFn success`);
     } catch (error) {
       console.error(`createCameraInputFn failed`);
     }
     if (cameraInput === undefined) {
       return;
     }
     try {
       // 当前版本支持camera.CameraConcurrentType.CAMERA_LIMITED_CAPABILITY模式并发打开相机。
       await cameraInput.open(camera.CameraConcurrentType.CAMERA_LIMITED_CAPABILITY);
     } catch (error) {
       let err = error as BusinessError;
       console.error(`createCameraInput failed, err code: ${err.code}.`);
     }
   }
   ```
8. 会话流程。

   ```typescript
   // 监听捕获会话错误变化。
   onSessionErrorChangeForConcurrent(session: camera.PhotoSession | camera.VideoSession): void {
     try {
       session.on('error', (captureSessionError: BusinessError): void => {
       });
     } catch (error) {
       let err = error as BusinessError;
       console.error(`onSessionErrorChangeForConcurrent err code: ${err.code}`);
     }
   }

   // 监听拍照事件。
   photoOutputCallBackForConcurrent(photoOutput: camera.PhotoOutput): void {
     try {

       // 监听拍照开始。
       photoOutput.on('captureStartWithInfo', (err: BusinessError, captureStartInfo: camera.CaptureStartInfo): void => {
         if (err) {
           console.error(`captureStartWithInfo failed, err code:${err.code}`);
           return;
         }
         console.info(`capture is called, captureId: ${captureStartInfo.captureId}.`);
       });

       // 监听拍照帧输出捕获。
       photoOutput.on('frameShutter', (err: BusinessError, frameShutterInfo: camera.FrameShutterInfo): void => {
         if (err) {
           console.error(`frameShutter failed, err code:${err.code}`);
           return;
         }
         console.info(`frameShutter is called, captureId: ${frameShutterInfo.captureId}.`);
       });

       // 监听拍照结束。
       photoOutput.on('captureEnd', (err: BusinessError, captureEndInfo: camera.CaptureEndInfo): void => {
         if (err) {
           console.error(`captureEnd failed, err code:${err.code}.`);
           return;
         }
         console.info(`captureEnd is called, captureId: ${captureEndInfo.captureId}.`);
       });

       // 监听拍照异常。
       photoOutput.on('error', (err: BusinessError): void => {
         console.error(`photoOutput error, err code: ${err.code}.`);
       });
       photoOutput.on('photoAssetAvailable', (err: BusinessError, photoAsset: photoAccessHelper.PhotoAsset) => {
         if (err) {
           console.error(`photoAssetAvailable error: ${err.code}.`);
           return;
         }
         console.info(`photoOutputCallBack photoAssetAvailable`);
         // 开发者可通过photoAsset调用媒体库相关接口，自定义处理图片。
         // 调用媒体库落盘接口保存一阶段图，二阶段图就绪后媒体库会主动帮应用替换落盘图片。
         let accessHelper: photoAccessHelper.PhotoAccessHelper =
           photoAccessHelper.getPhotoAccessHelper(this.context);
         this.mediaLibSavePhoto(photoAsset, accessHelper);
       });
     } catch (error) {
       let err = error as BusinessError;
       console.error(`photoOutputCallBackForConcurrent failed, err code: ${err.code}`);
     }
   }

   // 会话流程。
   async sessionFlowForConcurrentFn(cameraManager: camera.CameraManager, cameraInput: camera.CameraInput,
     previewOutput: camera.PreviewOutput, photoOutput: camera.PhotoOutput | undefined,
     videoOutput: camera.VideoOutput | undefined, curSceneMode: camera.SceneMode): Promise<void> {
     let session: camera.PhotoSession | camera.VideoSession | undefined = undefined;
     try {
       // 创建CaptureSession实例。
       if (curSceneMode === camera.SceneMode.NORMAL_PHOTO) {
         session = cameraManager.createSession(curSceneMode) as camera.PhotoSession;
       } else if (curSceneMode === camera.SceneMode.NORMAL_VIDEO) {
         session = cameraManager.createSession(curSceneMode) as camera.VideoSession;
       }
       if (session === undefined) {
         return;
       }
       this.onSessionErrorChangeForConcurrent(session);

       // 开始配置会话。
       session.beginConfig();

       // 向会话中添加相机输入流。
       session.addInput(cameraInput);

       // 向会话中添加预览输出流。
       session.addOutput(previewOutput);

       if (curSceneMode === camera.SceneMode.NORMAL_PHOTO) {
         if (photoOutput === undefined) {
           return;
         }

         // 拍照监听事件。
         this.photoOutputCallBackForConcurrent(photoOutput);

         // 向会话中添加拍照输出流。
         session.addOutput(photoOutput);
       } else if (curSceneMode === camera.SceneMode.NORMAL_VIDEO) {
         if (videoOutput === undefined) {
           return;
         }
         // 向会话中添加录像输出流。
         session.addOutput(videoOutput);
       }
       // 提交配置信息。
       await session.commitConfig();
       // 启动会话。
       await session.start();
     } catch (error) {
       let err = error as BusinessError;
       console.error(`sessionFlowForConcurrentFn fail, err code: ${err.code}.`);
     }
   }
   ```
9. 拍照，通过步骤8中配置的photoOutput使用前置或后置相机进行拍照，多摄同开状态下不支持前后相机同时拍照。

   ```typescript
   async takePicture(photoOutput: camera.PhotoOutput): Promise<void> {
     if (photoOutput === undefined || photoOutput === null) {
       console.error(`photoOutput is undefined or null`);
       return;
     }
     try {
       await photoOutput.capture();
     } catch (error) {
       let err = error as BusinessError;
       console.error(`capture failed, err code: ${err.code}.`);
     }
   }
   ```
10. 录制。

    ```typescript
    // 启动录制。
    async startVideoForConcurrent(videoOutput: camera.VideoOutput, avRecorder: media.AVRecorder): Promise<void> {
      try {
        await videoOutput?.start();
        await avRecorder?.start();
      } catch (error) {
        let err = error as BusinessError;
        console.error(`startVideo failed, err code: ${err.code}.`);
      }
    }

    // 停止录制。
    async stopVideoForConcurrent(videoOutput: camera.VideoOutput, avRecorder: media.AVRecorder): Promise<void> {
      try {
        if (avRecorder) {
          await avRecorder.stop();
        }
        if (videoOutput) {
          await videoOutput.stop();
        }
      } catch (error) {
        let err = error as BusinessError;
        console.error(`stopVideo failed, err code: ${err.code}.`);
      }
    }
    ```
11. 在多摄同开状态下，前/后置相机可配置的能力示例如下（当前版本仅支持本文开头部分所示的七项基础功能）。

    ```typescript
    // 闪光灯。
    hasFlashFn(flashMode: camera.FlashMode): void {
      try {
        // 检测是否有闪光灯。
        let hasFlash = this.session?.hasFlash();
        Logger.debug(TAG, `hasFlash success, hasFlash: ${hasFlash}`);
        // 检测闪光灯模式是否支持。
        let isFlashModeSupported = this.session?.isFlashModeSupported(flashMode);
        Logger.debug(TAG, `isFlashModeSupported success, isFlashModeSupported: ${isFlashModeSupported}`);
        // 设置闪光灯模式。
        if (isFlashModeSupported) {
          this.session?.setFlashMode(flashMode);
        }
      } catch (error) {
        console.error(`hasFlashFn failed, err: ${error.code}`);
      }
    }
    ```

    ```typescript
    // 曝光。
    setExposureModeForConcurrentFn(exposureMode: camera.ExposureMode,
      session: camera.PhotoSession | camera.VideoSession | undefined = undefined): void {
      try {
        // 检测曝光模式是否支持。
        let isExposureSupported = session?.isExposureModeSupported(exposureMode);
        // 设置曝光模式。
        if (isExposureSupported) {
          session?.setExposureMode(exposureMode);
        }
      } catch (error) {
        let err = error as BusinessError;
        console.error(`setExposureModeForConcurrentFn failed, err code: ${err.code}.`);
      }
    }
    ```

    ```typescript
    // 变焦。
    setZoomRatioFn(zoomRatio: number): void {
      Logger.info(TAG, `setZoomRatioFn value ${zoomRatio}`);
      // 获取支持的变焦范围。
      try {
        let zoomRatioRange = this.getZoomRatioRange();
        Logger.info(TAG, `getZoomRatioRange success: ${JSON.stringify(zoomRatioRange)}`);
      } catch (error) {
        let err = error as BusinessError;
        Logger.error(TAG, `getZoomRatioRange fail: ${err.code}`);
      }

      try {
        this.session?.setZoomRatio(zoomRatio);
        Logger.info(TAG, 'setZoomRatioFn success');
      } catch (error) {
        let err = error as BusinessError;
        Logger.error(TAG, `setZoomRatioFn fail: ${err.code}`);
      }
    }
    ```

    ```typescript
    // 曝光补偿。
    setExposureBiasFn(exposureBias: number,
      session: camera.PhotoSession | camera.VideoSession | undefined = undefined): void {
      // 查询曝光补偿范围。
      let biasRangeArray: number[] | undefined = [];
      try {
        biasRangeArray = session?.getExposureBiasRange();
        if (biasRangeArray == undefined || biasRangeArray.length !== 2 ||
          exposureBias < biasRangeArray[0] || exposureBias > biasRangeArray[1]) {
          console.error(`invalid exposureBias.`);
          return;
        }
        // 设置曝光补偿。
        session?.setExposureBias(exposureBias);
      } catch (error) {
        let err = error as BusinessError;
        console.error(`setExposureBiasFn failed, err code: ${err.code}.`);
      }
    }
    ```

    ```typescript
    // 对焦模式。
    setFocusMode(focusMode: camera.FocusMode,
      session: camera.PhotoSession | camera.VideoSession | undefined = undefined): void {
      try {
        // 检测对焦模式是否支持。
        let isSupported = session?.isFocusModeSupported(focusMode);
        // 设置对焦模式。
        if (!isSupported) {
          return;
        }
        session?.setFocusMode(focusMode);
      } catch (error) {
        let err = error as BusinessError;
        console.error(`setFocusMode failed, err code: ${err.code}`);
      }
    }
    ```

    ```typescript
    // 设置防抖。
    setStabilizationFn(session: camera.VideoSession, stabilizationMode: camera.VideoStabilizationMode) {
      try {
        session.setVideoStabilizationMode(stabilizationMode);
      } catch (error) {
        let err = error as BusinessError;
        console.error(`setVideoStabilizationMode failed, err code: ${err.code}`);
      }
    }
    ```

    ```typescript
    // 设置色彩空间。
    setColorSpaceFn(session: camera.PhotoSession | camera.VideoSession, color: colorSpaceManager.ColorSpace) {
      try {
        session.setColorSpace(color);
      } catch (error) {
        let err = error as BusinessError;
        console.error(`setColorspace failed, err code: ${err.code}`);
      }
    }
    ```
