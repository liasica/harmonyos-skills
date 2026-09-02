---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-map-23
title: MapKit服务中使用TileOverlayOptions访问瓦片地址tileUrl时报错：1007900060
breadcrumb: FAQ > 应用服务开发 > 地图服务（Map Kit） > MapKit服务中使用TileOverlayOptions访问瓦片地址tileUrl时报错：1007900060
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:47+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:a3335e6ca8c8d66509243246bde3999982bde07bfcc730a0992fb972ee8a687f
---

## 问题现象

在MapKit服务中使用TileOverlayOptions访问瓦片地址tileUrl时报错SSL peer certificate or SSH remote key was not OK，code:1007900060请问如何才能正确的设置证书或者在测试阶段绕过证书验证？

## 解决方案

在线下载瓦片图层方法，当前仅支持传出URL，不支持配置RCP策略，默认使用系统CA配置。

如果需要自行配置RCP策略，可以使用[本地加载](../harmonyos-guides/map-tile.md#本地加载)瓦片图层方法，需要您在指导中的tileProviderMethod方法中自行实现配置定制化RCP策略访问URL，下载瓦片并加载。
