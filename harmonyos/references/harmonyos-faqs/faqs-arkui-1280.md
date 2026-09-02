---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1280
title: 解决Slider精度问题
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 解决Slider精度问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:08+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:f5f8050732e17b814a9e03c9780203d30d1c70e9e04be2eb16a8d694a7cf5d72
---

## 问题现象

Slider组件，step设置为0.1时，滑动时显示的value不是正常的35.1、35.2、35.3，而是35.70000076293945、36.400001525878906这类数值，如何解决？

问题代码示例参考如下：

```screen
@Entry
@Component
struct Question {
  textTimerController: TextTimerController = new TextTimerController();
  @State tempLatrue: number = 35;

  build() {
    Column() {
      Slider({
        value: this.tempLatrue,
        min: 34.5,
        max: 43.1,
        style: SliderStyle.OutSet,
        step: 0.1
      })
        .width('100%')
        .margin({ top: 15, bottom: 15 })
        .onChange((value: number) => {
          this.tempLatrue = value;
        }).showTips(true, `${this.tempLatrue}`)
    }
  }
}
```

问题效果预览：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/dKgBOfWTSn6WUObdpDPC1w/zh-cn_image_0000002628757874.gif "点击放大")

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/6fpeuVJyR2OQYhZeITk6Sg/zh-cn_image_0000002658957189.gif "点击放大")

## 背景知识

[Slider](../harmonyos-references/js-components-basic-slider.md)：滑动条组件，用来快速调节设置值，如音量、亮度等。

## 解决方案

浮点数在计算机中是通过二进制形式存储的，某些十进制浮点数在二进制中无法精确表示，导致了运算结果的精度问题。

1. 使用toFixed(3)将数值转换为十进制定点模式表示的字符串，并保留小数点后3位。
2. 使用slice(0, -1)截取字符串。
3. 使用parseFloat返回一个新的浮点数，并展示。

```screen
@Entry
@Component
struct TextTimerExample {
  textTimerController: TextTimerController = new TextTimerController();
  @State tempLatrue: number = 35;

  build() {
    Column() {
      Slider({
        value: this.tempLatrue,
        min: 34.5,
        max: 43.1,
        style: SliderStyle.OutSet,
        step: 0.1
      })
        .width('100%')
        .margin({ top: 15, bottom: 15 })
        .onChange((value: number) => {
          this.tempLatrue = Number.parseFloat(value.toFixed(3).slice(0, -1));
        }).showTips(true, `${this.tempLatrue}`)
    }
  }
}
```
