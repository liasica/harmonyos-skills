---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-739
title: 如何实现为图片添加马赛克的效果
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何实现为图片添加马赛克的效果
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:20+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:2eb42206f9eac40cabe881d2c979640fe83948c69e6c204dfc871128d325b6cd
---

## 问题现象

从图库中选择手机相册图片，加载成功后展示在首页。为了保护隐私，用户可以在图片上触摸添加马赛克，并且绘制完成后可以实现撤销。如何实现该效果？

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/d_nqh0pUQHO9kgChBG1YVA/zh-cn_image_0000002628395464.gif "点击放大")

## 背景知识

* [相册管理模块](../harmonyos-references/js-apis-photoaccesshelper.md)提供了相册管理能力，包括创建相册、访问和修改相册中的媒体数据，可通过[PhotoViewPicker](../harmonyos-references/arkts-apis-photoaccesshelper-photoviewpicker.md)图库选择器对象来选择图片。
* [Canvas](../harmonyos-references/ts-components-canvas-canvas.md)提供画布组件，用于自定义绘制图形。该组件可通过[CanvasRenderingContext2D](../harmonyos-references/ts-canvasrenderingcontext2d.md)在Canvas组件上进行绘制，绘制对象可以是矩形、文本、图片等。
* [getImageData](../harmonyos-references/js-components-canvas-canvasrenderingcontext2d.md#getimagedata)：以当前Canvas指定区域内的像素创建ImageData对象。

## 解决方案

1. 通过PhotoViewPicker打开图库选择图片。

   ```ts
   // 选择图片
   private async selectImage() {
     // picker拉起图库，选择图片
     const picker = new photoAccessHelper.PhotoViewPicker();
     const result = await picker.select({
       maxSelectNumber: 1,
       MIMEType: photoAccessHelper.PhotoViewMIMETypes.IMAGE_TYPE
     });
     if (!result.photoUris.length) {
       return;
     }
     this.processImage(result.photoUris[0]);
   }
   ```
2. 使用Canvas组件绘制图片。

   ```ts
   // 绘制图片
   private clearAndDraw() {
     this.myPen.clearRect(0, 0, this.canvasWidth, this.canvasHeight);
     if (this.maskUri) {
       this.myPen.drawImage(new ImageBitmap(this.maskUri), 0, 0, this.canvasWidth, this.canvasHeight);
     }
   }
   ```
3. 为Canvas组件补充onTouch触摸事件监听，通过getImageData方法获取触摸点处的像素颜色数据。然后分别提取红、绿、蓝三个通道的值，使用rgb函数将提取的颜色值组合成一个颜色字符串，用于后续的填充操作。

   ```ts
   // 触摸事件
   .onTouch((event) => {
     const x = event.touches[0].x, y = event.touches[0].y;
     switch (event.type) {
       case TouchType.Down:
         const path = new DrawingPath();
         path.points.push({ x: x, y: y });
         this.paths.push(path);
         break;
       case TouchType.Move:
         this.paths[this.paths.length-1].points.push({ x: x, y: y });
         this.draw(x, y);
         break;
     }
   })
   ```
4. 利用数组记录绘制路径，撤销时移除最上层路径然后重新绘制即可实现“撤销”操作。

   ```ts
   Button('撤销').onClick(() => {
     if (this.paths.length >= 1) {
       this.paths.pop()!!;
     }
     console.debug(`----------撤销---`);
     if (this.maskUri) {
       console.debug(`----------撤销   ${this.paths.length}---`);
       this.clearAndDraw();
       this.paths.forEach((path) => {
         for (let i = 0; i < path.points.length; i++) {
           this.draw(path.points[i].x, path.points[i].y);
         }
       });
     }
   });
   ```

完整示例参考如下：

```ts
import { photoAccessHelper } from '@kit.MediaLibraryKit';
import { display, window } from '@kit.ArkUI';
import image from '@ohos.multimedia.image';
import { fileIo } from '@kit.CoreFileKit';
import { BusinessError } from '@kit.BasicServicesKit';

interface Point {
  x: number;
  y: number;
}

export class DrawingPath {
  points: Point[] = [];
}

@Entry
@Component
struct ImageAddMaskCase {
  @State @Watch('clearAndDraw')
  maskUri: string = '';
  // 画布尺寸
  @State private canvasWidth: number = 0;
  @State private canvasHeight: number = 0;
  // 展示区域的尺寸
  private screenWidth: number = 0;
  private screenHeight: number = 0;
  // 缩放比例
  @State private scaleFactor: number = 1;
  // 马赛克像素大小
  private maskRadius: number = 30;
  private paths: DrawingPath[] = [];
  private myPen: CanvasRenderingContext2D = new CanvasRenderingContext2D(new RenderingContextSettings(true));

  // 选择图片
  private async selectImage() {
    // picker拉起图库，选择图片
    const picker = new photoAccessHelper.PhotoViewPicker();
    const result = await picker.select({
      maxSelectNumber: 1,
      MIMEType: photoAccessHelper.PhotoViewMIMETypes.IMAGE_TYPE
    });
    if (!result.photoUris.length) {
      return;
    }
    this.processImage(result.photoUris[0]);
  }

  // 图片处理
  private async processImage(uri: string) {
    try {
      const file = fileIo.openSync(uri, fileIo.OpenMode.READ_ONLY);
      const imageSource = image.createImageSource(file.fd);
      const decodingOptions: image.DecodingOptions = {
        editable: true,
        desiredPixelFormat: 3,
      };
      imageSource.createPixelMap(decodingOptions, (err: BusinessError, pixelMap: image.PixelMap) => {
        if (err) {
          console.error(`Failed to create pixelMap. Code: ${err.code}, Message: ${err.message}`);
          return;
        }
        pixelMap.getImageInfo().then(info => {
          // 更新画布尺寸
          this.updateCanvasSize(info.size);
          this.maskUri = uri;
          // 计算缩放比例
          this.calculateScaleFactor();
        });
      });
    } catch (error) {
      console.error('Error processing image:', error);
    }
  }

  private updateCanvasSize(size: image.Size) {
    this.canvasWidth = this.getUIContext().px2vp(size.width);
    this.canvasHeight = this.getUIContext().px2vp(size.height);
  }

  // 根据图片的宽度、高度以及屏幕的宽度、高度计算缩放比例
  private calculateScaleFactor() {
    const widthRatio = this.screenWidth / this.canvasWidth;
    const heightRatio = this.screenHeight / this.canvasHeight;
    this.scaleFactor = Math.min(widthRatio, heightRatio);
    if (this.scaleFactor > 1) {
      this.scaleFactor = 1;
    }
  }

  // 绘制图片
  private clearAndDraw() {
    this.myPen.clearRect(0, 0, this.canvasWidth, this.canvasHeight);
    if (this.maskUri) {
      this.myPen.drawImage(new ImageBitmap(this.maskUri), 0, 0, this.canvasWidth, this.canvasHeight);
    }
  }

  // 计算可展示区域的屏幕宽度和高度
  private getScreenDimensions() {
    window.getLastWindow(this.getUIContext().getHostContext()).then(win => {
      const topSafeHeight =
        this.getUIContext().px2vp(win.getWindowAvoidArea(window.AvoidAreaType.TYPE_SYSTEM).topRect.height);
      const bottomSafeHeight = this.getUIContext()
        .px2vp(win.getWindowAvoidArea(window.AvoidAreaType.TYPE_NAVIGATION_INDICATOR).bottomRect.height);
      const displayInfo = display.getDefaultDisplaySync();
      this.screenWidth = this.getUIContext().px2vp(displayInfo.width);
      this.screenHeight = this.getUIContext().px2vp(displayInfo.height) - topSafeHeight - bottomSafeHeight - 50;
    });
  }

  // 获取
  aboutToAppear() {
    this.getScreenDimensions();
  }

  build() {
    Column() {
      Row({ space: 20 }) {
        // 加载图片
        Button('选择图片').onClick(() => this.selectImage());
        Button('撤销').onClick(() => {
          if (this.paths.length >= 1) {
            this.paths.pop()!!;
          }
          console.debug(`----------撤销---`);
          if (this.maskUri) {
            console.debug(`----------撤销   ${this.paths.length}---`);
            this.clearAndDraw();
            this.paths.forEach((path) => {
              for (let i = 0; i < path.points.length; i++) {
                this.draw(path.points[i].x, path.points[i].y);
              }
            });
          }
        });
        Button('清空').onClick(() => {
          if (this.maskUri) {
            this.clearAndDraw();
          }
        });
      }
      .width('100%')
      .height(50)
      .justifyContent(FlexAlign.Center);

      Canvas(this.myPen)
        .onReady(() => this.clearAndDraw())
        .width(this.canvasWidth)
        .height(this.canvasHeight)
        .scale({
          x: this.scaleFactor,
          y: this.scaleFactor,
          centerX: 0,
          centerY: 0
        })
        // 触摸事件
        .onTouch((event) => {
          const x = event.touches[0].x, y = event.touches[0].y;
          switch (event.type) {
            case TouchType.Down:
              const path = new DrawingPath();
              path.points.push({ x: x, y: y });
              this.paths.push(path);
              break;
            case TouchType.Move:
              this.paths[this.paths.length-1].points.push({ x: x, y: y });
              this.draw(x, y);
              break;
          }
        })
        .backgroundColor(Color.Pink);
    }
    .height('100%')
    .width('100%')
    .justifyContent(FlexAlign.Start)
    .alignItems(HorizontalAlign.Start);
  }

  private draw(x: number, y: number) {
    const data = this.myPen.getImageData(x, y, 1, 1).data;
    const color = `rgb(${data[0]}, ${data[1]}, ${data[2]})`;
    this.myPen.fillStyle = color;
    // 矩阵填充
    this.myPen.fillRect(x, y, this.maskRadius, this.maskRadius);
  }
}
```
