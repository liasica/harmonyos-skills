---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1038
title: 如何实现只对子组件进行横向裁剪，不进行纵向裁剪
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何实现只对子组件进行横向裁剪，不进行纵向裁剪
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:06+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:7c7f4d1dbe7eae8704bff855ef211133307e9e0976aa8112c56503bd48602426
---

## 问题现象

clip属性会把子组件超出父组件的部分全部裁剪掉，如何实现只裁剪横向溢出的部分，不裁剪纵向溢出的部分？以下图为例，如何裁剪绿色色块超出灰色矩形部分，不裁剪蓝色色块超出灰色矩形的部分？（灰色矩形部分为绿色色块和蓝色色块的父组件区域）

初始效果图如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/yjKXKVdnTcWoGf1GoCMFgg/zh-cn_image_0000002658924721.png "点击放大")

## 背景知识

* [clip](../harmonyos-references/ts-universal-attributes-sharp-clipping.md#clip18)属性会对子组件超出当前组件范围外的区域进行裁剪。无法控制裁剪范围。
* [clipShape](../harmonyos-references/ts-universal-attributes-sharp-clipping.md#clipshape18)会对指定区域进行裁剪，超出指定区域外的部分会被裁剪掉。指定区域在默认情况下左上角与当前组件左上角相同，可通过offset调整位置。

## 解决方案

给灰色矩形区域的父组件添加clipShape属性进行裁剪。RectShape在默认情况下左上角坐标与当前组件左上角坐标对齐，将宽度设为100%，水平方向不进行偏移，即可裁剪超出灰色区域的绿色色块，竖直方向上移10（与蓝色色块的上移高度对齐），即可刚好不裁剪掉蓝色色块。

RectShape示意图如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/bShLAlxSRS6EYVNtbJc9cQ/zh-cn_image_0000002628405516.png "点击放大")

```ts
import { RectShape } from '@kit.ArkUI';

@Entry
@Component
struct ClipShapeDemo {
  build() {
    Column() {
      Column() {
        // 父组件
        Column() {
          Column().height('100%');
          // 希望Text('1')能显示，高度溢出不裁剪
          Text('1')
            .width(36)
            .fontSize(15)
            .backgroundColor('#5291FF')
            .position({
              left: 0,
              top: 0
            })
            .translate({
              x: 0,
              y: -10
            });
          // 希望Text('2')水平溢出部分裁剪掉
          Text('2')
            .width(36)
            .fontSize(15)
            .backgroundColor('#61CFBE')
            .position({
              left: 0,
              top: 0
            })
            .translate({
              x: -10,
              y: 0
            });
        }.width(50)
        .clipShape(new RectShape({ width: '100%', height: 110 }).offset({ x: 0, y: -10 }))
        .backgroundColor('#E5E5EA');
      }.width('100%').height(100);

    }.width('100%').height('100%').justifyContent(FlexAlign.Center);
  }
}
```

实现效果如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/ef7BHWB0SIqYjlW6bHUdBw/zh-cn_image_0000002658804789.png "点击放大")

## 总结

clipShape可以指定裁剪区域，该区域可以自由控制位置、大小，并且可以超出当前组件。
