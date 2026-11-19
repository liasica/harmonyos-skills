---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/map-petalmaps
title: 通过地图应用实现导航等能力
breadcrumb: 指南 > 应用服务 > Map Kit（地图服务） > 通过地图应用实现导航等能力
category: harmonyos-guides
scraped_at: 2026-11-19T09:49:06+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:7cdfcc026a36428d3b3fad3d15b23c1c2f88939a54a47eba66a57b88a4870e6a
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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/Xknih5AmSVeah6ae2neQqw/zh-cn_image_0000002791566518.jpg?HW-CC-KV=V1&HW-CC-Date=20261119T014905Z&HW-CC-Expire=31536000000&HW-CC-Sign=EAC32CCC07B4DD7FCAA156A9B48BB15A069E621D883EDDF7488AA55DB1777BBD "点击放大")

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/mmWTWhe8QWqgqpv8lV86eQ/zh-cn_image_0000002820526471.jpg?HW-CC-KV=V1&HW-CC-Date=20261119T014905Z&HW-CC-Expire=31536000000&HW-CC-Sign=C4FDA992DAA4B2EE63420FD62D59B537ECE5ECA605E5F7DACA22C9212DE8BD87 "点击放大")

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
    // 可选，系统将自动通过逆地理编码生成描述
    destinationAddress: '这是我选择的演示名称'
  };
  await petalMaps.openMapPoiDetail(this.getUIContext().getHostContext(), params);
} catch (e) {
  console.error(`code:${e.code}, message:${e.message}`);
}
```

**图3** 打开地图应用查看地点详情

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/yfh5zzEuRDOrdKvb4YD_xQ/zh-cn_image_0000002820406471.jpg?HW-CC-KV=V1&HW-CC-Date=20261119T014905Z&HW-CC-Expire=31536000000&HW-CC-Sign=AF8F0AC04242980CA1FE473AE4FFE28FD6C0666BF98C334DBF709BDB5F8D45D2 "点击放大")

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/zd7ItRHtSbejZyDzcuwcag/zh-cn_image_0000002791726492.jpg?HW-CC-KV=V1&HW-CC-Date=20261119T014905Z&HW-CC-Expire=31536000000&HW-CC-Sign=B3EC8F7E86E50681A6D2A2EB42EACC6A06D3E84CAA4AE78F0B1436D95018DAA8 "点击放大")

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/FCSwndM7Q4yE5_lH2xowsQ/zh-cn_image_0000002791566520.jpg?HW-CC-KV=V1&HW-CC-Date=20261119T014905Z&HW-CC-Expire=31536000000&HW-CC-Sign=BC3F80FC208C59DDF860E1980663EADF563B6D55B1891A8C29E9B547BD698E15 "点击放大")

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fb/v3/TTsYybanRFGO3lLHWxIbMA/zh-cn_image_0000002820526473.png?HW-CC-KV=V1&HW-CC-Date=20261119T014905Z&HW-CC-Expire=31536000000&HW-CC-Sign=5EC662A290B9513672FB056C534C1F035B85213A7CA6C0FE82FD5E02F3134AE9 "点击放大")

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/H9F7Td7MTIGG5E7IX4-jXg/zh-cn_image_0000002820406473.jpg?HW-CC-KV=V1&HW-CC-Date=20261119T014905Z&HW-CC-Expire=31536000000&HW-CC-Sign=32AD8F97425F0C71BACE91BFEBDB997DBDFDECE9A7C9B8526BA9F07DEB1A274E "点击放大")

**图8** 打开地图应用地图资源（手机离线地图）管理页面

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/ScY1PP7xR9iaLwtLNcAeoQ/zh-cn_image_0000002791726494.jpg?HW-CC-KV=V1&HW-CC-Date=20261119T014905Z&HW-CC-Expire=31536000000&HW-CC-Sign=A4101E03DE3BC7CFB5ACDBA27AE0CCEB11CE2278B6060F1113D4724EDBBA711F "点击放大")

**图9** 打开地图应用导航语音管理页面

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/cYciD_uwTFm_ZQcmjjtLLA/zh-cn_image_0000002791566522.jpg?HW-CC-KV=V1&HW-CC-Date=20261119T014905Z&HW-CC-Expire=31536000000&HW-CC-Sign=A9B741D7E9E94DC4A62C0BEE0AC0F24CD3B6A9E3D2459C4F45AB4F12A414957E "点击放大")
