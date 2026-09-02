---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-camera-33
title: 如何正确关闭释放相机流
breadcrumb: FAQ > 媒体开发 > 拍照和图片 > 相机开发（Camera） > 如何正确关闭释放相机流
category: harmonyos-faqs
scraped_at: 2026-09-02T15:04:18+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:7545aa7073ca2de696efd4adc688d69a04e95671df78dff38d69158bddc25bb5
---

## 问题现象

在自定义相机开发中，由于开发者未能正确关闭或释放相机流，经常会出现各种错误，如关闭相机阻塞、日志报错、拍照回调不触发或者获取数据为空等。

## 背景知识

相机拍照流程一般分为获取相机管理器和相机设备、创建相机输入流、获取相机输出能力、创建相机预览输出流、创建拍照输出流、设置拍照回调、创建并配置相机会话、启动相机会话、触发拍照、保存图片、释放资源等流程，流程之间存在依赖关系，具体开发流程可参考[拍照（ArkTS）](../harmonyos-guides/camera-shooting.md)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1/v3/RESBg2EAR5SOKyoUmg1Gbw/zh-cn_image_0000002628552468.png "点击放大")

## 解决方案

* 若相机错误码为[7400109](../harmonyos-references/errorcode-camera.md#section7400109-相机设备被抢占)，表示相机设备被抢占导致无法使用相机，可能原因是由于之前的相机流未能正确关闭或释放导致同时打开2个相同摄像头。需要在创建CameraManager对象前对之前的相机流进行释放，参考代码如下：

  ```ts
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
  ```
* 若相机应用首次打开应用黑屏，或退到后台后再切到前台预览画面停止，则需要检查是否在页面的各生命周期正确释放相机流或初始化相机，核心代码如下：

  ```ts
  async requestPermissionsFn(): Promise<void> {
    let atManager = abilityAccessCtrl.createAtManager();
    if (this.context) {
      let res = await atManager.requestPermissionsFromUser(this.context, [this.cameraPermission]);
      for (let i = 0; i < res.permissions.length; i++) {
        if (this.cameraPermission.toString() === res.permissions[i] &&
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
  ```
* 在不同相机镜头进行切换时，也需要释放相机流：

  ```ts
  async changeCameraPosition() {
    await this.releaseCamera();
    this.cameraPosition = this.cameraPosition === camera.CameraPosition.CAMERA_POSITION_BACK ?
      camera.CameraPosition.CAMERA_POSITION_FRONT : camera.CameraPosition.CAMERA_POSITION_BACK;
    this.initCamera();
  }
  ```
* 若拍照回调不触发或者获取数据为空，可以在拍照执行后等待回调发生再停止会话，或者通过定时器[setInterval](../harmonyos-references/js-apis-timer.md#setinterval)延时异步调用会话停止使得会话可以先处理拍照响应数据，再关闭会话，避免会话因为当前任务被挂起导致无法监听到拍照回调事件。
* 完整示例代码如下：

  **说明** 

  参考[声明权限](../harmonyos-guides/declare-permissions.md)文档，需要先在module.json5文件中声明ohos.permission.CAMERA权限。

  ```ts
  import { camera } from '@kit.CameraKit';
  import { BusinessError } from '@kit.BasicServicesKit';
  import { abilityAccessCtrl, Permissions } from '@kit.AbilityKit';

  @Entry
  @Component
  struct Index {
    private xComponentCtl: XComponentController = new XComponentController();
    private xComponentSurfaceId: string = '';
    @State imageWidth: number = 1920;
    @State imageHeight: number = 1080;
    private cameraManager: camera.CameraManager | undefined = undefined;
    private cameras: Array<camera.CameraDevice> | Array<camera.CameraDevice> = [];
    private cameraInput: camera.CameraInput | undefined = undefined;
    private previewOutput: camera.PreviewOutput | undefined = undefined;
    private session: camera.VideoSession | undefined = undefined;
    private uiContext: UIContext = this.getUIContext();
    private context: Context | undefined = this.uiContext.getHostContext();
    private cameraPermission: Permissions = 'ohos.permission.CAMERA';
    @State isShow: boolean = false;
    @State cameraPosition: camera.CameraPosition = camera.CameraPosition.CAMERA_POSITION_BACK; // 默认使用后置摄像头

    async requestPermissionsFn(): Promise<void> {
      let atManager = abilityAccessCtrl.createAtManager();
      if (this.context) {
        let res = await atManager.requestPermissionsFromUser(this.context, [this.cameraPermission]);
        for (let i = 0; i < res.permissions.length; i++) {
          if (this.cameraPermission.toString() === res.permissions[i] &&
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
        let res = await atManager.requestPermissionOnSetting(this.context, [this.cameraPermission]);
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
            .height(this.imageWidth / this.imageHeight * 300);

          Button('切换摄像头')
            .type(ButtonType.ROUNDED_RECTANGLE)
            .backgroundColor('#0a59f7')
            .onClick(async () => {
              await this.changeCameraPosition();
            });
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
      .width('100%');
    }

    async changeCameraPosition() {
      await this.releaseCamera();
      this.cameraPosition = this.cameraPosition === camera.CameraPosition.CAMERA_POSITION_BACK ?
        camera.CameraPosition.CAMERA_POSITION_FRONT : camera.CameraPosition.CAMERA_POSITION_BACK;
      this.initCamera();
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
          this.cameraManager.getSupportedOutputCapability(curCamera, camera.SceneMode.NORMAL_VIDEO);
        if (!capability || capability.previewProfiles.length === 0) {
          console.error('capability is null || []');
          this.releaseCamera();
          return;
        }
        let minRatioDiff: number = 0.1;
        let surfaceRatio: number = this.imageWidth / this.imageHeight; // 最接近16:9宽高比。
        let previewProfile: camera.Profile = capability.previewProfiles[0];
        // 应用开发者根据实际业务需求选择一个支持的预览流previewProfile。
        // 此处以选择CAMERA_FORMAT_YUV_420_SP（NV21）格式、满足限定条件分辨率的预览流previewProfile为例。
        for (let index = 0; index < capability.previewProfiles.length; index++) {
          const tempProfile = capability.previewProfiles[index];
          let tempRatio = tempProfile.size.width >= tempProfile.size.height ?
            tempProfile.size.width / tempProfile.size.height : tempProfile.size.height / tempProfile.size.width;
          let currentRatio = Math.abs(tempRatio - surfaceRatio);
          if (currentRatio <= minRatioDiff && tempProfile.format == camera.CameraFormat.CAMERA_FORMAT_YUV_420_SP) {
            previewProfile = tempProfile;
            break;
          }
        }
        this.imageWidth = previewProfile.size.width; // 更新xComponent组件的宽。
        this.imageHeight = previewProfile.size.height; // 更新xComponent组件的高。
        console.info(`initCamera imageWidth:${this.imageWidth} imageHeight:${this.imageHeight}`);

        // 使用xComponentSurfaceId创建预览。
        this.previewOutput = this.cameraManager.createPreviewOutput(previewProfile, this.xComponentSurfaceId);
        if (!this.previewOutput) {
          console.error('initCamera createPreviewOutput');
          this.releaseCamera();
          return;
        }
        // 创建录像模式相机会话。
        let session = this.cameraManager.createSession(camera.SceneMode.NORMAL_VIDEO);
        if (!session) {
          console.error('session is null');
          this.releaseCamera();
          return;
        }
        this.session = session as camera.VideoSession;
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
  }
  ```
