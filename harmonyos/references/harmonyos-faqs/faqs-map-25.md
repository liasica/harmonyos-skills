---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-map-25
title: Map Kit如何实现离线地图能力
breadcrumb: FAQ > 应用服务开发 > 地图服务（Map Kit） > Map Kit如何实现离线地图能力
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:47+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:87cfe7db1764eff1cbd4fd0ab0b05b3170a358ca9a70e2486934b743bc7dedae
---

## 问题现象

应用在使用地图时，可能存在特殊环境无网络情况，Map Kit如何实现离线地图能力。

## 解决方案

HarmonyOS Next从API 20版本开始支持离线地图能力。

1. 手机打开“地图”应用（Petal Maps）,选择“我的”-“离线地图”-“地图资源管理”-“地区列表”，下载“全球基础包”，如果需要更详细的城市地图，可在“地区列表”页面下载指定城市的离线地图。
2. 开发应用时，按照[地图显示](../harmonyos-guides/map-presenting.md#地图显示)章节创建地图。应用运行后，在无网络情况下，自动使用步骤1下载的离线地图。
