---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkgraphics-2d-43
title: 实现一个可拖动的环形进度条且头尾使用自定义图片
breadcrumb: FAQ > 图形开发 > 2D图形（ArkGraphics 2D） > 实现一个可拖动的环形进度条且头尾使用自定义图片
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:46+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:f3a116f901722f770d00c570ca6f74b34e52b04678c215e8404c049b97f7608f
---

## 问题现象

如何实现一个具有拖动功能的环形进度条，并支持在进度条起始和结束位置使用自定义背景图片？

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/jHLFV2LIT-CZG9Clj8Vb8w/zh-cn_image_0000002658912567.png "点击放大")

## 背景知识

* [Canvas](../harmonyos-references/ts-components-canvas-canvas.md)组件用于自定义绘制图形，[onReady](../harmonyos-references/ts-components-canvas-canvas.md#onready)事件之后可使用Canvas相关API进行绘制。
* [CanvasRenderingContext2D](../harmonyos-references/ts-canvasrenderingcontext2d.md)可在Canvas组件上进行绘制，绘制对象可以是矩形、文本、图片等。
* [滑动手势（PanGesture）](../harmonyos-guides/arkts-gesture-events-single-gesture.md#滑动手势pangesture)用于触发滑动手势事件，滑动达到最小滑动距离（默认值为5vp）时滑动手势识别成功。

## 解决方案

1. 当Canvas组件触发onReady事件后，使用CanvasRenderingContext2D的arc方法绘制环形路径，并通过moveTo和lineTo方法添加刻度线，最终通过stroke方法将图形绘制到画布上。

   ```ts
   paint(ctx: CanvasRenderingContext2D) {
     // 清除之前的绘制指令
     ctx.reset();
     // 绘制进度条背景
     ctx.lineCap = 'round';
     ctx.lineWidth = this.lineWidth;
     ctx.strokeStyle = '#ff999696';
     ctx.beginPath();
     ctx.arc(ctx.width / 2, ctx.height / 2, this.radius, this.startAngle, this.endAngle);
     ctx.stroke();
     // 绘制进度条刻度
     ctx.lineWidth = 2;
     ctx.strokeStyle = '#000';
     const startR = this.radius - 4;
     const endR = this.radius + 4;
     ctx.beginPath();
     const count = 50;
     const startAngle = this.startAngle + 2 / count * (this.endAngle - this.startAngle);
     const deltaAngle = (1 - 3 / count) * (this.endAngle - this.startAngle);
     for (let i = 0; i < count; i++) {
       ctx.moveTo(ctx.width / 2 + startR * Math.cos(startAngle + deltaAngle * i / count),
         ctx.height / 2 + startR * Math.sin(startAngle + deltaAngle * i / count));
       ctx.lineTo(ctx.width / 2 + endR * Math.cos(startAngle + deltaAngle * i / count),
         ctx.height / 2 + endR * Math.sin(startAngle + deltaAngle * i / count));
     }
     ctx.stroke();
     // 绘制进度条内容
     ctx.strokeStyle = '#ff0';
     ctx.beginPath();
     ctx.arc(ctx.width / 2, ctx.height / 2, this.radius, this.startAngle,
       this.startAngle + this.currentValue * (this.endAngle - this.startAngle));
     ctx.stroke();
   }
   ```
2. 为组件绑定滑动手势事件。当手势识别成功时，根据滑动的localX和localY坐标，并结合组件的宽度和高度，记录当前的移动位置信息。

   ```ts
   .onActionStart(event => {
     const x = event.fingerList[0].localX - this.ctx.width / 2;
     const y = event.fingerList[0].localY - this.ctx.height / 2;
     const r = Math.sqrt(x * x + y * y);
     const cos = x / r;
     const theta = Math.atan(y / x);
     this.isUpdate =
       r >= this.radius - this.lineWidth / 2 && r <= this.radius + this.lineWidth / 2 && cos >= 0 &&
         theta >= -Math.PI / 2 && theta <= Math.PI / 2;
   })
   ```
3. 在滑动手势更新过程中，根据水平（x轴）和垂直（y轴）方向的位移计算滑动角度。

   ```ts
   function getAngleFromCoordinate(x: number, y: number) {
     let angle = Math.atan(Math.abs(y) / Math.abs(x));
     if (x >= 0) {
       if (y < 0) {
         return -angle;
       } else {
         return angle;
       }
     } else {
       if (y >= 0) {
         return Math.PI - angle;
       } else {
         return angle + Math.PI;
       }
     }
   }
   ```
4. 根据滑动的角度和半径，计算自定义图片头部与尾部在translate变换中的移动距离，并确定其最终位置。

   ```ts
   Image($r('app.media.startIcon')) // 此处仅为示例，请开发者自行替换为可用图片。
     .width(10)
     .translate({ x: this.radius * Math.cos(this.startAngle), y: this.radius * Math.sin(this.startAngle) });
   Image($r('app.media.startIcon'))
     .width(10)
     .translate({ x: this.radius * Math.cos(this.endAngle), y: this.radius * Math.sin(this.endAngle) });
   ```

完整示例参考如下：

```ts
function getAngleFromCoordinate(x: number, y: number) {
  let angle = Math.atan(Math.abs(y) / Math.abs(x));
  if (x >= 0) {
    if (y < 0) {
      return -angle;
    } else {
      return angle;
    }
  } else {
    if (y >= 0) {
      return Math.PI - angle;
    } else {
      return angle + Math.PI;
    }
  }
}

@Entry
@Component
struct DraggableCircularProgress {
  startAngle: number = -Math.PI / 2;
  @State endAngle: number = Math.PI / 2;
  radius: number = 100;
  private ctx = new CanvasRenderingContext2D(new RenderingContextSettings(true));
  currentValue: number = 0;
  private isUpdate: boolean = false;
  private lineWidth: number = 20;
  paint(ctx: CanvasRenderingContext2D) {
    // 清除之前的绘制指令
    ctx.reset();
    // 绘制进度条背景
    ctx.lineCap = 'round';
    ctx.lineWidth = this.lineWidth;
    ctx.strokeStyle = '#ff999696';
    ctx.beginPath();
    ctx.arc(ctx.width / 2, ctx.height / 2, this.radius, this.startAngle, this.endAngle);
    ctx.stroke();
    // 绘制进度条刻度
    ctx.lineWidth = 2;
    ctx.strokeStyle = '#000';
    const startR = this.radius - 4;
    const endR = this.radius + 4;
    ctx.beginPath();
    const count = 50;
    const startAngle = this.startAngle + 2 / count * (this.endAngle - this.startAngle);
    const deltaAngle = (1 - 3 / count) * (this.endAngle - this.startAngle);
    for (let i = 0; i < count; i++) {
      ctx.moveTo(ctx.width / 2 + startR * Math.cos(startAngle + deltaAngle * i / count),
        ctx.height / 2 + startR * Math.sin(startAngle + deltaAngle * i / count));
      ctx.lineTo(ctx.width / 2 + endR * Math.cos(startAngle + deltaAngle * i / count),
        ctx.height / 2 + endR * Math.sin(startAngle + deltaAngle * i / count));
    }
    ctx.stroke();
    // 绘制进度条内容
    ctx.strokeStyle = '#ff0';
    ctx.beginPath();
    ctx.arc(ctx.width / 2, ctx.height / 2, this.radius, this.startAngle,
      this.startAngle + this.currentValue * (this.endAngle - this.startAngle));
    ctx.stroke();
  }
  build() {
    Stack() {
      Stack() {
        Canvas(this.ctx)
          .width('100%')
          .height('100%')
          .onReady(() => {
            this.paint(this.ctx);
          })
          .gesture(
            PanGesture({ fingers: 1 })
              .onActionStart(event => {
                const x = event.fingerList[0].localX - this.ctx.width / 2;
                const y = event.fingerList[0].localY - this.ctx.height / 2;
                const r = Math.sqrt(x * x + y * y);
                const cos = x / r;
                const theta = Math.atan(y / x);
                this.isUpdate =
                  r >= this.radius - this.lineWidth / 2 && r <= this.radius + this.lineWidth / 2 && cos >= 0 &&
                    theta >= -Math.PI / 2 && theta <= Math.PI / 2;
              })
              .onActionUpdate(event => {
                if (this.isUpdate) {
                  const x = event.fingerList[0].localX - this.ctx.width / 2;
                  const y = event.fingerList[0].localY - this.ctx.height / 2;
                  this.endAngle = getAngleFromCoordinate(x, y);
                  this.paint(this.ctx);
                }
              })
              .onActionEnd(() => {
                this.isUpdate = false;
              })
          );
        Image($r('app.media.startIcon')) // 此处仅为示例，请开发者自行替换为可用图片。
          .width(10)
          .translate({ x: this.radius * Math.cos(this.startAngle), y: this.radius * Math.sin(this.startAngle) });
        Image($r('app.media.startIcon'))
          .width(10)
          .translate({ x: this.radius * Math.cos(this.endAngle), y: this.radius * Math.sin(this.endAngle) });
        Text()
          .width(145)
          .aspectRatio(1)
          .backgroundColor('#ff999696')
          .borderRadius('50%');
      }
      .width(120 * 2)
      .aspectRatio(1)
      .backgroundColor('#000')
      .borderRadius('50%');
    }
    .height('100%')
    .width('100%');
  }
}
```
