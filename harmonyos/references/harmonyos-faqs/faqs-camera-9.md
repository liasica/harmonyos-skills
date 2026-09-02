---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-camera-9
title: 如何实现相机关闭
breadcrumb: FAQ > 媒体开发 > 拍照和图片 > 相机开发（Camera） > 如何实现相机关闭
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:40+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:e2d6766018430731bcd75e12f744c278ae3ebbbc953a92e86025ce8fb4d103d9
---

实现相机关闭的参考代码如下：

```ts
// Stop the current session
  photoSession.stop();

// Release camera input stream
  cameraInput.close();

// Release preview output stream
  previewOutput.release();

// Release the photo output stream
  photoOutput.release();

// Release session
  photoSession.release();

// Session left blank
  photoSession = undefined;
```

## 参考链接

[拍照实践(ArkTS)](../harmonyos-guides/camera-shooting-case.md)
