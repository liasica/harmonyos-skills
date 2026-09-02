---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-926
title: 如何实现覆盖状态栏的渐变背景效果
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何实现覆盖状态栏的渐变背景效果
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:20+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:cd3380808a4dcb7fdfd52bc9c57c54f5097764772f4ec04926baa08752817c1c
---

## 问题现象

为了避免状态栏颜色与背景重合，需根据状态栏和内容区域的颜色进行沉浸式适配。在设置内容区域背景色时，需要设置颜色从右向左线性渐变。如何实现上述效果？

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/EKFPLN9SS82-P8MsFuOtsg/zh-cn_image_0000002658799579.png "点击放大")

## 背景知识

* [沉浸式页面开发](../best-practices/bpta-multi-device-window-immersive.md)常通过将应用页面延伸到状态栏的方式，来最大程度利用屏幕可视区域，使页面获得更大的布局空间。为了实现该效果，可通过对顶部组件使用[expandSafeArea](../harmonyos-references/ts-universal-attributes-expand-safe-area.md#expandsafearea)属性扩展安全区域属性。
* [linearGradient](../harmonyos-references/ts-universal-attributes-gradient-color.md#lineargradient)属性设置组件的颜色渐变效果，颜色渐变属于组件内容，绘制在背景上方。

## 解决方案

1. 沉浸式页面开发将应用页面延伸到状态栏。对页面中顶部组件使用expandSafeArea属性扩展安全区域属性。
2. 通过linearGradient来实现组件的颜色线性渐变。

完整示例参考如下：

```ts
@Entry
@Component
struct Linear {
  build() {
    Column() {
      Column() {
        Text('顶部渐变')
          .textAlign(TextAlign.Center)
          .fontSize(40)
          .width('100%')
      }
      .backgroundColor('#F08080')
      .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP])
      .linearGradient({
        // 实现从左到右，默认为垂直。90°为水平
        angle: 90,
        colors: [[0x8981F4, 0.0], [0x86C4E3, 0.3], [0x63CEBF, 1.0]]
      })
    }
    .width('100%')
    .height('100%')
  }
}
```
