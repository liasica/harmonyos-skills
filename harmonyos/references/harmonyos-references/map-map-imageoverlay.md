---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-map-imageoverlay
title: ImageOverlay
breadcrumb: API参考 > 应用服务 > Map Kit（地图服务） > ArkTS API > map（地图显示功能） > ImageOverlay
category: harmonyos-references
scraped_at: 2026-04-28T08:17:17+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:f7b340bb233a87c329aed6880b56065fc4599e190840beab5b5b63370312f78b
---

## 导入模块

PhonePC/2in1TabletWearable

```
1. import { mapCommon } from '@kit.MapKit';
```

## ImageOverlay

PhonePC/2in1TabletWearable

图片覆盖物。继承[BaseOverlay](map-map-baseoverlay.md)。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

**示例：**

```
1. let imageOverlayParams: mapCommon.ImageOverlayParams = {
2. bounds: {
3. southwest: { latitude: 32, longitude: 118 },
4. northeast: { latitude: 32.4, longitude: 118.4 }
5. },
6. // 图标需存放在resources/rawfile目录下
7. image: 'icon.png',
8. transparency: 0.3,
9. zIndex: 101,
10. anchorU: 0.5,
11. anchorV: 0.5,
12. clickable: true,
13. visible: true,
14. bearing: 0
15. };
16. let imageOverlay = await this.mapController.addImageOverlay(imageOverlayParams);
17. imageOverlay.setBearing(180);
18. let bearing: number = imageOverlay.getBearing();
```

### getBearing

PhonePC/2in1TabletWearable

getBearing(): number

获取覆盖物的旋转角度。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回覆盖物的旋转角度，单位：度。 |

**示例：**

```
1. let bearing: number = imageOverlay.getBearing();
```

### getBounds

PhonePC/2in1TabletWearable

getBounds(): mapCommon.LatLngBounds

获取覆盖物的矩形区域。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [mapCommon.LatLngBounds](map-common.md#latlngbounds) | 获取覆盖物的矩形区域。 |

**示例：**

```
1. let bounds: mapCommon.LatLngBounds = imageOverlay.getBounds();
```

### getHeight

PhonePC/2in1TabletWearable

getHeight(): number

获取覆盖物的高度。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 覆盖物的高度，单位：米。 |

**示例：**

```
1. let height: number = imageOverlay.getHeight();
```

### getWidth

PhonePC/2in1TabletWearable

getWidth(): number

获取覆盖物的宽度。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 覆盖物的宽度，单位：米。 |

**示例：**

```
1. let width: number = imageOverlay.getWidth();
```

### getPosition

PhonePC/2in1TabletWearable

getPosition(): mapCommon.LatLng

获取覆盖物的位置。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [mapCommon.LatLng](map-common.md#latlng) | 覆盖物的位置。 |

**示例：**

```
1. let position: mapCommon.LatLng = imageOverlay.getPosition();
```

### getTransparency

PhonePC/2in1TabletWearable

getTransparency(): number

获取覆盖物的透明度。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 覆盖物的透明度。取值范围：[0, 1]。0表示不透明，1表示全透明。 |

**示例：**

```
1. let transparency: number = imageOverlay.getTransparency();
```

### isClickable

PhonePC/2in1TabletWearable

isClickable(): boolean

获取是否可点击。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 是否可点击。  - true：可点击  - false：不可点击 |

**示例：**

```
1. let click: boolean = imageOverlay.isClickable();
```

### setBearing

PhonePC/2in1TabletWearable

setBearing(bearing: number): void

设置覆盖物的旋转角度。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

**参数**：

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| bearing | number | 是 | 覆盖物的旋转角度，单位：度。  以正北方向为0度、顺时针方向为正的角度，默认值为0，取值范围：[0, 360)。超出取值范围的值会换算成取值范围内的值，比如361会被换算成1，-1换算为359。 |

**示例：**

```
1. imageOverlay.setBearing(180);
```

### setClickable

PhonePC/2in1TabletWearable

setClickable(clickable: boolean): void

设置是否开启可点击开关。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

**参数**：

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| clickable | boolean | 是 | 是否开启可点击开关。  - true：开启  - false：不开启 |

**示例：**

```
1. imageOverlay.setClickable(false);
```

### setDimensions

PhonePC/2in1TabletWearable

setDimensions(width: number, height?: number): void

设置覆盖物的宽度和高度。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

**参数**：

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| width | number | 是 | 宽度，width为正整数，单位：米，异常值不处理。 |
| height | number | 否 | 高度，height为正整数，单位：米，异常值不处理。若不设置高度，则以覆盖物图片默认宽高比例显示高度。 |

**示例：**

```
1. imageOverlay.setDimensions(100000, 100000);
```

### setImage

PhonePC/2in1TabletWearable

setImage(image: ResourceStr | image.PixelMap): Promise<void>

设置覆盖物的图像。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

**参数**：

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| image | [ResourceStr](ts-types.md#resourcestr) | [image.PixelMap](arkts-apis-image-pixelmap.md) | 是 | 覆盖物的图像。  图片格式支持jpg、jpeg、png、gif、webp、svg。  **说明：**  [ResourceStr](ts-types.md#resourcestr)为Resource和string两种格式，其中string类型入参支持两种格式：  - 资源相对路径格式：图标存放在resources/rawfile，image参数传入rawfile文件夹下的相对路径。  - toDataURL格式（如data:image/png;base64,<图片的Base64字节编码值>）。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**示例：**

```
1. // 图标需存放在resources/rawfile目录下
2. await imageOverlay.setImage("icon.png");
```

### setBounds

PhonePC/2in1TabletWearable

setBounds(bounds: mapCommon.LatLngBounds): void

设置覆盖物的矩形区域。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

**参数**：

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| bounds | [mapCommon.LatLngBounds](map-common.md#latlngbounds) | 是 | 覆盖物的矩形区域。 |

**示例：**

```
1. let bounds: mapCommon.LatLngBounds = {
2. southwest: { longitude: 118, latitude: 31 },
3. northeast: { longitude: 119, latitude: 32 }
4. };
5. imageOverlay.setBounds(bounds);
```

### setPosition

PhonePC/2in1TabletWearable

setPosition(position: mapCommon.LatLng): void

设置覆盖物的位置。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

**参数**：

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| position | [mapCommon.LatLng](map-common.md#latlng) | 是 | 覆盖物的位置。 |

**示例：**

```
1. let position: mapCommon.LatLng = { longitude: 118, latitude: 31 };
2. imageOverlay.setPosition(position);
```

### setTransparency

PhonePC/2in1TabletWearable

setTransparency(transparency: number): void

设置覆盖物的透明度。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

**参数**：

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| transparency | number | 是 | 覆盖物的透明度。取值范围：[0, 1]。0表示不透明，1表示全透明。异常值不生效。 |

**示例：**

```
1. imageOverlay.setTransparency(0.1);
```
