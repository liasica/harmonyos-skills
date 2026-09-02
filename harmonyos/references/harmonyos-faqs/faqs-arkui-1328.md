---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1328
title: 如何对PNG图标进行着色
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何对PNG图标进行着色
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:09+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:0a7f860304a151c496476e035e66587605d974d5298689283bc6ac4020a87726
---

## 问题现象

如何对PNG图标进行着色，仅更改图标内容部分的颜色，空白部分保持不变？

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/GCCDFgw7Tb2KqiSNj1D72A/zh-cn_image_0000002658839133.png "点击放大")

## 背景知识

[colorBlend](../harmonyos-references/ts-universal-attributes-image-effect.md#colorblend18)：为组件添加颜色叠加效果。colorBlend属性会将指定的颜色与图像原始像素进行叠加混合，仅作用于非透明区域。透明区域因alpha通道值为0，不会参与混合计算。

## 解决方案

采用colorBlend属性结合Image组件的声明式语法实现。

```ts
@Entry
@Component
struct Page {
  build() {
    Column({ space: 20 }) {
      Row({ space: 20 }) {
        Text('修改过图标');
        Image($r('app.media.startIcon'))
          .colorBlend(Color.Red)
          .height(50)
          .width(50);
      };

      Row({ space: 20 }) {
        Text('原始的图标');
        Image($r('app.media.startIcon'))
          .height(50)
          .width(50);
      };
    }
    .justifyContent(FlexAlign.Center)
    .height('100%')
    .width('100%');
  }
}
```

## 常见FAQ

Q：使用colorBlend更改颜色，背景由透明变为白色。

A：colorBlend为颜色叠加，不支持仅设置非透明通道颜色，可以采用[colorFilter](../harmonyos-references/ts-basic-components-imagespan.md#colorfilter14)进行替代。
