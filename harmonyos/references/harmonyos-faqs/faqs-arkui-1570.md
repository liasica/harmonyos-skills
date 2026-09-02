---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1570
title: 如何实现饼状进度条展示效果
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何实现饼状进度条展示效果
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:11+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:fb2ba089c7b9158996bfab407e1be2435457e06f0ff7739e85098e3db319b4c8
---

## 问题现象

通过Canvas画布组件如何实现一个以饼图形式展示进度的效果？该饼图从零开始逐步展示进度的变化过程。

## 背景知识

* [Canvas](../harmonyos-references/ts-components-canvas-canvas.md)：提供画布组件，用于自定义绘制图形。
* [CanvasRenderingContext2D](../harmonyos-references/ts-canvasrenderingcontext2d.md)：使用CanvasRenderingContext2D在Canvas画布组件上进行绘制，绘制对象可以是图形、文本、线段、图片等。

## 解决方案

1. 使用Canvas绘制饼状图，该饼状图由两条直线和一条弧线构成。当两条直线完全重合时，若弧线覆盖整个圆周，则饼状图呈现为一个完整的圆形；若弧线长度为零，则饼状图不包含任何区域，呈现为空状态。
2. 将起始角度angle的初始值设置为-90度，在Canvas的onReady方法中，将最大角度参数设置为270度。

```ts
@Entry
@Component
struct CircleProgressDemo {
  @State radius: number = 0;
  @State centerX: number = 0;
  @State centerY: number = 0;
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  @State angle: number = -90;
  private timer: number | null = null;

  // this.radius为圆的半径
  start() {
    this.context.clearRect(-this.radius, -this.radius, this.context.width, this.context.height);
    this.context.fillStyle = '#0A59f7';
    this.context.beginPath();
    //  设置圆心的位置坐标轴为x=0,y=0(也可以把其他点设置为x=0,y=0，但是把这里设置为圆心是最方便计算的)
    this.context.moveTo(0, 0);
    // 画一条直线，从圆心连到直线终点1
    this.context.lineTo(0, -this.radius);
    // 画完圆弧的第一条边，开始准备画圆弧，这里需要准备的是圆弧的起始位置和终止位置
    // 起始位置为固定值，如上图所示，当前Y=0的位置在中心，所以起始的弧度，沿着圆心向右的那条线，往上走四分之一个圆的弧度即-π/2
    let startAngle = -Math.PI / 2;
    // 终止位置要根据当前的角度，动态算出即π/180*当前的角度angle
    let endAngle = Math.PI / 180 * this.angle;
    // 算出角度后，圆心(x=0,y=0)，半径(this.radius),起始弧度(startAngle),终止弧度(endAngle),画出圆弧
    this.context.arc(0, 0, this.radius, startAngle, endAngle);
    // 画出第二条直线，这里上面介绍的三角函数知识可以算出直线终点2的位置对应的x,y轴坐标
    let x = this.centerX * Math.cos(Math.PI / 180 * this.angle);
    let y = this.centerY * Math.sin(Math.PI / 180 * this.angle);
    // 画第二条直线，从圆心，到上面算出来的点
    this.context.lineTo(x, y);
    // 填充已经画好的饼状图
    this.context.fill();
  };

  aboutToDisappear(): void {
    if (this.timer !== null) {
      clearInterval(this.timer); // 清理定时器
      this.timer = null;
    }
  };

  build() {
    Column() {
      Canvas(this.context).width(250).height(250).backgroundColor(Color.White)
        .onReady(() => {
          // 根据画布的宽和高来计算圆形的位置，以及半径
          this.centerX = this.context.width / 2;
          this.centerY = this.context.height / 2;
          this.radius = this.context.width / 2;
          this.context.translate(this.centerX, this.centerY);
          this.timer = setInterval(() => {
            // 未跑完一圈，angle随着时间匀速递增
            if (this.angle <= 270) {
              this.angle++;
            } else {
              // 已跑完一圈，归零重新开始
              this.angle = -90;
            }
            this.start();
          }, 10);
        });
    }.justifyContent(FlexAlign.Center)
    .height('100%')
    .width('100%');
  }
}
```
