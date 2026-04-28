---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-camera-13
title: 如何开关闪光灯
breadcrumb: FAQ > 媒体开发 > 拍照和图片 > 相机开发（Camera） > 如何开关闪光灯
category: harmonyos-faqs
scraped_at: 2026-04-28T08:28:28+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:2ca1a19ef7bc19b80f70a7d78a12425ab7bc26dd0dcd70d6501e205764ff14a8
---

使用[isFlashModeSupported](../harmonyos-references/arkts-apis-camera-flashquery.md#isflashmodesupported11)方法检测设备是否支持需要设置的闪光灯模式后，使用[setFlashMode](../harmonyos-references/arkts-apis-camera-flash.md#setflashmode11)设置闪光灯模式。

**参考代码**

```
1. setFlash(captureSession: camera.PhotoSession,flashMode: camera.FlashMode) {
2. if (captureSession != null) {
3. let focusModeStatus: boolean = captureSession?.isFlashModeSupported(flashMode);
4. if (focusModeStatus) {
5. captureSession.setFlashMode(flashMode);
6. }
7. }
8. }
```

[SetFlash.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/CameraKit/entry/src/main/ets/pages/SetFlash.ets#L22-L29)
