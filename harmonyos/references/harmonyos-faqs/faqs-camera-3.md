---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-camera-3
title: 如何设置相机焦距
breadcrumb: FAQ > 媒体开发 > 拍照和图片 > 相机开发（Camera） > 如何设置相机焦距
category: harmonyos-faqs
scraped_at: 2026-04-28T08:28:26+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:215d0207ef0aa691b1c30d759de563ede60d9a7bd4c1857dd6888087455449bf
---

1. 判断当前摄像头是否为前置摄像头。前置摄像头不支持设置焦距。
2. 通过getZoomRatioRange接口获取设备焦距设置的最大和最小范围。
3. 判断目标焦距参数是否在步骤二获取的范围内，然后通过setZoomRatio接口设置相机焦距。

**参考链接**

[getZoomRatioRange](../harmonyos-references/arkts-apis-camera-zoomquery.md#getzoomratiorange11)、[setZoomRatio](../harmonyos-references/arkts-apis-camera-zoom.md#setzoomratio11)
