---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-scan-kit-new-00001
title: 如何获取扫码成功的那一帧图像
breadcrumb: FAQ > 媒体开发 > 拍照和图片 > 扫码服务（Scan） > 如何获取扫码成功的那一帧图像
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:43+08:00
doc_updated_at: 2026-08-13
content_hash: sha256:cdab215cd9c4e3219362df52a2253800698ae51513606d0c888974a432c6c364
---

## 问题现象

应用除了需要扫码获取码值之外，还需要获取扫码成功的码图图像，以便归档。应该如何获取扫码成功的那一帧图像？

## 背景知识

* 在开发相机应用时，需要先[申请相关权限](../harmonyos-guides/camera-preparation.md)。
* [双路预览(ArkTS)](../harmonyos-guides/camera-dual-channel-preview.md)：双路预览，即应用可同时使用两路预览流，一路用于在屏幕上显示，一路用于图像处理等其他操作，提升处理效率。
* [识别图像数据](../harmonyos-guides/scan-decodeimage.md)：图像数据识码能力支持对相机预览流数据中的条形码、二维码、MULTIFUNCTIONAL CODE进行识别，并获得码类型、码值、码位置、相机变焦比等信息。该能力可用于一图单码和一图多码的识别，比如条形码、付款码等。

## 解决方案

