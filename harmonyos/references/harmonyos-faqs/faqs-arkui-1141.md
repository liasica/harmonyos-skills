---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1141
title: Canvas绘制矩形无法覆盖文字
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > Canvas绘制矩形无法覆盖文字
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:06+08:00
doc_updated_at: 2026-08-13
content_hash: sha256:fb1685c2131543ed4a90dc361571d5c9eb10b99f88f19a72eab1d95ab178e1ca
---

## 问题现象

利用Canvas绘制矩形和文字，矩形无法覆盖文字范围。

问题代码示例参考如下：

```ts
@Entry
@Component
struct CanvasTestPage {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)
  drawText: string = 'Harmony你好\n测试一下换行的测试一下换行\n测试制表\t哈哈'

  build() {
    Column() {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .onReady(() => {
          this.context.font = '18vp sans-serif'
          let text: TextMetrics = this.context.measureText(this.drawText)
          this.context.fillStyle = 'rgba(0,0,0,0.3)'
          this.context.fillRect(0, 100, text.width, text.height)

          this.context.fillStyle = 'rgb(0,0,255)'
          this.context.fillText(this.drawText, 0, 100 + text.height)
        })
    }.margin(10)
  }
}
```

问题效果预览：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/TAh1sALVQoym6QzcW6qrJw/zh-cn_image_0000002658808969.png "点击放大")

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/ktq9CvNARiSta-L1hcrFOw/zh-cn_image_0000002628569606.png "点击放大")

## 背景知识

* [fillRect](../atomic-ascf/apis-canvas-rendering-context-2d.md#canvasrenderingcontext2dfillrect)：填充一个矩形，四个必填参数依次为矩形左上角点的x坐标、矩形左上角点的y坐标、指定矩形的宽度、指定矩形的高度，根据四个参数即可完成一个矩形的绘制。
* [fillText](../atomic-ascf/apis-canvas-rendering-context-2d.md#canvasrenderingcontext2dfilltext)：填充文本，三个必填参数依次为文本内容、文本绘制起点的x轴坐标、文本绘制起点的y轴坐标，根据三个参数即可确定填充文本的坐标。

## 问题定位

根据问题代码运行效果可以看出：灰色矩形宽度和文本宽度一致，x轴起点保持一致，但是蓝色文字y轴起点和灰色矩形y轴起点不一致，可以发现问题出现在fillRect绘制的y轴起点上。

```ts
this.context.fillText(this.drawText, 0, 100 + text.height)
```

该错误代码设置文本的y轴起点为“100+文本高度”。

## 分析结论

根据fillRect和fillText参数可知，保持矩形左上角点的y坐标和文本绘制起点的y轴坐标一致，即可保持绘制时在同一个y轴起点。

## 修改建议

1. 修改fillText的文本起点y轴坐标。
2. [textBaseline](../harmonyos-references/ts-components-canvas-common-property.md#textbaseline)可以设置文本绘制中的水平对齐方式，将其设置成top对齐，实现文本基线在文本块的顶部。若不设置，则默认为alphabetic对齐（按字母对齐）。

```ts
@Entry
@Component
struct CanvasFillRectPage {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  drawText: string = 'Harmony你好\n测试一下换行的测试一下换行\n测试制表\t哈哈';

  build() {
    Column() {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .onReady(() => {
          this.context.font = '18vp sans-serif';
          this.context.textBaseline = 'top';
          let text: TextMetrics = this.context.measureText(this.drawText);
          this.context.fillStyle = 'rgba(0,0,0,0.3)';
          this.context.fillRect(0, 100, text.width, text.height);
          this.context.fillStyle = 'rgb(0,0,255)';
          this.context.fillText(this.drawText, 0, 100);
        });
    }.margin(10);
  }
}
```
