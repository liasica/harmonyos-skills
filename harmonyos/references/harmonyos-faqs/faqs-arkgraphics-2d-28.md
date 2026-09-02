---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkgraphics-2d-28
title: 如何实现绘制内容在指定区域透明化
breadcrumb: FAQ > 图形开发 > 2D图形（ArkGraphics 2D） > 如何实现绘制内容在指定区域透明化
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:46+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:0e4b96c7971549458d8ec80b8c1d2538475580319bea9471a21b954b85cc9f60
---

## 问题现象

视频弹幕场景下，弹幕会规避人物所在区域，防止遮挡人物。HarmonyOS如何实现绘制组件与指定透明区域相交部分也透明化？

## 背景知识

* [drawing](../harmonyos-references/js-apis-graphics-drawing.md)模块提供基本的绘制能力，如绘制矩形、圆形、点、直线、自定义Path和字体等。其中[Font](../harmonyos-references/arkts-apis-graphics-drawing-font.md)是描述字型绘制时所使用的属性，如大小、字体等，[Canvas](../harmonyos-references/arkts-apis-graphics-drawing-canvas.md)模块提供绘制承载绘制内容与绘制状态的载体，其中诸多接口可以实现多种图形绘制。
* [BlendMode](../harmonyos-references/arkts-apis-graphics-drawing-e.md#blendmode)是混合模式枚举，混合模式会将两种颜色（源色、目标色）以特定的方式混合生成一种新的颜色，通常用于叠加、滤镜和遮罩等图形操作场景。混合操作会分别作用于红、绿、蓝三个颜色通道，采用相同的混合逻辑，而透明度（Alpha通道）则根据各模式的定义另行处理。
* [saveLayer](../harmonyos-references/arkts-apis-graphics-drawing-canvas.md#savelayer12)保存当前画布的矩阵和裁剪区域，并为后续绘制分配位图。相当于将前面绘制保存在单独的图层，后续绘制不影响当前区域。调用恢复接口[restore](../harmonyos-references/arkts-apis-graphics-drawing-canvas.md#restore12)将会舍弃对矩阵和裁剪区域做的更改，并绘制位图。

## 解决方案

使用Canvas实现人脸区域绘制透明化可参考以下步骤：

1. 调用系统相册选取人像图片，获取图片的宽高数据。在完成背景图片加载时，获取屏幕宽高属性，并将Image组件与Canvas宽高设置为与图片大小比例相同。
2. 使用@Watch监听人脸检测的返回结果，并刷新Canvas上的遮盖区域绘制结果。
3. 绘制文字并根据人脸检测结果绘制矩形区域，每一次绘制前使用saveLayer保存底层透明图层，组件绘制后，可以通过BlendMode的DST\_OUT（保留目标像素中不与源重叠的部分）实现指定区域相交部分保持透明。

示例代码如下：

```ts
import { faceDetector } from '@kit.CoreVisionKit';
import { image } from '@kit.ImageKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo } from '@kit.CoreFileKit';
import { photoAccessHelper } from '@kit.MediaLibraryKit';
import { display } from '@kit.ArkUI';
import { drawing, common2D } from '@kit.ArkGraphics2D';

const TAG: string = '[FaceDetector Demo]';

// 从相册选择照片，框选人脸

@Entry
@Component
struct Index {
  @State chooseImage: PixelMap | undefined = undefined;
  @State dataValues: string = '';
  @State @Watch('onChange') faceLeft: number = 0;
  @State @Watch('onChange') faceTop: number = 0;
  @State @Watch('onChange') faceWidth: number = 0;
  @State @Watch('onChange') faceHeight: number = 0;
  @State imageWidth: number = 1;
  @State imageHeight: number = 1;
  private ratio: number = 0;
  private context: DrawingRenderingContext = new DrawingRenderingContext();
  uiContext: UIContext | null = null;

  aboutToAppear() {
    this.uiContext = this.getUIContext();
    if (!this.uiContext) {
      console.warn('no uiContext');
      return;
    }
  }

  onChange() {
    console.info(`num change to ${this.faceLeft} ${this.faceTop} ${this.faceWidth} ${this.faceHeight}`);
    let canvas: drawing.Canvas | null = null;
    canvas = this.context.canvas;
    let color: common2D.Color = {
      alpha: 0,
      red: 0,
      green: 0,
      blue: 0
    };
    this.context.canvas.clear(color);
    // 保存原有图形信息，在新图层上进行绘制(统一渲染机制下使用setBlendMode()接口需要save和restore流程）
    canvas.saveLayer();
    // 创建画刷
    let brush = new drawing.Brush();
    // 设置目标像素颜色，即矩形的颜色
    brush.setColor({
      alpha: 255,
      red: 255,
      green: 0,
      blue: 0
    });
    // 创建绘制字体
    const font = new drawing.Font();
    // 设置字体大小
    font.setSize(100);
    // 创建字体绘制区域
    const textBlob =
      drawing.TextBlob.makeFromString('Hello, drawingRenderingContext', font,
        drawing.TextEncoding.TEXT_ENCODING_UTF8);
    // 关联画刷
    canvas.attachBrush(brush);
    // 绘制字体
    canvas.drawTextBlob(textBlob, 30, 500);
    // 设置混合模式为叠加模式
    brush.setBlendMode(drawing.BlendMode.DST_OUT);
    // 将源像素的画刷效果设置到Canvas中
    canvas.attachBrush(brush);
    // 绘制遮盖区域（源像素）
    canvas.drawRect(this.faceLeft, this.faceTop, this.faceLeft + this.faceWidth, this.faceTop + this.faceHeight);
    // 去除填充效果
    canvas.detachBrush();
    // 恢复原图层信息
    canvas.restore();
    this.context.invalidate();
  }

  build() {
    RelativeContainer() {
      Column() {
        Stack() {
          Image(this.chooseImage)
            .width(this.imageWidth)
            .height(this.imageHeight)
            .backgroundColor(Color.Black)
            .alignRules({
              top: { anchor: '__container__', align: VerticalAlign.Top },
              middle: { anchor: '__container__', align: HorizontalAlign.Center },
            })
            .id('choose_image')
            .zIndex(0)
            // .blendMode(BlendMode.SRC_IN,BlendApplyType.OFFSCREEN)
            .onComplete((event) => {
              if (event) {
                // 监听加载图片完成后的回调，并获取图片宽高
                console.info('image width:', event?.width);
                console.info('image height:', event?.height);
                let iWidth = event.width;
                let iHeight = event.height;
                let radio = iWidth / iHeight;
                try {
                  // 获取设备屏幕宽高
                  let dWidth = display.getDefaultDisplaySync().width;
                  let dHeight = display.getDefaultDisplaySync().height;
                  // 设置Image组件宽高与图片宽高一致
                  this.imageHeight = this.getUIContext().px2vp(dHeight * 0.5);
                  this.imageWidth = this.imageHeight * radio;
                  console.info('display width:', dWidth);
                  console.info('display height:', dHeight);
                  this.ratio = (dHeight * 0.5) / iHeight;
                } catch (exception) {
                  hilog.error(0x0000, TAG,
                    `Failed to get default display. Code: ${exception.code}, message: ${exception.message}`);
                }
              }
            });
          Canvas(this.context)
            .width(this.imageWidth)
            .height(this.imageHeight)
            .alignRules({
              top: { anchor: 'choose_image', align: VerticalAlign.Top },
              left: { anchor: 'choose_image', align: HorizontalAlign.Start },
            })
            .zIndex(1);
        };

        Button('Select image')
          .onClick(() => {
            if (!canIUse('SystemCapability.Graphics.Drawing')) {
              console.error('Drawing is not supported by system');
              return;
            }
            // 从相册选择图片
            this.selectImage();
          })
          .width('100%')
          .height(50)
          .alignRules({
            top: { anchor: 'face_data', align: VerticalAlign.Bottom },
            middle: { anchor: '__container__', align: HorizontalAlign.Center },
          })
          .margin({
            top: 20
          })
          .id('start_choose');
        // 点击进行人脸检测，并绘制矩形边框
        Button('Start detection')
          .fontColor(Color.White)
          .alignSelf(ItemAlign.Center)
          .width('100%')
          .height(50)
          .alignRules({
            top: { anchor: 'start_choose', align: VerticalAlign.Bottom },
            middle: { anchor: '__container__', align: HorizontalAlign.Center },
          })
          .margin({
            top: 20
          })
          .id('start_detect')
          .onClick(() => {
            // 没有获取到图片
            if (!this.chooseImage) {
              hilog.error(0x0000, TAG, 'Failed to detect face.');
              return;
            }
            faceDetector.init();
            let visionInfo: faceDetector.VisionInfo = {
              pixelMap: this.chooseImage
            };
            // 利用faceDetector.detect检测人脸，并获取人脸区域矩形边框
            faceDetector.detect(visionInfo)
              .then((data: faceDetector.Face[]) => {
                // 照片中不包含人脸
                if (data.length === 0) {
                  this.dataValues = 'No face is detected in the image. Select an image that contains a face.';
                } else {
                  if (data.length > 0) {
                    let faceResult = data[0];
                    // 将返回的四个数据进行等比例缩放
                    this.faceLeft = faceResult.rect.left * this.ratio;
                    this.faceTop = faceResult.rect.top * this.ratio;
                    this.faceWidth = faceResult.rect.width * this.ratio;
                    this.faceHeight = faceResult.rect.height * this.ratio;
                  }
                  let faceString = JSON.stringify(data);
                  hilog.info(0x0000, TAG, `faceString data is: ${faceString}`);
                  this.dataValues = faceString;
                }
                faceDetector.release();
              })
              .catch((error: BusinessError) => {
                hilog.error(0x0000, TAG,
                  `Face detection failed. Code: ${error.code}, message: ${error.message}`);
                this.dataValues = `Error: ${error.message}`;
              });
          });
      };

    }
    .width('100%')
    .height('100%');
  }

  // 从相册选择图片
  private async selectImage() {
    let uri = await this.openPhoto();
    if (uri === undefined) {
      hilog.error(0x0000, TAG, 'Failed to get uri.');
    }
    this.loadImage(uri);
  }

  // 打开图片
  private openPhoto(): Promise<string> {
    return new Promise<string>((resolve) => {
      let photoPicker: photoAccessHelper.PhotoViewPicker = new photoAccessHelper.PhotoViewPicker();
      photoPicker.select({
        MIMEType: photoAccessHelper.PhotoViewMIMETypes.IMAGE_TYPE,
        maxSelectNumber: 1
      }).then(res => {
        resolve(res.photoUris[0]);
        let color: common2D.Color = {
          alpha: 0,
          red: 0,
          green: 0,
          blue: 0
        };
        // 使用RGBA(0, 0, 0, 0)填充画布
        this.context.canvas.clear(color);
        this.context.invalidate();
      }).catch((err: BusinessError) => {
        hilog.error(0x0000, TAG,
          `Failed to get photo image uri.code：${err.code}，message：${err.message}`);
        resolve('');
      });
    });
  }

  // 加载图片
  private loadImage(name: string) {
    setTimeout(async () => {
      try {
        let imageSource: image.ImageSource | undefined = undefined;
        let fileSource = await fileIo.open(name, fileIo.OpenMode.READ_ONLY);
        imageSource = image.createImageSource(fileSource.fd);
        if (imageSource === undefined) {
          console.error('loadImage:imageSource undefined');
          return;
        }
        this.chooseImage = await imageSource.createPixelMap();
        this.dataValues = '';
        hilog.info(0x0000, TAG, 'this.chooseImage:', this.chooseImage);
        fileIo.close(fileSource);
      } catch (exception) {
        hilog.error(0x0000, TAG,
          `Failed to operation fileIo. Code: ${exception.code}, message: ${exception.message}`);
      }
    }, 100
    );
  }
}
```

## 常见FAQ

Q：使用Canvas实现时为什么要使用saveLayer？

A：saveLayer保持当前图层的透明效果，防止混合模式导致颜色变为默认颜色——不透明黑色。

## 总结

通过混合模式BlendMode，将遮盖区域设置为BlendMode.DST\_OUT，将目标像素（文字绘制）与源像素（遮盖区域）重合区域透明化，实现部分区域遮盖的效果。若需实现人脸区域遮盖，需要通过[人脸检测](../harmonyos-guides/core-vision-face-detector.md)获取识别区域坐标，并依据上述方案将坐标值传入遮盖区域绘制相关代码中。
