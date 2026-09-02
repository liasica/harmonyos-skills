---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-camera-37
title: 自定义相机预览界面有黑边
breadcrumb: FAQ > 媒体开发 > 拍照和图片 > 相机开发（Camera） > 自定义相机预览界面有黑边
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:41+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:d3cc46bb01756067e353999b7c2601cd4e3eaba7bc44f21c9d07ccb0365981ed
---

## 问题现象

在使用自定义相机进行拍照时，预览界面的左侧有黑边，影响使用体验，异常界面如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/-nhNvqWwQKmU-8kJzo4hNw/zh-cn_image_0000002628552472.png "点击放大")

## 背景知识

* [相机预览](../harmonyos-guides/camera-preview.md)需要通过创建XComponent组件为预览流提供Surface，再通过获取XComponent组件对应Surface的ID创建预览流。
* XComponent组件持有的Surface区域的显示效果影响相机预览界面的展示，Surface的默认位置与大小和XComponent组件一致，可通过[setXComponentSurfaceRect](../harmonyos-references/ts-basic-components-xcomponent.md#setxcomponentsurfacerect12)接口自定义调整Surface的位置和大小，[SurfaceRect](../harmonyos-references/ts-basic-components-xcomponent.md#surfacerect12对象说明)对象用于描述XComponent持有Surface的显示区域。

## 问题定位

设置XComponent相关问题参考如下：

```ts
XComponent({
  id: 'xComponentId',
  type: XComponentType.SURFACE,
  controller: this.xComponentController
})
  .onLoad(async () => {
    this.surfaceId = this.xComponentController.getXComponentSurfaceId();
    this.xComponentController.setXComponentSurfaceRect({
      offsetX: 20,
      offsetY: 20,
      surfaceWidth: this.surfaceRect.surfaceWidth,
      surfaceHeight: this.surfaceRect.surfaceHeight
    });
  })
  .width('100%')
  .height(this.getUIContext().px2vp(1920))
```

排查发现调用setXComponentSurfaceRect接口时，SurfaceRect对象中的offsetX和offsetY都设置成了20。

## 分析结论

SurfaceRect对象中的offsetX和offsetY，代表预览显示区域与XComponent组件左边缘和上边缘的距离，这部分区域将显示XComponent组件本身的背景色，代码中XComponent组件的背景是黑色，因此造成相机预览时有黑边的情况发生。

## 修改建议

修改SurfaceRect对象中的offsetX和offsetY的值为0（或不填默认为0），完整代码如下：

```ts
import { camera } from '@kit.CameraKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { bundleManager, abilityAccessCtrl, common, PermissionRequestResult, Permissions } from '@kit.AbilityKit';
import { display } from '@kit.ArkUI';
import { hilog } from '@kit.PerformanceAnalysisKit';

const DOMAIN: number = 0x0000;
const TAG: string = '[CameraDemo]';

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
  private displayWidth = display.getDefaultDisplaySync().width;
  // surface宽高根据需要自行选择
  private surfaceRect: SurfaceRect = {
    surfaceWidth: this.displayWidth,
    surfaceHeight: this.displayWidth
  };

  // 检查是否配置相应权限
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
        hilog.error(DOMAIN, TAG, `data: ${JSON.stringify(err)}`);
      });
  }

  onPageShow(): void {
    if (!this.notHasPermission) {
      let permissions: Permissions = 'ohos.permission.CAMERA';
      if (this.checkPermissions(permissions)) {
        // 初始化相机
        this.initCamera();
        this.notHasPermission = false;
      } else {
        this.notHasPermission = true;
      }
    }
  }

  onPageHide(): void {
    if (!this.notHasPermission) {
      // 释放相机相关资源
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
          this.xComponentController.setXComponentSurfaceRect({
            surfaceWidth: this.surfaceRect.surfaceWidth,
            surfaceHeight: this.surfaceRect.surfaceHeight
          });
        })
        .width('100%')
        .margin({ top: 50 })
        .height(this.getUIContext().px2vp(this.displayWidth))

      // 拍照按钮，开发者需将拍照图片替换成资源中的对应媒体文件
      Image($r('app.media.capture'))
        .height(70)
        .margin({ top: 100 })
        .onClick(() => {
          // 开发者需自定义拍照逻辑
        })
    }
    .backgroundColor('#000000')
    .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM])
    .height('100%')
    .width('100%')
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
      hilog.error(DOMAIN, TAG, 'camera.getCameraManager error');
      return;
    }

    // 获取相机列表
    let cameraArray: Array<camera.CameraDevice> = this.mCameraManager.getSupportedCameras();
    if (cameraArray.length <= 0) {
      hilog.error(DOMAIN, TAG, 'cameraManager.getSupportedCameras error');
      return;
    }

    let deviceIndex = cameraArray.findIndex((cameraDevice: camera.CameraDevice) => {
      return cameraDevice.cameraPosition === this.mCameraPosition;
    });
    // 没有找到对应位置的摄像头，可选择其他摄像头，具体场景具体对待
    if (deviceIndex === -1) {
      deviceIndex = 0;
      hilog.error(DOMAIN, TAG, 'camera not found!');
    }
    this.curCameraDevice = cameraArray[deviceIndex];

    // 创建相机输入流
    try {
      this.cameraInput = this.mCameraManager.createCameraInput(this.curCameraDevice);
    } catch (error) {
      let err = error as BusinessError;
      hilog.error(DOMAIN, TAG, `Failed to createCameraInput errorCode = ${err.code}`);
    }
    if (this.cameraInput === undefined) {
      return;
    }

    // 打开相机
    try {
      await this.cameraInput.open();
    } catch (error) {
      let err = error as BusinessError;
      hilog.error(DOMAIN, TAG, `Failed to open device, errorCode = ${err.code}`);
    }

    // 获取支持的模式类型
    let sceneModes: Array<camera.SceneMode> = this.mCameraManager.getSupportedSceneModes(this.curCameraDevice);
    let isSupportPhotoMode: boolean = sceneModes.indexOf(camera.SceneMode.NORMAL_PHOTO) >= 0;
    if (!isSupportPhotoMode) {
      hilog.error(DOMAIN, TAG, 'photo mode not support');
      return;
    }

    // 获取相机设备支持的输出流能力
    let cameraOutputCapability: camera.CameraOutputCapability =
      this.mCameraManager.getSupportedOutputCapability(this.curCameraDevice, camera.SceneMode.NORMAL_PHOTO);
    if (!cameraOutputCapability) {
      hilog.error(DOMAIN, TAG, 'cameraManager.getSupportedOutputCapability error');
      return;
    }
    let previewProfile = cameraOutputCapability.previewProfiles[0];
    cameraOutputCapability.previewProfiles.forEach((profile) => {
      if (profile.size.width / profile.size.height === this.surfaceRect.surfaceWidth / this.surfaceRect.surfaceHeight) {
        previewProfile = profile;
        return;
      }
    });

    // 创建预览输出流，其中参数surfaceId参考上文XComponent组件，预览流为XComponent组件提供的surface
    try {
      this.previewOutput = this.mCameraManager.createPreviewOutput(previewProfile, this.surfaceId);
    } catch (error) {
      let err = error as BusinessError;
      hilog.error(DOMAIN, TAG, `Failed to create the PreviewOutput instance. error code: ${err.code}`);
    }
    if (this.previewOutput === undefined) {
      return;
    }

    // 创建会话
    try {
      this.photoSession = this.mCameraManager.createSession(camera.SceneMode.NORMAL_PHOTO) as camera.PhotoSession;
    } catch (error) {
      let err = error as BusinessError;
      hilog.error(DOMAIN, TAG, `Failed to create the session instance. errorCode = ${err.code}`);
    }
    if (this.photoSession === undefined) {
      return;
    }

    // 开始配置会话
    try {
      this.photoSession.beginConfig();
    } catch (error) {
      let err = error as BusinessError;
      hilog.error(DOMAIN, TAG, `Failed to beginConfig. errorCode = ${err.code}`);
    }

    // 向会话中添加相机输入流
    try {
      this.photoSession.addInput(this.cameraInput);
    } catch (error) {
      let err = error as BusinessError;
      hilog.error(DOMAIN, TAG, `Failed to addInput. errorCode = ${err.code}`);
    }

    // 向会话中添加预览输出流
    try {
      this.photoSession.addOutput(this.previewOutput);
    } catch (error) {
      let err = error as BusinessError;
      hilog.error(DOMAIN, TAG, `Failed to addOutput(previewOutput). errorCode = ${err.code}`);
    }

    // 提交会话配置
    try {
      await this.photoSession.commitConfig();
    } catch (error) {
      let err = error as BusinessError;
      hilog.error(DOMAIN, TAG, `Failed to commit session configuration, errorCode = ${err.code}`);
    }

    // 启动会话
    try {
      await this.photoSession.start();
    } catch (error) {
      let err = error as BusinessError;
      hilog.error(DOMAIN, TAG, `Failed to start session. errorCode = ${err.code}`);
    }
  }
}
```

修改后的正常界面如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/SgwLjcaJT52ml6JnYT9UJQ/zh-cn_image_0000002658911795.png "点击放大")
