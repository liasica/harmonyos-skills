---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-map-30
title: 使用地图服务展示自定义信息窗时，返回上一页面产生崩溃如何解决
breadcrumb: FAQ > 应用服务开发 > 地图服务（Map Kit） > 使用地图服务展示自定义信息窗时，返回上一页面产生崩溃如何解决
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:47+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:e4aa2c383cc7b71eec2c6325eaa237072459e6d7197cfa155540cc38f1166cdf
---

## 问题现象

页面展示地图服务自定义信息窗时（如下图的点击店铺显示自定义图标），返回上一页面，产生崩溃。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/QA0yplS_QZWs5QiPQv_J9A/zh-cn_image_0000002658913581.png "点击放大")

## 背景知识

* [Marker](../harmonyos-references/map-map-marker.md)：地图服务中的标记，继承BaseOverlay。在调用map.MapComponentController类的addMarker方法时会返回该类型的实例。
* [getSnippet](../harmonyos-references/map-map-marker.md#getsnippet)：返回信息窗的子标题。

## 问题定位

1. 查看崩溃日志，报错“Unexpected Text in JSON: Empty Text”。查看具体报错的代码行内容为let XXX = JSON.parse(data) as object，判断是data为空导致崩溃。
2. 查看工程代码中data的来源为marker?.getSnippet()，即关闭页面时marker?.getSnippet()的值为空。
3. 确认在页面关闭时，地图服务会清除Marker，导致marker?.getSnippet()为空。

## 分析结论

使用地图服务的自定义信息窗能力时，使用marker?.getSnippet()获取信息窗标题，在页面退出时，地图服务会清除掉页面所有的覆盖物，包括Marker，此时marker?.getSnippet()获取的值为空字符串，使用JSON.parse转换marker?.getSnippet()获取的空字符串，会产生崩溃。

## 修改建议

使用try/catch方式对JSON.parse(data)进行异常防护，避免data为空值时产生崩溃。
