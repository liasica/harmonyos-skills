---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-camera-60
title: 不拉起相机实现无感拍照
breadcrumb: FAQ > 媒体开发 > 拍照和图片 > 相机开发（Camera） > 不拉起相机实现无感拍照
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:41+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:a82e5d4e3ebf71531fe46e93b09f01eac4f1b8a53cf5b90b73500297c7792e0d
---

## 问题现象

教育类应用需要在考试界面定时拍摄，以监测答题者是否有作弊行为，但是因为不想打断考试过程，所以想要在不拉起预览界面的情况下完成拍照，请问是否有可行的方案？

## 背景知识

* 在开发相机应用时，需要先[申请相关权限](../harmonyos-guides/camera-preparation.md)。
* [双路预览(ArkTS)](../harmonyos-guides/camera-dual-channel-preview.md)：双路预览，即应用可同时使用两路预览流，一路用于在屏幕上显示，一路用于图像处理等其他操作，提升处理效率。本文主要使用ImageReceiver的那一路预览流，移除掉XComponent那一路送显的预览流。

## 解决方案

业务场景要求不拉起相机实现无感拍照，其实主要是不能拉起XComponent预览界面，因此可以在双路预览方案的基础上，移除XComponent那一路送显的流，仅通过ImageReceiver那一路流去获取并处理相机拍摄到的帧数据。

示例代码如下：

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
  previewOutput?: camera.PreviewOutput;
  session?: camera.VideoSession;
}

const DOMAIN: number = 0x0000;
const TAG: string = '[CameraDemo]';

@Entry
@Component
struct Index {
  private imageReceiver: image.ImageReceiver | undefined = undefined;
  private imageReceiverSurfaceId: string = '';
  private imageWidth: number = 1080;
  private cameraManager: camera.CameraManager | undefined = undefined;
  private cameras: Array<camera.CameraDevice> | undefined = [];
  private uiContext: UIContext = this.getUIContext();
  private context: Context | undefined = this.uiContext.getHostContext();
  private cameraPermission: Permissions = 'ohos.permission.CAMERA'; // 申请权限
  private period: number = 10; // 定义提取视频帧时间间隔
  private canIProcess: boolean = false; // 是否需要处理ImageReceiver回图
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
      res.permissions.forEach((value: string, index: number) => {
        if (this.cameraPermission.toString() === value && res.authResults[index] !== 0) {
          this.context?.getApplicationContext().killAllProcesses();
        }
      });
    }
  }

  async aboutToAppear(): Promise<void> {
    await this.requestPermissionsFn();
    hilog.info(DOMAIN, TAG, 'aboutToAppear');
    await this.initImageReceiver();
    await this.initCamera();
    // 设置定时器，定时更新状态位
    setInterval(() => {
      this.canIProcess = true;
    }, this.period * 1000);
  }

  aboutToDisappear(): void {
    hilog.info(DOMAIN, TAG, 'aboutToDisappear');
    this.releaseCamera();
  }

  build() {
    Column() {
      Text('业务UI界面').font({size: 30, style: FontStyle.Italic})
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
      let size: image.Size = { width: this.imageWidth, height: this.imageWidth };
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
      // 获取并处理当前图像
      receiver.readNextImage((err: BusinessError, nextImage: image.Image) => {
        if (err || nextImage === undefined) {
          hilog.error(DOMAIN, TAG, 'readNextImage failed');
          return;
        }
        hilog.info(DOMAIN, TAG, `image arrived, can i process: ${this.canIProcess}.`);
        // 如果当前状态为无需处理，则在释放资源后直接跳过以减轻能耗负载。
        if (!this.canIProcess) {
          // 注意跳过处理时必须在这里手动释放资源，否则会因为消费端数据堆积而阻塞bufferQueue队列轮转
          nextImage.release();
          return;
        }
        this.canIProcess = false; // 如果当前需要处理，则先将状态位更新为无需处理后再处理当前帧数据，防止处理时间过长导致状态更新不及时
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
            let pixelMap: image.PixelMap;
            // stride与width一致
            if (stride === width) {
              pixelMap = await image.createPixelMap(imgComponent.byteBuffer, {
                size: { height: height, width: width },
                srcPixelFormat: pixelMapFormat,
              });
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
            }
            await this.packToData(pixelMap!); // 保存图片
            await pixelMap.release(); // 释放资源
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
    hilog.info(DOMAIN, TAG, `initCamera imageReceiverSurfaceId:${this.imageReceiverSurfaceId}`);
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
        hilog.error(DOMAIN, TAG, 'Back camera device not found!');
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
        this.cameraManager.getSupportedOutputCapability(cameraDevice, camera.SceneMode.NORMAL_PHOTO);
      if (!capability) {
        hilog.error(DOMAIN, TAG, 'getSupportedOutputCapability call failed');
        this.releaseCamera();
        return;
      }
      // 筛选预览Profile。这里筛选分辨率宽高比1:1，且分辨率>=1080的Profile，开发者可根据业务需要自定义筛选逻辑。
      let previewProfile = capability.previewProfiles.find((profile: camera.Profile) => {
        return profile.size.width === profile.size.height && profile.size.width >= this.imageWidth;
      });
      // 使用imageReceiverSurfaceId创建预览
      this.cameraResources.previewOutput =
        this.cameraManager.createPreviewOutput(previewProfile, this.imageReceiverSurfaceId);
      if (!this.cameraResources.previewOutput) {
        hilog.error(DOMAIN, TAG, 'initCamera createPreviewOutput');
        this.releaseCamera();
        return;
      }
      // 创建录像模式相机会话
      let session = this.cameraManager.createSession(camera.SceneMode.NORMAL_PHOTO);
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
      // 添加ImageReceiver预览流输出
      this.cameraResources.session.addOutput(this.cameraResources.previewOutput);
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
      await this.cameraResources.previewOutput?.release();
    } catch (error) {
      hilog.error(DOMAIN, TAG, `previewOutput release fail: ${JSON.stringify(error)}`);
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

## 常见FAQ

Q：代码中canIProcess参数的作用是什么？是否必须要有？

A：on('imageArrival')回调中涉及到PixelMap的创建和处理，这些操作耗费资源比较严重，如果持续处理会对性能造成不小的负担，因此使用canIProcess配合定时器的方式，隔一段时间处理一帧，这样处理既可以节约性能，又与业务场景相契合。考虑到考试场景可能耗时较久，建议还是参考这个处理思路，但如果业务处理逻辑不需要做繁杂的PixelMap处理，也可以考虑移除这套控制逻辑。
