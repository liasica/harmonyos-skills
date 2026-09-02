---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/map-convert-coordinate
title: 坐标纠偏
breadcrumb: 指南 > 应用服务 > Map Kit（地图服务） > 地图计算工具 > 坐标纠偏
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:58+08:00
doc_updated_at: 2026-05-18
content_hash: sha256:728f3ee555fb8e4a15d76c7c7a40ff9645e76fb255a39ff2bc66ec3850a98552
---

## 坐标系知识介绍

华为地图涉及2种坐标系：

* WGS84：一种大地坐标系，也是目前广泛使用的GPS全球卫星定位系统使用的坐标系。
* GCJ02：由中国国家测绘局制定的地理信息系统的坐标系统，是由WGS84坐标系经过加密后的坐标系。

## 华为地图使用的坐标类型

中国大陆使用GCJ02坐标系，中国台湾和海外使用WGS84坐标系。

## 场景介绍

华为地图在中国大陆使用GCJ02坐标系，若使用WGS84坐标系直接叠加在华为地图上，因坐标值不同，展示位置会有偏移。所以，在中国大陆如果使用WGS84坐标调用Map Kit服务，需要先将其转换为GCJ02坐标系再访问。

## 接口说明

以下是坐标纠偏功能相关接口，主要由[map](../harmonyos-references/map-module-desc.md)命名空间下的[convertCoordinateSync](../harmonyos-references/map-map-functions.md#convertcoordinatesync)、[rectifyCoordinate](../harmonyos-references/map-map-functions.md#rectifycoordinate)方法提供，更多接口及使用方法请参见[接口文档](../harmonyos-references/map-map-functions.md#convertcoordinatesync)。

| 接口名 | 描述 |
| --- | --- |
| [mapCommon.CoordinateType](../harmonyos-references/map-common.md#coordinatetype) | 坐标系类型。 |
| [convertCoordinateSync](../harmonyos-references/map-map-functions.md#convertcoordinatesync)(fromType: [mapCommon.CoordinateType](../harmonyos-references/map-common.md#coordinatetype), toType: [mapCommon.CoordinateType](../harmonyos-references/map-common.md#coordinatetype), location: [mapCommon.LatLng](../harmonyos-references/map-common.md#latlng)): [mapCommon.LatLng](../harmonyos-references/map-common.md#latlng) | 坐标转换，将WGS84坐标系转换为GCJ02坐标系。 |
| [rectifyCoordinate](../harmonyos-references/map-map-functions.md#rectifycoordinate)(context: [common.Context](../harmonyos-references/js-apis-inner-application-context.md), locations: Array<[mapCommon.CoordinateLatLng](../harmonyos-references/map-common.md#coordinatelatlng)>): Promise<Array<[mapCommon.CoordinateLatLng](../harmonyos-references/map-common.md#coordinatelatlng)>> | 坐标纠偏。 |
| [mapCommon.LatLng](../harmonyos-references/map-common.md#latlng) | 经纬度对象。 |

## 开发步骤

导入相关模块。

```typescript
import { map, mapCommon } from '@kit.MapKit';
```

### 坐标纠偏

[rectifyCoordinate](../harmonyos-references/map-map-functions.md#rectifycoordinate)接口根据用户输入的坐标系和坐标以及获取当前的路由地，判断是否需要修正坐标。如果需要修正，则返回修正后的坐标系和坐标。

**说明** 

* [rectifyCoordinate](../harmonyos-references/map-map-functions.md#rectifycoordinate)接口仅为解决原始坐标与华为地图展示偏转的问题。
* [rectifyCoordinate](../harmonyos-references/map-map-functions.md#rectifycoordinate)接口仅支持WGS84坐标系转为GCJ02坐标系。

```typescript
let locations: Array<mapCommon.CoordinateLatLng> = [
  {
    // 输入香港坐标和WGS84坐标系，若当前地图站点使用GCJ02坐标系，返回GCJ02坐标系和转换后的香港坐标（输入的坐标转换为GCJ02坐标系）
    coordinateType: mapCommon.CoordinateType.WGS84,
    location: {
      latitude: 22.280556,
      longitude: 114.984000
    }
  }
];
// 包含await的外层方法需要添加async关键字
let arr: Array<mapCommon.CoordinateLatLng> = await map.rectifyCoordinate(this.getUIContext().getHostContext(), locations);
```

### 坐标转换

初始化需要转换的坐标，调用[convertCoordinateSync](../harmonyos-references/map-map-functions.md#convertcoordinatesync)方法转换坐标。

```typescript
let wgs84Position: mapCommon.LatLng = {
  latitude: 30,
  longitude: 118
};
// 转换经纬度坐标
let gcj02Position: mapCommon.LatLng =
  map.convertCoordinateSync(mapCommon.CoordinateType.WGS84, mapCommon.CoordinateType.GCJ02, wgs84Position);
```
