---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1153
title: Canvas绘制蒙层在横屏的时候如何才能撑满屏幕
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > Canvas绘制蒙层在横屏的时候如何才能撑满屏幕
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:06+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:9053d106e337b4ce43487f1988e85b84f5a3560b1ec6670ea11b626feb81a4a6
---

## 问题现象

OCR识别卡证场景，通常需要在相机预览页面通过绘制Canvas蒙层，蒙层中切割出卡证识别区。横屏情况下出现蒙层未撑满屏幕的情况，要如何解决？

## 背景知识

Canvas：使用[CanvasRenderingContext2D](../harmonyos-references/ts-canvasrenderingcontext2d.md)实现矩形蒙层绘制，并剪切出卡证识别区域。

相机服务：相机拍照可参考[拍照实践](../harmonyos-guides/camera-shooting-case.md)。

## 问题定位

问题代码：

```ts
@Builder
  canvasVerticalView() {
    Stack({alignContent:Alignment.Top}){
      Stack() {
        XComponent({
          type: XComponentType.SURFACE,
          controller: this.mXComponentController,
          imageAIOptions: this.options
        })
          .onLoad(async () => {
            this.mXComponentController.setXComponentSurfaceRect({
              surfaceWidth: display.getDefaultDisplaySync().width,
              surfaceHeight: display.getDefaultDisplaySync().height - 150
            });
            surfaceId = this.mXComponentController.getXComponentSurfaceId();
            setTimeout(async () => {
              CameraIdManager.cameraShooting(0, surfaceId, context)
            }, 500);
          })
          .layoutWeight(1)
          .width('100%')
          .rotate({ angle: -90})
        Canvas(this.context)
          .width('100%')
          .layoutWeight(1)
          .onReady(() => {
            this.context.globalCompositeOperation = 'xor'
            // 计算画布尺寸
            const canvasWidth = this.getUIContext().px2vp(display.getDefaultDisplaySync().width);
            const canvasHeight = this.getUIContext().px2vp(display.getDefaultDisplaySync().height-150);
            // 计算图片绘制的位置，使其居中显示
            const imgWidth = 360;
            const imgHeight = 230;
            const x = (canvasWidth - imgWidth) / 2;
            const y = (canvasHeight - imgHeight) / 2;

            // 绘制背景矩形（半透明蒙层）
            this.context.beginPath();
            this.context.rect(0, 0, canvasWidth, canvasHeight);
            this.context.closePath();
            this.context.fillStyle = 'rgba(0, 0, 0, 0.5)';
            this.context.fill();
            CameraIdManager.cropRect = {
              x:this.getUIContext().vp2px(x),
              y:this.getUIContext().vp2px(y),
              size: {
                width: 960,
                height: 540
              }
            }
            // 保存当前画布状态
            this.context.save();
            // 图片内部区域
            // 圆角半径
            const radius = 18;
            this.context.beginPath();
            this.context.moveTo(x + radius, y);
            this.context.lineTo(x + imgWidth - radius, y);
            this.context.arc(x + imgWidth - radius, y + radius, radius, 1.5 * Math.PI, 2 * Math.PI);
            this.context.lineTo(x + imgWidth, y + imgHeight - radius);
            this.context.arc(x + imgWidth - radius, y + imgHeight - radius, radius, 0, 0.5 * Math.PI);
            this.context.lineTo(x + radius, y + imgHeight);
            this.context.arc(x + radius, y + imgHeight - radius, radius, 0.5 * Math.PI, Math.PI);
            this.context.lineTo(x, y + radius);
            this.context.arc(x + radius, y + radius, radius, Math.PI, 1.5 * Math.PI);
            this.context.closePath();
            // 将图片内部区域设置为裁剪区域
            this.context.clip();
            // 在裁剪区域内清除蒙层
            this.context.clearRect(x, y, imgWidth, imgHeight);
            // 恢复默认的裁剪区域
            this.context.restore();
            // 将ImageBitmap绘制到主画布上，指定图片的宽度和高度
            this.context.drawImage(this.img, x, y, imgWidth, imgHeight);
            // 使画布重绘
            this.context.canvas.invalidate();
          })
      }
      .width('100%')
      .layoutWeight(1)
    }
    .width('100%')
    .layoutWeight(1)
    .rotate({
      x: 0,
      y: 0,
      z: 1,
      centerX: '50%',
      centerY: '50%',
      angle: 90
    })
  }
```

当前实现横屏蒙层效果方案如下：

1. 使用Stack容器包裹Canvas。
2. Canvas中按竖屏绘制蒙版、裁剪卡证识别区，并使用drawImage()绘制卡证相框。
3. 使用rotate()将Stack容器旋转90度，得到横屏效果。

## 分析结论

分析问题代码实现逻辑，发现Canvas画布宽高是基于手机屏幕宽高进行设置，但横屏旋转时操作对象为Canvas的父容器Stack，导致Canvas宽度（屏幕宽度）变为高度导致无法占满屏幕。

## 修改建议

调整实现方案，不再旋转父容器Stack，而是在使用clip()裁剪卡证识别区和使用drawImage()绘制卡证相框时旋转Canvas。将坐标系原点移动至屏幕中央，并顺时针旋转90度。调整后的完整代码示例如下：

