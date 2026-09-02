---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-camera-7
title: 如何保证相机在全屏预览时不变形
breadcrumb: FAQ > 媒体开发 > 拍照和图片 > 相机开发（Camera） > 如何保证相机在全屏预览时不变形
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:40+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:217c91b8b307161669b9e8897c51508ceaea8bb3069304ee3689b33e2a8db597
---

需要获取手机的宽高比，通过手机屏幕的width/height与支持的预览尺寸的width/height对比，选择最接近的值。预览流与录像输出流的分辨率宽高比应保持一致。例如，示例代码中的宽高比为1920:1080=16:9，因此预览流的分辨率宽高比也应为16:9，可以选择640:360、960:540或1920:1080等分辨率。

## 参考链接

[预览(ArkTS)-相机开发指导](../harmonyos-guides/camera-preview.md)
