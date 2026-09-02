---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1386
title: 图片存在拉伸或压缩的现象
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 图片存在拉伸或压缩的现象
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:15+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:761beaaec8fa4ad73810b287fce6a1c975e3eaec85bd404c6e7a4a2a6b7f4b88
---

## 问题现象

应用内的图片在渲染时出现了非预期的拉伸或压缩变形，导致实际显示效果与设计预期不符。

## 背景知识

* [Image](../harmonyos-references/ts-basic-components-image.md#image-1)：通过图片数据源获取图片，用于后续渲染展示。
  + Image组件加载图片失败或图片尺寸为0时，图片组件大小自动为0，不跟随父组件的布局约束。
  + Image组件默认按照居中裁剪，例如组件宽高设置相同，原图长宽不等，此时按照中间区域进行裁剪。
  + Image加载成功且组件不设置宽高时，其显示大小自适应父组件。
* 当图片不保持宽高比增大或者缩小时，图片会出现拉伸现象。可以通过[objectFit](../harmonyos-references/ts-basic-components-image.md#objectfit)属性设置图片的填充效果，常用的填充效果如下：

  | 类型 | 描述 |
  | --- | --- |
  | cover | 保持宽高比进行缩小或者放大，使得图片两边都大于或等于显示边界，居中显示。 |
  | contain | 保持宽高比进行缩小或者放大，使得图片完全显示在显示边界内，居中显示。 |
  | fill | 不保持宽高比进行放大缩小，使得图片填充满显示边界。 |
  | none | 保持原有尺寸进行居中显示。 |

## 解决方案

当objectFit属性设置为ImageFit.Fill时，图片将不保持宽高比进行缩放以填满整个显示区域，这可能导致图片拉伸失真。同时如果Image组件未设置宽高属性，其尺寸将由父容器决定，并自动保持与父容器的宽高比例。

示例代码如下：

```ts
@Entry
@Component
struct Page {
  build() {
    Column() {
      // 本地资源，自行替换
      Image($r('app.media.startIcon'))
        .objectFit(ImageFit.Contain)
        .width('80%')
        .height('80%');
    }
    .height('100%')
    .width('100%')
    .justifyContent(FlexAlign.Center)
    .alignItems(HorizontalAlign.Center);
  }
}
```
