---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-tablet-28
title: 页面内容在平板上显示不全
breadcrumb: FAQ > 多设备场景 > 平板 > 常见问题 > 页面内容在平板上显示不全
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:48+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:62fb720c14b68613bbe5df98d1998c75d0704ad717cfcef0a2ab284017edda94
---

## 问题现象

Canvas画布组件在平板横屏显示时，绘制起点未动态变化，导致画布内容底部被其他组件遮挡。

```ts
@Entry
@Component
struct BezierCurveTo {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() => {
          this.context.fillStyle = '#D1D1D6';
          // 坐标都是固定值，容易造成布局异常
          this.context.fillRect(200, 200, 100, 100);
        });
    }
    .width('100%')
    .height('100%');
  }
}
```

## 背景知识

* [Canvas](../harmonyos-references/ts-components-canvas-canvas.md)：提供画布组件，用于自定义绘制图形。
* [CanvasRenderingContext2D](../harmonyos-references/ts-canvasrenderingcontext2d.md)：使用RenderingContext在Canvas组件上进行绘制，绘制对象可以是矩形、文本、图片等。

## 问题定位

检查代码中是否使用display.getDefaultDisplaySync()获取屏幕当前尺寸，并设置Canvas绘制时起点坐标数值是否根据屏幕尺寸动态计算。

## 分析结论

应用Canvas画布起点坐标为固定值，导致在平板上绘制时偏左或偏下，底部被页面其他组件遮挡，无法完全显示。

## 修改建议

使用display.getDefaultDisplaySync()获取屏幕当前尺寸，根据屏幕尺寸及绘制的图形尺寸动态计算绘制起点坐标。

```ts
import { display } from '@kit.ArkUI';

@Entry
@Component
struct BezierCurveTo {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  @State deviceWidth: number = 0;
  @State deviceHeight: number = 0;

  aboutToAppear(): void {
    // 获取屏幕宽高
    this.deviceWidth = this.getUIContext().px2vp(display.getDefaultDisplaySync().width);
    this.deviceHeight = this.getUIContext().px2vp(display.getDefaultDisplaySync().height);
  }

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#F1F3F5')
        .onReady(() => {
          this.context.fillStyle = '#D1D1D6';
          this.context.fillRect(this.deviceWidth * 0.5 - 50, this.deviceHeight * 0.5 - 100, 100, 100);
        });
    }
    .width('100%')
    .height('100%');
  }
}
```
