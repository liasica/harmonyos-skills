---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/map-offlinemapdata
title: 离线地图
breadcrumb: 指南 > 应用服务 > Map Kit（地图服务） > 离线地图
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:58+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:6b685dcfc690816af48369da4f52a4cc4fcf304237b92133c045f43bd7297302
---

## 场景介绍

从26.0.0开始，支持根据经纬度数组查询未下载的区域地图功能。

离线地图允许用户提前下载指定区域的地图数据，以便在无网络或网络不佳时正常使用地图功能。

## 接口说明

| 接口名 | 描述 |
| --- | --- |
| [getRecommendedCityIdsByLatLngs](../harmonyos-references/map-offline-map-data.md#getrecommendedcityidsbylatlngs)(context: [common.Context](../harmonyos-references/js-apis-inner-application-context.md), latlngs: [mapCommon.LatLng](../harmonyos-references/map-common.md#latlng)[]): Promise<string[]> | 根据经纬度数组查询设备上离线地图未下载的区域。 |

## 开发步骤

### 根据经纬度数组查询未下载的区域

1.导入相关模块。

```typescript
import { offlineMapData } from '@kit.MapKit';
import { mapCommon } from '@kit.MapKit';
```

2.通过[getRecommendedCityIdsByLatLngs](../harmonyos-references/map-offline-map-data.md#getrecommendedcityidsbylatlngs)，查询离线地图未下载的区域。

```typescript
try {
  // 经纬度数组
  let latLngArr: mapCommon.LatLng[] = [{
    latitude: 49.5,
    longitude: 3.5
  }, {
    latitude: 49.5,
    longitude: 4.5
  }, {
    latitude: 50.5,
    longitude: 4.5
  }, {
    latitude: 51.5,
    longitude: 4.5
  }];
  // 根据经纬度数组查询设备上未下载的区域
  let resArray: string[] = await offlineMapData.getRecommendedCityIdsByLatLngs(
    this.getUIContext().getHostContext(), latLngArr);
  console.info(`resArray: ${JSON.stringify(resArray)}`);
} catch (e) {
  console.error(`code:${e.code}, message:${e.message}`);
}
```
