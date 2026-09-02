---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-914
title: 如何解决Canvas绘制文本进行缩放后，内容模糊问题
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何解决Canvas绘制文本进行缩放后，内容模糊问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:19+08:00
doc_updated_at: 2026-08-13
content_hash: sha256:115eabce47db083f8c6cb43bb47a636aced4a01b6b3361449cc709a6e1924b09
---

## 问题现象

当对组件添加scale以实现放大效果时，Text组件所渲染的文本仍能保持清晰可辨，而通过Canvas组件绘制的文本则会出现模糊现象。

```ts
@Entry
@Component
struct Index {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  @State textScale: number = 1

  build() {
    Column() {
      Button('点击').onClick(() => {
        this.textScale = 5
      })
      Text('hello')
        .scale({ x: this.textScale, y: this.textScale })
        .margin({top:50})
      Column() {
        Canvas(this.context)
          .width('100%')
          .height(400)
          .onReady(() => {
            this.context.font = '70px sans-serif';
            // 描边宽度
            this.context.lineWidth = 4;
            // 填充颜色
            this.context.fillStyle = 'black';
            // 填充文本
            this.context.fillText('hello', 180,200);
          })
      }
      .scale({ x: this.textScale, y: this.textScale })

    }
  }
}
```

问题效果预览：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/igFEZNJNQcWFS0_WkwjeAg/zh-cn_image_0000002628399762.png "点击放大")

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/SDTAuqj_TE25zjf64iwMUA/zh-cn_image_0000002658799031.png "点击放大")

## 背景知识

[Canvas](../harmonyos-references/ts-components-canvas-canvas.md)提供画布组件，用于自定义绘制图形，开发者使用[CanvasRenderingContext2D](../harmonyos-references/ts-canvasrenderingcontext2d.md)对象和[OffscreenCanvasRenderingContext2D](../harmonyos-references/ts-offscreencanvasrenderingcontext2d.md)对象在Canvas组件上进行绘制，绘制对象可以是基础形状、文本、图片等。

## 解决方案

上述现象的出现是由于对Canvas画布进行了整体缩放操作，导致文字显示模糊。为解决此问题，需先使用[clearRect](../harmonyos-references/ts-components-canvas-common-method.md#clearrect)方法清除当前画布内容，随后在放大比例下重新绘制文字内容，从而保证文字的清晰度。

```ts
@Entry
@Component
struct Solution {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  @State textScale: number = 1;

  onDrawText() {
    // 文本字体大小
    this.context.font = `${70 * this.textScale}px sans-serif`;
    // 填充颜色
    this.context.fillStyle = 'black';
    // 填充文本
    this.context.fillText('hello', 180, 200);
  }

  build() {
    Column() {
      Button('点击').onClick(() => {
        this.textScale = 4;
        // 清除画布
        this.context.clearRect(0, 0, 500, 200);
        this.onDrawText();
      })
      Text('hello')
        .scale({ x: this.textScale, y: this.textScale })
        .margin({ top: 50 })
      Column() {
        Canvas(this.context)
          .width(500)
          .height(200)
          .onReady(() => {
            this.onDrawText();
          })
      }
    }
  }
}
```
