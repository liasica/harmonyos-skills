---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/camera-rotation-faq
title: 相机预览画面旋转异常问题
breadcrumb: 指南 > 媒体 > Camera Kit（相机服务） > Camera Kit常见问题 > 相机预览画面旋转异常问题
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:17+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:856488bfb97550f4bf915a8ec98c9f881a4397869b6eb1e723ce9f2dfef9b729
---

## 问题现象

应用在打开相机时，出现预览画面旋转异常现象，导致相机无法正常使用。

## 可能原因

相机预览旋转会出现在“会话配置过程中调用预览旋转接口”和“相机窗口发生旋转对预览角度进行修正”两种场景，如果没有在对应场景进行相应的旋转角度调整，则会导致预览画面旋转角度异常。具体原因可能有如下情况：

1. 在会话配置过程中，未适配相机预览旋转接口：[getPreviewRotation](../harmonyos-references/arkts-apis-camera-previewoutput.md#getpreviewrotation12)、[setPreviewRotation](../harmonyos-references/arkts-apis-camera-previewoutput.md#setpreviewrotation12)。
2. 会话配置过程中的时序不正确，即调用相机预览旋转接口前未完成会话[commitConfig](../harmonyos-references/arkts-apis-camera-session.md#commitconfig11)。
3. 相机窗口发生旋转时，未适配相机预览旋转接口。
4. getPreviewRotation、setPreviewRotation接口入参错误。

**问题分析步骤**

步骤一：确认在会话配置commitConfig后，是否有正确调用getPreviewRotation、setPreviewRotation。

步骤二：如果出现以下报错情况，说明在会话配置过程中，调用相机预览旋转接口前未完成会话commitConfig。

相关日志：PreviewOutput GetPreviewOutputRotation error!, session is nullptr|PreviewRotation call failed. error code: 7400201

步骤三：确认是否有监听Display对象变化，感知窗口当前状态。如当前相机窗口发生旋转时，需调用getPreviewRotation、setPreviewRotation对预览流进行角度修正。

步骤四：getPreviewRotation接口入参为当前相机窗口的旋转角度，通过display.getDefaultDisplaySync.rotation获得。setPreviewRotation接口入参中previewRotation为getPreviewRotation接口的输出。isDisplayLocked应与setXComponentSurfaceRotation的设置保持一致。

相关log搜索关键词：GetPreviewRotation|SetPreviewRotation|session is nullptr

## 案例分析

**问题现象**

应用在悬浮窗状态下打开扫一扫功能，在横屏和竖屏切换时，画面多旋转了90度。

**问题分析**

应用在悬浮窗下打开相机时，在会话配置过程中，适配了相机预览旋转接口，冷启动时预览旋转正常，当进行横竖屏旋转时，预览画面会旋转90度。

日志分析原因为：应用未在相机窗口发生旋转时，先调用getPreviewRotation/setPreviewRotation对预览流进行了角度修正。

**问题结论**

应用在相机窗口发生旋转时，没有调用getPreviewRotation、setPreviewRotation对预览流进行角度修正。

**修复建议**

相机窗口发生旋转时，调用getPreviewRotation、setPreviewRotation对预览流进行角度修正。

参考文档：[适配相机旋转角度(ArkTS)](camera-rotation-angle-adaptation.md#预览)。

## 预防措施

预览旋转接口需要在会话配置的过程中使用，建议在会话（session）调用commitConfig接口之后，start接口之前调用。

应用使用相机时，监听Display对象变化，感知窗口当前状态。如当前相机窗口发生旋转时，需对预览流进行角度修正。推荐在会话配置中完成调用预览旋转接口后，直接创建监听。

参考文档：[适配相机旋转角度(ArkTS)](camera-rotation-angle-adaptation.md#预览)。
