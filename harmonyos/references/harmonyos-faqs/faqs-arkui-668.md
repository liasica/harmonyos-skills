---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-668
title: Canvas绘制圆弧失败
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > Canvas绘制圆弧失败
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:16+08:00
doc_updated_at: 2026-08-13
content_hash: sha256:d2d518bbe7cb1534478eff62bcc2d168c1bccbb1c14bc823901173fa0330ab50
---

## 问题现象

在以下使用CanvasRenderingContext2D的arc方法绘制圆弧的过程中，无论如何修改percent的值以改变弧线的终止弧度，运行代码后都会出现一个完整的圆弧。

问题示例如下：

```ts
const FULL_CIRCLE_RADIAN = Math.PI * 2
const CHECK_GREEN = '#00CC66'

@Component
@Entry
export struct ReceiptIcon {
  @State radiusPx: number = 0
  percent: number = 0
  @State private strokeWidth: number = 0
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

  build() {
    Canvas(this.context)
      .onSizeChange((oldValue: SizeOptions, newValue: SizeOptions) => {
        this.radiusPx = Math.min(Number(newValue.width ?? 0), Number(newValue.height ?? 0)) * 0.5
        this.strokeWidth = this.radiusPx * 0.125
      })
      .onReady(() => {
        this.context.beginPath()
        this.context.strokeStyle = CHECK_GREEN
        this.context.lineWidth = this.strokeWidth
        this.context.arc(
          this.context.width / 2,
          this.context.height / 2,
          (this.radiusPx - this.strokeWidth * 0.5),
          -90,
          this.percent * FULL_CIRCLE_RADIAN
        )
        this.context.stroke()
        this.context.beginPath()
        this.context.fillStyle = CHECK_GREEN
        this.context.fill()
      })
  }
}
```

## 背景知识

* [CanvasRenderingContext2D](../harmonyos-references/ts-canvasrenderingcontext2d.md)组件可在Canvas画布组件上进行绘制，绘制对象可以是图形、文本、线段、图片等，该组件的[arc](../harmonyos-references/ts-components-canvas-common-method.md#arc)方法用于绘制弧线路径。
* 弧度是角的度量单位。它是由国际单位制导出的单位，英文缩写为rad。其定义为：弧长等于圆半径的弧所对应的圆心角为1rad。一个完整的圆所对应的弧度是2π。

## 问题定位

注意到开发者在arc方法的第四个参数为-90，应该是将弧度误用成了角度。

## 分析结论

在HarmonyOS中，关于角度的使用都是使用弧度，而不是角度。弧度和角度的具体换算方法如下：

弧度转角度：1rad=(180/π)°，角度转弧度：1°=(π/180)rad。

## 修改建议

将第四个参数-90改成-(π/2)，对应到代码中即为-(FULL\_CIRCLE\_RADIAN / 4)，代码修改如下所示：

```ts
const FULL_CIRCLE_RADIAN = Math.PI * 2;
const CHECK_GREEN = '#00CC66';

@Entry
@Component
export struct ReceiptIcon {
  @State radiusPx: number = 0;
  percent: number = 0;
  @State private strokeWidth: number = 0;
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);

  build() {
    Canvas(this.context)
      .onSizeChange((oldValue: SizeOptions, newValue: SizeOptions) => {
        this.radiusPx = Math.min(Number(newValue.width ?? 0), Number(newValue.height ?? 0)) * 0.5;
        this.strokeWidth = this.radiusPx * 0.125;
      })
      .onReady(() => {
        this.context.beginPath();
        this.context.strokeStyle = CHECK_GREEN;
        this.context.lineWidth = this.strokeWidth;
        this.context.arc(
          this.context.width / 2,
          this.context.height / 2,
          (this.radiusPx - this.strokeWidth * 0.5),
          -(FULL_CIRCLE_RADIAN / 4),
          this.percent * FULL_CIRCLE_RADIAN
        );
        this.context.stroke();
        this.context.beginPath();
        this.context.fillStyle = CHECK_GREEN;
        this.context.fill();
      });
  }
}
```
