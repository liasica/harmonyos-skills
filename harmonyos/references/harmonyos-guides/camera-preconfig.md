---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/camera-preconfig
title: 使用相机预配置(ArkTS)
breadcrumb: 指南 > 媒体 > Camera Kit（相机服务） > 开发相机应用基础能力(ArkTS) > 使用相机预配置(ArkTS)
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:45+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:7e7ba5b06b41ad328f4b081e5ba827cf8eb11ee4ab81079fa6fc47490ea36d07
---

相机预配置（Preconfig），对常用的场景和分辨率进行了预配置集成，可简化开发相机应用流程，提高应用的开发效率。

开发者在开发相机应用时，在获取到[CameraDevice](../harmonyos-references/arkts-apis-camera-i.md#cameradevice)之后，如果遵循通用流程开发，步骤较为繁琐。需要先调用[CameraManager](../harmonyos-references/arkts-apis-camera-cameramanager.md)的[getSupportedOutputCapability](../harmonyos-references/arkts-apis-camera-cameramanager.md#getsupportedoutputcapability11)来查询当前相机在指定模式下所支持的各类输出的配置信息，拿到[CameraOutputCapability](../harmonyos-references/arkts-apis-camera-i.md#cameraoutputcapability)之后，应用开发者还需要对里面的各类数据进行解析，筛选，找到自己需要的配置数据[Profile](../harmonyos-references/arkts-apis-camera-i.md#profile)以及[VideoProfile](../harmonyos-references/arkts-apis-camera-i.md#videoprofile)。最后使用对应的Profile以及VideoProfile创建对应的[PreviewOutput](../harmonyos-references/arkts-apis-camera-previewoutput.md)、[PhotoOutput](../harmonyos-references/arkts-apis-camera-photooutput.md)以及[VideoOutput](../harmonyos-references/arkts-apis-camera-videooutput.md)。

为了解决上述问题，优化应用开发流程，系统针对拍照（[PhotoSession](../harmonyos-references/arkts-apis-camera-photosession.md)）、录像（[VideoSession](../harmonyos-references/arkts-apis-camera-videosession.md)）两类场景，提供了[preconfig](../harmonyos-references/arkts-apis-camera-photosession.md#preconfig12)接口帮助开发者快速完成相机参数配置。推荐仅需要自定义拍照界面的无需开发专业相机应用的开发者，使用相机预配置功能快速开发应用。

在开发相机应用时，需要先[申请相关权限](camera-preparation.md)。以拍照（PhotoSession）为例，相机预配置（Preconfig）开发流程与[通用流程](camera-shooting-case.md)开发，存在以下差异：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/C2z_SiWpSHSKWsxkxMCZwg/zh-cn_image_0000002706674620.png)

**其他相关能力：**

* [CameraPicker](camera-picker.md)：无需开发相机功能，拉起系统相机获取照片或视频。
* [调用全量相机接口开发](camera-overview.md)：可开发自定义界面、分辨率、图像效果的专业相机应用。

## 规格说明

系统提供了4种预配置类型（[PreconfigType](../harmonyos-references/arkts-apis-camera-e.md#preconfigtype12)），分别为PRECONFIG\_720P、PRECONFIG\_1080P、PRECONFIG\_4K、PRECONFIG\_HIGH\_QUALITY。以及3种画幅比例规格（[PreconfigRatio](../harmonyos-references/arkts-apis-camera-e.md#preconfigratio12)），1:1画幅（PRECONFIG\_RATIO\_1\_1）、4:3画幅（PRECONFIG\_RATIO\_4\_3）、16:9画幅（PRECONFIG\_RATIO\_16\_9）。

**注意** 

由于不同的设备所支持的能力不同。使用相机预配置（Preconfig）功能时，需要先调用[canPreconfig](../harmonyos-references/arkts-apis-camera-photosession.md#canpreconfig12)检查对应的PreconfigType和PreconfigRatio的组合在当前设备上是否支持。

在不同的画幅比例下，其分辨率规格不同，详见下表。

* 普通拍照模式下的预览输出

  | 预配置类型PreconfigType | PRECONFIG\_RATIO\_1\_1 | PRECONFIG\_RATIO\_4\_3 | PRECONFIG\_RATIO\_16\_9 |
  | --- | --- | --- | --- |
  | PRECONFIG\_720P | 720x720 | 960x720 | 1280x720 |
  | PRECONFIG\_1080P | 1080x1080 | 1440x1080 | 1920x1080 |
  | PRECONFIG\_4K | 1080x1080 | 1440x1080 | 1920x1080 |
  | PRECONFIG\_HIGH\_QUALITY | 1440x1440 | 1920x1440 | 2560x1440 |
* 普通拍照模式下的拍照输出

  | 预配置类型PreconfigType | PRECONFIG\_RATIO\_1\_1 | PRECONFIG\_RATIO\_4\_3 | PRECONFIG\_RATIO\_16\_9 |
  | --- | --- | --- | --- |
  | PRECONFIG\_720P | 720x720 | 960x720 | 1280x720 |
  | PRECONFIG\_1080P | 1080x1080 | 1440x1080 | 1920x1080 |
  | PRECONFIG\_4K | 2160x2160 | 2880x2160 | 3840x2160 |
  | PRECONFIG\_HIGH\_QUALITY | 跟随Sensor（镜头）最大能力 | 跟随Sensor（镜头）最大能力 | 跟随Sensor（镜头）最大能力 |
* 普通录像模式下的预览输出

  | 预配置类型PreconfigType | PRECONFIG\_RATIO\_1\_1 | PRECONFIG\_RATIO\_4\_3 | PRECONFIG\_RATIO\_16\_9 |
  | --- | --- | --- | --- |
  | PRECONFIG\_720P | 720x720 | 960x720 | 1280x720 |
  | PRECONFIG\_1080P | 1080x1080 | 1440x1080 | 1920x1080 |
  | PRECONFIG\_4K | 1080x1080 | 1440x1080 | 1920x1080 |
  | PRECONFIG\_HIGH\_QUALITY | 1080x1080 | 1440x1080 | 1920x1080 |
* 普通录像模式下的录像输出

  | 预配置类型PreconfigType | PRECONFIG\_RATIO\_1\_1 | PRECONFIG\_RATIO\_4\_3 | PRECONFIG\_RATIO\_16\_9 |
  | --- | --- | --- | --- |
  | PRECONFIG\_720P | 720x720 | 960x720 | 1280x720 |
  | PRECONFIG\_1080P | 1080x1080 | 1440x1080 | 1920x1080 |
  | PRECONFIG\_4K | 2160x2160 | 2880x2160 | 3840x2160 |
  | PRECONFIG\_HIGH\_QUALITY | 2160x2160 | 2880x2160 | 3840x2160 |
* 普通录像模式下的拍照输出

  | 预配置类型PreconfigType | PRECONFIG\_RATIO\_1\_1 | PRECONFIG\_RATIO\_4\_3 | PRECONFIG\_RATIO\_16\_9 |
  | --- | --- | --- | --- |
  | PRECONFIG\_720P | 跟随Sensor（镜头）最大能力 | 跟随Sensor（镜头）最大能力 | 跟随Sensor（镜头）最大能力 |
  | PRECONFIG\_1080P | 跟随Sensor（镜头）最大能力 | 跟随Sensor（镜头）最大能力 | 跟随Sensor（镜头）最大能力 |
  | PRECONFIG\_4K | 跟随Sensor（镜头）最大能力 | 跟随Sensor（镜头）最大能力 | 跟随Sensor（镜头）最大能力 |
  | PRECONFIG\_HIGH\_QUALITY | 跟随Sensor（镜头）最大能力 | 跟随Sensor（镜头）最大能力 | 跟随Sensor（镜头）最大能力 |

## 开发步骤

详细的API说明请参考[Camera API参考](../harmonyos-references/js-apis-camera.md)。

1. 导入相关接口。

   ```ts
   import { camera } from '@kit.CameraKit';
   import { BusinessError } from '@kit.BasicServicesKit';
   import { common } from '@kit.AbilityKit';
   ```
2. 创建输出流Output。

   此处以创建预览流和拍照流为例。

   创建预览输出流时，涉及参数surfaceId。XComponent组件为预览流提供Surface（获取surfaceId请参考[getXcomponentSurfaceId](../harmonyos-references/ts-basic-components-xcomponent.md#getxcomponentsurfaceid9)方法），而XComponent的能力由UI提供，相关介绍可参考[XComponent组件参考](../harmonyos-references/ts-basic-components-xcomponent.md)。

   创建cameraManager对象的方法可参考[getCameraManager](../harmonyos-references/arkts-apis-camera-f.md#cameragetcameramanager)。

   Context获取方式请参考：[获取UIAbility的上下文信息](uiability-usage.md#获取uiability的上下文信息)。

   ```ts
   function createCameraOutput(context: common.BaseContext, surfaceId: string) : void {
     // 创建预览输出流
     let previewOutput: camera.PreviewOutput | undefined = undefined;
     let cameraManager = camera.getCameraManager(context);
     try {
       previewOutput = cameraManager.createPreviewOutput(surfaceId);
     } catch (error) {
       let err = error as BusinessError;
       console.error(`Failed to create the PreviewOutput instance. error code: ${err.code}`);
     }
     if (previewOutput === undefined) {
       return;
     }

     // 创建拍照输出流
     let photoOutput: camera.PhotoOutput | undefined = undefined;
     try {
       photoOutput = cameraManager.createPhotoOutput();
     } catch (error) {
       let err = error as BusinessError;
       console.error('Failed to createPhotoOutput errorCode = ' + err.code);
     }
     if (photoOutput === undefined) {
       return;
     }
   }
   ```
3. 调用[CameraManager](../harmonyos-references/arkts-apis-camera-cameramanager.md)中的[createCameraInput](../harmonyos-references/arkts-apis-camera-cameramanager.md#createcamerainput)方法，创建输入流Input。

   ```ts
   async function createAndOpenCameraInput(cameraManager: camera.CameraManager) : Promise<void> {
     // 获取相机列表
     let cameraArray: Array<camera.CameraDevice> = cameraManager.getSupportedCameras();
     if (cameraArray.length <= 0) {
       console.error("cameraManager.getSupportedCameras error");
       return;
     }
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
     // 打开相机
     await cameraInput.open();
   }
   ```
4. 调用[createSession](../harmonyos-references/arkts-apis-camera-cameramanager.md#createsession11)创建会话（Session）。

   **说明** 

   SceneMode需要指定为NORMAL\_PHOTO或NORMAL\_VIDEO，对应拍照场景[PhotoSession](../harmonyos-references/arkts-apis-camera-photosession.md)和录像场景[VideoSession](../harmonyos-references/arkts-apis-camera-videosession.md)。

   ```ts
   function createCameraSession(cameraManager: camera.CameraManager) : void {
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
   }
   ```
5. 调用[canPreconfig](../harmonyos-references/arkts-apis-camera-photosession.md#canpreconfig12)检查对应的PreconfigType和PreconfigRatio的组合在当前设备上是否支持。确认支持后，调用[preconfig](../harmonyos-references/arkts-apis-camera-photosession.md#preconfig12)启用Preconfig配置。

   ```ts
   function GetPreconfig(photoSession: camera.PhotoSession) : void {
     // 查询Preconfig能力
     try {
       let isPreconfigSupport = photoSession.canPreconfig(camera.PreconfigType.PRECONFIG_1080P);
       if (!isPreconfigSupport) {
         console.error('PhotoSession canPreconfig check fail.');
         return;
       }
     } catch (error) {
       let err = error as BusinessError;
       console.error('Failed to call canPreconfig. errorCode = ' + err.code);
       return;
     }

     // 配置Preconfig
     try {
       photoSession.preconfig(camera.PreconfigType.PRECONFIG_1080P);
     } catch (error) {
       let err = error as BusinessError;
       console.error('Failed to call preconfig. errorCode = ' + err.code);
       return;
     }
   }
   ```

   **说明** 

   若当前模式为普通录像模式，且[PreconfigType](../harmonyos-references/arkts-apis-camera-e.md#preconfigtype12)使用PRECONFIG\_HIGH\_QUALITY类型时，为避免录制失败，请务必将[AVRecorderProfile](../harmonyos-references/arkts-apis-media-i.md#avrecorderprofile9)配置文件中videoCodec参数必须配置为[VIDEO\_HEVC](../harmonyos-references/arkts-apis-media-e.md#codecmimetype8)，isHdr参数配置为true。
6. Session添加Input和Output。

   **说明** 

   Session调用preconfig接口成功之后，Session内部会将预置数据准备好，如果向Session中进行添加未配置Profile的Output，Session则会对相应的Output进行配置对应Profile。如果向Session中添加已配置Profile的Output，则Session的预配置数据不生效。

   ```ts
   async function initCamera(photoSession: camera.PhotoSession, cameraInput: camera.CameraInput,
     previewOutput: camera.PreviewOutput, photoOutput: camera.PhotoOutput) : Promise<void> {
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
     // 提交会话配置
     await photoSession.commitConfig();
   }
   ```
7. 启动Session。

   ```ts
   async function startCamera(photoSession: camera.PhotoSession) : Promise<void> {
     // 启动会话
     await photoSession.start().then(() => {
       console.info('Promise returned to indicate the session start success.');
     });
   }
   ```

## 完整示例

Context获取方式请参考：[获取UIAbility的上下文信息](uiability-usage.md#获取uiability的上下文信息)。

```ts
import { camera } from '@kit.CameraKit';
import { image } from '@kit.ImageKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo } from '@kit.CoreFileKit';
import { photoAccessHelper } from '@kit.MediaLibraryKit';

async function savePicture(buffer: ArrayBuffer, img: image.Image, context: Context): Promise<void> {
  let accessHelper: photoAccessHelper.PhotoAccessHelper = photoAccessHelper.getPhotoAccessHelper(context);
  let options: photoAccessHelper.CreateOptions = {
    title: Date.now().toString()
  };
  let photoUri: string = await accessHelper.createAsset(photoAccessHelper.PhotoType.IMAGE, 'jpg', options);
  let file: fileIo.File = fileIo.openSync(photoUri, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
  fileIo.writeSync(file.fd, buffer);
  fileIo.closeSync(file);
  await img.release();
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

async function cameraShootingCase(context: Context, surfaceId: string): Promise<void> {
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
    console.info('cameraId : ' + cameraArray[index].cameraId); // 获取相机ID
    console.info('cameraPosition : ' + cameraArray[index].cameraPosition); // 获取相机位置
    console.info('cameraType : ' + cameraArray[index].cameraType); // 获取相机类型
    console.info('connectionType : ' + cameraArray[index].connectionType); // 获取相机连接类型
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

  // 查询Preconfig能力
  try {
    let isPreconfigSupport = photoSession.canPreconfig(camera.PreconfigType.PRECONFIG_1080P);
    if (!isPreconfigSupport) {
      console.error('PhotoSession canPreconfig check fail.');
      return;
    }
  } catch (error) {
    let err = error as BusinessError;
    console.error('Failed to call canPreconfig. errorCode = ' + err.code);
    return;
  }

  // 配置Preconfig
  try {
    photoSession.preconfig(camera.PreconfigType.PRECONFIG_1080P);
  } catch (error) {
    let err = error as BusinessError;
    console.error('Failed to call preconfig. errorCode = ' + err.code);
    return;
  }

  // 创建预览输出流,其中参数 surfaceId 参考上文 XComponent 组件，预览流为XComponent组件提供的surface
  let previewOutput: camera.PreviewOutput | undefined = undefined;
  try {
    previewOutput = cameraManager.createPreviewOutput(surfaceId);
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
    photoOutput = cameraManager.createPhotoOutput();
  } catch (error) {
    let err = error as BusinessError;
    console.error('Failed to createPhotoOutput errorCode = ' + err.code);
  }
  if (photoOutput === undefined) {
    return;
  }

  // 调用上面的回调函数来保存图片
  setPhotoOutputCb(photoOutput, context);

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

  // 提交会话配置
  await photoSession.commitConfig();

  // 启动会话
  await photoSession.start().then(() => {
    console.info('Promise returned to indicate the session start success.');
  });
  // 判断设备是否支持闪光灯
  let flashStatus: boolean = false;
  try {
    flashStatus = photoSession.hasFlash();
  } catch (error) {
    let err = error as BusinessError;
    console.error('Failed to hasFlash. errorCode = ' + err.code);
  }
  console.info('Returned with the flash light support status:' + flashStatus);

  if (flashStatus) {
    // 判断是否支持自动闪光灯模式
    let flashModeStatus: boolean = false;
    try {
      let status: boolean = photoSession.isFlashModeSupported(camera.FlashMode.FLASH_MODE_AUTO);
      flashModeStatus = status;
    } catch (error) {
      let err = error as BusinessError;
      console.error('Failed to check whether the flash mode is supported. errorCode = ' + err.code);
    }
    if(flashModeStatus) {
      // 设置自动闪光灯模式
      try {
        photoSession.setFlashMode(camera.FlashMode.FLASH_MODE_AUTO);
      } catch (error) {
        let err = error as BusinessError;
        console.error('Failed to set the flash mode. errorCode = ' + err.code);
      }
    }
  }

  // 判断是否支持连续自动变焦模式
  let focusModeStatus: boolean = false;
  try {
    let status: boolean = photoSession.isFocusModeSupported(camera.FocusMode.FOCUS_MODE_CONTINUOUS_AUTO);
    focusModeStatus = status;
  } catch (error) {
    let err = error as BusinessError;
    console.error('Failed to check whether the focus mode is supported. errorCode = ' + err.code);
  }

  if (focusModeStatus) {
    // 设置连续自动变焦模式
    try {
      photoSession.setFocusMode(camera.FocusMode.FOCUS_MODE_CONTINUOUS_AUTO);
    } catch (error) {
      let err = error as BusinessError;
      console.error('Failed to set the focus mode. errorCode = ' + err.code);
    }
  }

  // 获取相机支持的可变焦距比范围
  let zoomRatioRange: Array<number> = [];
  try {
    zoomRatioRange = photoSession.getZoomRatioRange();
  } catch (error) {
    let err = error as BusinessError;
    console.error('Failed to get the zoom ratio range. errorCode = ' + err.code);
  }
  if (zoomRatioRange.length <= 0) {
    return;
  }
  // 设置可变焦距比
  try {
    photoSession.setZoomRatio(zoomRatioRange[0]);
  } catch (error) {
    let err = error as BusinessError;
    console.error('Failed to set the zoom ratio value. errorCode = ' + err.code);
  }
  let photoCaptureSetting: camera.PhotoCaptureSetting = {
    quality: camera.QualityLevel.QUALITY_LEVEL_HIGH, // 设置图片质量高
    rotation: camera.ImageRotation.ROTATION_0 // 设置图片旋转角度0
  }
  // 使用当前拍照设置进行拍照，需要在拍照时主动调用该接口拍摄图片。
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
