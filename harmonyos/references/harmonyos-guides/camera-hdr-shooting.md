---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/camera-hdr-shooting
title: HDR Vivid相机拍照(ArkTS)
breadcrumb: 指南 > 媒体 > Camera Kit（相机服务） > 开发相机应用基础能力(ArkTS) > HDR Vivid相机拍照(ArkTS)
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:16+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:b944ca9f830f2ac17db34e4cd88bbb45d83845918d2585e7dba11a2f097c7334
---

HarmonyOS支持调用接口拍摄HDR Vivid照片，可以拍出层次表现更细腻、光影细节更丰富的画面，提升画面质感，呈现更卓越的视觉效果。

当前示例提供完整的HDR Vivid拍照开发步骤，方便开发者实现HDR拍照的功能。更多HDR Vivid的开发指导，请参考[使用HDR Vivid特性开发媒体应用](multimedia-hdr-vivid.md)。

在参考以下示例前，建议开发者查看[相机开发指导(ArkTS)](camera-device-management.md)的具体章节，了解[设备输入](camera-device-input.md)、[会话管理](camera-session-management.md)、[拍照](camera-shooting.md)等单个流程。

## 开发步骤

1. 导入接口。

   ```ts
   import { camera } from '@kit.CameraKit';
   import { colorSpaceManager } from '@kit.ArkGraphics2D';
   import { image } from '@kit.ImageKit';
   import { BusinessError } from '@kit.BasicServicesKit';
   import { fileIo } from '@kit.CoreFileKit';
   import { photoAccessHelper } from '@kit.MediaLibraryKit';
   ```
