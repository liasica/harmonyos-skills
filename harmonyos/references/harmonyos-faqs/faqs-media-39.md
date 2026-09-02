---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-media-39
title: 系统录屏授权时允许和禁止的回调怎么调用
breadcrumb: FAQ > 媒体开发 > 音频和视频 > 媒体（Media ） > 系统录屏授权时允许和禁止的回调怎么调用
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:45+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:216e3d70a403b6238c2a2cb3af2d805c8291ba4270f323afde35dc2ba3dde455
---

## 问题现象

应用使用AVScreenCapture录屏取码流(C/C++)进行屏幕录制，场景是系统弹出录屏授权时，用户允许后才开始录制的流程，禁止会直接返回。文档中未找到录制授权时，用户允许或禁止的回调方法。

## 背景知识

* [AVScreenCapture](../harmonyos-guides/using-avscreencapture-for-buffer.md)：屏幕录制主要为主屏幕录屏功能，开发者可以调用录屏模块接口，完成屏幕录制，采集设备内、麦克风等的音视频源数据。
* [OH\_AVScreenCapture\_OnStateChange()](../harmonyos-references/capi-native-avscreen-capture-base-h.md#oh_avscreencapture_onstatechange)：录屏状态改变的监听事件。
* [OH\_AVScreenCaptureStateCode](../harmonyos-references/capi-native-avscreen-capture-base-h.md#oh_avscreencapturestatecode)：表示屏幕录制的状态码。

## 解决方案

通过OH\_AVScreenCapture\_OnStateChange接口监听录屏状态的改变，OH\_AVScreenCaptureStateCode状态码为OH\_SCREEN\_CAPTURE\_STATE\_STARTED时，代表用户允许录屏，状态码为OH\_SCREEN\_CAPTURE\_STATE\_CANCELED时，代表用户禁止录屏，[完整代码参考](https://gitee.com/harmonyos_samples/avscreen-capture-screen-record)。
