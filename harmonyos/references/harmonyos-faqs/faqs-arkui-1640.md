---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1640
title: 如何绘制包含emoji的图文混合内容
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何绘制包含emoji的图文混合内容
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:17+08:00
doc_updated_at: 2026-08-13
content_hash: sha256:e470a0776e1658a6c84f9e4eb06c1ac5f332b638cd5ef17fb03c376890bfe76b
---

## 问题现象

在drawTextBlob方法中，当emoji和文字内容是一个字符串混合在一起时，如何绘制包含emoji的图文混合内容？

## 背景知识

* [Canvas](../harmonyos-references/ts-components-canvas-canvas.md)组件主要用于自定义绘制图形。
* [drawTextBlob](../harmonyos-references/arkts-apis-graphics-drawing-canvas.md#drawtextblob)用于绘制一段文字。若构造blob的字体不支持待绘制字符，则该部分字符无法绘制。
* [CanvasRenderingContext2D](../harmonyos-references/ts-canvasrenderingcontext2d.md)是一个使用RenderingContext在Canvas组件上进行绘制的接口。
* [drawSingleCharacter](../harmonyos-references/arkts-apis-graphics-drawing-canvas.md#drawsinglecharacter12)用于绘制单个字符。当前字形中的字体不支持待绘制字符时，退化到使用系统字体绘制字符。

## 解决方案

在此场景下，绘制emoji和文字混合的字符串不适合使用drawTextBlob方法。

* 方案一：可以用画布绘制将emoji和文字内容一起作为文本显示。参考代码如下：

  ```ts
  @Entry
  @Component
  struct DrawingMixedGraphicsAndText {
    private settings: RenderingContextSettings = new RenderingContextSettings(true);
    private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
    private emoji: string = '123456\ud83d\ude06\ud83d\ude0b';

    build() {
      Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
        Canvas(this.context)
          .width('100%')
          .height('100%')
          .onReady(() => {
            this.context.font = `${this.getUIContext().vp2px(30)}px bold sans-serif-black`;
            this.context.fillText(this.emoji, 20, 50);
          });
      }
      .width('100%')
      .height('100%');
    }
  }
  ```

  效果预览：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/G8W1eZdARiOAQYmE1SxgZQ/zh-cn_image_0000002628662310.png "点击放大")
* 方案二：由于drawTextBlob不支持降级，可以通过接口drawSingleCharacter实现，drawSingleCharacter有字体退化处理的能力（在用户给的字体typeface不支持某些表情包时，可以退化查找其他已载入字体的typeface），没有设置字体会使用系统默认字体。具体使用可参考[drawSingleCharacter](../harmonyos-references/arkts-apis-graphics-drawing-canvas.md#drawsinglecharacter12)中的示例，将示例中绘制的字符串替换为emoji即可。

## 常见FAQ

Q：绘制带emoji或纯emoji的字符串的高度和宽度怎么获取呢？

A：可以使用文本计算[measureText](../harmonyos-references/ts-components-canvas-common-method.md#measuretext)，参考官方示例。
