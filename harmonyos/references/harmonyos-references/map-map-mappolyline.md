---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-map-mappolyline
title: MapPolyline
breadcrumb: API参考 > 应用服务 > Map Kit（地图服务） > ArkTS API > map（地图显示功能） > MapPolyline
category: harmonyos-references
scraped_at: 2026-04-28T08:17:11+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:fed5b30e96aa84ed58e146023708e25155e8cf06aad1cd6d0a81115cfe6e8473
---

## 导入模块

PhonePC/2in1TabletWearable

```
1. import { map, mapCommon } from '@kit.MapKit';
```

## MapPolyline

PhonePC/2in1TabletWearable

折线，继承[BaseOverlay](map-map-baseoverlay.md)。在调用map.[MapComponentController](map-map-mapcomponentcontroller.md)类的[addPolyline](map-map-mapcomponentcontroller.md#addpolyline)方法时会返回该类型的实例。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**示例：**

```
1. import { image } from '@kit.ImageKit';

3. // 数组存放图片内容
4. let customTextures: Array<ResourceStr | image.PixelMap> = new Array();
5. // 图标存放在resources/rawfile目录下
6. customTextures.push('icon/img.png');
7. customTextures.push('icon/img_1.png');
8. let cusIndexNumber: Array<number> = new Array();
9. // cusIndexNumber数组长度与折线点数量必须相同，数组元素内容与customTextures下标相对应，图片从数组第二个元素开始选择
10. cusIndexNumber.push(0, 0, 1);
11. let polylineOption: mapCommon.MapPolylineOptions = {
12. points: [
13. { latitude: 31.68, longitude: 118.166 },
14. { latitude: 31.48, longitude: 118.366 },
15. { latitude: 31.28, longitude: 118.766 }
16. ],
17. customTextures: customTextures,
18. customTextureIndexes: cusIndexNumber
19. };
20. let mapPolyline = await this.mapController.addPolyline(polylineOption);
```

### getColor

PhonePC/2in1TabletWearable

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

```
1. let color: number = mapPolyline.getColor();
```

### getColors

PhonePC/2in1TabletWearable

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

```
1. let colors: Array<number> = mapPolyline.getColors();
```

### getEndCap

PhonePC/2in1TabletWearable

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

```
1. let endCap: mapCommon.CapStyle = mapPolyline.getEndCap();
```

### getJointType

PhonePC/2in1TabletWearable

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

```
1. let jointType: mapCommon.JointType = mapPolyline.getJointType();
```

### getPatterns

PhonePC/2in1TabletWearable

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

```
1. let patterns: Array<mapCommon.PatternItem> = mapPolyline.getPatterns();
```

### getPoints

PhonePC/2in1TabletWearable

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

```
1. let points: Array<mapCommon.LatLng> = mapPolyline.getPoints();
```

### getStartCap

PhonePC/2in1TabletWearable

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

```
1. let startCap: mapCommon.CapStyle = mapPolyline.getStartCap();
```

### getWidth

PhonePC/2in1TabletWearable

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

```
1. let width: number = mapPolyline.getWidth();
```

### isClickable

PhonePC/2in1TabletWearable

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

```
1. let isClickable: boolean = mapPolyline.isClickable();
```

### isGeodesic

PhonePC/2in1TabletWearable

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

```
1. let isGeodesic: boolean = mapPolyline.isGeodesic();
```

### isGradient

PhonePC/2in1TabletWearable

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

```
1. let isGradient: boolean = mapPolyline.isGradient();
```

### setClickable

PhonePC/2in1TabletWearable

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

```
1. mapPolyline.setClickable(true);
```

### setColor

PhonePC/2in1TabletWearable

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

```
1. mapPolyline.setColor(0xff000000);
```

### setColors

PhonePC/2in1TabletWearable

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

```
1. mapPolyline.setColors([0xffffff00, 0xff000000]);
```

### setEndCap

PhonePC/2in1TabletWearable

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

```
1. mapPolyline.setEndCap(mapCommon.CapStyle.BUTT);
```

### setGeodesic

PhonePC/2in1TabletWearable

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

```
1. mapPolyline.setGeodesic(true);
```

### setGradient

PhonePC/2in1TabletWearable

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

```
1. mapPolyline.setGradient(true);
```

### setJointType

PhonePC/2in1TabletWearable

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

```
1. mapPolyline.setJointType(mapCommon.JointType.DEFAULT);
```

### setPatterns

PhonePC/2in1TabletWearable

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

```
1. let linePattern: Array<mapCommon.PatternItem> = [
2. { type: mapCommon.PatternItemType.DASH, length: 100 },
3. { type: mapCommon.PatternItemType.DOT, length: 100 },
4. { type: mapCommon.PatternItemType.GAP, length: 100 }
5. ];
6. mapPolyline.setPatterns(linePattern);
```

### setPoints

PhonePC/2in1TabletWearable

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

```
1. let points: Array<mapCommon.LatLng> = [
2. { latitude: 31.18, longitude: 118.766 },
3. { latitude: 31.38, longitude: 118.366 },
4. { latitude: 31.68, longitude: 118.566 },
5. { latitude: 31.98, longitude: 118.266 },
6. { latitude: 31.88, longitude: 118.866 }
7. ];
8. mapPolyline.setPoints(points);
```

### setStartCap

PhonePC/2in1TabletWearable

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

```
1. mapPolyline.setStartCap(mapCommon.CapStyle.BUTT);
```

### setWidth

PhonePC/2in1TabletWearable

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

```
1. mapPolyline.setWidth(20);
```

### setCustomTexture

PhonePC/2in1TabletWearable

setCustomTexture(customTexture: ResourceStr | image.PixelMap): Promise<void>

设置折线纹理。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| customTexture | [ResourceStr](ts-types.md#resourcestr) | [image.PixelMap](arkts-apis-image-pixelmap.md) | 是 | 折线纹理。建议纹理使用没有背景色（透明色）的图片。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象，异常值不处理。 |

**示例：**

```
1. // 图标存放在resources/rawfile目录下
2. await mapPolyline.setCustomTexture("icon/naviline_arrow.png");
```

### setCustomTexture

PhonePC/2in1TabletWearable

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

```
1. // 图标需存放在resources/rawfile目录下
2. await mapPolyline.setCustomTexture("icon/naviline_arrow.png", true);
```

### setCustomTextureIndexes

PhonePC/2in1TabletWearable

setCustomTextureIndexes(customTextureIndexes: number[]): Promise<void>

动态设置自定义纹理索引。折线设置纹理后，该接口可以将已有的纹理资源动态应用在各个折线段上。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.3(15)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.3(15)

**参数：**

| 参数名 | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| customTextureIndexes | number[] | 是 | 每个坐标对应的纹理索引。数组长度需要和points的数量保持一致，异常值不处理。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-map.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid input parameter. |

**示例：**

```
1. await mapPolyline.setCustomTextureIndexes([0,1,0]);
```
