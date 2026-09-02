---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/map-petalmaps
title: 通过地图应用实现导航等能力
breadcrumb: 指南 > 应用服务 > Map Kit（地图服务） > 通过地图应用实现导航等能力
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:58+08:00
doc_updated_at: 2026-06-12
content_hash: sha256:e0ee3812bbb2eb64354d6675d2a893f0e65f5a3d3647b2e805dba25d9d127201
---

## 场景介绍

从5.0.3(15)开始，支持地图应用首页、搜索地点、查看地点详情、规划路线和进行导航功能；从6.0.1(21)开始，支持地图应用发起打车功能；从6.1.1(24)开始，打开地图应用查看地点详情支持终点描述，支持拉起地图应用离线地图管理页面。

本章节将向您介绍如何打开地图应用实现如下能力：

* 打开地图应用首页
* 打开地图应用搜索地点
* 打开地图应用查看地点详情
* 打开地图应用规划路线
* 打开地图应用进行导航
* 打开地图应用发起打车
* 打开地图应用离线地图管理页面

## 接口说明

调用地图应用的功能主要通过[petalMaps](../harmonyos-references/map-petal-maps.md)命名空间下的[openMapHomePage](../harmonyos-references/map-petal-maps.md#openmaphomepage)、[openMapTextSearch](../harmonyos-references/map-petal-maps.md#openmaptextsearch)、[openMapPoiDetail](../harmonyos-references/map-petal-maps.md#openmappoidetail)、[openMapRoutePlan](../harmonyos-references/map-petal-maps.md#openmaprouteplan)、[openMapNavi](../harmonyos-references/map-petal-maps.md#openmapnavi)、[openMapTaxi](../harmonyos-references/map-petal-maps.md#openmaptaxi)、[openMapOfflineDataManagement](../harmonyos-references/map-petal-maps.md#openmapofflinedatamanagement)等接口实现，更多接口及使用方法请参见[接口文档](../harmonyos-references/map-petal-maps.md)。

| 接口说明 | 描述 |
| --- | --- |
| [TextSearchParams](../harmonyos-references/map-petal-maps.md#textsearchparams) | 文本搜索的参数。 |
| [PoiDetailParams](../harmonyos-references/map-petal-maps.md#poidetailparams) | POI详情的参数。 |
| [RoutePlanParams](../harmonyos-references/map-petal-maps.md#routeplanparams) | 路线规划的参数。 |
| [NaviParams](../harmonyos-references/map-petal-maps.md#naviparams) | 导航的参数。 |
| [TaxiParams](../harmonyos-references/map-petal-maps.md#taxiparams) | 打车的参数。 |
| [OfflineDataParams](../harmonyos-references/map-petal-maps.md#offlinedataparams) | 离线地图管理参数。 |
| [openMapHomePage](../harmonyos-references/map-petal-maps.md#openmaphomepage)(context: [common.Context](../harmonyos-references/js-apis-inner-application-context.md)): Promise<void> | 打开地图应用首页。 |
| [openMapTextSearch](../harmonyos-references/map-petal-maps.md#openmaptextsearch)(context: [common.Context](../harmonyos-references/js-apis-inner-application-context.md), textSearchParams: [TextSearchParams](../harmonyos-references/map-petal-maps.md#textsearchparams)): Promise<void> | 打开地图应用搜索地点。 |
| [openMapPoiDetail](../harmonyos-references/map-petal-maps.md#openmappoidetail)(context: [common.Context](../harmonyos-references/js-apis-inner-application-context.md), poiDetailParams: [PoiDetailParams](../harmonyos-references/map-petal-maps.md#poidetailparams)): Promise<void> | 打开地图应用查看地点详情。 |
| [openMapRoutePlan](../harmonyos-references/map-petal-maps.md#openmaprouteplan)(context: [common.Context](../harmonyos-references/js-apis-inner-application-context.md), routePlanParams: [RoutePlanParams](../harmonyos-references/map-petal-maps.md#routeplanparams)): Promise<void> | 打开地图应用规划路线。 |
| [openMapNavi](../harmonyos-references/map-petal-maps.md#openmapnavi)(context: [common.Context](../harmonyos-references/js-apis-inner-application-context.md), naviParams: [NaviParams](../harmonyos-references/map-petal-maps.md#naviparams)): Promise<void> | 打开地图应用进行导航。 |
| [openMapTaxi](../harmonyos-references/map-petal-maps.md#openmaptaxi)(context: [common.Context](../harmonyos-references/js-apis-inner-application-context.md), taxiParams: [TaxiParams](../harmonyos-references/map-petal-maps.md#taxiparams)): Promise<void> | 打开地图应用打车页面。 |
| [openMapOfflineDataManagement](../harmonyos-references/map-petal-maps.md#openmapofflinedatamanagement)(context: [common.Context](../harmonyos-references/js-apis-inner-application-context.md), offlineDataParams: [OfflineDataParams](../harmonyos-references/map-petal-maps.md#offlinedataparams)): Promise<void> | 打开地图应用的离线地图管理页面。 |

## 地图应用使用的坐标类型

在国内站点，中国大陆使用GCJ02坐标系，中国台湾使用WGS84坐标系。

在海外站点，统一使用WGS84坐标系。坐标系转换参考：[坐标纠偏](map-convert-coordinate.md)。

## 开发步骤

导入相关模块

```typescript
import { petalMaps } from '@kit.MapKit';
import { mapCommon } from '@kit.MapKit';
```

### 打开地图应用首页

通过[openMapHomePage](../harmonyos-references/map-petal-maps.md#openmaphomepage)，打开地图应用首页。

```typescript
try {
  await petalMaps.openMapHomePage(this.getUIContext().getHostContext());
} catch (e) {
  console.error(`code:${e.code}, message:${e.message}`);
}
```

**图1** 打开地图应用首页

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/HU3OxFunQsWmJMYX_bMOxA/zh-cn_image_0000002736434225.jpg "点击放大")

### 打开地图应用进行地点搜索

通过[openMapTextSearch](../harmonyos-references/map-petal-maps.md#openmaptextsearch)，传入搜索目标名称，打开地图应用进行地点搜索。

```typescript
try {
  let params: petalMaps.TextSearchParams = {
    destinationName: '云谷'
  };
  await petalMaps.openMapTextSearch(this.getUIContext().getHostContext(), params);
} catch (e) {
  console.error(`code:${e.code}, message:${e.message}`);
}
```

**图2** 打开地图应用进行地点搜索

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/I1nhyCY4SX6Sxw03FBVbkA/zh-cn_image_0000002706835074.jpg "点击放大")

### 打开地图应用查看地点详情

通过[openMapPoiDetail](../harmonyos-references/map-petal-maps.md#openmappoidetail)，传入地点的经纬度，打开地图应用查看地点详情。

```typescript
try {
  let params: petalMaps.PoiDetailParams = {
    destinationPosition: {
      latitude: 31.968789,
      longitude: 118.798537
    },
    destinationName: '标记点',
    zoom: 17,
    coordinateType: mapCommon.CoordinateType.GCJ02,
    destinationAddress: '这是我选择的演示名称'
  };
  await petalMaps.openMapPoiDetail(this.getUIContext().getHostContext(), params);
} catch (e) {
  console.error(`code:${e.code}, message:${e.message}`);
}
```

**图3** 打开地图应用查看地点详情

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/QLeQBDaIT6a5UDQmOofw_Q/zh-cn_image_0000002736314181.jpg "点击放大")

### 打开地图应用规划路线

通过[openMapRoutePlan](../harmonyos-references/map-petal-maps.md#openmaprouteplan)，传入终点经纬度，打开地图应用规划路线。

```typescript
try {
  let params: petalMaps.RoutePlanParams = {
    destinationPosition: {
      latitude: 31.983015468224288,
      longitude: 118.78058590757131
    }
  };
  await petalMaps.openMapRoutePlan(this.getUIContext().getHostContext(), params);
} catch (e) {
  console.error(`code:${e.code}, message:${e.message}`);
}
```

**图4** 打开地图应用规划路线

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/e8_GA3glS_GjxVO285U49A/zh-cn_image_0000002706675138.jpg "点击放大")

### 打开地图应用进行导航

通过[openMapNavi](../harmonyos-references/map-petal-maps.md#openmapnavi)，传入终点经纬度，打开地图应用发起导航。

```typescript
try {
  let params: petalMaps.NaviParams = {
    destinationPosition: {
      latitude: 31.983015468224288,
      longitude: 118.78058590757131
    }
  };
  await petalMaps.openMapNavi(this.getUIContext().getHostContext(), params);
} catch (e) {
  console.error(`code:${e.code}, message:${e.message}`);
}
```

**图5** 打开地图应用进行导航

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/C6yrR4T-QN6RMpcQY46T5g/zh-cn_image_0000002736434227.jpg "点击放大")

### 打开地图应用打车页面

通过[openMapTaxi](../harmonyos-references/map-petal-maps.md#openmaptaxi)，传入终点经纬度，打开地图应用发起打车。

```typescript
try {
  let params: petalMaps.TaxiParams = {
    destinationPosition: {
      latitude: 31.983015468224288,
      longitude: 118.78058590757131
    }
  };
  await petalMaps.openMapTaxi(this.getUIContext().getHostContext(), params);
} catch (e) {
  console.error(`code:${e.code}, message:${e.message}`);
}
```

**图6** 打开地图应用进行打车

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/05/v3/VeOCrHtQTPS2TAVk9f9pSA/zh-cn_image_0000002706835076.jpg "点击放大")

### 打开地图应用离线地图管理页面

通过[openMapOfflineDataManagement](../harmonyos-references/map-petal-maps.md#openmapofflinedatamanagement)，传入离线地图管理参数，打开地图应用离线地图管理页面。

```typescript
try {
  // 打开地图应用手表离线地图管理页面
  let params: petalMaps.OfflineDataParams = {
    scenarios: 'WATCH',
    // 推荐下载离线地图的地区集合
    recommendedRegionIds: ['1026355368865976081']
  };
  await petalMaps.openMapOfflineDataManagement(this.getUIContext().getHostContext(), params);
} catch (e) {
  console.error(`code:${e.code}, message:${e.message}`);
}

try {
  // 打开地图应用地图资源（手机离线地图）管理页面
  let params: petalMaps.OfflineDataParams = {
    scenarios: 'PHONE',
    // 推荐下载离线地图的地区集合
    recommendedRegionIds: ['1026355368865976081']
  };
  await petalMaps.openMapOfflineDataManagement(this.getUIContext().getHostContext(), params);
} catch (e) {
  console.error(`code:${e.code}, message:${e.message}`);
}

try {
  // 打开地图应用导航语音管理页面
  let params: petalMaps.OfflineDataParams = {
    scenarios: 'VOICE'
  };
  await petalMaps.openMapOfflineDataManagement(this.getUIContext().getHostContext(), params);
} catch (e) {
  console.error(`code:${e.code}, message:${e.message}`);
}
```

**图7** 打开地图应用手表离线地图管理页面

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/CJKc-D-eQG20EbWlgLRKHA/zh-cn_image_0000002736314183.jpg "点击放大")

**图8** 打开地图应用地图资源（手机离线地图）管理页面

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/PsUgP0YzRLO7YzdSfkWw_Q/zh-cn_image_0000002706675140.jpg "点击放大")

**图9** 打开地图应用导航语音管理页面

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1f/v3/SgRE3aSSRhyYdRbGYFlH9Q/zh-cn_image_0000002736434229.jpg "点击放大")
