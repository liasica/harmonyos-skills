---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1275
title: Column宽高自适应背景图片大小
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > Column宽高自适应背景图片大小
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:08+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:086a1e47dae817b0ca1baebe3d8f1e3b5eafd816084f4516c6b3dfff85c1afdc
---

## 问题现象

给Column设置一张背景图片，如何做到Column宽高自适应背景图片大小？即图片有多大，Column就有多大。

## 背景知识

* [Column](../harmonyos-references/ts-container-column.md)是一种线性布局组件，容器内子元素按照垂直方向排列。
* [Stack](../harmonyos-references/ts-container-stack.md)是层叠布局组件，提供元素可以重叠的布局。
* Image的[fitOriginalSize](../harmonyos-references/ts-basic-components-image.md#fitoriginalsize)属性用于设置图片的显示尺寸是否跟随图源尺寸。

## 解决方案

1. 在需要设置背景图片的Column中使用层叠布局组件Stack。
2. 在Stack中使用Image作为背景图片，并将Image的fitOriginalSize属性设置为true。

完整示例参考如下：

```ts
@Entry
@Component
struct ColumnLayout {
  build() {
    Column() {
      Column() {
        Stack() {
          Image($r('app.media.startIcon'))
            .fitOriginalSize(true);
        };
      };
    }.height('100%').width('100%');
  }
}
```

在IDE中查看ArkUI Inspector预览：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/YL4_iqcJQ320MoD9IVB1jw/zh-cn_image_0000002658835381.png "点击放大")

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/wA7mN5mUSiqhv9abH1YAHQ/zh-cn_image_0000002628756018.png "点击放大")
