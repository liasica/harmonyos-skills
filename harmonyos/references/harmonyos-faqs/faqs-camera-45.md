---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-camera-45
title: 打开相机进行拍照时，拍照预览区域尺寸异常
breadcrumb: FAQ > 媒体开发 > 拍照和图片 > 相机开发（Camera） > 打开相机进行拍照时，拍照预览区域尺寸异常
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:41+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:d6a07ad86e87a9e3f31224f4ae1c1c7cef2fe60f248d6548ead4d8cadc9d73f8
---

## 问题现象

使用XComponent渲染组件搭配Camera接口实现拍照功能时，页面拍照区域显示过小。

## 背景知识

* [Camera Kit(相机服务)](../harmonyos-guides/camera-overview.md)：本模块为开发者提供了一套简单易懂的相机服务接口。通过调用这些接口，开发者可以开发相机应用，访问和操作相机硬件，实现基础功能如预览、拍照和录像。此外，还可以通过接口组合完成更多操作，如控制闪光灯、曝光时间和对焦等。
* [XComponent(渲染组件)](../harmonyos-references/ts-basic-components-xcomponent.md)：提供用于图形绘制和媒体数据写入的Surface，XComponent负责将其嵌入到视图中，支持应用自定义Surface位置和大小。具体自定义指南可以参考[自定义渲染(XComponent)文档](../harmonyos-guides/napi-xcomponent-guidelines.md)。
* [display.getDefaultDisplaySync](../harmonyos-references/js-apis-display.md#displaygetdefaultdisplaysync9)：获取当前默认的display屏幕属性对象。其中包含了显示设备的屏幕宽高。

## 问题定位

1. 通过DevEco Studio自带的布局分析能力[ArkUI Inspector](../harmonyos-guides/ide-arkui-inspector.md)查看页面布局，可见页面通过XComponent组件渲染。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/BA-RyqbqQoaSPJ795Gz-Zw/zh-cn_image_0000002628392586.png "点击放大")
2. 由于现象是拍照区域大小异常，查询XComponent官方文档中跟大小，宽高，显示区域相关的API，发现通用属性中Width和Height属性以及setXComponentSurfaceRect方法都会影响XComponent的渲染显示区域。
3. 因此建议检查代码中XComponent的宽高属性及setXComponentSurfaceRect方法中surfaceWidth和surfaceHeight的值设置的是否与设备屏幕宽高一致，如果这些值设置不一致，则会导致拍摄显示区域出现尺寸异常的现象。

## 分析结论

1. 预览区域小是因为XComponent渲染组件的宽高的值设置未铺满屏幕，导致预览区域偏小。
2. 预览区域取景内容看起来视角小是因为Surface宽高设置大于XComponent组件宽高，导致只显示了正常预览内容的一部分。

## 修改建议

1. display.getDefaultDisplaySync获取当前显示设备的屏幕宽高。
2. 一般来说，不需要特意调整Surface宽高，因为默认使用XComponent宽高。但有一种特殊情况：当XComponent的宽高比例与预览分辨率的宽高比例差异较大时可能会导致预览画面压缩或拉伸，此场景可以通过setXComponentSurfaceRect接口设置Surface宽高使其与预览分辨率的宽高比例保持一致，防止预览变形。

完整示例可参考官方案例：[拍照比例自定义](../architecture-guides/ratio_camera-0000002252528422.md)。
