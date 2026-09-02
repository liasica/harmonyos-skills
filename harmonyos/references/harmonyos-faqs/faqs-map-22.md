---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-map-22
title: 为什么fromScreenLocation接口和getVisibleRegion接口获取的矩形顶点坐标不一致
breadcrumb: FAQ > 应用服务开发 > 地图服务（Map Kit） > 为什么fromScreenLocation接口和getVisibleRegion接口获取的矩形顶点坐标不一致
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:47+08:00
doc_updated_at: 2026-08-12
content_hash: sha256:45b2ac1a17ac0277c7b1ec7409b74c30eba79f47b655c2b3b3cc7620406314c4
---

## 问题现象

通过fromScreenLocation接口获取的屏幕中地图边界坐标经纬度和getVisibleRegion接口获取的可视区域的坐标经纬度不一致。

## 解决方案

[fromScreenLocation](../harmonyos-references/map-map-projection.md#fromscreenlocation)接口获取的是屏幕中展示的完整地图的矩形四个角所在位置坐标。

[getVisibleRegion](../harmonyos-references/map-map-projection.md#getvisibleregion)接口获取的是地图相机的矩形可视区域坐标，可视区域不包括padding边界。

所以当相机设置了padding边界时，fromScreenLocation接口和getVisibleRegion接口获取矩形区域四个顶点坐标会不一致。
