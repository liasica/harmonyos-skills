---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-989
title: Canvas如何实现惯性滑动
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > Canvas如何实现惯性滑动
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:05+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:149e1ba4a12e5827886648c5d2d48b54fdfd6cd28a25cffd01162c60cfaee2e2
---

## 问题现象

Canvas绘制一个数字列表，需要添加滑动手势才能实现滑动，但在手指松开之后，滑动就会停止，无法达到惯性滑动的效果，Canvas如何才能实现惯性滑动的效果？

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/k-vhNSplT8e6uRqWk3TSpA/zh-cn_image_0000002628401810.png "点击放大")

## 背景知识

[Canvas](../harmonyos-references/ts-components-canvas-canvas.md)可用于自定义绘制图形，如：形状、文本、图片等。创建Canvas组件时，最大面积不超过10000px\*10000px，超过最大面积则无法正常创建。

## 解决方案

整体思路如下：

1. 监听[滑动手势结束回调](../harmonyos-references/ts-basic-gestures-pangesture.md#onactionend)事件，触发执行惯性滚动的函数。

   ```screen
   .onActionEnd((event: GestureEvent) => {
     this.scrollFling(event.velocityX);
   })
   ```
2. 计算滑动速度和滑动距离，示例使用指数函数方式计算速度和距离，以达到先快后慢的效果。

   ```screen
   // 计算滑动速度和滑动距离，示例使用指数函数方式计算速度和距离，以达到先快后慢的效果
   const v = speed * Math.pow(Math.E, -frictionFactor * (speed - this.velocityX) / frameTime * (frameTime / 1000));
   const distance = v * (frameTime / 1000);
   this.offsetX += distance;
   ```
3. 启动一个定时器，每次达到定时时间，则根据上一步计算出的滑动距离，重新绘制画布。

   ```screen
   this.flingTimerId = setInterval(redrawCanvas, frameTime);
   ```
4. 在滑动时间不足或滑动距离超出范围时，则停止定时器。

   ```screen
   // 偏移量不在[-maxOffset, 0]区间时，需修正偏移量，并停止定时器
   if (this.offsetX > 0) {
     this.reset();
   }
   if (this.offsetX < -this.maxOffset) {
     this.reset();
   }
   ```

   ```screen
   if (this.flingTime < frameTime) { // 滑动时间不足时，停止定时器
     this.reset();
     return;
   }
   ```

完整示例参考如下：

```screen
const DRAW_SPACE: number = 8;
const CANVAS_HEIGHT: number = 200;

@Entry
@Component
struct CanvasFling {
  private listData: string[] = [];
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private canvas: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);

  private startX: number = 0;
  private offsetX: number = 0;
  private maxOffset: number = 0;

  private velocityX: number = 0;
  private flingTime: number = 0;
  private flingTimerId: number = -1;

  private initCanvas() {
    this.listData = Array(100).fill(0).map((_: number, index: number) => `${index + 1}`);
    this.drawCanvas();
  }

  private drawCanvas() {
    if (this.offsetX > 0) {
      this.offsetX = 0;
    }
    if (this.offsetX < -this.maxOffset) {
      this.offsetX = -this.maxOffset;
    }

    this.canvas.reset();

    this.canvas.font = 'normal normal 24vp sans-serif';
    this.canvas.fillStyle = '#000000';

    let width: number = 0;
    for (let i = 0; i < this.listData.length; i++) {
      const metrics = this.canvas.measureText(this.listData[i]);
      let x = i * DRAW_SPACE + width + this.offsetX;
      if (x >= 0 && x <= this.canvas.width) {
        this.canvas.fillText(this.listData[i], x, this.canvas.height / 2);
      }
      width += metrics.width;
    }
    this.maxOffset = width + this.canvas.width;
  }

  private onPanGestureUpdate(offsetX: number) {
    this.offsetX += offsetX - this.startX;
    this.startX = offsetX;
    this.drawCanvas();
  }

  private scrollFling(speed: number) {
    const frameTime: number = 16;       // 假设每隔16ms进行画布重绘
    const frictionFactor: number = 2;   // 摩擦系数，系数越大阻力越大

    this.velocityX = speed;
    this.flingTime = Math.abs(this.velocityX) / frictionFactor;

    const redrawCanvas = () => {
      if (this.flingTime < frameTime) { // 滑动时间不足时，停止定时器
        this.reset();
        return;
      }

      this.velocityX -= frictionFactor * frameTime;
      this.flingTime -= frameTime;

      // 计算滑动速度和滑动距离，示例使用指数函数方式计算速度和距离，以达到先快后慢的效果
      const v = speed * Math.pow(Math.E, -frictionFactor * (speed - this.velocityX) / frameTime * (frameTime / 1000));
      const distance = v * (frameTime / 1000);
      this.offsetX += distance;

      // 偏移量不在[-maxOffset, 0]区间时，需修正偏移量，并停止定时器
      if (this.offsetX > 0) {
        this.reset();
      }
      if (this.offsetX < -this.maxOffset) {
        this.reset();
      }

      this.drawCanvas();
    };

    this.stopTimer();
    this.flingTimerId = setInterval(redrawCanvas, frameTime);
  }

  private stopTimer() {
    if (this.flingTimerId !== -1) {
      clearInterval(this.flingTimerId);
      this.flingTimerId = -1;
    }
  }

  private reset() {
    this.flingTime = 0;
    this.velocityX = 0;
    this.stopTimer();
  }

  build() {
    Column() {
      Canvas(this.canvas)
        .size({ width: '100%', height: CANVAS_HEIGHT })
        .borderRadius(8)
        .borderWidth(1)
        .borderColor(Color.Gray)
        .clip(true)
        .onReady(() => {
          this.initCanvas();
        })
        .gesture(
          PanGesture()
            .onActionStart((event: GestureEvent) => {
              this.startX = event.offsetX;
            })
            .onActionUpdate((event: GestureEvent) => {
              this.onPanGestureUpdate(event.offsetX);
            })
            .onActionEnd((event: GestureEvent) => {
              this.scrollFling(event.velocityX);
            })
        )
    }
    .size({ width: '100%', height: '100%' })
    .padding(16)
    .justifyContent(FlexAlign.Center)
  }
}
```
