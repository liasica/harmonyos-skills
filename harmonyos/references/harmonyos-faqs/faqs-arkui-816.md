---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-816
title: Text组件如何分布在Stack组件的四个角
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > Text组件如何分布在Stack组件的四个角
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:20+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:d1601d7d1f8e3c6983ca1d7acd84d702af5e7f5ede48a83e4778534b71665b89
---

## 问题现象

Stack组件中有四个Text组件，如何使子组件分别分布在Stack组件的左上角，右上角，左下角，右下角？

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/3kCfrW2LShGLORetb4SYfQ/zh-cn_image_0000002628557804.png "点击放大")

## 背景知识

[justifyContent](../harmonyos-references/ts-container-column.md#justifycontent8)：设置子组件在水平或垂直方向上的对齐格式。

## 解决方案

首先将左上角、右上角的两个Text组件外层嵌套一个Row组件，左下角、右下角的两个Text组件外层嵌套一个Row组件，再将两个Row组件外层嵌套一个Column组件，最后给Row组件和Column组件添加justifyContent属性即可实现。

```ts
@Entry
@Component
struct StackDemo {
  build() {
    Stack({ alignContent: Alignment.TopStart }) {
      Column() {
        Row() {
          Text('左上角')
          Text('右上角')
        }.width('100%')
        .justifyContent(FlexAlign.SpaceBetween) // 设置子组件在水平方向上的对齐格式。

        Row() {
          Text('左下角')
          Text('右下角')
        }
        .width('100%')
        .justifyContent(FlexAlign.SpaceBetween) // 设置子组件在水平方向上的对齐格式。
      }
      .justifyContent(FlexAlign.SpaceBetween) // 设置子组件在垂直方向上的对齐格式。
      .width('100%')
      .height('100%')
    }
  }
}
```
