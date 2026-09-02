---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-camera-47
title: 自定义相机如何隔一段时间获取并保存预览帧的图像
breadcrumb: FAQ > 媒体开发 > 拍照和图片 > 相机开发（Camera） > 自定义相机如何隔一段时间获取并保存预览帧的图像
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:41+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:d22b20f7bbfca37e463f29f2bbf4111b99369252c8d0d799ca50915bc63503d4
---

## 问题现象

如何使用自定义相机打开前置摄像头，隔一段时间截取视频帧，编码成图片文件后保存到沙箱，以供后续发送图像数据进行识别？

## 背景知识

* [ImageReceiver](../harmonyos-references/arkts-apis-image-imagereceiver.md)为图像接收类，用于获取组件surface id，接收最新的图片和读取下一张图片，以及释放ImageReceiver实例。
* [packToData](../harmonyos-references/arkts-apis-image-imagepacker.md#packtodata13)可用于图片压缩或重新编码，可以使用此接口将PixelMap类型的数据编码成图片文件保存至应用沙箱。

## 解决方案

1. 首先使用[ImageReceiver](../harmonyos-references/arkts-apis-image-imagereceiver.md)接收预览帧图片，具体方法可参考[双路预览](../harmonyos-guides/camera-dual-channel-preview.md)。
2. 将获取到的预览帧图片编码成图片保存至应用沙箱，参考代码如下：

   ```ts
   /**
    * 将PixelMap对象的图片数据保存至应用沙箱路径
    * @param pixelMap 需要保存的pixelMap对象
    * @returns
    */
   async packToData(pixelMap: PixelMap) {
     try {
       let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
       let cacheDir: string = context.cacheDir;
       let now = Date.now();
       let fileUrl = cacheDir + `/${now}_packToData.jpg`;
       if (fs.accessSync(fileUrl)) {
         fs.unlinkSync(fileUrl);
       }
       let packOpts: image.PackingOption = { format: 'image/jpeg', quality: 98 };
       const imagePackerApi: image.ImagePacker = image.createImagePacker();
       imagePackerApi.packToData(pixelMap, packOpts)
         .then((data: ArrayBuffer) => {
           let file = fs.openSync(fileUrl, fs.OpenMode.READ_WRITE | fs.OpenMode.CREATE);
           fs.write(file.fd, data).then((writeLen: number) => {
             hilog.info(DOMAIN, TAG, `packToData succeed and size is: ${writeLen}, path is ${fileUrl}}`);
           }).catch((err: BusinessError) => {
             hilog.error(DOMAIN, TAG, `packToData failed with error message: ${err.message}, error code: ${err.code}`);
           }).finally(() => {
             fs.closeSync(file);
           });
         }).catch((error: BusinessError) => {
         hilog.error(DOMAIN, TAG, `packToData error，code ${error.code}, message is ${error.message}`);
       });
     } catch (err) {
       let e: BusinessError = err;
       hilog.error(DOMAIN, TAG,
         `write file by pixelmap error is: ${JSON.stringify(e.message)} and stack: ${JSON.stringify(e.stack)}`);
     }
   }
   ```
