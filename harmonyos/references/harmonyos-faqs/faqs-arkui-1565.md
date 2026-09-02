---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1565
title: 折叠屏展开态，页面下方按钮显示在视窗外
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 折叠屏展开态，页面下方按钮显示在视窗外
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:15+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:4734602735d5e8f25d2eeb7e909b5f480e36f4f77d882ebc05ca70f2bd35a2fe
---

## 问题现象

折叠屏展开态，部分带图片的页面，下方按钮显示在视窗外，无法点击。

## 背景知识

* [Image](../harmonyos-references/ts-basic-components-image.md)组件的[objectFit](../harmonyos-references/ts-basic-components-image.md#objectfit)属性可设置图片的填充效果。其中[ImageFit](../harmonyos-references/ts-appendix-enums.md#imagefit).Contain为保持宽高比进行缩小或者放大，使得图片或视频完全显示在显示边界内，对齐方式为水平居中，ImageFit.Cover为保持宽高比进行缩小或者放大，使得图片或视频两边都大于或等于显示边界，对齐方式为水平居中。
* [Scroll](../harmonyos-references/ts-container-scroll.md)组件：可滚动的容器组件，当子组件的布局尺寸超过父组件的尺寸时，内容可以滚动。

## 问题定位

1. 查阅页面代码中Image组件的objectFit属性是否为ImageFit.Contain或ImageFit.Cover，使得图片能够保持宽高比缩放。
2. 查阅页面代码中Image组件是否在Scroll容器中。

## 分析结论

页面代码中Image组件的objectFit属性为ImageFit.Contain或ImageFit.Cover，折叠屏展开后，屏幕宽度变大，Image组件的宽度变大，图片的宽度也会变大，在图片宽高比不变的情况下，图片高度也会变大，如果外层没有Scroll组件，就会把下面的按钮挤到屏幕外。

## 修改建议

在页面内容区加层Scroll组件，把Image组件嵌套在里面，保证图片尺寸变大的时候能够上下滑动，避免把下面的组件挤到屏幕外。可参考官方Scroll的基本[使用示例](../harmonyos-references/ts-container-scroll.md#示例1设置scroller控制器)。
