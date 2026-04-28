---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-map-flowfieldoverlay
title: FlowFieldOverlay
breadcrumb: API参考 > 应用服务 > Map Kit（地图服务） > ArkTS API > map（地图显示功能） > FlowFieldOverlay
category: harmonyos-references
scraped_at: 2026-04-28T08:17:20+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:963ca869a1004afb914d43f3fe39f7983d32e677c5d30f416d273f23b0b327f8
---

## 导入模块

PhonePC/2in1Tablet

```
1. import { map, mapCommon } from '@kit.MapKit';
```

## FlowFieldOverlay

PhonePC/2in1Tablet

流场图层管理对象。在调用map.[MapComponentController](map-map-mapcomponentcontroller.md)类的[addFlowFieldOverlay](map-map-mapcomponentcontroller.md#addflowfieldoverlay)方法时会返回该类型的实例，继承[BaseOverlay](map-map-baseoverlay.md)。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core.EnhancedOverlay

**起始版本：** 6.0.0(20)

**示例：**

```
1. let params: mapCommon.FlowFieldOverlayParams = {
2. // data为GRIB2规范的json数据，需开发者自行传输，可参考流场数据格式参考
3. data: 'xxx'
4. };
5. let fieldOverlay = await mapController.addFlowFieldOverlay(params);
```

### setStyle

PhonePC/2in1Tablet

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

```
1. let style: mapCommon.ParticleStyle = {
2. count: 200,
3. color: 0xff009575,
4. maxSpeed: 60,
5. speedFactor: 0.3
6. };
7. fieldOverlay.setStyle(style);
```

### getStyle

PhonePC/2in1Tablet

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

```
1. let style: mapCommon.ParticleStyle = fieldOverlay.getStyle();
```
