---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-map-flowfieldoverlay
title: Interface (FlowFieldOverlay)
breadcrumb: API参考 > 应用服务 > Map Kit（地图服务） > ArkTS API > map（地图显示功能） > Interface (FlowFieldOverlay)
category: harmonyos-references
scraped_at: 2026-09-02T15:02:59+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:4aa961509d468c86d1d3aea2500ac1bca0fdd9c49fceff4da6e538f613a743b4
---

## 导入模块

```typescript
import { map, mapCommon } from '@kit.MapKit';
```

## FlowFieldOverlay

流场图层管理对象。在调用map.[MapComponentController](map-map-mapcomponentcontroller.md)类的[addFlowFieldOverlay](map-map-mapcomponentcontroller.md#addflowfieldoverlay)方法时会返回该类型的实例，继承[BaseOverlay](map-map-baseoverlay.md)。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core.EnhancedOverlay

**起始版本：** 6.0.0(20)

**示例：**

```typescript
let params: mapCommon.FlowFieldOverlayParams = {
  // data为GRIB2规范的json数据，需开发者自行传输，可参考流场数据格式参考
  data: 'xxx'
};
let fieldOverlay = await mapController.addFlowFieldOverlay(params);
```

### setStyle

setStyle(style: mapCommon.ParticleStyle): void

设置粒子样式。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core.EnhancedOverlay

**起始版本：** 6.0.0(20)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| style | [mapCommon.ParticleStyle](map-common.md#particlestyle) | 是 | 粒子样式。 |

**示例：**

```typescript
let style: mapCommon.ParticleStyle = {
  count: 200,
  color: 0xff009575,
  maxSpeed: 60,
  speedFactor: 0.3
};
fieldOverlay.setStyle(style);
```

### getStyle

getStyle(): mapCommon.ParticleStyle

获取粒子样式。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core.EnhancedOverlay

**起始版本：** 6.0.0(20)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [mapCommon.ParticleStyle](map-common.md#particlestyle) | 粒子样式。 |

**示例：**

```typescript
let style: mapCommon.ParticleStyle = fieldOverlay.getStyle();
```
