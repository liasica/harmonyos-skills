---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-575
title: ImageSpan使用场景
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > ImageSpan使用场景
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:01+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:5fe433eb803a4367e0529dbb649d5976f65702a47755dbe280d5d68da8a65f6d
---

## 问题现象

如何实现下图中的追加评论效果？

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/q-rZSLXGR0-dZgSnfG2Tpg/zh-cn_image_0000002658791437.png "点击放大")

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/GdwJ2MLkSPaoVqW41lMWew/zh-cn_image_0000002628552050.gif "点击放大")

## 背景知识

* [Span](../harmonyos-references/ts-basic-components-span.md)：作为Text、ContainerSpan组件的子组件，用于显示行内文本的组件。
* [ImageSpan](../harmonyos-references/ts-basic-components-imagespan.md)：Text、ContainerSpan组件的子组件，用于显示行内图片。

## 解决方案

将图片换成镂空图，ImageSpan使用margin属性调整位置。

```screen
@Entry
@Component
struct ImageSpanExample {
  content: string = '到了绿湖底部，面上神色一动。';

  build() {
    Column() {
      Text() {
        Span("\n" + this.content)
          .fontSize(20)
        Span('  11  ')
        ImageSpan($r('app.media.startIcon'))  // 需开发者换成镂空的图
          .width('26vp')
          .height('26vp')
          .margin({ left: -27, bottom: -2 })
      }
    }
    .width('100%')
    .height('100%')
  }
}
```
