---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-map-marker
title: Marker
breadcrumb: API参考 > 应用服务 > Map Kit（地图服务） > ArkTS API > map（地图显示功能） > Marker
category: harmonyos-references
scraped_at: 2026-04-29T14:07:54+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:878b8d1b54b8ca85b9317902a908a2729fd49e96bfc5ac3bb717d9ffb4c06367
---

## 导入模块

PhonePC/2in1TabletWearable

```
1. import { map, mapCommon } from '@kit.MapKit';
```

## Marker

PhonePC/2in1TabletWearable

标记，继承[BaseOverlay](map-map-baseoverlay.md)。在调用map.[MapComponentController](map-map-mapcomponentcontroller.md)类的[addMarker](map-map-mapcomponentcontroller.md#addmarker)方法时会返回该类型的实例。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**示例：**

```
1. let markerOptions: mapCommon.MarkerOptions = {
2. position: {
3. latitude: 39.9,
4. longitude: 116.4
5. }
6. };
7. let marker: map.Marker = await this.mapController.addMarker(markerOptions);
```

### getTitle

PhonePC/2in1TabletWearable

getTitle(): string

返回信息窗的标题。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 信息窗的标题。 |

**示例：**

```
1. let title: string = marker.getTitle();
```

### getSnippet

PhonePC/2in1TabletWearable

getSnippet(): string

返回信息窗的子标题。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 信息窗的子标题。 |

**示例：**

```
1. let snippet: string = marker.getSnippet();
```

### getAlpha

PhonePC/2in1TabletWearable

getAlpha(): number

获取标记的透明度。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 标记的透明度，取值范围：[0, 1]。 |

**示例：**

```
1. let alpha: number = marker.getAlpha();
```

### getPosition

PhonePC/2in1TabletWearable

getPosition(): mapCommon.LatLng

获取标记的位置。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [mapCommon.LatLng](map-common.md#latlng) | 标记的位置。 |

**示例：**

```
1. let position: mapCommon.LatLng = marker.getPosition();
```

### getRotation

PhonePC/2in1TabletWearable

getRotation(): number

获取标记的旋转角度。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 标记的旋转角度，单位：度。 |

**示例：**

```
1. let rotation: number = marker.getRotation();
```

### isClickable

PhonePC/2in1TabletWearable

isClickable(): boolean

获取标记是否可以点击。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 标记是否可以点击。  - true：可以  - false：不可以 |

**示例：**

```
1. let isClickable: boolean = marker.isClickable();
```

### isDraggable

PhonePC/2in1TabletWearable

isDraggable(): boolean

获取标记是否可以通过长按来拖拽。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 标记是否可以通过长按来拖拽。  - true：可以  - false：不可以 |

**示例：**

```
1. let isDraggable: boolean = marker.isDraggable();
```

### isFlat

PhonePC/2in1TabletWearable

isFlat(): boolean

获取标记是否平贴地图。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 标记是否平贴地图。  - true：平贴地图  - false：面对相机 |

**示例：**

```
1. let isFlat: boolean = marker.isFlat();
```

### setAlpha

PhonePC/2in1TabletWearable

setAlpha(alpha: number): void

设置标记的透明度属性。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| 参数名 | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| alpha | number | 是 | 标记的透明度，取值范围：[0, 1]，异常值不处理。  0：完全透明  1：完全不透明 |

**示例：**

```
1. marker.setAlpha(0.5);
```

### setClickable

PhonePC/2in1TabletWearable

setClickable(clickable: boolean): void

设置标记是否可以点击。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| 参数名 | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| clickable | boolean | 是 | 设置标记是否可以点击，异常值不处理。  - true：可以  - false：不可以 |

**示例：**

```
1. marker.setClickable(true);
```

### setDraggable

PhonePC/2in1TabletWearable

setDraggable(draggable: boolean): void

设置标记是否可以长按拖拽。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| 参数名 | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| draggable | boolean | 是 | 是否可以长按拖拽，异常值不处理。  - true：可以  - false：不可以 |

**示例：**

```
1. marker.setDraggable(true);
```

### setFlat

PhonePC/2in1TabletWearable

setFlat(flat: boolean): void

设置标记是否平贴地图。如果标记平贴地图，则在相机旋转和倾斜时，标记仍将停留在地图上，它将保持与照相机缩放时相同的大小。 如果标记面对相机，它将始终面向相机绘制，并随相机旋转和倾斜。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| 参数名 | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| flat | boolean | 是 | 是否平贴地图，异常值不处理。  - true：平贴地图  - false：面对相机 |

**示例：**

```
1. marker.setFlat(true);
```

### setIcon

PhonePC/2in1TabletWearable

setIcon(icon: string | image.PixelMap | Resource): Promise<void>

设置标记的图标。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| 参数名 | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| icon | string | [image.PixelMap](arkts-apis-image-pixelmap.md) | [Resource](ts-types.md#resource) | 是 | 标记的图标，异常值不处理。  - 图片格式支持jpg、jpeg、png、gif、webp、svg。  - string类型入参支持两种格式：  - 资源相对路径格式：图标存放在resources/rawfile，icon参数传入rawfile文件夹下的相对路径。  - toDataURL格式（如data:image/png;base64,<图片的Base64字节编码值>）  **说明：**  从5.0.0(12)版本开始，icon属性支持[Resource](ts-types.md#resource)和[image.PixelMap](arkts-apis-image-pixelmap.md)类型。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**示例：**

```
1. // 图标需存放在resources/rawfile目录下
2. await marker.setIcon('icon/test.png');
```

### setMarkerAnchor

PhonePC/2in1TabletWearable

setMarkerAnchor(anchorU: number, anchorV: number): void

设置标记的锚点位置。锚点是标记图标接触地图平面的点，图标的左顶点为（0, 0）点，右顶点为（1, 0）点，左底点为（0, 1）点，右底点为（1, 1）点。例如，在标记X（0.5, 0.3）处的锚点坐标如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/apgSao7SRLu-h4kw0aBARg/zh-cn_image_0000002558607768.png?HW-CC-KV=V1&HW-CC-Date=20260429T060752Z&HW-CC-Expire=86400&HW-CC-Sign=E03C18402698AAFA2CE7DAE475C5C773BF6CA5A58E73430E5EFE592014E808F4)

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| 参数名 | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| anchorU | number | 是 | 锚点的水平坐标，以图像宽度的比例，取值范围：[0, 1]，异常值不处理。 |
| anchorV | number | 是 | 锚点的垂直坐标，以图像高度的比例，取值范围：[0, 1]，异常值不处理。 |

**示例：**

```
1. marker.setMarkerAnchor(1.0, 1.0);
```

### setPosition

PhonePC/2in1TabletWearable

setPosition(latLng: mapCommon.LatLng): void

设置标记的位置坐标。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| 参数名 | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| latLng | [mapCommon.LatLng](map-common.md#latlng) | 是 | 标记的位置坐标，异常值不处理。 |

**示例：**

```
1. let position: mapCommon.LatLng = {
2. latitude: 39.9,
3. longitude: 116.4
4. };
5. marker.setPosition(position);
```

### setRotation

PhonePC/2in1TabletWearable

setRotation(rotation: number): void

设置标记的旋转角度，即标记围绕标记锚点顺时针旋转的角度，旋转轴垂直于标记。默认旋转角度为0，默认位置为北对齐。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| 参数名 | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| rotation | number | 是 | 标记的旋转角度，单位：度。  以正北方向为0度、顺时针方向为正的角度，取值范围：[0, 360)。超出取值范围的值会换算成取值范围内的值，比如361会被换算成1，-1换算为359，null和undefind不处理。 |

**示例：**

```
1. marker.setRotation(30);
```

### setTitle

PhonePC/2in1TabletWearable

setTitle(title: string): void

设置信息窗的标题。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| 参数名 | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| title | string | 是 | 信息窗口的标题，超长字串超出部分用省略号“…”表示，异常值不处理。 |

**示例：**

```
1. marker.setTitle("title");
```

### setSnippet

PhonePC/2in1TabletWearable

setSnippet(snippet: string): void

设置信息窗口的子标题。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| 参数名 | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| snippet | string | 是 | 信息窗口的子标题，超长字串超出部分用省略号“…”表示，异常值不处理。 |

**示例：**

```
1. marker.setSnippet("su");
```

### setInfoWindowAnchor

PhonePC/2in1TabletWearable

setInfoWindowAnchor(anchorU: number, anchorV: number): void

设置信息窗的锚点位置。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| 参数名 | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| anchorU | number | 是 | 锚点在水平方向上的位置，取值范围：[0, 1]，异常值不处理。 |
| anchorV | number | 是 | 锚点在垂直方向上的位置，取值范围：[0, 1]，异常值不处理。 |

**示例：**

```
1. marker.setInfoWindowAnchor(0.5, 0.5);
```

### setInfoWindowVisible

PhonePC/2in1TabletWearable

setInfoWindowVisible(visible: boolean): void

设置信息窗是否可见。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| 参数名 | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| visible | boolean | 是 | 设置信息窗是否可见，异常值不处理。  - true：可见  - false：不可见 |

**示例：**

```
1. marker.setInfoWindowVisible(true);
```

### isInfoWindowVisible

PhonePC/2in1TabletWearable

isInfoWindowVisible(): boolean

返回信息窗是否可见。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**返回值：**

| **类型** | **说明** |
| --- | --- |
| boolean | 信息窗口是否可见。  - true：可见  - false：不可见 |

**示例：**

```
1. let visible: boolean = marker.isInfoWindowVisible();
```

### setAnimation

PhonePC/2in1TabletWearable

setAnimation(animation: Animation): void

设置标记的动画，不支持[FontSizeAnimation](map-map-fontsizeanimation.md)。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| 参数名 | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| animation | [Animation](map-map-animation.md) | 是 | 动画，异常值不处理。 |

**示例：**

```
1. let animation: map.AlphaAnimation = new map.AlphaAnimation(0.2, 1);
2. animation.setDuration(3000);
3. let callbackStart = () => {
4. console.info("animationStart", `callback`);
5. };
6. let callbackEnd = () => {
7. console.info("animationEnd", `callback`);
8. };
9. animation.on("animationStart", callbackStart);
10. animation.on("animationEnd", callbackEnd);
11. animation.setFillMode(map.AnimationFillMode.BACKWARDS);
12. animation.setRepeatMode(map.AnimationRepeatMode.RESTART);
13. animation.setRepeatCount(100);

15. marker.setAnimation(animation);
```

### startAnimation

PhonePC/2in1TabletWearable

startAnimation(): void

启动标记的动画。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**示例：**

```
1. let animation: map.AlphaAnimation = new map.AlphaAnimation(0.2, 1);
2. animation.setDuration(3000);
3. let callbackStart = () => {
4. console.info("animationStart", `callback`);
5. };
6. let callbackEnd = () => {
7. console.info("animationEnd", `callback`);
8. };
9. animation.on("animationStart", callbackStart);
10. animation.on("animationEnd", callbackEnd);
11. animation.setFillMode(map.AnimationFillMode.BACKWARDS);
12. animation.setRepeatMode(map.AnimationRepeatMode.RESTART);
13. animation.setRepeatCount(100);

15. marker.setAnimation(animation);
16. marker.startAnimation();
```

### clearAnimation

PhonePC/2in1TabletWearable

clearAnimation(): void

清除标记的动画。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**示例：**

```
1. marker.clearAnimation();
```

### getAltitude

PhonePC/2in1TabletWearable

getAltitude(): number

获取海拔高度。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 海拔高度，单位：米。 |

**示例：**

```
1. let altitude: number = marker.getAltitude();
```

### setAltitude

PhonePC/2in1TabletWearable

setAltitude(altitude: number): void

设置海拔高度。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| altitude | number | 是 | 海拔高度，单位：米，异常值不处理。 |

**示例：**

```
1. marker.setAltitude(500);
```

### setAnnotationVisible

PhonePC/2in1TabletWearable

setAnnotationVisible(visible: boolean): void

设置标记是否显示文本。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.1.1(19)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.1.1(19)

**参数：**

| 参数名 | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| visible | boolean | 是 | 标记是否显示文本，异常值不处理。  - true：显示  - false：不显示 |

**示例：**

```
1. marker.setAnnotationVisible(true);
```

### isAnnotationVisible

PhonePC/2in1TabletWearable

isAnnotationVisible(): boolean

返回标记文本是否可见。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.1.1(19)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.1.1(19)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 标记文本是否可见。  - true：可见  - false：不可见 |

**示例：**

```
1. let isVisible = marker.isAnnotationVisible();
```

### setPriority

PhonePC/2in1TabletWearable

setPriority(priority: number): void

设置标记碰撞优先级。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本6.1.0(23)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 6.1.0(23)

**参数：**

| 参数名 | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| priority | number | 是 | 设置标记的碰撞优先级。数值越大，优先级越低，两个标记（Marker）碰撞时优先级低的标记（Marker）被隐藏。该值为整数，取值范围：[0, 65535]，超出范围不处理，异常值不处理。 |

**示例：**

```
1. marker.setPriority(50);
```

### getPriority

PhonePC/2in1TabletWearable

getPriority(): number

获取标记冲突优先级。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本6.1.0(23)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 6.1.0(23)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 标记的碰撞优先级。数值越大，优先级越低，两个标记（Marker）碰撞时优先级低的标记（Marker）被隐藏。 |

**示例：**

```
1. let priority: number = marker.getPriority();
```

### setIconBuilder

PhonePC/2in1TabletWearable

setIconBuilder(iconBuilder: CustomBuilder): Promise<void>

设置生成标记图标的自定义组件。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 6.0.0(20)

**参数：**

| 参数名 | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| iconBuilder | [CustomBuilder](ts-types.md#custombuilder8) | 是 | 自定义组件，异常值不处理。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-map.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1002601005 | Failed to generate the icon of the custom component. |

**示例：**

```
1. @Builder
2. renderBuilder() {
3. Stack({ alignContent: Alignment.Center }) {
4. Text('Test Icon Builder')
5. }
6. .height(50)
7. .width(200)
8. }
9. // 设置自定义组件
10. try {
11. await this.marker?.setIconBuilder(() => {
12. this.renderBuilder();
13. })
14. } catch (error) {
15. let err = error as BusinessError;
16. console.error('Marker icon builder test error code' + err.code + 'message:' + err.message);
17. }
```

### setOffset

PhonePC/2in1TabletWearable

setOffset(x: number, y: number): void

设置标记图标的偏移量。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本6.0.2(22)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 6.0.2(22)

**参数：**

| 参数名 | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| x | number | 是 | X轴方向的偏移量，单位：px，原点是图标的中心点，null、undefined和NaN不处理。 |
| y | number | 是 | Y轴方向的偏移量，单位：px，原点是图标的中心点，null、undefined和NaN不处理。 |

**示例：**

```
1. marker.setOffset(20,20);
```

### getOffsetX

PhonePC/2in1TabletWearable

getOffsetX(): number

获取标记图标在X轴方向的偏移量。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本6.0.2(22)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 6.0.2(22)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 获取标记图标在X轴方向的偏移量，单位：px，原点是图标的中心点。 |

**示例：**

```
1. let X: number = marker.getOffsetX();
```

### getOffsetY

PhonePC/2in1TabletWearable

getOffsetY(): number

获取标记图标在Y轴方向的偏移量。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本6.0.2(22)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 6.0.2(22)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 获取标记图标在Y轴方向的偏移量，单位：px，原点是图标的中心点，异常值不处理。 |

**示例：**

```
1. let Y: number = marker.getOffsetY();
```
