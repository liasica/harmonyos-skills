---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-camera-48
title: 如何在相机预览界面绘制人脸跟踪框
breadcrumb: FAQ > 媒体开发 > 拍照和图片 > 相机开发（Camera） > 如何在相机预览界面绘制人脸跟踪框
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:41+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:0412ecf1b4a41aa8093aa9753d4c89ffeea7a77537a5ceda837dcf294c121755
---

## 问题现象

人脸跟踪在相机的很多场景下有着广泛应用，如行人检测、相机的人像模式拍摄，需要在相机预览界面对人脸进行实时跟踪，如何绘制人脸跟踪框？

## 背景知识

[元数据](../harmonyos-guides/camera-metadata.md)（Metadata）是对相机返回的图像信息数据的描述和上下文，针对图像信息，提供的更详细的数据，如照片或视频中，识别人像的取景框坐标等信息。

## 解决方案

* 可以使用元数据流对人脸区域进行实时检测，首先要根据相机管理器和支持的输出能力获取元数据输出流：

  ```ts
  /**
   * 获取元数据输出流
   * @param cameraManager 相机管理器实例
   * @param cameraOutputCapability 相机支持的输出能力
   * @return 元数据输出流
   */
  getMetadataOutput(cameraManager: camera.CameraManager,
  cameraOutputCapability: camera.CameraOutputCapability) {
    let metadataObjectTypes: Array<camera.MetadataObjectType> = cameraOutputCapability.supportedMetadataObjectTypes;
    try {
      this.metadataOutput = cameraManager.createMetadataOutput(metadataObjectTypes);
    } catch (error) {
      let err = error as BusinessError;
      console.error(`Failed to createMetadataOutput, error code: ${err.code}`);
    }
  }
  ```
* 然后需要对元数据流是否可用进行监听，获取人脸位置信息，注意返回的人脸坐标为归一化坐标，需要根据实际预览界面的宽高进行转换，以预览界面只有一个人脸为例：

  ```ts
  /**
   * 元数据流可用监听，获取人脸位置信息
   * @param metadataOutput 元数据输出流
   */
  onMetadataObjectsAvailable(metadataOutput: camera.MetadataOutput): void {
    metadataOutput.on('metadataObjectsAvailable',
    (err: BusinessError, metadataObjectArr: Array<camera.MetadataObject>) => {
      if (err !== undefined && err.code !== 0) {
        return;
      }
      if (metadataObjectArr.length === 1) {
        let faceRect = metadataObjectArr[0];
        if (faceRect.boundingBox.topLeftX && faceRect.boundingBox.topLeftY && faceRect.boundingBox.width &&
        faceRect.boundingBox.height) {
          this.faceTopLeftX = this.getUIContext().px2vp(faceRect.boundingBox.topLeftX) * this.actualWidth;
          this.faceTopLeftY = this.getUIContext().px2vp(faceRect.boundingBox.topLeftY) * this.actualHeight;
          this.faceWidth = this.getUIContext().px2vp(faceRect.boundingBox.width) * this.actualWidth;
          this.faceHeight = this.getUIContext().px2vp(faceRect.boundingBox.height) * this.actualHeight;
          // 打印人脸归一化坐标
          console.info(`人脸归一化坐标：boundingBox = ${JSON.stringify(faceRect.boundingBox)}`);
        }
      }
    });
  }
  ```
* 还需要对元数据流错误信息进行监听：

  ```ts
  /**
   * 元数据流错误信息监听
   * @param metadataOutput 元数据输出流
   */
  onMetadataError(metadataOutput: camera.MetadataOutput): void {
    metadataOutput.on('error', (metadataOutputError: BusinessError) => {
      console.error(`Metadata output error code: ${metadataOutputError.code}`);
    });
  }
  ```
