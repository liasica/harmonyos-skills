---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-offline-map-data
title: offlineMapData（离线地图）
breadcrumb: API参考 > 应用服务 > Map Kit（地图服务） > ArkTS API > offlineMapData（离线地图）
category: harmonyos-references
scraped_at: 2026-09-02T14:53:23+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:18ec5c33e2734bf2e3d475ffd7b78045726f2cd4693efb59520b84f0ae89d54b
---

本模块提供获取离线地图功能。

**起始版本：** 26.0.0

## 导入模块

```typescript
import { offlineMapData } from '@kit.MapKit';
```

## getRecommendedCityIdsByLatLngs

getRecommendedCityIdsByLatLngs(context: common.Context, latlngs: mapCommon.LatLng[]): Promise<string[]>

根据经纬度数组查询设备上离线地图未下载的区域。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Map.Core.OfflineMapData

**起始版本：** 26.0.0

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| context | [common.Context](js-apis-inner-application-context.md) | 是 | Context上下文。 |
| latlngs | [mapCommon.LatLng](map-common.md#latlng)[] | 是 | 经纬度数组，最大长度为20，异常值返回空数组[]。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string[]> | Promise对象，返回推荐区域列表数组。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-map.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1002600001 | System internal error. |
| 1002600004 | The Map permission is not enabled. |

**示例：**

```typescript
// 经纬度数组
let latLngArr: mapCommon.LatLng[] = [
  { latitude: 49.5, longitude: 3.5 },
  { latitude: 49.5, longitude: 4.5 },
  { latitude: 50.5, longitude: 4.5 },
  { latitude: 51.5, longitude: 4.5 }];
let resArray: string[] = await offlineMapData.getRecommendedCityIdsByLatLngs(this.getUIContext().getHostContext(), latLngArr);
```
