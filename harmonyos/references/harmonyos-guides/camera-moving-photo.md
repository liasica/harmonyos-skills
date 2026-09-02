---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/camera-moving-photo
title: 动态照片拍摄(ArkTS)
breadcrumb: 指南 > 媒体 > Camera Kit（相机服务） > 开发相机应用基础能力(ArkTS) > 动态照片拍摄(ArkTS)
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:45+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:7753fe61070f32fca3d46d2c55fd99aa5d456309a2384f9462308e2ff23b35eb
---

相机框架提供动态照片拍摄能力，业务应用可以类似拍摄普通照片一样，一键式拍摄得到动态照片。

应用开发动态照片主要分为以下步骤：

* 应用开发动态照片前，请参考[申请相机开发的权限](camera-preparation.md)、[相机管理](camera-device-management.md)、[设备输入](camera-device-input.md)、[会话管理](camera-session-management.md)等流程完成相机应用开发必选能力配置。
* 查询当前设备的当前模式是否支持拍摄动态照片。
* 如果支持动态照片，可以调用相机框架提供的使能接口**使能**动态照片能力。
* 监听照片回调，将照片存入媒体库。可参考[MediaLibrary Kit-访问和管理动态照片资源](photoaccesshelper-movingphoto.md)。

## 开发步骤

详细的API说明请参考[@ohos.multimedia.camera (相机管理)](../harmonyos-references/arkts-apis-camera.md)。

**说明** 

* 拍摄动态照片需要麦克风权限ohos.permission.MICROPHONE，权限申请和校验的方式请参考[开发准备](camera-preparation.md)。否则拍摄的照片没有声音。

1. 导入依赖，需要导入相机框架、媒体库、图片相关领域依赖。

   ```ts
   import { camera } from '@kit.CameraKit';
   import { photoAccessHelper } from '@kit.MediaLibraryKit';
   import { BusinessError } from '@kit.BasicServicesKit';
   ```
