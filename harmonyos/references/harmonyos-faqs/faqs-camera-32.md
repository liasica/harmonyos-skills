---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-camera-32
title: 自定义相机如何切换前后摄像头
breadcrumb: FAQ > 媒体开发 > 拍照和图片 > 相机开发（Camera） > 自定义相机如何切换前后摄像头
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:41+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:d3e612f0428dcf26f21eb8c5cf901c732b9a8eebbc8ae858061baa1712effa00
---

## 问题现象

开发者在使用自定义相机进行拍照或录像时，经常需要切换前后摄像头。本文以相机预览为例，提供了一套针对相机前后摄像头切换处理过程的规范。

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/mdFx30hcQ1mr3rDGOcgIAg/zh-cn_image_0000002658791847.gif "点击放大")

## 背景知识

* 在初始化相机时，可以使用相机管理器类[CameraManager](../harmonyos-references/arkts-apis-camera-cameramanager.md)创建CameraInput、PreviewOutput等实例，根据需求创建指定[SceneMode](../harmonyos-references/arkts-apis-camera-e.md#scenemode11)下的Session，完成Session配置。
* 在相机位置转换时，可以使用[CameraPosition](../harmonyos-references/arkts-apis-camera-e.md#cameraposition)中的枚举值来表示相机位置。
* 摄像头切换时，必须先进行相机流的释放，才能重新创建相机输入流等。

## 解决方案

1. 在开发相机应用时，需要先[申请相机相关权限](../harmonyos-guides/camera-preparation.md)：

   ```screen
   {
     "name": "ohos.permission.CAMERA",
     "reason": "$string:reason_camera",
     "usedScene": {
       "abilities": [
         "EntryAbility"
       ]
     }
   },
   ```
2. 在切换前后摄像头时，首先需要对当前的相机流进行释放，否则在执行输入流创建、会话配置等操作时会出现异常。然后判断当前摄像头位置进行前后切换，最后需要再次初始化相机，重新创建相机管理器、输入输出流等：

   ```screen
   async changeCameraPosition() {
     this.releaseCamera();
     this.mCameraPosition = this.mCameraPosition === camera.CameraPosition.CAMERA_POSITION_BACK ?
     camera.CameraPosition.CAMERA_POSITION_FRONT : camera.CameraPosition.CAMERA_POSITION_BACK;
     this.initCamera();
   }
   ```
3. 释放相机流的相关代码如下：

   ```screen
   async releaseCamera() {
     // 释放相机输入流
     if (this.cameraInput) {
       this.cameraInput.close();
     }
     // 释放预览输入流
     if (this.previewOutput) {
       this.previewOutput.release();
     }
     // 停止当前会话
     if (this.photoSession) {
       this.photoSession.stop();
     }
     // 释放会话
     if (this.photoSession) {
       this.photoSession.release();
     }
     this.photoSession = undefined;
   }
   ```
4. 将XComponent嵌入到视图的主界面相关代码参考如下：

   ```screen
   build() {
     Column() {
       XComponent({
         id: 'xComponentId',
         type: XComponentType.SURFACE,
         controller: this.xComponentController
       })
         .onLoad(async () => {
           this.surfaceId = this.xComponentController.getXComponentSurfaceId();
           this.xComponentController.setXComponentSurfaceRect(this.surfaceRect);
         })
         .margin(5)
         .border({ width: 1, color: Color.White })
         .width('100%')
         .height(this.getUIContext().px2vp(1920))

       Button('切换摄像头')
         .margin({ top: 10 })
         .onClick(() => {
           this.changeCameraPosition();
         })
     }
     .width('100%')
   }
   ```

完整示例参考如下：

```screen
import { camera } from '@kit.CameraKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { image } from '@kit.ImageKit';
import { bundleManager, abilityAccessCtrl, common, PermissionRequestResult, Permissions } from '@kit.AbilityKit';

@Entry
@Component
struct Index {
  private notHasPermission: boolean = true;
  private surfaceId: string = '';
  private context = this.getUIContext().getHostContext();
  private xComponentController: XComponentController = new XComponentController();
  private curCameraDevice: camera.CameraDevice | undefined = undefined; // 当前相机设备
  private cameraInput: camera.CameraInput | undefined = undefined; // 相机输入流
  private previewOutput: camera.PreviewOutput | undefined = undefined; // 预览输出流
  private photoSession: camera.PhotoSession | undefined = undefined; // 普通拍照模式会话
  private mCameraManager: camera.CameraManager = camera.getCameraManager(this.context);
  private mCameraPosition: camera.CameraPosition = camera.CameraPosition.CAMERA_POSITION_BACK;
  // surface宽高根据需要自行选择
  private surfaceRect: SurfaceRect = {
    surfaceWidth: 1440,
    surfaceHeight: 1440
  };
  private imageSize: image.Size = { width: 1440, height: 1440 };

  checkPermissions(permission: Permissions) {
    let atManager = abilityAccessCtrl.createAtManager();
    let bundleInfo = bundleManager.getBundleInfoForSelfSync(bundleManager.BundleFlag.GET_BUNDLE_INFO_WITH_APPLICATION);
    let tokenID = bundleInfo.appInfo.accessTokenId;
    let authResults = atManager.checkAccessTokenSync(tokenID, permission);
    return authResults === abilityAccessCtrl.GrantStatus.PERMISSION_GRANTED;
  }

  aboutToAppear(): void {
    let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
    let context: Context = this.getUIContext().getHostContext() as common.UIAbilityContext;
    atManager.requestPermissionsFromUser(context, ['ohos.permission.CAMERA'])
      .then((data: PermissionRequestResult) => {
        if (data.authResults[0] === 0) {
          this.notHasPermission = false;
          this.initCamera();
        } else if (data.authResults[0] === -1) {
          this.notHasPermission = true;
        }
      })
      .catch((err: BusinessError) => {
        console.error(`data: ${JSON.stringify(err)}`);
      });
  }

  onPageShow(): void {
    if (!this.notHasPermission) {
      let permissions: Permissions = 'ohos.permission.CAMERA';
      if (this.checkPermissions(permissions)) {
        this.initCamera();
        this.notHasPermission = false;
      } else {
        this.notHasPermission = true;
      }
    }
  }

  onPageHide(): void {
    if (!this.notHasPermission) {
      this.releaseCamera();
    }
  }

  build() {
    Column() {
      XComponent({
        id: 'xComponentId',
        type: XComponentType.SURFACE,
        controller: this.xComponentController
      })
        .onLoad(async () => {
          this.surfaceId = this.xComponentController.getXComponentSurfaceId();
          this.xComponentController.setXComponentSurfaceRect(this.surfaceRect);
        })
        .margin(5)
        .border({ width: 1, color: Color.White })
        .width('100%')
        .height(this.getUIContext().px2vp(1920))

      Button('切换摄像头')
        .margin({ top: 10 })
        .onClick(() => {
          this.changeCameraPosition();
        })
    }
    .width('100%')
  }

  async changeCameraPosition() {
    this.releaseCamera();
    this.mCameraPosition = this.mCameraPosition === camera.CameraPosition.CAMERA_POSITION_BACK ?
    camera.CameraPosition.CAMERA_POSITION_FRONT : camera.CameraPosition.CAMERA_POSITION_BACK;
    this.initCamera();
  }

  async releaseCamera() {
    // 释放相机输入流
    if (this.cameraInput) {
      this.cameraInput.close();
    }
    // 释放预览输入流
    if (this.previewOutput) {
      this.previewOutput.release();
    }
    // 停止当前会话
    if (this.photoSession) {
      this.photoSession.stop();
    }
    // 释放会话
    if (this.photoSession) {
      this.photoSession.release();
    }
    this.photoSession = undefined;
  }

  async initCamera(): Promise<void> {
    // 创建CameraManager对象
    if (!this.mCameraManager) {
      console.error('camera.getCameraManager error');
      return;
    }

    // 获取相机列表
    let cameraArray: Array<camera.CameraDevice> = this.mCameraManager.getSupportedCameras();
    if (cameraArray.length <= 0) {
      console.error('cameraManager.getSupportedCameras error');
      return;
    }

    for (let index = 0; index < cameraArray.length; index++) {
      console.info(`cameraId : ${cameraArray[index].cameraId}`); // 获取相机ID
      console.info(`cameraPosition : ${cameraArray[index].cameraPosition}`); // 获取相机位置
      console.info(`cameraType : ${cameraArray[index].cameraType}`); // 获取相机类型
      console.info(`connectionType : ${cameraArray[index].connectionType}`); // 获取相机连接类型
    }

    let deviceIndex = cameraArray.findIndex((cameraDevice: camera.CameraDevice) => {
      return cameraDevice.cameraPosition === this.mCameraPosition;
    });
    // 没有找到对应位置的摄像头，可选择其他摄像头，具体场景具体对待
    if (deviceIndex === -1) {
      deviceIndex = 0;
      console.error('not found camera');
    }
    this.curCameraDevice = cameraArray[deviceIndex];

    // 创建相机输入流
    try {
      this.cameraInput = this.mCameraManager.createCameraInput(this.curCameraDevice);
    } catch (error) {
      let err = error as BusinessError;
      console.error(`Failed to createCameraInput errorCode = ${err.code}`);
    }
    if (this.cameraInput === undefined) {
      return;
    }

    // 打开相机
    try {
      await this.cameraInput.open();
    } catch (error) {
      let err = error as BusinessError;
      console.error(`Failed to open device, errorCode = ${err.code}`);
    }

    // 获取支持的模式类型
    let sceneModes: Array<camera.SceneMode> = this.mCameraManager.getSupportedSceneModes(this.curCameraDevice);
    let isSupportPhotoMode: boolean = sceneModes.indexOf(camera.SceneMode.NORMAL_PHOTO) >= 0;
    if (!isSupportPhotoMode) {
      console.error('photo mode not support');
      return;
    }

    // 获取相机设备支持的输出流能力
    let cameraOutputCapability: camera.CameraOutputCapability =
      this.mCameraManager.getSupportedOutputCapability(this.curCameraDevice, camera.SceneMode.NORMAL_PHOTO);
    if (!cameraOutputCapability) {
      console.error('cameraManager.getSupportedOutputCapability error');
      return;
    }
    let previewProfile = cameraOutputCapability.previewProfiles[0];
    cameraOutputCapability.previewProfiles.forEach((profile) => {
      if (profile.size.width === this.imageSize.width && profile.size.height === this.imageSize.height) {
        previewProfile = profile;
        return;
      }
    });

    // 创建预览输出流，其中参数surfaceId参考上文XComponent组件，预览流为XComponent组件提供的surface
    try {
      this.previewOutput = this.mCameraManager.createPreviewOutput(previewProfile, this.surfaceId);
    } catch (error) {
      let err = error as BusinessError;
      console.error(`Failed to create the PreviewOutput instance. error code: ${err.code}`);
    }
    if (this.previewOutput === undefined) {
      return;
    }

    // 创建会话
    try {
      this.photoSession = this.mCameraManager.createSession(camera.SceneMode.NORMAL_PHOTO) as camera.PhotoSession;
    } catch (error) {
      let err = error as BusinessError;
      console.error(`Failed to create the session instance. errorCode = ${err.code}`);
    }
    if (this.photoSession === undefined) {
      return;
    }

    // 开始配置会话
    try {
      this.photoSession.beginConfig();
    } catch (error) {
      let err = error as BusinessError;
      console.error(`Failed to beginConfig. errorCode = ${err.code}`);
    }

    // 向会话中添加相机输入流
    try {
      this.photoSession.addInput(this.cameraInput);
    } catch (error) {
      let err = error as BusinessError;
      console.error(`Failed to addInput. errorCode = ${err.code}`);
    }

    // 向会话中添加预览输出流
    try {
      this.photoSession.addOutput(this.previewOutput);
    } catch (error) {
      let err = error as BusinessError;
      console.error(`Failed to addOutput(previewOutput). errorCode = ${err.code}`);
    }

    // 提交会话配置
    try {
      await this.photoSession.commitConfig();
    } catch (error) {
      let err = error as BusinessError;
      console.error(`Failed to commit session configuration, errorCode = ${err.code}`);
    }

    // 启动会话
    try {
      await this.photoSession.start();
    } catch (error) {
      let err = error as BusinessError;
      console.error(`Failed to start session. errorCode = ${err.code}`);
    }
  }
}
```

## 常见FAQ

Q：自定义相机录制视频过程中，是否能实现前后摄像头的切换？

A：视频录制过程中不支持前后摄像头的切换，切换需要销毁并重新创建相机流。

Q：在前后摄像头切换时，如何解决画面停顿时间长的问题？

A：可以通过预览流截图，实现[模糊动效](../harmonyos-guides/camera-animation.md#模糊动效)，从而完成前后置切换的动效，提升用户体验。
