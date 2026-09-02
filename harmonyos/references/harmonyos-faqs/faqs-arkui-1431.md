---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1431
title: 如何设置组件单边阴影样式
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何设置组件单边阴影样式
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:20+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:70e454b364ed55e91552d2b4f42e7c119df60d6d9c30dea6d6f3e1d66125e3f6
---

## 问题现象

如何设置矩形组件仅显示单边阴影（如上边阴影），其他三边不显示？

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/yicWB4xxQh6GKmPgEXyviQ/zh-cn_image_0000002658843017.gif "点击放大")

## 背景知识

HarmonyOS提供阴影接口[shadow](../harmonyos-references/ts-universal-attributes-image-effect.md#shadow)可以为当前组件添加阴影效果，该接口支持两种类型参数：

* [ShadowOptions](../harmonyos-references/ts-universal-attributes-image-effect.md#shadowoptions对象说明)类型可自定义阴影效果，用于设置阴影的模糊半径、阴影的颜色、X轴和Y轴的偏移量。在ShadowOptions模式下，当radius=0或者color的透明度为0时，无阴影效果。
* [ShadowStyle](../harmonyos-references/ts-universal-attributes-image-effect.md#shadowstyle10枚举说明)类型可简单配置阴影样式，主要改变阴影的大小尺寸。

## 解决方案

利用上层组件的特殊阴影样式配置与下层矩形组件的布局拼接，可实现单边阴影效果。

完整示例参考如下：

```screen
@Entry
@Component
struct ShadowDemo {
  @State flag: boolean = false;

  build() {
    Column() {
      if (this.flag) {
        Row() {
        }
        .width(200)
        .height(10)
        .shadow({
          color: '#ff745454', // 阴影颜色
          radius: 20, // 阴影模糊半径
          offsetY: -20, // 阴影Y轴偏移量(负值表示向上)
        })
      }

      Row() {
        // 组件内容
        Text('设置单边阴影')
          .fontColor(Color.Black)
          .width(100)
          .height(100)
          .onClick(() => {
            this.flag = !this.flag;
          })
      }
      .justifyContent(FlexAlign.Center)
      .width(200)
      .height(200)
      .backgroundColor('#0a59f7')
      .offset({ x: 0, y: -10 })
    }
    .margin({ top: 50 })
    .width('100%')
  }
}
```

## 总结

当前组件通用属性支持阴影类型、模糊半径、颜色及X/Y轴偏移量的配置，但无法直接实现单边阴影。通过组合设置部分子组件的阴影样式，并与其他子组件拼接，可间接实现单边阴影效果。
