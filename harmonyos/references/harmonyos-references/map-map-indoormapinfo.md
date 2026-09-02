---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-map-indoormapinfo
title: Interface (IndoorMapInfo)
breadcrumb: API参考 > 应用服务 > Map Kit（地图服务） > ArkTS API > map（地图显示功能） > Interface (IndoorMapInfo)
category: harmonyos-references
scraped_at: 2026-09-02T14:53:23+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:ae0bcb01108fe180afe588de0626ceb67043ccf8c31ceb1d1d4dabc6be8b0e75
---

## 导入模块

```typescript
import { map } from '@kit.MapKit';
```

## IndoorMapInfo

室内图信息。当进入室内图时，会通过[on](map-map-mapeventmanager.md#onindoormapenter)方法触发回调，并返回[IndoorMapInfo](map-map-indoormapinfo.md)类型的实例，从而实现室内导航、楼层切换等功能。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.1.1(19)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**设备行为差异：** 在5.1.1(19)及之后版本该接口在phone、tablet和PC/2in1均可正常使用，在其他设备中返回801错误码。

**起始版本：** 5.1.1(19)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| buildingId | string | 否 | 否 | 表示建筑物的id。 |
| floorNames | string[] | 否 | 否 | 建筑物楼层名称数组。 |
| floorOrders | number[] | 否 | 否 | 建筑楼层顺序数组。 |
| currentFloorName | string | 否 | 否 | 当前展示楼层的名称。 |

**示例：**

```typescript
mapEventManager.on('indoorMapEnter', (indoorMapInfo: map.IndoorMapInfo)=>{
  console.info('indoorMapinfo: ' , indoorMapInfo);
})
```
