---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-camera-54
title: 如何实现自定义相机画面镜像效果
breadcrumb: FAQ > 媒体开发 > 拍照和图片 > 相机开发（Camera） > 如何实现自定义相机画面镜像效果
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:41+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:a8f95e9618767f7b9c46685d08a2890bf240c6aca7a361b50d862b029fb7e83c
---

## 问题现象

在使用前置摄像头拍摄时，预览画面呈现水平镜像翻转的情况，如何能使拍摄的照片和视频也呈现出镜像画面？

## 背景知识

* 前置摄像头与预览画面镜像设计：用户使用前置摄像头大多是在自拍或者视频通话等场景，镜像画面的设计能够让用户有照镜子的感觉，符合视觉习惯，同时也让用户在自拍或者视频通话时能够更顺畅地调整自己的姿势或构图，减少因左右颠倒而产生的认知冲突，增强使用的便利性。
* 拍照、录像等场景的镜像设置接口说明：

  | 场景 | 接口 | 说明 |
  | --- | --- | --- |
  | 拍照 | [isMirrorSupported（PhotoOutput）](../harmonyos-references/arkts-apis-camera-photooutput.md#ismirrorsupported) | 查询是否支持镜像拍照。 |
  | 拍照 | [PhotoCaptureSetting](../harmonyos-references/arkts-apis-camera-i.md#photocapturesetting) | 拍摄照片的设置。其中mirror属性即为镜像使能开关（默认关）。 |
  | 拍照 | [enableMirror（PhotoOutput）](../harmonyos-references/arkts-apis-camera-photooutput.md#enablemirror13) | 是否启用动态照片镜像拍照。需先调用isMirrorSupported（PhotoOutput）检查设备支持情况。 |
  | 录像 | [isMirrorSupported（VideoOutput）](../harmonyos-references/arkts-apis-camera-videooutput.md#ismirrorsupported15) | 查询是否支持镜像录像。后置镜头返回为false。 |
  | 录像 | [enableMirror（VideoOutput）](../harmonyos-references/arkts-apis-camera-videooutput.md#enablemirror15) | 启用/关闭镜像录像。需先调用isMirrorSupported（VideoOutput）检查当前设备支持情况。 |
* 在开发相机应用时，需要先[申请相关权限](../harmonyos-guides/camera-preparation.md)。

## 解决方案

HarmonyOS中，使用前置相机拍摄的照片和视频默认是非镜像的，如果希望拍摄的照片或者视频也以镜像方式呈现，则可以通过镜像使能接口来改变这一情况。本文以拍摄照片场景为例，给出镜像使能接口的实现方案，完整样例代码如下：

```ts
import { camera } from '@kit.CameraKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { abilityAccessCtrl, Permissions } from '@kit.AbilityKit';
import { photoAccessHelper } from '@kit.MediaLibraryKit';
import { PromptAction } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  private xComponentCtl: XComponentController = new XComponentController();
  private xComponentSurfaceId: string = '';
  private cameraManager: camera.CameraManager | undefined = undefined;
  private cameras: Array<camera.CameraDevice> | Array<camera.CameraDevice> = [];
  private cameraInput: camera.CameraInput | undefined = undefined;
  private previewOutput: camera.PreviewOutput | undefined = undefined;
  private photoOutput: camera.PhotoOutput | undefined = undefined;
  private session: camera.PhotoSession | undefined = undefined;
  private uiContext: UIContext = this.getUIContext();
  private context: Context | undefined = this.uiContext.getHostContext();
  private cameraPermissions: Array<Permissions> = ['ohos.permission.CAMERA', 'ohos.permission.MICROPHONE'];
  @State isShow: boolean = false;
  @State cameraPosition: camera.CameraPosition = camera.CameraPosition.CAMERA_POSITION_FRONT; // 默认使用前置摄像头
  @State isMirror: boolean = false; // 默认关闭镜像
  @State mirrorMessage: string = this.isMirror ? '镜像: on' : '镜像: off';

  async requestPermissionsFn(): Promise<void> {
    let atManager = abilityAccessCtrl.createAtManager();
    if (this.context) {
      let res = await atManager.requestPermissionsFromUser(this.context, this.cameraPermissions);
      for (let i = 0; i < res.permissions.length; i++) {
        if (this.cameraPermissions[0].toString() === res.permissions[i] &&
          res.authResults[i] === abilityAccessCtrl.GrantStatus.PERMISSION_GRANTED) {
          this.isShow = true;
        }
      }
    }
  }

  aboutToAppear(): void {
    this.requestPermissionsFn();
  }

  onPageShow(): void {
    console.info('onPageShow');
    if (this.xComponentSurfaceId !== '') {
      this.initCamera();
    }
  }

  onPageHide(): void {
    console.info('onPageHide');
    this.releaseCamera();
  }

  async requestPermissions(): Promise<void> {
    let atManager = abilityAccessCtrl.createAtManager();
    if (this.context) {
      let res = await atManager.requestPermissionOnSetting(this.context, this.cameraPermissions);
      for (let i = 0; i < res.length; i++) {
        if (res[i] === abilityAccessCtrl.GrantStatus.PERMISSION_GRANTED) {
          this.isShow = true;
        } else {
          this.isShow = false;
        }
      }
    }
  }

  build() {
    Column({ space: 20 }) {
      if (this.isShow) {
        XComponent({
          id: 'componentId',
          type: XComponentType.SURFACE,
          controller: this.xComponentCtl
        })
          .onLoad(async () => {
            console.info('onLoad is called');
            this.xComponentSurfaceId = this.xComponentCtl.getXComponentSurfaceId(); // 获取组件surfaceId。
            // 初始化相机，组件实时渲染每帧预览流数据。
            this.initCamera();
          })
          .width(300)
          .height(300)

        Button(this.mirrorMessage)
          .type(ButtonType.ROUNDED_RECTANGLE)
          .backgroundColor('#0a59f7')
          .onClick(() => {
            this.changeMirrorState();
          })
        Button('拍摄普通照片')
          .type(ButtonType.ROUNDED_RECTANGLE)
          .backgroundColor('#0a59f7')
          .onClick(() => {
            this.takePhoto();
          })
        Button('拍摄动态照片')
          .type(ButtonType.ROUNDED_RECTANGLE)
          .backgroundColor('#0a59f7')
          .onClick(() => {
            this.takeLivePhoto();
          })

      } else {
        Button('请先授予相机权限')
          .type(ButtonType.ROUNDED_RECTANGLE)
          .backgroundColor('#0a59f7')
          .onClick(() => {
            this.requestPermissions();
          });
      }
    }
    .justifyContent(FlexAlign.Center)
    .height('100%')
    .width('100%')
  }

  changeMirrorState() {
    if (!this.photoOutput?.isMirrorSupported()) { // 如果当前模式不支持镜像拍照，给出弹窗提醒
      let promptAction: PromptAction = this.uiContext.getPromptAction();
      try {
        promptAction.showDialog({
          title: '镜像拍照开启失败',
          message: '当前模式不支持开启镜像拍照！',
          buttons: [{ text: '确认', color: '#000000' }]
        }, (err, data) => {
          if (err) {
            console.error('showDialog err: ' + err);
            return;
          }
          console.info('showDialog success callback, click button: ' + data.index);
        });
      } catch (error) {
        let message = (error as BusinessError).message;
        let code = (error as BusinessError).code;
        console.error(`showdialog args error code is ${code}, message is ${message}`);
      }
      return;
    }
    this.isMirror = !this.isMirror;
    this.mirrorMessage = this.isMirror ? '镜像: on' : '镜像: off';
  }

  takePhoto() {
    if (!this.photoOutput?.isMirrorSupported()) {
      console.warn('Mirror switch is not supported on this device!');
    }
    let photoCaptureSetting: camera.PhotoCaptureSetting = {
      quality: camera.QualityLevel.QUALITY_LEVEL_HIGH, // 设置图片质量高。
      mirror: this.isMirror
    };
    this.photoOutput?.capture(photoCaptureSetting);
  }

  takeLivePhoto() {
    if (!this.photoOutput?.isMovingPhotoSupported()) {
      console.error('Moving photo is not supported on this device!');
      return;
    }
    this.photoOutput?.enableMovingPhoto(true);
    if (!this.photoOutput?.isMirrorSupported()) {
      console.warn('Mirror switch is not supported on this device!');
    } else {
      this.photoOutput?.enableMirror(this.isMirror);
    }
    this.takePhoto();
  }

  // 初始化相机。
  async initCamera(): Promise<void> {
    console.info(`initCamera previewOutput xComponentSurfaceId:${this.xComponentSurfaceId}`);
    try {
      // 获取相机管理器实例。
      this.cameraManager = camera.getCameraManager(this.context);
      if (!this.cameraManager) {
        console.error('initCamera getCameraManager');
        return;
      }
      // 获取当前设备支持的相机device列表。
      this.cameras = this.cameraManager.getSupportedCameras();
      if (!this.cameras) {
        console.error('initCamera getSupportedCameras');
      }
      // 选择一个相机device，创建cameraInput输出对象。
      let curCamera = this.cameras[0];
      for (let index = 0; index < this.cameras.length; index++) {
        const tempCamera = this.cameras[index];
        if (this.cameraPosition == tempCamera.cameraPosition) {
          curCamera = tempCamera;
          break;
        }
      }
      this.cameraInput = this.cameraManager.createCameraInput(curCamera);
      if (!this.cameraInput) {
        console.error('initCamera createCameraInput');
        return;
      }
      // 打开相机。
      await this.cameraInput.open();
      // 获取相机device支持的profile。
      let capability: camera.CameraOutputCapability =
        this.cameraManager.getSupportedOutputCapability(curCamera, camera.SceneMode.NORMAL_PHOTO);
      if (!capability || capability.previewProfiles.length === 0) {
        console.error('capability is null || []');
        this.releaseCamera();
        return;
      }
      // 应用开发者根据实际业务需求选择一个支持的预览流previewProfile。此处为简化流程选择分辨率宽高比1:1的profile，不存在时选择第一个。
      let previewProfile: camera.Profile | undefined = capability.previewProfiles.find(
        (profile) => {
          return profile.size.width === profile.size.height;
        });
      if (previewProfile === undefined) {
        previewProfile = capability.previewProfiles[0];
      }
      // 使用xComponentSurfaceId创建预览。
      this.previewOutput = this.cameraManager.createPreviewOutput(previewProfile, this.xComponentSurfaceId);
      if (!this.previewOutput) {
        console.error('initCamera createPreviewOutput');
        this.releaseCamera();
        return;
      }

      // 按照分辨率宽高比1:1来选择PhotoProfile，选不到时选择第一个。
      let photoProfile: camera.Profile | undefined = capability.photoProfiles.find(
        (profile) => {
          return profile.size.width === profile.size.height;
        });
      if (photoProfile === undefined) {
        photoProfile = capability.photoProfiles[0];
      }
      this.photoOutput = this.cameraManager.createPhotoOutput(photoProfile);
      this.photoAssesAvailable(); // 注册监听

      // 创建拍照模式相机会话。
      let session = this.cameraManager.createSession(camera.SceneMode.NORMAL_PHOTO);
      if (!session) {
        console.error('session is null');
        this.releaseCamera();
        return;
      }
      this.session = session as camera.PhotoSession;
      // 开始配置会话。
      this.session.beginConfig();
      // 添加相机设备输入。
      this.session.addInput(this.cameraInput);
      // 添加预览流输出。
      this.session.addOutput(this.previewOutput);
      // 添加拍照流输出
      this.session.addOutput(this.photoOutput);
      // 提交会话配置。
      await this.session.commitConfig();
      // 开始启动已配置的输入输出流。
      await this.session.start();
    } catch (error) {
      let err = error as BusinessError;
      console.error(`initCamera fail, err.code: ${err.code}, err.message: ${err.message}.`);
      this.releaseCamera();
    }
  }

  // 释放相机。
  async releaseCamera(): Promise<void> {
    console.info('start releaseCamera');
    // 停止当前会话。
    await this.session?.stop().catch((e: BusinessError) => {
      console.error('Failed to stop session: ', e);
    });
    // 释放相机输入流。
    await this.cameraInput?.close().catch((e: BusinessError) => {
      console.error('Failed to close the camera: ', e);
    });
    // 释放预览输出流。
    await this.previewOutput?.release().catch((e: BusinessError) => {
      console.error('Failed to stop the preview stream: ', e);
    });
    // 释放会话。
    await this.session?.release().then(() => {
      this.session = undefined;
    }).catch((e: BusinessError) => {
      console.error('Failed to release session: ', e);
    });
    console.info('end releaseCamera.');
  }

  getPhotoAccessHelper(): photoAccessHelper.PhotoAccessHelper {
    let phAccessHelper = photoAccessHelper.getPhotoAccessHelper(this.context);
    return phAccessHelper;
  }

  async mediaLibSavePhoto(photoAsset: photoAccessHelper.PhotoAsset,
    phAccessHelper: photoAccessHelper.PhotoAccessHelper): Promise<void> {
    try {
      let assetChangeRequest: photoAccessHelper.MediaAssetChangeRequest =
        new photoAccessHelper.MediaAssetChangeRequest(photoAsset);
      assetChangeRequest.saveCameraPhoto();
      await phAccessHelper.applyChanges(assetChangeRequest);
      console.info('apply saveCameraPhoto successfully');
    } catch (err) {
      console.error(`apply saveCameraPhoto failed with error: ${err.code}, ${err.message}`);
    }
  }

  photoAssesAvailable() {
    this.photoOutput?.on('photoAssetAvailable',
      (err: BusinessError, photoAsset: photoAccessHelper.PhotoAsset): void => {
        if (err) {
          console.error(`photoAssetAvailable error: ${err}.`);
          return;
        }
        console.info('photoOutPutCallBack photoAssetAvailable');
        // 调用媒体库落盘接口保存一阶段图和动态照片视频。
        this.mediaLibSavePhoto(photoAsset, this.getPhotoAccessHelper());
      });
  }
}
```

## 常见FAQ

Q：在照片拍摄的业务代码中已经调用photoOutput.enableMirror(false)禁用了镜像照片，但是实际拍摄的照片却仍然是镜像的，这是为什么？

A：普通照片拍摄时，镜像使能开关以PhotoCaptureSetting的mirror属性值为准。

Q：后置摄像头拍照和录像是否可以通过相机模块的镜像使能接口设置成镜像？

A：当前后置摄像头拍照和录像模式下均不支持设置镜像，在使用后置摄像头起流之后通过isMirrorSupported()查询接口返回的结果是false，强行调用镜像使能接口会报错。
