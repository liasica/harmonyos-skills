---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/map-petalmaps
title: 通过地图应用实现导航等能力
breadcrumb: 指南 > 应用服务 > Map Kit（地图服务） > 通过地图应用实现导航等能力
category: harmonyos-guides
scraped_at: 2026-04-29T13:39:18+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:58eaae35e2b925294b5c50fbe7c0061e14e4f411b4f7f89def97820d411b64c1
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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1/v3/aU5Txby2Sbuh7uZKcTG7HA/zh-cn_image_0000002589325423.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T053721Z&HW-CC-Expire=86400&HW-CC-Sign=A9791BA60D3C43313487AEB833554E017F157B8CF963C70467A99FF93FC3A5DE "点击放大")

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/M3YMu6wkS0SaPKr-4BrZ9w/zh-cn_image_0000002589245361.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T053721Z&HW-CC-Expire=86400&HW-CC-Sign=9CAED17A41E5BE5F57D598F8B372E28A43044A3F58A0110C547D0F0C9A103DE4 "点击放大")

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/LTNOnX6aTriPCl1zxzavbw/zh-cn_image_0000002558765554.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T053721Z&HW-CC-Expire=86400&HW-CC-Sign=B1E5CC2A568A880496B04D8DE02BAC9625754966AEB8D80C68C512EB8D57A98B "点击放大")

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/qT9pxkY_R2WBxkc564C2Zg/zh-cn_image_0000002558605898.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T053721Z&HW-CC-Expire=86400&HW-CC-Sign=67CA74F63C9B82B9DE098A25163F32F40171B0058CA454603E832F73902CBA8E "点击放大")

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/LAZkn1v7QImKxGE3VPbcng/zh-cn_image_0000002589325425.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T053721Z&HW-CC-Expire=86400&HW-CC-Sign=8EA5E36886C15D8C4E19619A6A9D7EC0BADE6C8E4E97C5CCF687EC68360385C1 "点击放大")

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/G0x82PPCSqyACE9g2RxcbA/zh-cn_image_0000002589245363.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T053721Z&HW-CC-Expire=86400&HW-CC-Sign=3A799BA7E66B214AF5D2BA281C4BD934D1172D3FB6D656578CA1E69E866C03C1 "点击放大")
