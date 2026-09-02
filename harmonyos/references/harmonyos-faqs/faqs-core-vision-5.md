---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-core-vision-5
title: 如何对文本识别的文本行增加边框描边
breadcrumb: FAQ > AI功能开发 > 机器学习 > 基础视觉（Core Vision） > 如何对文本识别的文本行增加边框描边
category: harmonyos-faqs
scraped_at: 2026-09-02T15:04:39+08:00
doc_updated_at: 2026-08-13
content_hash: sha256:8382679fb3bed819187c665d8dd1b533e9d5940e5296feb60ce109c55d629ccb
---

## 问题现象

使用textRecognition对图片进行文字识别，需要对图片上识别到的文本增加边框描边的效果，如下图所示，该如何实现？

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/A3jNV2ViQBagLxchSKn6IQ/zh-cn_image_0000002628554728.png "点击放大")

## 背景知识

[textRecognition（文字识别）](../harmonyos-references/core-vision-text-recognition-api.md)：通用文字识别服务提供图像信息转换为字符信息的能力。通过拍照、扫描等光学输入方式，把各种票据、卡证、表格、报刊、书籍等印刷品文字转化为图像信息，再利用文字识别技术将图像信息转化为计算机等设备可以使用的字符信息，便于用户**提取字符内容**、**屏幕坐标**及**外框**。

