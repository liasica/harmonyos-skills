---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/camera-concurrent-open
title: 多摄同开(ArkTS)
breadcrumb: 指南 > 媒体 > Camera Kit（相机服务） > 开发相机应用基础能力(ArkTS) > 多摄同开(ArkTS)
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:45+08:00
doc_updated_at: 2026-07-21
content_hash: sha256:da732d6a2d0c9d68a3c5b74c3ac61fc72f2d16ddaf6d5ee757f5539c7d810891
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
   import { BusinessError } from '@kit.BasicServicesKit';
   ```
2. 通过[getCameraDevice](../harmonyos-references/arkts-apis-camera-cameramanager.md#getcameradevice18)获取对应的前置和后置相机。如果接口返回undefined，基于示例中的配置信息，表示当前设备不支持指定位置（前置/后置）的默认类型相机，无法实现多摄同开功能。

   ```ts
   function getSupportedCamerasFn(cameraManager: camera.CameraManager)
   {
     let cameras = cameraManager.getSupportedCameras();

     // 如果相机数量少于2，说明只存在单侧相机，返回。
     if (cameras.length < 2) {
      return;
     }

     // 获取逻辑后置和逻辑前置。
     let curCameraDeviceBack = cameraManager.getCameraDevice(camera.CameraPosition.CAMERA_POSITION_BACK, camera.CameraType.CAMERA_TYPE_DEFAULT);
     let curCameraDeviceFront = cameraManager.getCameraDevice(camera.CameraPosition.CAMERA_POSITION_FRONT, camera.CameraType.CAMERA_TYPE_DEFAULT);
   }
   ```
3. 获取对应的并发能力集。通过[getCameraConcurrentInfos](../harmonyos-references/arkts-apis-camera-cameramanager.md#getcameraconcurrentinfos18)获取相机的输出并发能力信息数组[CameraConcurrentInfo](../harmonyos-references/arkts-apis-camera-i.md#cameraconcurrentinfo18)，数组内部包含相机在对应并发模式下支持的模式和输出能力，**在多摄同开场景下设置的模式和输出能力必须在并发能力集的范围之内**。若[getCameraConcurrentInfos](../harmonyos-references/arkts-apis-camera-cameramanager.md#getcameraconcurrentinfos18)接口返回空数组，则表明当前设备不支持并发功能。

   ```ts
   function getSupportedOutputCapabilityFn(cameraManager: camera.CameraManager, curCameraDeviceFront: camera.CameraDevice, curCameraDeviceBack: camera.CameraDevice)
   {
     // 检查当前相机是否支持拍照模式，获取原始能力集。
     let sceneModes = cameraManager.getSupportedSceneModes(curCameraDeviceFront);
     if (sceneModes === undefined) {
       return;
     }
     let isSupported: boolean = sceneModes.includes(camera.SceneMode.NORMAL_PHOTO);
     if (!isSupported) {
       return;
     }
     let cameraOutputCapability = cameraManager.getSupportedOutputCapability(curCameraDeviceFront, camera.SceneMode.NORMAL_PHOTO);

     let deviceArray: Array<camera.CameraDevice> = [curCameraDeviceFront, curCameraDeviceBack];

     // 获取并发能力集。
     let concurrentInfo: Array<camera.CameraConcurrentInfo> = cameraManager.getCameraConcurrentInfos(deviceArray);

     if (concurrentInfo.length === 0) {
      return;
     }

     // 用并发能力集替换原始能力集。
     for (let i = 0; i < concurrentInfo.length; i++) {
       if (concurrentInfo[i].device.cameraPosition == camera.CameraPosition.CAMERA_POSITION_FRONT) {
         cameraOutputCapability = concurrentInfo[i].outputCapabilities[0];
         break;
       }
     }
   }
   ```
4. 确定预览输出流。

   ```ts
   function getPreviewOutputFn(cameraManager: camera.CameraManager, cameraOutputCapability: camera.CameraOutputCapability, surfaceId: string)
   {
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
       return;
     }
     let index = previewProfiles.findIndex((previewProfile: camera.Profile) => {
       return previewProfile.size.width === previewProfileObj.size.width &&
       previewProfile.size.height === previewProfileObj.size.height &&
       previewProfile.format === previewProfileObj.format;
     });
     if (index === -1) {
       return;
     }

     // 创建previewOutput输出对象。
     let previewOutput = cameraManager.createPreviewOutput(previewProfileObj, surfaceId);
     if (previewOutput === undefined) {
       return;
     }
   }
   ```
5. 确定拍照输出流。

   ```ts
   function getPhotoOutputFn(cameraManager: camera.CameraManager, cameraOutputCapability: camera.CameraOutputCapability)
   {
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
      return;
     }
     let index = photoProfiles.findIndex((photoProfile: camera.Profile) => {
       return photoProfile.size.width === photoProfileObj.size.width &&
       photoProfile.size.height === photoProfileObj.size.height &&
       photoProfile.format === photoProfileObj.format;
     });
     if (index === -1) {
       return;
     }
     let photoOutput = cameraManager.createPhotoOutput(photoProfileObj);
     if (photoOutput === undefined) {
       return;
     }
   }
   ```
6. 确定录像输出流。

   ```ts
   async function createAVRecorder(): Promise<media.AVRecorder | undefined> {
     let avRecorder: media.AVRecorder | undefined = undefined;
     try {
       avRecorder = await media.createAVRecorder();
     } catch (error) {
     console.error('createAVRecorder error')
     }
     return avRecorder;
   }

   function initFd(context: common.Context): number {
     let filesDir = context.filesDir;
     let filePath = filesDir + `/${Date.now()}.mp4`;
     AppStorage.setOrCreate<string>('filePath', filePath);
     let file: fileIo.File = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
     return file.fd;
   }

   async function prepareAVRecorder(videoProfileObj: camera.VideoProfile, curCameraDevice: camera.CameraDevice, avRecorder: media.AVRecorder, context: common.Context): Promise<void> {
     let fd = initFd(context);
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
       console.error(`prepareAVRecorder prepare err`);
     });
   }

   async function getVideoOutputFn(cameraManager: camera.CameraManager, cameraOutputCapability: camera.CameraOutputCapability, concurrentInfo: Array<camera.CameraConcurrentInfo>, curCameraDeviceFront: camera.CameraDevice, context: common.Context)
   {
    // 此处创建录像输出流以format：1003，size：1920*1080的videoProfile为例，对应的videoProfile必须在getCameraConcurrentInfos获取到的并发能力信息数组范围内。
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
       return;
     }
     let index = videoProfiles.findIndex((videoProfile: camera.VideoProfile) => {
       return videoProfile.size.width === videoProfileObj.size.width &&
         videoProfile.size.height === videoProfileObj.size.height &&
         videoProfile.format === videoProfileObj.format &&
         videoProfile.frameRateRange.min <= 60 &&
         videoProfile.frameRateRange.max <= 60;
     });
     if (index === -1) {
       return;
     }
     videoProfileObj = videoProfiles[index];
     let avRecorder = await createAVRecorder();
     if (avRecorder === undefined) {
       return;
     }
     await prepareAVRecorder(videoProfileObj, curCameraDeviceFront, avRecorder, context);
     let videoSurfaceId = await avRecorder.getInputSurface();
     let videoOutput = cameraManager.createVideoOutput(videoProfileObj, videoSurfaceId);
     if (videoOutput === undefined) {
       return;
     }
   }
   ```
7. 打开相机。通过[open](../harmonyos-references/arkts-apis-camera-camerainput.md#open18)以多摄同开状态打开指定相机。在使用[open](../harmonyos-references/arkts-apis-camera-camerainput.md#open18)接口前，请先查询接口是否支持并发能力集，并优先调用[getCameraConcurrentInfos](../harmonyos-references/arkts-apis-camera-cameramanager.md#getcameraconcurrentinfos18)方法，获取多摄同开状态下的相机并发能力集。请勿在未查询并发能力集的情况下使用[open](../harmonyos-references/arkts-apis-camera-camerainput.md#open18)，否则会导致打开相机失败。

   ```ts
   async function initCamera(cameraManager: camera.CameraManager, cameraDevice: camera.CameraDevice) {
     let cameraInput: camera.CameraInput | undefined = undefined;
     try {
       cameraInput = cameraManager.createCameraInput(cameraDevice);
       console.info('createCameraInputFn success');
     } catch (error) {
       console.error(`createCameraInputFn failed`);
     }
     if (cameraInput === undefined) {
       return;
     }
     let isOpenSuccess = false;
     try {

       // 当前版本支持camera.CameraConcurrentType.CAMERA_LIMITED_CAPABILITY模式并发打开相机。
       await cameraInput.open(camera.CameraConcurrentType.CAMERA_LIMITED_CAPABILITY);
       isOpenSuccess = true;
     } catch (error) {
       console.error(`createCameraInput failed`);
     }
     if (!isOpenSuccess) {
       return;
     }
   }
   ```
8. 会话流程。

   ```ts
    // 监听捕获会话错误变化。
   function onSessionErrorChange(session: camera.PhotoSession | camera.VideoSession): void {
     try {
       session.on('error', (captureSessionError: BusinessError): void => {
       });
     } catch (error) {
       console.error('onCaptureSessionErrorChange error');
     }
   }

   let handlePhotoAssetCb: (photoAsset: photoAccessHelper.PhotoAsset) => void = () => {
   };

   // 监听拍照事件。
   function photoOutputCallBack(photoOutput: camera.PhotoOutput): void {
     try {

       // 监听拍照开始。
       photoOutput.on('captureStartWithInfo', (err: BusinessError, captureStartInfo: camera.CaptureStartInfo): void => {
     });

     // 监听拍照帧输出捕获。
     photoOutput.on('frameShutter', (err: BusinessError, frameShutterInfo: camera.FrameShutterInfo): void => {
     });

    // 监听拍照结束。
     photoOutput.on('captureEnd', (err: BusinessError, captureEndInfo: camera.CaptureEndInfo): void => {
     });

     // 监听拍照异常。
     photoOutput.on('error', (data: BusinessError): void => {
     });
     photoOutput.on('photoAssetAvailable', (err: BusinessError, photoAsset: photoAccessHelper.PhotoAsset) => {
       if (photoAsset === undefined) {
         return;
       }
       handlePhotoAssetCb(photoAsset);
     });
     } catch (err) {
     }
   }

   // 会话流程。
   async function sessionFlowFn(cameraManager: camera.CameraManager, cameraInput: camera.CameraInput,
     previewOutput: camera.PreviewOutput, photoOutput: camera.PhotoOutput | undefined, videoOutput: camera.VideoOutput | undefined, curSceneMode: camera.SceneMode): Promise<void> {
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
       onSessionErrorChange(session);

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
         photoOutputCallBack(photoOutput);

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
     } catch (error) {
       console.error(`sessionFlowFn fail`);
     }
   }
   ```
9. 拍照，通过步骤8中配置的photoOutput使用前置或后置相机进行拍照，多摄同开状态下不支持前后相机同时拍照。

   ```ts
   async function takePicture(photoOutput: camera.PhotoOutput): Promise<void> {
     if (photoOutput === undefined) {
       return;
     }
     if (photoOutput === null) {
       return;
     }

     if (photoOutput) {
       await photoOutput.capture();
     } else {
       console.info('photoOutput is undefined or null');
     }
   }
   ```
10. 录制。

    ```ts
    let isRecording = false;

    // 启动录制。
    async function startVideo(videoOutput: camera.VideoOutput, avRecorder: media.AVRecorder): Promise<void> {
      try {
        await videoOutput?.start();
        await avRecorder?.start();
        isRecording = true;
      } catch (error) {
        console.error(`startVideo err`);
      }
    }

    // 停止录制。
    async function stopVideo(videoOutput: camera.VideoOutput, avRecorder: media.AVRecorder): Promise<void> {
      if (!isRecording) {
        return;
      }
      try {
        if (avRecorder) {
          await avRecorder.stop();
        }
        if (videoOutput) {
          await videoOutput.stop();
        }
        isRecording = false;
      } catch (error) {
        console.error(`stopVideo err`);
      }
    }
    ```
11. 在多摄同开状态下，前/后置相机可配置的能力示例如下（当前版本仅支持本文开头部分所示的七项基础功能）。

    ```ts
    // 闪光灯。
    function hasFlashFn(flashMode: camera.FlashMode, session: camera.PhotoSession | camera.VideoSession | undefined = undefined): void {

      // 检测是否有闪光灯。
      let hasFlash = session?.hasFlash();

      // 检测闪光灯模式是否支持。
      let isFlashModeSupported = session?.isFlashModeSupported(flashMode);

      // 设置闪光灯模式。
      if (isFlashModeSupported) {
        session?.setFlashMode(flashMode);
      }
    }

    // 曝光。
    function hasExposureFn(ExposureMode: camera.ExposureMode, session: camera.PhotoSession | camera.VideoSession | undefined = undefined): void {

      // 检测曝光模式是否支持。
      let hasFlash = session?.isExposureModeSupported(ExposureMode);

      // 设置曝光模式。
      if (hasFlash) {
        session?.setExposureMode(ExposureMode);
      }
    }

    // 获取可变焦距范围。
    function getZoomRatioRange(session: camera.PhotoSession | camera.VideoSession | undefined = undefined): Array<number> {
      let zoomRatioRange: Array<number> = [];
      if (session !== undefined) {
        zoomRatioRange = session.getZoomRatioRange();
      }
      return zoomRatioRange;
    }

    // 变焦。
    function setZoomRatioFn(zoomRatio: number, session: camera.PhotoSession | camera.VideoSession | undefined = undefined): void {

      // 获取支持的变焦范围。
      let zoomRatioRange = getZoomRatioRange();
      try {
        session?.setZoomRatio(zoomRatio);
      } catch (error) {
        console.error(`setZoomRatioFn fail`);
      }
    }

    // 曝光补偿。
    function setExposureBiasFn(exposureBias: number, session: camera.PhotoSession | camera.VideoSession | undefined = undefined): void {

      // 查询曝光补偿范围。
      let biasRangeArray: Array<number> | undefined = [];
      biasRangeArray = session?.getExposureBiasRange();

      // 设置曝光补偿。
      session?.setExposureBias(exposureBias);
    }

    // 对焦模式。
    function setFocusMode(focusMode: camera.FocusMode, session: camera.PhotoSession | camera.VideoSession | undefined = undefined): void {

      // 检测对焦模式是否支持。
      let isSupported = session?.isFocusModeSupported(focusMode);

      // 设置对焦模式。
      if (!isSupported) {
        return;
      }
      session?.setFocusMode(focusMode);
    }
    ```
