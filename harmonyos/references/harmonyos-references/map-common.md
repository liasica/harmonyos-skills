---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-common
title: mapCommon（地图属性模型）
breadcrumb: API参考 > 应用服务 > Map Kit（地图服务） > ArkTS API > mapCommon（地图属性模型）
category: harmonyos-references
scraped_at: 2026-04-28T08:17:25+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:fb54e3c60b47c82773c15b199748620ee5406dffa636acad04b05adf21cc84aa
---

本模块提供map组件相关属性设置接口。

**起始版本：** 4.1.0(11)

## 导入模块

PhonePC/2in1TabletWearable

```
1. import { mapCommon } from '@kit.MapKit';
```

## MapOptions

PhonePC/2in1TabletWearable

提供Map组件初始化的属性。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| mapType | [MapType](map-common.md#maptype) | 否 | 是 | 地图类型，默认值为[MapType](map-common.md#maptype).STANDARD，异常值按默认值处理。  **元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。 |
| position | [CameraPosition](map-common.md#cameraposition) | 否 | 否 | 地图相机位置。  **元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。 |
| bounds | [LatLngBounds](map-common.md#latlngbounds) | 否 | 是 | 地图展示边界，异常值根据无边界处理。  **元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。  **说明：**  西南角纬度不能大于东北角纬度。 |
| minZoom | number | 否 | 是 | 地图最小层级，有效范围：[2, 20]，默认值为2，异常值按默认值处理。  如果设置的最小缩放级别小于2，minZoom会取2。  **元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。 |
| maxZoom | number | 否 | 是 | 地图最大层级，有效范围：[2, 20]，默认值为20，异常值按默认值处理。  如果设置的最大缩放级别大于20，maxZoom会取20。  **元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。 |
| rotateGesturesEnabled | boolean | 否 | 是 | 是否支持旋转手势，默认值为true，异常值按默认值处理。  - true：支持  - false：不支持  **元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。 |
| scrollGesturesEnabled | boolean | 否 | 是 | 是否支持滑动手势，默认值为true，异常值按默认值处理。  - true：支持  - false：不支持  **元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。 |
| zoomGesturesEnabled | boolean | 否 | 是 | 是否支持缩放手势，默认值为true，异常值按默认值处理。  - true：支持  - false：不支持  **元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。 |
| tiltGesturesEnabled | boolean | 否 | 是 | 是否支持倾斜手势，默认值为true，异常值按默认值处理。  - true：支持  - false：不支持  **元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。 |
| zoomControlsEnabled | boolean | 否 | 是 | 是否展示缩放控件，默认值为true，异常值按默认值处理。  - true：展示  - false：不展示  **元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。 |
| myLocationControlsEnabled | boolean | 否 | 是 | 是否展示我的位置按钮，默认值为false，异常值按默认值处理。  - true：展示  - false：不展示  **元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。 |
| compassControlsEnabled | boolean | 否 | 是 | 是否展示指南针控件，默认值为true，异常值按默认值处理。  - true：展示  - false：不展示  **元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。 |
| scaleControlsEnabled | boolean | 否 | 是 | 是否展示比例尺，默认值为false，异常值按默认值处理。  - true：展示  - false：不展示  **元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。 |
| padding | [Padding](map-common.md#padding) | 否 | 是 | 设置地图和边界的距离，默认值为{ left: 0 , top: 0 , right: 0 , bottom: 0 }。  **元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。 |
| styleId | string | 否 | 是 | 自定义样式ID。ID不生效时，使用系统样式。使用方式详见[显示自定义地图](../harmonyos-guides/map-style.md)章节。  **起始版本：** 5.0.0(12)  **元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。 |
| dayNightMode | [DayNightMode](map-common.md#daynightmode) | 否 | 是 | 日间夜间模式，默认值为[DayNightMode](map-common.md#daynightmode).DAY（日间模式）。  **起始版本：** 5.0.0(12)  **元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。 |
| alwaysShowScaleEnabled | boolean | 否 | 是 | 是否一直显示比例尺，只有比例尺启用时该参数才生效。启用比例尺可以由地图初始化时scaleControlsEnabled属性设置为true或者通过[setScaleControlsEnabled](map-map-mapcomponentcontroller.md#setscalecontrolsenabled)方法设置为true。  - true：始终显示  - false：关闭始终显示  默认是false。  **起始版本：** 5.0.0(12)  **元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。 |
| logoScale | number | 否 | 是 | Logo缩放比例，取值范围是[0.8, 1]，默认值是1，异常值按默认值处理。  **起始版本：** 5.0.3(15)  **元服务API：** 从版本5.0.3(15)开始，该接口支持在元服务中使用。 |
| sphereEnabled | boolean | 否 | 是 | 是否开启3D地球效果，默认值为false。  - true：开启3D地球效果  - false：关闭3D地球效果  **起始版本：** 5.0.3(15)  **元服务API：** 从版本5.0.3(15)开始，该接口支持在元服务中使用。 |
| indoorMapEnabled | boolean | 否 | 是 | 是否启用室内图，默认值为false。  - true：开启室内图  - false：关闭室内图  **起始版本：** 5.1.1(19)  **元服务API：** 从版本5.1.1(19)开始，该接口支持在元服务中使用。 |
| scaleUnit | [ScaleUnit](map-common.md#scaleunit) | 否 | 是 | 地图比例尺单位，默认值为[ScaleUnit](map-common.md#scaleunit).METRIC\_UNIT（公制单位）。  **起始版本：** 5.1.1(19)  **元服务API：** 从版本5.1.1(19)开始，该接口支持在元服务中使用。 |
| language | string | 否 | 是 | 地图语言。语种取值请参见[地图组件支持语言](../harmonyos-guides/map-language.md#地图组件支持语言)列表。默认使用当前系统语言。  **起始版本：** 6.0.0(20)  **元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。 |
| approveNumberEnabled | boolean | 否 | 是 | 是否显示审图号并附带logo，只有路由地在中国才会显示。  - true：显示审图号  - false：隐藏审图号  **起始版本：** 6.1.0(23)  **元服务API：** 从版本6.1.0(23)开始，该接口支持在元服务中使用。 |

**示例：**

```
1. // 地图初始化参数
2. let mapOptions: mapCommon.MapOptions = {
3. mapType: mapCommon.MapType.STANDARD,
4. position: {
5. target: {
6. latitude: 39.9,
7. longitude: 116.4
8. },
9. zoom: 10
10. },
11. bounds: {
12. northeast: {
13. latitude: 41.5,
14. longitude: 125.5
15. },
16. southwest: {
17. latitude: 37.5,
18. longitude: 108.5
19. }
20. },
21. maxZoom: 20,
22. minZoom: 2,
23. rotateGesturesEnabled: true,
24. scrollGesturesEnabled: true,
25. zoomGesturesEnabled: true,
26. zoomControlsEnabled: true,
27. myLocationControlsEnabled: false,
28. dayNightMode: mapCommon.DayNightMode.NIGHT,
29. scaleControlsEnabled: true,
30. alwaysShowScaleEnabled: true,
31. scaleUnit: mapCommon.ScaleUnit.METRIC_UNIT,
32. language: 'zh-Hans',
33. approveNumberEnabled: true
34. };
```

## LatLng

PhonePC/2in1TabletWearable

经纬度对象。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

| 名称 | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| latitude | number | 否 | 否 | 纬度，取值范围：[-90, 90]。 |
| longitude | number | 否 | 否 | 经度，取值范围：[-180, 180)。 |

**示例：**

```
1. let position: mapCommon.LatLng = {
2. latitude: 39.9,
3. longitude: 116.4
4. };
```

## CameraPosition

PhonePC/2in1TabletWearable

相机状态，包括位置、倾斜角、缩放级别等信息。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

| 名称 | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| target | [LatLng](map-common.md#latlng) | 否 | 否 | 地图中心位置的经纬度坐标。 |
| zoom | number | 否 | 否 | 屏幕中心附近的缩放级别，取值范围：[2, 20]，默认值为2。 |
| tilt | number | 否 | 是 | 相机的倾斜角度，即相机与垂直于地球表面的线的夹角，取值范围：[0, 75]，默认值为0。 |
| bearing | number | 否 | 是 | 地图旋转角度。  以正北方向为0度、顺时针方向为正的角度，默认值为0，取值范围：[0, 360)。超出取值范围的值会换算成取值范围内的值，比如361会被换算成1，-1换算为359。 |

**示例：**

```
1. let cameraPosition: mapCommon.CameraPosition = {
2. target: {
3. latitude: 39.9,
4. longitude: 116.4
5. },
6. zoom: 10,
7. tilt: 45,
8. bearing: 90
9. };
```

## LatLngBounds

PhonePC/2in1TabletWearable

经纬度划分的一个矩形区域。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

| 名称 | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| northeast | [LatLng](map-common.md#latlng) | 否 | 否 | 东北角经纬度。 |
| southwest | [LatLng](map-common.md#latlng) | 否 | 否 | 西南角经纬度。 |

**示例：**

```
1. let bounds: mapCommon.LatLngBounds = {
2. northeast: {
3. latitude: 41.5,
4. longitude: 125.5
5. },
6. southwest: {
7. latitude: 37.5,
8. longitude: 108.5
9. }
10. };
```

## PatternItem

PhonePC/2in1TabletWearable

圆、多边形或折线的边框样式。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

| 名称 | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| type | [PatternItemType](map-common.md#patternitemtype) | 否 | 否 | 边框样式类型。 |
| length | number | 否 | 是 | 边框样式类型为DASH或GAP时的边框长度，默认值为1，取值范围：大于等于0，单位：px。 |

**示例：**

```
1. let patternItem: mapCommon.PatternItem = {
2. type: mapCommon.PatternItemType.DASH,
3. length: 10
4. };
```

## MyLocationStyle

PhonePC/2in1TabletWearable

自定义定位样式。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

| 名称 | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| anchorU | number | 否 | 是 | 锚点横坐标方向的偏移量，建议取值[0, 1]，默认值为0.5。  **元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。 |
| anchorV | number | 否 | 是 | 锚点纵坐标方向的偏移量，建议取值[0, 1]，默认值为0.5。  **元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。 |
| icon | string | [image.PixelMap](arkts-apis-image-pixelmap.md) | [Resource](ts-types.md#resource) | 否 | 是 | 定位图标。  - 图片格式支持jpg、jpeg、png、gif、webp、svg。  - string类型入参支持两种格式：  - 资源相对路径格式：图标存放在resources/rawfile，icon参数传入rawfile文件夹下的相对路径。  - toDataURL格式（如data:image/png;base64,<图片的Base64字节编码值>）。  **说明：**  从5.0.0(12)版本开始，icon属性支持[image.PixelMap](arkts-apis-image-pixelmap.md)和[Resource](ts-types.md#resource)类型。  **元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。 |
| radiusFillColor | number | 否 | 是 | 定位图标填充色，默认值为0x8F7570FF（紫色），颜色值为ARGB格式。  **元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。 |
| displayType | [MyLocationDisplayType](map-common.md#mylocationdisplaytype) | 否 | 是 | 定位图标的展示样式，默认值为[MyLocationDisplayType](map-common.md#mylocationdisplaytype).DEFAULT。  **起始版本：** 5.0.0(12)  **元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。 |

**示例：**

```
1. let style: mapCommon.MyLocationStyle = {
2. anchorU: 0.5,
3. anchorV: 1,
4. radiusFillColor: 0xffff0000,
5. // 图标需存放在resources/rawfile目录下
6. icon: 'test.png',
7. displayType: mapCommon.MyLocationDisplayType.FOLLOW
8. };
```

## Poi

PhonePC/2in1TabletWearable

地图上的POI对象。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

| 名称 | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| id | string | 否 | 否 | POI的标识。 |
| name | string | 否 | 否 | POI的名称。 |
| position | [LatLng](map-common.md#latlng) | 否 | 否 | POI的经纬度位置。 |

**示例：**

```
1. let poi: mapCommon.Poi = {
2. id: "1001",
3. name: "城东烧烤店",
4. position: {
5. latitude: 39.6,
6. longitude: 116.4
7. }
8. };
```

## BaseOverlayOptions

PhonePC/2in1TabletWearable

定义覆盖物基本属性。[MarkerOptions](map-common.md#markeroptions)、[MapCircleOptions](map-common.md#mapcircleoptions)、[MapPolygonOptions](map-common.md#mappolygonoptions)、[MapPolylineOptions](map-common.md#mappolylineoptions)、[MapArcParams](map-common.md#maparcparams)、[ImageOverlayParams](map-common.md#imageoverlayparams)、[BasePriorityOverlayParams](map-common.md#basepriorityoverlayparams)等继承该基础类。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

| 名称 | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| visible | boolean | 否 | 是 | 是否可见，默认值为true，异常值按默认值处理。  - true：可见  - false：不可见 |
| zIndex | number | 否 | 是 | 覆盖物的叠加顺序，具有较大z指数的覆盖物会绘制在具有较小z指数的覆盖物上，具有相同z指数的叠加顺序为元素添加的先后顺序。覆盖物初始化时如果未设置zIndex参数，默认值为0。异常值按默认值处理。  **说明：**  [BasePriorityOverlayParams](map-common.md#basepriorityoverlayparams)的zIndex向下取整数。 |

## MarkerOptions

PhonePC/2in1TabletWearable

描述Marker属性，继承[BaseOverlayOptions](map-common.md#baseoverlayoptions)。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| position | [LatLng](map-common.md#latlng) | 否 | 否 | 标记的位置坐标。  **元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。 |
| rotation | number | 否 | 是 | 标记的旋转角度，单位：度。  以正北方向为0度、顺时针方向为正的角度，默认值为0，取值范围：[0, 360)。超出取值范围的值会换算成取值范围内的值，比如361会被换算成1，-1换算为359。  **元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。 |
| icon | string | [image.PixelMap](arkts-apis-image-pixelmap.md) | [Resource](ts-types.md#resource) | 否 | 是 | 图标，不传时显示默认图标。  - 图片格式支持jpg、jpeg、png、gif、webp、svg。  - string类型入参支持两种格式：  - 资源相对路径格式：图标存放在resources/rawfile，icon参数传入rawfile文件夹下的相对路径。  - toDataURL格式（如data:image/png;base64,<图片的Base64字节编码值>）。  **元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。  **说明：**  从5.0.0(12)版本开始，icon属性支持[image.PixelMap](arkts-apis-image-pixelmap.md)和[Resource](ts-types.md#resource)类型。 |
| alpha | number | 否 | 是 | 透明度，取值范围[0, 1]，0代表完全透明，1表示完全不透明，默认值为1，异常值按默认值处理。  **元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。 |
| anchorU | number | 否 | 是 | 锚点的水平坐标，以图像宽度的比例，建议取值[0, 1]，默认值为0.5，异常值按默认值处理。  **元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。 |
| anchorV | number | 否 | 是 | 锚点的垂直坐标，以图像高度的比例，建议取值[0, 1]，默认值为1，异常值按默认值处理。  **元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。 |
| clickable | boolean | 否 | 是 | 标记是否可以点击，默认值为false，异常值按默认值处理。  - true：可点击  - false：不可点击  **元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。 |
| draggable | boolean | 否 | 是 | 是否可以通过长按来拖拽，默认值为false，异常值按默认值处理。  - true：可拖拽  - false：不可拖拽  **元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。 |
| flat | boolean | 否 | 是 | 是否平贴地图，默认值为false，异常值按默认值处理。  - true：可平贴  - false：不可平贴  **元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。 |
| title | string | 否 | 是 | 信息窗口的标题，超长字串超出部分用省略号“...”表示。  **元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。 |
| snippet | string | 否 | 是 | 信息窗口的子标题，超长字串超出部分用省略号“...”表示。  **元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。 |
| infoWindowAnchorU | number | 否 | 是 | 指示标记信息窗口的锚点在水平方向上的位置。值范围：[0, 1]，默认值为0.5，异常值按默认值处理。  **元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。 |
| infoWindowAnchorV | number | 否 | 是 | 指示标记信息窗口的锚点在垂直方向上的位置。值范围：[0, 1]，默认值为0，异常值按默认值处理。  **元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。 |
| altitude | number | 否 | 是 | 海拔高度，单位：米，默认值为0，异常值按默认值处理。  **起始版本：** 5.0.0(12)  **元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。 |
| collisionRule | [CollisionRule](map-common.md#collisionrule) | 否 | 是 | 标记与地图POI之间的冲突处理规则，默认值为[CollisionRule](map-common.md#collisionrule).NONE。异常值按照默认值处理。  **说明：**  从5.0.3(15)版本开始，collisionRule属性支持CollisionRule.NONE和CollisionRule.ALL类型；从6.1.0(23)版本开始，collisionRule属性新增支持CollisionRule.NAME和CollisionRule.ICON\_CASCADE类型。  **起始版本：** 5.0.3(15)  **元服务API：** 从版本5.0.3(15)开始，该接口支持在元服务中使用。 |
| annotations | [Text](map-common.md#text)[] | 否 | 是 | 标记的注释，最小长度为1，最大长度为3。  **起始版本：** 5.0.3(15)  **元服务API：** 从版本5.0.3(15)开始，该接口支持在元服务中使用。 |
| showIcon | boolean | 否 | 是 | 是否显示标记的图标，默认值为true。根据显示的图标对异常值进行处理。  - true：显示标记的图标  - false：不显示标记的图标  **起始版本：** 5.0.3(15)  **元服务API：** 从版本5.0.3(15)开始，该接口支持在元服务中使用。 |
| annotationPosition | [TextPosition](map-common.md#textposition) | 否 | 是 | 注释相对于图标的位置，默认值为[TextPosition](map-common.md#textposition).DEFAULT。  **起始版本：** 5.0.3(15)  **元服务API：** 从版本5.0.3(15)开始，该接口支持在元服务中使用。 |
| iconBuilder | [CustomBuilder](ts-types.md#custombuilder8) | 否 | 是 | 用于生成标记图标的自定义组件。自定义组件的优先级高于图标属性。  **起始版本：** 6.0.0(20)  **元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用 |
| offsetX | number | 否 | 是 | 标记图标沿X轴的偏移量，X轴向右是正方向，原点是图标的中心点，单位：px。若只设置了一个offsetX，offsetY默认设置为0，异常值不处理。若设置offsetX则偏移量以offsetX为准，若未设置offsetX则偏移量以anchorU为准。  **起始版本：** 6.0.2(22)  **元服务API：** 从版本6.0.2(22)开始，该接口支持在元服务中使用 |
| offsetY | number | 否 | 是 | 标记图标沿Y轴的偏移量，Y轴向下是正方向，原点是图标的中心点，单位：px。若只设置了一个offsetY，offsetX默认设置为0，异常值不处理。若设置offsetY则偏移量以offsetY为准，若未设置offsetY则偏移量以anchorV为准。  **起始版本：** 6.0.2(22)  **元服务API：** 从版本6.0.2(22)开始，该接口支持在元服务中使用 |
| forceVisible | boolean | 否 | 是 | 碰撞后是否强制显示，默认值为false，异常值按默认值处理。  - true：碰撞后仍能显示  - false：碰撞后不强制显示  **起始版本：** 6.1.0(23)  **元服务API：** 从版本6.1.0(23)开始，该接口支持在元服务中使用。 |
| priority | number | 否 | 是 | 两个标记（Marker）碰撞时优先级低的标记（Marker）被隐藏，碰撞优先级，数值越大，优先级越低。该值为整数，取值范围：[0, 65535]。  当取值小于最小值时，按照取值范围的最小值处理；取值大于最大值时，按照取值范围的最大值处理。  当不配置或取值为null、undefined，默认为2147483647，即碰撞优先级最低。  **起始版本：** 6.1.0(23)  **元服务API：** 从版本6.1.0(23)开始，该接口支持在元服务中使用。 |
| minZoom | number | 否 | 是 | 展示的最小地图层级，默认值为2。最小层级不大于最大层级，不小于2，异常值按默认值处理。如果设置的最小缩放级别小于2，minZoom会取2。  **起始版本：** 6.1.0(23)  **元服务API：** 从版本6.1.0(23)开始，该接口支持在元服务中使用。 |
| maxZoom | number | 否 | 是 | 展示的最大地图层级，默认值为20。最大层级不大于20，不小于最小层级，异常值按默认值处理。如果设置的最大缩放级别大于20，maxZoom会取20。  **起始版本：** 6.1.0(23)  **元服务API：** 从版本6.1.0(23)开始，该接口支持在元服务中使用。 |

**示例：**

```
1. let markerOptions: mapCommon.MarkerOptions = {
2. position: {
3. latitude: 39.9,
4. longitude: 116.4
5. },
6. rotation: 0,
7. visible: true,
8. zIndex: 0,
9. alpha: 1,
10. anchorU: 0.5,
11. anchorV: 1,
12. clickable: true,
13. draggable: true,
14. flat: false,
15. // 图标需存放在resources/rawfile目录下
16. icon: 'test.png',
17. altitude: 100,
18. collisionRule: mapCommon.CollisionRule.ALL,
19. offsetX: 20,
20. offsetY: 20,
21. forceVisible: true,
22. priority: 5,
23. minZoom: 5,
24. maxZoom: 19
25. };
```

## MapCircleOptions

PhonePC/2in1TabletWearable

描述MapCircle属性，继承[BaseOverlayOptions](map-common.md#baseoverlayoptions)。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| center | [LatLng](map-common.md#latlng) | 否 | 否 | 圆的圆心，不能为空。圆的中心点纬度在[-85.051119, 85.051119]范围内才能画出圆。若圆中心点纬度为-85.051119或85.051119时，能画出半径为1米的圆。异常值不处理。 |
| radius | number | 否 | 否 | 圆的半径，单位：m，取值范围：大于等于0，默认值为0，异常值按默认值处理。 |
| clickable | boolean | 否 | 是 | 圆的可点击性，默认值为false，异常值按默认值处理。  - true：可点击  - false：不可点击 |
| fillColor | number | 否 | 是 | 圆的填充颜色，默认值为0x00000000（透明），颜色值为ARGB格式，异常值按默认值处理。 |
| strokeColor | number | 否 | 是 | 圆的边框颜色，默认值为0xff000000（黑色），颜色值为ARGB格式，异常值按默认值处理。 |
| patterns | Array<[PatternItem](map-common.md#patternitem)> | 否 | 是 | 圆的边框样式，默认值为空数组，异常值按默认值处理。 |
| strokeWidth | number | 否 | 是 | 圆的边框宽度，单位：px，默认值为10，取值范围：大于等于0，异常值按默认值处理。 |

**示例：**

```
1. let mapCircleOptions: mapCommon.MapCircleOptions = {
2. center: {
3. latitude: 39.9,
4. longitude: 116.4
5. },
6. radius: 5000,
7. clickable: true,
8. fillColor: 0XFF00FFFF,
9. strokeColor: 0xFFFF0000,
10. strokeWidth: 10,
11. visible: true,
12. zIndex: 15
13. };
```

## MapPolygonOptions

PhonePC/2in1TabletWearable

描述MapPolygon属性，继承[BaseOverlayOptions](map-common.md#baseoverlayoptions)。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| points | Array<[LatLng](map-common.md#latlng)> | 否 | 否 | 多边形的一组顶点，纬度取值范围：[-85.2, 85.2]，异常值不处理。 |
| holes | Array<Array<[LatLng](map-common.md#latlng)>> | 否 | 是 | 多边形的一组空心洞，默认值为空数组，异常值按默认值处理。  **说明：**  当空心洞的坐标贴合多边形边缘时，会导致渲染出现异常，渲染多余的空心区域。 |
| clickable | boolean | 否 | 是 | 多边形的可点击性，默认值为false，异常值按默认值处理。  - true：可点击  - false：不可点击 |
| fillColor | number | 否 | 是 | 多边形的填充颜色，默认值为0x00000000（透明），颜色值为ARGB格式，异常值按默认值处理。 |
| geodesic | boolean | 否 | 是 | 多边形的线段是否为大地曲线，默认值为false，异常值按默认值处理。  - true：大地曲线  - false：非大地曲线 |
| strokeColor | number | 否 | 是 | 多边形的边框颜色，默认值为0xff000000（黑色），颜色值为ARGB格式，异常值按默认值处理。 |
| jointType | [JointType](map-common.md#jointtype) | 否 | 是 | 多边形线条的拐角样式，默认值为[JointType](map-common.md#jointtype).DEFAULT，异常值按默认值处理。 |
| patterns | Array<[PatternItem](map-common.md#patternitem)> | 否 | 是 | 多边形的边框样式，默认值为空数组，异常值按默认值处理。 |
| strokeWidth | number | 否 | 是 | 多边形的边框宽度，单位：px，默认值为10，取值范围：大于等于0，异常值按默认值处理。 |

**示例：**

```
1. let polygonOptions: mapCommon.MapPolygonOptions = {
2. points: [
3. { latitude: 41.893478, longitude: 116.4 },
4. { latitude: 41.893478, longitude: 121.4 },
5. { latitude: 45.893478, longitude: 121.4 },
6. { latitude: 45.893478, longitude: 116.4 }
7. ],
8. holes: [],
9. clickable: true,
10. fillColor: 0xff00DE00,
11. geodesic: false,
12. strokeColor: 0xff000000,
13. jointType: mapCommon.JointType.DEFAULT,
14. patterns: [],
15. strokeWidth: 10,
16. visible: true,
17. zIndex: 0
18. };
```

## MapPolylineOptions

PhonePC/2in1TabletWearable

描述MapPolyline属性，继承[BaseOverlayOptions](map-common.md#baseoverlayoptions)。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| points | Array<[LatLng](map-common.md#latlng)> | 否 | 否 | 折线的一组顶点，异常值不处理。  **元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。 |
| clickable | boolean | 否 | 是 | 折线的可点击性，默认值为false，异常值按默认值处理。  - true：可点击  - false：不可点击  **元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。 |
| color | number | 否 | 是 | 折线的颜色，默认值为0xff000000（黑色），颜色值为ARGB格式，异常值按默认值处理。  **元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。 |
| colors | Array<number> | 否 | 是 | 折线的多段颜色，默认值为空数组（黑色），颜色值为ARGB格式，异常值按默认值处理。  **元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。 |
| startCap | [CapStyle](map-common.md#capstyle) | 否 | 是 | 折线的起始顶点的样式，默认值为[CapStyle](map-common.md#capstyle).BUTT，异常值按默认值处理。  **元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。 |
| endCap | [CapStyle](map-common.md#capstyle) | 否 | 是 | 折线的结束顶点的样式，默认值为[CapStyle](map-common.md#capstyle).BUTT，异常值按默认值处理。  **元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。 |
| geodesic | boolean | 否 | 是 | 折线的线段是否为大地曲线，默认值为false，异常值按默认值处理。  - true：大地曲线  - false：非大地曲线  **元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。 |
| jointType | [JointType](map-common.md#jointtype) | 否 | 是 | 折线的线条拐角样式，默认值为[JointType](map-common.md#jointtype).DEFAULT，异常值按默认值处理。  **元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。 |
| patterns | Array<[PatternItem](map-common.md#patternitem)> | 否 | 是 | 折线的样式，默认值为空数组，异常值按默认值处理。  **元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。 |
| width | number | 否 | 是 | 折线的宽度，单位：px，默认值为10，取值范围：[0, 512]，大于512按512处理。  **元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。 |
| gradient | boolean | 否 | 是 | 折线的渐变属性，默认值为false，异常值按默认值处理。  - true：可渐变  - false：不可渐变  **元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。 |
| customTexture | [ResourceStr](ts-types.md#resourcestr) | [image.PixelMap](arkts-apis-image-pixelmap.md) | 否 | 是 | 折线纹理。建议纹理使用没有背景色（透明色）的图片。  **起始版本：** 5.0.0(12)  **元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。  **说明：**  从版本6.1.0(23)开始，新增调整纹理间距功能，可通过更换带有更宽透明背景的纹理图片，实现纹理间距调整。 |
| isTextureMappingUsed | boolean | 否 | 是 | 是否使用贴图的方式处理纹理，默认值为false。  - true：使用贴图的方式处理纹理  - false：不使用贴图的方式处理纹理  **起始版本：** 5.0.3(15)  **元服务API：** 从版本5.0.3(15)开始，该接口支持在元服务中使用。 |
| customTextures | Array<[ResourceStr](ts-types.md#resourcestr) | [image.PixelMap](arkts-apis-image-pixelmap.md)> | 否 | 是 | 多个纹理图片。  **起始版本：** 5.0.3(15)  **元服务API：** 从版本5.0.3(15)开始，该接口支持在元服务中使用。  **说明：**  如果同时传入customTexture和customTextures，则呈现customTexture的效果。 |
| customTextureIndexes | Array<number> | 否 | 是 | 每个坐标对应的纹理索引。  **起始版本：** 5.0.3(15)  **元服务API：** 从版本5.0.3(15)开始，该接口支持在元服务中使用。  **说明：**  如果传入customTextures，则必须传入customTextureIndexes，同时customTextureIndexes的数组长度必须和points数组长度一致，customTextureIndexes每个元素取值必须在0到customTextures数组长度-1的范围内，如果不满足，返回错误码401。 |

**示例：**

```
1. let polylineOption: mapCommon.MapPolylineOptions = {
2. points: [
3. { latitude: 39.693478, longitude: 116.334595 },
4. { latitude: 39.593478, longitude: 116.434595 },
5. { latitude: 39.593478, longitude: 116.134595}
6. ],
7. clickable: true,
8. color: 0xff000000,
9. startCap: mapCommon.CapStyle.BUTT,
10. endCap: mapCommon.CapStyle.BUTT,
11. geodesic: false,
12. jointType: mapCommon.JointType.DEFAULT,
13. patterns: [{ type: 0, length: 100 }, { type: 0, length: 100 }, { type: 0, length: 100 }],
14. visible: true,
15. width: 20,
16. zIndex: 0,
17. gradient: false,
18. // 图标需存放在resources/rawfile目录下
19. customTexture: "icon/naviline_arrow.png",
20. isTextureMappingUsed: false
21. };
```

## BasePriorityOverlayParams

PhonePC/2in1TabletWearable

描述气泡、点注释等覆盖物的基础信息，继承[BaseOverlayOptions](map-common.md#baseoverlayoptions)。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| anchorU | number | 否 | 是 | POI的锚点在水平方向上的位置，值的范围为[0, 1]，默认值为0.5，异常值按默认值处理。 |
| anchorV | number | 否 | 是 | POI的锚点在垂直方向上的位置，值的范围为[0, 1]，默认值为1，异常值按默认值处理。 |
| forceVisible | boolean | 否 | 是 | POI的显示属性，默认值为false，异常值按默认值处理。  - true：碰撞后仍能显示  - false：碰撞后不可显示 |
| priority | number | 否 | 是 | 碰撞优先级，数值越大，优先级越低，默认值为Number.MAX\_VALUE，异常值按默认值处理。 |
| minZoom | number | 否 | 是 | 展示的地图最小图层，有效范围：[2, 20]，默认值为2，异常值按默认值处理。如果设置的最小缩放级别小于2，minZoom会取2。  约束条件：最小层级不大于最大层级，不小于2。 |
| maxZoom | number | 否 | 是 | 展示的地图最大图层，有效范围：[2, 20]，默认值为20，异常值按默认值处理。如果设置的最大缩放级别大于20，maxZoom会取20。  约束条件：最大层级不大于20，不小于最小层级。 |

## PointAnnotationParams

PhonePC/2in1TabletWearable

描述点注释属性，继承[BasePriorityOverlayParams](map-common.md#basepriorityoverlayparams)。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| position | [LatLng](map-common.md#latlng) | 否 | 否 | 点注释图标锚点，异常值不处理。  **元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。 |
| repeatable | boolean | 否 | 是 | 点注释名称与地图POI名称相同时，是否支持去重，默认值为false，异常值按默认值处理。  - true：支持去重  - false：不支持去重  **元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。  **说明：**  碰撞规则为[CollisionRule](map-common.md#collisionrule).NONE时，repeatable不支持设置。 |
| collisionRule | [CollisionRule](map-common.md#collisionrule) | 否 | 是 | 点注释的碰撞规则，默认值为[CollisionRule](map-common.md#collisionrule).NAME，异常值按默认值处理。  **元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。  **说明：**  设置碰撞规则为[CollisionRule](map-common.md#collisionrule).ALL，需要同时设置覆盖物碰撞优先级priority属性。 |
| titles | Array<[Text](map-common.md#text)> | 否 | 否 | 点注释的标题，数组长度最小为1，最大为3。  **元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。 |
| icon | string | [image.PixelMap](arkts-apis-image-pixelmap.md) | [Resource](ts-types.md#resource) | 否 | 是 | 点注释的图标，不传时使用默认图标。  - 图片格式支持jpg、jpeg、png、gif、webp、svg。  - string类型入参支持两种格式：  1. 资源相对路径格式：图标存放在resources/rawfile，icon参数传入rawfile文件夹下的相对路径。  2. toDataURL格式（如data:image/png;base64,<图片的Base64字节编码值>）。  **元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。  **说明：**  从5.0.0(12)版本开始，icon属性支持[image.PixelMap](arkts-apis-image-pixelmap.md)和[Resource](ts-types.md#resource)类型。 |
| showIcon | boolean | 否 | 是 | 点注释是否展示图标。默认值为true。  - true：展示  - false：不展示  **元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。 |
| textPosition | [TextPosition](map-common.md#textposition) | 否 | 是 | 设置点注释的文本位置。  默认值为[TextPosition](map-common.md#textposition).DEFAULT。  **起始版本：** 5.0.0(12)  **元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。 |

**示例：**

```
1. let pointAnnotationOptions: mapCommon.PointAnnotationParams = {
2. position: {
3. latitude: 39.918,
4. longitude: 116.397
5. },
6. repeatable: true,
7. collisionRule: mapCommon.CollisionRule.NAME,
8. titles: [{
9. content: "Title1",
10. color: 0xFF000000,
11. fontSize: 15,
12. strokeColor: 0xFFFFFFFF,
13. strokeWidth: 2,
14. fontStyle: mapCommon.FontStyle.ITALIC
15. }],
16. // 图标需存放在resources/rawfile目录下
17. icon: "test.png",
18. showIcon: true,
19. anchorU: 0.5,
20. anchorV: 1,
21. forceVisible: false,
22. priority: 3,
23. minZoom: 2,
24. maxZoom: 20,
25. visible: true,
26. zIndex: 10
27. };
```

## BubbleParams

PhonePC/2in1TabletWearable

描述气泡属性，继承[BasePriorityOverlayParams](map-common.md#basepriorityoverlayparams)。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| positions | Array<Array<[LatLng](map-common.md#latlng)>> | 否 | 否 | 气泡位置，系统基于多个位置段计算图标的适当位置，异常值不处理。 |
| icons | Array<string | [image.PixelMap](arkts-apis-image-pixelmap.md) | [Resource](ts-types.md#resource)> | 否 | 否 | 气泡图标，异常值不处理。  - 必须提供4个方向的图标，传入的图标宽高需要相同。  - 图片格式支持jpg、jpeg、png、gif、webp、svg。  - string类型入参支持两种格式：  - 资源相对路径格式：图标存放在resources/rawfile，icon参数传入rawfile文件夹下的相对路径。  - toDataURL格式（如data:image/png;base64,<图片的Base64字节编码值>）。  **说明：**  从5.0.0(12)版本开始，icon属性支持[image.PixelMap](arkts-apis-image-pixelmap.md)和[Resource](ts-types.md#resource)类型。 |

**示例：**

```
1. let bubbleOptions: mapCommon.BubbleParams = {
2. positions: [[{ latitude: 39.9, longitude: 116.4 }]],
3. // 图片按照左上右下的顺序取值，图片需存放在resources/rawfile目录下
4. icons: [
5. 'icon1.png',
6. 'icon2.png',
7. 'icon3.png',
8. 'icon4.png'
9. ],
10. forceVisible: true,
11. priority: 3,
12. minZoom: 2,
13. maxZoom: 20,
14. visible: true,
15. zIndex: 1
16. };
```

## Text

PhonePC/2in1TabletWearable

用于描述点注释标题的文本属性。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| content | string | 否 | 否 | 标题内容，超长字串超出部分用省略号“...”表示。 |
| color | number | 否 | 是 | 标题字体颜色，默认值为0xFF000000（黑色），颜色值为ARGB格式。 |
| fontSize | number | 否 | 是 | 标题字体大小，默认值为15，单位：px。取值范围：[0,100]，超出范围按范围内最大值或最小值处理。 |
| strokeColor | number | 否 | 是 | 标题描边颜色，默认值为0xFFFFFFFF（白色），颜色值为ARGB格式。 |
| strokeWidth | number | 否 | 是 | 标题描边宽度，默认值为2，单位：px。取值范围：[0,10]，超出范围按范围内最大值或最小值处理。 |
| fontStyle | [FontStyle](map-common.md#fontstyle) | 否 | 是 | 标题字体样式，默认值为[FontStyle](map-common.md#fontstyle).REGULAR，异常值按默认值处理。 |

**示例：**

```
1. let text: mapCommon.Text = {
2. content: "南京夫子庙",
3. color: 0xFF000000,
4. fontSize: 15,
5. strokeColor: 0xFFFFFFFF,
6. strokeWidth: 2,
7. fontStyle: mapCommon.FontStyle.ITALIC
8. };
```

## Padding

PhonePC/2in1TabletWearable

设置地图和边界的距离的参数。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| left | number | 否 | 是 | 在地图左侧增加的填充距离，单位：px，默认值为0，异常值按照默认值处理。 |
| top | number | 否 | 是 | 在地图顶部增加的填充距离，单位：px，默认值为0，异常值按照默认值处理。 |
| right | number | 否 | 是 | 在地图右侧增加的填充距离，单位：px，默认值为0，异常值按照默认值处理。 |
| bottom | number | 否 | 是 | 在地图底部增加的填充距离，单位：px，默认值为0，异常值按照默认值处理。 |

**示例：**

```
1. // 初始化参数，左边距0，底边距50
2. let padding: mapCommon.Padding = {
3. left: 0,
4. bottom: 50
5. };
```

## VisibleRegion

PhonePC/2in1TabletWearable

VisibleRegion包含四个点，这四个点定义了地图相机的四边形可视区域。因为相机可能会倾斜，所以这个多边形也可以是梯形而不一定是矩形。如果相机正好位于可视区域中心上方，则形状为矩形，但如果相机倾斜，则形状将显示为最短边最接近视点的梯形。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| farLeft | [LatLng](map-common.md#latlng) | 否 | 否 | 定义相机的左上角。 |
| farRight | [LatLng](map-common.md#latlng) | 否 | 否 | 定义相机的右上角。 |
| bounds | [LatLngBounds](map-common.md#latlngbounds) | 否 | 否 | 定义的可视区域的最小边界框。 |
| nearLeft | [LatLng](map-common.md#latlng) | 否 | 否 | 定义相机的左下角。 |
| nearRight | [LatLng](map-common.md#latlng) | 否 | 否 | 定义相机的右下角。 |

**示例：**

```
1. // 示例中this.mapController来源参考指南显示地图示例代码
2. let projection: map.Projection = this.mapController?.getProjection();
3. let visibleRegion: mapCommon.VisibleRegion = projection.getVisibleRegion();
```

## MapPoint

PhonePC/2in1TabletWearable

屏幕坐标点。屏幕左顶点为（0, 0）点，positionX正值代表可视区域向右移动，负值代表可视区域向左移动。positionY正值代表可视区域向下移动，负值代表可视区域向上移动。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| positionX | number | 否 | 否 | 点的X坐标，单位：px。 |
| positionY | number | 否 | 否 | 点的Y坐标，单位：px。 |

**示例：**

```
1. let point: mapCommon.MapPoint = {
2. positionX: 100,
3. positionY: 100
4. };
```

## CustomMapStyleOptions

PhonePC/2in1TabletWearable

自定义样式参数。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| styleId | string | 否 | 是 | 自定义样式ID。  **说明：**  styleId和styleContent同时传入，优先使用styleId。styleId可在[Petal Maps Studio](https://developer.petalmaps.com/console/studio/)平台上创建。 |
| styleContent | string | 否 | 是 | 离线样式内容，内容格式参见[样式参考](../harmonyos-guides/map-style.md#样式参考)。 |

**示例：**

```
1. // styleId需要替换为您自己的样式ID，样式ID可在Petal Maps Studio平台上创建
2. let param: mapCommon.CustomMapStyleOptions = {
3. styleId: "xxxxxxx"
4. };
```

## ClusterItem

PhonePC/2in1TabletWearable

待聚合节点。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| position | [LatLng](map-common.md#latlng) | 否 | 否 | 待聚合节点的坐标。 |

**示例：**

```
1. let clusterItem: mapCommon.ClusterItem = {
2. position: {
3. latitude: 39.99,
4. longitude: 116.334595
5. }
6. };
```

## ClusterOverlayParams

PhonePC/2in1TabletWearable

聚合图层参数。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| clusterItems | Array<[ClusterItem](map-common.md#clusteritem)> | 否 | 否 | 待聚合节点数组。 |
| distance | number | 否 | 否 | 聚合节点聚合的距离，单位：vp。 |

接口提供以下方法，支持聚合项自定义图标。

| 返回类型 | 方法 |
| --- | --- |
| Promise<[image.PixelMap](arkts-apis-image-pixelmap.md)> | [getCustomIcon](map-common.md#getcustomicon)?(clusterItems: Array<[ClusterItem](map-common.md#clusteritem)>)  根据聚合项自定义图标，使用Promise异步回调。 |

**示例：**

```
1. let clusterItem1: mapCommon.ClusterItem = {
2. position: {
3. latitude: 39.89,
4. longitude: 116.335595
5. }
6. };
7. let clusterItem2: mapCommon.ClusterItem = {
8. position: {
9. latitude: 39.99,
10. longitude: 116.334595
11. }
12. };
13. let array: Array<mapCommon.ClusterItem> = [
14. clusterItem1,
15. clusterItem2
16. ];
17. let clusterOverlayParams: mapCommon.ClusterOverlayParams = { distance: 40, clusterItems: array };
```

### getCustomIcon

PhonePC/2in1TabletWearable

getCustomIcon?(clusterItems: Array<ClusterItem>): Promise<image.PixelMap>

根据聚合项自定义图标。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| clusterItems | Array<[ClusterItem](map-common.md#clusteritem)> | 是 | 聚合节点数组。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[image.PixelMap](arkts-apis-image-pixelmap.md)> | Promise对象，返回[image.PixelMap](arkts-apis-image-pixelmap.md)。 |

**示例：**

```
1. // 实现mapCommon.ClusterOverlayParams中的getCustomIcon方法
2. import { mapCommon } from '@kit.MapKit';
3. import { image } from '@kit.ImageKit';

5. export class ClusterOverlayParamsMore implements mapCommon.ClusterOverlayParams {
6. clusterItems: mapCommon.ClusterItem[] = new Array();
7. private offCanvas: OffscreenCanvas = new OffscreenCanvas(62, 62);
8. private settings: RenderingContextSettings = new RenderingContextSettings(true);

10. constructor(clusterItems: mapCommon.ClusterItem[], distance: number) {
11. this.clusterItems = clusterItems;
12. this.distance = distance;
13. }

15. distance: number = 0;

17. // 自定义聚合图标，例如将cluster的clusterItems的第一个clusterItem的经度作为文本，绘制圆形图标
18. async getCustomIcon(clusterItems: mapCommon.ClusterItem[]): Promise<image.PixelMap> {
19. let offContext = this.offCanvas.getContext("2d", this.settings);

21. offContext.clearRect(0, 0, 62, 62);
22. // 绘制圆形
23. offContext.fillStyle = 0xff990000;
24. offContext.beginPath();
25. offContext.arc(31, 31, 30, 0, 6.28);
26. offContext.stroke();
27. offContext.fill();
28. offContext.save();

30. // 在圆形内绘制文本，文本信息为clusterItems的第一个聚合点的经度
31. offContext.font = '20vp sans-serif';
32. offContext.textAlign = 'center';
33. offContext.textBaseline = 'middle';
34. offContext.fillStyle = 0xffffffff;
35. offContext.fillText(JSON.stringify(clusterItems[0].position.longitude).substring(0,3), 31, 31);
36. offContext.restore();
37. let iconPixelMap = offContext.getPixelMap(0, 0, 62, 62);
38. return iconPixelMap;
39. }
40. }
```

## ImageOverlayParams

PhonePC/2in1TabletWearable

覆盖物参数。继承[BaseOverlayOptions](map-common.md#baseoverlayoptions)。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| bounds | [LatLngBounds](map-common.md#latlngbounds) | 否 | 是 | 设置基于矩形区域的覆盖物的位置。position和bounds是可选的，但是两个参数需要必填其中一个参数，当两者都入参时，bounds具有更高的优先级。position入参时，width为必填参数。 |
| position | [LatLng](map-common.md#latlng) | 否 | 是 | 设置覆盖物的位置。position和bounds是可选的，但是两个参数需要必填其中一个，当两者都入参时，bounds具有更高的优先级。position入参时，width为必填参数。 |
| width | number | 否 | 是 | 覆盖物的宽度，单位：米，仅当position有值时有效，width为正整数。 |
| height | number | 否 | 是 | 覆盖物的高度，单位：米，当position和width都有值时才有效，height为正整数。 |
| anchorU | number | 否 | 是 | 覆盖物的锚点在水平方向上的位置。取值范围：[0,1]。默认值为0.5。  **说明：**  当bounds有值时，设置anchorU会改变覆盖物的锚点在水平方向上的位置，不会改变bounds的范围。 |
| anchorV | number | 否 | 是 | 覆盖物的锚点在垂直方向上的位置。取值范围：[0,1]。默认值为0.5。  **说明：**  当bounds有值时，设置anchorV会改变覆盖物的锚点在垂直方向上的位置，不会改变bounds的范围。 |
| bearing | number | 否 | 是 | 覆盖物的旋转角度。  以正北方向为0度、顺时针方向为正的角度，默认值为0，取值范围：[0, 360)。超出取值范围的值会换算成取值范围内的值，比如361会被换算成1，-1换算为359。 |
| clickable | boolean | 否 | 是 | 覆盖物是否可单击。  - true：可点击。  - false：不可点击。  默认值为false。 |
| image | [ResourceStr](ts-types.md#resourcestr) | [image.PixelMap](arkts-apis-image-pixelmap.md) | 否 | 否 | 覆盖物的图像入参。  图片格式支持jpg、jpeg、png、gif、webp、svg。  **说明：**  [ResourceStr](ts-types.md#resourcestr)为Resource和string两种格式，其中string类型入参支持两种格式：  - 资源相对路径格式：图标存放在resources/rawfile，image参数传入rawfile文件夹下的相对路径。  - toDataURL格式（如data:image/png;base64,<图片的Base64字节编码值>）。 |
| transparency | number | 否 | 是 | 覆盖物的透明度。  取值范围：[0, 1]。  0表示不透明，1表示全透明。  默认值为0。 |

**示例：**

```
1. let imageOverlayParams: mapCommon.ImageOverlayParams = {
2. bounds: { southwest: { latitude: 32, longitude: 118 }, northeast: { latitude: 32.4, longitude: 118.4 } },
3. // 图标需存放在resources/rawfile目录下
4. image: 'icon/icon.png',
5. transparency: 0.3,
6. zIndex: 101,
7. anchorU: 0.5,
8. anchorV: 0.5,
9. clickable: true,
10. visible: true,
11. bearing: 90
12. };
```

## BuildingOverlayParams

PhonePC/2in1TabletWearable

3D建筑参数。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| points | Array<[LatLng](map-common.md#latlng)> | 否 | 否 | 建筑底面坐标集合。  最少三个坐标点，而且坐标点按顺时针方向连接可以形成完整的平面。 |
| totalHeight | number | 否 | 否 | 建筑距离地面的高度，单位：米。  限制最大高度30000米。 |
| floorBottomHeight | number | 否 | 否 | 所选楼层底部到地面的高度，单位：米。 |
| topFaceColor | number | 否 | 是 | 建筑顶部的颜色，颜色值是ARGB格式。  默认值为红色（0xffff0000）。 |
| sideFaceColor | number | 否 | 是 | 建筑侧面的颜色，颜色值是ARGB格式。  默认值为红色（0xffff0000）。 |
| floorColor | number | 否 | 是 | 所选楼层的顶部颜色，颜色值为ARGB格式。  默认值为红色（0xffff0000）。 |
| showLevel | number | 否 | 是 | 建筑开始显示的层级。取值范围：[2,20]，默认值为15，超出范围按默认值处理。 |
| animationDuration | number | 否 | 是 | 动画时长，单位：ms。取值需大于等于100ms，默认值为0，超出范围按默认值处理。 |
| sideTexture | [BuildingTexture](map-common.md#buildingtexture) | 否 | 是 | 建筑的侧面纹理。 |
| floorTexture | [BuildingTexture](map-common.md#buildingtexture) | 否 | 是 | 所选楼层的纹理。 |

**示例：**

```
1. let points: Array<mapCommon.LatLng> = [
2. {
3. latitude: 31.984794,
4. longitude: 118.765865
5. },
6. {
7. latitude: 31.98468,
8. longitude: 118.766076
9. },
10. {
11. latitude: 31.98472,
12. longitude: 118.766116
13. },
14. {
15. latitude: 31.98463,
16. longitude: 118.766292
17. },
18. {
19. latitude: 31.984586,
20. longitude: 118.766251
21. },
22. {
23. latitude: 31.984536,
24. longitude: 118.766344
25. },
26. {
27. latitude: 31.984633,
28. longitude: 118.766446
29. },
30. {
31. latitude: 31.9848,
32. longitude: 118.766285
33. },
34. {
35. latitude: 31.984925,
36. longitude: 118.766312
37. },
38. {
39. latitude: 31.985282,
40. longitude: 118.766661
41. },
42. {
43. latitude: 31.985438,
44. longitude: 118.766419
45. },
46. {
47. latitude: 31.985801,
48. longitude: 118.766755
49. },
50. {
51. latitude: 31.985856,
52. longitude: 118.766504
53. },
54. {
55. latitude: 31.985785,
56. longitude: 118.766434
57. },
58. {
59. latitude: 31.985821,
60. longitude: 118.766278
61. },
62. {
63. latitude: 31.985897,
64. longitude: 118.766311
65. },
66. {
67. latitude: 31.985944,
68. longitude: 118.766095
69. },
70. {
71. latitude: 31.985909,
72. longitude: 118.766069
73. },
74. {
75. latitude: 31.985794,
76. longitude: 118.765989
77. },
78. {
79. latitude: 31.9857,
80. longitude: 118.766029
81. },
82. {
83. latitude: 31.985658,
84. longitude: 118.766164
85. },
86. {
87. latitude: 31.985647,
88. longitude: 118.766271
89. },
90. {
91. latitude: 31.985574,
92. longitude: 118.766297
93. },
94. {
95. latitude: 31.985458,
96. longitude: 118.766285
97. },
98. {
99. latitude: 31.985271,
100. longitude: 118.766002
101. },
102. {
103. latitude: 31.985219,
104. longitude: 118.766002
105. },
106. {
107. latitude: 31.985135,
108. longitude: 118.766029
109. },
110. {
111. latitude: 31.985093,
112. longitude: 118.766083
113. },
114. {
115. latitude: 31.985019,
116. longitude: 118.766109
117. },
118. {
119. latitude: 31.984978,
120. longitude: 118.766083
121. },
122. {
123. latitude: 31.984794,
124. longitude: 118.765865
125. }
126. ];
127. points.reverse();
128. // 3D建筑参数
129. let buildingOverlayOptions: mapCommon.BuildingOverlayParams =
130. {
131. // 3D建筑的范围参数（点为顺时针绘制）
132. points: points,
133. // 3D建筑的高度
134. totalHeight: 51,
135. // 3D建筑的选中楼层高度
136. floorBottomHeight: 33,
137. // 3D建筑的顶部颜色
138. topFaceColor: 0xffa4b8f7,
139. // 3D建筑的侧面颜色
140. sideFaceColor: 0x44a4b8f7,
141. // 3D建筑的选中楼层颜色
142. floorColor: 0xff000000,
143. // 3D建筑的展示层级
144. showLevel: 14,
145. // 3D建筑选中楼层从底部升起的动画时长
146. animationDuration: 5000,
147. // 3D建筑侧面的纹理
148. sideTexture: { image: $r("app.media.side_tex"), height: 3, width: 3 },
149. // 3D建筑选中楼层的纹理
150. floorTexture: { image: $r("app.media.floor_tex"), height: 3, width: 3 }
151. };
```

## BuildingTexture

PhonePC/2in1TabletWearable

建筑纹理。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| image | [ResourceStr](ts-types.md#resourcestr) | [image.PixelMap](arkts-apis-image-pixelmap.md) | 否 | 否 | 纹理图片。  图片格式支持jpg、jpeg、png、gif、webp、svg。  **说明：**  [ResourceStr](ts-types.md#resourcestr)为Resource和string两种格式，其中string类型入参支持两种格式：  - 资源相对路径格式：图标存放在resources/rawfile，image参数传入rawfile文件夹下的相对路径。  - toDataURL格式（如data:image/png;base64,<图片的Base64字节编码值>）。 |
| width | number | 否 | 是 | 纹理宽度，单位：米，取值大于等于0，默认值为3，异常值按默认值处理。 |
| height | number | 否 | 是 | 纹理高度，单位：米，取值大于等于0，默认值为3，异常值按默认值处理。 |

**示例：**

```
1. let buildingTexture: mapCommon.BuildingTexture = {
2. image: $r("app.media.floor_tex"),
3. height: 10,
4. width: 10
5. };
```

## TraceOverlayParams

PhonePC/2in1TabletWearable

动态轨迹的参数。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| points | Array<[LatLng](map-common.md#latlng)> | 否 | 否 | 跟踪点。  points个数上限为100000。 |
| width | number | 否 | 是 | 轨迹宽度，单位：px。  默认值为10。  取值范围：[0, 512]，大于512按512处理。 |
| color | number | 否 | 是 | 轨迹颜色，颜色值是ARGB格式。  默认值为0xaaff0000。 |
| isMapMoving | boolean | 否 | 是 | 设置地图和轨迹是否一起移动。  - true：地图和轨迹一起移动  - false：仅轨迹移动  默认值为false。 |
| animationDuration | number | 否 | 是 | 轨迹动画持续时间，单位为毫秒，最小值为100。  默认值为5000。  **说明：**  当持续时间小于100毫秒时，时间将按默认值5000毫秒处理。 |
| animationCallback | Callback<number> | 否 | 是 | 监听轨迹的当前位置。返回点的索引。 |

**示例：**

```
1. // 示例中this.mapController来源参考指南显示地图示例代码
2. // marker1的参数
3. let markerOptions1: mapCommon.MarkerOptions = {
4. position: {
5. latitude: 31.99227173519985,
6. longitude: 118.7622219990476
7. },
8. // 图标需存放在resources/base/media目录下
9. icon: $r("app.media.track_setting_sport_map_marker_22"),
10. anchorU: 0.5,
11. anchorV: 1,
12. visible: true
13. };
14. // 新增marker1
15. let markerBoy1 = await this.mapController.addMarker(markerOptions1);
16. let boyImages1: map.PlayImageAnimation = new map.PlayImageAnimation();
17. boyImages1.setDuration(1000);
18. let resourceArray: Array<Resource> = new Array();
19. resourceArray.push($r("app.media.side_0"));
20. resourceArray.push($r("app.media.side_1"));
21. resourceArray.push($r("app.media.side_2"));
22. resourceArray.push($r("app.media.side_3"));
23. resourceArray.push($r("app.media.side_4"));
24. resourceArray.push($r("app.media.side_5"));
25. resourceArray.push($r("app.media.side_6"));
26. resourceArray.push($r("app.media.side_7"));
27. resourceArray.push($r("app.media.side_8"));
28. resourceArray.push($r("app.media.side_9"));
29. resourceArray.push($r("app.media.side_10"));
30. resourceArray.push($r("app.media.side_11"));
31. resourceArray.push($r("app.media.side_12"));
32. resourceArray.push($r("app.media.side_13"));
33. resourceArray.push($r("app.media.side_14"));
34. resourceArray.push($r("app.media.side_15"));
35. resourceArray.push($r("app.media.side_16"));
36. resourceArray.push($r("app.media.side_17"));
37. resourceArray.push($r("app.media.side_18"));
38. resourceArray.push($r("app.media.side_19"));
39. resourceArray.push($r("app.media.side_20"));
40. await boyImages1.addImages(resourceArray);
41. boyImages1.setRepeatCount(-1);

43. // marker1添加动画
44. markerBoy1.setAnimation(boyImages1);
45. markerBoy1.startAnimation();

47. // marker2的参数
48. let markerOptions2: mapCommon.MarkerOptions = {
49. position: {
50. latitude: 31.99227173519985,
51. longitude: 118.7622219990476
52. },
53. // 图标需存放在resources/base/media目录下
54. icon: $r("app.media.track_setting_sport_map_marker_22"),
55. anchorU: 0.5,
56. anchorV: 1,
57. visible: false
58. };
59. // 新增marker2
60. let markerBoy2 = await this.mapController.addMarker(markerOptions2);
61. let boyImages2: map.PlayImageAnimation = new map.PlayImageAnimation();
62. boyImages2.setDuration(1000);
63. let resourceArray2: Array<Resource> = new Array();
64. resourceArray2.push($r("app.media.behavior_front_cycling_boy_000"));
65. resourceArray2.push($r("app.media.behavior_front_cycling_boy_001"));
66. resourceArray2.push($r("app.media.behavior_front_cycling_boy_002"));
67. resourceArray2.push($r("app.media.behavior_front_cycling_boy_003"));
68. resourceArray2.push($r("app.media.behavior_front_cycling_boy_004"));
69. resourceArray2.push($r("app.media.behavior_front_cycling_boy_005"));
70. resourceArray2.push($r("app.media.behavior_front_cycling_boy_006"));
71. resourceArray2.push($r("app.media.behavior_front_cycling_boy_007"));
72. resourceArray2.push($r("app.media.behavior_front_cycling_boy_008"));
73. resourceArray2.push($r("app.media.behavior_front_cycling_boy_009"));
74. resourceArray2.push($r("app.media.behavior_front_cycling_boy_010"));
75. resourceArray2.push($r("app.media.behavior_front_cycling_boy_011"));
76. resourceArray2.push($r("app.media.behavior_front_cycling_boy_012"));
77. resourceArray2.push($r("app.media.behavior_front_cycling_boy_013"));
78. resourceArray2.push($r("app.media.behavior_front_cycling_boy_014"));
79. resourceArray2.push($r("app.media.behavior_front_cycling_boy_015"));
80. resourceArray2.push($r("app.media.behavior_front_cycling_boy_016"));
81. resourceArray2.push($r("app.media.behavior_front_cycling_boy_017"));
82. resourceArray2.push($r("app.media.behavior_front_cycling_boy_018"));
83. await boyImages2.addImages(resourceArray2);
84. boyImages2.setRepeatCount(-1);
85. // marker2添加动画
86. markerBoy2.setAnimation(boyImages2);
87. markerBoy2.startAnimation();

89. let points: Array<mapCommon.LatLng> = new Array();
90. points.push({ latitude: 31.99685233070878, longitude: 118.75846023442728 });
91. points.push({ latitude: 31.99671325810786, longitude: 118.75846738985165 });
92. points.push({ latitude: 31.99659191076709, longitude: 118.7585347621686 });
93. points.push({ latitude: 31.99648202537233, longitude: 118.7586266510386 });
94. points.push({ latitude: 31.99637707201552, longitude: 118.75872004590596 });
95. points.push({ latitude: 31.996278207010903, longitude: 118.75880449946251 });
96. points.push({ latitude: 31.996187481969695, longitude: 118.7588781960278 });
97. points.push({ latitude: 31.996092248919354, longitude: 118.75895330554488 });
98. points.push({ latitude: 31.995962740450565, longitude: 118.75904721407304 });
99. points.push({ latitude: 31.995792921394, longitude: 118.75916904998051 });
100. points.push({ latitude: 31.995601885713416, longitude: 118.7593235241019 });
101. points.push({ latitude: 31.995398221178277, longitude: 118.75949998588176 });
102. points.push({ latitude: 31.995185902197715, longitude: 118.7596871082939 });
103. points.push({ latitude: 31.994983473052656, longitude: 118.75987334062296 });
104. points.push({ latitude: 31.99482433699269, longitude: 118.76002095184032 });
105. points.push({ latitude: 31.994709073721708, longitude: 118.76012902920532 });
106. points.push({ latitude: 31.99460732100702, longitude: 118.76023892576234 });
107. points.push({ latitude: 31.99449284962087, longitude: 118.7603694232856 });
108. points.push({ latitude: 31.99435358179254, longitude: 118.76053622438056 });
109. points.push({ latitude: 31.99420771148339, longitude: 118.76072790126692 });
110. points.push({ latitude: 31.994075194901523, longitude: 118.7609100960977 });
111. points.push({ latitude: 31.993952686158877, longitude: 118.7610741329013 });
112. points.push({ latitude: 31.993840180644217, longitude: 118.7612193418965 });
113. points.push({ latitude: 31.993733787150244, longitude: 118.76135383115654 });
114. points.push({ latitude: 31.993617206525155, longitude: 118.76150529647698 });

116. // 动态轨迹的入参
117. let traceOptions: mapCommon.TraceOverlayParams = {
118. // 轨迹点
119. points: points,
120. // 轨迹的动画时长
121. animationDuration: 5000,
122. // 相机是否跟随动画移动
123. isMapMoving: true,
124. // 轨迹的颜色
125. color: 0xAAFFAA00,
126. // 轨迹的宽度
127. width: 20,
128. // 轨迹的动画回调（回调轨迹点的index）
129. animationCallback: (pointIndex) => {
130. // 换成骑行
131. if (pointIndex === 10) {
132. markerBoy1.setVisible(false);
133. markerBoy2.setVisible(true);
134. }
135. }
136. };
137. let markers: Array<map.Marker> = new Array();
138. markers.push(markerBoy1, markerBoy2);
139. // 新增轨迹点动画
140. let traceOverlay = await this.mapController.addTraceOverlay(traceOptions, markers);
```

## MapArcParams

PhonePC/2in1TabletWearable

弧线的参数。继承[BaseOverlayOptions](map-common.md#baseoverlayoptions)。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| startPoint | [LatLng](map-common.md#latlng) | 否 | 否 | 起始位置。 |
| centerPoint | [LatLng](map-common.md#latlng) | 否 | 否 | 中心位置。 |
| endPoint | [LatLng](map-common.md#latlng) | 否 | 否 | 结束位置。 |
| color | number | 否 | 是 | 弧线的颜色，默认值为0xFFFFFFFF（白色），颜色值为ARGB格式，异常值按默认值处理。 |
| width | number | 否 | 是 | 弧线的宽度，默认值为10，单位：px，取值范围：大于等于0，异常值按默认值处理。 |

**示例：**

```
1. // 设置弧线参数
2. let mapArcParams: mapCommon.MapArcParams = {
3. // 弧线起点坐标
4. startPoint: {
5. latitude: 39.913138,
6. longitude: 116.415112
7. },
8. // 弧线终点坐标
9. endPoint: {
10. latitude: 28.239473,
11. longitude: 112.954094
12. },
13. // 弧线中心点坐标
14. centerPoint: {
15. latitude: 33.86970399048567,
16. longitude: 112.08633528544145
17. },
18. width: 10,
19. color: 0xffff0000,
20. visible: true,
21. zIndex: 100
22. };
```

## CoordinateLatLng

PhonePC/2in1TabletWearable

指定的坐标系和坐标。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| coordinateType | [CoordinateType](map-common.md#coordinatetype) | 否 | 否 | 坐标系类型。 |
| location | [LatLng](map-common.md#latlng) | 否 | 否 | 坐标。 |

**示例：**

```
1. let location: mapCommon.CoordinateLatLng = {
2. coordinateType: mapCommon.CoordinateType.GCJ02,
3. location: { latitude: 31.984410259206815, longitude: 118.76625379397866 }
4. };
```

## TileOverlayParams

PhonePC/2in1TabletWearable

瓦片图层的参数。继承[BaseOverlayOptions](map-common.md#baseoverlayoptions)。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.3(15)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.3(15)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| tileUrl | string | 否 | 否 | 瓦片图层的URL地址。  必须是以http或者https开头的URL且包含占位符{x}、{y}和{z}。 |
| transparency | number | 否 | 是 | 瓦片图层的透明度。  取值范围为[0, 1]，0表示不透明，1表示透明。  默认值为0。 |
| fadeIn | boolean | 否 | 是 | 是否开启瓦片图层淡入。  - true：开启瓦片图层淡入。  - false：不开启瓦片图层淡入。  默认值为true。 |

**示例：**

```
1. let params: mapCommon.TileOverlayParams = {
2. // 设置地图瓦片图层的地址，必须是以http或者https开头的URL且包含占位符{x}、{y}和{z}
3. tileUrl: "https://xxx/xxx?x={x}&y={y}&z={z}",
4. transparency: 0,
5. fadeIn: false
6. };
```

## TileOverlayOptions

PhonePC/2in1TabletWearable

瓦片图层的参数。继承[BaseOverlayOptions](map-common.md#baseoverlayoptions)。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 6.0.0(20)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| tileUrl | string | 否 | 是 | 瓦片图层的URL地址。  必须是以http或者https开头的URL且包含占位符{x}、{y}和{z}。 |
| tileProvider | [TileProvider](map-common.md#tileprovider) | 否 | 是 | 根据瓦片坐标获取瓦片。 |
| transparency | number | 否 | 是 | 瓦片图层的透明度。  取值范围为[0, 1]，0表示不透明，1表示透明。  默认值为0。 |
| fadeIn | boolean | 否 | 是 | 是否开启瓦片图层淡入。  - true：开启瓦片图层淡入。  - false：不开启瓦片图层淡入。  默认值为true。 |
| diskCacheEnabled | boolean | 否 | 是 | 是否启用磁盘缓存。  - true：开启磁盘缓存。  - false：不开启磁盘缓存。  默认值为false。 |
| diskCacheSize | number | 否 | 是 | 磁盘缓存大小，单位：KB，默认值：20480。 |
| diskCachePath | string | 否 | 是 | 磁盘缓存路径。如果启用了磁盘缓存，则必须配置。 |

**示例：**

```
1. let params: mapCommon.TileOverlayOptions = {
2. // 设置地图瓦片图层的地址，必须是以http或者https开头的URL且包含占位符{x}、{y}和{z}
3. tileUrl: "https://xxx/xxx?x={x}&y={y}&z={z}",
4. diskCacheEnabled: true,
5. diskCacheSize: 20480,
6. diskCachePath: '/data/storage/el2/database'
7. };
```

## HeatmapParams

PhonePC/2in1TabletWearable

热力图的参数。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 6.0.0(20)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| id | string | 否 | 否 | 热力图ID。 |
| data | [WeightedLatLng](map-common.md#weightedlatlng)[] | 否 | 否 | 热力图数据（建议数据量小于10000条）。 |
| color | Record<number, number> | 否 | 是 | 热力图颜色，ARGB格式。取值范围：[0，1]，key是数据密度，value是ARGB格式的颜色。默认值：{ 0: 0x00026C39, 0.15: 0xAA138C4A, 0.3: 0xFF82CB67, 0.45: 0xFFE3F399, 0.6: 0xFFFEDE89, 0.75: 0xFFF67C4A, 0.9: 0xFFBE1827, 1: 0xFFA90426 }  如果某个记录的key取值范围或者value格式非法的话，移除这条记录，如果都不合法，就使用默认值。 |
| intensity | number | Record<number, number> | 否 | 是 | 热力图强度，可以配置不同层级的强度，key表示层级，value表示按强度，如果是number类型，所有层级使用同一个强度。  小于等于0按默认值1处理。 |
| opacity | number | Record<number, number> | 否 | 是 | 热力图透明度。取值范围[0，1]，0表示不透明，1表示透明，小于0按照最小值0处理，大于1按照最大值1处理。如果是number类型，所有层级使用同一个透明度。默认值：0。 |
| radius | number | Record<number, number> | 否 | 是 | 热力图半径，可以配置不同层级的半径，key表示层级，value表示按半径，如果是number类型，所有层级使用同一个半径，默认值10，默认单位：[RadiusUnit](map-common.md#radiusunit).PIXEL\_UNIT。 |
| radiusUnit | [RadiusUnit](map-common.md#radiusunit) | 否 | 是 | 半径单位。默认值：[RadiusUnit](map-common.md#radiusunit).PIXEL\_UNIT。 |
| visible | boolean | 否 | 是 | 热力图是否可见。默认值：true。  - true：可见。  - false：不可见。 |

## RadiusUnit

PhonePC/2in1TabletWearable

半径单位。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 6.0.0(20)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| PIXEL\_UNIT | 0 | 像素px。 |
| METER\_UNIT | 1 | 米。 |

## WeightedLatLng

PhonePC/2in1TabletWearable

加权经纬度。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 6.0.0(20)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| point | [LatLng](map-common.md#latlng) | 否 | 否 | 经纬度。 |
| intensity | number | 否 | 是 | 强度的权重，取值范围：[0，+∞)，默认值：1，异常值按默认值处理。 |

## TileProvider

PhonePC/2in1TabletWearable

type TileProvider = (x: number, y: number, z: number) => Promise<ArrayBuffer>

根据瓦片坐标获取瓦片。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 6.0.0(20)

| **名称** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| x | number | 是 | X坐标。 |
| y | number | 是 | Y坐标。 |
| z | number | 是 | Z坐标。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<ArrayBuffer> | Promise对象，返回瓦片字节。 |

## MvtOverlayParams

PhonePC/2in1Tablet

矢量图层的参数。继承[BaseOverlayOptions](map-common.md#baseoverlayoptions)。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Map.Core.EnhancedOverlay

**起始版本：** 6.0.0(20)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| source | [MvtSource](map-common.md#mvtsource) | 否 | 否 | 矢量图层的来源。  元服务API：从版本6.0.0(20)开始，该接口支持在元服务中使用。 |
| layers | [MvtLayer](map-common.md#mvtlayer)[] | 否 | 否 | 样式数组，建议矢量图层少于2000层，确保矢量图层的流畅度。  元服务API：从版本6.0.0(20)开始，该接口支持在元服务中使用。 |
| blurIntensity | number | Record<number, number> | 否 | 是 | 矢量图层的模糊度，不支持3D地球。  模糊度范围：[0, 20]，小数向下取整，默认值为0，异常值按默认值处理。  若传数字，表示所有缩放层级按同一模糊度处理。  若传键值对，key为缩放层级，value为模糊度，有效层级范围：[2，20]，层级异常值大于20取20，小于2取2。例如：{ 5: 5, 10: 8, 18: 15}，2到4层级为0，默认不模糊，5到9层级模糊度为5，10到17层级模糊度为8，18到20层级模糊度为15。  **起始版本：** 6.0.2(22)  **元服务API：** 从版本6.0.2(22)开始，该接口支持在元服务中使用。 |

## MvtSource

PhonePC/2in1Tablet

矢量图层的来源。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core.EnhancedOverlay

**起始版本：** 6.0.0(20)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| tileUrl | string | 否 | 是 | 矢量图层的数据下载URL模板。URL必须包含占位符{x}、{y}和{z}。  **说明：**  使用在线下载方式添加矢量图层时（即使用tileUrl方式），需要申请访问网络的权限：ohos.permission.INTERNET。 |
| tileProvider | [TileProvider](map-common.md#tileprovider) | 否 | 是 | 根据瓦片坐标获取瓦片。 |
| minZoom | number | 否 | 是 | 最小缩放层级，默认值：2。 |
| maxZoom | number | 否 | 是 | 最大缩放层级，默认值：20。 |

## MvtLayer

PhonePC/2in1Tablet

样式数组，用于配置样式。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core.EnhancedOverlay

**起始版本：** 6.0.0(20)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| id | string | 否 | 否 | 唯一标识，用于添加、更新或移除图层。 |
| type | [MvtLayerType](map-common.md#mvtlayertype) | 否 | 否 | 矢量图层类型。 |
| sourceLayer | string | 否 | 否 | 矢量图层数据中图层的名称。 |
| paint | [MvtPaint](map-common.md#mvtpaint) | 否 | 是 | 用于配置几何体的渲染，如填充、描边等。 |

## MvtPaint

PhonePC/2in1Tablet

用于配置几何体的渲染，如填充、描边等。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core.EnhancedOverlay

**起始版本：** 6.0.0(20)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| fillColor | number | [Expression](map-common.md#expression) | 否 | 是 | 填充颜色，默认值：0x000000，异常值按默认值处理。支持：  - 十六进制RGB格式。  - 从矢量图层数据的属性中读取。 |
| fillOpacity | number | [Expression](map-common.md#expression) | 否 | 是 | 填充不透明度，默认值：0，异常值按默认值处理。支持：  - 介于0到1之间的数字。  - 从矢量图层数据的属性中读取。 |

## MvtLayerType

PhonePC/2in1Tablet

矢量图层类型。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core.EnhancedOverlay

**起始版本：** 6.0.0(20)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| FILL | 'fill' | 填充多边形。 |

## Expression

PhonePC/2in1Tablet

矢量图层叠加表达式。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core.EnhancedOverlay

**起始版本：** 6.0.0(20)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| operator | [Operator](map-common.md#operator) | 否 | 否 | 操作符。 |
| args | string | string[] | [Expression](map-common.md#expression)[] | 否 | 否 | 参数。  **说明：**  string[]和[Expression](map-common.md#expression)[]类型为预留类型，将来使用。 |

## Operator

PhonePC/2in1Tablet

操作符。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core.EnhancedOverlay

**起始版本：** 6.0.0(20)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| GET | 'get' | 获取操作符。 |

## FlowFieldOverlayParams

PhonePC/2in1Tablet

流场图层的参数。继承[BaseOverlayOptions](map-common.md#baseoverlayoptions)。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core.EnhancedOverlay

**起始版本：** 6.0.0(20)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| data | string | 否 | 否 | 流场图层的数据，数据格式参见[流场数据格式参考](../harmonyos-guides/map-flow-field.md#流场数据格式参考)。 |
| style | [ParticleStyle](map-common.md#particlestyle) | 否 | 是 | 粒子样式。 |

## ParticleStyle

PhonePC/2in1Tablet

粒子样式。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core.EnhancedOverlay

**起始版本：** 6.0.0(20)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| count | number | 否 | 是 | 粒子数，默认值：2000，异常值按默认值处理，建议小于10000。 |
| color | number | 否 | 是 | 粒子颜色，ARGB格式，默认值：0xffff69b4，异常值按默认值处理。 |
| maxSpeed | number | 否 | 是 | 粒子最大速度，默认值：70，单位：m/s，建议小于255，异常值按默认值处理。 |
| speedFactor | number | 否 | 是 | 粒子速度因子，取值范围[0,1]，默认值：0.2，异常值按默认值处理。 |

## MassPointItem

PhonePC/2in1TabletWearable

海量点列表。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 6.0.0(20)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| itemId | string | 否 | 否 | 项目的唯一标识符。 |
| position | [LatLng](map-common.md#latlng) | 否 | 否 | 项目的经纬度坐标。 |
| title | string | 否 | 是 | 标题。 |
| snippet | string | 否 | 是 | 点的内容。 |

## MassPointOverlayParams

PhonePC/2in1TabletWearable

海量点的参数。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 6.0.0(20)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| id | string | 否 | 否 | 海量点的唯一标识。 |
| items | [MassPointItem](map-common.md#masspointitem)[] | 否 | 否 | 海量点列表（建议数据量小于100000条）。 |
| icon | [ResourceStr](ts-types.md#resourcestr) | [image.PixelMap](arkts-apis-image-pixelmap.md) | 否 | 否 | 海量点的图标。 |
| anchorU | number | 否 | 是 | 图标锚点在水平方向上的位置，取值范围：[0, 1]，默认值：0.5。 |
| anchorV | number | 否 | 是 | 图标锚点在垂直方向上的位置，取值范围：[0, 1]，默认值：0.5。 |

## MapType

PhonePC/2in1TabletWearable

地图类型。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| STANDARD | 0 | 标准地图，展示道路、建筑物以及河流等重要的自然特征。  **元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。 |
| NONE | 1 | 空地图，没有加载任何数据的地图。  **元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。 |
| TERRAIN | 2 | 地形图，在保留了行政区划边界、POI、楼块等地图要素的基础上，呈现完整清晰描绘地形走势的标准地图。  **元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。  **说明：**  - 地图缩放层级在大于5且小于14的区间内才能看到地形图效果。  - 地形图在智能表设备上不显示效果。 |
| SATELLITE | 3 | 卫星图，显示卫星照片的地图，只支持中国。  **起始版本：** 6.0.0(20)  **元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。 |
| HYBRID | 4 | 混合地图，在显示卫星照片的同时也显示路网信息。  **起始版本：** 6.0.0(20)  **元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。 |

## PatternItemType

PhonePC/2in1TabletWearable

描述圆、多边形或折线的边框样式类型。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| DASH | 0 | 表示折线、多边形或圆的边框中的短划线。 |
| DOT | 1 | 表示折线、多边形或圆的边框的点。 |
| GAP | 2 | 表示折线、多边形或圆中边框的间隙。 |

## JointType

PhonePC/2in1TabletWearable

折线、多边形的拐角绘制样式。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| DEFAULT | 0 | 使用尖角连接路径段。 |
| BEVEL | 1 | 使用斜角连接路径段。 |
| ROUND | 2 | 使用圆角连接路径段。 |

## LogoAlignment

PhonePC/2in1TabletWearable

地图Logo的对齐方式。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| BOTTOM\_START | 0 | 将Logo放置在左下角位置。  **元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。 |
| BOTTOM\_END | 1 | 将Logo放置在右下角位置。  **元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。 |
| TOP\_START | 2 | 将Logo放置在左上角位置。  **元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。 |
| TOP\_END | 3 | 将Logo放置在右上角位置。  **元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。 |
| TOP\_CENTER | 4 | 将Logo放置在上方居中位置。  **起始版本：** 5.1.1(19)  **元服务API：** 从版本5.1.1(19)开始，该接口支持在元服务中使用。 |
| BOTTOM\_CENTER | 5 | 将Logo放置在底部居中位置。  **起始版本：** 5.1.1(19)  **元服务API：** 从版本5.1.1(19)开始，该接口支持在元服务中使用。 |

## CapStyle

PhonePC/2in1TabletWearable

用于自定义折线端点（起始顶点和末端顶点）样式。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| BUTT | 0 | 线的两端是平行线。 |
| ROUND | 1 | 在线的两端延长半圆。 |
| SQUARE | 2 | 在线的两端延伸一个矩形。 |

## CollisionRule

PhonePC/2in1TabletWearable

地图POI之间的碰撞规则。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NONE | 0 | 名称和图标都不参与碰撞。  **元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。 |
| NAME | 1 | 仅名称参与碰撞。  **元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。 |
| ALL | 2 | 图标和名称都参与碰撞。  **元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。 |
| ICON\_CASCADE | 3 | 图标碰撞规则。只有标记（Marker）支持此规则。  **起始版本：** 6.1.0(23)  **元服务API：** 从版本6.1.0(23)开始，该接口支持在元服务中使用。 |

## FontStyle

PhonePC/2in1TabletWearable

点注释标题的字体样式。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| REGULAR | 0 | regular（常规粗细）。 |
| BOLD | 1 | bold（加粗）。 |
| ITALIC | 2 | italic（斜体）。 |
| BOLD\_ITALIC | 3 | bold and italic（斜体加粗）。 |
| MEDIUM | 4 | medium（中等粗细）。 |
| MEDIUM\_ITALIC | 5 | medium and italic（斜体，中等粗细）。 |

## CoordinateType

PhonePC/2in1TabletWearable

坐标系类型。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| WGS84 | 0 | WGS84坐标系。 |
| GCJ02 | 1 | GCJ02坐标系。 |

## MyLocationDisplayType

PhonePC/2in1TabletWearable

定位图标的展示模式。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| DEFAULT | 0 | 连续定位，相机不移动到我的位置，定位蓝点跟踪设备移动。  **元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。 |
| LOCATE | 1 | 定位一次，且将相机移动到地图中心点。  **元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。 |
| FOLLOW | 2 | 连续定位，且将相机移动到地图中心点，定位蓝点跟随设备移动。  **元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。 |
| FOLLOW\_ROTATE | 3 | 连续定位，且将相机移动到地图中心点，定位蓝点依照设备方向旋转，并且会跟随设备移动。  **元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。  **说明：**  使用FOLLOW\_ROTATE需应用申请传感器权限：ohos.permission.ACCELEROMETER。 |
| TRACK\_ROTATE | 4 | 连续定位，位置图标会跟随设备的移动并根据设备方向旋转，但不会移动到地图中心。  **起始版本：** 6.0.0(20)  **元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。  **说明：**  使用FOLLOW\_ROTATE需应用申请传感器权限：ohos.permission.ACCELEROMETER。 |

## DayNightMode

PhonePC/2in1TabletWearable

地图日间夜间模式。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| DAY | 0 | 日间模式。 |
| NIGHT | 1 | 夜间模式。 |
| AUTO | 2 | 自动模式，如果系统打开深色开关，显示夜间模式，否则显示日间模式。 |

## ScaleUnit

PhonePC/2in1TabletWearable

地图比例尺公英制单位。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.1.1(19)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.1.1(19)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| METRIC\_UNIT | 0 | 公制单位。 |
| IMPERIAL\_UNIT | 1 | 英制单位。 |

## TextPosition

PhonePC/2in1TabletWearable

设置点注释的文本位置。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| DEFAULT | 0 | 默认模式。 |
| TOP | 1 | 文本显示在图标上方。 |
| BOTTOM | 2 | 文本显示在图标下方。 |
| LEFT | 3 | 文本显示在图标的左侧。 |
| RIGHT | 4 | 文本显示在图标的右侧。 |

## MapElementType

PhonePC/2in1TabletWearable

地图元素类型。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| OVERLAY | 1 | 覆盖物，包括[MapCircle](map-map-mapcircle.md)、[MapPolygon](map-map-mappolygon.md)、[MapPolyline](map-map-mappolyline.md)、[MapArc](map-map-maparc.md)、[ImageOverlay](map-map-imageoverlay.md)、[TraceOverlay](map-map-traceoverlay.md)。 |
| POI | 2 | 底图[Poi](map-common.md#poi)。 |
| CUSTOM\_POI | 3 | 支持碰撞的覆盖物，包括[PointAnnotation](map-map-pointannotation.md)、[Bubble](map-map-bubble.md)。 |
| MARKER | 4 | 包括[Marker](map-map-marker.md)、[ClusterOverlay](map-map-clusteroverlay.md)。 |
