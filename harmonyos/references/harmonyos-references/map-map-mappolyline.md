---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-map-mappolyline
title: Interface (MapPolyline)
breadcrumb: API参考 > 应用服务 > Map Kit（地图服务） > ArkTS API > map（地图显示功能） > Interface (MapPolyline)
category: harmonyos-references
scraped_at: 2026-09-02T15:02:58+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:b6b7057306b426a8bdb586ab5c21b4a5ba85a5d9ea32cb32f828fdc607d098e8
---

## 导入模块

```typescript
import { map, mapCommon } from '@kit.MapKit';
```

## MapPolyline

折线，继承[BaseOverlay](map-map-baseoverlay.md)。在调用map.[MapComponentController](map-map-mapcomponentcontroller.md)类的[addPolyline](map-map-mapcomponentcontroller.md#addpolyline)方法时会返回该类型的实例。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**示例：**

```typescript
import { image } from '@kit.ImageKit';

// 数组存放图片内容
let customTextures: Array<ResourceStr | image.PixelMap> = new Array();
// 图标存放在resources/rawfile目录下
customTextures.push('icon/img.png');
customTextures.push('icon/img_1.png');
let cusIndexNumber: Array<number> = new Array();
// cusIndexNumber数组长度与折线点数量必须相同，数组元素内容与customTextures下标相对应，图片从数组第二个元素开始选择
cusIndexNumber.push(0, 0, 1);
let polylineOption: mapCommon.MapPolylineOptions = {
  points: [
    { latitude: 31.68, longitude: 118.166 },
    { latitude: 31.48, longitude: 118.366 },
    { latitude: 31.28, longitude: 118.766 }
  ],
  customTextures: customTextures,
  customTextureIndexes: cusIndexNumber
};
let mapPolyline = await this.mapController.addPolyline(polylineOption);
```

### getColor

getColor(): number

获取折线的颜色值。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | ARGB格式颜色值。 |

**示例：**

```typescript
let color: number = mapPolyline.getColor();
```

### getColors

getColors(): Array<number>

获取折线的分段颜色值数组。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<number> | 折线的分段颜色值数组。 |

**示例：**

```typescript
let colors: Array<number> = mapPolyline.getColors();
```

### getEndCap

getEndCap(): mapCommon.CapStyle

获取折线的末尾端点样式。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [mapCommon.CapStyle](map-common.md#capstyle) | 折线的末尾端点样式。 |

**示例：**

```typescript
let endCap: mapCommon.CapStyle = mapPolyline.getEndCap();
```

### getJointType

getJointType(): mapCommon.JointType

获取折线除起始和结束顶点之外的所有顶点的节点类型属性。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [mapCommon.JointType](map-common.md#jointtype) | 折线除起始和结束顶点之外的所有顶点的节点类型属性。 |

**示例：**

```typescript
let jointType: mapCommon.JointType = mapPolyline.getJointType();
```

### getPatterns

getPatterns(): Array<mapCommon.PatternItem>

获取折线的样式属性。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<[mapCommon.PatternItem](map-common.md#patternitem)> | 折线的样式属性。 |

**示例：**

```typescript
let patterns: Array<mapCommon.PatternItem> = mapPolyline.getPatterns();
```

### getPoints

getPoints(): Array<mapCommon.LatLng>

获取折线的顶点坐标属性。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<[mapCommon.LatLng](map-common.md#latlng)> | 折线的顶点坐标属性。 |

**示例：**

```typescript
let points: Array<mapCommon.LatLng> = mapPolyline.getPoints();
```

### getStartCap

getStartCap(): mapCommon.CapStyle

获取折线的起始端点样式。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [mapCommon.CapStyle](map-common.md#capstyle) | 折线的起始端点样式。 |

**示例：**

```typescript
let startCap: mapCommon.CapStyle = mapPolyline.getStartCap();
```

### getWidth

getWidth(): number

获取折线的宽度属性。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 折线的宽度属性，单位：px。 |

**示例：**

```typescript
let width: number = mapPolyline.getWidth();
```

### isClickable

isClickable(): boolean

获取折线的可点击属性。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 折线的可点击性。  - true：可点击  - false：不可点击 |

**示例：**

```typescript
let isClickable: boolean = mapPolyline.isClickable();
```

### isGeodesic

isGeodesic(): boolean

获取折线的大地线属性。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 折线的大地线属性。  - true：大地线  - false：非大地线 |

**示例：**

```typescript
let isGeodesic: boolean = mapPolyline.isGeodesic();
```

### isGradient

isGradient(): boolean

获取折线的渐变属性。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 折线的渐变属性。  - true：渐变  - false：不渐变 |

**示例：**

```typescript
let isGradient: boolean = mapPolyline.isGradient();
```

### setClickable

setClickable(clickable: boolean): void

设置折线是否可以点击。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| 参数名 | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| clickable | boolean | 是 | 设置折线是否可以点击，异常值不处理。  - true：可以  - false：不可以 |

**示例：**

```typescript
mapPolyline.setClickable(true);
```

### setColor

setColor(color: number): void

设置折线的颜色值。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| 参数名 | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| color | number | 是 | ARGB格式颜色值，异常值不处理。 |

**示例：**

```typescript
mapPolyline.setColor(0xff000000);
```

### setColors

setColors(colors: Array<number>): void

设置折线的多段颜色值数组。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| 参数名 | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| colors | Array<number> | 是 | 多段颜色，ARGB格式颜色值数组，异常值不处理。 |

**示例：**

```typescript
mapPolyline.setColors([0xffffff00, 0xff000000]);
```

### setEndCap

setEndCap(endCap: mapCommon.CapStyle): void

设置折线的末尾端点样式。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| 参数名 | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| endCap | [mapCommon.CapStyle](map-common.md#capstyle) | 是 | 折线的末尾端点样式，异常值不处理。 |

**示例：**

```typescript
mapPolyline.setEndCap(mapCommon.CapStyle.BUTT);
```

### setGeodesic

setGeodesic(geodesic: boolean): void

设置是否将折线的每个线段绘制为大地线。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| 参数名 | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| geodesic | boolean | 是 | 将折线的每个线段绘制为大地线，异常值不处理。  - true：每段绘制为大地线  - false：不是大地线 |

**示例：**

```typescript
mapPolyline.setGeodesic(true);
```

### setGradient

setGradient(gradient: boolean): void

设置折线的渐变属性是否启用。需设置折线颜色方可生效。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| 参数名 | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| gradient | boolean | 是 | 设置折线的渐变属性是否启用，异常值不处理。  - true：渐变  - false：不渐变 |

**示例：**

```typescript
mapPolyline.setGradient(true);
```

### setJointType

setJointType(jointType: mapCommon.JointType): void

设置折线除起始和结束顶点之外的所有顶点的节点类型。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| 参数名 | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| jointType | [mapCommon.JointType](map-common.md#jointtype) | 是 | 节点类型，异常值不处理。 |

**示例：**

```typescript
mapPolyline.setJointType(mapCommon.JointType.DEFAULT);
```

### setPatterns

setPatterns(patterns: Array<mapCommon.PatternItem>): void

设置折线的样式。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| 参数名 | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| patterns | Array<[mapCommon.PatternItem](map-common.md#patternitem)> | 是 | [PatternItem](map-common.md#patternitem)对象的集合，异常值不处理。 |

**示例：**

```typescript
let linePattern: Array<mapCommon.PatternItem> = [
  { type: mapCommon.PatternItemType.DASH, length: 100 },
  { type: mapCommon.PatternItemType.DOT, length: 100 },
  { type: mapCommon.PatternItemType.GAP, length: 100 }
];
mapPolyline.setPatterns(linePattern);
```

### setPoints

setPoints(points: Array<mapCommon.LatLng>): void

设置折线的顶点坐标。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| 参数名 | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| points | Array<[mapCommon.LatLng](map-common.md#latlng)> | 是 | 折线顶点的集合。默认情况下，折线不闭合；要形成闭合的折线，起点和终点必须相同，异常值不处理。 |

**示例：**

```typescript
let points: Array<mapCommon.LatLng> = [
  { latitude: 31.18, longitude: 118.766 },
  { latitude: 31.38, longitude: 118.366 },
  { latitude: 31.68, longitude: 118.566 },
  { latitude: 31.98, longitude: 118.266 },
  { latitude: 31.88, longitude: 118.866 }
];
mapPolyline.setPoints(points);
```

### setStartCap

setStartCap(startCap: mapCommon.CapStyle): void

设置折线的起始端点样式。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| 参数名 | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| startCap | [mapCommon.CapStyle](map-common.md#capstyle) | 是 | 折线的起始端点样式，异常值不处理。 |

**示例：**

```typescript
mapPolyline.setStartCap(mapCommon.CapStyle.BUTT);
```

### setWidth

setWidth(width: number): void

设置折线的宽度。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| 参数名 | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| width | number | 是 | 折线的宽度，单位：px，取值范围：大于等于0，异常值不处理。 |

**示例：**

```typescript
mapPolyline.setWidth(20);
```

### setCustomTexture

setCustomTexture(customTexture: ResourceStr | image.PixelMap): Promise<void>

设置折线纹理。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| customTexture | [ResourceStr](ts-types.md#resourcestr) | [image.PixelMap](arkts-apis-image-pixelmap.md) | 是 | 折线纹理。建议纹理使用没有背景色（透明色）的图片，异常值不处理。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**示例：**

```typescript
// 图标存放在resources/rawfile目录下
await mapPolyline.setCustomTexture("icon/naviline_arrow.png");
```

### setCustomTexture

setCustomTexture(customTexture: ResourceStr | image.PixelMap, isTextureMappingUsed: boolean): Promise<void>

设置折线纹理。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.3(15)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.3(15)

**参数：**

| 参数名 | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| customTexture | [ResourceStr](ts-types.md#resourcestr) | [image.PixelMap](arkts-apis-image-pixelmap.md) | 是 | 折线纹理。建议纹理使用没有背景色（透明色）的图片，异常值不处理。 |
| isTextureMappingUsed | boolean | 是 | 是否使用贴图模式进行纹理绘制，异常值不处理。  - true：使用贴图模式  - false：不使用贴图模式，建议纹理没有背景色（使用透明色） |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**示例：**

```typescript
// 图标需存放在resources/rawfile目录下
await mapPolyline.setCustomTexture("icon/naviline_arrow.png", true);
```

### setCustomTextureIndexes

setCustomTextureIndexes(customTextureIndexes: number[]): Promise<void>

动态设置自定义纹理索引。折线设置纹理后，该接口可以将已有的纹理资源动态应用在各个折线段上。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.3(15)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.3(15)

**参数：**

| 参数名 | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| customTextureIndexes | number[] | 是 | 每个坐标对应的纹理索引。数组长度需要和points的数量保持一致，数组中的元素取值范围：自然数，异常值不处理。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**示例：**

```typescript
await mapPolyline.setCustomTextureIndexes([0,1,0]);
```

### addLineText

addLineText(lineText: mapCommon.LineText): void

添加折线的线条文本。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 26.0.0

**参数：**

| 参数名 | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| lineText | [mapCommon.LineText](map-common.md#linetext) | 是 | 折线的线条文本参数，异常值作为无响应处理。 |

**示例：**

```typescript
let textLine: mapCommon.LineText = {
  lineNames: ['第一段文字', '第二段文字'],
  lineNameIndexes: [0, 1, 1, 2],
  nameOnRight: false,
  color: 0xFF000000,
  fontSize: 15,
  strokeColor: 0xFFFFFFFF,
  fontStyle: 0
};
mapPolyline.addLineText(textLine);
```

### removeLineText

removeLineText(): void

删除折线的文本。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 26.0.0

**示例：**

```typescript
mapPolyline.removeLineText();
```
