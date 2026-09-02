---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1443
title: 如何让一个组件显示在另一个组件上面
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何让一个组件显示在另一个组件上面
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:21+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:a4f8cf0348f3f3e22c13f5757ddbb83f2e59a067577288ca4c2a5a96fc0dde03
---

## 问题现象

两个独立的A、B组件，需要A组件在B组件的上面显示。在不使用Stack的情况下，有什么方案能够实现？

## 背景知识

* [position](../harmonyos-references/ts-universal-attributes-location.md#position)：绝对定位，确定子组件相对父组件内容区的位置。当父容器为Row/Column/Flex时，设置position的子组件不占位。
* [zIndex](../harmonyos-references/ts-universal-attributes-z-order.md#zindex)：设置组件的堆叠顺序，zIndex值越大，显示层级越高，即zIndex值大的组件会覆盖在zIndex值小的组件上方。

## 解决方案

使用position定位属性，将A组件脱离标准流，配合zIndex设置A组件的层级将其展示在上层，实现A组件展示在B组件上层的效果。

示例代码如下：

```ts
@Entry
@Component
struct ZIndexExample {
  build() {
    Column() {
      Button('A组件')
        .width(200)
        .height(50)
        .fontColor(Color.Black)
        .backgroundColor('#d9dadd')
        .position({ x: 90, y: 50 })
        .zIndex(99)
      Column() {
        Text('B组件').padding({top:20});
      }
      .width('90%').height(150).backgroundColor('#f2f3f5').borderRadius(10)
    }
    .width('100%')
  }
}
```

运行效果图如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/NBHUhC_mT3qDJKesOUPHaw/zh-cn_image_0000002628764156.png "点击放大")

## 常见FAQ

Q：默认情况下，不指定组件的zIndex值，默认是多少？

A：默认情况下，组件的zIndex值是0。
