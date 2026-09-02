---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-map-tileoverlay
title: Interface (TileOverlay)
breadcrumb: API参考 > 应用服务 > Map Kit（地图服务） > ArkTS API > map（地图显示功能） > Interface (TileOverlay)
category: harmonyos-references
scraped_at: 2026-09-02T15:02:59+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:85e48b9e04e0262deb6b8ccfcda3370e33c46525067391d10585fc42f444f8e8
---

## 导入模块

```typescript
import { map, mapCommon } from '@kit.MapKit';
```

## TileOverlay

瓦片图层，继承[BaseOverlay](map-map-baseoverlay.md)。瓦片图层是一种基于[BaseOverlay](map-map-baseoverlay.md)实现的地图覆盖层，用于展示自定义瓦片。

**说明** 

由于性能考虑，建议最多添加10个TileOverlay，且提供的图层瓦片分辨率是256\*256。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.3(15)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.3(15)

**示例：**

```typescript
let params: mapCommon.TileOverlayParams = {
  // 开发者的地图瓦片图层地址，必须使用以http或者https开头的URL地址，且需包含?x={x}&y={y}&z={z}格式的占位符
  tileUrl: "https://xxx/xxx?x={x}&y={y}&z={z}",
  transparency: 0,
  fadeIn: false
};
let tileOverlay: map.TileOverlay = this.mapController?.addTileOverlay(params);
```

### clearTileCache

clearTileCache(): void

清除瓦片图层的缓存。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.3(15)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.3(15)

**示例：**

```typescript
tileOverlay.clearTileCache();
```

### setFadeIn

setFadeIn(fadeIn: boolean): void

是否开启瓦片图层淡入。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.3(15)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.3(15)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| fadeIn | boolean | 是 | 是否开启瓦片图层淡入。  - true：开启瓦片图层淡入。  - false：不开启瓦片图层淡入。 |

**示例：**

```typescript
tileOverlay.setFadeIn(false);
```

### setTransparency

setTransparency(transparency: number): void

设置瓦片图层的透明度。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.3(15)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.3(15)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| transparency | number | 是 | 瓦片图层的透明度。取值范围：[0, 1]。0表示不透明，1表示全透明，异常值不处理。 |

**示例：**

```typescript
tileOverlay.setTransparency(0.5);
```

### getFadeIn

getFadeIn(): boolean

返回是否开启瓦片图层淡入。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.3(15)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.3(15)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回是否开启瓦片图层淡入。  - true：已开启瓦片图层淡入。  - false：未开启瓦片图层淡入。 |

**示例：**

```typescript
let isFadeIn: boolean = tileOverlay.getFadeIn();
```

### getTransparency

getTransparency(): number

返回瓦片图层的透明度。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.3(15)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.3(15)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回瓦片图层的透明度。取值范围：[0, 1]，0表示不透明，1表示全透明。 |

**示例：**

```typescript
let transparency: number = tileOverlay.getTransparency();
```

### clearDiskCache

clearDiskCache(): Promise<void>

清除磁盘缓存，内存缓存也会被清除。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 6.0.0(20)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**示例：**

```typescript
tileOverlay.clearDiskCache();
```