```ts
import display from '@ohos.display';
import { image } from '@kit.ImageKit';

@Entry
@Component
struct Index {
  mXComponentController: XComponentController = new XComponentController;
  screenWidthPx: number = 0;
  screenHeightPx: number = 0;
  cameraCropRect: image.Region = {
    size: { width: 0, height: 0 },
    x: 0,
    y: 0
  };
  private aiController: ImageAnalyzerController = new ImageAnalyzerController();
  private options: ImageAIOptions = {
    types: [ImageAnalyzerType.SUBJECT, ImageAnalyzerType.TEXT],
    aiController: this.aiController
  };
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  private cardFrontPhoto: ImageBitmap =
    new ImageBitmap('/common/images/id_card_bg.png'); // id_card_bg.png仅供参考使用，开发者可替换为实际使用图片

  aboutToAppear() {
    let displayDefaultInfo = display.getDefaultDisplaySync();
    this.screenWidthPx = displayDefaultInfo.width;
    this.screenHeightPx = displayDefaultInfo.height;
  }

  @Builder
  canvasVerticalView() {
    Stack({ alignContent: Alignment.Top }) {
      Stack() {
        XComponent({
          type: XComponentType.SURFACE,
          controller: this.mXComponentController,
          imageAIOptions: this.options
        })
          .onLoad(async () => {
            this.mXComponentController.setXComponentSurfaceRect({
              surfaceWidth: display.getDefaultDisplaySync().width,
              surfaceHeight: display.getDefaultDisplaySync().height - 150
            });

            setTimeout(async () => {
              // 启动相机
            }, 500);

          })
          .layoutWeight(1)
          .width('100%')
          .backgroundColor('#aac4b7b7')
        Canvas(this.context)
          .width('100%')
          .layoutWeight(1)
          .onReady(() => {
            this.context.globalCompositeOperation = 'xor';
            // 计算画布尺寸
            const canvasWidth = this.getUIContext().px2vp(display.getDefaultDisplaySync().width);
            const canvasHeight = this.getUIContext().px2vp(display.getDefaultDisplaySync().height);
            // 计算图片绘制的位置，使其居中显示
            const imgWidth = 360;
            const imgHeight = 230;
            const x = (canvasWidth - imgWidth) / 2;
            const y = (canvasHeight - imgHeight) / 2;
            // 绘制背景矩形（半透明蒙层）
            this.context.beginPath();
            this.context.rect(0, 0, canvasWidth, canvasHeight);
            this.context.closePath();
            this.context.fillStyle = 'rgba(0, 0, 0, 0.5)';
            this.context.fill();
            this.cameraCropRect = {
              x: this.getUIContext().vp2px(x),
              y: this.getUIContext().vp2px(y),
              size: {
                width: 960,
                height: 540
              }
            };
            // 保存当前画布状态
            this.context.save();
            // 将坐标系平移至画布中心
            this.context.translate(canvasWidth / 2, canvasHeight / 2); // 假设画布宽高均为300，中心点(150,150)
            // 旋转90度（顺时针，Math.PI/2弧度）
            this.context.rotate(Math.PI / 2);
            // 绘制背景矩形（半透明蒙层）
            const radius = 18;
            this.context.beginPath();
            this.context.moveTo(-imgWidth / 2 + radius, -imgHeight / 2);
            this.context.lineTo(-imgWidth / 2 + imgWidth - radius, -imgHeight / 2);
            this.context.arc(-imgWidth / 2 + imgWidth - radius, -imgHeight / 2 + radius, radius, 1.5 * Math.PI,
              2 * Math.PI);
            this.context.lineTo(-imgWidth / 2 + imgWidth, -imgHeight / 2 + imgHeight - radius);
            this.context.arc(-imgWidth / 2 + imgWidth - radius, -imgHeight / 2 + imgHeight - radius, radius, 0,
              0.5 * Math.PI);
            this.context.lineTo(-imgWidth / 2 + radius, -imgHeight / 2 + imgHeight);
            this.context.arc(-imgWidth / 2 + radius, -imgHeight / 2 + imgHeight - radius, radius, 0.5 * Math.PI,
              Math.PI);
            this.context.lineTo(-imgWidth / 2, -imgHeight / 2 + radius);
            this.context.arc(-imgWidth / 2 + radius, -imgHeight / 2 + radius, radius, Math.PI, 1.5 * Math.PI);
            this.context.closePath();
            // 将图片内部区域设置为裁剪区域
            this.context.clip();
            // 在裁剪区域内清除蒙层
            this.context.clearRect(-imgWidth / 2,
              -imgHeight / 2, imgWidth, imgHeight);
            // 恢复默认的裁剪区域
            this.context.restore();
            // 保存当前画布状态
            this.context.save();
            // 将坐标系平移至画布中心
            this.context.translate(canvasWidth / 2, canvasHeight / 2); // 假设画布宽高均为300，中心点(150,150)
            // 旋转90度（顺时针，Math.PI/2弧度）
            this.context.rotate(Math.PI / 2);
            // 绘制图片（旋转后坐标已变化，需调整绘制位置）
            this.context.drawImage(
              this.cardFrontPhoto,
              -imgWidth / 2,
              -imgHeight / 2, // x坐标：旋转后原高度变为宽度，取负半值居中
              // y坐标：同理
              imgWidth, // 绘制宽度（旋转后原高度作为新宽度）
              imgHeight
            );
            this.context.restore(); // 恢复之前保存的绘图状态
            // 使画布重绘
            this.context.canvas.invalidate();
          })
      }
      .width('100%')
      .layoutWeight(1)

      Text('请将人像放在框内,确保边角完整、文字清晰')
        .fontSize(15)
        .fontColor(Color.White)
        .width('100%')
        .textAlign(TextAlign.Center)
    }
    .width('100%')
    .layoutWeight(1)
  }

  build() {
    Column() {
      this.canvasVerticalView();
      Row() {
        Button('变焦')
        Button('拍照')
      }
      .width('100%')
      .height(78)
      .justifyContent(FlexAlign.SpaceAround)
    }
    .height('100%')
    .backgroundColor(Color.Transparent)
  }
}
```
