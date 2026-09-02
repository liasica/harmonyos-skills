---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/camera-hdr-recording
title: HDR Vivid相机录像(ArkTS)
breadcrumb: 指南 > 媒体 > Camera Kit（相机服务） > 开发相机应用基础能力(ArkTS) > HDR Vivid相机录像(ArkTS)
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:45+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:6973a3e5d9d5377baa2b0cb675bd82bc6fbe012d1f780e6496d5d12ca7cbf5d9
---

HarmonyOS支持调用接口，录制HDR Vivid视频，可以拍出层次表现更细腻、光影细节更丰富的画面，提升画面质感，呈现更卓越的视觉效果。

当前示例提供完整的HDR Vivid录像开发步骤，方便开发者实现录制HDR Vivid视频的功能。更多HDR Vivid的开发指导，请参考[使用HDR Vivid特性开发媒体应用](multimedia-hdr-vivid.md)。

在参考以下示例前，建议开发者查看[相机开发指导(ArkTS)](camera-device-management.md)的具体章节，了解[设备输入](camera-device-input.md)、[会话管理](camera-session-management.md)、[录像](camera-recording.md)等单个流程。

## 开发步骤

1. 导入接口。

   ```ts
   import { camera } from '@kit.CameraKit';
   import { colorSpaceManager } from '@kit.ArkGraphics2D';
   import { BusinessError } from '@kit.BasicServicesKit';
   import { media } from '@kit.MediaKit';
   import { common } from '@kit.AbilityKit';
   import { photoAccessHelper } from '@kit.MediaLibraryKit';
   import { fileIo } from '@kit.CoreFileKit';
   ```
