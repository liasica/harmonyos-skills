---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkgraphics-2d-21
title: DrawingRenderingContext绘制图像图形如何填充
breadcrumb: FAQ > 图形开发 > 2D图形（ArkGraphics 2D） > DrawingRenderingContext绘制图像图形如何填充
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:46+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:25d03b15754e55c32254de2829d500e2d6e12cf38f6b2efe556ccc39078e8e11
---

## 问题现象

使用DrawingRenderingContext绘制图像时，图像默认为实心黑色，如何改变绘制图像的填充颜色或边框颜色。

## 背景知识

使用[DrawingRenderingContext](../harmonyos-references/ts-drawingrenderingcontext.md)实现在[Canvas](../harmonyos-references/ts-components-canvas-canvas.md)组件上进行图案图形绘制。

大部分的几何形状与文本均可以选择使用画笔或者使用画刷来实现绘制。使用画笔可以绘制图形框，使用画刷可以绘制实心图形，也可以结合两者绘制带描边的实心图形。

## 解决方案

如果想要使用DrawingRenderingContext绘制非默认的实心图案，并实现自己想要的填充效果，可以通过设置Canvas的画笔（Pen）和画刷（Brush）进行图形绘制来实现填充效果。

* 绘制图形框：

  设置画笔样式，使用attachpen将画笔应用到画布绘制中，关键代码如下：

  ```ts
  const canvas = this.context.canvas;
  let pen = new drawing.Pen();
  pen.setColor(255, 0, 0, 0);
  pen.setStrokeWidth(4);
  canvas.attachPen(pen);
  const font = new drawing.Font();
  font.setSize(150);
  const textBlob =
    drawing.TextBlob.makeFromString('Hello World!', font, drawing.TextEncoding.TEXT_ENCODING_UTF8);
  canvas.drawTextBlob(textBlob, 200, 600);
  canvas.detachPen();
  this.context.invalidate();
  ```

  效果预览：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/7X3eHZR6SWmZkw_zZ9jz9w/zh-cn_image_0000002628553238.png "点击放大")
* 绘制实心图形：

  设置画刷样式，使用attachbrush将画刷应用到画布绘制中，关键代码如下：

  ```ts
  const canvas = this.context.canvas;
  let brush = new drawing.Brush();
  brush.setColor(255, 10, 89, 247);
  canvas.attachBrush(brush);
  canvas.drawCircle(600, 600, Math.min(400, 400) / 2);
  canvas.detachBrush();
  this.context.invalidate();
  ```

  效果预览：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/Rqf2oy3QSLanoPBVkj9a3Q/zh-cn_image_0000002658912553.png "点击放大")
* 绘制带描边的实心图形：

  绘制图案时若既要描边又要填充，可以将画笔和画刷样式都应用到画布绘制中，以绘制带描边的同心圆为示例，代码如下：

  ```ts
  const canvas = this.context.canvas;
  const pen = new drawing.Pen();
  pen.setColor(255, 0, 0, 0);
  pen.setStrokeWidth(4);
  canvas.attachPen(pen);
  let outBrush = new drawing.Brush();
  outBrush.setColor(255, 10, 89, 247);
  canvas.attachBrush(outBrush);
  canvas.drawCircle(600, 600, Math.max(400, 200) / 2);
  let innerBrush = new drawing.Brush();
  innerBrush.setColor(255, 241, 243, 245);
  canvas.attachBrush(innerBrush);
  canvas.drawCircle(600, 600, Math.min(400, 200) / 2);
  canvas.detachPen();
  canvas.detachBrush();
  this.context.invalidate();
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/4U5F9_C6RiqtwoVt_j1Zdg/zh-cn_image_0000002658792613.png "点击放大")

完整运行示例代码如下：

```ts
import { common2D, drawing } from '@kit.ArkGraphics2D';
import { LengthMetrics } from '@kit.ArkUI';

@Entry
@Component
struct Drawing {
  private context: DrawingRenderingContext = new DrawingRenderingContext();

  @Styles
  marginPx(){
    .width('100%')
    .height(40)
    .constraintSize({ maxWidth: '100%' })
    .margin({
      right: 16,
      left: 16
    });
  }

  build() {
    Flex({
      direction: FlexDirection.Column,
      alignItems: ItemAlign.Center,
      justifyContent: FlexAlign.Center,
      space: { main: LengthMetrics.px(16) }
    }) {
      Button('清除绘制')
        .onClick(() => {
          let color: common2D.Color = {
            alpha: 0,
            red: 0,
            green: 0,
            blue: 0
          };
          this.context.canvas.clear(color);
          this.context.invalidate();
        })
        .marginPx();
      Button('绘制图形框')
        .onClick(() => {
          const canvas = this.context.canvas;
          let pen = new drawing.Pen();
          pen.setColor(255, 0, 0, 0);
          pen.setStrokeWidth(4);
          canvas.attachPen(pen);
          const font = new drawing.Font();
          font.setSize(150);
          const textBlob =
            drawing.TextBlob.makeFromString('Hello World!', font, drawing.TextEncoding.TEXT_ENCODING_UTF8);
          canvas.drawTextBlob(textBlob, 200, 600);
          canvas.detachPen();
          this.context.invalidate();
        })
        .marginPx();
      Button('绘制实心图形')
        .onClick(() => {
          const canvas = this.context.canvas;
          let brush = new drawing.Brush();
          brush.setColor(255, 10, 89, 247);
          canvas.attachBrush(brush);
          canvas.drawCircle(600, 600, Math.min(400, 400) / 2);
          canvas.detachBrush();
          this.context.invalidate();
        })
        .marginPx();
      Button('绘制带描边的同心图形')
        .onClick(() => {
          const canvas = this.context.canvas;
          const pen = new drawing.Pen();
          pen.setColor(255, 0, 0, 0);
          pen.setStrokeWidth(4);
          canvas.attachPen(pen);
          let outBrush = new drawing.Brush();
          outBrush.setColor(255, 10, 89, 247);
          canvas.attachBrush(outBrush);
          canvas.drawCircle(600, 600, Math.max(400, 200) / 2);
          let innerBrush = new drawing.Brush();
          innerBrush.setColor(255, 241, 243, 245);
          canvas.attachBrush(innerBrush);
          canvas.drawCircle(600, 600, Math.min(400, 200) / 2);
          canvas.detachPen();
          canvas.detachBrush();
          this.context.invalidate();
        })
        .marginPx();

      Canvas(this.context)
        .width('100%')
        .height('100%');
    }
    .width('100%')
    .height('80%');
  }
}
```
