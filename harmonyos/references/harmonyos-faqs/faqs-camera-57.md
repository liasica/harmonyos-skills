---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-camera-57
title: 如何使自定义相机完成对焦后拍照
breadcrumb: FAQ > 媒体开发 > 拍照和图片 > 相机开发（Camera） > 如何使自定义相机完成对焦后拍照
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:41+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:fcbb691795661208d9d5ffa275b8321454550149c9df9cbfe98b8d77a90139c5
---

## 问题现象

使用自定义相机实现扫码组件，在识别到条形码后触发拍照，相机对焦模式设置为FOCUS\_MODE\_CONTINUOUS\_AUTO（连续自动对焦），有时会出现拍照模糊的情况。如何实现扫码后对焦完成自动拍照，使拍照结果清晰？

## 背景知识

* 在开发相机应用时，需要先申请相机相关权限，确保应用拥有访问相机硬件及其他功能的权限，具体可参考[申请相机开发的权限](../harmonyos-guides/camera-preparation.md)。
* 可以注册[on('focusStateChange')](../harmonyos-references/arkts-apis-camera-photosession.md#onfocusstatechange11)事件监听相机聚焦的状态变化，仅在对焦模式设置为自动对焦模式，并设置对焦点后，触发该事件。具体可参考：[对焦](../harmonyos-guides/camera-focus.md)。

## 解决方案

在扫码完成后，将相机对焦模式设置为FOCUS\_MODE\_AUTO（自动对焦），通过[setFocusPoint](../harmonyos-references/arkts-apis-camera-focus.md#setfocuspoint11)接口设置对焦点为条形码中心，注册[focusStateChange](../harmonyos-references/arkts-apis-camera-photosession.md#onfocusstatechange11)事件，监听焦点状态变化，确保对焦成功后，触发拍照，相关代码如下：

```ts
let focusModeStatus: boolean = false;
try {
  // photoSession为相机会话。
  focusModeStatus = resources.photoSession.isFocusModeSupported(camera.FocusMode.FOCUS_MODE_AUTO);
} catch (err) {
  console.error('failed to check whether the focus mode is supported: ' + JSON.stringify(err));
}
if (focusModeStatus) {
  const focusPoint: camera.Point = { x: 0.5, y: 0.5 };
  try {
    // 设置对焦模式为自动对焦。
    resources.photoSession.setFocusMode(camera.FocusMode.FOCUS_MODE_AUTO);
    // 设置对焦点为条形码中心。
    resources.photoSession.setFocusPoint(focusPoint);
    console.info(`succeed in set focus mode`);
  } catch (err) {
    console.error(`failed to set the focus mode: ${JSON.stringify(err)}`);
  }
}

let focusStatePrev = camera.FocusState.FOCUS_STATE_SCAN; // 上一次对焦状态。
// 监听焦点变化事件。
resources.photoSession.on('focusStateChange', async (err: BusinessError, focusState: camera.FocusState) => {
  if (err !== undefined && err.code !== 0) {
    console.error(`focus status change error: ${JSON.stringify(err)}`);
    return;
  }
  // 上一次对焦状态为触发对焦，当前对焦状态为对焦成功，此时完成对焦。
  if (focusStatePrev === camera.FocusState.FOCUS_STATE_SCAN &&
    focusState === camera.FocusState.FOCUS_STATE_FOCUSED) {
    await resources.photoOutput!.capture(); // 触发拍照。
  }
  focusStatePrev = focusState;
});
```

完整代码如下：

```ts
import { camera } from '@kit.CameraKit';
import { image } from '@kit.ImageKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { abilityAccessCtrl, common, Permissions } from '@kit.AbilityKit';

const permissions: Array<Permissions> = ['ohos.permission.CAMERA'];

async function reqPermissionsFromUser(permissions: Array<Permissions>, context: common.UIAbilityContext) {
  let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
  try {
    await atManager.requestPermissionsFromUser(context, permissions);
  } catch (err) {
    console.error(`request permissions from user failed, ${JSON.stringify(err)}`);
  }
}

interface ShootingResources {
  cameraInput?: camera.CameraInput;
  previewOutput?: camera.PreviewOutput;
  photoOutput?: camera.PhotoOutput;
  photoSession?: camera.PhotoSession;
}

const resources: ShootingResources = {};

function setPhotoOutputCb(photoOutput: camera.PhotoOutput): void {
  if (!photoOutput) {
    console.error('photoOutput is null');
    return;
  }
  // 设置回调之后，调用photoOutput的capture方法，就会将拍照的buffer回传到回调中。
  photoOutput?.on('photoAvailable', (err: BusinessError, photo: camera.Photo): void => {
    console.info('getPhoto start');
    if (err && err.code !== 0) {
      console.error('getPhoto failed');
      return;
    }
    if (!photo || !photo.main) {
      console.error('photo is null');
      return;
    }
    let imageObj = photo.main;
    imageObj.getComponent(image.ComponentType.JPEG,
      async (errCode: BusinessError, component: image.Component) => {
        console.info('getComponent start');
        if (errCode && errCode.code !== 0) {
          console.error('getComponent failed');
          imageObj.release();
          return;
        }
        let buffer: ArrayBuffer;
        if (component && component.byteBuffer) {
          buffer = component.byteBuffer;
        } else {
          console.error('byteBuffer is null');
          imageObj.release();
          return;
        }
        // 如需要在图库中看到所保存的图片、视频资源，请使用用户无感的安全控件创建媒体资源。
        let imageSource = image.createImageSource(buffer);
        let pixelMap = await imageSource.createPixelMap();
        AppStorage.setOrCreate('PixelMap', pixelMap);

        // buffer处理结束后需要释放该资源，如果未正确释放资源会导致后续拍照获取不到buffer。
        imageObj.release();
      });
  });
}

async function cameraShootingCase(context: Context, surfaceId: string): Promise<void> {
  try {
    // 创建CameraManager对象。
    let cameraManager: camera.CameraManager = camera.getCameraManager(context);
    if (!cameraManager) {
      console.error('camera.getCameraManager error');
      return;
    }

    // 监听相机状态变化。
    cameraManager.on('cameraStatus', (err: BusinessError, cameraStatusInfo: camera.CameraStatusInfo) => {
      if (err !== undefined && err.code !== 0) {
        console.error('cameraStatus with errorCode = ' + err.code);
        return;
      }
      console.info(`camera : ${cameraStatusInfo.camera.cameraId}`);
      console.info(`status: ${cameraStatusInfo.status}`);
    });

    // 获取相机列表。
    let cameraArray: Array<camera.CameraDevice> = cameraManager.getSupportedCameras();
    if (!cameraArray || cameraArray.length <= 0) {
      console.error('cameraManager.getSupportedCameras error');
      return;
    }

    for (let index = 0; index < cameraArray.length; index++) {
      console.info('cameraId : ' + cameraArray[index].cameraId); // 获取相机ID。
      console.info('cameraPosition : ' + cameraArray[index].cameraPosition); // 获取相机位置。
      console.info('cameraType : ' + cameraArray[index].cameraType); // 获取相机类型。
      console.info('connectionType : ' + cameraArray[index].connectionType); // 获取相机连接类型。
    }

    // 创建相机输入流。
    resources.cameraInput = cameraManager.createCameraInput(cameraArray[0]);
    if (!resources.cameraInput) {
      console.error('cameraInput is null');
      return;
    }

    // 监听cameraInput错误信息。
    let cameraDevice: camera.CameraDevice = cameraArray[0];
    resources.cameraInput.on('error', cameraDevice, (error: BusinessError) => {
      console.error(`Camera input error code: ${error.code}`);
    });

    // 打开相机。
    await resources.cameraInput.open();

    // 获取支持的模式类型。
    let sceneModes: Array<camera.SceneMode> = cameraManager.getSupportedSceneModes(cameraArray[0]);
    let isSupportPhotoMode: boolean = sceneModes.indexOf(camera.SceneMode.NORMAL_PHOTO) >= 0;
    if (!isSupportPhotoMode) {
      console.error('photo mode not support');
      releaseResources();
      return;
    }

    // 获取相机设备支持的输出流能力。
    let cameraOutputCap: camera.CameraOutputCapability =
      cameraManager.getSupportedOutputCapability(cameraArray[0], camera.SceneMode.NORMAL_PHOTO);
    if (!cameraOutputCap) {
      console.error('cameraManager.getSupportedOutputCapability error');
      return;
    }
    console.info('outputCapability: ' + JSON.stringify(cameraOutputCap));

    let previewProfilesArray: Array<camera.Profile> = cameraOutputCap.previewProfiles;
    if (!previewProfilesArray || previewProfilesArray.length <= 0) {
      console.error('previewProfilesArray is null or []');
      releaseResources();
      return;
    }

    let photoProfilesArray: Array<camera.Profile> = cameraOutputCap.photoProfiles;
    if (!photoProfilesArray || photoProfilesArray.length <= 0) {
      console.error('photoProfilesArray is null or []');
      releaseResources();
      return;
    }

    // 创建预览输出流，其中参数surfaceId参考上文XComponent组件，预览流为XComponent组件提供的surface。
    resources.previewOutput = cameraManager.createPreviewOutput(previewProfilesArray[0], surfaceId);
    if (!resources.previewOutput) {
      console.error('previewOutput is null');
      releaseResources();
      return;
    }
    try {
      // 监听预览输出错误信息。
      resources.previewOutput.on('error', (error: BusinessError) => {
        console.error(`Preview output error code: ${error.code}`);
      });
    } catch (e) {
      console.error(`previewOutput.on call failed, error: ${JSON.stringify(e)}`);
    }

    // 创建拍照输出流。
    resources.photoOutput = cameraManager.createPhotoOutput(photoProfilesArray[0]);
    if (!resources.photoOutput) {
      console.error('photoOutput is null');
      releaseResources();
      return;
    }

    // 调用上面的回调函数来展示图片。
    setPhotoOutputCb(resources.photoOutput);

    // 创建会话。
    let photoSession = cameraManager.createSession(camera.SceneMode.NORMAL_PHOTO);
    if (!photoSession) {
      console.error('photoSession is null');
      releaseResources();
      return;
    }
    resources.photoSession = photoSession as camera.PhotoSession;
    try {
      // 监听session错误信息。
      resources.photoSession.on('error', (error: BusinessError) => {
        console.error(`Capture session error code: ${error.code}`);
      });
    } catch (e) {
      console.error(`photoSession.on call failed, error: ${JSON.stringify(e)}`);
    }

    // 开始配置会话。
    resources.photoSession.beginConfig();

    // 向会话中添加相机输入流。
    resources.photoSession.addInput(resources.cameraInput);

    // 向会话中添加预览输出流。
    resources.photoSession.addOutput(resources.previewOutput);

    // 向会话中添加拍照输出流。
    resources.photoSession.addOutput(resources.photoOutput);

    // 提交会话配置。
    await resources.photoSession.commitConfig();

    // 启动会话。
    await resources.photoSession.start();
    // 判断设备是否支持闪光灯。
    let flashStatus: boolean = false;
    flashStatus = resources.photoSession.hasFlash();
    console.info('Returned with the flash light support status:' + flashStatus);

    if (flashStatus) {
      // 判断是否支持自动闪光灯模式。
      let flashModeStatus: boolean = resources.photoSession.isFlashModeSupported(camera.FlashMode.FLASH_MODE_AUTO);
      if (flashModeStatus) {
        // 设置自动闪光灯模式。
        resources.photoSession.setFlashMode(camera.FlashMode.FLASH_MODE_AUTO);
      }
    }
    let focusModeStatus: boolean = false;
    try {
      // photoSession为相机会话。
      focusModeStatus = resources.photoSession.isFocusModeSupported(camera.FocusMode.FOCUS_MODE_AUTO);
    } catch (err) {
      console.error('failed to check whether the focus mode is supported: ' + JSON.stringify(err));
    }
    if (focusModeStatus) {
      const focusPoint: camera.Point = { x: 0.5, y: 0.5 };
      try {
        // 设置对焦模式为自动对焦。
        resources.photoSession.setFocusMode(camera.FocusMode.FOCUS_MODE_AUTO);
        // 设置对焦点为条形码中心。
        resources.photoSession.setFocusPoint(focusPoint);
        console.info(`succeed in set focus mode`);
      } catch (err) {
        console.error(`failed to set the focus mode: ${JSON.stringify(err)}`);
      }
    }

    let focusStatePrev = camera.FocusState.FOCUS_STATE_SCAN; // 上一次对焦状态。
    // 监听焦点变化事件。
    resources.photoSession.on('focusStateChange', async (err: BusinessError, focusState: camera.FocusState) => {
      if (err !== undefined && err.code !== 0) {
        console.error(`focus status change error: ${JSON.stringify(err)}`);
        return;
      }
      // 上一次对焦状态为触发对焦，当前对焦状态为对焦成功，此时完成对焦。
      if (focusStatePrev === camera.FocusState.FOCUS_STATE_SCAN &&
        focusState === camera.FocusState.FOCUS_STATE_FOCUSED) {
        await resources.photoOutput!.capture(); // 触发拍照。
      }
      focusStatePrev = focusState;
    });

    // 会话置空。
    resources.photoSession = undefined;
  } catch (error) {
    console.error(`cameraShootingCase call failed, error: ${JSON.stringify(error)}`);
    releaseResources();
  }
}

async function releaseResources(): Promise<void> {
  // 停止当前会话。
  await resources.photoSession?.stop().catch((e: BusinessError) => {
    console.error('photoSession stop failed: ', e);
  });

  // 释放相机输入流。
  await resources.cameraInput?.close().catch((e: BusinessError) => {
    console.error('cameraInput close failed: ', e);
  });

  // 释放预览输出流。
  await resources.previewOutput?.release().catch((e: BusinessError) => {
    console.error('previewOutput release failed: ', e);
  });

  // 释放拍照输出流。
  await resources.photoOutput?.release().catch((e: BusinessError) => {
    console.error('photoOutput release failed: ', e);
  });

  // 释放会话。
  await resources.photoSession?.release().catch((e: BusinessError) => {
    console.error('photoSession release failed: ', e);
  });
}

@Entry
@Component
struct Index {
  @StorageLink('PixelMap') pixelMap: image.PixelMap | undefined = undefined;
  private mXComponentCtrl: XComponentController = new XComponentController();

  aboutToAppear(): void {
    let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
    reqPermissionsFromUser(permissions, context);
  }

  build() {
    Column({ space: 40 }) {
      Image(this.pixelMap)
        .width('50%')
        .aspectRatio(1)
        .backgroundColor(Color.Black)

      XComponent({
        type: XComponentType.SURFACE,
        controller: this.mXComponentCtrl,
      })
        .width('50%')
        .aspectRatio(1)
        .renderFit(RenderFit.RESIZE_CONTAIN)

      Button() {
        Text('拍照')
          .padding(10)
          .fontSize(30);
      }
      .onClick(() => {
        let surfaceId = this.mXComponentCtrl.getXComponentSurfaceId();
        let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
        cameraShootingCase(context, surfaceId);
      });
    }
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.Center)
  }
}
```
