---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1441
title: 关于Span减少字体大小无法自适应缩放的问题
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 关于Span减少字体大小无法自适应缩放的问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:10+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:be1cae7bab63d7ae4b701273fc49f7cfd62b37d7befedd6204bb0370a6d0c5e7
---

## 问题现象

在Text中使用了多个Span，每个Span使用不同的颜色，希望这个组件宽度不超过一个固定值，当超过时，通过减小字体大小来进行自适应。目前给Text组件设置minFontSize不起作用，有什么方案能够实现自适应？

示例代码：

```ts
@Entry
@Component
struct NavigationPage {
  build() {
    Navigation(){
      Text() {
        Span('Span')
          .fontColor('#65ba5f')
        Span('123456789')
          .fontColor('#0A59F7')
      }
      .fontSize($r('app.float.page_text_font_size'))
      .maxFontSize($r('app.float.page_text_font_size'))
      .minFontSize($r('app.float.page_text_font_size'))
      .maxLines(1)
    }
    .padding(24)
    .mode(NavigationMode.Stack)
    .backgroundColor('#F1F3F5')
    .height('100%')
    .width('100%')
  }
}
```

异常效果图：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/bW1SNaz8S8OC-yA8mEGZAw/zh-cn_image_0000002658843523.png "点击放大")

## 背景知识

* [Text组件](../harmonyos-references/ts-basic-components-text.md)：显示一段文本的组件，包含Span子组件。除支持通用属性，还支持minFontSize、maxFontSize等属性。
* [Span组件](../harmonyos-references/ts-basic-components-span.md)：作为Text组件的子组件，用于显示行内文本的组件。支持继承的属性仅包括：fontColor、fontSize、fontStyle、fontWeight、decoration、letterSpacing、textCase、fontfamily、textShadow。

## 解决方案

Span组件本身是行内元素，默认情况下它的宽度是由其内容自动撑开的，不能直接设置宽度，会一直撑开到撑满父组件为止，建议换成Text组件。

代码如下：

```ts
// @Extend(Text)可以支持Text的私有属性minFontSize
@Extend(Text)
function fancy() {
  .maxLines(1)
  .minFontSize(12)
  .maxFontSize(30)
  .fontColor('#f1f2f3')
  .width(70)
  .height(30);
}

@Entry
@Component
struct TextAreaPage {
  build() {
    Row() {
      Text('123456').fancy().backgroundColor('#8C43F2');
      Text('1234567890123456').fancy().backgroundColor('#A45AC6');
    }
    .padding(24)
    .width('100%')
    .height('100%');
  }
}
```
