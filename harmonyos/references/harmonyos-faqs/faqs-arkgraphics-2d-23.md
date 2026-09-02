---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkgraphics-2d-23
title: Canvas实现镂空效果
breadcrumb: FAQ > 图形开发 > 2D图形（ArkGraphics 2D） > Canvas实现镂空效果
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:46+08:00
doc_updated_at: 2026-08-13
content_hash: sha256:abfc92e03dc85ebb29821ebb7fa0122284fac1b1fa251346159db47cac7582cc
---

## 问题现象

如何使用Canvas组件实现镂空效果？

## 背景知识

* [Canvas](../harmonyos-references/ts-components-canvas-canvas.md)：提供画布的组件，用于自定义绘制图形，其基于[CanvasRenderingContext2D](../harmonyos-references/ts-canvasrenderingcontext2d.md)进行绘制，绘制对象可以是矩形、文本、图片等。
* [clearRect](../harmonyos-references/ts-components-canvas-common-method.md#clearrect)：删除指定区域内的绘制内容。
* [blendMode](../harmonyos-references/ts-universal-attributes-image-effect.md#blendmode11)：将当前控件的内容（包含子节点内容）与下方画布（可能为离屏画布）已有内容进行混合。

## 解决方案

* **方案一**：在Canvas组件中，通过CanvasRenderingContext2D的[rect](../harmonyos-references/ts-components-canvas-common-method.md#rect)方法绘制一个矩形，并将[globalCompositeOperation](../harmonyos-references/ts-components-canvas-common-property.md#globalcompositeoperation)属性设置为xor，以实现图层的异或合成效果。由于xor模式会使重叠区域的颜色值为透明，因此可以通过该方式使绘制区域与背景产生透明重叠，从而达到镂空的视觉效果。

  ```ts
  import { display } from '@kit.ArkUI';

  @Entry
  @Component
  struct ClearRectOne {
    private settings: RenderingContextSettings = new RenderingContextSettings(true);
    private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);

    build() {
      Stack({ alignContent: Alignment.TopStart }) {
        Canvas(this.context)
          .width('100%')
          .height('100%')
          .onReady(() => {
            // 设置全局合成操作模式为XOR
            this.context.globalCompositeOperation = 'xor';
            this.context.beginPath();
            // 计算屏幕宽度和高度并绘制矩形
            this.context.rect(0, 0, this.getUIContext().px2vp(display.getDefaultDisplaySync().width),
              this.getUIContext().px2vp(display.getDefaultDisplaySync().height) - 40);
            this.context.closePath();
            this.context.fillStyle = '#000000';
            this.context.fill();
            this.context.beginPath();
            this.context.rect(100, 100, 200, 200);
            this.context.closePath();
            this.context.fillStyle = '#000000';
            this.context.fill();
          })
          .opacity(0.6);
      }
      .backgroundColor(Color.Yellow)
      .width('100%')
      .height('100%');
    }
  }
  ```
* **方案二**：使用clearRect清除部分区域，形成镂空效果。

  ```ts
  @Entry
  @Component
  struct ClearRectTwo {
    private settings: RenderingContextSettings = new RenderingContextSettings(true);
    private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);

    build() {
      Stack({ alignContent: Alignment.TopStart }) {
        Canvas(this.context)
          .width(200)
          .height(200)
          .backgroundColor(undefined)
          .onReady(async () => {
            // 设置填充色
            this.context.fillStyle = '#000000';
            // 绘制覆盖整个Canvas的矩形
            this.context.fillRect(0, 0, 140, 140);
            // 在矩形中心位置创建镂空区域
            this.context.clearRect(40, 40, 60, 60);
          })
          .opacity(0.6);
      }
      .backgroundColor(Color.Yellow)
      .padding({ top: 100, left: 120 })
      .width('100%')
      .height('100%');
    }
  }
  ```
* **方案三**：除了通过Canvas方法实现外，还可以通过设置重叠组件的blendMode属性，实现重叠部分透明的效果。

  ```ts
  @Entry
  @Component
  struct ClearRectThree {
    build() {
      Stack() {
        // 背景设置
        Column() {
        }
        .width('100%')
        .height('100%')
        .backgroundColor(Color.Yellow);

        Stack() {
          // 绘制镂空区域
          Circle({ width: 50, height: 50 })
            .blendMode(BlendMode.XOR, BlendApplyType.OFFSCREEN);
        }
        .blendMode(BlendMode.SRC_OVER, BlendApplyType.OFFSCREEN)
        .backgroundColor('rgba(0, 0, 0, 1)')
        .width(80)
        .height(80);
      }
      .width('100%')
      .height('100%');
    }
  }
  ```
