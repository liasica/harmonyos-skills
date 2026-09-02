---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkgraphics-2d-24
title: 如何绘制虚线
breadcrumb: FAQ > 图形开发 > 2D图形（ArkGraphics 2D） > 如何绘制虚线
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:46+08:00
doc_updated_at: 2026-08-13
content_hash: sha256:aa3e177474bf75d086399f3a7b3e0ec74f1cffe1efa2c2113069efd5b2c845fc
---

## 问题现象

页面中如何绘制虚线作为边框或分隔线？

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/D91NRnUWQDmCM-_pDOqbww/zh-cn_image_0000002628553240.png "点击放大")

## 背景知识

[Divider](../harmonyos-references/ts-basic-components-divider.md)组件能够分隔不同内容块或内容元素，可以在视觉上界定内容区域和引导用户视线移动，例如，使用垂直虚线分隔列，可以使用户更清晰地查看每一列的内容，同时保持整体的简洁感。Divider除通用属性外，还支持以下四个属性：

* [border](../harmonyos-references/ts-universal-attributes-border.md#border)属性可以为组件实现边框样式。其对象参数[BorderOptions](../harmonyos-references/ts-types.md#borderoptions)中的style设置为Dashed时，显示为一系列短的方形虚线；dashGap可以控制虚线的间距。

* 除border这一属性外，也可以通过[borderStyle](../harmonyos-references/ts-universal-attributes-border.md#borderstyle)，[borderWidth](../harmonyos-references/ts-universal-attributes-border.md#borderwidth)，[borderColor](../harmonyos-references/ts-universal-attributes-border.md#bordercolor)，[borderRadius](../harmonyos-references/ts-universal-attributes-border.md#borderradius)几个属性组合实现虚线的边框样式，从效果上来看，这几个属性都相当于BorderOptions的具体内容。
* [Canvas](../harmonyos-references/ts-components-canvas-canvas.md)是一种画布组件，用于自定义绘制图形，绘制对象可以是基础形状、文本、图片等，[CanvasRenderingContext2D](../harmonyos-references/ts-canvasrenderingcontext2d.md)是该组件的参数，开发者可使用它于Canvas组件上进行绘制。
* [setLineDash](../harmonyos-references/ts-components-canvas-common-method.md#setlinedash)是CanvasRenderingContext2D组件的方法，可用于设置画布的虚线样式。

## 解决方案

* **方案一**：通过给Divider设置borderStyle+borderWidth属性或border属性实现。可参考官网示例[示例1（基本样式用法）](../harmonyos-references/ts-universal-attributes-border.md#示例1基本样式用法)。
* **方案二**：通过Canvas绘制。

  border属性仅能设置间隔长度均匀的虚线，如果需要绘制间隔长度不均匀的虚线，需要Canvas实现。

  1. 创建Canvas组件，传入CanvasRenderingContext2D对象。

     ```ts
     Canvas(this.context)
       .width('100%')
       .height('100%')
       .onReady(() => {
         this.context.lineWidth = 1;
         this.context.strokeStyle = 'black';
         // 用户可在这自定义虚线的样式
         this.context.setLineDash([10, 20, 30, 40, 50, 40, 30, 20, 10]);
         this.wrapText(0, 40, this.context.width);
       });
     ```
  2. 使用context的setLineDash方法，该方法会传入一个number数组，分别交替表示虚线的长度以及虚线的间隔，如果遍历完数组后虚线未达到屏幕的边缘，则会重新遍历数组继续绘制。

     ```ts
     this.context.setLineDash([10, 20, 30, 40, 50, 40, 30, 20, 10]);
     ```
  3. 使用context的stroke方法进行绘制。

     ```ts
     wrapText(x: number, y: number, maxWidth?: number) {
       this.context.beginPath();
       this.context.moveTo(x, y + 10);
       this.context.lineTo(maxWidth, y + 10);
       this.context.stroke();
       this.context.closePath();
     }
     ```
  4. 完整示例参考如下：

     ```ts
     @Entry
     @Component
     struct DashedLine {
       private settings: RenderingContextSettings = new RenderingContextSettings(true);
       private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);

       wrapText(x: number, y: number, maxWidth?: number) {
         this.context.beginPath();
         this.context.moveTo(x, y + 10);
         this.context.lineTo(maxWidth, y + 10);
         this.context.stroke();
         this.context.closePath();
       }
       build() {
         Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
           Canvas(this.context)
             .width('100%')
             .height('100%')
             .onReady(() => {
               this.context.lineWidth = 1;
               this.context.strokeStyle = 'black';
               // 用户可在这自定义虚线的样式
               this.context.setLineDash([10, 20, 30, 40, 50, 40, 30, 20, 10]);
               this.wrapText(0, 40, this.context.width);
             });
         }
         .width('100%')
         .height('100%');
       }
     }
     ```
