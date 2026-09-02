---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-map-24
title: Map Kit加载地图时偶现不展示默认Marker标记
breadcrumb: FAQ > 应用服务开发 > 地图服务（Map Kit） > Map Kit加载地图时偶现不展示默认Marker标记
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:47+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:9305f7c1134da6f09a3012157721db5bca59b7fad654814df08c8c3c885103c6
---

## 问题现象

应用加载地图时，有时不展示默认的Marker标记。

## 背景知识

[getEventManager](../harmonyos-references/map-map-mapcomponentcontroller.md#geteventmanager)：返回地图监听事件管理器。

## 问题定位

1. 通过日志定位每次地图不展示默认Marker标记时，原因均为调用addMarker时，地图还未初始化完成。
2. 查看代码中调用addMarker相关方法的时间点，是在aboutToAppear()中同时调用了地图初始化和添加默认Marker的方法，导致存在地图未初始化完成时，就调用了添加默认Marker的方法的情况，添加Marker不成功。

## 分析结论

在页面的aboutToAppear()中同时调用了地图初始化和添加默认Marker的方法，导致存在地图未初始化完成时，就调用了添加默认Marker的方法的情况，导致最终添加Marker不成功。

## 修改建议

在初始化地图方法的callback回调中，执行添加默认Marker的方法，保证地图初始化完成后再调用添加默认Marker的方法。正确用法见[添加标记](../harmonyos-guides/map-marker.md#添加标记)。
