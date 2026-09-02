---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-857
title: 更换系统语言后组件出现显示遮挡
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 更换系统语言后组件出现显示遮挡
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:15+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:557cd0be3fa91382a721890938a3b826076707bfd0ae974be0b1179110fdf36c
---

## 问题现象

更换系统语言后（由中文切换为英文）组件出现显示遮挡。

## 背景知识

当应用需要提供给不同国家和地区的用户使用时，为了满足这些用户在语言、文化方面的需求，需要将应用进行[本地化定制](../harmonyos-guides/l10n.md)，使应用加载和显示符合所在地域使用习惯的内容。界面加载的内容包括文本字符、图片、音频、视频等资源。

## 问题定位

1. 通过DevEco Testing确认页面布局样式，发现开发者使用Text组件用于展示文本。
2. 检查发现Text组件设置固定宽高，且未使用Scroll组件，导致当文本内容较多时，页面无法滚动。

## 分析结论

页面中使用Text组件展示文本，当展示内容为中文时，Text组件刚好可以完全覆盖文本内容。而当系统切换语言为英文时，由于对应的英文内容较长，固定宽高的Text组件无法展示完全，从而导致英文文本覆盖了下面的组件。

## 修改建议

如果开发者无法确认不同语言文本内容量时，可以考虑使用Scroll进行包裹，当子组件的布局尺寸超过父组件的尺寸时，内容可以滚动。修复后代码如下：

1. 首先在string.json文件中分别配置GettingStarted对应的中文和英文。
2. 在页面中使用对应的字符内容。

   ```screen
   @Component
   @Entry
   struct MyCustScroll {
     build() {
       Column() {
         // 当子组件的布局尺寸超过父组件的尺寸时，内容可以滚动。
         Scroll() {
           // 使用资源文件，需根据实际业务自行选择
           Text($r('app.string.GettingStarted'))
             .fontSize(16);
         }
         .padding(16)
         .width(300)
         .height(115)
         .backgroundColor(Color.Pink);

         Button('确认')
           .width(300)
           .margin(20);
       }.padding(20);
     }
   }
   ```
