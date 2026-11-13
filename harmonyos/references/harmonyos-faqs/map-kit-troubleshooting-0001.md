---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/map-kit-troubleshooting-0001
title: Map Kit地图加载Marker不展示问题
breadcrumb: FAQ > 应用服务开发 > 地图服务（Map Kit） > 故障排查 > Map Kit地图加载Marker不展示问题
category: harmonyos-faqs
scraped_at: 2026-11-13T09:06:32+08:00
doc_updated_at: 2026-11-12
content_hash: sha256:a40ec25339517b8e315c0dfcbe1ebc4da82c4497cac49ba28828871bef300093
---

## 问题现象

应用加载地图时，有时不展示默认的Marker标记。

## 定位过程

1. 通过日志定位每次地图不展示默认Marker标记时，原因均为调用addMarker时，地图还未初始化完成。
2. 查看代码中调用addMarker相关方法的时间点，是在aboutToAppear()中同时调用了地图初始化和添加默认Marker的方法，导致存在地图未初始化完成时，就调用了添加默认Marker的方法的情况，添加Marker不成功。

## 分析结论

在页面的aboutToAppear()中同时调用了地图初始化和添加默认Marker的方法，导致存在地图未初始化完成时，就调用了添加默认Marker的方法的情况，导致最终添加Marker不成功。

## 修改建议

在初始化地图方法的callback回调中，执行添加默认Marker的方法，保证地图初始化完成后再调用添加默认Marker的方法。正确用法见[添加标记](../doccenter-capabilities/map-marker.md#添加标记)。
