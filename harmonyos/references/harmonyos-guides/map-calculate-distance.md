---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/map-calculate-distance
title: 距离计算
breadcrumb: 指南 > 应用服务 > Map Kit（地图服务） > 地图计算工具 > 距离计算
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:29+08:00
doc_updated_at: 2026-05-18
content_hash: sha256:0e9bef8258b747ee39703747eba7ce13a01213829b2381927f11168b0d6d407c
---

## 场景介绍

根据用户指定的两个经纬度坐标点，计算这两个点间的直线距离，单位为米。

## 接口说明

以下是距离计算功能相关接口，主要由[map](../harmonyos-references/map-module-desc.md)命名空间下的[calculateDistance](../harmonyos-references/map-map-functions.md#calculatedistance)方法提供，更多接口及使用方法请参见[接口文档](../harmonyos-references/map-map-functions.md#calculatedistance)。

| 接口名 | 描述 |
| --- | --- |
| [mapCommon.LatLng](../harmonyos-references/map-common.md#latlng) | 经纬度对象。 |
| [calculateDistance](../harmonyos-references/map-map-functions.md#calculatedistance)(from: [mapCommon.LatLng](../harmonyos-references/map-common.md#latlng), to: [mapCommon.LatLng](../harmonyos-references/map-common.md#latlng)): number | 计算坐标点之间的距离。 |

## 开发步骤

1. 导入相关模块。

   ```typescript
   import { map, mapCommon } from '@kit.MapKit';
   ```
2. 初始化需要计算的坐标，调用[calculateDistance](../harmonyos-references/map-map-functions.md#calculatedistance)方法计算距离。

   ```typescript
   let fromLatLng: mapCommon.LatLng = {
     latitude: 38,
     longitude: 118
   };
   let toLatLng: mapCommon.LatLng = {
     latitude: 39,
     longitude: 119
   };
   // 计算坐标点之间的距离
   let distance = map.calculateDistance(fromLatLng, toLatLng);
   ```
