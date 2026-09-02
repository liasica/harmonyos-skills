---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkgraphics-2d-39
title: Canvas图片绘制的常见使用场景
breadcrumb: FAQ > 图形开发 > 2D图形（ArkGraphics 2D） > Canvas图片绘制的常见使用场景
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:47+08:00
doc_updated_at: 2026-08-13
content_hash: sha256:8397099ecb0ebc39ebeb255bdddec20909fcea1ed0614e2a08a3b3d0097eee0c
---

## 问题现象

开发者在使用Canvas进行图片绘制时，可能会遇到以下几类场景：

* 场景一：如何在Canvas上绘制项目资源中的图片，并调整其大小以铺满整个画布？
* 场景二：如何将Canvas绘制的图片转换为Base64字符串？
* 场景三：如何将Canvas绘制的图片导出为PNG格式并保存至设备相册？

## 背景知识

* [Canvas](../harmonyos-references/ts-components-canvas-canvas.md)：提供画布组件，用于自定义绘制图形，开发者使用[CanvasRenderingContext2D](../harmonyos-references/ts-canvasrenderingcontext2d.md)对象和[OffscreenCanvasRenderingContext2D](../harmonyos-references/ts-offscreencanvasrenderingcontext2d.md)对象在Canvas组件上进行绘制，绘制对象可以是基础形状、文本、图片等。
* [getPixelMap](../harmonyos-references/ts-components-canvas-common-method.md#getpixelmap)：以当前Canvas指定区域内的像素创建PixelMap对象。
* [Image Kit](../harmonyos-guides/image-overview.md)：提供了对图片文件进行解析、处理、重新构造的能力。
* [drawImage](../harmonyos-references/ts-components-canvas-common-method.md#drawimage)：提供了多种绘制模式，可根据实际需求，对图像进行完整绘制、拉伸/压缩绘制，或先进行裁剪再进行拉伸/压缩绘制，灵活适应不同场景下的图像处理需求。

## 解决方案

* 场景一：如何在Canvas上绘制项目资源中的图片，并调整其大小以铺满整个画布？
  1. 调用getMediaContentSync接口获取图像数据，并通过图像解码机制将其转换为PixelMap实例。
  2. 利用drawImage方法将PixelMap图像绘制至Canvas画布；当图像的原始尺寸与画布尺寸完全匹配时，图像将被完整填充画布区域。

  ```ts
  import { image } from '@kit.ImageKit';

  const canvas_width = 400;
  const canvas_heith = canvas_width / 2;

  @Entry
  @Component
  export struct Index1 {
    private settings: RenderingContextSettings = new RenderingContextSettings(true);
    private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
    private contextFull: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
    async drawImage() {
      // 获取媒体内容（这里是启动图标）
      const fileData: Uint8Array =
        this.getUIContext().getHostContext()?.resourceManager.getMediaContentSync($r('app.media.startIcon').id) as Uint8Array;
      // 将文件数据转换为缓冲区
      const buffer = fileData.buffer;
      // 创建图像源对象
      const imageSource: image.ImageSource = image.createImageSource(buffer);
      // 设置解码选项
      let opts: image.DecodingOptions = {
        // 是否可编辑
        editable: true,
        // 目标大小
        desiredSize: {
          height: 400,
          width: 400
        }
      };
      // 创建像素映射对象
      const pixelMap: image.PixelMap = await imageSource.createPixelMap(opts);
      // 完整绘制：参数对应绘制区域左上角在x/y轴的位置
      this.context.drawImage(pixelMap, 100, 0);
      // 拉伸绘制：参数对应绘制区域左上角在x/y轴的位置以及绘制区域的宽度和高度
      this.contextFull.drawImage(pixelMap, 0, 0, canvas_width, canvas_heith);
    }
    build() {
      Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Start }) {
        Canvas(this.context)
          .backgroundColor('#F5DC62')
          .height('30%');
        Row().height('30%');
        Canvas(this.contextFull)
          .backgroundColor('#F5DC62')
          .onReady(() => {
            this.drawImage();
          })
          .width(canvas_width)
          .height(canvas_heith);
      };
    }
  }
  ```
* 场景二：如何将Canvas绘制的图片转换为Base64字符串？
  1. 使用packToData接口将PixelMap转换为ArrayBuffer格式的二进制数据。
  2. 使用Uint8Array接口创建一个指向该ArrayBuffer的视图，从而获得一个无符号整数数组。
  3. 通过Base64Helper的encodeToStringSync接口，将该Uint8Array编码为Base64格式的字符串。

  ```ts
  import { image } from '@kit.ImageKit';
  import { util } from '@kit.ArkTS';

  @Entry
  @Component
  struct Index2 {
    private settings: RenderingContextSettings = new RenderingContextSettings(true);
    private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
    @State picBase64: string = '';
    // PixelMap转base64实现代码
    async pixelToBase64(data: PixelMap): Promise<string> {
      const imagePackerApi: image.ImagePacker = image.createImagePacker();
      let packOpts: image.PackingOption = { format: 'image/png', quality: 100 };
      try {
        let readBuffer: ArrayBuffer = await imagePackerApi.packToData(data, packOpts);
        let bufferArr = new Uint8Array(readBuffer);
        let help = new util.Base64Helper;
        let base = help.encodeToStringSync(bufferArr);
        return base;
      } catch (err) {
        return '';
      }
    }

    build() {
      Scroll() {
        Column() {
          Canvas(this.context)
            .width(300)
            .height(300)
            .backgroundColor('#ffffff')
            .onReady(() => {
              let grad = this.context.createConicGradient(0, 50, 80);
              grad.addColorStop(0.0, '#ff0000');
              grad.addColorStop(0.5, '#ffffff');
              grad.addColorStop(1.0, '#00ff00');
              this.context.fillStyle = grad;
              this.context.fillRect(0, 30, 100, 100);
            });
          // 显示base64字符串
          Text(this.picBase64);
          // 将base64字符串显示为图片
          if (this.picBase64 != '') {
            Image('data:image/png;base64,' + this.picBase64);
          }
          Button('获取图片数据Base64')
            .onClick(async () => {
              let width = this.context.width;
              let height = this.context.height;
              let pixelmap = this.context.getPixelMap(0, 0, width, height);
              let str = await this.pixelToBase64(pixelmap);
              this.picBase64 = str;
            });
        };
      }
      .width('100%')
      .height('100%');
    }
  }
  ```
* 场景三：如何将Canvas绘制的图片导出为PNG格式并保存至设备相册？
  1. 使用OffscreenCanvas创建一个离屏渲染的画布，并获取其绘图上下文，用于绘制图像。
  2. 通过getPixelMap方法获取指定区域的像素数据，生成PixelMap对象。
  3. 利用ImagePacker中的packToData方法，将像素数据编码为PNG格式，确保未绘制区域保持透明。
  4. 通过文件管理接口创建并打开一个新文件，将生成的PNG图片数据写入该文件，完成后关闭文件。
  5. 调用showAssetsCreationDialog以获取相册保存权限的URI，然后将沙箱目录中的图片写入设备相册。

  ```ts
  import { image } from '@kit.ImageKit';
  import { fileIo, fileUri, ReadOptions, WriteOptions } from '@kit.CoreFileKit';
  import { photoAccessHelper } from '@kit.MediaLibraryKit';

  @Entry
  @Component
  export struct Index3 {
    message: string = 'hello world!';
    private settings: RenderingContextSettings = new RenderingContextSettings(true);
    private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
    private offCanvas: OffscreenCanvas = new OffscreenCanvas(300, 300);
    private offContext?: OffscreenCanvasRenderingContext2D;

    build() {
      Column() {
        Canvas(this.context)
          .height(300)
          .width('100%')
          .onReady(() => {
            this.offContext = this.offCanvas.getContext('2d', this.settings);
            this.offContext.fillStyle = 'rgb(255,0,0)';
            this.offContext.fillRect(0, 0, this.context.width, this.context.height);
            this.offContext.fillStyle = 'rgb(255,255,255)';
            this.offContext.font = '60px sans-serif';
            this.offContext.textAlign = 'start';
            this.offContext.textBaseline = 'top';
            this.offContext.fillText(this.message, 100, 100);
            this.context.transferFromImageBitmap(this.offCanvas.transferToImageBitmap());
          });

        Button('保存图片')
          .onClick(() => {
            this.onSave();
          });
      }
      .alignItems(HorizontalAlign.Center);
    }

    async onSave() {
      if (this.offContext) {
        const pixelMap: image.PixelMap =
          this.offContext.getPixelMap(0, 0, 300, 300);
        const imagePackerApi = image.createImagePacker();
        // 此处支持jpg、jpeg等格式
        const buffer = await imagePackerApi.packToData(pixelMap, { format: 'image/png', quality: 100 });
        const filePath = this.getUIContext().getHostContext()?.filesDir + `/${(new Date).getTime()}.png`;
        try {
          const file = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
          fileIo.writeSync(file.fd, buffer);
          fileIo.closeSync(file.fd);
          const config: photoAccessHelper.PhotoCreationConfig[] = [];
          config.push({
            fileNameExtension: 'png',
            photoType: photoAccessHelper.PhotoType.IMAGE,
          });
          const phAccessHelper = photoAccessHelper.getPhotoAccessHelper(this.getUIContext().getHostContext());
          const srcUri = [fileUri.getUriFromPath(filePath)];
          const desUris = await phAccessHelper.showAssetsCreationDialog(srcUri, config);
          this.copyToPhoto(filePath, desUris[0]);

        } catch (error) {
          console.error(JSON.stringify(error));
        }
      }
    }

    // 保存到指定路径
    copyToPhoto(srcFilePath: string, destFilePath: string) {
      const srcFile = fileIo.openSync(srcFilePath, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
      const destFile = fileIo.openSync(destFilePath, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
      // 读取源文件内容并写入至目的文件
      const stat = fileIo.statSync(srcFilePath);
      const bufSize = stat.size;
      let readSize = 0;
      const buf = new ArrayBuffer(bufSize);
      const readOptions: ReadOptions = {
        offset: readSize,
        length: bufSize
      };
      let readLen = fileIo.readSync(srcFile.fd, buf, readOptions);
      while (readLen > 0) {
        readSize += readLen;
        let writeOptions: WriteOptions = {
          length: readLen
        };
        fileIo.writeSync(destFile.fd, buf, writeOptions);
        readOptions.offset = readSize;
        readLen = fileIo.readSync(srcFile.fd, buf, readOptions);
      }
      // 关闭文件
      fileIo.closeSync(srcFile);
      fileIo.closeSync(destFile);
    }
  }
  ```