当前[customScan.start](../harmonyos-references/scan-customscan-api.md#start-1)支持获取扫码的图像流，但是不能保证获取到稳定清晰的码图图像，因此本文主要介绍的是如何使用双路预览+图像识码的方式来完成码图识别和码图保存。

本文主要思路是利用双路预览中用于图像处理的那一路预览流，从中获取图像帧数据，获取数据后调用图像识码的接口，如果成功识别到码值则将解析出来的码值返回以供后续业务处理，同时保留当前的帧图像作为码图留档。

样例代码如下：

```ts
import { camera } from '@kit.CameraKit';
import { image } from '@kit.ImageKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo as fs } from '@kit.CoreFileKit';
import { abilityAccessCtrl, common, Permissions } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { detectBarcode, scanBarcode, scanCore } from '@kit.ScanKit';

interface CameraResources {
  videoOutput?: camera.VideoOutput;
  cameraInput?: camera.CameraInput;
  previewOutput1?: camera.PreviewOutput;
  previewOutput2?: camera.PreviewOutput;
  session?: camera.VideoSession;
}

const DOMAIN: number = 0x0000;
const TAG: string = '[CameraDemo]';

let zoomRatioRange: number[] = []; // 变焦比范围
let currentFov: number = 1; // 当前变焦比

@Entry
@Component
struct Index {
  @State isShow: boolean = false;
  @State zoom: number = 1; // 当前缩放值
  @State isShowZoom: boolean = false; // 是否显示缩放提示
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
  private cameraResources: CameraResources = {};
  private cameraPosition = camera.CameraPosition.CAMERA_POSITION_BACK; //后置相机
  private isFind: boolean = false;

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

  async onPageShow(): Promise<void> {
    this.isFind = false;
    hilog.info(DOMAIN, TAG, 'onPageShow');
    this.initImageReceiver();
    if (this.xComponentSurfaceId !== '') {
      this.initCamera();
    }
  }

  onPageHide(): void {
    this.isFind = false;
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
          .gesture(
            PinchGesture({ fingers: 2 })
              .onActionUpdate((event: GestureEvent) => {
                if (event) {
                  // 根据手势缩放比例计算新变焦比
                  this.zoom = currentFov * event.scale;
                  this.isShowZoom = true;
                  // 限制变焦比在有效范围内
                  if (this.zoom > zoomRatioRange[1]) {
                    this.zoom = zoomRatioRange[1];
                  } else if (this.zoom < zoomRatioRange[0]) {
                    this.zoom = zoomRatioRange[0];
                  }
                  // 调用相机接口设置变焦比
                  this.cameraResources.session?.setZoomRatio(this.zoom);
                }
              })
              .onActionEnd(() => {
                // 手势结束时更新当前变焦比
                if (this.cameraResources.session) {
                  currentFov = this.cameraResources.session.getZoomRatio();
                }
                this.isShowZoom = false;
              })
          )
          .renderFit(RenderFit.RESIZE_CONTAIN)
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

  async barcodeRecognized(imgBuffer: ArrayBuffer, width: number, height: number): Promise<string | undefined> {
    let scanResult: string | undefined = undefined;
    let byteImg: detectBarcode.ByteImage = {
      byteBuffer: imgBuffer,
      width: width,
      height: height,
      format: detectBarcode.ImageFormat.NV21
    };
    let options: scanBarcode.ScanOptions = {
      scanTypes: [scanCore.ScanType.ALL],
      enableMultiMode: true,
      enableAlbum: false
    };
    try {
      await detectBarcode.decodeImage(byteImg, options).then((data: detectBarcode.DetectResult) => {
        hilog.info(DOMAIN, TAG,
          `Succeeded in getting DetectResult by promise with options, result is ${JSON.stringify(data)}`);
        scanResult = data.scanResults[0].originalValue; // 这里默认选择扫码结果的第一条，应用可根据实际情况修改。
      }).catch((err: BusinessError) => {
        hilog.error(DOMAIN, TAG,
          `Failed to get DetectResult by promise with options. Code: ${err.code}, message: ${err.message}`);
      });
    } catch (err) {
      hilog.error(DOMAIN, TAG, `Failed to detectBarcode. Code: ${err.code}, message: ${err.message}`);
    }
    return scanResult;
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
            hilog.error(DOMAIN, TAG, 'getComponent failed.');
          }
          if (!imgComponent.byteBuffer || this.isFind) { // 如果buffer为空或者已经找到扫码成功的那一帧图片，则直接退出
            nextImage.release();
            hilog.error(DOMAIN, TAG, 'getImage failed.');
            return;
          }

          let width = nextImage.size.width; // 获取图片的宽
          let height = nextImage.size.height; // 获取图片的高
          let stride = imgComponent.rowStride; // 获取图片的stride
          let imageFormat = nextImage.format; // 获取图片的format
          // 处理stride对齐
          hilog.info(DOMAIN, TAG, `getComponent with width:${width} height:${height} stride:${stride}`);
          let pixelMapFormat = this.formatToPixelMapFormatMap.get(imageFormat) ?? image.PixelMapFormat.NV21;
          let mSize = this.pixelMapFormatToSizeMap.get(pixelMapFormat) ?? 1.5;
          let imgBuffer = imgComponent.byteBuffer;
          if (stride != width) {
            const dstBufferSize = width * height * mSize; // 以NV21为例（YUV_420_SP格式的图片）YUV_420_SP内存计算公式：长x宽+(长x宽)/2
            const dstArr = new Uint8Array(dstBufferSize);
            for (let j = 0; j < height * mSize; j++) {
              const srcBuf = new Uint8Array(imgComponent.byteBuffer, j * stride, width);
              dstArr.set(srcBuf, j * width);
            }
            imgBuffer = dstArr.buffer as ArrayBuffer;
          }
          // 尝试扫码获取结果
          let scanResult = await this.barcodeRecognized(imgBuffer, width, height);
          if (scanResult) {
            // pixelMap创建时使用的size、srcPixelFormat需要与相机预览输出流previewProfile中的size、format保持一致，此处format以NV21格式为例
            let pixelMap: image.PixelMap;
            pixelMap = await image.createPixelMap(imgBuffer, {
              size: { height: height, width: width },
              srcPixelFormat: pixelMapFormat,
            });
            this.packToData(pixelMap);
            this.isFind = true;
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
        if (device.cameraPosition === this.cameraPosition) {
          cameraDevice = device;
          return;
        }
      });

      // 未找到后置摄像头
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
      let bestPixels: number = 0;
      // 不限定格式，在宽高比匹配的所有profile中选择分辨率最高的，以获得最清晰的预览图像
      for (let index = 0; index < capability.previewProfiles.length; index++) {
        const tempProfile = capability.previewProfiles[index];
        let tempRatio = tempProfile.size.width >= tempProfile.size.height ?
          tempProfile.size.width / tempProfile.size.height : tempProfile.size.height / tempProfile.size.width;
        let currentRatio = Math.abs(tempRatio - surfaceRatio);
        let pixels = tempProfile.size.width * tempProfile.size.height;
        if (currentRatio <= minRatioDiff && pixels > bestPixels &&
          tempProfile.format === camera.CameraFormat.CAMERA_FORMAT_YUV_420_SP &&
          tempProfile.size.width >= this.imageWidth
        ) {
          previewProfile = tempProfile;
          bestPixels = pixels;
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
      // 初始化相机并获取变焦比范围
      zoomRatioRange = this.cameraResources.session.getZoomRatioRange();
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

## **常见FAQ**

Q：如何通过[customScan.start](../harmonyos-references/scan-customscan-api.md#start-1)接口的frameCallback回调去获取扫码成功的那一帧图像？

A：当前还无法精准获取识别成功的码图图像，可关注Scan Kit后续的版本迭代。

Q：通过Demo保存的码图图像为什么有一些看起来很模糊，甚至是不完整的码图？

A：通过该样例保存的码图都能被系统识别，保存的图片可能看起来模糊或者缺损，但实际上并不影响码图识别。可将码图适当放大，然后使用搭载HarmonyOS系统的设备扫描码图，看是否能否识别出码值。
