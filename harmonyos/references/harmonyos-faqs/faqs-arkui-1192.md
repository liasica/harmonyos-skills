---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1192
title: 如何解决linearGradient渐变到透明时出现黑色的问题
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何解决linearGradient渐变到透明时出现黑色的问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:27+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:3f0633d666d7fa71919982f04d7f5f421855b06239f84d14d70d0f3137f044a2
---

## 问题现象

使用linearGradient实现渐变色，颜色渐变成透明，但不符合预期，比如中间会出现黑色，问题代码如下：

```ts
@Entry
@Component
struct LinearGradientDemo {
  build() {
    Column({ space: 5 }) {
      Row()
        .width('calc(100% - 32vp)')
        .height(150)
        .margin({
          left: 16,
          right: 16
        })
        .linearGradient({
          direction: GradientDirection.Bottom,
          colors: [['#0A59F7', 0], [Color.Transparent, 1]]
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

问题现象如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/ZULbSqNySh2XUqMAwHBuKg/zh-cn_image_0000002628752868.png "点击放大")

## 背景知识

[linearGradient](../harmonyos-references/ts-universal-attributes-gradient-color.md#lineargradient)：设置组件的颜色线性渐变效果。

[Color](../harmonyos-references/ts-appendix-enums.md#color)：颜色枚举说明，其中Transparent的值为rgba(0,0,0,0)，'#00FFFFFF'表示全透明白色。

## 解决方案

Color.Transparent的值为rgba(0,0,0,0)，相当于完全透明的黑色，颜色从'#0A59F7'到Color.Transparent，过程中趋近黑色，所以渐变到透明的中间有黑色，将渐变颜色改成值为'#00FFFFFF'的全透明白色即可，实现代码如下：

```ts
@Entry
@Component
struct LinearGradientDemo {
  build() {
    Column({ space: 5 }) {
      Row()
        .width('calc(100% - 32vp)')
        .height(150)
        .margin({
          left: 16,
          right: 16
        })
        .linearGradient({
          direction: GradientDirection.Bottom,
          colors: [['#0A59F7', 0], [Color.Transparent, 1]]
        })
      Row()
        .width('calc(100% - 32vp)')
        .height(150)
        .margin({
          left: 16,
          right: 16
        })
        .linearGradient({
          direction: GradientDirection.Bottom,
          colors: [['#0A59F7', 0], ['#00FFFFFF', 1]]
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

效果图如下，第二个渐变色中间无黑色。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/4XxyZ_qcSHiTGNbMJoBVBQ/zh-cn_image_0000002658952187.png "点击放大")

## 常见FAQ

Q：使用linearGradient设置渐变颜色时，若渐变颜色设置为白色，如colors: [['#194B63FF', 0], ['#FFFFFF', 1]]，颜色由浅变深最后渐变成白色，不符合预期。

A：将白色设置透明度，可避免颜色由浅变深最后渐变成白色的情况，如colors: [['#194B63FF', 0], ['#00FFFFFF', 1]]。
