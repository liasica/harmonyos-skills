---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-camera-34
title: 如何处理相机旋转的相关问题
breadcrumb: FAQ > 媒体开发 > 拍照和图片 > 相机开发（Camera） > 如何处理相机旋转的相关问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:41+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:1c16d75476a8858e72f6c55175a2558374da1fb6d13c6e417190efb06226aa32
---

## 问题现象

由于相机安装角度的问题，在进行相机开发时经常会遇到成像角度与预览角度不一致的问题，这时需要对最终成像进行旋转。

## 背景知识

* 进行相机开发前需申请对应的权限，具体可查看[申请相机开发的权限](../harmonyos-guides/camera-preparation.md)章节。
* 在预览时，图像旋转角度与屏幕显示旋转角度相关。系统将以原始图像方向为基线，根据相机镜头角度和屏幕显示补偿角度，旋转图像。图像旋转角度=镜头安装角度+屏幕显示补偿角度，屏幕显示补偿角度的值与屏幕旋转角度相等。具体可参考[相机旋转角度的术语](../harmonyos-guides/camera-rotation-term.md)和[适配相机旋转角度](../harmonyos-guides/camera-rotation-angle-adaptation.md)。

## 解决方案

* **场景一：使用XComponent预览图片发生旋转。**
  + **问题现象：** 在横屏状态下使用XComponent预览图片产生90度旋转。
  + **解决方案：** 使用rotate属性对展示预览流的XComponent组件进行旋转。预览流顺时针旋转了90度，需要将XComponent逆时针旋转90度，然后还需要指定XComponent的大小，防止旋转后图像拉伸变形。此外，[rotate](../harmonyos-references/ts-universal-attributes-transformation.md#rotate)还是组件的通用属性，在使用其他组件展示图像时也可以使用此属性调整角度，如Row、Image等。

* **场景二：使用ImageReceiver接收图片旋转。**
  + **问题现象：** 使用[ImageReceiver](../harmonyos-references/arkts-apis-image-imagereceiver.md)接收相机预览流图片，将获取到的YUV数据buffer解码成RGBA\_8888的图片并进行实时送显，角度与实际拍摄角度不一致，如下图所示：

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/IxqJ4pAkSjGhd06Ub2hHpQ/zh-cn_image_0000002658911793.png "点击放大")
  + **解决方案：** 目前预览流角度固定后置摄像头得到的YUV数据顺时针旋转270度。可以对buffer数据再顺时针旋转90度，使用旋转后的buffer创建[ImageSource](../harmonyos-references/arkts-apis-image-imagesource.md)，再进行解码等操作，核心代码见rotateYUVDegree90()方法，完整参考代码如下：

    ```ts
    import { BusinessError } from '@kit.BasicServicesKit';
    import { abilityAccessCtrl, common } from '@kit.AbilityKit';
    import { camera } from '@kit.CameraKit';
    import { image } from '@kit.ImageKit';

    /**
     * YUV数据旋转函数，在onImageArrival回调时调用得到新的buffer
     * @param arr 需要旋转的buffer数据
     * @param imageWidth 图片宽度
     * @param imageHeight 图片高度
     * @returns 旋转90度后的buffer数据
     */
    export function rotateYUVDegree90(arr: ArrayBuffer, imageWidth: number, imageHeight: number): ArrayBuffer {
      let yuv: Uint8Array = new Uint8Array(imageWidth * imageHeight * 3 / 2);
      let data: Uint8Array = new Uint8Array(arr);
      let i = 0;
      // 将Y分量进行旋转
      for (let x = 0; x < imageWidth; x++) {
        for (let y = imageHeight - 1; y >= 0; y--) {
          yuv[i] = data[y * imageWidth + x];
          i++;
        }
      }
      // 将颜色分量U、V进行旋转
      i = imageWidth * imageHeight * 3 / 2 - 1;
      for (let x = imageWidth - 1; x > 0; x = x - 2) {
        for (let y = 0; y < imageHeight / 2; y++) {
          yuv[i] = data[(imageWidth * imageHeight) + (y * imageWidth) + x];
          i--;
          yuv[i] = data[(imageWidth * imageHeight) + (y * imageWidth) + (x - 1)];
          i--;
        }
      }
      return yuv.buffer;
    }

    @Entry
    @Component
    struct Index {
      @State imgUrl: PixelMap | undefined = undefined;
      private flag: boolean = true;
      private photoOutput: camera.PhotoOutput | undefined = undefined;
      private captureSession: camera.Session | undefined = undefined;
      private context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
      private previewProfilesObj2: camera.Profile | undefined = undefined;
      private receiver: image.ImageReceiver | undefined = undefined;

      aboutToAppear() {
        abilityAccessCtrl.createAtManager()
          .requestPermissionsFromUser(this.getUIContext().getHostContext(), ['ohos.permission.CAMERA'])
          .then(() => {
            this.createDualChannelPreview();
          });
      }

      onPageShow(): void {
        this.createDualChannelPreview();
      }

      async createDualChannelPreview(): Promise<void> {
        let cameraManager: camera.CameraManager = camera.getCameraManager(this.context);
        // 获取支持的相机设备对象
        let camerasDevices: Array<camera.CameraDevice> = cameraManager.getSupportedCameras();
        // 获取profile对象
        let profiles: camera.CameraOutputCapability =
          cameraManager.getSupportedOutputCapability(camerasDevices[0], camera.SceneMode.NORMAL_PHOTO);
        let previewProfiles: Array<camera.Profile> = profiles.previewProfiles;
        // 预览流2
        this.previewProfilesObj2 = previewProfiles[0];
        this.receiver = image.createImageReceiver(this.previewProfilesObj2.size, 2000, 8);
        // 创建预览流2输出对象
        let imageReceiverSurfaceId: string = await this.receiver.getReceivingSurfaceId();
        let previewOutput2: camera.PreviewOutput =
          cameraManager.createPreviewOutput(this.previewProfilesObj2, imageReceiverSurfaceId);
        let photoProfilesArray: Array<camera.Profile> = profiles.photoProfiles;
        try {
          this.photoOutput = cameraManager.createPhotoOutput(photoProfilesArray[0]);
        } catch (error) {
          let err = error as BusinessError;
          console.error(`Create photoOutput error: ${err.code}`);
        }
        if (this.photoOutput === undefined) {
          return;
        }
        // 创建cameraInput对象
        let cameraInput: camera.CameraInput = cameraManager.createCameraInput(camerasDevices[0]);
        // 打开相机
        await cameraInput.open();
        // 会话流程
        this.captureSession = cameraManager.createSession(1);
        // 开始配置会话
        this.captureSession.beginConfig();
        // 把CameraInput加入到会话
        this.captureSession.addInput(cameraInput);
        // 把预览流2加入到会话
        this.captureSession.addOutput(previewOutput2);

        try {
          this.captureSession.addOutput(this.photoOutput);
        } catch (error) {
          let err = error as BusinessError;
          console.error(`Add photoOutput error: ${err.code}}`);
        }
        // 提交配置信息
        await this.captureSession.commitConfig();
        // 会话开始
        await this.captureSession.start();
        this.onImageArrival(this.receiver);
      }

      async onImageArrival(receiver: image.ImageReceiver): Promise<void> {
        // Image格式与PixelMap格式映射关系。
        let formatToPixelMapFormatMap = new Map<number, image.PixelMapFormat>([
          [12, image.PixelMapFormat.RGBA_8888],
          [25, image.PixelMapFormat.NV21],
          [35, image.PixelMapFormat.YCBCR_P010],
          [36, image.PixelMapFormat.YCRCB_P010]
        ]);
        // PixelMapFormat格式的单个像素点大小映射关系。
        let pixelMapFormatToSizeMap = new Map<image.PixelMapFormat, number>([
          [image.PixelMapFormat.RGBA_8888, 4],
          [image.PixelMapFormat.NV21, 1.5],
          [image.PixelMapFormat.YCBCR_P010, 3],
          [image.PixelMapFormat.YCRCB_P010, 3]
        ]);
        receiver.on('imageArrival', () => {
          console.info('imageArrival 接收图片触发');
          receiver.readLatestImage((err, nextImage: image.Image) => {
            if (err || nextImage === undefined) {
              return;
            }
            nextImage.getComponent(image.ComponentType.JPEG, (err, imgComponent: image.Component) => {
              if (err || imgComponent === undefined) {
                return;
              }
              if (this.flag) {
                if (imgComponent.byteBuffer as ArrayBuffer) {
                  let width = nextImage.size.width; // 获取图片的宽。
                  let height = nextImage.size.height; // 获取图片的高。
                  let stride = imgComponent.rowStride; // 获取图片的stride。
                  let imageFormat = nextImage.format; // 获取图片的format。
                  let pixelMapFormat = formatToPixelMapFormatMap.get(imageFormat) ?? image.PixelMapFormat.NV21;
                  let mSize = pixelMapFormatToSizeMap.get(pixelMapFormat) ?? 1.5;
                  let sourceOptions: image.SourceOptions = {
                    sourceDensity: 120,
                    sourcePixelFormat: 8,
                    sourceSize: {
                      height: this.previewProfilesObj2!.size.height,
                      width: this.previewProfilesObj2!.size.width
                    },
                  };
                  let decodingOptions: image.DecodingOptions = {
                    editable: true,
                    desiredPixelFormat: 3,
                  };
                  if (stride == width) {
                    // 调用旋转函数
                    let buffer: ArrayBuffer =
                      rotateYUVDegree90(imgComponent.byteBuffer, this.previewProfilesObj2!.size.width,
                        this.previewProfilesObj2!.size.height);
                    let imageResource = image.createImageSource(buffer, sourceOptions);
                    imageResource.createPixelMap(decodingOptions).then((res) => {
                      this.imgUrl = res;
                    });
                  } else { // stride与width不一致。
                    const dstBufferSize = width * height * mSize;
                    const dstArr = new Uint8Array(dstBufferSize);
                    for (let j = 0; j < height * mSize; j++) {
                      const srcBuf = new Uint8Array(imgComponent.byteBuffer, j * stride, width);
                      dstArr.set(srcBuf, j * width);
                    }
                    // 调用旋转函数
                    let buffer: ArrayBuffer =
                      rotateYUVDegree90(dstArr.buffer as ArrayBuffer, this.previewProfilesObj2!.size.width,
                        this.previewProfilesObj2!.size.height);
                    let imageResource = image.createImageSource(buffer, sourceOptions);
                    imageResource.createPixelMap(decodingOptions).then((res) => {
                      this.imgUrl = res;
                    });
                  }
                } else {
                  return;
                }
              }
              nextImage.release();
            });
          });
        });
      }

      build() {
        Column() {
          Row() {
            // 将编辑好的pixelMap传递给状态变量imgUrl后，通过Image组件进行渲染
            Image(this.imgUrl).objectFit(ImageFit.Cover).width('100%').height('50%')
          }.backgroundColor('#F0F0F0')

          Row({ space: 20 }) {
            Button('暂停预览').onClick(() => {
              this.flag = false;
            })
              .width(100)
              .height(100)

            Button('继续预览').onClick(() => {
              this.flag = true;
            })
              .width(100)
              .height(100)
          }
          .margin({ top: 20 })
        }
      }
    }
    ```

    旋转之后的预览图像如下图所示：

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/j8xdnfApSGetHU-LZRvV2A/zh-cn_image_0000002628392580.png "点击放大")
* **场景三：视频通话旋转。**
  + **问题现象：** 两个设备之间进行视频通话，存在设备间持握方向不一致问题，导致一端看到的另一端画面是颠倒的。
  + **解决方案：** 在本端将画面转正，再通过网络发送到对端，可以使用libyuv三方库进行自绘制场景预览角度的归一化处理。