* 最后可以在主界面根据实时监听到的人脸坐标绘制跟踪框：

  ```ts
  build() {
    Column({ space: 20 }) {
      Stack({ alignContent: Alignment.TopStart }) {
        XComponent({
          type: XComponentType.SURFACE,
          controller: this.mXComponentController,
          imageAIOptions: this.options
        })
          .backgroundColor(Color.Gray)
          .onLoad(async () => {
            // 动态计算XComponent的宽高，确保与相机预览比例一致
            const displayWidth = display.getDefaultDisplaySync().width;
            // 更新XComponent的实际显示高度
            this.mXComponentController.setXComponentSurfaceRect({
              surfaceWidth: displayWidth,
              surfaceHeight: this.surfaceHeight
            });
            this.actualWidth = displayWidth;
            this.actualHeight = this.surfaceHeight;
            // 同步更新状态变量，确保UI使用正确高度
            this.xComponentSurfaceId = this.mXComponentController.getXComponentSurfaceId();
          })
          .height(this.getUIContext().px2vp(this.surfaceHeight))

        // 绘制人脸区域，宽高和位置需动态变化
        Text()
          .border({ width: 1, color: Color.Orange })
          .position({ y: this.faceTopLeftY, x: this.faceTopLeftX })
          .visibility(this.showRect ? Visibility.Visible : Visibility.Hidden)
          .width(this.faceWidth)
          .height(this.faceHeight)
      }

      Button('点击开始检测人脸')
        .onClick(() => {
          // 显示人像区域
          this.showRect = true;
        })

      Button('点击取消检测人脸')
        .onClick(() => {
          // 不显示人像区域
          this.showRect = false;
        })
    }
  }
  ```

完整示例参考如下：