[TextRecognitionResult](../harmonyos-references/core-vision-text-recognition-api.md#textrecognitionresult)：文本识别的结果信息，包括文本内容和坐标信息。

[TextLine](../harmonyos-references/core-vision-text-recognition-api.md#textline)：描述图像中的一行文本，其中value为文本行的文本内容。cornerPoints为以顺时针返回该文本行的外框位置点列表。

[Canvas对象](../harmonyos-guides/ui-js-components-canvas.md)：Canvas组件提供画布，用于自定义绘制图形。

[CanvasRenderingContext2D对象](../harmonyos-guides/ui-js-components-canvasrenderingcontext2d.md)：使用CanvasRenderingContext2D在Canvas画布组件上进行绘制，绘制对象可以是图形、文本、线段、图片等。

## 解决方案

1. 使用[textRecognition](../harmonyos-references/core-vision-text-recognition-api.md)识别图片上的文本信息：

   调用[textRecognition.recognizeText](../harmonyos-references/core-vision-text-recognition-api.md#textrecognitionrecognizetext)的API，识别图片上的文本信息。其返回结果中包含有[TextBlock](../harmonyos-references/core-vision-text-recognition-api.md#textblock)，取该属性下的value，即可得到文本识别到的文本内容。lines为该段落包含的文本行内容，其中cornerPoints属性表示了该文本行的外框位置的阵列，其单位为px。
2. 根据文本段落的外框描述阵列信息，结合[CanvasContext.strokeRect](../atomic-ascf/apis-canvas-context.md#canvascontextstrokerect)方法，绘制一个矩形。strokeRect的入参为起始点坐标x和y，矩形的宽度以及高度。

   **说明** 

   注意，该方法的单位为vp。通过上一步文字识别获取到的外框描述矩阵数据的单位为px，因此需要使用[像素单位转换](../harmonyos-references/ts-pixel-units.md)进行转换。

   这里坐标点的x即为cornerPoints[0]属性x的值，y即为cornerPoints的[0]属性y的值，矩形的宽度使用cornerPoints的[2]属性x的值减去cornerPoints的[0]属性x的值，矩形的高度则可以使用cornerPoints的[3]属性y的值减去cornerPoints的[0]属性y的值，这样即可为识别到的文本增加边框描边的效果。

   **说明** 

   因为识别到的文本段落可能会有多个，这里需要根据自己的需求，针对相应的文本段落增加上述的边框描边处理。

   完整的示例代码：

   ```ts
   import { textRecognition } from '@kit.CoreVisionKit';
   import { image } from '@kit.ImageKit';
   import { hilog } from '@kit.PerformanceAnalysisKit';
   import { BusinessError } from '@kit.BasicServicesKit';
   import { fileIo } from '@kit.CoreFileKit';
   import { photoAccessHelper } from '@kit.MediaLibraryKit';

   @Entry
   @Component
   struct Index {
     @State chooseImage: PixelMap | undefined = undefined;
     @State dataValues: string = '';
     canvasWidth: number = 300;
     canvasHeight: number = 300;
     imageWidth: number = 0;
     imageHeight: number = 0;
     private imageSource: image.ImageSource | undefined = undefined;
     private settings: RenderingContextSettings = new RenderingContextSettings(true);
     private readonly ctx: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);

     // 根据坐标进行绘图描边
     drawLineRect(cornerPoints: Array<Array<number>>, strokeColor?: string,
       fillColor?: string, lineDash?: Array<number>) {
       strokeColor = strokeColor || '#f04b3d';
       lineDash = lineDash || [];
       this.ctx.beginPath();
       this.ctx.setLineDash(lineDash);
       this.ctx.lineWidth = 3;
       this.ctx.moveTo(cornerPoints[0][0], cornerPoints[0][1]);
       this.ctx.lineTo(cornerPoints[1][0], cornerPoints[1][1]);
       this.ctx.lineTo(cornerPoints[2][0], cornerPoints[2][1]);
       this.ctx.lineTo(cornerPoints[3][0], cornerPoints[3][1]);
       this.ctx.lineTo(cornerPoints[0][0], cornerPoints[0][1]);
       this.ctx.strokeStyle = strokeColor;
       this.ctx.stroke();
       if (fillColor) {
         this.ctx.fillStyle = fillColor;
         this.ctx.fill();
       }
       this.ctx.closePath();
     }

     // 对坐标进行等比例缩放
     changeCornerPointSize(x: number, y: number) {
       const ratioX = this.canvasWidth / this.imageWidth; // X轴缩放比例
       const ratioY = this.canvasHeight / this.imageHeight; // Y轴缩放比例
       return [x * ratioX, y * ratioY];
     }

     async aboutToAppear(): Promise<void> {
       const initResult = await textRecognition.init();
       hilog.info(0x0000, 'OCRDemo', `OCR service initialization result:${initResult}`);
     }

     async aboutToDisappear(): Promise<void> {
       await textRecognition.release();
       hilog.info(0x0000, 'OCRDemo', 'OCR service released successfully');
     }

     build() {
       Column() {
         Stack() {
           Canvas(this.ctx)
             .width('100%')
             .height('100%')
         }.height('60%')

         Text(this.dataValues)
           .copyOption(CopyOptions.LocalDevice)
           .height('15%')
           .margin(10)
           .width('60%')

         Button('选择图片')
           .type(ButtonType.Capsule)
           .fontColor(Color.White)
           .alignSelf(ItemAlign.Center)
           .width('80%')
           .margin(10)
           .onClick(() => {
             // 拉起图库，获取图片资源
             this.selectImage();
           })

         Button('开始识别')
           .type(ButtonType.Capsule)
           .fontColor(Color.White)
           .alignSelf(ItemAlign.Center)
           .width('80%')
           .margin(10)
           .onClick(async () => {
             this.textRecognitionTest();
           })
       }
       .width('100%')
       .height('100%')
       .justifyContent(FlexAlign.Center)
     }

     private textRecognitionTest() {
       if (!this.chooseImage) {
         return;
       }
       // 调用文本识别接口
       let visionInfo: textRecognition.VisionInfo = {
         pixelMap: this.chooseImage
       };
       let textConfiguration: textRecognition.TextRecognitionConfiguration = {
         isDirectionDetectionSupported: false
       };
       textRecognition.recognizeText(visionInfo, textConfiguration)
         .then((data: textRecognition.TextRecognitionResult) => {
           // 识别成功，获取对应的结果
           let recognitionString = JSON.stringify(data);
           hilog.info(0x0000, 'OCRDemo', `Succeeded in recognizing text：${recognitionString}`);
           // 将结果更新到Text中显示
           this.dataValues = data.value;
           // 获取识别文本段落的外框描述阵列信息
           let point1 = this.changeCornerPointSize(data.blocks[0].lines[0].cornerPoints[0].x,
             data.blocks[0].lines[0].cornerPoints[0].y);
           let point2 = this.changeCornerPointSize(data.blocks[0].lines[0].cornerPoints[1].x,
             data.blocks[0].lines[0].cornerPoints[1].y);
           let point3 = this.changeCornerPointSize(data.blocks[0].lines[0].cornerPoints[2].x,
             data.blocks[0].lines[0].cornerPoints[2].y);
           let point4 = this.changeCornerPointSize(data.blocks[0].lines[0].cornerPoints[3].x,
             data.blocks[0].lines[0].cornerPoints[3].y);
           this.drawLineRect([point1, point2, point3, point4], '#f04b3d');
         })
         .catch((error: BusinessError) => {
           hilog.error(0x0000, 'OCRDemo', `Failed to recognize text. Code: ${error.code}, message: ${error.message}`);
           this.dataValues = `Error: ${error.message}`;
         });
     }

     private async selectImage() {
       let uri = await this.openPhoto();
       if (uri === undefined) {
         return;
       }
       this.loadImage(uri);
     }

     private openPhoto(): Promise<string> {
       return new Promise<string>((resolve) => {
         let photoPicker: photoAccessHelper.PhotoViewPicker = new photoAccessHelper.PhotoViewPicker();
         photoPicker.select({
           MIMEType: photoAccessHelper.PhotoViewMIMETypes.IMAGE_TYPE,
           maxSelectNumber: 1
         }).then((res: photoAccessHelper.PhotoSelectResult) => {
           resolve(res.photoUris[0]);
         }).catch((err: BusinessError) => {
           hilog.error(0x0000, 'OCRDemo', `Failed to get photo image uri. Code：${err.code}，message：${err.message}`);
           resolve('');
         });
       });
     }

     private loadImage(name: string) {
       setTimeout(async () => {
         let fileSource = await fileIo.open(name, fileIo.OpenMode.READ_ONLY);
         this.imageSource = image.createImageSource(fileSource.fd);
         this.chooseImage = await this.imageSource.createPixelMap();
         let imageInfo = await this.chooseImage.getImageInfo();
         this.imageWidth = imageInfo.size.width;
         this.imageHeight = imageInfo.size.height;
         console.info('width:' + this.imageWidth, 'height:' + this.imageHeight);
         this.ctx.drawImage(this.chooseImage, 0, 0, this.canvasWidth, this.canvasHeight);
       }, 100);
     }
   }
   ```
