---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/map-convert-coordinate
title: 坐标纠偏
breadcrumb: 指南 > 应用服务 > Map Kit（地图服务） > 地图计算工具 > 坐标纠偏
category: harmonyos-guides
scraped_at: 2026-04-28T07:49:55+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:db4fd683b760cfd9acdf9480a996a1c913dacb79a3b2ddc922fa5cf1d6e5666c
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

以下是坐标纠偏功能相关接口，主要由[map](../harmonyos-references/map-module-desc.md)命名空间下的[convertCoordinateSync](../harmonyos-references/map-map-convertcoordinatesync.md)、[rectifyCoordinate](../harmonyos-references/map-map-rectifycoordinate.md)方法提供，更多接口及使用方法请参见[接口文档](../harmonyos-references/map-map-convertcoordinatesync.md)。

| 接口名 | 描述 |
| --- | --- |
| [mapCommon.CoordinateType](../harmonyos-references/map-common.md#coordinatetype) | 坐标系类型。 |
| [convertCoordinateSync](../harmonyos-references/map-map-convertcoordinatesync.md)(fromType: [mapCommon.CoordinateType](../harmonyos-references/map-common.md#coordinatetype), toType: [mapCommon.CoordinateType](../harmonyos-references/map-common.md#coordinatetype), location: [mapCommon.LatLng](../harmonyos-references/map-common.md#latlng)): [mapCommon.LatLng](../harmonyos-references/map-common.md#latlng) | 坐标转换，将WGS84坐标系转换为GCJ02坐标系。 |
| [rectifyCoordinate](../harmonyos-references/map-map-rectifycoordinate.md)(context: [common.Context](../harmonyos-references/js-apis-inner-application-context.md), locations: Array<[mapCommon.CoordinateLatLng](../harmonyos-references/map-common.md#coordinatelatlng)>): Promise<Array<[mapCommon.CoordinateLatLng](../harmonyos-references/map-common.md#coordinatelatlng)>> | 坐标纠偏。 |
| [mapCommon.LatLng](../harmonyos-references/map-common.md#latlng) | 经纬度对象。 |

## 开发步骤

导入相关模块。

```
1. import { map, mapCommon } from '@kit.MapKit';
```

### 坐标纠偏

[rectifyCoordinate](../harmonyos-references/map-map-rectifycoordinate.md)接口根据用户输入的坐标系和坐标以及获取当前的路由地，判断是否需要修正坐标。如果需要修正，则返回修正后的坐标系和坐标。

说明

* [rectifyCoordinate](../harmonyos-references/map-map-rectifycoordinate.md)接口仅为解决原始坐标与华为地图展示偏转的问题。
* [rectifyCoordinate](../harmonyos-references/map-map-rectifycoordinate.md)接口仅支持WGS84坐标系转为GCJ02坐标系。

```
1. let locations: Array<mapCommon.CoordinateLatLng> = [
2. {
3. // 输入香港坐标和WGS84坐标系，若当前地图站点使用GCJ02坐标系，返回GCJ02坐标系和转换后的香港坐标（输入的坐标转换为GCJ02坐标系）
4. coordinateType: mapCommon.CoordinateType.WGS84,
5. location: {
6. latitude: 22.280556,
7. longitude: 114.984000
8. }
9. }
10. ];
11. // 包含await的外层方法需要添加async关键字
12. let arr: Array<mapCommon.CoordinateLatLng> = await map.rectifyCoordinate(this.getUIContext().getHostContext(), locations);
```

### 坐标转换

初始化需要转换的坐标，调用[convertCoordinateSync](../harmonyos-references/map-map-convertcoordinatesync.md)方法转换坐标。

```
1. let wgs84Position: mapCommon.LatLng = {
2. latitude: 30,
3. longitude: 118
4. };
5. // 转换经纬度坐标
6. let gcj02Position: mapCommon.LatLng =
7. map.convertCoordinateSync(mapCommon.CoordinateType.WGS84, mapCommon.CoordinateType.GCJ02, wgs84Position);
```
