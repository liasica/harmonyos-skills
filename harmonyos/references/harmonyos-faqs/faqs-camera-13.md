---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-camera-13
title: 如何开关闪光灯
breadcrumb: FAQ > 媒体开发 > 拍照和图片 > 相机开发（Camera） > 如何开关闪光灯
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:41+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:89ffc98deaae59d1fa2ff120465f3dfe7190cdf2b61d0e26177298c0d1eee8ce
---

使用[isFlashModeSupported](../harmonyos-references/arkts-apis-camera-flashquery.md#isflashmodesupported11)方法检测设备是否支持需要设置的闪光灯模式后，使用[setFlashMode](../harmonyos-references/arkts-apis-camera-flash.md#setflashmode11)设置闪光灯模式。

参考代码：

```ts
setFlash(captureSession: camera.PhotoSession,flashMode: camera.FlashMode) {
  if (captureSession != null) {
    let focusModeStatus: boolean = captureSession?.isFlashModeSupported(flashMode);
    if (focusModeStatus) {
      captureSession.setFlashMode(flashMode);
    }
  }
}
```