2. 确定拍照输出流。

   通过[CameraOutputCapability](../harmonyos-references/arkts-apis-camera-i.md#cameraoutputcapability)中的photoProfiles属性，可获取当前设备支持的拍照输出流，通过[createPhotoOutput](../harmonyos-references/arkts-apis-camera-cameramanager.md#createphotooutput11)方法创建拍照输出流。

   ```typescript
   getPhotoOutput(cameraManager: camera.CameraManager,
     cameraOutputCapability: camera.CameraOutputCapability): camera.PhotoOutput | undefined {
     let photoProfilesArray: camera.Profile[] = cameraOutputCapability.photoProfiles;
     if (!photoProfilesArray || photoProfilesArray.length === 0) {
       console.error('photoProfilesArray is null or []');
     }
     let photoOutput: camera.PhotoOutput | undefined = undefined;
     try {
       this.photoProfileObj = photoProfilesArray[0]
       photoOutput = cameraManager.createPhotoOutput(photoProfilesArray[0]);
     } catch (error) {
       let err = error as BusinessError;
       console.error(`Failed to createPhotoOutput. error: ${err}`);
     }
     return photoOutput;
   }
   ```
3. 查询当前设备当前模式是否支持动态照片能力。

   **说明** 

   查询是否支持动态照片前需要先完成相机会话配置、提交和启动会话，详细开发步骤请参考[会话管理](camera-session-management.md)。

   ```typescript
   isMovingPhotoSupported(): boolean {
     let isSupported: boolean = false;
     try {
       if (this.photoOutput == undefined) {
         console.error(`photoOutput is nullptr.`);
         return false;
       }
       isSupported = this.photoOutput.isMovingPhotoSupported();
     } catch (error) {
       // 失败返回错误码error.code并处理。
       let err = error as BusinessError;
       console.error(`The isMovingPhotoSupported call failed. error code: ${err.code}`);
     }
     return isSupported;
   }
   ```
4. 使能动态照片拍照能力。

   **说明** 

   使能动态照片前需要使能[分段式拍照](camera-deferred-capture.md)能力。

   ```typescript
   enableMovingPhoto(enable: boolean): void {
     try {
       if (this.photoOutput != undefined) {
         console.info(TAG, `enableMovingPhoto: ${enable}`);
         this.photoOutput.enableMovingPhoto(enable);
       }
     } catch (error) {
       // 失败返回错误码error.code并处理。
       let err = error as BusinessError;
       console.error(`The enableMovingPhoto call failed. error code: ${err.code}`);
     }
   }
   ```
5. 触发拍照，与普通拍照方式相同，请参考[拍照](camera-shooting.md)。

## 状态监听

在相机应用开发过程中，可以随时监听动态照片拍照输出流状态。通过注册photoAsset的回调函数获取监听结果，photoOutput创建成功时即可监听。

```typescript
onPhotoOutputPhotoAssetAvailable(photoOutput: camera.PhotoOutput, context: Context): void {
  photoOutput.on('photoAssetAvailable', (err: BusinessError, photoAsset: photoAccessHelper.PhotoAsset) => {
    if (err) {
      console.error(`photoAssetAvailable error: ${err}.`);
      return;
    }
    console.info('photoOutputCallBack photoAssetAvailable');
    // 开发者可通过photoAsset调用媒体库相关接口，自定义处理图片。
    // 处理方式一：调用媒体库落盘接口保存一阶段图，二阶段图就绪后媒体库会主动帮应用替换落盘图片。
    let accessHelper: photoAccessHelper.PhotoAccessHelper =
      photoAccessHelper.getPhotoAccessHelper(this.context);
    this.mediaLibSavePhoto(photoAsset, accessHelper);
    // 处理方式二：调用媒体库接口请求图片并注册一阶段图或二阶段图buffer回调，自定义使用。
    this.mediaLibRequestBuffer(photoAsset, context, this.callback);
  });
}

async mediaLibSavePhoto(photoAsset: photoAccessHelper.PhotoAsset,
  phAccessHelper: photoAccessHelper.PhotoAccessHelper): Promise<void> {
  try {
    let assetChangeRequest: photoAccessHelper.MediaAssetChangeRequest =
      new photoAccessHelper.MediaAssetChangeRequest(photoAsset);
    assetChangeRequest.saveCameraPhoto();
    await phAccessHelper.applyChanges(assetChangeRequest);
    phAccessHelper.release().catch(() => {
      console.error(`release failed.`);
    });
  } catch (error) {
    Logger.error(`apply saveCameraPhoto failed with error: ${error.code}, ${error.message}`);
  }
}

async mediaLibRequestBuffer(photoAsset: photoAccessHelper.PhotoAsset, context: Context,
  callback: (pixelMap: image.PixelMap, url: string) => void) {
  class MediaDataHandler implements photoAccessHelper.MediaAssetDataHandler<ArrayBuffer> {
    onDataPrepared(data: ArrayBuffer) {
      if (data === undefined) {
        Logger.error('Error occurred when preparing data');
        return;
      }
      let imageSource = image.createImageSource(data);
      imageSource.createPixelMap().then((pixelMap: image.PixelMap) => {
        callback(pixelMap, photoAsset.uri);
      }).catch((err: BusinessError) => {
        Logger.error(`createPixelMap err:${err.code}`);
      })
    }
  }

  let requestOptions: photoAccessHelper.RequestOptions = {
    deliveryMode: photoAccessHelper.DeliveryMode.FAST_MODE,
  }
  const handler = new MediaDataHandler();
  try {
    await photoAccessHelper.MediaAssetManager.requestImageData(context, photoAsset, requestOptions, handler);
  } catch (error) {
    console.error(`requestImageData failed, err: ${error.code}`);
  }
}
```

## HDR动态照片

从API version 23开始，相机提供HDR动态照片拍摄能力，即组成动态照片的静态图片与动态短视频均为高动态范围（HDR）内容，能够在高光与暗部细节、色彩层次和整体质感方面优于SDR成片效果。

应用可以通过配置预览输出格式（Profile.format）和色彩空间（ColorSpace）灵活决定输出SDR/HDR动态照片。具体对应关系如下表所示，所有能力需先查后用，支持的预览输出格式通过接口[getSupportedFullOutputCapability](../harmonyos-references/arkts-apis-camera-cameramanager.md#getsupportedfulloutputcapability23)查询，支持的色彩空间通过接口[getSupportedColorSpaces](../harmonyos-references/arkts-apis-camera-colormanagementquery.md#getsupportedcolorspaces12)查询。

| 静图动态范围 | 短视频动态范围 | 预览输出格式 | 色彩空间 |
| --- | --- | --- | --- |
| SDR | SDR | CAMERA\_FORMAT\_YUV\_420\_SP | SRGB |
| HDR | SDR | CAMERA\_FORMAT\_YUV\_420\_SP | DISPLAY\_P3 |
| HDR | HDR | CAMERA\_FORMAT\_YCRCB\_P010、  CAMERA\_FORMAT\_YCBCR\_P010 | BT2020\_HLG |

**HDR配置说明**

* 在配置预览输出流时，需要先通过接口[getSupportedFullOutputCapability](../harmonyos-references/arkts-apis-camera-cameramanager.md#getsupportedfulloutputcapability23)查询当前镜头和模式支持的完整能力，选择的预览输出格式为P010（CAMERA\_FORMAT\_YCRCB\_P010/CAMERA\_FORMAT\_YCBCR\_P010）。
* 在配置色彩空间时，需要先通过接口[getSupportedColorSpaces](../harmonyos-references/arkts-apis-camera-colormanagementquery.md#getsupportedcolorspaces12)获取当前设备所支持的色彩空间，再通过接口[setColorSpace](../harmonyos-references/arkts-apis-camera-colormanagement.md#setcolorspace12)设置色彩空间为BT2020\_HLG。具体请参考[setColorSpace](../harmonyos-references/arkts-apis-camera-colormanagement.md#setcolorspace12)说明。
