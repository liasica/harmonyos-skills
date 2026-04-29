---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-map-tileoverlay
title: TileOverlay
breadcrumb: API参考 > 应用服务 > Map Kit（地图服务） > ArkTS API > map（地图显示功能） > TileOverlay
category: harmonyos-references
scraped_at: 2026-04-29T14:08:01+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:5a8a4c2a7524c842ccb79faa22c75aa02e98a38f5064d765f691ca00a7107ad4
---

## 导入模块

PhonePC/2in1TabletWearable

```
1. import { map, mapCommon } from '@kit.MapKit';
```

## TileOverlay

PhonePC/2in1TabletWearable

瓦片图层，继承[BaseOverlay](map-map-baseoverlay.md)。瓦片图层是一种基于[BaseOverlay](map-map-baseoverlay.md)实现的地图覆盖层，用于展示自定义瓦片。

说明

由于性能考虑，建议最多添加10个TileOverlay，且提供的图层瓦片分辨率是256\*256。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.3(15)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.3(15)

**示例：**

```
1. let params: mapCommon.TileOverlayParams = {
2. // 设置地图瓦片图层的地址，必须是以http或者https开头的URL且包含占位符{x}、{y}和{z}
3. tileUrl: "https://xxx/xxx?x={x}&y={y}&z={z}",
4. transparency: 0,
5. fadeIn: false
6. };
7. let tileOverlay: map.TileOverlay = this.mapController?.addTileOverlay(params);
```

### clearTileCache

PhonePC/2in1TabletWearable

clearTileCache(): void

清除瓦片图层的缓存。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.3(15)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.3(15)

**示例：**

```
1. tileOverlay.clearTileCache();
```

### setFadeIn

PhonePC/2in1TabletWearable

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

```
1. tileOverlay.setFadeIn(false);
```

### setTransparency

PhonePC/2in1TabletWearable

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

```
1. tileOverlay.setTransparency(0.5);
```

### getFadeIn

PhonePC/2in1TabletWearable

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

```
1. let isFadeIn: boolean = tileOverlay.getFadeIn();
```

### getTransparency

PhonePC/2in1TabletWearable

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

```
1. let transparency: number = tileOverlay.getTransparency();
```

### clearDiskCache

PhonePC/2in1TabletWearable

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

```
1. tileOverlay.clearDiskCache();
```
