---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-tablet-4
title: 应用在平板设备上的拍照取景框发生了旋转
breadcrumb: FAQ > 多设备场景 > 平板 > 常见问题 > 应用在平板设备上的拍照取景框发生了旋转
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:48+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:df87fce7ffeb6aba5d68cca93e42c3447985717cd6399e9597171d48d752dd6c
---

## 问题现象

用户使用相机预览时，发现界面在手机上显示正常，但在平板上却出现了90度旋转的情况。

## 背景知识

* 开发者可以使用[PhotoCaptureSetting](../harmonyos-references/arkts-apis-camera-i.md#photocapturesetting)进行拍摄照片的设置。
* 可以对[ImageRotation](../harmonyos-references/arkts-apis-camera-e.md#imagerotation)进行设置，将预览流进行旋转。

## 问题定位

1. 检查代码中XComponent预览流组件是否设置[rotate](../harmonyos-references/ts-universal-attributes-transformation.md#rotate)属性，针对不同设备主动旋转角度调整组件方向。
2. 检查代码中是否使用[setXComponentSurfaceRotation](../harmonyos-references/ts-basic-components-xcomponent.md#setxcomponentsurfacerotation12)锁定Surface旋转方向，使其不跟随屏幕方向变化。

## 分析结论

平板的传感器方向与手机传感器方向不同，应用未手动设置rotate属性调整平板设备下XComponent组件的方向，导致在平板下，图像预览发生旋转。

## 修改建议

屏幕方向锁定，当XComponent类型为SURFACE("surface")时，使用setXComponentSurfaceRotation设置XComponent使Surface在屏幕旋转时锁定方向，不跟随屏幕进行旋转，参考代码如下，以下代码需在module.json5配置文件的requestPermissions标签中对[ohos.permission.CAMERA](../harmonyos-guides/permissions-for-all-user.md#ohospermissioncamera)相机权限进行[声明权限](../harmonyos-guides/declare-permissions.md)：

```screen
import { camera } from '@kit.CameraKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { abilityAccessCtrl, Permissions } from '@kit.AbilityKit';

@Entry
@Component
struct CameraExampleDemo {
  private xComponentCtl: XComponentController = new XComponentController();
  private xComponentSurfaceId: string = '';
  @State imageWidth: number = 1920;
  @State imageHeight: number = 1080;
  private cameraManager: camera.CameraManager | undefined = undefined;
  private cameras: Array<camera.CameraDevice> = [];
  private cameraInput: camera.CameraInput | undefined = undefined;
  private previewOutput: camera.PreviewOutput | undefined = undefined;
  private session: camera.VideoSession | undefined = undefined;
  private uiContext: UIContext = this.getUIContext();
  private context: Context | undefined = this.uiContext.getHostContext();
  private cameraPermission: Permissions = 'ohos.permission.CAMERA';
  @State isShow: boolean = false;
  private isLock: boolean = true;

  async requestPermissionsFn(): Promise<void> {
    let atManager = abilityAccessCtrl.createAtManager();
    if (this.context) {
      let res = await atManager.requestPermissionsFromUser(this.context, [this.cameraPermission]);
      for (let i = 0; i < res.permissions.length; i++) {
        if (this.cameraPermission.toString() === res.permissions[i] && res.authResults[i] === 0) {
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

  build() {
    Column() {
      if (this.isShow) {
        XComponent({
          id: 'componentId',
          type: XComponentType.SURFACE,
          controller: this.xComponentCtl
        })
          .onLoad(async () => {
            let surfaceRotation: SurfaceRotationOptions = { lock: this.isLock };
            this.xComponentCtl.setXComponentSurfaceRotation(surfaceRotation);
            this.xComponentSurfaceId = this.xComponentCtl.getXComponentSurfaceId(); // 获取组件surfaceId。
            // 初始化相机，组件实时渲染每帧预览流数据。
            this.initCamera();
          })
          .width(this.uiContext.px2vp(this.imageWidth))
          .height(this.uiContext.px2vp(this.imageHeight));
      }
    }
    .justifyContent(FlexAlign.Center)
    .height('100%')
    .width('100%');
  }

  // 初始化相机。
  async initCamera(): Promise<void> {
    console.info(`initCamera previewOutput xComponentSurfaceId:${this.xComponentSurfaceId}`);
    try {
      // 获取相机管理器实例。
      this.cameraManager = camera.getCameraManager(this.context);
      if (!this.cameraManager) {
        console.error('initCamera getCameraManager');
      }
      // 获取当前设备支持的相机device列表。
      this.cameras = this.cameraManager.getSupportedCameras();
      if (!this.cameras) {
        console.error('initCamera getSupportedCameras');
      }
      // 选择一个相机device，创建cameraInput输出对象。
      this.cameraInput = this.cameraManager.createCameraInput(this.cameras[0]);
      if (!this.cameraInput) {
        console.error('initCamera createCameraInput');
      }
      // 打开相机。
      await this.cameraInput.open().catch((err: BusinessError) => {
        console.error(`initCamera open fail: ${err}`);
      });

      // 获取相机device支持的profile。
      let capability: camera.CameraOutputCapability =
        this.cameraManager.getSupportedOutputCapability(this.cameras[0], camera.SceneMode.NORMAL_VIDEO);
      if (!capability) {
        console.error('initCamera getSupportedOutputCapability');
      }
      let minRatioDiff: number = 1;
      let surfaceRatio: number = this.imageWidth / this.imageHeight; // 最接近16:9宽高比。
      let previewProfile: camera.Profile = capability.previewProfiles[0];
      // 应用开发者根据实际业务需求选择一个支持的预览流previewProfile。
      // 此处以选择CAMERA_FORMAT_YUV_420_SP（NV21）格式、满足限定条件条件分辨率的预览流previewProfile为例。
      for (let index = 0; index < capability.previewProfiles.length; index++) {
        const tempProfile = capability.previewProfiles[index];
        let tempRatio = tempProfile.size.width >= tempProfile.size.height ?
          tempProfile.size.width / tempProfile.size.height : tempProfile.size.height / tempProfile.size.width;
        let currentRatio = Math.abs(tempRatio - surfaceRatio);
        if (currentRatio <= minRatioDiff && tempProfile.format === camera.CameraFormat.CAMERA_FORMAT_YUV_420_SP) {
          previewProfile = tempProfile;
          break;
        }
      }
      this.imageWidth = previewProfile.size.width; // 更新xComponent组件的宽。
      this.imageHeight = previewProfile.size.height; // 更新xComponent组件的高。
      // 使用xComponentSurfaceId创建预览。
      this.previewOutput = this.cameraManager.createPreviewOutput(previewProfile, this.xComponentSurfaceId);

      if (!this.previewOutput) {
        console.error('initCamera createPreviewOutput');
      }
      // 创建录像模式相机会话。
      this.session = this.cameraManager.createSession(camera.SceneMode.NORMAL_VIDEO) as camera.VideoSession;
      if (!this.session) {
        console.error('initCamera createSession');
      }
      // 开始配置会话。
      this.session.beginConfig();
      // 添加相机设备输入。
      this.session.addInput(this.cameraInput);
      // 添加预览流输出。
      this.session.addOutput(this.previewOutput);
      // 提交会话配置。
      await this.session.commitConfig();
      // 开始启动已配置的输入输出流。
      await this.session.start();

    } catch (error) {
      // 停止当前会话。
      await this.session?.stop();
      // 释放相机输入流。
      await this.cameraInput?.close();
      // 释放预览输出流。
      await this.previewOutput?.release();
      // 释放会话。
      await this.session?.release();
      console.error(`initCamera fail: ${error}`);
    }
  }

  // 释放相机。
  async releaseCamera(): Promise<void> {
    console.info('releaseCamera E');
    try {
      // 停止当前会话。
      await this.session?.stop();
      // 释放相机输入流。
      await this.cameraInput?.close();
      // 释放预览输出流。
      await this.previewOutput?.release();
      // 释放会话。
      await this.session?.release();
    } catch (error) {
      console.error(`initCamera fail: ${error}`);
    }
  }
}
```
