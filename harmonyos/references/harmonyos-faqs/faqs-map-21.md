---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-map-21
title: 地图如何批量添加Marker
breadcrumb: FAQ > 应用服务开发 > 地图服务（Map Kit） > 地图如何批量添加Marker
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:47+08:00
doc_updated_at: 2026-08-12
content_hash: sha256:defd1219e1618454eb165f7337b2e195552af290fc534a129c07b9ca619a1e4c
---

## 问题现象

在某些场景，需要在地图上同时标记大量相同属性、目的的Marker点位，此时采用依次绘制所有Marker的方式会导致绘制时间长、代码量大的情况。如何在地图上批量绘制海量Marker？

## 背景知识

* [海量点图层](../harmonyos-guides/map-mass-point.md)：用于批量展示坐标点数据。海量点图层支持处理的点数量级跨度较大，从几十个点至十万个点都可以应用海量点图层进行处理。
* Promise.all：Promise.all是JavaScript中处理并发异步任务的方法。

## 解决方案

* 方案一：如果添加的Marker图标相同，通过[addMassPointOverlay](../harmonyos-references/map-map-mapcomponentcontroller.md#addmasspointoverlay)接口一次性添加海量点图层。
* 方案二：如果添加的Marker图标不同，可以采用Promise.all并发执行[addMarker](../harmonyos-references/map-map-mapcomponentcontroller.md#addmarker)。但此种方法，在同步执行较多添加Marker操作时，可能导致性能压力较大。建议将待添加的Marker点分批，每批Marker点采用Promise.all并发执行添加操作。
