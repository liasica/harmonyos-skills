---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1156
title: Image组件按照宽度进行填充加载时高度裁剪问题
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > Image组件按照宽度进行填充加载时高度裁剪问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:06+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:d03b73776101cc784806f4e40b92222c3a604bce5c18383ff5fbbba5406988d8
---

## 问题现象

在指定Image容器的高度的情况下，将图片按照宽度进行填充加载，并且需要图片从上到下展示，对高度超出部分进行裁剪，如何实现？

不作处理时的代码如下：

```ts
@Entry
@Component
struct DisplayTest1 {
  build() {
    Column({ space: 20 }) {
      Row() {
        Image($r('app.media.startIcon'))
          .objectFit(ImageFit.None);
      }
      .width('100%')
      .height(200) // 需要设置的图片高度
      .backgroundColor('#ECA724');
    }
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.Center);
  }
}
```

预览效果图如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/jYGRnkoiTBK3QxFPL0wF7w/zh-cn_image_0000002628569614.png "点击放大")

## 背景知识

* 关于图片的填充加载，可以使用[Image](../harmonyos-references/ts-basic-components-image.md)组件的[objectFit](../harmonyos-references/ts-basic-components-image.md#objectfit)属性，此属性可以设置图片的填充效果。objectFit属性的参数类型为ImageFit，所有图片的填充效果见[ImageFit](../harmonyos-references/ts-appendix-enums.md#imagefit)参考文档。
* [Scroll](../harmonyos-references/ts-container-scroll.md)组件为可滚动的容器组件，当子组件的布局尺寸超过父组件的尺寸时，内容可以滚动。

## 解决方案

目前没有哪一种ImageFit可以直接实现该效果，因此需要先设置Image的填充方式，再对溢出容器部分进行裁剪处理。

1. 首先将Image填充加载，把objectFit属性改为.objectFit(ImageFit.Cover)。

   此时预览效果图如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/L5T8pKIoQ4GNI4jMYSzttQ/zh-cn_image_0000002628409714.png "点击放大")

2. 然后对超出Row容器的部分进行裁剪，满足图片从上到下展示。此时可以使用Scroll容器替代Row容器，因为Scroll容器默认是对元素进行从上往下滚动，再将Scroll的滚动条隐藏，并设置不可滚动就能实现效果。

   修改后的示例代码如下：

   ```ts
   @Entry
   @Component
   struct DisplayTest2 {
     build() {
       Column({ space: 20 }) {
         Scroll() {
           Image($r('app.media.startIcon'))
             .objectFit(ImageFit.Cover);
         }
         .width('100%')
         .height(200) // 需要设置的图片高度
         .scrollBar(BarState.Off) // 滚动条常驻显示
         .enabled(false) // 禁用滑动
         .backgroundColor('#ECA724');
       }
       .width('100%')
       .height('100%')
       .justifyContent(FlexAlign.Center);
     }
   }
   ```

   预览效果图如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/IQtK6HCGToSHEflb1ILC5A/zh-cn_image_0000002658928935.png "点击放大")

   此时的效果已满足该场景要求。
