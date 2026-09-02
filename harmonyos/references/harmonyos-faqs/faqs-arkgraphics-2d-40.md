---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkgraphics-2d-40
title: 如何使OffscreenCanvas绘制的内容同步到多个Canvas中
breadcrumb: FAQ > 图形开发 > 2D图形（ArkGraphics 2D） > 如何使OffscreenCanvas绘制的内容同步到多个Canvas中
category: harmonyos-faqs
scraped_at: 2026-09-02T15:04:24+08:00
doc_updated_at: 2026-08-13
content_hash: sha256:8cd8ace7988411c8193c19e59aa963dfbe4c8cb0da9b3d919458dc9dec4956f1
---

## 问题现象

父子自定义组件中都存在Canvas画布，如何能够绘制一次内容使其同步在这些Canvas画布中？

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/J6HT67w-TeGlqdzPZ7iDNA/zh-cn_image_0000002628393364.png "点击放大")

## 背景知识

* [Canvas](../harmonyos-references/ts-components-canvas-canvas.md)是画布组件，提供了一个用于绘制内容的区域。
* [OffscreenCanvas](../harmonyos-references/ts-components-offscreencanvas.md)是用于离屏绘制的画笔，可以在一个类中创建并绘制内容，然后在自定义组件中通过[getImageData](../harmonyos-references/ts-components-canvas-common-method.md#getimagedata)将绘制的内容传递到不同Canvas上。
* [使用状态变量驱动画布刷新](../harmonyos-guides/arkts-drawing-customization-on-canvas.md#使用状态变量驱动画布刷新)：状态变量变更时，本身不会导致Canvas中绘制内容的更新，这时可以用@Watch去监听状态变量的更新，通过@Watch的回调方法去主动地更新绘制内容。

## 解决方案

1. 创建一个类，包含OffscreenCanvas的初始化及绘制方法。该类通过@Observed装饰，使得绘制的内容可以传递到不同组件中的Canvas上。

   ```ts
   import { LengthMetricsUnit } from '@kit.ArkUI';

   const WH: number = 256;

   @Observed
   class DemoLayer {
     canvas: OffscreenCanvas;
     context: OffscreenCanvasRenderingContext2D;
     data: ImageData | undefined;
     fp: number = 0;

     constructor() {
       this.canvas = new OffscreenCanvas(WH, WH, LengthMetricsUnit.PX);
       this.context = this.canvas.getContext('2d', new RenderingContextSettings(false));
     }

     draw(): void {
       this.context.fillStyle = '#5291FF';
       this.context.fillRect(0, 0, WH, WH);
       this.context.lineWidth = 5;
       this.context.strokeStyle = '#F1F3F5';
       this.context.beginPath();
       this.context.ellipse(WH / 2, WH / 2, WH / 2, WH / 2, 0, 0, Math.PI * 2);
       this.context.stroke();
     }

     flip(): void {
       this.fp = 1 - this.fp;
     }
   }
   ```
2. 通过类的实例，将绘制的内容传递给不同Canvas的画笔。

   **说明** 

   在Index中是直接通过点击操作执行的putImageData，在DemoItem中则是通过@Watch的回调执行的putImageData。

   ```ts
   @Entry
   @Component
   struct SyncCanvasContent {
     message: string = '点击最大的方框进行绘图';
     private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(new RenderingContextSettings(false));
     private context2: CanvasRenderingContext2D = new CanvasRenderingContext2D(new RenderingContextSettings(false));
     @State layer: DemoLayer = new DemoLayer();

     build() {
       RelativeContainer() {

         Text(this.message)
           .id('DemoHelloWorld')
           .fontSize(28)
           .fontWeight(FontWeight.Bold)
           .alignRules({
             center: { anchor: '__container__', align: VerticalAlign.Bottom },
             middle: { anchor: '__container__', align: HorizontalAlign.Center }
           });

         DemoItem({ layer: this.layer })
           .alignRules({
             center: { anchor: '__container__', align: VerticalAlign.Top },
             middle: { anchor: '__container__', align: HorizontalAlign.Center }
           });

         Row({ space: 20 }) {
           Canvas(this.context)
             .width(200)
             .height(200)
             .borderWidth(2)
             .onClick(() => this.onButtonClick());

           Canvas(this.context2)
             .width(100)
             .height(100)
             .borderWidth(2);
         }
         .alignRules({
           center: { anchor: '__container__', align: VerticalAlign.Center },
           middle: { anchor: '__container__', align: HorizontalAlign.Center }
         });

       }
       .height('100%')
       .width('100%');
     }

     onButtonClick(): void {
       console.info('onButtonClick');
       this.layer.draw();
       this.layer.data = this.layer.context.getImageData(0, 0, WH, WH);
       this.context.putImageData(this.layer.data, 0, 0);
       // 此句用于证明layer中的绘画数据可以被多个context使用
       this.context2.putImageData(this.layer.data, 0, 0);
     }
   }

   @Component
   struct DemoItem {
     private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(new RenderingContextSettings(false));
     @ObjectLink @Watch('change') layer: DemoLayer;

     change() {
       this.context.putImageData(this.layer.data, 0, 0);
     }

     build() {
       Stack() {
         Canvas(this.context)
           .width('100%')
           .height('100%');
       }
       .width(60)
       .height(60)
       .borderWidth(2);
     }
   }
   ```
