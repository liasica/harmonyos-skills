---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-tablet-26
title: 平板打开应用，部分组件不可见
breadcrumb: FAQ > 多设备场景 > 平板 > 常见问题 > 平板打开应用，部分组件不可见
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:48+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:e970756e8ab7aaf46c92432758b60d06ae94f355a3ade81b5b11914342697ff9
---

## 问题现象

对比手机，平板打开相同应用，因应用未适配多端设备，导致部分组件不可见。

## 背景知识

[自适应布局](../best-practices/bpta-multi-device-adaptive-layout.md)：可采用自适应拉伸、自适应缩放、自适应延伸、自适应折行等手段，确保组件能自适应不同屏幕尺寸的设备。

## 问题定位

1. 使用UIView查看平板上的页面布局，可见组件存在，只是挤压到了屏幕之外。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/fa77NhhKSW62OLJb5GeD1A/zh-cn_image_0000002628552236.png "点击放大")
2. 检查页面的相关组件的尺寸属性是否设置成了固定值。

## 分析结论

平板上页面内的组件并没有消失，只是组件的尺寸设置成了固定值，未能适配平板的屏幕尺寸，显示在了屏幕之外。

## 修改建议

可采用自适应布局的方式设置组件尺寸和位置属性，例如此例中可通过自适应缩放中的占比能力保证组件能够正常的显示，例如下面代码。

```ts
@Entry
@Component
struct ViewHidingIssueDemo {
  build() {
    Column() {
      Row() {
        Text('不同意，退出')
          .textAlign(TextAlign.Center)
          .width('50%')
        Divider()
          .vertical(true)
        Text('同意')
          .width('50%')
          .textAlign(TextAlign.Center)
      }
      .width('100%')
      .height('20%')
      .backgroundColor(Color.Gray)
    }
    .justifyContent(FlexAlign.Center)
    .width('100%')
    .height('100%')
  }
}
```