2. 查询支持的色彩空间。

   ```ts
   function getSupportedColorSpaces(session: camera.PhotoSession): Array<colorSpaceManager.ColorSpace> {
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
3. 设置色彩空间。

   如果是SDR拍照色彩空间需要设置为SRGB，如果是HDR拍照色彩空间需要设置为DISPLAY\_P3。具体参考[setColorSpace](../harmonyos-references/arkts-apis-camera-colormanagement.md#setcolorspace12)。

   ```ts
   function setColorSpaceBeforeCommitConfig(session: camera.PhotoSession, isHdr: boolean): void {
     let colorSpace: colorSpaceManager.ColorSpace = isHdr? colorSpaceManager.ColorSpace.DISPLAY_P3 : colorSpaceManager.ColorSpace.SRGB;
     let colorSpaces: Array<colorSpaceManager.ColorSpace> = getSupportedColorSpaces(session);
     let isSupportedColorSpaces = colorSpaces.indexOf(colorSpace) >= 0;
     if (isSupportedColorSpaces) {
       console.info(`setColorSpace: ${colorSpace}`);
       session.setColorSpace(colorSpace);
       let activeColorSpace:colorSpaceManager.ColorSpace = session.getActiveColorSpace();
       console.info(`activeColorSpace: ${activeColorSpace}`);
     } else {
       console.info(`colorSpace: ${colorSpace} is not support`);
     }
   }
   ```
4. 实现HDR拍照。

   在提交会话配置前执行步骤3设置色彩空间，其余流程按照正常拍照流程开发。

   ```ts
   async function savePicture(buffer: ArrayBuffer, img: image.Image, context: Context): Promise<void> {
     let accessHelper: photoAccessHelper.PhotoAccessHelper = photoAccessHelper.getPhotoAccessHelper(context);
     let options: photoAccessHelper.CreateOptions = {
       title: Date.now().toString()
     };
     let photoUri: string = await accessHelper.createAsset(photoAccessHelper.PhotoType.IMAGE, 'jpg', options);
     // createAsset的调用需要ohos.permission.READ_IMAGEVIDEO和ohos.permission.WRITE_IMAGEVIDEO的权限
     let file: fileIo.File = fileIo.openSync(photoUri, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
     await fileIo.write(file.fd, buffer);
     fileIo.closeSync(file);
     img.release();
   }

   function setPhotoOutputCb(photoOutput: camera.PhotoOutput, context: Context): void {
     // 设置回调之后，调用photoOutput的capture方法，就会将拍照的buffer回传到回调中
     photoOutput.on('photoAvailable', (errCode: BusinessError, photo: camera.Photo): void => {
       console.info('getPhoto start');
       console.info(`err: ${JSON.stringify(errCode)}`);
       if (errCode || photo === undefined) {
         console.error('getPhoto failed');
         return;
       }
       let imageObj = photo.main;
       imageObj.getComponent(image.ComponentType.JPEG, (errCode: BusinessError, component: image.Component): void => {
         console.info('getComponent start');
         if (errCode || component === undefined) {
           console.error('getComponent failed');
           return;
         }
         let buffer: ArrayBuffer;
         if (component.byteBuffer) {
           buffer = component.byteBuffer;
         } else {
           console.error('byteBuffer is null');
           return;
         }
         savePicture(buffer, imageObj, context);
       });
     });
   }

   async function cameraHdrShootingCase(context: Context, surfaceId: string): Promise<void> {
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
     let cameraArray: Array<camera.CameraDevice> = cameraManager.getSupportedCameras();
     if (cameraArray.length <= 0) {
       console.error("cameraManager.getSupportedCameras error");
       return;
     }

     for (let index = 0; index < cameraArray.length; index++) {
       console.info('cameraId : ' + cameraArray[index].cameraId);                          // 获取相机ID
       console.info('cameraPosition : ' + cameraArray[index].cameraPosition);              // 获取相机位置
       console.info('cameraType : ' + cameraArray[index].cameraType);                      // 获取相机类型
       console.info('connectionType : ' + cameraArray[index].connectionType);              // 获取相机连接类型
     }

     // 创建相机输入流
     let cameraInput: camera.CameraInput | undefined = undefined;
     try {
       cameraInput = cameraManager.createCameraInput(cameraArray[0]);
     } catch (error) {
       let err = error as BusinessError;
       console.error('Failed to createCameraInput errorCode = ' + err.code);
     }
     if (cameraInput === undefined) {
       return;
     }

     // 监听cameraInput错误信息
     let cameraDevice: camera.CameraDevice = cameraArray[0];
     cameraInput.on('error', cameraDevice, (error: BusinessError) => {
       console.error(`Camera input error code: ${error.code}`);
     })

     // 打开相机
     await cameraInput.open();

     // 获取支持的模式类型
     let sceneModes: Array<camera.SceneMode> = cameraManager.getSupportedSceneModes(cameraArray[0]);
     let isSupportPhotoMode: boolean = sceneModes.indexOf(camera.SceneMode.NORMAL_PHOTO) >= 0;
     if (!isSupportPhotoMode) {
       console.error('photo mode not support');
       return;
     }
     // 获取相机设备支持的输出流能力
     let cameraOutputCap: camera.CameraOutputCapability = cameraManager.getSupportedOutputCapability(cameraArray[0], camera.SceneMode.NORMAL_PHOTO);
     if (!cameraOutputCap) {
       console.error("cameraManager.getSupportedOutputCapability error");
       return;
     }
     console.info("outputCapability: " + JSON.stringify(cameraOutputCap));

     let previewProfilesArray: Array<camera.Profile> = cameraOutputCap.previewProfiles;
     if (!previewProfilesArray) {
       console.error("createOutput previewProfilesArray == null || undefined");
     }

     let photoProfilesArray: Array<camera.Profile> = cameraOutputCap.photoProfiles;
     if (!photoProfilesArray) {
       console.error("createOutput photoProfilesArray == null || undefined");
     }

     // 创建预览输出流,其中参数 surfaceId 参考上文 XComponent 组件，预览流为XComponent组件提供的surface
     let previewOutput: camera.PreviewOutput | undefined = undefined;
     try {
       previewOutput = cameraManager.createPreviewOutput(previewProfilesArray[0], surfaceId);
     } catch (error) {
       let err = error as BusinessError;
       console.error(`Failed to create the PreviewOutput instance. error code: ${err.code}`);
     }
     if (previewOutput === undefined) {
       return;
     }
     // 监听预览输出错误信息
     previewOutput.on('error', (error: BusinessError) => {
       console.error(`Preview output error code: ${error.code}`);
     });

     // 创建拍照输出流
     let photoOutput: camera.PhotoOutput | undefined = undefined;
     try {
       photoOutput = cameraManager.createPhotoOutput(photoProfilesArray[0]);
     } catch (error) {
       let err = error as BusinessError;
       console.error('Failed to createPhotoOutput errorCode = ' + err.code);
     }
     if (photoOutput === undefined) {
       return;
     }

     // 调用上面的回调函数来保存图片
     setPhotoOutputCb(photoOutput, context);

     // 创建会话
     let photoSession: camera.PhotoSession | undefined = undefined;
     try {
       photoSession = cameraManager.createSession(camera.SceneMode.NORMAL_PHOTO) as camera.PhotoSession;
     } catch (error) {
       let err = error as BusinessError;
       console.error('Failed to create the session instance. errorCode = ' + err.code);
     }
     if (photoSession === undefined) {
       return;
     }
     // 监听session错误信息
     photoSession.on('error', (error: BusinessError) => {
       console.error(`Capture session error code: ${error.code}`);
     });

     // 开始配置会话
     try {
       photoSession.beginConfig();
     } catch (error) {
       let err = error as BusinessError;
       console.error('Failed to beginConfig. errorCode = ' + err.code);
     }

     // 向会话中添加相机输入流
     try {
       photoSession.addInput(cameraInput);
     } catch (error) {
       let err = error as BusinessError;
       console.error('Failed to addInput. errorCode = ' + err.code);
     }

     // 向会话中添加预览输出流
     try {
       photoSession.addOutput(previewOutput);
     } catch (error) {
       let err = error as BusinessError;
       console.error('Failed to addOutput(previewOutput). errorCode = ' + err.code);
     }

     // 向会话中添加拍照输出流
     try {
       photoSession.addOutput(photoOutput);
     } catch (error) {
       let err = error as BusinessError;
       console.error('Failed to addOutput(photoOutput). errorCode = ' + err.code);
     }

     // 设置色彩空间
     setColorSpaceBeforeCommitConfig(photoSession, true);

     // 提交会话配置
     await photoSession.commitConfig();

     // 启动会话
     await photoSession.start().then(() => {
       console.info('Promise returned to indicate the session start success.');
     });

     let photoCaptureSetting: camera.PhotoCaptureSetting = {
       quality: camera.QualityLevel.QUALITY_LEVEL_HIGH, // 设置图片质量高
       rotation: camera.ImageRotation.ROTATION_0 // 设置图片旋转角度0
     }
     // 使用当前拍照设置进行拍照
     photoOutput.capture(photoCaptureSetting, (err: BusinessError) => {
       if (err) {
         console.error(`Failed to capture the photo ${err.message}`);
         return;
       }
       console.info('Callback invoked to indicate the photo capture request success.');
     });

     // 需要在拍照结束之后调用以下关闭摄像头和释放会话流程，避免拍照未结束就将会话释放。
     // 停止当前会话
     await photoSession.stop();

     // 释放相机输入流
     await cameraInput.close();

     // 释放预览输出流
     await previewOutput.release();

     // 释放拍照输出流
     await photoOutput.release();

     // 释放会话
     await photoSession.release();

     // 会话置空
     photoSession = undefined;
   }
   ```
