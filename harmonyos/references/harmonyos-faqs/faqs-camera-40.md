---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-camera-40
title: 使用折叠屏手机进行相机预览，在展开态时黑屏
breadcrumb: FAQ > 媒体开发 > 拍照和图片 > 相机开发（Camera） > 使用折叠屏手机进行相机预览，在展开态时黑屏
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:41+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:8ea86b65619ce89b2f2c22597fb538dd5adf8cc63c96efa8bc65b1bfcd406f8c
---

## 问题现象

使用折叠屏手机进行自定义相机开发，在折叠态时预览画面正常显示，展开态时则出现黑屏。

## 背景知识

* 相机开发模型为Surface模型，该模型主要通过Surface实现数据交互。在开发相机应用界面时，首先需要通过创建[XComponent](../harmonyos-references/ts-basic-components-xcomponent.md)组件为预览流提供Surface。
* [renderFit](../harmonyos-references/ts-universal-attributes-renderfit.md#renderfit18)设置宽高动画过程中的组件内容填充方式。

## 问题定位

查看XComponent组件的内容填充方式是否设置了RenderFit.RESIZE\_COVER。

## 分析结论

相机预览渲染组件XComponent使用的SURFACE类型，其背景色是黑色，在API version 18之前，其renderFit通用属性仅支持设置为RenderFit.RESIZE\_FILL，应用却设置的RenderFit.RESIZE\_COVER，不符合官网使用要求，导致展开态时黑屏。

## 修改建议

修改相机预览渲染组件XComponent的renderFit属性为RenderFit.RESIZE\_FILL，即可使折叠屏相机在展开态时正常显示预览画面。

## 常见FAQ

Q：如何设置相机预览渲染组件XComponent全屏显示？

A：真机版本升级到API18及以上版本，设置属性renderFit(RenderFit.RESIZE\_COVER)，请参考文档：[组件内容填充方式](../harmonyos-references/ts-universal-attributes-renderfit.md#renderfit18)。