3. 使用[setInterval](../harmonyos-references/js-apis-timer.md#setinterval)定时器，设置时间定时执行步骤2：

   ```ts
   onPageShow(): void {
     hilog.info(DOMAIN, TAG, 'onPageShow');
     this.initImageReceiver();
     if (this.xComponentSurfaceId !== '') {
       this.initCamera();
     }
     // 将提取到的视频帧编码进应用沙箱
     setInterval(() => {
       this.packToData(this.previewImage!);
     }, this.period * 1000);
   }
   ```

完整代码如下：

```ts
import { camera } from '@kit.CameraKit';
import { image } from '@kit.ImageKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo as fs } from '@kit.CoreFileKit';
import { abilityAccessCtrl, common, Permissions } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

interface CameraResources {
  videoOutput?: camera.VideoOutput;
  cameraInput?: camera.CameraInput;
  previewOutput1?: camera.PreviewOutput;
  previewOutput2?: camera.PreviewOutput;
  session?: camera.VideoSession;
}

const DOMAIN: number = 0x0000;
const TAG: string = '[CameraDemo]';

@Entry
@Component
struct Index {
  @State isShow: boolean = false;
  private previewImage: image.PixelMap | undefined = undefined;
  private imageReceiver: image.ImageReceiver | undefined = undefined;
  private imageReceiverSurfaceId: string = '';
  private xComponentCtl: XComponentController = new XComponentController();
  private xComponentSurfaceId: string = '';
  private imageWidth: number = 1920;
  private imageHeight: number = 1080;
  private cameraManager: camera.CameraManager | undefined = undefined;
  private cameras: Array<camera.CameraDevice> | undefined = [];
  private uiContext: UIContext = this.getUIContext();
  private context: Context | undefined = this.uiContext.getHostContext();
  private cameraPermission: Permissions = 'ohos.permission.CAMERA'; // 申请权限
  private period: number = 3; // 定义提取视频帧时间间隔
  private cameraResources: CameraResources = {};

  /**
   * 向用户申请权限
   * @returns
   */
  async requestPermissionsFn(): Promise<void> {
    let atManager = abilityAccessCtrl.createAtManager();
    if (this.context) {
      let res = await atManager.requestPermissionsFromUser(this.context, [this.cameraPermission]);
      if (!res || !res.permissions || res.permissions.length === 0) {
        hilog.error(DOMAIN, TAG, 'requestPermissionsFromUser interface call fails');
        return;
      }
      if (res.permissions.length !== res.authResults.length) {
        hilog.error(DOMAIN, TAG, 'Authentication result mismatch');
        return;
      }
      res.permissions.forEach((value: string, index: number, permissions: string[]) => {
        if (this.cameraPermission.toString() === value && res.authResults[index] === 0) {
          this.isShow = true;
        }
        permissions.forEach((permission: string) => {
          hilog.info(DOMAIN, TAG, `${permission} granted`);
        });
      });
    }
  }

  aboutToAppear(): void {
    this.requestPermissionsFn();
  }

  onPageShow(): void {
    hilog.info(DOMAIN, TAG, 'onPageShow');
    this.initImageReceiver();
    if (this.xComponentSurfaceId !== '') {
      this.initCamera();
    }
    // 将提取到的视频帧编码进应用沙箱
    setInterval(() => {
      this.packToData(this.previewImage!);
    }, this.period * 1000);
  }

  onPageHide(): void {
    hilog.info(DOMAIN, TAG, 'onPageHide');
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
            hilog.info(DOMAIN, TAG, 'onLoad is called');
            this.xComponentSurfaceId = this.xComponentCtl.getXComponentSurfaceId(); // 获取组件surfaceId
            // 初始化相机，组件实时渲染每帧预览流数据
            this.initCamera();
          })
          .width(this.uiContext.px2vp(this.imageHeight))
          .height(this.uiContext.px2vp(this.imageWidth))
      }
    }
    .justifyContent(FlexAlign.Center)
    .height('100%')
    .width('100%')
  }

  /**
   * 获取ImageReceiver的SurfaceId
   * @returns
   */
  async initImageReceiver(): Promise<void> {
    if (!this.imageReceiver) {
      // 创建ImageReceiver
      let size: image.Size = { width: this.imageWidth, height: this.imageHeight };
      try {
        this.imageReceiver = image.createImageReceiver(size, image.ImageFormat.JPEG, 8);
      } catch (error) {
        let err = error as BusinessError;
        hilog.error(DOMAIN, TAG, `Init image receiver failed. error code: ${err.code}`);
        return;
      }
      // 获取第一路流SurfaceId
      this.imageReceiverSurfaceId = await this.imageReceiver.getReceivingSurfaceId();
      hilog.info(DOMAIN, TAG, `initImageReceiver imageReceiverSurfaceId:${this.imageReceiverSurfaceId}`);
      // 注册监听处理预览流每帧图像数据
      this.onImageArrival(this.imageReceiver);
    }
  }

  // Image格式与PixelMap格式映射关系
  private formatToPixelMapFormatMap = new Map<number, image.PixelMapFormat>([
    [12, image.PixelMapFormat.RGBA_8888],
    [25, image.PixelMapFormat.NV21],
    [35, image.PixelMapFormat.YCBCR_P010],
    [36, image.PixelMapFormat.YCRCB_P010]
  ]);
  // PixelMapFormat格式的单个像素点大小映射关系
  private pixelMapFormatToSizeMap = new Map<image.PixelMapFormat, number>([
    [image.PixelMapFormat.RGBA_8888, 4],
    [image.PixelMapFormat.NV21, 1.5],
    [image.PixelMapFormat.YCBCR_P010, 3],
    [image.PixelMapFormat.YCRCB_P010, 3]
  ]);

  /**
   * 将PixelMap对象的图片数据保存至应用沙箱路径
   * @param pixelMap 需要保存的pixelMap对象
   * @returns
   */
  async packToData(pixelMap: PixelMap) {
    try {
      let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
      let cacheDir: string = context.cacheDir;
      let now = Date.now();
      let fileUrl = cacheDir + `/${now}_packToData.jpg`;
      if (fs.accessSync(fileUrl)) {
        fs.unlinkSync(fileUrl);
      }
      let packOpts: image.PackingOption = { format: 'image/jpeg', quality: 98 };
      const imagePackerApi: image.ImagePacker = image.createImagePacker();
      imagePackerApi.packToData(pixelMap, packOpts)
        .then((data: ArrayBuffer) => {
          let file = fs.openSync(fileUrl, fs.OpenMode.READ_WRITE | fs.OpenMode.CREATE);
          fs.write(file.fd, data).then((writeLen: number) => {
            hilog.info(DOMAIN, TAG, `packToData succeed and size is: ${writeLen}, path is ${fileUrl}}`);
          }).catch((err: BusinessError) => {
            hilog.error(DOMAIN, TAG, `packToData failed with error message: ${err.message}, error code: ${err.code}`);
          }).finally(() => {
            fs.closeSync(file);
          });
        }).catch((error: BusinessError) => {
        hilog.error(DOMAIN, TAG, `packToData error，code ${error.code}, message is ${error.message}`);
      });
    } catch (err) {
      let e: BusinessError = err;
      hilog.error(DOMAIN, TAG,
        `write file by pixelmap error is: ${JSON.stringify(e.message)} and stack: ${JSON.stringify(e.stack)}`);
    }
  }

  /**
   * 注册ImageReceiver图像监听
   * @param receiver
   * @returns
   */
  onImageArrival(receiver: image.ImageReceiver): void {
    // 注册imageArrival监听
    receiver.on('imageArrival', () => {
      hilog.info(DOMAIN, TAG, 'image arrival');
      // 获取图像
      receiver.readNextImage((err: BusinessError, nextImage: image.Image) => {
        if (err || nextImage === undefined) {
          hilog.error(DOMAIN, TAG, 'readNextImage failed');
          return;
        }
        // 解析图像内容
        nextImage.getComponent(image.ComponentType.JPEG, async (err: BusinessError, imgComponent: image.Component) => {
          if (err || imgComponent === undefined) {
            hilog.error(DOMAIN, TAG, 'getComponent failed');
          }
          if (imgComponent.byteBuffer) {
            let width = nextImage.size.width; // 获取图片的宽
            let height = nextImage.size.height; // 获取图片的高
            let stride = imgComponent.rowStride; // 获取图片的stride
            let imageFormat = nextImage.format; // 获取图片的format
            let pixelMapFormat = this.formatToPixelMapFormatMap.get(imageFormat) ?? image.PixelMapFormat.NV21;
            let mSize = this.pixelMapFormatToSizeMap.get(pixelMapFormat) ?? 1.5;
            hilog.info(DOMAIN, TAG, `getComponent with width:${width} height:${height} stride:${stride}`);
            // pixelMap创建时使用的size、srcPixelFormat需要与相机预览输出流previewProfile中的size、format保持一致，此处format以NV21格式为例
            // stride与width一致
            let pixelMap: image.PixelMap;
            if (stride === width) {
              pixelMap = await image.createPixelMap(imgComponent.byteBuffer, {
                size: { height: height, width: width },
                srcPixelFormat: pixelMapFormat,
              });
              this.previewImage = pixelMap;
            } else {
              // stride与width不一致
              const dstBufferSize = width * height * mSize; // 以NV21为例（YUV_420_SP格式的图片）YUV_420_SP内存计算公式：长x宽+(长x宽)/2
              const dstArr = new Uint8Array(dstBufferSize);
              for (let j = 0; j < height * mSize; j++) {
                const srcBuf = new Uint8Array(imgComponent.byteBuffer, j * stride, width);
                dstArr.set(srcBuf, j * width);
              }
              pixelMap = await image.createPixelMap(dstArr.buffer, {
                size: { height: height, width: width },
                srcPixelFormat: pixelMapFormat,
              });
              this.previewImage = pixelMap;
            }
          } else {
            hilog.error(DOMAIN, TAG, 'byteBuffer is null');
          }
          // 确保当前buffer没有在使用的情况下，可进行资源释放
          // 如果对buffer进行异步操作，需要在异步操作结束后再释放该资源（nextImage.release()）
          nextImage.release();
          hilog.info(DOMAIN, TAG, 'image process done');
        });
      });
    });
  }

  /**
   * 初始化相机流程
   * @returns
   */
  async initCamera(): Promise<void> {
    hilog.info(DOMAIN, TAG,
      `initCamera imageReceiverSurfaceId:${this.imageReceiverSurfaceId} xComponentSurfaceId:${this.xComponentSurfaceId}`);
    try {
      // 获取相机管理器实例
      this.cameraManager = camera.getCameraManager(this.context);
      if (!this.cameraManager) {
        hilog.error(DOMAIN, TAG, 'getCameraManager call failed');
        return;
      }
      // 获取当前设备支持的相机device列表
      this.cameras = this.cameraManager.getSupportedCameras();
      if (!this.cameras || this.cameras.length === 0) {
        hilog.error(DOMAIN, TAG, 'getSupportedCameras call failed');
        return;
      }
      let cameraDevice: camera.CameraDevice | undefined = undefined;
      this.cameras.forEach((device: camera.CameraDevice) => {
        if (device.cameraPosition === camera.CameraPosition.CAMERA_POSITION_FRONT) {
          cameraDevice = device;
          return;
        }
      });

      // 未找到前置摄像头
      if (cameraDevice === undefined) {
        hilog.error(DOMAIN, TAG, 'Front camera device not found!');
        return;
      }

      // 选择一个相机device，创建cameraInput输出对象
      this.cameraResources.cameraInput = this.cameraManager.createCameraInput(cameraDevice);
      if (!this.cameraResources.cameraInput) {
        hilog.error(DOMAIN, TAG, 'createCameraInput call failed');
        return;
      }
      // 打开相机
      await this.cameraResources.cameraInput.open();
      // 获取相机device支持的profile
      let capability: camera.CameraOutputCapability =
        this.cameraManager.getSupportedOutputCapability(cameraDevice, camera.SceneMode.NORMAL_VIDEO);
      if (!capability) {
        hilog.error(DOMAIN, TAG, 'getSupportedOutputCapability call failed');
        this.releaseCamera();
        return;
      }
      let minRatioDiff: number = 0.1;
      let surfaceRatio: number = this.imageWidth / this.imageHeight; // 最接近16:9宽高比
      let previewProfile: camera.Profile = capability.previewProfiles[0];
      // 应用开发者根据实际业务需求选择一个支持的预览流previewProfile
      // 此处以选择CAMERA_FORMAT_YUV_420_SP（NV21）格式、满足限定条件分辨率的预览流previewProfile为例
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
      this.imageWidth = previewProfile.size.width; // 更新xComponent组件的宽
      this.imageHeight = previewProfile.size.height; // 更新xComponent组件的高
      hilog.info(DOMAIN, TAG, `initCamera imageWidth: ${this.imageWidth} imageHeight: ${this.imageHeight}`);
      // 使用imageReceiverSurfaceId创建第一路预览
      this.cameraResources.previewOutput1 =
        this.cameraManager.createPreviewOutput(previewProfile, this.imageReceiverSurfaceId);
      if (!this.cameraResources.previewOutput1) {
        hilog.error(DOMAIN, TAG, 'initCamera createPreviewOutput1');
        this.releaseCamera();
        return;
      }
      // 使用xComponentSurfaceId创建第二路预览
      this.cameraResources.previewOutput2 =
        this.cameraManager.createPreviewOutput(previewProfile, this.xComponentSurfaceId);
      if (!this.cameraResources.previewOutput2) {
        hilog.error(DOMAIN, TAG, 'initCamera createPreviewOutput2');
        this.releaseCamera();
        return;
      }
      // 创建录像模式相机会话
      let session = this.cameraManager.createSession(camera.SceneMode.NORMAL_VIDEO);
      if (!session) {
        hilog.error(DOMAIN, TAG, 'session is null');
        this.releaseCamera();
        return;
      }
      this.cameraResources.session = session as camera.VideoSession;
      // 开始配置会话
      this.cameraResources.session.beginConfig();
      // 添加相机设备输入
      this.cameraResources.session.addInput(this.cameraResources.cameraInput);
      // 添加第一路预览流输出
      this.cameraResources.session.addOutput(this.cameraResources.previewOutput1);
      // 添加第二路预览流输出
      this.cameraResources.session.addOutput(this.cameraResources.previewOutput2);
      // 提交会话配置
      await this.cameraResources.session.commitConfig();
      // 开始启动已配置的输入输出流
      await this.cameraResources.session.start();
    } catch (error) {
      hilog.error(DOMAIN, TAG, `initCamera fail: ${JSON.stringify(error)}`);
      this.releaseCamera();
    }
  }

  /**
   * 释放相机相关资源
   * @returns
   */
  async releaseCamera(): Promise<void> {
    hilog.info(DOMAIN, TAG, 'releaseCamera E');
    try {
      // 停止当前会话
      await this.cameraResources.session?.stop();
    } catch (error) {
      hilog.error(DOMAIN, TAG, `session.stop call failed, error: ${JSON.stringify(error)}`);
    }
    try {
      // 释放相机输入流
      await this.cameraResources.cameraInput?.close();
    } catch (error) {
      hilog.error(DOMAIN, TAG, `camera close fail: ${JSON.stringify(error)}`);
    }
    try {
      // 释放预览输出流
      await this.cameraResources.previewOutput1?.release();
    } catch (error) {
      hilog.error(DOMAIN, TAG, `previewOutput1 release fail: ${JSON.stringify(error)}`);
    }
    try {
      // 释放拍照输出流
      await this.cameraResources.previewOutput2?.release();
    } catch (error) {
      hilog.error(DOMAIN, TAG, `previewOutput2 release fail: ${JSON.stringify(error)}`);
    }
    try {
      // 释放会话
      await this.cameraResources.session?.release();
    } catch (error) {
      hilog.error(DOMAIN, TAG, `session release fail: ${JSON.stringify(error)}`);
    }
  }
}
```

注意使用相机功能前，需要在module.json5文件中申请相机权限：

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
