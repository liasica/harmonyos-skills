---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-camera-42
title: 相机连续两次调用拍照方法报错
breadcrumb: FAQ > 媒体开发 > 拍照和图片 > 相机开发（Camera） > 相机连续两次调用拍照方法报错
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:41+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:de67471fbe55b5b384ce00289b59a354e0e0a7f67326023f9cc4832780884121
---

## 问题现象

在自定义相机中，连续两次调用拍照方法，会出现如下报错：

```log
CameraService, start capture picture 1
CameraService, start capture picture 2
CameraService, capture callback 1 err: undefined
SendRequest 168: failed, handle:31 error:13 desc:IStreamCapture proxy:3130119360 time:230783611856317
{Capture():42} HStreamCaptureProxy Capture failed, error: 13
{Capture():602} PhotoOutput Failed to Capture!, errCode: 13
CameraService, capture callback 2 err: {"code":"7400102","message":""}
```

## 背景知识

* [拍照](../harmonyos-guides/camera-shooting.md)是相机的最重要功能之一，拍照模块基于相机复杂的逻辑，为了保证用户拍出的照片质量，在中间步骤可以设置分辨率、闪光灯、焦距、照片质量及旋转角度等信息。
* [on('captureReady')](../harmonyos-references/arkts-apis-camera-photooutput.md#oncaptureready12)监听可拍下一张，通过注册回调函数获取结果，使用callback异步回调。

## 问题定位

连续两次调用拍照方法的核心代码如下：

```ts
Logger.error(TAG, 'start capture picture 1');
this.photoOutput?.capture(photoSettings, (err) => {
  Logger.error(TAG, `capture callback 1 err: ${err}`);
});

Logger.error(TAG, 'start capture picture 2');
this.photoOutput?.capture(photoSettings, (err) => {
  Logger.error(TAG, `capture callback 2 err: ${err}`);
});
```

错误码7400102表示接口执行顺序错误，可以发现在代码中第二次调用capture方法时，并不能确保第一次的capture方法已经执行完毕，报错原因为两次方法同时执行造成了冲突。

## 分析结论

在调用第二次capture方法时，需要确保第一次的capture方法已经执行完毕。

## 修改建议

如需多次调用capture方法，可以对拍照输出流注册[on('captureReady')](../harmonyos-references/arkts-apis-camera-photooutput.md#oncaptureready12)监听，监听到上一次拍摄完成时再异步调用capture方法，并当拍摄次数达到规定次数后取消监听：

```ts
import { camera } from '@kit.CameraKit';
import { BusinessError, emitter } from '@kit.BasicServicesKit';
import { photoAccessHelper } from '@kit.MediaLibraryKit';
import { common } from '@kit.AbilityKit';
import { colorSpaceManager } from '@kit.ArkGraphics2D';
import { hilog } from '@kit.PerformanceAnalysisKit';

const DOMAIN: number = 0x0000;
const TAG: string = '[CameraShooterPage]';

let previewOutput: camera.PreviewOutput;
let cameraInput: camera.CameraInput;
let photoSession: camera.PhotoSession;
let photoOutPut: camera.PhotoOutput;
let currentContext: Context;
let uri: string;

export async function cameraShooting(cameraPosition: number, surfaceId: string, context: Context): Promise<void> {
  currentContext = context;
  releaseCamera();
  try {
    // 获取相机管理器对象
    let cameraManager: camera.CameraManager = camera.getCameraManager(context);
    let cameraArray: camera.CameraDevice[] = cameraManager.getSupportedCameras();
    if (cameraArray.length <= 0) {
      return;
    }
    // 创建相机输入流
    cameraInput = cameraManager.createCameraInput(cameraArray[cameraPosition]);
    await cameraInput.open();
    // 获取支持的相机模式
    let sceneModes: camera.SceneMode[] = cameraManager.getSupportedSceneModes(cameraArray[cameraPosition]);
    // 获取支持的相机输出能力
    let cameraOutputCap: camera.CameraOutputCapability =
      cameraManager.getSupportedOutputCapability(cameraArray[cameraPosition], camera.SceneMode.NORMAL_PHOTO);

    let isSupportPhotoMode: boolean = sceneModes.indexOf(camera.SceneMode.NORMAL_PHOTO) >= 0;
    if (!isSupportPhotoMode) {
      return;
    }
    if (!cameraOutputCap) {
      return;
    }

    // 获取预览流的Profile列表
    let previewProfilesArray: camera.Profile[] = cameraOutputCap.previewProfiles;
    // 选择合适的预览流分辨率，可以手动选取或通过代码选取
    let previewProfile: camera.Profile | undefined = undefined;
    for (let i = previewProfilesArray.length - 1; i >= 0; i--) {
      if (previewProfilesArray[i].size.width / previewProfilesArray[i].size.height === 4 / 3) {
        previewProfile = previewProfilesArray[i];
        break;
      }
    }

    // 创建预览输出流，surfaceId为显示组件的id
    previewOutput = cameraManager.createPreviewOutput(previewProfile, surfaceId);

    // 获取支持的拍照流profile
    let photoProfilesArray: camera.Profile[] = cameraOutputCap.photoProfiles.slice().reverse();
    let photoProfile: camera.Profile | undefined = undefined;
    if (previewProfile !== undefined) {
      // 选择与预览流分辨率宽高比一致的拍照流分辨率
      photoProfile = photoProfilesArray.find((profile: camera.Profile) => {
        return profile.size.height * previewProfile!.size.width === previewProfile!.size.height * profile.size.width;
      });
    }

    if (previewOutput === undefined) {
      return;
    }
    // 创建拍照输出流
    photoOutPut = cameraManager.createPhotoOutput(photoProfile);
    if (photoOutPut === undefined) {
      return;
    }
    // 将图片保存至媒体库
    setPhotoOutputCb(photoOutPut);
    // 创建相机会话
    photoSession = cameraManager.createSession(camera.SceneMode.NORMAL_PHOTO) as camera.PhotoSession;
    if (photoSession === undefined) {
      return;
    }
    // 开始相机会话
    photoSession.beginConfig();
    photoSession.addInput(cameraInput);
    photoSession.addOutput(previewOutput);
    photoSession.addOutput(photoOutPut);
    photoSession.setColorSpace(colorSpaceManager.ColorSpace.DISPLAY_P3);
    await photoSession.commitConfig();
    await photoSession.start();
  } catch (error) {
    hilog.error(DOMAIN, TAG, `The cameraShooting call failed. error: ${JSON.stringify(error)}`);
  }
}

// 拍照函数
export async function capture(isFront: boolean) {
  try {
    // 拍照输出设置
    let settings: camera.PhotoCaptureSetting = {
      quality: camera.QualityLevel.QUALITY_LEVEL_HIGH,
      rotation: camera.ImageRotation.ROTATION_0,
      mirror: isFront
    };
    photoOutPut.capture(settings);
  } catch (error) {
    hilog.error(DOMAIN, TAG, `The capture call failed. error: ${error.code}`);
  }
}

// 连拍设置函数
export async function burstCapture(isFront: boolean, captureCount: number) {
  await capture(isFront);
  let currCount = 1;
  photoOutPut.on('captureReady', async () => {
    await capture(isFront);
    currCount++;
    if (currCount >= captureCount) {
      emitter.emit('burstCaptureOff');
    }
  });
  emitter.once('burstCaptureOff', () => {
    photoOutPut.off('captureReady');
  });
}

// 相机相关资源释放
export async function releaseCamera(): Promise<void> {
  try {
    if (photoSession) {
      photoSession.stop();
    }
    if (cameraInput) {
      cameraInput.close();
    }
    if (previewOutput) {
      previewOutput.release();
    }
    if (photoSession) {
      photoSession.release();
    }
    if (photoOutPut) {
      emitter.off('burstCaptureOff');
      photoOutPut.off('photoAssetAvailable');
      photoOutPut.off('captureReady');
      photoOutPut.release();
    }
  } catch (error) {
    hilog.error(DOMAIN, TAG, `The releaseCamera call failed. error: ${error.code}`);
  }
}

// 将拍照图片保存至媒体库
function setPhotoOutputCb(photoOutput: camera.PhotoOutput): void {
  photoOutput.on('photoAssetAvailable',
    async (_err: BusinessError, photoAsset: photoAccessHelper.PhotoAsset): Promise<void> => {
      let accessHelper: photoAccessHelper.PhotoAccessHelper =
        photoAccessHelper.getPhotoAccessHelper(currentContext);
      let assetChangeRequest: photoAccessHelper.MediaAssetChangeRequest =
        new photoAccessHelper.MediaAssetChangeRequest(photoAsset);
      try {
        assetChangeRequest.saveCameraPhoto();
        await accessHelper.applyChanges(assetChangeRequest);
        uri = photoAsset.uri;
        AppStorage.setOrCreate('photoUri', await photoAsset.getThumbnail());
      } catch (error) {
        hilog.error(DOMAIN, TAG, `The setPhotoOutputCb call failed. error: ${error.code}`);
      }
    });
}

// 预览照片
export function previewPhoto(context: Context): void {
  let photoContext = context as common.UIAbilityContext;
  photoContext.startAbility({
    parameters: { uri: uri },
    action: 'ohos.want.action.viewData',
    bundleName: 'com.huawei.hmos.photos',
    abilityName: 'com.huawei.hmos.photos.MainAbility'
  }, (err: BusinessError) => {
    hilog.error(DOMAIN, TAG, `The previewPhoto call failed. error: ${err.code}`);
  });
}
```

主页面的代码示例参考如下：

```ts
import { dataSharePredicates } from '@kit.ArkData';
import { abilityAccessCtrl, Permissions } from '@kit.AbilityKit';
import { camera } from '@kit.CameraKit';
import { photoAccessHelper } from '@kit.MediaLibraryKit';
import { filePreview } from '@kit.PreviewKit';
import { curves, display } from '@kit.ArkUI';
import { hilog } from '@kit.PerformanceAnalysisKit';
import {
  cameraShooting, burstCapture, previewPhoto,
} from '../utils/CameraShooter';

const DOMAIN: number = 0x0000;
const TAG: string = '[XComponentPage]';

let cameraPosition = 0;
let surfaceId = '';
let storage = new LocalStorage();
// 需要连续拍摄的照片个数
let picturesTaken: number = 3;
// 设备显示屏的宽度
let displayWidth: number = display.getDefaultDisplaySync().width;

@Component
@Entry(storage)
export struct Index {
  @StorageLink('photoUri') photoUri: string | Resource | PixelMap = '';
  @State context: Context = this.getUIContext().getHostContext()!;
  mXComponentController: XComponentController = new XComponentController;
  permissions: Array<Permissions> = [
    'ohos.permission.CAMERA',
  ];
  private isFront: boolean = false;

  onPageShow(): void {
    filePreview.closePreview(this.context);
  }

  async aboutToAppear() {
    try {
      abilityAccessCtrl.createAtManager().requestPermissionsFromUser(this.context, this.permissions).then(() => {
        setTimeout(async () => {
          cameraShooting(cameraPosition, surfaceId, this.context);
        }, 200);
      });
    } catch (error) {
      hilog.error(DOMAIN, TAG, `The updatePreview call failed. error: ${JSON.stringify(error)}`);
    }
  }

  build() {
    RelativeContainer() {
      // 主视图页面
      XComponent({
        type: XComponentType.SURFACE,
        controller: this.mXComponentController
      })
        .onLoad(async () => {
          this.mXComponentController.setXComponentSurfaceRotation({ lock: true });
          this.mXComponentController.setXComponentSurfaceRect({
            surfaceWidth: displayWidth,
            surfaceHeight: displayWidth * 4 / 3
          });
          surfaceId = this.mXComponentController.getXComponentSurfaceId();
        })

      // 拍摄完后显示缩略图
      Row() {
        Image(this.photoUri)
          .borderWidth(this.photoUri === '' ? 0 : 1)
          .borderColor(Color.White)
          .height(50)
          .width(50)
          .borderRadius(25)
          .animation({ curve: curves.springMotion() })
          .onClick(() => {
            if (this.photoUri !== '') {
              previewPhoto(this.context);
            }
          })

        Image($r('app.media.capture'))
          .height(50)
          .onClick(() => {
            // isFront为是否摄像头是否前置，picturesTaken为连续调用capture的次数
            burstCapture(this.isFront, picturesTaken);
          })

        // 前后摄像头切换
        Image($r('app.media.switch_camera'))
          .height(50)
          .animation({ curve: curves.springMotion() })
          .onClick(async () => {
            cameraPosition = cameraPosition === camera.CameraPosition.CAMERA_POSITION_BACK ?
            camera.CameraPosition.CAMERA_POSITION_UNSPECIFIED : camera.CameraPosition.CAMERA_POSITION_BACK;
            cameraShooting(cameraPosition, surfaceId, this.context);
          })
      }
      .id('controlPanel')
      .width('100%')
      .justifyContent(FlexAlign.SpaceAround)
      .alignRules({
        bottom: { anchor: '__container__', align: VerticalAlign.Bottom }
      })
      .margin({ bottom: '60vp' })
    }
    .height('100%')
    .backgroundColor('#000000')
  }

  // 获取照片的缩略图
  async getThumbnail(): Promise<void> {
    let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
    predicates.orderByDesc(photoAccessHelper.PhotoKeys.DATE_ADDED);
    let fetchOptions: photoAccessHelper.FetchOptions = {
      fetchColumns: [],
      predicates: predicates
    };
    let photoHelper = photoAccessHelper.getPhotoAccessHelper(this.context);
    try {
      let fetchResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> =
        await photoHelper.getAssets(fetchOptions);
      if (fetchResult !== undefined) {
        let photoAsset: photoAccessHelper.PhotoAsset = await fetchResult.getFirstObject();
        this.photoUri = await photoAsset.getThumbnail();
      }
    } catch (error) {
      hilog.error(DOMAIN, TAG, `The getThumbnail call failed. error: ${JSON.stringify(error)}`);
    }
  }
}

export async function fromBack(context: Context): Promise<void> {
  cameraShooting(cameraPosition, surfaceId, context);
}
```
