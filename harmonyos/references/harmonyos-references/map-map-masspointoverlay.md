---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-map-masspointoverlay
title: Interface (MassPointOverlay)
breadcrumb: API参考 > 应用服务 > Map Kit（地图服务） > ArkTS API > map（地图显示功能） > Interface (MassPointOverlay)
category: harmonyos-references
scraped_at: 2026-09-02T15:02:59+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:93538ea403e42a88a345e57737eaebde03d3d27010092e9d862a2dc2d5cb6380
---

## 导入模块

```typescript
import { map, mapCommon } from '@kit.MapKit';
```

## MassPointOverlay

海量点的管理对象。在调用map.[MapComponentController](map-map-mapcomponentcontroller.md)类的[addMassPointOverlay](map-map-mapcomponentcontroller.md#addmasspointoverlay)方法时会返回该类型的实例。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 6.0.0(20)

**示例：**

```typescript
let items: mapCommon.MassPointItem[] = [];
for (let i = 0; i < 1000; i++) {
  // 将海量点存入items
  items.push({
    // itemId为开发者自定义标识符
    itemId: 'test' + i,
    // 经纬度坐标
    position: {
      longitude: 118.11111 + Math.random() * 1 - 0.5,
      latitude: 32.11111 + Math.random() * 1 - 0.5
    },
    snippet: 'test' + i,
    title: 'test' + i
  })
}
let params: mapCommon.MassPointOverlayParams = {
  id: 'test',
  items: items,
  // 图标存放在resources/rawfile，icon参数传入rawfile文件夹下的相对路径
  icon: 'icon/maps_blue_dot.png'
}
let massPointOverlay = await this.mapController?.addMassPointOverlay(params);
```

### getId

getId(): string

获取海量点的ID。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 6.0.0(20)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 海量点的ID。 |

**示例：**

```typescript
let Id = massPointOverlay.getId();
```

### setItems

setItems(items: mapCommon.MassPointItem[]): void

更新海量点列表。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 6.0.0(20)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| items | [mapCommon.MassPointItem](map-common.md#masspointitem)[] | 是 | 海量点列表（建议数据量小于100000条）。 |

**示例：**

```typescript
let items: mapCommon.MassPointItem[] = [
  {
    itemId: '1',
    position: { latitude: 32.11111, longitude: 118.11111 }
  },
  {
    itemId: '2',
    position: { latitude: 32.22222, longitude: 118.22222 }
  }
];
massPointOverlay.setItems(items);
```

### getItems

getItems(): mapCommon.MassPointItem[]

获取海量点列表。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 6.0.0(20)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [mapCommon.MassPointItem](map-common.md#masspointitem)[] | 海量点列表。 |

**示例：**

```typescript
let MassPointItem: mapCommon.MassPointItem[] = this.massPointOverlay.getItems();
```

### setAnchorU

setAnchorU(anchorU: number): void

更新图标锚点在水平方向上的位置。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 6.0.0(20)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| anchorU | number | 是 | 更新图标锚点在水平方向上的位置，取值范围：[0, 1]。 |

**示例：**

```typescript
massPointOverlay.setAnchorU(0.6);
```

### getAnchorU

getAnchorU(): number

获取图标锚点在水平方向上的位置。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 6.0.0(20)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 图标锚点在水平方向上的位置。 |

**示例：**

```typescript
let AnchorU: number = this.massPointOverlay.getAnchorU();
```

### setAnchorV

setAnchorV(anchorV: number): void

更新图标锚点在垂直方向上的位置。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 6.0.0(20)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| anchorV | number | 是 | 更新图标锚点在垂直方向上的位置，取值范围：[0, 1]。 |

**示例：**

```typescript
massPointOverlay.setAnchorV(0.6);
```

### getAnchorV

getAnchorV(): number

获取图标锚点在垂直方向上的位置。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 6.0.0(20)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 图标锚点在垂直方向上的位置。 |

**示例：**

```typescript
let AnchorV: number = this.massPointOverlay.getAnchorV();
```

### setVisible

setVisible(visible: boolean): void

设置海量点是否可见。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 6.0.0(20)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| visible | boolean | 是 | 海量点是否可见。  - true：可见。  - false：不可见。 |

**示例：**

```typescript
massPointOverlay.setVisible(true);
```

### isVisible

isVisible(): boolean

获取海量点是否可见。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 6.0.0(20)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 海量点是否可见。  - true：可见。  - false：不可见。 |

**示例：**

```typescript
let isVisible: boolean = massPointOverlay.isVisible();
```

### remove

remove(): void

删除海量点。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 6.0.0(20)

**示例：**

```typescript
massPointOverlay.remove();
```
