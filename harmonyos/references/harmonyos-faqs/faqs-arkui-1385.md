---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1385
title: 如何实现环形仪表盘
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何实现环形仪表盘
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:27+08:00
doc_updated_at: 2026-08-13
content_hash: sha256:9ff11dcdd7a254abee09b80487522da1831c1979cf6af9c267f50026c4af426b
---

## 问题现象

如何实现环形仪表盘，并在圆盘周围添加动态漂浮的图片？

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/t9G6YTJFSZi5j6xaaTjusw/zh-cn_image_0000002628602664.png "点击放大")

## 背景知识

[Canvas](../harmonyos-guides/arkts-drawing-customization-on-canvas.md)提供画布组件，用于自定义绘制图形，开发者使用[CanvasRenderingContext2D](../harmonyos-references/ts-canvasrenderingcontext2d.md)对象和[OffscreenCanvasRenderingContext2D](../harmonyos-references/ts-offscreencanvasrenderingcontext2d.md)对象在Canvas组件上进行绘制，支持绘制形状、文本、图像及复杂动画。[CanvasRenderingContext2D.arc](../harmonyos-references/ts-components-canvas-common-method.md#arc)方法可以绘制弧线。

## 解决方案

使用Stack布局+Canvas画布组件，实现环形仪表盘，并让图片在周围浮动。下面是具体实现步骤：

1. 在编辑器终端导入三方库[@ohos/crypto-js](https://ohpm.openharmony.cn/#/cn/detail/@ohos%2Fcrypto-js)。
2. 绘制环形背景：使用arc方法绘制一个圆弧，中心在画布的中心，半径70，从-5π/4开始到π/4结束，形成一个环形背景。
3. 绘制分割线和数字：循环60次，每次计算角度theta，从-5π/4开始，每次增加π/40。每隔15个单位（i % 15 === 0）绘制一条长分割线，并在适当位置使用strokeText绘制数字。
4. 绘制动态进度条：使用setInterval更新进度。
5. 动态漂浮图片的实现：每个FloatImage组件通过angle和radius参数定位，围绕仪表盘周围均匀分布。angle控制旋转角度，radius控制距离中心的距离，形成漂浮效果。

```ts
import { MeasureOptions, MeasureUtils } from '@kit.ArkUI';
import CryptoJS from '@ohos/crypto-js';

@Entry
@Component
struct DialPage {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  private context1: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  private timer: number | null = null;
  @State steps: number = 323;
  @State uiContext: UIContext = this.getUIContext();
  @State uiContextMeasure: MeasureUtils = this.uiContext.getMeasureUtils();

  getX(style: MeasureOptions, r: number, lineWidth: number, index: number, theta: number) {
    let width = this.uiContext.px2vp(this.uiContextMeasure.measureText(style));
    let init = (this.context.width >> 1) + (r - (lineWidth >> 1)) * Math.cos(theta);
    if (index === 15 * 2) {
      init -= width >> 1;
    }
    if (index / 15 > 2) {
      init -= width + 1;
    }
    return init;
  }

  getY(r: number, lineWidth: number, index: number, theta: number) {
    let init = (this.context.height >> 1) + (r - (lineWidth >> 1)) * Math.sin(theta);
    if (index === 15 * 2) {
      init += 10;
    }
    return init;
  }

  resetStepProgress() {
    if (this.timer) {
      clearInterval(this.timer);
      this.timer = null;
    }
    this.steps = 0;
    this.context1.clearRect(0, 0, this.context1.width, this.context1.height);
    this.startStepTimer();
  }

  startStepTimer() {
    this.timer = setInterval(() => {
      if (this.steps < 6000) {
        this.steps += 1;
      } else {
        if (this.timer) {
          clearInterval(this.timer);
          this.timer = null;
        }
        return;
      }
      this.context1.clearRect(0, 0, this.context1.width, this.context1.height);
      this.context1.beginPath();
      let progress = Math.max(Math.min(this.steps / 6000, 1), 0);
      this.context1.arc(this.context1.width >> 1, this.context1.height >> 1, 70, -5 * 3.14 / 4,
        -5 * 3.14 / 4 + progress * 6 * 3.14 / 4);
      this.context1.strokeStyle = '#0A59F7';
      this.context1.stroke();
    }, 16);
  }

  build() {
    Stack() {
      Image('')
        .width('100%')
        .height('100%')
        .background('#F1F3F5');
      Canvas(this.context)
        .onReady(() => {
          this.context.lineWidth = 10;
          // 绘制表盘进度条背景
          this.context.lineCap = 'round';
          this.context.arc(this.context.width >> 1, this.context.height >> 1, 70, -5 * 3.14 / 4, 3.14 / 4);
          this.context.strokeStyle = '#fff';
          this.context.stroke();
          // 绘制分割线
          let lineLength: number = 8;
          this.context.lineWidth = 1;
          this.context.strokeStyle = '#00f';
          this.context.font = 'normal 100 10vp sans-serif';
          this.context.beginPath();
          let lineWidth = 15;
          for (let i = 0; i <= 60; i++) {
            let theta = -5 * 3.14 / 4 + 3.14 / 40 * i;
            this.context.moveTo((this.context.width >> 1) + (70 + (lineWidth >> 1)) * Math.cos(theta),
              (this.context.height >> 1) + (70 + (lineWidth >> 1)) * Math.sin(theta));
            if (i % 15 === 0) {
              this.context.lineTo((this.context.width >> 1) + (70 + lineLength + (lineWidth >> 1)) * Math.cos(theta),
                (this.context.height >> 1) + (70 + lineLength + (lineWidth >> 1)) * Math.sin(theta));
              // 绘制数字
              this.context.strokeText(`${i * 100}`,
                this.getX({ textContent: `${i * 100}`, fontSize: 10, fontWeight: 100 }, 70, lineWidth, i, theta),
                this.getY(70, lineWidth, i, theta));
            } else {
              this.context.lineTo((this.context.width >> 1) +
                (70 + (lineLength >> 1) + (lineWidth >> 1)) * Math.cos(theta),
                (this.context.height >> 1) + (70 + (lineLength >> 1) + (lineWidth >> 1)) * Math.sin(theta));
            }
          }
          this.context.stroke();
        });
      Canvas(this.context1)
        .onReady(() => {
          this.context1.lineWidth = 10;
          this.context1.lineCap = 'round';
          // 启用定时器
          this.startStepTimer();
        });
      Text('今日步数')
        .fontSize(11)
        .offset({ y: -27 });
      Text(`${this.steps}`)
        .fontSize(30)
        .fontWeight(700)
        .offset({ y: 5 });
      FloatImage({ angle: -4.5 * 3.14 / 4, radius: 130 });
      FloatImage({ angle: -3.9 * 3.14 / 4, radius: 130 });
      FloatImage({ angle: -3.3 * 3.14 / 4, radius: 130 });
      FloatImage({ angle: -0.7 * 3.14 / 4, radius: 130 });
      FloatImage({ angle: 0.5 * 3.14 / 4, radius: 130 });
      Column({ space: 16 }) {
        Button('步数兑换')
          .width(200)
          .fontColor('#fff')
          .fontWeight(400)
          .onClick(() => {
            this.resetStepProgress();
          });
        Text('点击即可刷新次数')
          .fontSize(12)
          .fontColor('#ccc');
      }
      .offset({ y: 130 });
    }
    .width('100%')
    .height('100%');
  }
}

@Component
struct FloatImage {
  @State offsetY: number = -5;
  @Require angle: number;
  @Require radius: number;

  build() {
    Row() {
      Image($r('app.media.startIcon'));
    }
    .width(50)
    .height(50)
    .padding(10)
    .offset({ x: this.radius * Math.cos(this.angle), y: this.radius * Math.sin(this.angle) + this.offsetY })
    .animation({
      duration: 1000,
      iterations: -1,
      playMode: PlayMode.Alternate,
      delay: Math.floor(CryptoJS.lib.WordArray.random(1).words[0] / 0x100000000 * 500)
    })
    .borderRadius(30)
    .radialGradient({ radius: 25, colors: [['#0000', 0.9], ['#fff', 0.9]], center: ['50%', '50%'] })
    .onAppear(() => {
      this.offsetY = 5;
    });
  }
}
```

## 总结

应用场景：将数据展示为环形图表，通常用于数据分析，将数据进行可视化处理；也可用于仪表盘等特殊场景。
