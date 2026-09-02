---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1005
title: 如何实现画布绘制的图案随手指移动
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何实现画布绘制的图案随手指移动
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:25+08:00
doc_updated_at: 2026-08-13
content_hash: sha256:b7aea366b45050bff9b5360e7600b14272ec63f4af34feea0a621816d08eac35
---

## 问题现象

画布中绘制一个图案，如何实现手指在画布中移动时，图案也会跟手指的移动方位一起移动？

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/G9QpGsMmSTK1qxgj4Ng35Q/zh-cn_image_0000002658923991.png "点击放大")

## 背景知识

* [Canvas](../harmonyos-references/ts-components-canvas-canvas.md)提供画布组件，用于自定义绘制图形，开发者使用[CanvasRenderingContext2D对象](../harmonyos-references/ts-canvasrenderingcontext2d.md)和[OffscreenCanvasRenderingContext2D对象](../harmonyos-references/ts-offscreencanvasrenderingcontext2d.md)在Canvas组件上进行绘制，绘制对象可以是基础形状、文本、图片等。
* [onTouch](../harmonyos-references/ts-universal-events-touch.md#ontouch)触摸事件回调，由手指在组件上按下、滑动或抬起时触发。

## 解决方案

想要做到图案的移动，可以利用画布中的[clearRect](../atomic-ascf/apis-canvas-rendering-context-2d.md#canvasrenderingcontext2dclearrect)方法。每当触发滑动事件时先获取画布中原来的图案，再通过clearRect方法清空当前的画布，将图案按照新的位置绘制。

1. 在画布中绘制图案。
2. 给画布添加触摸事件，手指按下时记录当前的坐标，滑动时清空画布并根据手指滑动的偏移量重新绘制图案。

```ts
@Entry
@Component
struct CanvasPage {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  @State cX: number = 100;
  @State cY: number = 100;
  @State startX: number = 0;
  @State startY: number = 0;

  upDate(x: number, y: number) {
    this.context.clearRect(0, 0, 400, 400);
    this.context.beginPath();
    this.context.arc(this.cX + x - this.startX, this.cY + y - this.startY, 50, 0, Math.PI * 2);
    this.context.lineWidth = 2;
    this.context.stroke();
  }

  build() {
    Column() {
      Canvas(this.context)
        .onReady(() => {
          this.context.beginPath();
          this.context.arc(this.cX, this.cY, 50, 0, Math.PI * 2);
          this.context.lineWidth = 2;
          this.context.stroke();
        })
        .onTouch((e) => {
          if (e.type === TouchType.Down) {
            this.startX = e.touches[0].x;
            this.startY = e.touches[0].y;
          }
          if (e.type === TouchType.Move) {
            this.upDate(e.touches[0].x, e.touches[0].y);
          }
          if (e.type === TouchType.Up) {
            this.cX = this.cX + e.touches[0].x - this.startX;
            this.cY = this.cY + e.touches[0].y - this.startY;
          }
        })
        .width(300)
        .height(300)
        .backgroundColor('#f1f3f5')
        .borderRadius(6);
    }
    .height('100%')
    .width('100%');
  }
}
```
