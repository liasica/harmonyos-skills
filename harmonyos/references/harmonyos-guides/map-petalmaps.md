---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/map-petalmaps
title: 通过地图应用实现导航等能力
breadcrumb: 指南 > 应用服务 > Map Kit（地图服务） > 通过地图应用实现导航等能力
category: harmonyos-guides
scraped_at: 2026-04-28T07:49:55+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:bc5267e060a4664c15038a7761c87f0a3c173de433d8bb08dd01b2c351b5b970
---

## 场景介绍

从5.0.3(15)开始，支持地图应用首页、搜索地点、查看地点详情、规划路线和进行导航功能；从6.0.1(21)开始，支持地图应用发起打车功能。

本章节将向您介绍如何打开地图应用实现如下能力：

* 打开地图应用首页
* 打开地图应用搜索地点
* 打开地图应用查看地点详情
* 打开地图应用规划路线
* 打开地图应用进行导航
* 打开地图应用发起打车

## 接口说明

调用地图应用的功能主要通过[petalMaps](../harmonyos-references/map-petal-maps.md)命名空间下的[openMapHomePage](../harmonyos-references/map-petal-maps.md#openmaphomepage)、[openMapTextSearch](../harmonyos-references/map-petal-maps.md#openmaptextsearch)、[openMapPoiDetail](../harmonyos-references/map-petal-maps.md#openmappoidetail)、[openMapRoutePlan](../harmonyos-references/map-petal-maps.md#openmaprouteplan)、[openMapNavi](../harmonyos-references/map-petal-maps.md#openmapnavi)、[openMapTaxi](../harmonyos-references/map-petal-maps.md#openmaptaxi)等接口实现，更多接口及使用方法请参见[接口文档](../harmonyos-references/map-petal-maps.md)。

| 接口说明 | 描述 |
| --- | --- |
| [TextSearchParams](../harmonyos-references/map-petal-maps.md#textsearchparams) | 文本搜索的参数。 |
| [PoiDetailParams](../harmonyos-references/map-petal-maps.md#poidetailparams) | POI详情的参数。 |
| [RoutePlanParams](../harmonyos-references/map-petal-maps.md#routeplanparams) | 路线规划的参数。 |
| [NaviParams](../harmonyos-references/map-petal-maps.md#naviparams) | 导航的参数。 |
| [TaxiParams](../harmonyos-references/map-petal-maps.md#taxiparams) | 打车的参数。 |
| [openMapHomePage](../harmonyos-references/map-petal-maps.md#openmaphomepage)(context: [common.Context](../harmonyos-references/js-apis-inner-application-context.md)): Promise<void> | 打开地图应用首页。 |
| [openMapTextSearch](../harmonyos-references/map-petal-maps.md#openmaptextsearch)(context: [common.Context](../harmonyos-references/js-apis-inner-application-context.md), textSearchParams: [TextSearchParams](../harmonyos-references/map-petal-maps.md#textsearchparams)): Promise<void> | 打开地图应用搜索地点。 |
| [openMapPoiDetail](../harmonyos-references/map-petal-maps.md#openmappoidetail)(context: [common.Context](../harmonyos-references/js-apis-inner-application-context.md), poiDetailParams: [PoiDetailParams](../harmonyos-references/map-petal-maps.md#poidetailparams)): Promise<void> | 打开地图应用查看地点详情。 |
| [openMapRoutePlan](../harmonyos-references/map-petal-maps.md#openmaprouteplan)(context: [common.Context](../harmonyos-references/js-apis-inner-application-context.md), routePlanParams: [RoutePlanParams](../harmonyos-references/map-petal-maps.md#routeplanparams)): Promise<void> | 打开地图应用规划路线。 |
| [openMapNavi](../harmonyos-references/map-petal-maps.md#openmapnavi)(context: [common.Context](../harmonyos-references/js-apis-inner-application-context.md), naviParams: [NaviParams](../harmonyos-references/map-petal-maps.md#naviparams)): Promise<void> | 打开地图应用进行导航。 |
| [openMapTaxi](../harmonyos-references/map-petal-maps.md#openmaptaxi)(context: [common.Context](../harmonyos-references/js-apis-inner-application-context.md), taxiParams: [TaxiParams](../harmonyos-references/map-petal-maps.md#taxiparams)): Promise<void> | 打开地图应用打车页面。 |

## 地图应用使用的坐标类型

在国内站点，中国大陆使用GCJ02坐标系，中国台湾使用WGS84坐标系。

在海外站点，统一使用WGS84坐标系。坐标系转换参考：[坐标纠偏](map-convert-coordinate.md)。

## 开发步骤

导入相关模块

```
1. import { petalMaps } from '@kit.MapKit'
```

### 打开地图应用首页

通过[openMapHomePage](../harmonyos-references/map-petal-maps.md#openmaphomepage)，打开地图应用首页。

```
1. try {
2. await petalMaps.openMapHomePage(this.getUIContext().getHostContext());
3. } catch (e) {
4. console.error(`code:${e.code}, message:${e.message}`);
5. }
```

**图1** 打开地图应用首页

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/Tu36bt00RTSWBfvhy5FXzg/zh-cn_image_0000002552799402.jpg?HW-CC-KV=V1&HW-CC-Date=20260427T234954Z&HW-CC-Expire=86400&HW-CC-Sign=FE05AA06EF9FA78A364BEF2347D6635223F874F7558AAE076A4EEDA6B0F06948 "点击放大")

### 打开地图应用进行地点搜索

通过[openMapTextSearch](../harmonyos-references/map-petal-maps.md#openmaptextsearch)，传入搜索目标名称，打开地图应用进行地点搜索。

```
1. try {
2. let params: petalMaps.TextSearchParams = {
3. destinationName: '云谷'
4. };
5. await petalMaps.openMapTextSearch(this.getUIContext().getHostContext(), params);
6. } catch (e) {
7. console.error(`code:${e.code}, message:${e.message}`);
8. }
```

**图2** 打开地图应用进行地点搜索

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/caJNoDkDTs-8EdLQkLFy9A/zh-cn_image_0000002583439097.jpg?HW-CC-KV=V1&HW-CC-Date=20260427T234954Z&HW-CC-Expire=86400&HW-CC-Sign=5465F81F362F238CF7F1DD123CF63141D14C3B77B5D8121898B5F77351B5B752 "点击放大")

### 打开地图应用查看地点详情

通过[openMapPoiDetail](../harmonyos-references/map-petal-maps.md#openmappoidetail)，传入地点的经纬度，打开地图应用查看地点详情。

```
1. try {
2. let params: petalMaps.PoiDetailParams = {
3. destinationPosition: {
4. latitude: 32.02065982629459,
5. longitude: 118.788899213002
6. },
7. destinationPoiId: '563233191438217472'
8. };
9. await petalMaps.openMapPoiDetail(this.getUIContext().getHostContext(), params);
10. } catch (e) {
11. console.error(`code:${e.code}, message:${e.message}`);
12. }
```

**图3** 打开地图应用查看地点详情

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/e__lx-bsRsSU2scPmFVRDw/zh-cn_image_0000002552959052.jpg?HW-CC-KV=V1&HW-CC-Date=20260427T234954Z&HW-CC-Expire=86400&HW-CC-Sign=795AC63F01E4AD63F3CB9A0D805225BD2E384D5C17722FE48FA9326AECE0BB50 "点击放大")

### 打开地图应用规划路线

通过[openMapRoutePlan](../harmonyos-references/map-petal-maps.md#openmaprouteplan)，传入终点经纬度，打开地图应用规划路线。

```
1. try {
2. let params: petalMaps.RoutePlanParams = {
3. destinationPosition: {
4. latitude: 31.983015468224288,
5. longitude: 118.78058590757131
6. }
7. };
8. await petalMaps.openMapRoutePlan(this.getUIContext().getHostContext(), params);
9. } catch (e) {
10. console.error(`code:${e.code}, message:${e.message}`);
11. }
```

**图4** 打开地图应用规划路线

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/_MbkdbswQI-CH16pEduM1A/zh-cn_image_0000002583479053.jpg?HW-CC-KV=V1&HW-CC-Date=20260427T234954Z&HW-CC-Expire=86400&HW-CC-Sign=E9C0A00F2CC5DBD36FA2CEB7E56079324061288E9334F840FCBAEA7002BA5952 "点击放大")

### 打开地图应用进行导航

通过[openMapNavi](../harmonyos-references/map-petal-maps.md#openmapnavi)，传入终点经纬度，打开地图应用发起导航。

```
1. try {
2. let params: petalMaps.NaviParams = {
3. destinationPosition: {
4. latitude: 31.983015468224288,
5. longitude: 118.78058590757131
6. }
7. };
8. await petalMaps.openMapNavi(this.getUIContext().getHostContext(), params);
9. } catch (e) {
10. console.error(`code:${e.code}, message:${e.message}`);
11. }
```

**图5** 打开地图应用进行导航

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1f/v3/BishgdOXTb-_up3AzZkLTg/zh-cn_image_0000002552799404.jpg?HW-CC-KV=V1&HW-CC-Date=20260427T234954Z&HW-CC-Expire=86400&HW-CC-Sign=0A2C38B2992D7A7614E1616D48C714F943EA296A518627D4F4E2632334131851 "点击放大")

### 打开地图应用打车页面

通过[openMapTaxi](../harmonyos-references/map-petal-maps.md#openmaptaxi)，传入终点经纬度，打开地图应用发起打车。

```
1. try {
2. let params: petalMaps.TaxiParams = {
3. destinationPosition: {
4. latitude: 31.983015468224288,
5. longitude: 118.78058590757131
6. }
7. };
8. await petalMaps.openMapTaxi(this.getUIContext().getHostContext(), params);
9. } catch (e) {
10. console.error(`code:${e.code}, message:${e.message}`);
11. }
```

**图6** 打开地图应用进行打车

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/BRIqfZ_ERiqJHwaSMTFcSg/zh-cn_image_0000002583439099.jpg?HW-CC-KV=V1&HW-CC-Date=20260427T234954Z&HW-CC-Expire=86400&HW-CC-Sign=A8A8F48258B76E0254EC89D40A308980407A1E28B05C1584B0DC1C435AC2285C "点击放大")
