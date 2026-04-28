---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-camera-7
title: 如何保证相机在全屏预览时不变形
breadcrumb: FAQ > 媒体开发 > 拍照和图片 > 相机开发（Camera） > 如何保证相机在全屏预览时不变形
category: harmonyos-faqs
scraped_at: 2026-04-28T08:28:26+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:a92f35e8305404f1c2e9ec0b73f8c5cc96c61e6e5ea3c943c25e739dca40c7cc
---

需要获取手机的宽高比，通过手机屏幕的width/height与支持的预览尺寸的width/height对比，选择最接近的值。预览流与录像输出流的分辨率宽高比应保持一致。例如，示例代码中的宽高比为1920:1080=16:9，因此预览流的分辨率宽高比也应为16:9，可以选择640:360、960:540或1920:1080等分辨率。

**参考链接**

[预览(ArkTS)-相机开发指导](../harmonyos-guides/camera-preview.md)
