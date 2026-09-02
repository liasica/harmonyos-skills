---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/scan-faq-18
title: 自定义界面扫码同时调用本地图片识码时，应用概率性自动退出
breadcrumb: 指南 > 媒体 > Scan Kit（统一扫码服务） > Scan Kit常见问题 > 自定义界面扫码同时调用本地图片识码时，应用概率性自动退出
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:19+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:0695862b0d7d0a8218d27705ff1998b53d43a313cbd810384708f031e2850bcd
---

**问题现象**

自定义界面扫码，点击图库，选中图片进行本地图片识码时，应用概率性的自动退出。

**解决措施**

自定义界面扫码接口和识别本地图片接口不支持并发执行。

点击图库按钮的时候，需要先暂停并释放相机流（[stop](../harmonyos-references/scan-customscan-api.md#stop)、[release](../harmonyos-references/scan-customscan-api.md#release)），再进行本地图片识码。
