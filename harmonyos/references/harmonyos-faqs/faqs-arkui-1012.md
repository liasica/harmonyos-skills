---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1012
title: Canvas绘制文字时如何设置样式
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > Canvas绘制文字时如何设置样式
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:25+08:00
doc_updated_at: 2026-08-13
content_hash: sha256:29581fc0e5f9577694135b52830bdb33470669e35a55721c10686176aff91d5c
---

## 问题现象

Canvas提供了绘制文字的API，开发者在使用fillText绘制文字时会遇到以下场景：

* **场景一**：如何设置字体常规样式？
* **场景二**：如何绘制自定义字体？
* **场景三**：如何绘制渐变色字体？
* **场景四**：如何设置字体阴影？

## 背景知识

* [Canvas](../harmonyos-guides/arkts-drawing-customization-on-canvas.md)：提供画布组件，用于自定义绘制图形，开发者使用CanvasRenderingContext2D对象和OffscreenCanvasRenderingContext2D对象在Canvas组件上进行绘制，绘制对象可以是基础形状、文本、图片等。
* [font](../harmonyos-references/ts-components-canvas-common-property.md#font)：设置文本绘制中的字体样式，此属性为只写属性，API version 20及以后支持注册过的自定义字体。
* [fillText](../atomic-ascf/apis-canvas-rendering-context-2d.md#canvasrenderingcontext2dfilltext)：绘制填充类文本。
* [strokeText](../atomic-ascf/apis-canvas-rendering-context-2d.md#canvasrenderingcontext2dstroketext)：绘制描边类文本。
* [createLinearGradient](../harmonyos-references/ts-components-canvas-common-method.md#createlineargradient)：用于创建一个线性渐变色。
* [shadowBlur](../harmonyos-references/ts-components-canvas-common-property.md#shadowblur)：设置绘制阴影时的模糊级别。

## 解决方案

* **场景一**：设置字体常规样式。

  Canvas提供了fillText和strokeText两个API分别用于绘制填充类文本和绘制描边类文本，另外提供了font属性来设置字体样式，其语法如下：ctx.font = 'font-style font-weight font-size font-family'。具体示例可以参照官网[font](../harmonyos-references/ts-components-canvas-common-property.md#font)属性。
* **场景二**：绘制自定义字体。

  在API version 20及以后版本Canvas支持使用自定义字体绘制，有以下两种方式：
  1. 直接调用字体引擎的[fontCollection.loadFontSync](../harmonyos-references/js-apis-graphics-text.md#loadfontsync)接口来注册，示例可以参照官网[font](../harmonyos-references/ts-components-canvas-common-property.md#font)属性。
  2. 通过ArkUI的异步接口[this.uiContext.getFont().registerFont](../harmonyos-references/arkts-apis-uicontext-font.md#registerfont)注册：

     ```ts
     @Entry
     @Component
     struct CanvasCustomFont {
       private settings: RenderingContextSettings = new RenderingContextSettings(true);
       private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);

       aboutToAppear(): void {
         this.getUIContext().getFont().registerFont({
           familyName: 'customFont',
           familySrc: $rawfile('customFont.ttf') // rawfile目录下自定义字体，开发者可以自行替换
         });
       }

       build() {
         Column() {
           Button('Draw Custom Font').width(200).onClick(() => {
             this.context.font = '150px customFont';
             this.context.fillText('Hello World!', 60, 200);
           });
           Canvas(this.context)
             .width('100%')
             .height('100%')
             .onReady(() => {
               this.context.font = '150px sans-serif';
               this.context.fillText('Hello World!', 60, 100);
             });
         }
         .width('100%')
         .height('100%')
         .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM]);
       }
     }
     ```

     效果预览：

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/vsPTp0DcRXujV6FOKwBilw/zh-cn_image_0000002658804045.png "点击放大")

* **场景三**：绘制渐变色字体。

  Canvas提供了createLinearGradient、createRadialGradient和createConicGradient接口用于创建渐变色，创建完成后可以使用fillStyle或者strokeStyle来指定绘制的填充色和线条颜色。

  ```ts
  @Entry
  @Component
  struct CanvasGradFont {
    private settings: RenderingContextSettings = new RenderingContextSettings(true);
    private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);

    build() {
      Column() {
        Canvas(this.context)
          .width('100%')
          .height('100%')
          .onReady(() => {
            this.context.font = '150px sans-serif';
            // 创建一个线性渐变
            let grad = this.context.createLinearGradient(50, 0, 300, 100);
            grad.addColorStop(0.0, '#f88b57');
            grad.addColorStop(0.4, '#aee4a0');
            grad.addColorStop(0.7, '#c4d1ec');
            grad.addColorStop(0.9, '#c08dcc');
            // 后续fill相关绘制都会使用该线性渐变
            this.context.fillStyle = grad;
            this.context.fillText('Hello World!', 60, 100);

            // 创建一个径向渐变
            let radialGrad = this.context.createRadialGradient(200, 200, 50, 200, 200, 200);
            radialGrad.addColorStop(0.0, 'rgb(39,135,217)');
            radialGrad.addColorStop(0.5, 'rgb(255,238,240)');
            radialGrad.addColorStop(1.0, 'rgb(112,112,112)');
            // 后续stroke相关绘制都会使用该径向渐变
            this.context.strokeStyle = radialGrad;
            this.context.strokeText('Hello World!', 60, 200);
          });
      }
      .width('100%')
      .height('100%')
      .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM]);
    }
  }
  ```

  效果预览：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/40o0lB3SQKyt0gtkh6zB8g/zh-cn_image_0000002628404776.png "点击放大")

* **场景四**：设置字体阴影。

  通过设置shadowBlur和shadowColor属性可以增加阴影设置效果，以此来实现文字阴影效果。

  ```ts
  @Entry
  @Component
  struct CanvasShadowFont {
    private settings: RenderingContextSettings = new RenderingContextSettings(true);
    private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);

    build() {
      Column() {
        Canvas(this.context)
          .width('100%')
          .height('100%')
          .onReady(() => {
            this.context.font = '150px sans-serif';
            this.context.fillText('Hello World!', 60, 100);
            // 设置阴影样式
            this.context.shadowBlur = 30;
            this.context.shadowColor = 'rgb(0,0,0)';
            this.context.fillText('Hello World!', 60, 200);
          });
      }
      .width('100%')
      .height('100%')
      .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM]);
    }
  }
  ```

  效果预览：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/Vf05NfuYR7m_XM1z4n3cSA/zh-cn_image_0000002628564682.png "点击放大")

## 总结

Canvas提供了绘制文字的API，其文字样式主要受到font、fillStyle和strokeStyle属性影响：

1. font属性可设置font-style、font-weight、font-size和font-family这四个文字属性，其中font-family可以指定字体系列。除了系统提供的sans-serif、serif和monospace，还支持设置自定义字体。
2. fillStyle和strokeStyle属性用于设置Canvas绘制的填充色和线条颜色，设置以后对后续的fill和stroke操作生效，由于字体绘制是通过fillText和strokeText实现的，因此也可以通过fillStyle和strokeStyle实现渐变色和阴影效果。