2. 获取预览、录像的配置项。

   HDR录像的输出格式需要设置成10bit的CAMERA\_FORMAT\_YCRCB\_P010。具体参考[setColorSpace](../harmonyos-references/arkts-apis-camera-colormanagement.md#setcolorspace12)。

   **说明** 

   预览流与录像输出流的分辨率的宽高比要保持一致，如果设置XComponent组件中的Surface显示区域宽高比为1920:1080 = 16:9，则需要预览流中的分辨率的宽高比也为16:9，如分辨率选择640:360，或960:540，或1920:1080，以此类推。

   ```ts
   function getPreviewProfile(previewProfiles: Array<camera.Profile>, size: camera.Size): undefined | camera.Profile {
     let previewProfile: undefined | camera.Profile = previewProfiles.find((profile: camera.Profile) => {
       return profile.format === camera.CameraFormat.CAMERA_FORMAT_YCRCB_P010 &&
         profile.size.width === size.width && profile.size.height == size.height
     });
     return previewProfile;
   }

   function getVideoProfile(videoProfiles: Array<camera.VideoProfile>, size: camera.Size): undefined | camera.VideoProfile {
     let videoProfile: undefined | camera.VideoProfile = videoProfiles.find((profile: camera.VideoProfile) => {
       return profile.format === camera.CameraFormat.CAMERA_FORMAT_YCRCB_P010 &&
         profile.size.width === size.width && profile.size.height == size.height
     });
     return videoProfile;
   }
   ```
3. 查询是否支持视频防抖。

   HDR录像需要支持视频防抖。

   ```ts
   function isVideoStabilizationModeSupported(session: camera.VideoSession, mode: camera.VideoStabilizationMode): boolean {
     let isSupported: boolean = false;
     try {
       isSupported = session.isVideoStabilizationModeSupported(mode);
     } catch (error) {
       // 失败返回错误码error.code并处理
       let err = error as BusinessError;
       console.error(`The isVideoStabilizationModeSupported call failed. error code: ${err.code}`);
     }
     return isSupported;
   }
   ```
4. 设置视频防抖。

   ```ts
   function setVideoStabilizationMode(session: camera.VideoSession): void {
     let mode: camera.VideoStabilizationMode = camera.VideoStabilizationMode.AUTO;
     // 查询是否支持视频防抖
     let isSupported: boolean = isVideoStabilizationModeSupported(session, mode);
     if (isSupported) {
       console.info(`setVideoStabilizationMode: ${mode}`);
       // 设置视频防抖
       try {
         session.setVideoStabilizationMode(mode);
       } catch (error) {
         // 失败返回错误码error.code并处理
         let err = error as BusinessError;
         console.error(`setVideoStabilizationMode call failed. error code: ${err.code}`);
       }
       let activeVideoStabilizationMode = session.getActiveVideoStabilizationMode();
       console.info(`activeVideoStabilizationMode: ${activeVideoStabilizationMode}`);
     } else {
       console.info(`videoStabilizationMode: ${mode} is not support`);
     }
   }
   ```
5. 查询支持的色彩空间。

   ```ts
   function getSupportedColorSpaces(session: camera.VideoSession): Array<colorSpaceManager.ColorSpace> {
     let colorSpaces: Array<colorSpaceManager.ColorSpace> = [];
     try {
       colorSpaces = session.getSupportedColorSpaces();
     } catch (error) {
       let err = error as BusinessError;
       console.error(`The getSupportedColorSpaces call failed. error code: ${err.code}`);
     }
     return colorSpaces;
   }
   ```
6. 设置色彩空间。

   如果是SDR录像色彩空间需要设置为BT709\_LIMIT，如果是HDR录像色彩空间需要设置为BT2020\_HLG\_LIMIT。具体参考[setColorSpace](../harmonyos-references/arkts-apis-camera-colormanagement.md#setcolorspace12)。建议在提交会话配置之前调用[setColorSpace](../harmonyos-references/arkts-apis-camera-colormanagement.md#setcolorspace12)。

   ```ts
   function setColorSpaceBeforeCommitConfig(session: camera.VideoSession, isHdr: boolean): void {
     let colorSpace: colorSpaceManager.ColorSpace = isHdr? colorSpaceManager.ColorSpace.BT2020_HLG_LIMIT : colorSpaceManager.ColorSpace.BT709_LIMIT;
     let colorSpaces: Array<colorSpaceManager.ColorSpace> = session.getSupportedColorSpaces();
     let isSupportedColorSpaces = colorSpaces.indexOf(colorSpace) >= 0;
     if (isSupportedColorSpaces) {
       console.info(`setColorSpace: ${colorSpace}`);
       try {
         session.setColorSpace(colorSpace);
       } catch (error) {
         // 失败返回错误码error.code并处理
         let err = error as BusinessError;
         console.error(`setColorSpace call failed. error code: ${err.code}`);
       }
       let activeColorSpace:colorSpaceManager.ColorSpace = session.getActiveColorSpace();
       console.info(`activeColorSpace: ${activeColorSpace}`);
     } else {
       console.info(`colorSpace: ${colorSpace} is not support`);
     }
   }
   ```
7. 实现HDR录像。

   在创建预览输出、录像输出前执行步骤2获取配置项，提交会话配置前执行步骤6设置色彩空间，提交会话配置后执行步骤4设置视频防抖，其余流程按照正常录像流程开发。

   **说明** 

   如需在提交会话配置后，设置视频防抖模式和色彩空间，为避免相机输出流配置异常，请先通过[setVideoStabilizationMode](../harmonyos-references/arkts-apis-camera-stabilization.md#setvideostabilizationmode11)方法4. 设置视频防抖后，再通过[setColorSpace](../harmonyos-references/arkts-apis-camera-colormanagement.md#setcolorspace12)方法完成6.设置色彩空间。

   ```ts
   async function cameraHdrRecordingCase(context: common.Context, surfaceId: string): Promise<void> {
     // 创建CameraManager对象
     let cameraManager: camera.CameraManager = camera.getCameraManager(context);
     if (!cameraManager) {
       console.error("camera.getCameraManager error");
       return;
     }

     // 监听相机状态变化
     cameraManager.on('cameraStatus', (err: BusinessError, cameraStatusInfo: camera.CameraStatusInfo) => {
       if (err !== undefined && err.code !== 0) {
         console.error('cameraStatus with errorCode = ' + err.code);
         return;
       }
       console.info(`camera : ${cameraStatusInfo.camera.cameraId}`);
       console.info(`status: ${cameraStatusInfo.status}`);
     });

     // 获取相机列表
     let cameraArray: Array<camera.CameraDevice> = [];
     try {
       cameraArray = cameraManager.getSupportedCameras();
     } catch (error) {
       let err = error as BusinessError;
       console.error(`getSupportedCameras call failed. error code: ${err.code}`);
     }

     if (cameraArray.length <= 0) {
       console.error("cameraManager.getSupportedCameras error");
       return;
     }

     // 获取支持的模式类型
     let sceneModes: Array<camera.SceneMode> = cameraManager.getSupportedSceneModes(cameraArray[0]);
     let isSupportVideoMode: boolean = sceneModes.indexOf(camera.SceneMode.NORMAL_VIDEO) >= 0;
     if (!isSupportVideoMode) {
       console.error('video mode not support');
       return;
     }

     // 获取相机设备支持的输出流能力
     let cameraOutputCap: camera.CameraOutputCapability = cameraManager.getSupportedOutputCapability(cameraArray[0], camera.SceneMode.NORMAL_VIDEO);
     if (!cameraOutputCap) {
       console.error("cameraManager.getSupportedOutputCapability error")
       return;
     }
     console.info("outputCapability: " + JSON.stringify(cameraOutputCap));

     let previewProfilesArray: Array<camera.Profile> = cameraOutputCap.previewProfiles;
     if (!previewProfilesArray) {
       console.error("createOutput previewProfilesArray == null || undefined");
       return;
     }

     let videoProfilesArray: Array<camera.VideoProfile> = cameraOutputCap.videoProfiles;
     if (!videoProfilesArray) {
       console.error("createOutput videoProfilesArray == null || undefined");
       return;
     }
     // videoProfile的宽高需要与AVRecorderProfile的宽高保持一致，并且需要使用AVRecorderProfile所支持的宽高
     let videoSize: camera.Size = {
       width: 640,
       height: 480
     }
     let previewProfile: undefined | camera.Profile = getPreviewProfile(previewProfilesArray, videoSize);
     if (!previewProfile) {
       console.error('previewProfile is not found');
       return;
     }
     let videoProfile: undefined | camera.VideoProfile = getVideoProfile(videoProfilesArray, videoSize);
     if (!videoProfile) {
       console.error('videoProfile is not found');
       return;
     }
     // 配置参数以实际硬件设备支持的范围为准
     let aVRecorderProfile: media.AVRecorderProfile = {
       audioBitrate: 48000,
       audioChannels: 2,
       audioCodec: media.CodecMimeType.AUDIO_AAC,
       audioSampleRate: 48000,
       fileFormat: media.ContainerFormatType.CFT_MPEG_4,
       videoBitrate: 2000000,
       videoCodec: media.CodecMimeType.VIDEO_HEVC,
       videoFrameWidth: videoSize.width,
       videoFrameHeight: videoSize.height,
       videoFrameRate: 30,
       isHdr: true
     };
     let options: photoAccessHelper.CreateOptions = {
       title: Date.now().toString()
     };
     let accessHelper: photoAccessHelper.PhotoAccessHelper = photoAccessHelper.getPhotoAccessHelper(context);
     let videoUri: string = await accessHelper.createAsset(photoAccessHelper.PhotoType.VIDEO, 'mp4', options);
     let file: fileIo.File = fileIo.openSync(videoUri, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
     let aVRecorderConfig: media.AVRecorderConfig = {
       audioSourceType: media.AudioSourceType.AUDIO_SOURCE_TYPE_MIC,
       videoSourceType: media.VideoSourceType.VIDEO_SOURCE_TYPE_SURFACE_YUV,
       profile: aVRecorderProfile,
       url: `fd://${file.fd.toString()}`, // 文件需先由调用者创建，赋予读写权限，将文件fd传给此参数，eg.fd://45--file:///data/media/01.mp4
       rotation: 0, // 合理值0、90、180、270，非合理值prepare接口将报错
       location: { latitude: 30, longitude: 130 }
     };

     let avRecorder: media.AVRecorder | undefined = undefined;
     try {
       avRecorder = await media.createAVRecorder();
     } catch (error) {
       let err = error as BusinessError;
       console.error(`createAVRecorder call failed. error code: ${err.code}`);
     }

     if (avRecorder === undefined) {
       return;
     }

     try {
       await avRecorder.prepare(aVRecorderConfig);
     } catch (error) {
       let err = error as BusinessError;
       console.error(`prepare call failed. error code: ${err.code}`);
     }

     let videoSurfaceId: string | undefined = undefined; // 该surfaceID用于传递给相机接口创建videoOutput
     try {
       videoSurfaceId = await avRecorder.getInputSurface();
     } catch (error) {
       let err = error as BusinessError;
       console.error(`getInputSurface call failed. error code: ${err.code}`);
     }
     if (videoSurfaceId === undefined) {
       return;
     }
     // 创建VideoOutput对象
     let videoOutput: camera.VideoOutput | undefined = undefined;
     try {
       videoOutput = cameraManager.createVideoOutput(videoProfile, videoSurfaceId);
     } catch (error) {
       let err = error as BusinessError;
       console.error(`Failed to create the videoOutput instance. error: ${JSON.stringify(err)}`);
     }
     if (videoOutput === undefined) {
       return;
     }
     // 监听视频输出错误信息
     videoOutput.on('error', (error: BusinessError) => {
       console.error(`Preview output error code: ${error.code}`);
     });

     // 创建会话
     let videoSession: camera.VideoSession | undefined = undefined;
     try {
       videoSession = cameraManager.createSession(camera.SceneMode.NORMAL_VIDEO) as camera.VideoSession;
     } catch (error) {
       let err = error as BusinessError;
       console.error(`Failed to create the session instance. error: ${JSON.stringify(err)}`);
     }
     if (videoSession === undefined) {
       return;
     }
     // 监听session错误信息
     videoSession.on('error', (error: BusinessError) => {
       console.error(`Video session error code: ${error.code}`);
     });

     // 开始配置会话
     try {
       videoSession.beginConfig();
     } catch (error) {
       let err = error as BusinessError;
       console.error(`Failed to beginConfig. error: ${JSON.stringify(err)}`);
     }

     // 创建相机输入流
     let cameraInput: camera.CameraInput | undefined = undefined;
     try {
       cameraInput = cameraManager.createCameraInput(cameraArray[0]);
     } catch (error) {
       let err = error as BusinessError;
       console.error(`Failed to createCameraInput. error: ${JSON.stringify(err)}`);
     }
     if (cameraInput === undefined) {
       return;
     }
     // 监听cameraInput错误信息
     let cameraDevice: camera.CameraDevice = cameraArray[0];
     cameraInput.on('error', cameraDevice, (error: BusinessError) => {
       console.error(`Camera input error code: ${error.code}`);
     });

     // 打开相机
     try {
       await cameraInput.open();
     } catch (error) {
       let err = error as BusinessError;
       console.error(`Failed to open cameraInput. error: ${JSON.stringify(err)}`);
     }

     // 向会话中添加相机输入流
     try {
       videoSession.addInput(cameraInput);
     } catch (error) {
       let err = error as BusinessError;
       console.error(`Failed to add cameraInput. error: ${JSON.stringify(err)}`);
     }

     // 创建预览输出流，其中参数 surfaceId 参考下面 XComponent 组件，预览流为XComponent组件提供的surface
     let previewOutput: camera.PreviewOutput | undefined = undefined;
     try {
       previewOutput = cameraManager.createPreviewOutput(previewProfile, surfaceId);
     } catch (error) {
       let err = error as BusinessError;
       console.error(`Failed to create the PreviewOutput instance. error: ${JSON.stringify(err)}`);
     }

     if (previewOutput === undefined) {
       return;
     }
     // 向会话中添加预览输出流
     try {
       videoSession.addOutput(previewOutput);
     } catch (error) {
       let err = error as BusinessError;
       console.error(`Failed to add previewOutput. error: ${JSON.stringify(err)}`);
     }

     // 向会话中添加录像输出流
     try {
       videoSession.addOutput(videoOutput);
     } catch (error) {
       let err = error as BusinessError;
       console.error(`Failed to add videoOutput. error: ${JSON.stringify(err)}`);
     }

     // 设置色彩空间
     setColorSpaceBeforeCommitConfig(videoSession, true);

     // 提交会话配置
     try {
       await videoSession.commitConfig();
     } catch (error) {
       let err = error as BusinessError;
       console.error(`videoSession commitConfig error: ${JSON.stringify(err)}`);
     }

     // 设置视频防抖
     setVideoStabilizationMode(videoSession);

     // 启动会话
     try {
       await videoSession.start();
     } catch (error) {
       let err = error as BusinessError;
       console.error(`videoSession start error: ${JSON.stringify(err)}`);
     }

     // 启动录像输出流
     videoOutput.start((err: BusinessError) => {
       if (err) {
         console.error(`Failed to start the video output. error: ${JSON.stringify(err)}`);
         return;
       }
       console.info('Callback invoked to indicate the video output start success.');
     });

     // 开始录像
     try {
       await avRecorder.start();
     } catch (error) {
       let err = error as BusinessError;
       console.error(`avRecorder start error: ${JSON.stringify(err)}`);
     }

     // 停止录像输出流
     videoOutput.stop((err: BusinessError) => {
       if (err) {
         console.error(`Failed to stop the video output. error: ${JSON.stringify(err)}`);
         return;
       }
       console.info('Callback invoked to indicate the video output stop success.');
     });

     // 停止录像
     try {
       await avRecorder.stop();
     } catch (error) {
       let err = error as BusinessError;
       console.error(`avRecorder stop error: ${JSON.stringify(err)}`);
     }

     // 停止当前会话
     await videoSession.stop();

     // 关闭文件
     fileIo.closeSync(file);

     // 释放相机输入流
     await cameraInput.close();

     // 释放预览输出流
     await previewOutput.release();

     // 释放录像输出流
     await videoOutput.release();

     // 释放会话
     await videoSession.release();

     // 会话置空
     videoSession = undefined;
   }
   ```
