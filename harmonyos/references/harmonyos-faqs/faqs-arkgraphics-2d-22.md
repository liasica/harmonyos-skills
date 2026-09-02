---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkgraphics-2d-22
title: 如何在Canvas上绘制不同对齐方式的文字
breadcrumb: FAQ > 图形开发 > 2D图形（ArkGraphics 2D） > 如何在Canvas上绘制不同对齐方式的文字
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:46+08:00
doc_updated_at: 2026-08-13
content_hash: sha256:f37c6bfe8d1af6aadca0d530639c983b9ce45276e908c1e6bc81c520b9fa68fb
---

## 问题现象

通过Canvas绘制填充类文本时，如何实现整体文字的对齐方式？例如居中、居右或者居左？

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6a/v3/sLGvBTamQu2e74zt6QPEQw/zh-cn_image_0000002628393354.png "点击放大")

## 背景知识

* [Canvas](../harmonyos-references/ts-components-canvas-canvas.md)提供画布组件，[CanvasRenderingContext2D](../harmonyos-references/ts-canvasrenderingcontext2d.md)接口能够使用RenderingContext在Canvas组件上进行绘制，绘制对象可以是矩形、文本、图片等。
* [fillText](../atomic-ascf/apis-canvas-rendering-context-2d.md#canvasrenderingcontext2dfilltext)方法能够绘制填充类文本，但一次只能绘制指定区域内的文本，无法一次性绘制具有不同对齐方式的文本。

## 解决方案

实现在Canvas上绘制不同对齐方式的文字，具体方法如下：

1. 创建RenderingContextSettings和CanvasRenderingContext2D对象，用于配置和管理Canvas的渲染上下文。同时定义leftText、centerText和rightText三个变量，分别用于展示左对齐、居中对齐和右对齐的文字内容；letterSpacing用于设置字符间距；lineX用于标识参考线的水平位置。

   ```ts
   private settings: RenderingContextSettings = new RenderingContextSettings(true);
   private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
   private leftText: string = '文字左对齐';
   private centerText: string = '文字居中对齐';
   private rightText: string = '文字右对齐';
   private letterSpacing: number = 1;
   private lineX: number = 200;
   ```
2. getTotalWidth方法用于计算指定文本的总宽度，其实现方式为逐个遍历文本中的字符，并累加每个字符的宽度及其对应的间距，最终得到文本整体的宽度总和。

   ```ts
   getTotalWidth(text: string): number {
     let totalWidth = 0;
     for (let i = 0; i < text.length; i++) {
       // 累计已占用宽度
       if (i === text.length - 1) {
         totalWidth += this.context.measureText(text[i]).width;
       } else {
         totalWidth += this.context.measureText(text[i]).width + this.letterSpacing;
       }
     }
     return totalWidth;
   }
   ```
3. 在Canvas的onReady事件中，首先将画笔颜色设置为蓝色，并绘制一条参考线作为对齐基准。随后，在该事件处理函数中，通过计算确定文本的绘制位置，并利用循环调用fillText方法，依次绘制具有不同对齐方式的文本内容：
   * 左对齐：通过累加每个字符的宽度和间距，确定文字绘制的起始位置。

     ```ts
     let leftTotalWidth = this.lineX;
     this.context.font = '24vp sans-serif';
     for (let i = 0; i < this.leftText.length; i++) {
       this.context.fillText(this.leftText[i], leftTotalWidth, 50);
       // 累计已占用宽度
       if (i === this.leftText.length - 1) {
         leftTotalWidth += this.context.measureText(this.leftText[i]).width;
       } else {
         leftTotalWidth += this.context.measureText(this.leftText[i]).width + this.letterSpacing;
       }
     }
     ```
   * 居中对齐：先计算文本的总宽度，然后将起始位置设置为（lineX-总宽度一半），以实现居中对齐。

     ```ts
     let centerTotalWidth = 0;
     centerTotalWidth = this.getTotalWidth(this.centerText);
     centerTotalWidth = this.lineX - centerTotalWidth / 2;
     for (let i = 0; i < this.centerText.length; i++) {
       this.context.fillText(this.centerText[i], centerTotalWidth, 90);
       // 累计已占用宽度
       if (i === this.centerText.length - 1) {
         centerTotalWidth += this.context.measureText(this.centerText[i]).width;
       } else {
         centerTotalWidth += this.context.measureText(this.centerText[i]).width + this.letterSpacing;
       }
     }
     ```
   * 右对齐：先计算文本的总宽度，然后将起始位置设置为（lineX-总宽度），以实现右对齐。

     ```ts
     let rightTotalWidth = 0;
     rightTotalWidth = this.getTotalWidth(this.rightText);
     rightTotalWidth = this.lineX - rightTotalWidth;
     for (let i = 0; i < this.rightText.length; i++) {
       this.context.fillText(this.rightText[i], rightTotalWidth, 130);
       // 累计已占用宽度
       if (i === this.rightText.length - 1) {
         rightTotalWidth += this.context.measureText(this.rightText[i]).width;
       } else {
         rightTotalWidth += this.context.measureText(this.rightText[i]).width + this.letterSpacing;
       }
     }
     ```

完整示例参考如下：

```ts
@Entry
@Component
struct Index {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  private leftText: string = '文字左对齐';
  private centerText: string = '文字居中对齐';
  private rightText: string = '文字右对齐';
  private letterSpacing: number = 1;
  private lineX: number = 200;
  getTotalWidth(text: string): number {
    let totalWidth = 0;
    for (let i = 0; i < text.length; i++) {
      // 累计已占用宽度
      if (i === text.length - 1) {
        totalWidth += this.context.measureText(text[i]).width;
      } else {
        totalWidth += this.context.measureText(text[i]).width + this.letterSpacing;
      }
    }
    return totalWidth;
  }
  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor(Color.White)
        .onReady(() => {
          this.context.strokeStyle = Color.Black;
          this.context.moveTo(this.lineX, 10);
          this.context.lineTo(this.lineX, 160);
          this.context.stroke();
          // 左对齐
          let leftTotalWidth = this.lineX;
          this.context.font = '24vp sans-serif';
          for (let i = 0; i < this.leftText.length; i++) {
            this.context.fillText(this.leftText[i], leftTotalWidth, 50);
            // 累计已占用宽度
            if (i === this.leftText.length - 1) {
              leftTotalWidth += this.context.measureText(this.leftText[i]).width;
            } else {
              leftTotalWidth += this.context.measureText(this.leftText[i]).width + this.letterSpacing;
            }
          }
          // 居中对齐
          let centerTotalWidth = 0;
          centerTotalWidth = this.getTotalWidth(this.centerText);
          centerTotalWidth = this.lineX - centerTotalWidth / 2;
          for (let i = 0; i < this.centerText.length; i++) {
            this.context.fillText(this.centerText[i], centerTotalWidth, 90);
            // 累计已占用宽度
            if (i === this.centerText.length - 1) {
              centerTotalWidth += this.context.measureText(this.centerText[i]).width;
            } else {
              centerTotalWidth += this.context.measureText(this.centerText[i]).width + this.letterSpacing;
            }
          }
          // 右对齐
          let rightTotalWidth = 0;
          rightTotalWidth = this.getTotalWidth(this.rightText);
          rightTotalWidth = this.lineX - rightTotalWidth;
          for (let i = 0; i < this.rightText.length; i++) {
            this.context.fillText(this.rightText[i], rightTotalWidth, 130);
            // 累计已占用宽度
            if (i === this.rightText.length - 1) {
              rightTotalWidth += this.context.measureText(this.rightText[i]).width;
            } else {
              rightTotalWidth += this.context.measureText(this.rightText[i]).width + this.letterSpacing;
            }
          }
        })
        .margin({top:125})
    }
    .width('100%')
    .height('100%')
  }
}
```

## 常见FAQ

Q：将UI组件绘制到Canvas上后，如何截取Canvas获取图片？

A：使用[getPixelMap](../harmonyos-references/ts-components-canvas-common-method.md#getpixelmap)方法即可。

Q：解决方案里的方法能够实现多行文字的对齐效果吗？

A：不能，解决方案是通过绘制参考线，计算和参考线的距离来实现对齐效果，仅供参考，使用多行文字会无法显示完整文字。
