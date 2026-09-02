---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-map-mapsignalline
title: Interface (MapSignalLine)
breadcrumb: API参考 > 应用服务 > Map Kit（地图服务） > ArkTS API > map（地图显示功能） > Interface (MapSignalLine)
category: harmonyos-references
scraped_at: 2026-09-02T15:02:59+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:4abc0b8c22377e33a269f57c94933f1897767bb16669bf15abd4df0431aa54cf
---

## 导入模块

```typescript
import { map, mapCommon } from '@kit.MapKit';
```

## MapSignalLine

信号路线管理对象，继承[BaseOverlay](map-map-baseoverlay.md)。在调用[addSignalLine](map-map-mapcomponentcontroller.md#addsignalline)方法时会返回该类型的实例。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 26.0.0

**示例：**

```typescript
let mapSignalParams: mapCommon.MapSignalParams = {
  signalId: 'signalId1'
};
mapSignalParams.points =
  [{ longitude: 118.553695, latitude: 32.050789 },
    { longitude: 118.553738, latitude: 32.050884 },
    { longitude: 118.548506, latitude: 32.048543 },
    { longitude: 118.548413, latitude: 32.048374 },
    { longitude: 118.547185, latitude: 32.048252 },
    { longitude: 118.546939, latitude: 32.048296 }]
// 添加信号路线
let mapSignalLine1 = await mapController.addSignalLine(mapSignalParams);
```

### setColors

setColors(colors: number[]): void

设置信号路线的颜色。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 26.0.0

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| colors | number[] | 是 | 信号路线的颜色，三个颜色分别对应弱、中、强信号，数组长度必须为3，ARGB格式，例如：[0xFF000000, 0xFFFFDF42, 0xFF42B0FF]。异常值不处理。 |

**示例：**

```typescript
// 设置信号路线的颜色
signalLine.setColors([0xFF000000, 0xFFFFDF42, 0xFF42B0FF]);
```

### getColors

getColors(): number[]

获取信号路线的颜色。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 26.0.0

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number[] | 信号路线的颜色。 |

**示例：**

```typescript
// 获取信号路线颜色
let colors: number[] = signalLine.getColors()
```

### setWidth

setWidth(width: number): void

设置信号路线的宽度。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 26.0.0

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| width | number | 是 | 信号路线的宽度，单位：px，有效范围为：[0, 512]。异常值不处理。 |

**示例：**

```typescript
// 设置线宽为20
signalLine.setWidth(20);
```

### getWidth

getWidth(): number

获取信号路线的宽度。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 26.0.0

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 信号路线的宽度。 |

**示例：**

```typescript
// 获取信号路线宽度
let width: number = signalLine.getWidth()
```
