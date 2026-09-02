---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-camera-16
title: 视频流支持哪些格式
breadcrumb: FAQ > 媒体开发 > 拍照和图片 > 相机开发（Camera） > 视频流支持哪些格式
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:41+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:fc45c9429df84fd9492c162428effb1266f2e1d7021b19e96f9e9e327ff4b498
---

## 问题现象

视频流除了使用ArrayBuffer和Uint8Array，还可以使用Blob。这些字节数据可以转换为不同格式的图片。

## 解决措施

TS层无其他格式，这些字节数据可以转换为PixelMap，经过编码后可以转换为JPEG、WebP和PNG格式（目前支持这三种）。
