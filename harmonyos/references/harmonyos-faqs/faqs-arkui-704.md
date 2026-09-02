---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-704
title: Canvas实现量角器功能
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > Canvas实现量角器功能
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:16+08:00
doc_updated_at: 2026-08-13
content_hash: sha256:b550b2c318901e3d40b74f843ba13a3e2f773a390d9a1fc474517886a2006a55
---

## 问题现象

如何使用Canvas组件实现量角器功能？

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/js0GTL3iQGWDLkcNLarSUQ/zh-cn_image_0000002628554890.gif "点击放大")

## 背景知识

* [Canvas](../harmonyos-guides/arkts-drawing-customization-on-canvas.md)提供画布组件，用于自定义绘制图形，开发者使用[CanvasRenderingContext2D](../harmonyos-references/ts-canvasrenderingcontext2d.md)对象和[OffscreenCanvasRenderingContext2D](../harmonyos-references/ts-offscreencanvasrenderingcontext2d.md)对象在Canvas组件上进行绘制，支持绘制形状、文本、图像及复杂动画。[CanvasRenderingContext2D.arc](../harmonyos-references/ts-components-canvas-common-method.md#arc)方法可以绘制弧线。
* [onTouch](../harmonyos-references/ts-universal-events-touch.md#ontouch)是一种触摸事件，手指触摸动作会触发该回调函数。

## 解决方案

使用Canvas画布组件，自定义绘制带有刻度的环形图表。具体实现步骤如下：

1. 绘制量角器面板：在draw()方法中，清除画布。使用arc()方法绘制一个半径为120的半圆，形成量角器的面板。
2. 绘制刻度线：循环从90度到270度，每次增加5度。使用moveTo()和lineTo()方法绘制每个刻度线，刻度线从半径120处向内缩进3个单位。
3. 绘制指针：使用arc()方法绘制一个扇形区域，从180度（正左方）开始，根据angle变量的值绘制到相应的角度。使用stroke()和fill()方法完成指针的绘制。
4. 处理触摸事件：在onTouch事件中，计算触摸点相对于中心点的坐标。使用Math.atan()计算角度，并根据需要调整角度范围到0到180度。更新angle变量并调用draw()方法重绘量角器，显示当前角度。
5. 显示当前角度：使用Text组件显示当前角度值，格式化为两位小数。

```ts
@Entry
@ComponentV2
struct GaugeScale {
  @Local angle: number = 0;
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  private radius: number = 120;
  private centerX: number = 0;
  private centerY: number = 0;

  draw() {
    this.context.clearRect(0, 0, this.context.width, this.context.height);
    // 绘制面板
    this.context.beginPath();
    this.context.arc(this.centerX, this.centerY, this.radius, Math.PI, Math.PI * 2);
    this.context.lineWidth = 1;
    this.context.strokeStyle = 'black';
    this.context.stroke(); // 绘制刻度
    for (let i = 90; i <= 270; i += 5) {
      this.context.beginPath();
      this.context.lineWidth = 1;
      this.context.strokeStyle = 'red';
      this.context.moveTo(this.centerX + this.radius * Math.sin(i / 180 * Math.PI),
        this.centerY + this.radius * Math.cos(i / 180 * Math.PI));
      this.context.lineTo(this.centerX + (this.radius - 3) * Math.sin(i / 180 * Math.PI),
        this.centerY + (this.radius - 3) * Math.cos(i / 180 * Math.PI));
      this.context.stroke();
    } // 绘制指针
    this.context.beginPath();
    this.context.strokeStyle = 'green';
    this.context.fillStyle = '#8000ff00';
    this.context.moveTo(this.centerX, this.centerY);
    this.context.lineTo(0, this.centerY);
    this.context.arc(this.centerX, this.centerY, this.radius, Math.PI, Math.PI * (1 + this.angle / 180));
    this.context.lineTo(this.centerX, this.centerY);
    this.context.stroke();
    this.context.fill();
  }

  build() {
    Column() {
      Canvas(this.context)
        .width(300)
        .height(150)
        .backgroundColor(Color.Pink)
        .onReady(() => {
          this.centerX = this.context.width / 2;
          this.centerY = this.context.height;
          this.draw();
        })
        .onTouch((event) => {
          let x = this.centerX - event.touches[0].x;
          let y = this.centerY - event.touches[0].y;
          if (y >= 0) {
            this.angle = Math.atan(y / x) * (180 / Math.PI);
            if (this.angle < 0) { // 表示钝角
              this.angle += 180;
            }
            this.draw();
          } else if (x < 0 && y < 0 && this.angle != 0) {
            this.angle = 180;
            this.draw();
          } else if (x > 0 && y < 0 && this.angle != 180) {
            this.angle = 0;
            this.draw();
          }
        });
      Text('当前角度：' + this.angle.toFixed(2));
    }.width('100%').height('100%').justifyContent(FlexAlign.Center).alignItems(HorizontalAlign.Center);
  }
}
```
