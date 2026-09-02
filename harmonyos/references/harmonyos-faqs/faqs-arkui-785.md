---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-785
title: 如何实现圆角矩形进度条
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何实现圆角矩形进度条
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:24+08:00
doc_updated_at: 2026-08-13
content_hash: sha256:1dbb406f21b8a593864a05ed116daeafdbde1c85c1f886f9f2422da7b1148526
---

## 问题现象

ArkTS中，如何使用Canvas实现圆角矩形边框的进度条效果？

## 背景知识

* [Canvas](../harmonyos-references/ts-components-canvas-canvas.md)：是一种画布组件，用于自定义绘制图形，绘制对象可以是基础形状、文本、图片等。
* [CanvasRenderingContext2D](../harmonyos-references/ts-canvasrenderingcontext2d.md)：是Canvas组件的参数，可使用它在Canvas画布上进行绘制，绘制对象可以是矩形、文本、图片等。
* [Stack](../harmonyos-references/ts-container-stack.md)：堆叠容器，子组件按照顺序依次入栈，后一个子组件覆盖前一个子组件。

## 解决方案

使用Canvas，根据进度绘制带有圆角的矩形。具体步骤如下：

1. 通过Canvas组件的大小，计算整个圆角矩形的周长。
2. 根据当前进度，计算出对应的当前进度条长度。
3. 使用[beginPath](../harmonyos-references/ts-components-canvas-common-method.md#beginpath)开始新路径，根据当前进度长度，按照顺时针从矩形右上角开始，依次绘制矩形的四条边，并在每个角落使用[arc](../harmonyos-references/ts-components-canvas-common-method.md#arc)方法绘制圆角，最后填充路径并关闭。

完整示例代码如下：

```ts
@Entry
@Component
struct RoundedRectProgress {
  @State @Watch('drawRoundedRectProgress') progressValue: number = 0; // 进度值(0-100)
  private intervalId: number = -1;
  private isStart: boolean = false;
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);

  // 绘制圆角矩形边框进度条
  drawRoundedRectProgress() {
    let ctx: CanvasRenderingContext2D = this.context;
    let progress: number = this.progressValue;
    let width: number = ctx.width;
    let height: number = ctx.height;
    const lineWidth = this.getUIContext().vp2px(2); // 进度条宽度
    const borderRadius = height / 2; // 圆角半径
    // 清除画布
    ctx.clearRect(0, 0, width, height);
    // 计算圆角矩形路径总长度
    const straightLength = (width - 2 * borderRadius) * 2 + (height - 2 * borderRadius) * 2;
    const cornerLength = 2 * Math.PI * borderRadius; // 四个角落的总弧长
    // 总路径长度
    const totalLength = straightLength + cornerLength;
    // 当前进度对应的路径长度
    const currentLength = (progress / 100) * totalLength;
    // 设置样式
    ctx.lineWidth = lineWidth;
    ctx.lineCap = 'round';
    ctx.strokeStyle = '#ff0a59F7';
    // 开始绘制路径
    ctx.beginPath();
    ctx.moveTo(width - borderRadius, lineWidth / 2);
    if (currentLength <= cornerLength / 4) { // 进度终点在右上角弧度
      const angle = (currentLength / (Math.PI * borderRadius / 2)) * (Math.PI / 2);
      ctx.arc(width - borderRadius, borderRadius, borderRadius - lineWidth / 2, -Math.PI / 2,
        -Math.PI / 2 + angle, false);
    } else if (currentLength <= (cornerLength / 4 + height - 2 * borderRadius)) { // 进度终点在右侧竖边
      ctx.arc(width - borderRadius, borderRadius, borderRadius - lineWidth / 2, -Math.PI / 2, 0, false);
      const remaining = currentLength - cornerLength / 4;
      ctx.moveTo(width - lineWidth / 2, borderRadius);
      ctx.lineTo(width - lineWidth / 2, borderRadius + remaining);
    } else if (currentLength <= (cornerLength / 2 + height - 2 * borderRadius)) { // 进度终点在右下角弧度
      ctx.arc(width - borderRadius, borderRadius, borderRadius - lineWidth / 2, -Math.PI / 2, 0, false);
      ctx.moveTo(width - lineWidth / 2, borderRadius);
      ctx.lineTo(width - lineWidth / 2, height - borderRadius);
      const remaining = currentLength - cornerLength / 4 - (height - 2 * borderRadius);
      const angle = (remaining / (Math.PI * borderRadius / 2)) * (Math.PI / 2);
      ctx.arc(width - borderRadius, height - borderRadius, borderRadius - lineWidth / 2, 0, angle, false);
    } else if (currentLength <= (cornerLength / 2 + height - 2 * borderRadius + width - 2 * borderRadius)) { // 进度终点在底边
      ctx.arc(width - borderRadius, borderRadius, borderRadius - lineWidth / 2, -Math.PI / 2, 0, false);
      ctx.moveTo(width - lineWidth / 2, borderRadius);
      ctx.lineTo(width - lineWidth / 2, height - borderRadius);
      ctx.arc(width - borderRadius, height - borderRadius, borderRadius - lineWidth / 2, 0, Math.PI / 2, false);
      const remaining = currentLength - (cornerLength / 2 + height - 2 * borderRadius);
      ctx.moveTo(width - borderRadius, height - lineWidth / 2);
      ctx.lineTo(width - borderRadius - remaining, height - lineWidth / 2);
    } else if (currentLength <=
      (cornerLength * 3 / 4 + height - 2 * borderRadius + width - 2 * borderRadius)) { // 进度终点在左下角弧度
      ctx.arc(width - borderRadius, borderRadius, borderRadius - lineWidth / 2, -Math.PI / 2, 0, false);
      ctx.moveTo(width - lineWidth / 2, borderRadius);
      ctx.lineTo(width - lineWidth / 2, height - borderRadius);
      ctx.arc(width - borderRadius, height - borderRadius, borderRadius - lineWidth / 2, 0, Math.PI / 2, false);
      ctx.moveTo(width - borderRadius, height - lineWidth / 2);
      ctx.lineTo(borderRadius, height - lineWidth / 2);
      const remaining = currentLength - (cornerLength / 2 + height - 2 * borderRadius + width - 2 * borderRadius);
      const angle = (remaining / (Math.PI * borderRadius / 2)) * (Math.PI / 2);
      ctx.arc(borderRadius, height - borderRadius, borderRadius - lineWidth / 2, Math.PI / 2, Math.PI / 2 + angle,
        false);
    } else if (currentLength <=
      (cornerLength * 3 / 4 + 2 * (height - 2 * borderRadius) + width - 2 * borderRadius)) { // 进度终点在左侧竖边
      ctx.arc(width - borderRadius, borderRadius, borderRadius - lineWidth / 2, -Math.PI / 2, 0, false);
      ctx.moveTo(width - lineWidth / 2, borderRadius);
      ctx.lineTo(width - lineWidth / 2, height - borderRadius);
      ctx.arc(width - borderRadius, height - borderRadius, borderRadius - lineWidth / 2, 0, Math.PI / 2, false);
      ctx.moveTo(width - borderRadius, height - lineWidth / 2);
      ctx.lineTo(borderRadius, height - lineWidth / 2);
      ctx.arc(borderRadius, height - borderRadius, borderRadius - lineWidth / 2, Math.PI / 2, Math.PI, false);
      const remaining = currentLength - (cornerLength * 3 / 4 + height - 2 * borderRadius + width - 2 * borderRadius);
      ctx.moveTo(lineWidth / 2, height - borderRadius);
      ctx.lineTo(lineWidth / 2, height - borderRadius - remaining);
    } else if (currentLength <=
      (cornerLength + 2 * (height - 2 * borderRadius) + width - 2 * borderRadius)) { // 进度终点在左上角弧度
      ctx.arc(width - borderRadius, borderRadius, borderRadius - lineWidth / 2, -Math.PI / 2, 0, false);
      ctx.moveTo(width - lineWidth / 2, borderRadius);
      ctx.lineTo(width - lineWidth / 2, height - borderRadius);
      ctx.arc(width - borderRadius, height - borderRadius, borderRadius - lineWidth / 2, 0, Math.PI / 2, false);
      ctx.moveTo(width - borderRadius, height - lineWidth / 2);
      ctx.lineTo(borderRadius, height - lineWidth / 2);
      ctx.arc(borderRadius, height - borderRadius, borderRadius - lineWidth / 2, Math.PI / 2, Math.PI, false);
      ctx.moveTo(lineWidth / 2, height - borderRadius);
      ctx.lineTo(lineWidth / 2, borderRadius);
      const remaining =
        currentLength - (cornerLength * 3 / 4 + 2 * (height - 2 * borderRadius) + width - 2 * borderRadius);
      const angle = (remaining / (Math.PI * borderRadius / 2)) * (Math.PI / 2);
      ctx.arc(borderRadius, borderRadius, borderRadius - lineWidth / 2, Math.PI, Math.PI + angle, false);
    } else if (currentLength <= totalLength) { // 进度终点在顶边
      ctx.arc(width - borderRadius, borderRadius, borderRadius - lineWidth / 2, -Math.PI / 2, 0, false);
      ctx.moveTo(width - lineWidth / 2, borderRadius);
      ctx.lineTo(width - lineWidth / 2, height - borderRadius);
      ctx.arc(width - borderRadius, height - borderRadius, borderRadius - lineWidth / 2, 0, Math.PI / 2, false);
      ctx.moveTo(width - borderRadius, height - lineWidth / 2);
      ctx.lineTo(borderRadius, height - lineWidth / 2);
      ctx.arc(borderRadius, height - borderRadius, borderRadius - lineWidth / 2, Math.PI / 2, Math.PI, false);
      ctx.moveTo(lineWidth / 2, height - borderRadius);
      ctx.lineTo(lineWidth / 2, borderRadius);
      ctx.arc(borderRadius, borderRadius, borderRadius - lineWidth / 2, Math.PI, Math.PI * 3 / 2, false);
      const remaining = currentLength - (totalLength - width + 2 * borderRadius);
      ctx.moveTo(borderRadius, lineWidth / 2);
      ctx.lineTo(borderRadius + remaining, lineWidth / 2);
    }
    // 绘制路径
    ctx.stroke();
    ctx.closePath();
  }

  // 动画控制，定时器模拟进度状态
  startAnimation() {
    this.intervalId = setInterval(() => {
      this.progressValue++;
      if (this.progressValue > 100) {
        this.progressValue = 0;
      }
    }, 100);
  }

  stopAnimation() {
    clearInterval(this.intervalId);
    this.intervalId = -1;
  }

  build() {
    Column({ space: 20 }) {
      // 进度条显示
      Stack() {
        Canvas(this.context)
          .width(200)
          .height(50)
          .backgroundColor('#001fb7bc')
          .onAreaChange(() => {
            this.drawRoundedRectProgress();
          })
          .borderRadius(25)
        Row() { // 用于显示内容信息
          Text(`${this.progressValue}` + '%')
            .fontColor('#e6000000')
            .fontSize(20)
        }
        .width(190)
        .height(40)
        .justifyContent(FlexAlign.Center)
        .backgroundColor('#F1F2F2')
        .borderRadius(20)
      }
      .alignContent(Alignment.Center)
      .width(200)
      .height(50)
      .backgroundColor('#001c1c1c')

      // 控制按钮
      Row({ space: 10 }) {
        Button('开始')
          .onClick(() => {
            if (this.isStart === false) {
              this.startAnimation();
              this.isStart = true;
            }
          })
        Button('暂停')
          .onClick(() => {
            if (this.isStart === true) {
              this.stopAnimation();
              this.isStart = false;
            }
          })
      }
      .width('100%')
      .justifyContent(FlexAlign.Center)
    }
    .width('100%')
    .height('100%')
    .padding(20)
    .justifyContent(FlexAlign.Center)
  }
}
```
