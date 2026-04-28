---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/map-introduction
title: Map Kit简介
breadcrumb: 指南 > 应用服务 > Map Kit（地图服务） > Map Kit简介
category: harmonyos-guides
scraped_at: 2026-04-28T07:49:42+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:e890018ba44bc75a436545c77bed7d47b9b6bfbe5275d2e3fb614eec22783b73
---

Map Kit（地图服务）为开发者提供强大而便捷的地图能力，助力全球开发者实现个性化显示地图、位置搜索和路径规划等功能，轻松完成地图构建工作。您可以轻松地在HarmonyOS应用/元服务中集成地图相关的功能，全方位提升用户体验。

Map Kit提供了全球3.2亿的 POI（Point of Interest，兴趣点）。在地图表达中，一个 POI可代表一家商铺、一栋办公楼、一处景点等等。

Map Kit不断优化丰富地图的细节呈现能力，例如在POI和路网信息展示方面，根据POI属性信息及区域路网差异，在不同层级比例尺条件下，为用户展示更合适的POI和路网信息。手势交互方面，提供了包括缩放、旋转、移动、倾斜等流畅的交互体验。

## 场景介绍

中国大陆使用GCJ02坐标系，中国台湾和海外使用WGS84坐标系。详见[坐标纠偏](map-convert-coordinate.md)。

Map Kit提供以下功能，满足绝大多数地图开发的需求：

* [创建地图](map-presenting.md)：创建地图组件、设置地图属性、自定义地图等。
* [地图交互](map-controls-and-interaction.md)：控制地图的交互手势和交互按钮。
* [在地图上绘制](map-marker.md)：添加位置标记、覆盖物以及各种形状等。
* [位置搜索](map-site-search.md)：多种查询POI信息的能力，提供正地理编码、逆地理编码的能力。
* [路径规划](map-navi-routes.md)：提供驾车、步行、骑行路径规划能力。
* [静态图](map-static-diagram.md)：获取一张地图图片。
* [地图Picker](map-location-details.md)：提供地点详情展示控件、地点选取控件、区划选择控件。
* [通过地图应用实现导航等能力](map-petalmaps.md)：查看位置详情、查看路径规划、发起导航、发起内容搜索。
* [地图计算工具](map-convert-coordinate.md)：华为地图涉及的2种坐标系及其使用区域和转换。

## 约束和限制

### 支持的国家/地区

请参见[支持的国家/地区](map-supported.md)。

### 支持的设备

本kit仅适用于Phone、Tablet、PC/2in1和Wearable。

### 示例代码

Map Kit（地图服务）示例代码，请参考[示例代码](https://gitcode.com/HarmonyOS_Samples/map-kit_-sample-code_-demo-arkts)。

## 模拟器支持情况

* 通用差异：请参见“[模拟器与真机的差异](ide-emulator-specification.md#section1227613205203)”。
* ARM模拟器：petalMaps命名空间下相关功能不支持，我的位置功能不支持。
* x86模拟器：petalMaps命名空间下相关功能不支持，我的位置功能不支持，手表不支持。