```ts
import { camera } from '@kit.CameraKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { image } from '@kit.ImageKit';
import { bundleManager, abilityAccessCtrl, PermissionRequestResult, Permissions } from '@kit.AbilityKit';
import { display } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  @State faceTopLeftX: number = 0;
  @State faceTopLeftY: number = 0;
  @State faceWidth: number = 0;
  @State faceHeight: number = 0;
  @State actualWidth: number = 0;
  @State actualHeight: number = 0;
  @State showRect: boolean = false;
  private imageSize: image.Size = { width: 480, height: 640 };
  private context: Context = this.getUIContext().getHostContext() as Context;
  private mXComponentController: XComponentController = new XComponentController;
  private cameraManager: camera.CameraManager | undefined = undefined;
  private cameraSession: camera.PhotoSession | undefined = undefined;
  private photoOutput: camera.PhotoOutput | undefined = undefined;
  private cameraInput: camera.CameraInput | undefined = undefined;
  private previewOutput: camera.PreviewOutput | undefined = undefined;
  private metadataOutput: camera.MetadataOutput | undefined = undefined;
  private aiController: ImageAnalyzerController = new ImageAnalyzerController();
  private xComponentSurfaceId: string = '';
  private notHasPermission: boolean = true;
  private displayWidth = display.getDefaultDisplaySync().width;
  private surfaceHeight = this.displayWidth * (this.imageSize.height / this.imageSize.width);
  private options: ImageAIOptions = {
    types: [ImageAnalyzerType.SUBJECT, ImageAnalyzerType.TEXT],
    aiController: this.aiController
  };

  checkPermissions(permission: Permissions) {
    let atManager = abilityAccessCtrl.createAtManager();
    let bundleInfo = bundleManager.getBundleInfoForSelfSync(bundleManager.BundleFlag.GET_BUNDLE_INFO_WITH_APPLICATION);
    let tokenID = bundleInfo.appInfo.accessTokenId;
    let authResults = atManager.checkAccessTokenSync(tokenID, permission);
    return authResults === abilityAccessCtrl.GrantStatus.PERMISSION_GRANTED;
  }

  aboutToAppear(): void {
    let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
    atManager.requestPermissionsFromUser(this.context, ['ohos.permission.CAMERA'])
      .then((data: PermissionRequestResult) => {
        if (data.authResults[0] === 0) {
          this.notHasPermission = false;
          this.prepareCamera();
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
        this.prepareCamera();
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

  aboutToDisappear(): void {
    if (!this.notHasPermission) {
      this.releaseCamera();
    }
  }

  build() {
    Column({ space: 20 }) {
      Stack({ alignContent: Alignment.TopStart }) {
        XComponent({
          type: XComponentType.SURFACE,
          controller: this.mXComponentController,
          imageAIOptions: this.options
        })
          .backgroundColor(Color.Gray)
          .onLoad(async () => {
            // 动态计算XComponent的宽高，确保与相机预览比例一致
            const displayWidth = display.getDefaultDisplaySync().width;
            // 更新XComponent的实际显示高度
            this.mXComponentController.setXComponentSurfaceRect({
              surfaceWidth: displayWidth,
              surfaceHeight: this.surfaceHeight
            });
            this.actualWidth = displayWidth;
            this.actualHeight = this.surfaceHeight;
            // 同步更新状态变量，确保UI使用正确高度
            this.xComponentSurfaceId = this.mXComponentController.getXComponentSurfaceId();
          })
          .height(this.getUIContext().px2vp(this.surfaceHeight))

        // 绘制人脸区域，宽高和位置需动态变化
        Text()
          .border({ width: 1, color: Color.Orange })
          .position({ y: this.faceTopLeftY, x: this.faceTopLeftX })
          .visibility(this.showRect ? Visibility.Visible : Visibility.Hidden)
          .width(this.faceWidth)
          .height(this.faceHeight)
      }

      Button('点击开始检测人脸')
        .onClick(() => {
          // 显示人像区域
          this.showRect = true;
        })

      Button('点击取消检测人脸')
        .onClick(() => {
          // 不显示人像区域
          this.showRect = false;
        })
    }
  }

  createCameraManager() {
    // 创建CameraManager对象
    let cameraManager: camera.CameraManager = camera.getCameraManager(this.context);
    if (!cameraManager) {
      console.error('CameraDemo camera.getCameraManager error');
      return;
    }
    this.cameraManager = cameraManager;
    // 监听相机状态变化
    this.cameraManager.on('cameraStatus', (err: BusinessError, cameraStatusInfo: camera.CameraStatusInfo) => {
      if (err) {
        console.error(`Camera status listener failed: ${JSON.stringify(err)}}`);
        return;
      }
      console.info(`CameraDemo camera: ${cameraStatusInfo.camera.cameraId}, status: ${cameraStatusInfo.status}`);
    });
  }

  async prepareCamera() {
    this.createCameraManager();

    if (!this.cameraManager) {
      console.error('CameraDemo cameraManager is undefined.');
      return;
    }
    // 获取支持指定的相机设备对象
    let cameraDevices: Array<camera.CameraDevice> = [];
    let cameraDevice: camera.CameraDevice;
    try {
      cameraDevices = this.cameraManager.getSupportedCameras();
    } catch (error) {
      let err = error as BusinessError;
      console.error(`CameraDemo The getSupportedCameras call failed. error: ${JSON.stringify(err)}`);
    }
    cameraDevices.forEach((cameraDevice: camera.CameraDevice) => {
      console.info(`CameraDemo cameraId: ${cameraDevice.cameraId}, cameraPosition: ${cameraDevice.cameraPosition.toString()}, cameraType: ${cameraDevice.cameraType.toString()}, connectionType: ${cameraDevice.connectionType.toString()}`);
    });

    // 创建相机输入流
    try {
      cameraDevice = cameraDevices[1];
      this.cameraInput = this.cameraManager.createCameraInput(cameraDevice);
    } catch (error) {
      let err = error as BusinessError;
      console.error(`CameraDemo createCaptureSession error. error: ${JSON.stringify(err)}`);
      return;
    }
    // 监听cameraInput错误信息
    this.cameraInput.on('error', cameraDevice, (error: BusinessError) => {
      console.error(`CameraDemo Camera input error: ${JSON.stringify(error)}`);
    });

    // 打开相机
    try {
      await this.cameraInput.open();
    } catch (error) {
      let err = error as BusinessError;
      // 相机不可用错误码
      if (error.code === 1000500001) {
        this.releaseCamera();
        await this.prepareCamera();
        return;
      }
      console.error(`CameraDemo cameraInput open error. error: ${JSON.stringify(err)}`);
    }

    // 获取相机设备支持的输出流能力
    let cameraOutputCapability: camera.CameraOutputCapability =
      this.cameraManager.getSupportedOutputCapability(cameraDevices[0], camera.SceneMode.NORMAL_PHOTO);
    if (!cameraOutputCapability) {
      console.error('CameraDemo cameraManager.getSupportedOutputCapability error');
      return;
    }

    let targetProfile: camera.Profile | undefined;
    for (let profile of cameraOutputCapability.previewProfiles) {
      if (profile.size.width === this.imageSize.height && profile.size.height === this.imageSize.width) {
        targetProfile = profile;
        break;
      }
    }
    if (targetProfile) {
      const previewProfile = targetProfile;
      this.imageSize.height = targetProfile?.size?.height;
      this.imageSize.width = targetProfile?.size?.width;
      console.info(`选择的最佳预览尺寸：宽 = ${this.imageSize.width}, 高 = ${this.imageSize.height}`);
      this.getMetadataOutput(this.cameraManager, cameraOutputCapability);
      if (!this.metadataOutput) {
        console.error('initCamera metadataOutput error');
        return;
      }
      this.metadataOutput.start().then(() => {
        console.info('metadataOutput start');
      }).catch((err: BusinessError) => {
        console.error(`metadataOutput start err: ${JSON.stringify(err)}`);
      });
      this.onMetadataObjectsAvailable(this.metadataOutput);
      this.onMetadataError(this.metadataOutput);

      // 创建预览输出流
      try {
        this.previewOutput = this.cameraManager.createPreviewOutput(previewProfile, this.xComponentSurfaceId);
        if (!this.previewOutput) {
          console.error('previewOutput undefined!');
        }
      } catch (error) {
        let err = error as BusinessError;
        console.error(`CameraDemo createCaptureSession error. error: ${JSON.stringify(err)}`);
        return;
      }

      // 监听预览输出流的错误信息
      this.previewOutput.on('error', (error: BusinessError) => {
        console.error(`CameraDemo previewOutput error: ${JSON.stringify(error)}`);
      });

      // 选取合适的分辨率
      try {
        let photoProfile: camera.Profile | undefined = undefined;
        cameraOutputCapability.photoProfiles.forEach((profile) => {
          if (profile.size.width === this.imageSize.width && profile.size.height === this.imageSize.height) {
            photoProfile = profile;
            return;
          }
        });
        if (photoProfile) {
          this.photoOutput = this.cameraManager.createPhotoOutput(photoProfile);
        }
      } catch (error) {
        let err = error as BusinessError;
        console.error(`CameraDemo createPhotoOutput error ${JSON.stringify(err)}`);
      }
      if (this.photoOutput === undefined) {
        console.error('CameraDemo photoOutput is undefined.');
        return;
      }

      // 创建相机会话
      try {
        this.cameraSession = this.cameraManager.createSession<camera.PhotoSession>(camera.SceneMode.NORMAL_PHOTO);
      } catch (error) {
        let err = error as BusinessError;
        console.error(`CameraDemo createCaptureSession error. error: ${JSON.stringify(err)}`);
        return;
      }

      // 监听session错误信息
      this.cameraSession.on('error', (error: BusinessError) => {
        console.error(`CameraDemo Capture session error: ${JSON.stringify(error)}`);
      });

      // 开始会话配置
      try {
        this.cameraSession.beginConfig();
      } catch (error) {
        let err = error as BusinessError;
        console.error(`CameraDemo beginConfig error. error: ${JSON.stringify(err)}`);
      }

      // 向会话中添加相机输入流
      try {
        this.cameraSession.addInput(this.cameraInput);
      } catch (error) {
        let err = error as BusinessError;
        console.error(`CameraDemo addInput error. error: ${JSON.stringify(err)}`);
      }

      // 向会话中添加预览输出流和元数据输出流
      try {
        this.cameraSession.addOutput(this.previewOutput);
        this.cameraSession.addOutput(this.metadataOutput);
      } catch (error) {
        let err = error as BusinessError;
        console.error(`CameraDemo add previewOutput error. error: ${JSON.stringify(err)}`);
      }

      // 向会话中添加拍照输出流
      try {
        this.cameraSession.addOutput(this.photoOutput);
      } catch (error) {
        let err = error as BusinessError;
        console.error(`CameraDemo add photoOutput error. error: ${JSON.stringify(err)}`);
      }

      // 提交会话配置
      try {
        await this.cameraSession.commitConfig();
      } catch (error) {
        let err = error as BusinessError;
        console.error(`CameraDemo captureSession commitConfig error: ${JSON.stringify(err)}`);
      }

      // 启动会话
      try {
        await this.cameraSession.start();
      } catch (error) {
        let err = error as BusinessError;
        console.error(`CameraDemo captureSession start error: ${JSON.stringify(err)}`);
      }
    }
  }

  // 释放相机流
  async releaseCamera() {
    if (this.cameraInput) {
      this.cameraInput.close();
    }
    if (this.previewOutput) {
      this.previewOutput.release();
    }
    if (this.photoOutput) {
      this.photoOutput.release();
    }
    if (this.cameraSession) {
      this.cameraSession.stop();
    }
    if (this.cameraSession) {
      this.cameraSession.release();
    }
    if (this.metadataOutput) {
      this.metadataOutput.release();
    }
    this.cameraSession = undefined;
  }

  /**
   * 获取元数据输出流
   * @param cameraManager 相机管理器实例
   * @param cameraOutputCapability 相机支持的输出能力
   * @return 元数据输出流
   */
  getMetadataOutput(cameraManager: camera.CameraManager,
    cameraOutputCapability: camera.CameraOutputCapability) {
    let metadataObjectTypes: Array<camera.MetadataObjectType> = cameraOutputCapability.supportedMetadataObjectTypes;
    try {
      this.metadataOutput = cameraManager.createMetadataOutput(metadataObjectTypes);
    } catch (error) {
      let err = error as BusinessError;
      console.error(`Failed to createMetadataOutput, error code: ${err.code}`);
    }
  }

  /**
   * 元数据流可用监听，获取人脸位置信息
   * @param metadataOutput 元数据输出流
   */
  onMetadataObjectsAvailable(metadataOutput: camera.MetadataOutput): void {
    metadataOutput.on('metadataObjectsAvailable',
      (err: BusinessError, metadataObjectArr: Array<camera.MetadataObject>) => {
        if (err !== undefined && err.code !== 0) {
          return;
        }
        if (metadataObjectArr.length === 1) {
          let faceRect = metadataObjectArr[0];
          if (faceRect.boundingBox.topLeftX && faceRect.boundingBox.topLeftY && faceRect.boundingBox.width &&
          faceRect.boundingBox.height) {
            this.faceTopLeftX = this.getUIContext().px2vp(faceRect.boundingBox.topLeftX) * this.actualWidth;
            this.faceTopLeftY = this.getUIContext().px2vp(faceRect.boundingBox.topLeftY) * this.actualHeight;
            this.faceWidth = this.getUIContext().px2vp(faceRect.boundingBox.width) * this.actualWidth;
            this.faceHeight = this.getUIContext().px2vp(faceRect.boundingBox.height) * this.actualHeight;
            // 打印人脸归一化坐标
            console.info(`人脸归一化坐标：boundingBox = ${JSON.stringify(faceRect.boundingBox)}`);
          }
        }
      });
  }

  /**
   * 元数据流错误信息监听
   * @param metadataOutput 元数据输出流
   */
  onMetadataError(metadataOutput: camera.MetadataOutput): void {
    metadataOutput.on('error', (metadataOutputError: BusinessError) => {
      console.error(`Metadata output error code: ${metadataOutputError.code}`);
    });
  }
}
```

在使用相机功能前需要在module.json5文件中配置相机权限：

```json
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

## 总结

元数据每秒钟可以获取大约30次回调，优于使用[ImageReceiver](../harmonyos-references/arkts-apis-image-imagereceiver.md)获取预览帧图片后再使用[Core Vision Kit](../harmonyos-guides/core-vision-introduction.md)中的[人脸检测能力](../harmonyos-guides/core-vision-face-detector.md)（此方法每秒钟获取到的回调远少于元数据，会造成相机预览界面的严重卡顿），所以在对流数据进行检测时应优先选择[Camera Kit](../harmonyos-guides/camera-overview.md)中提供的元数据能力。
