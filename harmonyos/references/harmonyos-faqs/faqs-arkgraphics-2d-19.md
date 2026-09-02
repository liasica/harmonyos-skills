---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkgraphics-2d-19
title: Canvas绘制翻角效果
breadcrumb: FAQ > 图形开发 > 2D图形（ArkGraphics 2D） > Canvas绘制翻角效果
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:46+08:00
doc_updated_at: 2026-08-13
content_hash: sha256:ec99e1ebf288462be065746fb23d579d04e58f83c3ece793659b5d5d03d042ef
---

## 问题现象

如何使用Canvas实现翻角效果，类似于书籍装帧的折角设计，使页面的翻角效果更加生动。

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/02/v3/A8Dtk8D2RF2Ok_Dn9o6ntw/zh-cn_image_0000002628393352.png "点击放大")

## 背景知识

* [Canvas](../harmonyos-references/ts-components-canvas-canvas.md)：提供画布组件，用于自定义绘制图形。
* [RenderingContextSettings](../harmonyos-references/ts-canvasrenderingcontext2d.md#renderingcontextsettings)：用来配置CanvasRenderingContext2D对象的参数，包括是否开启抗锯齿。
* [CanvasRenderingContext2D](../harmonyos-references/ts-canvasrenderingcontext2d.md#renderingcontextsettings)：使用RenderingContext在Canvas组件上进行绘制，绘制对象可以是矩形、文本、图片等。
* [quadraticCurveTo](../harmonyos-references/ts-components-canvas-common-method.md#quadraticcurveto)：创建二次贝赛尔曲线的路径。
* [arc](../harmonyos-references/ts-components-canvas-common-method.md#arc)：绘制弧线路径。

## 解决方案

使用CanvasRenderingContext2D中的moveTo，lineTo等函数绘制各个部分的线条，最后将线条连接回起点完成翻角效果。

完整示例参考如下：

```ts
@Entry
@Component
struct Clip {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);

  build() {
    Column() {
      Canvas(this.context)
        .height(200)
        .width('100%')
        .onReady(() => {
          this.context.moveTo(50, 0);
          this.context.quadraticCurveTo(55, 5, 55, 25); // 左上角向右下的弧线
          this.context.lineTo(55, 40); // 竖直向下的竖线
          this.context.arc(60, 40, 5, Math.PI, Math.PI / 2, true); // 左下角的半圆弧线
          this.context.lineTo(75, 45); // 绘制水平横线
          this.context.quadraticCurveTo(95, 45, 100, 50); // 右下角的弧线
          this.context.lineTo(50, 0);
          let gradient = this.context.createLinearGradient(50, 50, 75, 75);
          gradient.addColorStop(0, '#ccc');
          gradient.addColorStop(0.7, '#111');
          gradient.addColorStop(1, '#000');
          this.context.fillStyle = gradient;
          this.context.fill(); // 对封闭的路径进行填充
          this.context.beginPath(); // 新建路径
          this.context.moveTo(50, 0);
          this.context.lineTo(100, 50);
          this.context.lineTo(100, 0);
          this.context.lineTo(50, 0);
          this.context.closePath(); // 闭合路径
          this.context.fillStyle = '#ff6600';
          this.context.fill();
        });
    }
    .margin({ top: 200, left: 120 })
    .width('100%')
    .height('100%')
  }
}
```
