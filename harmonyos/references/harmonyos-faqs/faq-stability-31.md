---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faq-stability-31
title: 点击拍照按钮后，页面上所有按钮点击无效
breadcrumb: FAQ > 应用质量 > 技术质量 > 稳定性 > 点击拍照按钮后，页面上所有按钮点击无效
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:49+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:4276443055cbbb065fca85b8e75fa08532e281cf74e3c8a70f154c87bde8183d
---

## 问题现象

点击拍照按钮后，再点击页面上的其他内容，均无响应。

## 背景知识

* [Camera Kit简介](../harmonyos-guides/camera-overview.md)：开发者通过调用Camera Kit(相机服务)提供的接口可以开发相机应用，应用通过访问和操作相机硬件，实现基础操作，如预览、拍照和录像；还可以通过接口组合完成更多操作，如控制闪光灯和曝光时间、对焦或调焦等。
* [on('photoAvailable')](../harmonyos-references/arkts-apis-camera-photooutput.md#onphotoavailable11)：注册监听全质量图上报。使用callback异步回调。
* [弹出框概述](../harmonyos-guides/arkts-base-dialog-overview.md)：弹出框是一种模态窗口，通常用于在保持当前上下文环境的同时，临时展示用户需关注的信息或待处理的操作。

## 问题定位

1. 在hilog日志中搜索关键字Click accepted，在06:47:02.067点击了拍照按钮。

   ```screen
   05-22 06:47:02.067 51708 51708 I C03945/com.hx.example/AceStateStyle: [(100000:100000:scope)] Find customNode by self: CameraPage
   05-22 06:47:02.067 51708 51708 I C0391E/com.hx.example/AceGesture: [(100000:100000:scope)] Click try accept
   05-22 06:47:02.067  1054 50298 I C02BA5/CameraDaemon/PackageAckExcuter: T:8 OnRequestAck<133>: cameraId0(202) reqType(1-) targetMap(0x8604000) status(0) ts(113312041453us)
   05-22 06:47:02.067 51708 51708 I C03951/com.hx.example/InputKeyFlow: [(100000:100000:scope)] Click accepted, tag: Text
   ```
2. 搜索关键字touch test，在点击拍照按钮之后，后续的点击事件被Text组件接收。

   ```screen
   05-22 06:47:20.583 51708 51708 I C03951/com.hx.example/InputKeyFlow: [(100000:100000:scope)] InputTracking id:68948, touch test hitted node info: fingerId: 0{ tag: Text, depth: 7 };
   05-22 06:47:20.583 51708 51708 I C03951/com.hx.example/InputKeyFlow: [(100000:100000:scope)] InputTracking id:68948, touch test hitted recognizer type info: recognizer type ClickRecognizer node info: { tag: Text };
   ```
3. 对比正常的日志，点击事件应该被Image组件接收。

   ```screen
   07-10 11:16:10.398   61994-61994   I   [(100000:100000:scope)] InputTracking id:211547, touch test hitted node info: fingerId: 0{ tag: Image, depth: 8 };
   07-10 11:16:10.398   61994-61994   I   [(100000:100000:scope)] InputTracking id:211547, touch test hitted recognizer type info: recognizer type ClickRecognizer node info: { tag: Image };
   ```
4. 在点击拍照按钮后，应用使用了透明的Text组件覆盖在页面上，导致所有按钮点击无效。
5. 搜索关键字photoAvailable，没有相关日志，可以判断拍照还未结束。

## 分析结论

在拍照还未结束时，页面上存在透明的Text组件接收了所有点击事件，导致被覆盖的按钮点击无效。

## 修改建议

使用[自定义弹出框](../harmonyos-guides/arkts-uicontext-custom-dialog.md)代替透明的组件，提示用户正在进行拍照操作，代码可参考其中的[完整示例](../harmonyos-guides/arkts-uicontext-custom-dialog.md#完整示例)。
