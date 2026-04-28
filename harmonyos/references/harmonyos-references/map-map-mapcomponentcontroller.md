---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-map-mapcomponentcontroller
title: MapComponentController
breadcrumb: API参考 > 应用服务 > Map Kit（地图服务） > ArkTS API > map（地图显示功能） > MapComponentController
category: harmonyos-references
scraped_at: 2026-04-28T08:17:11+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:cdd36a1d59d9834d4b645ff6981e9b198439b3c258addb2ee47c831151831e7c
---

## 导入模块

PhonePC/2in1TabletWearable

```
1. import { map, mapCommon } from '@kit.MapKit';
```

## MapComponentController

PhonePC/2in1TabletWearable

地图的主要功能入口类，与地图有关的所有方法从此处接入，并提供事件监听管理功能。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**示例：**

```
1. import { MapComponent, mapCommon, map } from '@kit.MapKit';
2. import { AsyncCallback } from '@kit.BasicServicesKit';

4. @Entry
5. @Component
6. struct HuaweiMapDemo {
7. private TAG = "HuaweiMapDemo";
8. private mapOptions?: mapCommon.MapOptions;
9. private callback?: AsyncCallback<map.MapComponentController>;
10. private mapController?: map.MapComponentController;
11. private mapEventManager?: map.MapEventManager;

13. aboutToAppear(): void {
14. // 地图初始化参数，设置地图中心点坐标及层级
15. this.mapOptions = {
16. position: {
17. target: {
18. latitude: 39.9,
19. longitude: 116.4
20. },
21. zoom: 10
22. }
23. };

25. // 地图初始化的回调
26. this.callback = async (err, mapController) => {
27. if (!err) {
28. // 获取地图的控制器类，用来操作地图
29. this.mapController = mapController;
30. // 返回地图组件的监听事件管理接口
31. this.mapEventManager = this.mapController.getEventManager();
32. let callback = () => {
33. console.info(this.TAG, `on-mapLoad`);
34. }
35. this.mapEventManager.on("mapLoad", callback);

37. // 执行自定义的方法
38. this.customizedMethod();
39. }
40. };
41. }

43. // 自定义的方法
44. private customizedMethod() {
45. // ...
46. }

48. build() {
49. Stack() {
50. // 调用MapComponent组件初始化地图
51. MapComponent({ mapOptions: this.mapOptions, mapCallback: this.callback })
52. .width('100%')
53. .height('100%')
54. }.height('100%')
55. }
56. }
```

说明

MapComponentController中的方法需要放在上述示例的地图初始化的回调中运行或自定义的方法中运行。

### animateCamera

PhonePC/2in1TabletWearable

animateCamera(update: CameraUpdate, duration?: number): void

在指定的持续时间内以动画的形式更新相机状态。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| update | [CameraUpdate](map-map-cameraupdate.md) | 是 | 相机状态将要发生的变化，异常值不处理。 |
| duration | number | 否 | 动画的持续时间，单位：ms，默认值为250，取值范围：大于0，异常值按默认值处理。 |

**示例：**

```
1. let target: mapCommon.LatLng = {
2. latitude: 39.9,
3. longitude: 116.4
4. };
5. let cameraPosition: mapCommon.CameraPosition = {
6. target: target,
7. zoom: 10
8. };
9. // 新建CameraUpdate对象
10. let cameraUpdate: map.CameraUpdate = map.newCameraPosition(cameraPosition);
11. // 在1000ms内以动画的形式移动相机
12. this.mapController.animateCamera(cameraUpdate, 1000);
```

### animateCameraStatus

PhonePC/2in1TabletWearable

animateCameraStatus(update: CameraUpdate, duration?: number): Promise<AnimateResult>

在指定的持续时间内以动画的形式更新相机状态，并返回动画结果。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| update | [CameraUpdate](map-map-cameraupdate.md) | 是 | 相机状态将要发生的变化，异常值返回401错误码。 |
| duration | number | 否 | 动画的持续时间，单位：ms，默认值为250，取值范围：大于0，异常值按默认值处理。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[AnimateResult](map-map-animateresult.md)> | Promise对象，返回[AnimateResult](map-map-animateresult.md)。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-map.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid input parameter. |

**示例：**

```
1. let target: mapCommon.LatLng = {
2. latitude: 39.9,
3. longitude: 116.4
4. };
5. let cameraPosition: mapCommon.CameraPosition = {
6. target: target,
7. zoom: 10
8. };
9. // 新建CameraUpdate对象
10. let cameraUpdate: map.CameraUpdate = map.newCameraPosition(cameraPosition);
11. // 在1000ms内以动画的形式移动相机
12. let animateResult = await this.mapController.animateCameraStatus(cameraUpdate, 1000);
```

### animateCameraWithMarker

PhonePC/2in1TabletWearable

animateCameraWithMarker(update: CameraUpdate, marker: Marker, duration: number): Promise<AnimateResult>

在指定的持续时间内以动画的形式更新相机状态，并更新指定的marker。使用Promise异步回调。相机移动过程中不能被打断，否则[AnimateResult](map-map-animateresult.md)的参数isCanceled返回值为true。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| update | [CameraUpdate](map-map-cameraupdate.md) | 是 | 相机状态将要发生的变化，异常值不处理。 |
| marker | [Marker](map-map-marker.md) | 是 | 标记，异常值不处理。 |
| duration | number | 是 | 动画的持续时间，单位：ms，默认值为250，取值范围：大于0，异常值按默认值处理。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[AnimateResult](map-map-animateresult.md)> | Promise对象，返回[AnimateResult](map-map-animateresult.md)。 |

**示例：**

```
1. let target: mapCommon.LatLng = {
2. latitude: 39.9,
3. longitude: 116.4
4. };
5. let cameraPosition: mapCommon.CameraPosition = {
6. target: target,
7. zoom: 10
8. };
9. // 新建CameraUpdate对象
10. let cameraUpdate: map.CameraUpdate = map.newCameraPosition(cameraPosition);
11. // marker初始化参数
12. let markerOptions: mapCommon.MarkerOptions = {
13. position: {
14. latitude: 39.9,
15. longitude: 116.4
16. },
17. title: "XXX",
18. // 图标需存放在resources/rawfile目录下
19. icon: 'icon/icon.png',
20. clickable: true
21. };
22. // 新建marker
23. let marker = await this.mapController?.addMarker(markerOptions);
24. // 在1000ms内以动画的形式移动相机, 并更新指定的marker
25. await this.mapController.animateCameraWithMarker(cameraUpdate, marker, 1000);
```

### animateCameraWithMarkers

PhonePC/2in1TabletWearable

animateCameraWithMarkers(update: CameraUpdate, markers: Array<Marker>, duration: number): Promise<AnimateResult>

在指定的持续时间内以动画的形式更新相机状态，并更新传入的marker，支持传一组标记。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| update | [CameraUpdate](map-map-cameraupdate.md) | 是 | 相机状态将要发生的变化，异常值返回401错误码。 |
| markers | Array<[Marker](map-map-marker.md)> | 是 | 一组标记。  **说明：**  一组标记的位置必须相同，否则会返回401错误码。 |
| duration | number | 是 | 动画的持续时间，单位：ms，默认值为250，取值范围：大于0，异常值按默认值处理。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[AnimateResult](map-map-animateresult.md)> | Promise对象，返回[AnimateResult](map-map-animateresult.md)。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-map.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid input parameter. |

**示例：**

```
1. let target: mapCommon.LatLng = {
2. latitude: 39.9,
3. longitude: 116.4
4. };
5. let cameraPosition: mapCommon.CameraPosition = {
6. target: target,
7. zoom: 10
8. };
9. // 新建CameraUpdate对象
10. let cameraUpdate: map.CameraUpdate = map.newCameraPosition(cameraPosition);
11. // marker1初始化参数
12. let markerOptions1: mapCommon.MarkerOptions = {
13. position: {
14. latitude: 31.984410259206815,
15. longitude: 118.76625379397866
16. },
17. title: "icon",
18. // 图标需存放在resources/rawfile目录下
19. icon: 'icon/icon.png',
20. clickable: true
21. };
22. let markerOptions2: mapCommon.MarkerOptions = {
23. position: {
24. latitude: 31.984410259206815,
25. longitude: 118.76625379397866
26. },
27. title: "avocado",
28. // 图标需存放在resources/rawfile目录下
29. icon: 'icon/avocado.png',
30. clickable: true,
31. anchorU: 0.5,
32. anchorV: 1
33. };
34. let marker1 = await this.mapController?.addMarker(markerOptions1);
35. // marker2初始化参数
36. let marker2 = await this.mapController?.addMarker(markerOptions2);
37. // 在1000ms内以动画的形式移动相机, 并更新指定的marker
38. await this.mapController.animateCameraWithMarkers(cameraUpdate, [marker1, marker2], 1000);
```

### stopAnimation

PhonePC/2in1TabletWearable

stopAnimation(): void

停止当前执行的改变地图状态的动画。调用该方法时，相机立即停止移动并保持在该位置。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**示例：**

```
1. this.mapController.stopAnimation();
```

### clear

PhonePC/2in1TabletWearable

clear(): void

移除地图上所有的圆、标记、折线等覆盖物。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**示例：**

```
1. this.mapController.clear();
```

### moveCamera

PhonePC/2in1TabletWearable

moveCamera(update: CameraUpdate): void

更新相机状态。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| update | [CameraUpdate](map-map-cameraupdate.md) | 是 | 相机状态将要发生的变化，异常值不处理。 |

**示例：**

```
1. let target: mapCommon.LatLng = {
2. latitude: 39.9,
3. longitude: 116.4
4. };
5. let cameraPosition: mapCommon.CameraPosition = {
6. target: target,
7. zoom: 10
8. };
9. // 新建CameraUpdate对象
10. let cameraUpdate: map.CameraUpdate = map.newCameraPosition(cameraPosition);
11. // 移动相机
12. this.mapController.moveCamera(cameraUpdate);
```

### getCameraPosition

PhonePC/2in1TabletWearable

getCameraPosition(): mapCommon.CameraPosition

获取相机的当前状态信息。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [mapCommon.CameraPosition](map-common.md#cameraposition) | 相机的当前状态信息。 |

**示例：**

```
1. let cameraPosition: mapCommon.CameraPosition = this.mapController.getCameraPosition();
```

### setLatLngBounds

PhonePC/2in1TabletWearable

setLatLngBounds(bounds: mapCommon.LatLngBounds): void

指定一个[mapCommon.LatLngBounds](map-common.md#latlngbounds)来约束相机目标，使用户移动地图时，相机目标不会移出此边界。当设置新的边界时，新边界将覆盖之前设置的边界。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| bounds | [mapCommon.LatLngBounds](map-common.md#latlngbounds) | 是 | 约束相机目标的边界，异常值不处理。  **说明：**  西南角纬度大于东北角纬度时不生效。 |

**示例：**

```
1. let bounds:mapCommon.LatLngBounds = {
2. northeast: {
3. latitude: 31,
4. longitude: 118
5. },
6. southwest: {
7. latitude: 30,
8. longitude: 117
9. }
10. };
11. this.mapController.setLatLngBounds(bounds);
```

### setPointToCenter

PhonePC/2in1TabletWearable

setPointToCenter(point: mapCommon.MapPoint): void

将屏幕上的像素位置设置为地图的中心点。使用此方法后，地图将根据设置的屏幕坐标进行缩放和旋转。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| point | [mapCommon.MapPoint](map-common.md#mappoint) | 是 | 屏幕坐标点，异常值不处理。 |

**示例：**

```
1. let point: mapCommon.MapPoint = {
2. positionX: 1000,
3. positionY: 1000
4. };
5. this.mapController.setPointToCenter(point);
```

### setMaxZoom

PhonePC/2in1TabletWearable

setMaxZoom(maxZoom: number): void

设置相机最大缩放级别。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| maxZoom | number | 是 | 相机最大缩放级别。取值范围：[2, 20]，超出此范围时，系统自动调整为边界值。  在取值范围内，传入的值小于当前minZoom，最大缩放级别和最小缩放级别都会被设置为当前传入的值。异常值不处理。 |

**示例：**

```
1. this.mapController.setMaxZoom(10);
```

### setMinZoom

PhonePC/2in1TabletWearable

setMinZoom(minZoom: number): void

设置相机最小缩放级别。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| minZoom | number | 是 | 相机最小缩放级别。取值范围：[2, 20]，超出此范围时，系统自动调整为边界值。  在取值范围内，传入的值大于当前maxZoom，最大缩放级别和最小缩放级别都会被设置为当前传入的值。异常值不处理。 |

**示例：**

```
1. this.mapController.setMinZoom(3);
```

### getMaxZoom

PhonePC/2in1TabletWearable

getMaxZoom(): number

获取相机最大缩放级别。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 相机最大缩放级别。 |

**示例：**

```
1. let maxZoom: number = this.mapController.getMaxZoom();
```

### getMinZoom

PhonePC/2in1TabletWearable

getMinZoom(): number

获取相机最小缩放级别。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 相机最小缩放级别。 |

**示例：**

```
1. let minZoom: number = this.mapController.getMinZoom();
```

### setTrafficEnabled

PhonePC/2in1TabletWearable

setTrafficEnabled(enabled: boolean): void

打开或关闭路况图层。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| enabled | boolean | 是 | 打开或关闭路况图层，异常值不处理。  - true：打开路况图层  - false：关闭路况图层 |

**示例：**

```
1. this.mapController.setTrafficEnabled(true);
```

### isTrafficEnabled

PhonePC/2in1TabletWearable

isTrafficEnabled(): boolean

获取路况图层开启状态。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | - true：路况图层为开启状态  - false：路况图层为关闭状态 |

**示例：**

```
1. let isTrafficEnabled: boolean = this.mapController.isTrafficEnabled();
```

### setBuildingEnabled

PhonePC/2in1TabletWearable

setBuildingEnabled(enabled: boolean): void

打开或者关闭3D建筑图层。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| enabled | boolean | 是 | 打开或者关闭3D建筑图层，异常值不处理。  - true：打开3D建筑图层  - false：关闭3D建筑图层  **说明：**  打开3D建筑图层后将地图缩放层级调整为16级或以上，即可展现3D图层效果。 |

**示例：**

```
1. this.mapController.setBuildingEnabled(true);
```

### isBuildingEnabled

PhonePC/2in1TabletWearable

isBuildingEnabled(): boolean

获取3D建筑图层开启状态。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | - true：3D建筑图层为开启状态  - false：3D建筑图层为关闭状态 |

**示例：**

```
1. let isBuildingEnabled: boolean = this.mapController.isBuildingEnabled();
```

### setMyLocationEnabled

PhonePC/2in1TabletWearable

setMyLocationEnabled(myLocationEnabled: boolean): void

我的位置图层功能开关，默认使用系统的连续定位能力显示用户位置。开关打开后，“我的位置”按钮默认显示在地图的右下角。点击“我的位置”按钮，将会在屏幕中心显示当前定位，以蓝色圆点的形式呈现。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| myLocationEnabled | boolean | 是 | 我的位置图层功能开关，异常值不处理。  - true：启用我的位置图层  - false：禁用我的位置图层 |

**示例：**

```
1. this.mapController.setMyLocationEnabled(true);
```

### setMyLocation

PhonePC/2in1TabletWearable

setMyLocation(location: geoLocationManager.Location): void

Map Kit默认使用系统的连续定位能力显示用户位置，如果您希望定制显示频率或者精准度，可以调用此接口设置我的位置坐标。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| location | [geoLocationManager.Location](js-apis-geolocationmanager.md#location) | 是 | 用户的位置，异常值不处理。  **说明：**  location参数需使用WGS84坐标系。 |

**示例：**

```
1. // 需要引入@kit.LocationKit模块
2. import { geoLocationManager } from '@kit.LocationKit';

4. let location = await geoLocationManager.getCurrentLocation();
5. this.mapController.setMyLocation(location);
```

### setMyLocationStyle

PhonePC/2in1TabletWearable

setMyLocationStyle(style: mapCommon.MyLocationStyle): Promise<void>

设置用户的位置样式。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| style | [mapCommon.MyLocationStyle](map-common.md#mylocationstyle) | 是 | 用户的位置样式，异常值不处理。  **说明：**  如果displayType使用FOLLOW\_ROTATE需应用申请传感器权限：ohos.permission.ACCELEROMETER，具体可参考[声明权限](../harmonyos-guides/declare-permissions.md)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**示例：**

```
1. let style: mapCommon.MyLocationStyle = {
2. anchorU: 0.5,
3. anchorV: 0.5,
4. radiusFillColor: 0xffff0000,
5. // icon为自定义图标资源，使用时需要替换，图标存放在resources/rawfile
6. icon: 'icon/avocado.png'
7. };
8. await this.mapController.setMyLocationStyle(style);
```

### isMyLocationEnabled

PhonePC/2in1TabletWearable

isMyLocationEnabled(): boolean

获取我的位置图层的开启状态。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 我的位置图层的开启状态。  - true：启用  - false：禁用 |

**示例：**

```
1. let isMyLocationEnabled: boolean = this.mapController.isMyLocationEnabled();
```

### setZoomGesturesEnabled

PhonePC/2in1TabletWearable

setZoomGesturesEnabled(enabled: boolean): void

设置是否启用缩放手势。默认情况下，缩放手势处于启用状态。

* 启用状态，用户可以使用以下手势缩放相机：

  1. 单指双击可将缩放级别提高1（放大）层级，用双指单击可将缩放级别降低1（缩小）层级。
  2. 双指张合，实现放大缩小。
  3. 单指双击实现单指缩放，第二次点时按住，然后上划缩小，或下划放大。
* 禁用状态，缩放手势无效。此设置不影响缩放按钮，也不限制通过接口移动相机和相机动画。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| enabled | boolean | 是 | 设置是否启用缩放手势，异常值不处理。  - true：启用缩放手势  - false：禁用缩放手势 |

**示例：**

```
1. this.mapController.setZoomGesturesEnabled(true);
```

### isZoomGesturesEnabled

PhonePC/2in1TabletWearable

isZoomGesturesEnabled(): boolean

获取缩放手势功能的启用状态。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 缩放手势功能的启用状态。  - true：启用缩放手势  - false：禁用缩放手势 |

**示例：**

```
1. let isZoomGesturesEnabled: boolean = this.mapController.isZoomGesturesEnabled();
```

### setScrollGesturesEnabled

PhonePC/2in1TabletWearable

setScrollGesturesEnabled(enabled: boolean): void

设置是否启用滚动手势。默认情况下，滚动手势处于启用状态。

* 启用状态，用户可以通过滑动来平移相机。
* 禁用状态，滑动无效。此设置不限制通过接口移动相机和相机动画。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| enabled | boolean | 是 | 设置是否启用滚动手势，异常值不处理。  - true：启用滚动手势  - false：禁用滚动手势 |

**示例：**

```
1. this.mapController.setScrollGesturesEnabled(true);
```

### isScrollGesturesEnabled

PhonePC/2in1TabletWearable

isScrollGesturesEnabled(): boolean

获取滚动手势的启用状态。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 滚动手势的启用状态。  - true：启用滚动手势  - false：禁用滚动手势 |

**示例：**

```
1. let isScrollGesturesEnabled: boolean = this.mapController.isScrollGesturesEnabled();
```

### setRotateGesturesEnabled

PhonePC/2in1TabletWearable

setRotateGesturesEnabled(enabled: boolean): void

设置是否启用旋转手势，默认情况下，旋转手势处于启用状态。

* 启用状态，用户可以使用两指旋转手势旋转相机。
* 禁用状态，用户将无法通过手势旋转相机。此设置不限制用户点击指南针图标以重置相机方向，也不限制通过接口移动相机和相机动画。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| enabled | boolean | 是 | 设置是否启用旋转手势，异常值不处理。  - true：启用旋转手势  - false：禁用旋转手势 |

**示例：**

```
1. this.mapController.setRotateGesturesEnabled(true);
```

### isRotateGesturesEnabled

PhonePC/2in1TabletWearable

isRotateGesturesEnabled(): boolean

获取旋转手势的启用状态。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 旋转手势的启用状态。  - true：启用旋转手势  - false：禁用旋转手势 |

**示例：**

```
1. let isRotateGesturesEnabled: boolean = this.mapController.isRotateGesturesEnabled();
```

### setTiltGesturesEnabled

PhonePC/2in1TabletWearable

setTiltGesturesEnabled(enabled: boolean): void

设置是否启用倾斜手势，默认情况下，倾斜手势处于启用状态。

* 启用状态，用户可以使用两指垂直向上或者向下滑动来倾斜相机。
* 禁用状态，用户无法通过手势来倾斜相机。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| enabled | boolean | 是 | 设置是否启用倾斜手势，异常值不处理。  - true：启用倾斜手势  - false：禁用倾斜手势 |

**示例：**

```
1. this.mapController.setTiltGesturesEnabled(true);
```

### isTiltGesturesEnabled

PhonePC/2in1TabletWearable

isTiltGesturesEnabled(): boolean

获取倾斜手势的启用状态。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 倾斜手势的启用状态。  - true：启用倾斜手势  - false：禁用倾斜手势 |

**示例：**

```
1. let isTiltGesturesEnabled: boolean = this.mapController.isTiltGesturesEnabled();
```

### setZoomControlsEnabled

PhonePC/2in1TabletWearable

setZoomControlsEnabled(enabled: boolean): void

设置是否启用缩放控制器，默认情况下，缩放控件处于启用状态。

* 启用状态，地图上会出现由一对按钮组成的缩放控件（用于缩放地图）。点击按钮时，会使相机放大（或缩小）一个缩放级别。
* 禁用状态，不会显示缩放控件。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| enabled | boolean | 是 | 设置是否启用缩放控制器，异常值不处理。  - true：启用缩放控制器  - false：禁用缩放控制器 |

**示例：**

```
1. this.mapController.setZoomControlsEnabled(true);
```

### isZoomControlsEnabled

PhonePC/2in1TabletWearable

isZoomControlsEnabled(): boolean

获取缩放控制器的启用状态。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 缩放控制器的启用状态。  - true：启用缩放控制器  - false：禁用缩放控制器 |

**示例：**

```
1. let isZoomControlsEnabled: boolean = this.mapController.isZoomControlsEnabled();
```

### setMyLocationControlsEnabled

PhonePC/2in1TabletWearable

setMyLocationControlsEnabled(enabled: boolean): void

设置是否启用我的位置按钮。只显示按钮，在不开启我的位置图层功能的情况下，点击按钮没反应。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| enabled | boolean | 是 | 设置是否启用我的位置按钮，异常值不处理。  - true：启用我的位置按钮  - false：禁用我的位置按钮 |

**示例：**

```
1. this.mapController.setMyLocationControlsEnabled(true);
```

### isMyLocationControlsEnabled

PhonePC/2in1TabletWearable

isMyLocationControlsEnabled(): boolean

获取我的位置按钮的启用状态。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 我的位置按钮的启用状态。  - true：启用  - false：禁用 |

**示例：**

```
1. let isMyLocationControlsEnabled: boolean = this.mapController.isMyLocationControlsEnabled();
```

### setScaleControlsEnabled

PhonePC/2in1TabletWearable

setScaleControlsEnabled(enabled: boolean): void

设置是否启用比例尺。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| enabled | boolean | 是 | 设置是否启用比例尺，异常值不处理。  - true：启用比例尺  - false：禁用比例尺 |

**示例：**

```
1. this.mapController.setScaleControlsEnabled(true);
```

### isScaleControlsEnabled

PhonePC/2in1TabletWearable

isScaleControlsEnabled(): boolean

获取比例尺的启用状态。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 比例尺的启用状态。  - true：启用  - false：禁用 |

**示例：**

```
1. let isScaleControlsEnabled: boolean = this.mapController.isScaleControlsEnabled();
```

### setCompassControlsEnabled

PhonePC/2in1TabletWearable

setCompassControlsEnabled(enabled: boolean): void

设置是否启用指南针。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| enabled | boolean | 是 | 设置是否启用指南针，异常值不处理。  - true：启用指南针  - false：禁用指南针 |

**示例：**

```
1. this.mapController.setCompassControlsEnabled(true);
```

### isCompassControlsEnabled

PhonePC/2in1TabletWearable

isCompassControlsEnabled(): boolean

获取指南针的启用状态。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 指南针的启用状态。  - true：启用  - false：禁用 |

**示例：**

```
1. let isCompassControlsEnabled: boolean = this.mapController.isCompassControlsEnabled();
```

### setGestureScaleByMapCenter

PhonePC/2in1TabletWearable

setGestureScaleByMapCenter(enabled: boolean): void

设置以固定屏幕中心点进行缩放功能是否可用，默认是禁用状态。

* 启用状态，地图将以传入的固定屏幕点进行缩放。通过[setPointToCenter](map-map-mapcomponentcontroller.md#setpointtocenter)方法设置屏幕中心点坐标。
* 禁用状态，将以手指点击的位置为中心进行缩放。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| enabled | boolean | 是 | 设置以固定屏幕中心点进行缩放功能是否可用，异常值不处理。  - true：启用，地图将以传入的固定屏幕点进行缩放。  - false：禁用，地图将以手指点击的位置为中心进行缩放。 |

**示例：**

```
1. this.mapController.setGestureScaleByMapCenter(true);
```

### isGestureScaleByMapCenter

PhonePC/2in1TabletWearable

isGestureScaleByMapCenter(): boolean

获取以固定屏幕中心点进行缩放功能的开启状态。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 以固定屏幕中心点进行缩放功能的开启状态。  - true：启用  - false：禁用 |

**示例：**

```
1. let isGestureScaleByMapCenter: boolean = this.mapController.isGestureScaleByMapCenter();
```

### setLogoAlignment

PhonePC/2in1TabletWearable

setLogoAlignment(alignment: mapCommon.LogoAlignment): void

设置地图Logo的对齐方式。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| alignment | [mapCommon.LogoAlignment](map-common.md#logoalignment) | 是 | 地图Logo的对齐方式，异常值不处理。 |

**示例：**

```
1. this.mapController.setLogoAlignment(mapCommon.LogoAlignment.BOTTOM_START);
```

### setLogoPadding

PhonePC/2in1TabletWearable

setLogoPadding(padding: mapCommon.Padding): void

设置地图边界与Logo之间的间距。Logo的尺寸固定，不受地图缩放影响，始终以像素为单位显示。

* 当您设置的任意padding值超出范围（例如：负值，或超出边界）时被认为非法，Logo位置不变化。
* 当Logo位置在左下角时left和bottom参数生效。
* 当Logo位置在右上角时right和top参数生效，以此类推。

说明

在调整设置地图边界与Logo之间的间距时，请避免隐藏或遮盖Logo。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| padding | [mapCommon.Padding](map-common.md#padding) | 是 | 地图边界与Logo之间的间距，异常值不处理。 |

**示例：**

```
1. let padding: mapCommon.Padding = {
2. left: 0,
3. bottom: 50
4. };
5. this.mapController.setLogoPadding(padding);
```

### getScalePerPixel

PhonePC/2in1TabletWearable

getScalePerPixel(): number

获取当前缩放级别下，地图上1像素点对应的长度，单位：米。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 地图上1像素点对应的长度，单位：米。 |

**示例：**

```
1. let scalePerPixel: number = this.mapController.getScalePerPixel();
```

### addMarker

PhonePC/2in1TabletWearable

addMarker(options: mapCommon.MarkerOptions): Promise<Marker>

在地图上添加一个标记。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| options | [mapCommon.MarkerOptions](map-common.md#markeroptions) | 是 | 标记的属性设置。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[Marker](map-map-marker.md)> | Promise对象，返回[Marker](map-map-marker.md)。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-map.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid input parameter. |
| 1002601001 | The object to be operated does not exist. |
| 1002601005 | Failed to generate the icon of the customized component.  **说明：**  从6.0.0(20)版本开始。 |

**示例：**

```
1. // Marker初始化参数
2. let markerOptions: mapCommon.MarkerOptions = {
3. position: {
4. latitude: 39.9,
5. longitude: 116.4
6. },
7. rotation: 0,
8. visible: true,
9. zIndex: 0,
10. alpha: 1,
11. anchorU: 0.5,
12. anchorV: 1,
13. clickable: true,
14. draggable: true,
15. flat: false,
16. // 图标存放在resources/rawfile
17. icon: 'test.png'
18. };
19. // 在地图上添加一个marker
20. let marker: map.Marker = await this.mapController.addMarker(markerOptions);
```

### addCircle

PhonePC/2in1TabletWearable

addCircle(options: mapCommon.MapCircleOptions): Promise<MapCircle>

在地图上添加一个圆，指定圆心经纬度和圆的半径，用于表示某个位置的周边范围。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| options | [mapCommon.MapCircleOptions](map-common.md#mapcircleoptions) | 是 | 圆的属性设置。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[MapCircle](map-map-mapcircle.md)> | Promise对象，返回[MapCircle](map-map-mapcircle.md)。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-map.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid input parameter. |
| 1002601001 | The object to be operated does not exist. |

**示例：**

```
1. // Circle初始化参数
2. let mapCircleOptions: mapCommon.MapCircleOptions = {
3. center: {
4. latitude: 39.9,
5. longitude: 116.4
6. },
7. patterns: [{
8. type: 0,
9. length: 100
10. }, {
11. type: 1,
12. length: 100
13. }, {
14. type: 2,
15. length: 100
16. }],
17. radius: 700,
18. fillColor: 0XFF00FFFF,
19. strokeColor: 0xFFFF0000,
20. strokeWidth: 10,
21. zIndex: 15
22. };
23. // 在地图上添加一个Circle
24. let mapCircle: map.MapCircle = await this.mapController.addCircle(mapCircleOptions);
```

### addPolyline

PhonePC/2in1TabletWearable

addPolyline(options: mapCommon.MapPolylineOptions): Promise<MapPolyline>

在地图上添加一条折线。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| options | [mapCommon.MapPolylineOptions](map-common.md#mappolylineoptions) | 是 | 折线的属性设置。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[MapPolyline](map-map-mappolyline.md)> | Promise对象，返回[MapPolyline](map-map-mappolyline.md)。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-map.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid input parameter. |
| 1002601001 | The object to be operated does not exist. |

**示例：**

```
1. // 初始化参数
2. let polylineOption: mapCommon.MapPolylineOptions = {
3. // 折线坐标点，必传
4. points: [{
5. latitude: 31.984410,
6. longitude: 118.7662537
7. }, {
8. latitude: 31.084410,
9. longitude: 118.0662537
10. }],
11. clickable: true,
12. color: 0xff000000,
13. startCap: mapCommon.CapStyle.BUTT,
14. endCap: mapCommon.CapStyle.BUTT,
15. geodesic: false,
16. jointType: mapCommon.JointType.DEFAULT,
17. visible: true,
18. width: 10,
19. zIndex: 0,
20. gradient: false
21. };
22. // 在地图上添加一条折线
23. let mapPolyline: map.MapPolyline = await this.mapController.addPolyline(polylineOption);
```

### addPolygon

PhonePC/2in1TabletWearable

addPolygon(options: mapCommon.MapPolygonOptions): Promise<MapPolygon>

在地图上添加一个多边形。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| options | [mapCommon.MapPolygonOptions](map-common.md#mappolygonoptions) | 是 | 多边形的属性设置。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[MapPolygon](map-map-mappolygon.md)> | Promise对象，返回[MapPolygon](map-map-mappolygon.md)。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-map.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid input parameter. |
| 1002601001 | The object to be operated does not exist. |

**示例：**

```
1. // 初始化参数
2. let polygonOptions: mapCommon.MapPolygonOptions = {
3. // 多边形坐标点，必传
4. points: [{
5. latitude: 31.98441,
6. longitude: 118.066253
7. }, {
8. latitude: 31.98441,
9. longitude: 118.766253
10. }, {
11. latitude: 32.98441,
12. longitude: 118.766253
13. }, {
14. latitude: 32.98441,
15. longitude: 118.066253
16. }],
17. clickable: true,
18. fillColor: 0xff00DE00,
19. geodesic: false,
20. strokeColor: 0xff000000,
21. jointType: mapCommon.JointType.DEFAULT,
22. strokeWidth: 10,
23. visible: true,
24. zIndex: 10
25. };
26. // 在地图上添加一个多边形
27. let mapPolygon: map.MapPolygon = await this.mapController.addPolygon(polygonOptions);
```

### addPointAnnotation

PhonePC/2in1TabletWearable

addPointAnnotation(params: mapCommon.PointAnnotationParams): Promise<PointAnnotation>

在地图上添加一个点注释。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| params | [mapCommon.PointAnnotationParams](map-common.md#pointannotationparams) | 是 | 点注释的属性设置。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[PointAnnotation](map-map-pointannotation.md)> | Promise对象，返回[PointAnnotation](map-map-pointannotation.md)。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-map.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid input parameter. |
| 1002601001 | The object to be operated does not exist. |

**示例：**

```
1. let pointAnnotationOptions: mapCommon.PointAnnotationParams = {
2. // 定义点注释图标锚点
3. position: {
4. latitude: 39.918,
5. longitude: 116.397
6. },
7. // 定义点注释名称与地图POI名称相同时，是否支持去重
8. repeatable: true,
9. // 定义点注释的碰撞规则
10. collisionRule: mapCommon.CollisionRule.NAME,
11. // 定义点注释的标题，数组长度最小为1，最大为3
12. titles: [{
13. // 定义标题内容
14. content: "Title1",
15. // 定义标题字体颜色
16. color: 0xFF000000,
17. // 定义标题字体大小
18. fontSize: 15,
19. // 定义标题描边颜色
20. strokeColor: 0xFFFFFFFF,
21. // 定义标题描边宽度
22. strokeWidth: 2,
23. // 定义标题字体样式
24. fontStyle: mapCommon.FontStyle.ITALIC
25. }],
26. // 定义点注释的图标，图标存放在resources/rawfile
27. icon: "icon/avocado.png",
28. // 定义点注释是否展示图标
29. showIcon: true,
30. // 定义点注释的锚点在水平方向上的位置
31. anchorU: 0.5,
32. // 定义点注释的锚点在垂直方向上的位置
33. anchorV: 1,
34. // 定义点注释的显示属性，为true时，在被碰撞后仍能显示
35. forceVisible: false,
36. // 定义碰撞优先级，数值越大，优先级越低
37. priority: 3,
38. // 定义点注释展示的最小层级
39. minZoom: 2,
40. // 定义点注释展示的最大层级
41. maxZoom: 20,
42. // 定义点注释是否可见
43. visible: true,
44. // 定义点注释叠加层级属性
45. zIndex: 10
46. };
47. let pointAnnotation: map.PointAnnotation = await this.mapController.addPointAnnotation(pointAnnotationOptions);
```

### addBubble

PhonePC/2in1TabletWearable

addBubble(params: mapCommon.BubbleParams): Promise<Bubble>

在地图上添加气泡。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| params | [mapCommon.BubbleParams](map-common.md#bubbleparams) | 是 | 气泡的属性设置。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[Bubble](map-map-bubble.md)> | Promise对象，返回[Bubble](map-map-bubble.md)。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-map.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid input parameter. |
| 1002601001 | The object to be operated does not exist. |

**示例：**

```
1. let bubbleOptions: mapCommon.BubbleParams = {
2. // 气泡位置
3. positions: [[{ latitude: 31, longitude: 118 }]],
4. // 气泡图标，需要传4个方向的图标，图标存放在resources/rawfile
5. icons: [
6. 'icon.png',
7. 'icon.png',
8. 'icon.png',
9. 'icon.png'
10. ],
11. // 定义气泡的显示属性，为true时，在被碰撞后仍能显示
12. forceVisible: true,
13. // 定义气泡碰撞优先级，数值越大，优先级越低
14. priority: 3,
15. // 定义气泡展示的最小层级
16. minZoom: 2,
17. // 定义气泡展示的最大层级
18. maxZoom: 20,
19. // 定义气泡是否可见
20. visible: true,
21. // 定义气泡叠加层级属性
22. zIndex: 1
23. };
24. let bubble: map.Bubble = await this.mapController.addBubble(bubbleOptions);
```

### setPadding

PhonePC/2in1TabletWearable

setPadding(padding?: mapCommon.Padding): void

设置地图和边界的距离来定义地图的可见区域。地图图层元素将适应填充，例如，缩放控件、指南针等将被移动到适应定义的区域，相机将相对于可见区域的中心移动。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| padding | [mapCommon.Padding](map-common.md#padding) | 否 | 地图和边界的距离，异常值不处理。 |

**示例：**

```
1. // 初始化参数，左边距0，底边距50
2. let padding: mapCommon.Padding = {
3. left: 0,
4. bottom: 50
5. };
6. this.mapController.setPadding(padding);
```

### getProjection

PhonePC/2in1TabletWearable

getProjection(): Projection

获取Projection对象，用于实现屏幕坐标和经纬度坐标之间的相互转换。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Projection](map-map-projection.md) | [Projection](map-map-projection.md)对象。 |

**示例：**

```
1. let projection: map.Projection = this.mapController.getProjection();
```

### setCustomMapStyle

PhonePC/2in1TabletWearable

setCustomMapStyle(customMapStyleOptions: mapCommon.CustomMapStyleOptions): Promise<void>

将地图样式修改为自定义样式。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| customMapStyleOptions | [mapCommon.CustomMapStyleOptions](map-common.md#custommapstyleoptions) | 是 | 自定义样式参数，异常值不处理。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-map.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1002601002 | The custom map style file does not exist. |
| 1002601004 | The style content format is incorrect. |

**示例：**

```
1. // styleId需要替换为您自己的样式ID，样式ID可在Petal Maps Studio平台上创建
2. let param: mapCommon.CustomMapStyleOptions = {
3. styleId: "xxxxxxx"
4. };
5. await this.mapController.setCustomMapStyle(param);
```

### getDayNightMode

PhonePC/2in1TabletWearable

getDayNightMode(): mapCommon.DayNightMode

查询地图的日间夜间模式。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [mapCommon.DayNightMode](map-common.md#daynightmode) | 日间夜间模式。 |

**示例：**

```
1. let mode = this.mapController.getDayNightMode();
```

### setDayNightMode

PhonePC/2in1TabletWearable

setDayNightMode(mode: mapCommon.DayNightMode): void

设置地图的日间夜间模式。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| mode | [mapCommon.DayNightMode](map-common.md#daynightmode) | 是 | 日间夜间模式，异常值不处理。 |

**示例：**

```
1. this.mapController.setDayNightMode(mapCommon.DayNightMode.AUTO);
```

### getMapType

PhonePC/2in1TabletWearable

getMapType(): mapCommon.MapType

查询地图类型。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

**返回值：**

| **类型** | **说明** |
| --- | --- |
| [mapCommon.MapType](map-common.md#maptype) | 查询地图的类型。 |

**示例：**

```
1. let mapType = this.mapController.getMapType();
```

### setMapType

PhonePC/2in1TabletWearable

setMapType(mapType: mapCommon.MapType): void

设置地图类型。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| mapType | [mapCommon.MapType](map-common.md#maptype) | 是 | 地图类型，异常值不处理。 |

**示例：**

```
1. this.mapController.setMapType(mapCommon.MapType.TERRAIN);
```

### setScalePosition

PhonePC/2in1TabletWearable

setScalePosition(point: mapCommon.MapPoint): void

设置比例尺控件的位置。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| point | [mapCommon.MapPoint](map-common.md#mappoint) | 是 | 比例尺位置，异常值不处理。  **说明：**  比例尺在穿戴设备上默认处于左右居中位置，接口传入的positionX值在穿戴设备上不显示效果。 |

**示例：**

```
1. let point: mapCommon.MapPoint = {
2. // 以当前地图组件左上角为原点，向右移动1000
3. positionX: 1000,
4. // 以当前地图组件左上角为原点，向下移动1000
5. positionY: 1000
6. };
7. this.mapController.setScalePosition(point);
```

### getScaleLevel

PhonePC/2in1TabletWearable

getScaleLevel(): number

查询当前层级的比例尺大小。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

**返回值：**

| **类型** | **说明** |
| --- | --- |
| number | 接口返回比例尺上的文本数字，单位：米。 |

**示例：**

```
1. let level = this.mapController.getScaleLevel();
```

### setCompassPosition

PhonePC/2in1TabletWearable

setCompassPosition(point: mapCommon.MapPoint): void

设置指南针位置。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| point | [mapCommon.MapPoint](map-common.md#mappoint) | 是 | 设置指南针位置，即指南针左上角相对地图组件左上角的偏移量，单位：px，异常值不处理。 |

**示例：**

```
1. let point: mapCommon.MapPoint = {
2. positionX: 10,
3. positionY: 10
4. };
5. this.mapController.setCompassPosition(point);
```

### setAllGesturesEnabled

PhonePC/2in1TabletWearable

setAllGesturesEnabled(enabled: boolean): void

提供禁用所有手势的接口。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| enabled | boolean | 是 | 提供禁用所有手势的接口，异常值不处理。  - true：启用手势  - false：禁用手势 |

**示例：**

```
1. this.mapController.setAllGesturesEnabled(true);
```

### getScaleControlsHeight

PhonePC/2in1TabletWearable

getScaleControlsHeight(): number

获取比例尺控件的高度。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 比例尺控件的高度，单位：vp。 |

**示例：**

```
1. let height = this.mapController.getScaleControlsHeight();
```

### getScaleControlsWidth

PhonePC/2in1TabletWearable

getScaleControlsWidth(): number

获取比例尺控件的宽度。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 比例尺控件的宽度，单位：vp。 |

**示例：**

```
1. let width = this.mapController.getScaleControlsWidth();
```

### setAlwaysShowScaleEnabled

PhonePC/2in1TabletWearable

setAlwaysShowScaleEnabled(enabled: boolean): void

设置是否始终显示比例尺。该功能需优先使用[setScaleControlsEnabled](map-map-mapcomponentcontroller.md#setscalecontrolsenabled)方法开启比例尺控件方可使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| enabled | boolean | 是 | 设置是否始终显示比例尺，异常值不处理。  - true：始终显示  - false：关闭始终显示，比例尺显示2秒后关闭 |

**示例：**

```
1. this.mapController.setAlwaysShowScaleEnabled(true);
```

### isAlwaysShowScaleEnabled

PhonePC/2in1TabletWearable

isAlwaysShowScaleEnabled(): boolean

返回是否始终显示比例尺。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | - true: 始终显示  - false: 关闭始终显示 |

**示例：**

```
1. let scaleEnabled: boolean = this.mapController.isAlwaysShowScaleEnabled();
```

### addClusterOverlay

PhonePC/2in1TabletWearable

addClusterOverlay(params: mapCommon.ClusterOverlayParams): Promise<ClusterOverlay>

新增聚合图层。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| params | [mapCommon.ClusterOverlayParams](map-common.md#clusteroverlayparams) | 是 | 聚合图层参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[ClusterOverlay](map-map-clusteroverlay.md)> | Promise对象，返回[ClusterOverlay](map-map-clusteroverlay.md)。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-map.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid input parameter. |
| 1002601001 | The object to be operated does not exist. |

**示例：**

```
1. let clusterItem1: mapCommon.ClusterItem = {
2. position: {
3. latitude: 31.98,
4. longitude: 118.766
5. }
6. };
7. let clusterItem2: mapCommon.ClusterItem = {
8. position: {
9. latitude: 31.68,
10. longitude: 118.366
11. }
12. };
13. let array: Array<mapCommon.ClusterItem> = [
14. clusterItem1,
15. clusterItem2
16. ];
17. let clusterOverlayParams: mapCommon.ClusterOverlayParams = { distance: 40, clusterItems: array };
18. let clusterOverlay: map.ClusterOverlay = await this.mapController.addClusterOverlay(clusterOverlayParams);
```

### addImageOverlay

PhonePC/2in1TabletWearable

addImageOverlay(params: mapCommon.ImageOverlayParams): Promise<ImageOverlay>

新增图片覆盖物。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| params | [mapCommon.ImageOverlayParams](map-common.md#imageoverlayparams) | 是 | 覆盖物参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[ImageOverlay](map-map-imageoverlay.md)> | Promise对象，返回[ImageOverlay](map-map-imageoverlay.md)。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-map.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid input parameter. |
| 1002601001 | The object to be operated does not exist. |

**示例：**

```
1. let imageOverlayParams: mapCommon.ImageOverlayParams = {
2. bounds: {
3. southwest: { latitude: 32, longitude: 118 },
4. northeast: { latitude: 32.4, longitude: 118.4 }
5. },
6. // 图标需存放在resources/rawfile目录下
7. image: 'icon/icon.png',
8. transparency: 0.3,
9. zIndex: 101,
10. anchorU: 0.5,
11. anchorV: 0.5,
12. clickable: true,
13. visible: true,
14. bearing: 0
15. };
16. let imageOverlay = await this.mapController?.addImageOverlay(imageOverlayParams);
```

### snapshot

PhonePC/2in1TabletWearable

snapshot(): Promise<image.PixelMap>

生成地图快照。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[image.PixelMap](arkts-apis-image-pixelmap.md)> | Promise对象，返回[image.PixelMap](arkts-apis-image-pixelmap.md)。 |

**示例：**

```
1. import { image } from '@kit.ImageKit';

3. let image: image.PixelMap = await this.mapController.snapshot();
```

### addBuildingOverlay

PhonePC/2in1TabletWearable

addBuildingOverlay(params: mapCommon.BuildingOverlayParams): Promise<BuildingOverlay>

添加3D建筑。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| params | [mapCommon.BuildingOverlayParams](map-common.md#buildingoverlayparams) | 是 | 3D建筑相关属性。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[BuildingOverlay](map-map-buildingoverlay.md)> | Promise对象，返回[BuildingOverlay](map-map-buildingoverlay.md)。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-map.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid input parameter. |
| 1002601001 | The object to be operated does not exist. |

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
152. let cameraUpdate = map.newCameraPosition({
153. target: {
154. latitude: 31.984794,
155. longitude: 118.765865
156. },
157. zoom: 18,
158. tilt: 70
159. });
160. // 将地图镜头移动到3D建筑区域
161. this.mapController?.moveCamera(cameraUpdate);
162. // 新建3D建筑
163. let buildingOverlay: map.BuildingOverlay = await this.mapController?.addBuildingOverlay(buildingOverlayOptions);
```

### addTraceOverlay

PhonePC/2in1TabletWearable

addTraceOverlay(params: mapCommon.TraceOverlayParams, markers?: Array<Marker>): Promise<TraceOverlay>

绘制动态轨迹，支持传一组标记，标记将和轨迹一起移动。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| params | [mapCommon.TraceOverlayParams](map-common.md#traceoverlayparams) | 是 | 动态轨迹参数。 |
| markers | Array<[Marker](map-map-marker.md)> | 否 | 动态轨迹的图片数组，异常值不处理。  **说明：**  一组标记的位置必须相同。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[TraceOverlay](map-map-traceoverlay.md)> | Promise对象，返回[TraceOverlay](map-map-traceoverlay.md)。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-map.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid input parameter. |
| 1002601001 | The object to be operated does not exist. |

**示例：**

```
1. // marker1的参数
2. let markerOptions1: mapCommon.MarkerOptions = {
3. position: {
4. latitude: 31.99227173519985,
5. longitude: 118.7622219990476
6. },
7. // 图标需存放在resources/base/media目录下
8. icon: $r("app.media.track_setting_sport_map_marker_22"),
9. anchorU: 0.5,
10. anchorV: 1,
11. visible: true
12. };
13. // 新增marker1
14. let markerBoy1 = await this.mapController.addMarker(markerOptions1);
15. let boyImages1: map.PlayImageAnimation = new map.PlayImageAnimation();
16. boyImages1.setDuration(1000);
17. let resourceArray: Array<Resource> = new Array();
18. resourceArray.push($r("app.media.side_0"));
19. resourceArray.push($r("app.media.side_1"));
20. resourceArray.push($r("app.media.side_2"));
21. resourceArray.push($r("app.media.side_3"));
22. resourceArray.push($r("app.media.side_4"));
23. resourceArray.push($r("app.media.side_5"));
24. resourceArray.push($r("app.media.side_6"));
25. resourceArray.push($r("app.media.side_7"));
26. resourceArray.push($r("app.media.side_8"));
27. resourceArray.push($r("app.media.side_9"));
28. resourceArray.push($r("app.media.side_10"));
29. resourceArray.push($r("app.media.side_11"));
30. resourceArray.push($r("app.media.side_12"));
31. resourceArray.push($r("app.media.side_13"));
32. resourceArray.push($r("app.media.side_14"));
33. resourceArray.push($r("app.media.side_15"));
34. resourceArray.push($r("app.media.side_16"));
35. resourceArray.push($r("app.media.side_17"));
36. resourceArray.push($r("app.media.side_18"));
37. resourceArray.push($r("app.media.side_19"));
38. resourceArray.push($r("app.media.side_20"));
39. await boyImages1.addImages(resourceArray);
40. boyImages1.setRepeatCount(-1);

42. // marker1添加动画
43. markerBoy1.setAnimation(boyImages1);
44. markerBoy1.startAnimation();

46. // marker2的参数
47. let markerOptions2: mapCommon.MarkerOptions = {
48. position: {
49. latitude: 31.99227173519985,
50. longitude: 118.7622219990476
51. },
52. // 图标需存放在resources/base/media目录下
53. icon: $r("app.media.track_setting_sport_map_marker_22"),
54. anchorU: 0.5,
55. anchorV: 1,
56. visible: false
57. };
58. // 新增marker2
59. let markerBoy2 = await this.mapController.addMarker(markerOptions2);
60. let boyImages2: map.PlayImageAnimation = new map.PlayImageAnimation();
61. boyImages2.setDuration(1000);
62. let resourceArray2: Array<Resource> = new Array();
63. resourceArray2.push($r("app.media.behavior_front_cycling_boy_000"));
64. resourceArray2.push($r("app.media.behavior_front_cycling_boy_001"));
65. resourceArray2.push($r("app.media.behavior_front_cycling_boy_002"));
66. resourceArray2.push($r("app.media.behavior_front_cycling_boy_003"));
67. resourceArray2.push($r("app.media.behavior_front_cycling_boy_004"));
68. resourceArray2.push($r("app.media.behavior_front_cycling_boy_005"));
69. resourceArray2.push($r("app.media.behavior_front_cycling_boy_006"));
70. resourceArray2.push($r("app.media.behavior_front_cycling_boy_007"));
71. resourceArray2.push($r("app.media.behavior_front_cycling_boy_008"));
72. resourceArray2.push($r("app.media.behavior_front_cycling_boy_009"));
73. resourceArray2.push($r("app.media.behavior_front_cycling_boy_010"));
74. resourceArray2.push($r("app.media.behavior_front_cycling_boy_011"));
75. resourceArray2.push($r("app.media.behavior_front_cycling_boy_012"));
76. resourceArray2.push($r("app.media.behavior_front_cycling_boy_013"));
77. resourceArray2.push($r("app.media.behavior_front_cycling_boy_014"));
78. resourceArray2.push($r("app.media.behavior_front_cycling_boy_015"));
79. resourceArray2.push($r("app.media.behavior_front_cycling_boy_016"));
80. resourceArray2.push($r("app.media.behavior_front_cycling_boy_017"));
81. resourceArray2.push($r("app.media.behavior_front_cycling_boy_018"));
82. await boyImages2.addImages(resourceArray2);
83. boyImages2.setRepeatCount(-1);
84. // marker2添加动画
85. markerBoy2.setAnimation(boyImages2);
86. markerBoy2.startAnimation();

88. let points: Array<mapCommon.LatLng> = new Array();
89. points.push({ latitude: 31.99685233070878, longitude: 118.75846023442728 });
90. points.push({ latitude: 31.99671325810786, longitude: 118.75846738985165 });
91. points.push({ latitude: 31.99659191076709, longitude: 118.7585347621686 });
92. points.push({ latitude: 31.99648202537233, longitude: 118.7586266510386 });
93. points.push({ latitude: 31.99637707201552, longitude: 118.75872004590596 });
94. points.push({ latitude: 31.996278207010903, longitude: 118.75880449946251 });
95. points.push({ latitude: 31.996187481969695, longitude: 118.7588781960278 });
96. points.push({ latitude: 31.996092248919354, longitude: 118.75895330554488 });
97. points.push({ latitude: 31.995962740450565, longitude: 118.75904721407304 });
98. points.push({ latitude: 31.995792921394, longitude: 118.75916904998051 });
99. points.push({ latitude: 31.995601885713416, longitude: 118.7593235241019 });
100. points.push({ latitude: 31.995398221178277, longitude: 118.75949998588176 });
101. points.push({ latitude: 31.995185902197715, longitude: 118.7596871082939 });
102. points.push({ latitude: 31.994983473052656, longitude: 118.75987334062296 });
103. points.push({ latitude: 31.99482433699269, longitude: 118.76002095184032 });
104. points.push({ latitude: 31.994709073721708, longitude: 118.76012902920532 });
105. points.push({ latitude: 31.99460732100702, longitude: 118.76023892576234 });
106. points.push({ latitude: 31.99449284962087, longitude: 118.7603694232856 });
107. points.push({ latitude: 31.99435358179254, longitude: 118.76053622438056 });
108. points.push({ latitude: 31.99420771148339, longitude: 118.76072790126692 });
109. points.push({ latitude: 31.994075194901523, longitude: 118.7609100960977 });
110. points.push({ latitude: 31.993952686158877, longitude: 118.7610741329013 });
111. points.push({ latitude: 31.993840180644217, longitude: 118.7612193418965 });
112. points.push({ latitude: 31.993733787150244, longitude: 118.76135383115654 });
113. points.push({ latitude: 31.993617206525155, longitude: 118.76150529647698 });

115. // 动态轨迹的入参
116. let traceOptions: mapCommon.TraceOverlayParams = {
117. // 轨迹点
118. points: points,
119. // 轨迹的动画时长
120. animationDuration: 5000,
121. // 相机是否跟随动画移动
122. isMapMoving: true,
123. // 轨迹的颜色
124. color: 0xAAFFAA00,
125. // 轨迹的宽度
126. width: 20,
127. // 轨迹的动画回调（回调轨迹点的index）
128. animationCallback: (pointIndex) => {
129. // 换成骑行
130. if (pointIndex === 10) {
131. markerBoy1.setVisible(false);
132. markerBoy2.setVisible(true);
133. }
134. }
135. };
136. let markers: Array<map.Marker> = new Array();
137. markers.push(markerBoy1, markerBoy2);
138. // 新增轨迹点动画
139. let traceOverlay: map.TraceOverlay = await this.mapController.addTraceOverlay(traceOptions, markers);
```

### addArc

PhonePC/2in1TabletWearable

addArc(params: mapCommon.MapArcParams): MapArc

在地图上添加一条弧线。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| params | [mapCommon.MapArcParams](map-common.md#maparcparams) | 是 | 弧线的相关属性。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| MapArc | 返回[MapArc](map-map-maparc.md)。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-map.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid input parameter. |
| 1002601001 | The object to be operated does not exist. |

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
23. // 添加弧线
24. this.mapController.addArc(mapArcParams);
```

### show

PhonePC/2in1TabletWearable

show(): void

将地图切换到前台，开发者在绘制地图页面的生命周期onPageShow中调用。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

**示例：**

```
1. // 页面每次显示时触发一次，包括路由过程、应用进入前台等场景，仅@Entry装饰的自定义组件生效
2. onPageShow(): void {
3. // 绘制地图页面的生命周期onPageShow，将地图切换到前台
4. if (this.mapController) {
5. this.mapController.show();
6. }
7. }
```

### hide

PhonePC/2in1TabletWearable

hide(): void

将地图切换到后台，开发者在绘制地图页面的生命周期onPageHide中调用。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

**示例：**

```
1. // 页面每次隐藏时触发一次，包括路由过程、应用进入后台等场景，仅@Entry装饰的自定义组件生效。
2. onPageHide(): void {
3. // 绘制地图页面的生命周期onPageHide，将地图切换到后台
4. if (this.mapController) {
5. this.mapController.hide();
6. }
7. }
```

### getEventManager

PhonePC/2in1TabletWearable

getEventManager(): MapEventManager

返回地图监听事件管理器。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

**返回值：**

| **类型** | **说明** |
| --- | --- |
| [MapEventManager](map-map-mapeventmanager.md) | 地图监听事件管理器。 |

**示例：**

```
1. let mapEventManager: map.MapEventManager = this.mapController.getEventManager();
```

### setDisplayOrder

PhonePC/2in1TabletWearable

setDisplayOrder(types: Array<mapCommon.MapElementType>): void

设置地图元素的显示顺序，按照从低到高排列，即后面的覆盖物会压盖前面的覆盖物。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

**参数**：

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| types | Array<[mapCommon.MapElementType](map-common.md#mapelementtype)> | 是 | 四类地图元素的显示顺序，默认顺序为[1, 2, 3, 4]。  入参的长度必须是4，且必须是[mapCommon.MapElementType](map-common.md#mapelementtype)的4个取值，如果不满足，则返回错误码401。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-map.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid input parameter. |

**示例：**

```
1. let mapElementTypeArr: Array<mapCommon.MapElementType> = [
2. mapCommon.MapElementType.OVERLAY,
3. mapCommon.MapElementType.POI,
4. mapCommon.MapElementType.CUSTOM_POI,
5. mapCommon.MapElementType.MARKER];
6. this.mapController.setDisplayOrder(mapElementTypeArr);
```

### setLogoScale

PhonePC/2in1TabletWearable

setLogoScale(logoScale: number): void

修改Logo缩放比例。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.3(15)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.3(15)

**参数**：

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| logoScale | number | 是 | Logo缩放比例，取值范围：[0.8, 1]。异常值返回401错误码。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-map.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid input parameter. |

**示例：**

```
1. this.mapController.setLogoScale(0.9);
```

### getLogoScale

PhonePC/2in1TabletWearable

getLogoScale(): number

查询Logo缩放比例。缩放比例取值范围是[0.8,1]。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.3(15)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.3(15)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | Logo缩放比例。 |

**示例：**

```
1. let logoScale: number = this.mapController.getLogoScale();
```

### isSphereEnabled

PhonePC/2in1TabletWearable

isSphereEnabled(): boolean

获取3D地球开启状态。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.3(15)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.3(15)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | - true：3D地球为开启状态  - false：3D地球为关闭状态 |

**示例：**

```
1. let result: boolean = this.mapController.isSphereEnabled();
```

### setSphereEnabled

PhonePC/2in1TabletWearable

setSphereEnabled(enabled: boolean): void

以动画形式切换2D或3D地球。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.3(15)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.3(15)

**参数**：

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| enabled | boolean | 是 | 以动画形式切换2D或3D地球，异常值不处理。取值范围：  - true：开启3D地球  - false：开启2D地球 |

**示例：**

```
1. this.mapController.setSphereEnabled(true);
```

### setSphereEnabled

PhonePC/2in1TabletWearable

setSphereEnabled(enabled: boolean, animateDuration: number): void

以动画形式切换2D或3D地球。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 6.0.0(20)

**参数**：

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| enabled | boolean | 是 | 以动画形式切换2D或3D地球，异常值不处理。取值范围：  - true：开启3D地球  - false：开启2D地球 |
| animateDuration | number | 是 | 动画持续时间，单位：ms，取值范围：大于0，异常值不处理。 |

**示例：**

```
1. this.mapController.setSphereEnabled(true, 1000);
```

### setSphereEnabled

PhonePC/2in1TabletWearable

setSphereEnabled(enabled: boolean, animateDuration: number, cityLight: boolean): void

以动画形式切换2D或3D地球。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本6.1.0(23)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 6.1.0(23)

**参数**：

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| enabled | boolean | 是 | 以动画形式切换2D或3D地球，异常值不处理。取值范围：  - true：开启3D地球  - false：开启2D地球 |
| animateDuration | number | 是 | 动画持续时间，单位：ms，取值范围：大于0，异常值不处理。 |
| cityLight | boolean | 是 | 是否启用城市灯光，需要开启3D地球，异常值不处理。  - true：开启城市灯光  - false：关闭城市灯光 |

**示例：**

```
1. this.mapController.setSphereEnabled(true, 1000, true);
```

### addHeatmap

PhonePC/2in1TabletWearable

addHeatmap(params: mapCommon.HeatmapParams): Promise<Heatmap>

添加热力图，使用Promise异步回调。热力图适用于大数据密度可视化场景，如人流分布，热点区域等。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 6.0.0(20)

**参数**：

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| params | [mapCommon.HeatmapParams](map-common.md#heatmapparams) | 是 | 添加热力图的参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[Heatmap](map-map-heatmap.md)> | Promise对象，返回[Heatmap](map-map-heatmap.md)，热力图覆盖物。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-map.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1002601001 | The object to be operated does not exist. |
| 1002600015 | The heatmap ID already exists. |

**示例：**

```
1. let data: mapCommon.WeightedLatLng[] = [];
2. for (let i = 0; i < 500; i++) {
3. data.push({
4. point: {
5. longitude: 118.000000 + Math.random() * 1 - 0.25,
6. latitude: 31.000000 + Math.random() * 1 - 0.25,
7. },
8. intensity: 1
9. });
10. }
11. let heatMapOptions: mapCommon.HeatmapParams = {
12. id: 'heatmap0001',
13. data: data,
14. radius: 20,
15. intensity: {
16. 2: 1,
17. 5: 5,
18. 8: 10
19. },
20. }
21. await this.mapController?.addHeatmap(heatMapOptions)
```

### addMvtOverlay

PhonePC/2in1Tablet

addMvtOverlay(params: mapCommon.MvtOverlayParams): MvtOverlay

添加矢量图层。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core.EnhancedOverlay

**起始版本：** 6.0.0(20)

**参数**：

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| params | [mapCommon.MvtOverlayParams](map-common.md#mvtoverlayparams) | 是 | 矢量图层的参数。  **说明：**  使用在线下载方式添加矢量图层时（即使用[mapCommon.MvtOverlayParams](map-common.md#mvtoverlayparams)中[mapCommon.MvtSource](map-common.md#mvtsource)参数的tileUrl方式），需要申请访问网络的权限：ohos.permission.INTERNET。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [MvtOverlay](map-map-mvtoverlay.md) | 矢量图层管理对象。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-map.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1022100001 | The operation object does not exist. |

```
1. let params: mapCommon.MvtOverlayParams = {
2. source: {
3. // 设置矢量图层的地址,必须是以http或者https开头的URL且包含占位符{x}、{y}和{z}
4. tileUrl: 'http://xxx/tiles/{z}/{x}/{y}.pbf',
5. minZoom: 2,
6. maxZoom: 15
7. },
8. layers: [{
9. id: 'layer-map',
10. type: mapCommon.MvtLayerType.FILL,
11. // 对应矢量图层数据中图层的name字段
12. sourceLayer: 'XX',
13. paint: {
14. fillColor: {
15. operator: mapCommon.Operator.GET,
16. args: 'fill'
17. },
18. fillOpacity: {
19. operator: mapCommon.Operator.GET,
20. args: 'fill-opacity'
21. }
22. }
23. }]
24. };
25. let mvtOverlay = this.mapController?.addMvtOverlay(params);
```

### setFramePerSecond

PhonePC/2in1TabletWearable

setFramePerSecond(fps: number): void

设置每秒期望的帧数。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 6.0.0(20)

**参数**：

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| fps | number | 是 | 每秒期望的帧数，取值范围：[1, 60]。异常值返回401错误码。 |

**示例：**

```
1. this.mapController?.setFramePerSecond(60);
```

### addFlowFieldOverlay

PhonePC/2in1Tablet

addFlowFieldOverlay(params: mapCommon.FlowFieldOverlayParams): Promise<FlowFieldOverlay>

添加流场图层，适用于风场和洋流场景。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core.EnhancedOverlay

**起始版本：** 6.0.0(20)

**参数**：

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| params | [mapCommon.FlowFieldOverlayParams](map-common.md#flowfieldoverlayparams) | 是 | 流场图层的参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[FlowFieldOverlay](map-map-flowfieldoverlay.md)> | Promise对象，返回流场图层的管理对象。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-map.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1022100001 | The operation object does not exist. |

**示例：**

```
1. let params: mapCommon.FlowFieldOverlayParams = {
2. // data为GRIB2规范的json数据，需开发者自行传输，可参考流场数据格式参考
3. data: 'xxx'
4. };
5. let fieldOverlay = await this.mapController.addFlowFieldOverlay(params);
```

### addMassPointOverlay

PhonePC/2in1TabletWearable

addMassPointOverlay(params: mapCommon.MassPointOverlayParams): Promise<MassPointOverlay>

添加海量点图层。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 6.0.0(20)

**参数**：

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| params | [mapCommon.MassPointOverlayParams](map-common.md#masspointoverlayparams) | 是 | 海量点图层的参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[MassPointOverlay](map-map-masspointoverlay.md)> | Promise对象，返回海量点的管理对象。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-map.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1002601001 | The object to be operated does not exist. |

**示例：**

```
1. let items: mapCommon.MassPointItem[] = [];
2. for (let i = 0; i < 1000; i++) {
3. // 将海量点存入items
4. items.push({
5. itemId: 'test' + i,
6. position: {
7. longitude: 118.11111 + Math.random() * 1 - 0.5,
8. latitude: 32.11111 + Math.random() * 1 - 0.5,
9. },
10. snippet: 'test' + i,
11. title: 'test' + i
12. })
13. }
14. let params: mapCommon.MassPointOverlayParams = {
15. id: 'test',
16. items: items,
17. // 图标存放在resources/rawfile，icon参数传入rawfile文件夹下的相对路径
18. icon: 'icon/maps_blue_dot.png',
19. }
20. let massPointOverlay = await this.mapController?.addMassPointOverlay(params);
```

### setLanguage

PhonePC/2in1TabletWearable

setLanguage(language: string): void

设置地图组件语言。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 6.0.0(20)

**参数**：

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| language | string | 是 | 地图语言，异常值不处理。语种取值请参见[地图组件支持语言](../harmonyos-guides/map-language.md#地图组件支持语言)列表。 |

**示例：**

```
1. this.mapController?.setLanguage('ja');
```

### getLanguage

PhonePC/2in1TabletWearable

getLanguage(): string

获取地图组件语言。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 6.0.0(20)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 地图语言。语种取值请参见[地图组件支持语言](../harmonyos-guides/map-language.md#地图组件支持语言)列表。 |

**示例：**

```
1. let language = this.mapController?.getLanguage();
```

### changeMyLocationLayerOrder

PhonePC/2in1TabletWearable

changeMyLocationLayerOrder(isBelow: boolean): void

更改我的位置图层相对于覆盖物的压盖顺序。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本6.0.1(21)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 6.0.1(21)

**参数**：

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| isBelow | boolean | 是 | 我的位置图层是否位于覆盖物之下，异常值不处理。  - true：我的位置图层位于覆盖物之下  - false：我的位置图层位于覆盖物之上  **说明：**  该接口对[Marker](map-map-marker.md)、[MapPolyline](map-map-mappolyline.md)、[MapPolygon](map-map-mappolygon.md)、[MapCircle](map-map-mapcircle.md)、[PointAnnotation](map-map-pointannotation.md)、[Bubble](map-map-bubble.md)、[ImageOverlay](map-map-imageoverlay.md)、[MapArc](map-map-maparc.md)、[TraceOverlay](map-map-traceoverlay.md)、底图[Poi](map-common.md#poi)生效。 |

**示例：**

```
1. this.mapController?.changeMyLocationLayerOrder(true);
```

### addTileOverlay

PhonePC/2in1TabletWearable

addTileOverlay(params: mapCommon.TileOverlayParams | mapCommon.TileOverlayOptions): TileOverlay

新增瓦片图层。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.3(15)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.3(15)

**参数**：

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| params | [mapCommon.TileOverlayParams](map-common.md#tileoverlayparams) | [mapCommon.TileOverlayOptions](map-common.md#tileoverlayoptions) | 是 | 瓦片图层参数。  **说明：**  从6.0.0(20)版本开始，params属性支持[mapCommon.TileOverlayOptions](map-common.md#tileoverlayoptions)类型。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [TileOverlay](map-map-tileoverlay.md) | 瓦片图层。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-map.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1002601001 | The object to be operated does not exist. |

**示例：**

```
1. let params: mapCommon.TileOverlayOptions = {
2. // 设置地图瓦片图层的地址，必须是以http或者https开头的URL且包含占位符{x}、{y}和{z}
3. // 需要替换为开发者自己的在线地址
4. tileUrl: "https://xxx/xxx?x={x}&y={y}&z={z}",
5. // 透明度
6. transparency: 0.5,
7. // 开启瓦片图层淡入
8. fadeIn: true,
9. // 开启磁盘缓存
10. diskCacheEnabled: true,
11. // 磁盘缓存大小 默认大小 20480KB, 单位KB
12. diskCacheSize: 20480,
13. // 存放磁盘缓存的沙箱路径
14. diskCachePath: this.getUIContext().getHostContext()?.databaseDir
15. };
16. let tileOverlay: map.TileOverlay = this.mapController?.addTileOverlay(params);
```

### on('cameraChange')

PhonePC/2in1TabletWearable

on(type: 'cameraChange', callback: Callback<mapCommon.LatLng>): void

监听地图相机状态变化事件。使用callback异步回调。此回调不会在动画过程中触发，而是在动画结束时触发。

建议使用[MapEventManager.on(type: 'cameraChange')](map-map-mapeventmanager.md#oncamerachange)。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数**：

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| type | string | 是 | 'cameraChange'：监听地图相机状态变化事件。 |
| callback | Callback<[mapCommon.LatLng](map-common.md#latlng)> | 是 | 回调函数，返回[mapCommon.LatLng](map-common.md#latlng)，监听地图相机状态变化事件。该回调不会在动画过程中触发，而是在动画结束时触发。 |

**示例：**

```
1. this.mapController.on("cameraChange", (position) => {
2. console.info("cameraChange", `on-cameraChange position = ${position.longitude}`);
3. });
```

### off('cameraChange')

PhonePC/2in1TabletWearable

off(type: 'cameraChange', callback: Callback<void>): void

取消监听地图相机状态变化事件。使用callback异步回调。

建议使用[MapEventManager.off(type: 'cameraChange')](map-map-mapeventmanager.md#offcamerachange)。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数**：

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| type | string | 是 | 'cameraChange'：监听地图相机状态变化事件。 |
| callback | Callback<void> | 是 | 回调函数，无返回结果的回调函数。 |

**示例：**

```
1. this.mapController.off("cameraChange", (position) => {
2. console.info("cameraChange", `off-cameraChange`);
3. });
```

### on('cameraIdle')

PhonePC/2in1TabletWearable

on(type: 'cameraIdle', callback: Callback<void>): void

监听相机移动结束事件。使用callback异步回调。

建议使用[MapEventManager.on(type: 'cameraIdle')](map-map-mapeventmanager.md#oncameraidle)。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| type | string | 是 | 'cameraIdle'：监听相机移动结束事件。 |
| callback | Callback<void> | 是 | 回调函数，无返回结果的回调函数。 |

**示例：**

```
1. this.mapController.on("cameraIdle", () => {
2. console.info("cameraIdle", `on-cameraIdle`);
3. });
```

### off('cameraIdle')

PhonePC/2in1TabletWearable

off(type: 'cameraIdle', callback: Callback<void>): void

取消监听相机移动结束事件。使用callback异步回调。

建议使用[MapEventManager.off(type: 'cameraIdle')](map-map-mapeventmanager.md#offcameraidle)。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| type | string | 是 | 'cameraIdle'：监听相机移动结束事件。 |
| callback | Callback<void> | 是 | 回调函数，无返回结果的回调函数。 |

**示例：**

```
1. this.mapController.off("cameraIdle", () => {
2. console.info("cameraIdle", `off-cameraIdle`);
3. });
```

### on('cameraMoveCancel')

PhonePC/2in1TabletWearable

on(type: 'cameraMoveCancel', callback: Callback<void>): void

监听相机移动取消事件。使用callback异步回调。

建议使用[MapEventManager.on(type: 'cameraMoveCancel')](map-map-mapeventmanager.md#oncameramovecancel)。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| type | string | 是 | 'cameraMoveCancel'：监听地图相机移动取消事件。 |
| callback | Callback<void> | 是 | 回调函数，无返回结果的回调函数。 |

**示例：**

```
1. this.mapController.on("cameraMoveCancel", () => {
2. console.info("cameraMoveCancel", `on-cameraMoveCancel`);
3. });
```

### off('cameraMoveCancel')

PhonePC/2in1TabletWearable

off(type: 'cameraMoveCancel', callback: Callback<void>): void

取消监听相机移动取消事件。使用callback异步回调。

建议使用[MapEventManager.off(type: 'cameraMoveCancel')](map-map-mapeventmanager.md#offcameramovecancel)。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| type | string | 是 | 'cameraMoveCancel'：监听地图相机移动取消事件。 |
| callback | Callback<void> | 是 | 回调函数，无返回结果的回调函数。 |

**示例：**

```
1. this.mapController.off("cameraMoveCancel", () => {
2. console.info("cameraMoveCancel", `off-cameraMoveCancel`);
3. });
```

### on('cameraMove')

PhonePC/2in1TabletWearable

on(type: 'cameraMove', callback: Callback<void>): void

监听相机移动事件。使用callback异步回调。

建议使用[MapEventManager.on(type: 'cameraMove')](map-map-mapeventmanager.md#oncameramove)。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| type | string | 是 | 'cameraMove'：监听相机移动事件。 |
| callback | Callback<void> | 是 | 回调函数，无返回结果的回调函数。 |

**示例：**

```
1. this.mapController.on("cameraMove", () => {
2. console.info("cameraMove", `on-cameraMove`);
3. });
```

### off('cameraMove')

PhonePC/2in1TabletWearable

off(type: 'cameraMove', callback: Callback<void>): void

取消监听相机移动事件。使用callback异步回调。

建议使用[MapEventManager.off(type: 'cameraMove')](map-map-mapeventmanager.md#offcameramove)。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| type | string | 是 | 'cameraMove'：监听相机移动事件。 |
| callback | Callback<void> | 是 | 回调函数，无返回结果的回调函数。 |

**示例：**

```
1. this.mapController.off("cameraMove", () => {
2. console.info("cameraMove", `off-cameraMove`);
3. });
```

### on('cameraMoveStart')

PhonePC/2in1TabletWearable

on(type: 'cameraMoveStart', callback: Callback<number>): void

监听相机移动开始事件。使用callback异步回调。

建议使用[MapEventManager.on(type: 'cameraMoveStart')](map-map-mapeventmanager.md#oncameramovestart)。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| type | string | 是 | 'cameraMoveStart'：监听相机移动开始事件。 |
| callback | Callback<number> | 是 | 回调函数，返回number。  number表示相机改变的原因：  1：地图上的用户手势  2：用户交互产生的默认动画  3：开发人员启动的动画 |

**示例：**

```
1. this.mapController.on("cameraMoveStart", (reason) => {
2. console.info("cameraMoveStart", `on-cameraMoveStart reason = ${reason}`);
3. });
```

### off('cameraMoveStart')

PhonePC/2in1TabletWearable

off(type: 'cameraMoveStart', callback: Callback<void>): void

取消监听相机移动开始事件。使用callback异步回调。

建议使用[MapEventManager.off(type: 'cameraMoveStart')](map-map-mapeventmanager.md#offcameramovestart)。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| type | string | 是 | 'cameraMoveStart'：监听相机移动开始事件。 |
| callback | Callback<void> | 是 | 回调函数，无返回结果的回调函数。 |

**示例：**

```
1. this.mapController.off("cameraMoveStart", () => {
2. console.info("cameraMoveStart", `off-cameraMoveStart`);
3. });
```

### on('mapClick')

PhonePC/2in1TabletWearable

on(type: 'mapClick', callback: Callback<mapCommon.LatLng>): void

监听地图点击事件。使用callback异步回调。

建议使用[MapEventManager.on(type: 'mapClick')](map-map-mapeventmanager.md#onmapclick)。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| type | string | 是 | 'mapClick'：监听地图点击事件。 |
| callback | Callback<[mapCommon.LatLng](map-common.md#latlng)> | 是 | 回调函数，返回[mapCommon.LatLng](map-common.md#latlng)。 |

**示例：**

```
1. this.mapController.on("mapClick", (position) => {
2. console.info("mapClick", `on-mapClick position = ${position.longitude}`);
3. });
```

### off('mapClick')

PhonePC/2in1TabletWearable

off(type: 'mapClick', callback: Callback<void>): void

取消监听地图点击事件。使用callback异步回调。

建议使用[MapEventManager.off(type: 'mapClick')](map-map-mapeventmanager.md#offmapclick)。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| type | string | 是 | 'mapClick'：监听地图点击事件。 |
| callback | Callback<void> | 是 | 回调函数，无返回结果的回调函数。 |

**示例：**

```
1. this.mapController.off("mapClick", () => {
2. console.info("mapClick", `off-mapClick`);
3. });
```

### on('mapLoad')

PhonePC/2in1TabletWearable

on(type: 'mapLoad', callback: Callback<void>): void

监听地图加载事件。使用callback异步回调。

建议使用[MapEventManager.on(type: 'mapLoad')](map-map-mapeventmanager.md#onmapload)。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| type | string | 是 | 'mapLoad'：监听地图加载事件。 |
| callback | Callback<void> | 是 | 回调函数，无返回结果的回调函数。 |

**示例：**

```
1. this.mapController.on("mapLoad", () => {
2. console.info("mapLoad", `on-mapLoad`);
3. });
```

### off('mapLoad')

PhonePC/2in1TabletWearable

off(type: 'mapLoad', callback: Callback<void>): void

取消监听地图加载事件。使用callback异步回调。

建议使用[MapEventManager.off(type: 'mapLoad')](map-map-mapeventmanager.md#offmapload)。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| type | string | 是 | 'mapLoad'：监听地图加载事件。 |
| callback | Callback<void> | 是 | 回调函数，无返回结果的回调函数。 |

**示例：**

```
1. this.mapController.off("mapLoad", () => {
2. console.info("mapLoad", `off-mapLoad`);
3. });
```

### on('mapLongClick')

PhonePC/2in1TabletWearable

on(type: 'mapLongClick', callback: Callback<mapCommon.LatLng>): void

监听地图长按事件。使用callback异步回调。

建议使用[MapEventManager.on(type: 'mapLongClick')](map-map-mapeventmanager.md#onmaplongclick)。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| type | string | 是 | 'mapLongClick'：监听地图长按事件。 |
| callback | Callback<[mapCommon.LatLng](map-common.md#latlng)> | 是 | 回调函数，返回[mapCommon.LatLng](map-common.md#latlng)。 |

**示例：**

```
1. this.mapController.on("mapLongClick", () => {
2. console.info("mapLongClick", `on-mapLongClick`);
3. });
```

### off('mapLongClick')

PhonePC/2in1TabletWearable

off(type: 'mapLongClick', callback: Callback<void>): void

取消监听地图长按事件。使用callback异步回调。

建议使用[MapEventManager.off(type: 'mapLongClick')](map-map-mapeventmanager.md#offmaplongclick)。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| type | string | 是 | 'mapLongClick'：监听地图长按事件。 |
| callback | Callback<void> | 是 | 回调函数，无返回结果的回调函数。 |

**示例：**

```
1. this.mapController.off("mapLongClick", () => {
2. console.info("mapLongClick", `off-mapLongClick`);
3. });
```

### on('myLocationButtonClick')

PhonePC/2in1TabletWearable

on(type: 'myLocationButtonClick', callback: Callback<void>): void

监听我的位置按钮点击事件。使用callback异步回调。

建议使用[MapEventManager.on(type: 'myLocationButtonClick')](map-map-mapeventmanager.md#onmylocationbuttonclick)。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| type | string | 是 | 'myLocationButtonClick'：监听我的位置按钮点击事件。 |
| callback | Callback<void> | 是 | 回调函数，无返回结果的回调函数。 |

**示例：**

```
1. this.mapController.on("myLocationButtonClick", () => {
2. console.info("myLocationButtonClick", `on-myLocationButtonClick`);
3. });
```

### off('myLocationButtonClick')

PhonePC/2in1TabletWearable

off(type: 'myLocationButtonClick', callback: Callback<void>): void

取消监听我的位置按钮点击事件。使用callback异步回调。

建议使用[MapEventManager.off(type: 'myLocationButtonClick')](map-map-mapeventmanager.md#offmylocationbuttonclick)。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| type | string | 是 | 'myLocationButtonClick'：监听我的位置按钮点击事件。 |
| callback | Callback<void> | 是 | 回调函数，无返回结果的回调函数。 |

**示例：**

```
1. this.mapController.off("myLocationButtonClick", () => {
2. console.info("myLocationButtonClick", `off-myLocationButtonClick`);
3. });
```

### on('myLocationClick')

PhonePC/2in1TabletWearable

on(type: 'myLocationClick', callback: Callback<mapCommon.LatLng>): void

监听我的位置点击事件。使用callback异步回调。

建议使用[MapEventManager.on(type: 'myLocationClick')](map-map-mapeventmanager.md#onmylocationclick)。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| type | string | 是 | 'myLocationClick'：监听我的位置点击事件。 |
| callback | Callback<[mapCommon.LatLng](map-common.md#latlng)> | 是 | 回调函数，返回[mapCommon.LatLng](map-common.md#latlng)。 |

**示例：**

```
1. this.mapController.on("myLocationClick", (position) => {
2. console.info("myLocationClick", `on-myLocationClick position = ${position.longitude}`);
3. });
```

### off('myLocationClick')

PhonePC/2in1TabletWearable

off(type: 'myLocationClick', callback: Callback<void>): void

取消监听我的位置点击事件。使用callback异步回调。

建议使用[MapEventManager.off(type: 'myLocationClick')](map-map-mapeventmanager.md#offmylocationclick)。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| type | string | 是 | 'myLocationClick'：监听我的位置点击事件。 |
| callback | Callback<void> | 是 | 回调函数，无返回结果的回调函数。 |

**示例：**

```
1. this.mapController.off("myLocationClick", () => {
2. console.info("myLocationClick", `off-myLocationClick`);
3. });
```

### on('poiClick')

PhonePC/2in1TabletWearable

on(type: 'poiClick', callback: Callback<mapCommon.Poi>): void

监听POI点击事件。使用callback异步回调。

建议使用[MapEventManager.on(type: 'poiClick')](map-map-mapeventmanager.md#onpoiclick)。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| type | string | 是 | 'poiClick'：监听POI点击事件。 |
| callback | Callback<[mapCommon.Poi](map-common.md#poi)> | 是 | 回调函数，返回[mapCommon.Poi](map-common.md#poi)。 |

**示例：**

```
1. this.mapController.on("poiClick", (poi) => {
2. console.info("poiClick", `on-poiClick poi = ${poi.id}`);
3. });
```

### off('poiClick')

PhonePC/2in1TabletWearable

off(type: 'poiClick', callback: Callback<void>): void

取消监听POI点击事件。使用callback异步回调。

建议使用[MapEventManager.off(type: 'poiClick')](map-map-mapeventmanager.md#offpoiclick)。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| type | string | 是 | 'poiClick'：监听POI点击事件。 |
| callback | Callback<void> | 是 | 回调函数，无返回结果的回调函数。 |

**示例：**

```
1. this.mapController.off("poiClick", () => {
2. console.info("poiClick", `off-poiClick`);
3. });
```

### on('markerClick')

PhonePC/2in1TabletWearable

on(type: 'markerClick', callback: Callback<Marker>): void

监听标记点击事件。使用callback异步回调。

建议使用[MapEventManager.on(type: 'markerClick')](map-map-mapeventmanager.md#onmarkerclick)。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| type | string | 是 | 'markerClick'：监听标记点击事件。 |
| callback | Callback<[Marker](map-map-marker.md)> | 是 | 回调函数，返回[Marker](map-map-marker.md)。 |

**示例：**

```
1. this.mapController.on("markerClick", (marker) => {
2. console.info("markerClick", `on-markerClick position = ${marker.getId()}`);
3. });
```

### off('markerClick')

PhonePC/2in1TabletWearable

off(type: 'markerClick', callback: Callback<void>): void

取消监听标记点击事件。使用callback异步回调。

建议使用[MapEventManager.off(type: 'markerClick')](map-map-mapeventmanager.md#offmarkerclick)。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| type | string | 是 | 'markerClick'：监听标记点击事件。 |
| callback | Callback<void> | 是 | 回调函数，无返回结果的回调函数。 |

**示例：**

```
1. this.mapController.off("markerClick", () => {
2. console.info("markerClick", `off-markerClick`);
3. });
```

### on('markerDragStart')

PhonePC/2in1TabletWearable

on(type: 'markerDragStart', callback: Callback<Marker>): void

监听标记开始拖拽事件。使用callback异步回调。

建议使用[MapEventManager.on(type: 'markerDragStart')](map-map-mapeventmanager.md#onmarkerdragstart)。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| type | string | 是 | 'markerDragStart'：监听标记开始拖拽事件。 |
| callback | Callback<[Marker](map-map-marker.md)> | 是 | 回调函数，返回[Marker](map-map-marker.md)。 |

**示例：**

```
1. this.mapController.on("markerDragStart", (marker) => {
2. console.info("markerDragStart", `on-markerDragStart position = ${marker.getId()}`);
3. });
```

### off('markerDragStart')

PhonePC/2in1TabletWearable

off(type: 'markerDragStart', callback: Callback<void>): void

取消监听标记开始拖拽事件。使用callback异步回调。

建议使用[MapEventManager.off(type: 'markerDragStart')](map-map-mapeventmanager.md#offmarkerdragstart)。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| type | string | 是 | 'markerDragStart'：监听标记开始拖拽事件。 |
| callback | Callback<void> | 是 | 回调函数，无返回结果的回调函数。 |

**示例：**

```
1. this.mapController.off("markerDragStart", () => {
2. console.info("markerDragStart", `off-markerDragStart`);
3. });
```

### on('markerDrag')

PhonePC/2in1TabletWearable

on(type: 'markerDrag', callback: Callback<Marker>): void

监听标记拖拽事件。使用callback异步回调。

建议使用[MapEventManager.on(type: 'markerDrag')](map-map-mapeventmanager.md#onmarkerdrag)。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| type | string | 是 | 'markerDrag'：监听标记拖拽事件。 |
| callback | Callback<[Marker](map-map-marker.md)> | 是 | 回调函数，返回[Marker](map-map-marker.md)。 |

**示例：**

```
1. this.mapController.on("markerDrag", (marker) => {
2. console.info("markerDrag", `on-markerDrag position = ${marker.getId()}`);
3. });
```

### off('markerDrag')

PhonePC/2in1TabletWearable

off(type: 'markerDrag', callback: Callback<void>): void

取消监听标记拖拽事件。使用callback异步回调。

建议使用[MapEventManager.off(type: 'markerDrag')](map-map-mapeventmanager.md#offmarkerdrag)。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| type | string | 是 | 'markerDrag'：监听标记拖拽事件。 |
| callback | Callback<void> | 是 | 回调函数，无返回结果的回调函数。 |

**示例：**

```
1. this.mapController.off("markerDrag", () => {
2. console.info("markerDrag", `off-markerDrag`);
3. });
```

### on('markerDragEnd')

PhonePC/2in1TabletWearable

on(type: 'markerDragEnd', callback: Callback<Marker>): void

监听标记拖拽结束事件。使用callback异步回调。

建议使用[MapEventManager.on(type: 'markerDragEnd')](map-map-mapeventmanager.md#onmarkerdragend)。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| type | string | 是 | 'markerDragEnd'：监听标记拖拽结束事件。 |
| callback | Callback<[Marker](map-map-marker.md)> | 是 | 回调函数，返回[Marker](map-map-marker.md)。 |

**示例：**

```
1. this.mapController.on("markerDragEnd", (marker) => {
2. console.info("markerDragEnd", `on-markerDragEnd position = ${marker.getId()}`);
3. });
```

### off('markerDragEnd')

PhonePC/2in1TabletWearable

off(type: 'markerDragEnd', callback: Callback<void>): void

取消监听标记拖动结束事件。使用callback异步回调。

建议使用[MapEventManager.off(type: 'markerDragEnd')](map-map-mapeventmanager.md#offmarkerdragend)。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| type | string | 是 | 'markerDragEnd'：监听标记拖动结束事件。 |
| callback | Callback<void> | 是 | 回调函数，无返回结果的回调函数。 |

**示例：**

```
1. this.mapController.off("markerDragEnd", () => {
2. console.info("markerDragEnd", `off-markerDragEnd`);
3. });
```

### on('circleClick')

PhonePC/2in1TabletWearable

on(type: 'circleClick', callback: Callback<MapCircle>): void

监听圆点击事件。使用callback异步回调。

建议使用[MapEventManager.on(type: 'circleClick')](map-map-mapeventmanager.md#oncircleclick)。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| type | string | 是 | 'circleClick'：监听圆点击事件。 |
| callback | Callback<[MapCircle](map-map-mapcircle.md)> | 是 | 回调函数，返回[MapCircle](map-map-mapcircle.md)。 |

**示例：**

```
1. this.mapController.on("circleClick", (position) => {
2. console.info("circleClick", `on-circleClick position = ${position.getCenter().longitude}`);
3. });
```

### off('circleClick')

PhonePC/2in1TabletWearable

off(type: 'circleClick', callback: Callback<void>): void

取消监听圆点击事件。使用callback异步回调。

建议使用[MapEventManager.off(type: 'circleClick')](map-map-mapeventmanager.md#offcircleclick)。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| type | string | 是 | 'circleClick'：监听圆点击事件。 |
| callback | Callback<void> | 是 | 回调函数，无返回结果的回调函数。 |

**示例：**

```
1. this.mapController.off("circleClick", () => {
2. console.info("circleClick", `off-circleClick`);
3. });
```

### on('polylineClick')

PhonePC/2in1TabletWearable

on(type: 'polylineClick', callback: Callback<MapPolyline>): void

监听折线点击事件。使用callback异步回调。

建议使用[MapEventManager.on(type: 'polylineClick')](map-map-mapeventmanager.md#onpolylineclick)。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| type | string | 是 | 'polylineClick'：监听折线点击事件。 |
| callback | Callback<[MapPolyline](map-map-mappolyline.md)> | 是 | 回调函数，返回[MapPolyline](map-map-mappolyline.md)。 |

**示例：**

```
1. this.mapController.on("polylineClick", (polyline) => {
2. console.info("polylineClick", `on-polylineClick position = ${polyline.getId()}`);
3. });
```

### off('polylineClick')

PhonePC/2in1TabletWearable

off(type: 'polylineClick', callback: Callback<void>): void

取消监听折线点击事件。使用callback异步回调。

建议使用[MapEventManager.off(type: 'polylineClick')](map-map-mapeventmanager.md#offpolylineclick)。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| type | string | 是 | 'polylineClick'：监听折线点击事件。 |
| callback | Callback<void> | 是 | 回调函数，无返回结果的回调函数。 |

**示例：**

```
1. this.mapController.off("polylineClick", () => {
2. console.info("polylineClick", "off-polylineClick");
3. });
```

### on('polygonClick')

PhonePC/2in1TabletWearable

on(type: 'polygonClick', callback: Callback<MapPolygon>): void

监听多边形点击事件。使用callback异步回调。

建议使用[MapEventManager.on(type: 'polygonClick')](map-map-mapeventmanager.md#onpolygonclick)。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| type | string | 是 | 'polygonClick'：监听多边形点击事件。 |
| callback | Callback<[MapPolygon](map-map-mappolygon.md)> | 是 | 回调函数，返回[MapPolygon](map-map-mappolygon.md)。 |

**示例：**

```
1. this.mapController.on("polygonClick", (polygon) => {
2. console.info("polygonClick", `on-polygonClick position = ${polygon.getId()}`);
3. });
```

### off('polygonClick')

PhonePC/2in1TabletWearable

off(type: 'polygonClick', callback: Callback<void>): void

取消监听多边形点击事件。使用callback异步回调。

建议使用[MapEventManager.off(type: 'polygonClick')](map-map-mapeventmanager.md#offpolygonclick)。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| type | string | 是 | 'polygonClick'：监听多边形点击事件。 |
| callback | Callback<void> | 是 | 回调函数，无返回结果的回调函数。 |

**示例：**

```
1. this.mapController.off("polygonClick", () => {
2. console.info("polygonClick", "off-polygonClick");
3. });
```

### on('infoWindowClick')

PhonePC/2in1TabletWearable

on(type: 'infoWindowClick', callback: Callback<Marker>): void

监听信息窗点击事件。使用callback异步回调。

建议使用[MapEventManager.on(type: 'infoWindowClick')](map-map-mapeventmanager.md#oninfowindowclick)。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| type | string | 是 | 'infoWindowClick'：监听信息窗点击事件。 |
| callback | Callback<[Marker](map-map-marker.md)> | 是 | 回调函数，返回[Marker](map-map-marker.md)。 |

**示例：**

```
1. this.mapController.on("infoWindowClick", (infoWindow) => {
2. console.info("infoWindowClick", `on-infoWindowClick infoWindow = ${infoWindow.getId()}`);
3. });
```

### off('infoWindowClick')

PhonePC/2in1TabletWearable

off(type: 'infoWindowClick', callback: Callback<void>): void

取消监听信息窗点击事件。使用callback异步回调。

建议使用[MapEventManager.off(type: 'infoWindowClick')](map-map-mapeventmanager.md#offinfowindowclick)。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| type | string | 是 | 'infoWindowClick'：监听信息窗点击事件。 |
| callback | Callback<void> | 是 | 回调函数，无返回结果的回调函数。 |

**示例：**

```
1. this.mapController.off("infoWindowClick", () => {
2. console.info("infoWindowClick", `off-infoWindowClick`);
3. });
```

### on('infoWindowClose')

PhonePC/2in1TabletWearable

on(type: 'infoWindowClose', callback: Callback<Marker>): void

监听信息窗关闭事件。使用callback异步回调。

建议使用[MapEventManager.on(type: 'infoWindowClose')](map-map-mapeventmanager.md#oninfowindowclose)。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| type | string | 是 | 'infoWindowClose'：监听信息窗关闭事件。 |
| callback | Callback<[Marker](map-map-marker.md)> | 是 | 回调函数，返回[Marker](map-map-marker.md)。 |

**示例：**

```
1. this.mapController.on("infoWindowClose", (infoWindowClose) => {
2. console.info("infoWindowClose", `on-infoWindowClose infoWindowClose = ${infoWindowClose.getId()}`);
3. });
```

### off('infoWindowClose')

PhonePC/2in1TabletWearable

off(type: 'infoWindowClose', callback: Callback<void>): void

取消监听信息窗关闭事件。使用callback异步回调。

建议使用[MapEventManager.off(type: 'infoWindowClose')](map-map-mapeventmanager.md#offinfowindowclose)。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| type | string | 是 | 'infoWindowClose'：监听信息窗关闭事件。 |
| callback | Callback<void> | 是 | 回调函数，无返回结果的回调函数。 |

**示例：**

```
1. this.mapController.off("infoWindowClose", () => {
2. console.info("infoWindowClose", `off-infoWindowClose`);
3. });
```

### on('pointAnnotationClick')

PhonePC/2in1TabletWearable

on(type: 'pointAnnotationClick', callback: Callback<PointAnnotation>): void

监听点注释点击事件。使用callback异步回调。

建议使用[MapEventManager.on(type: 'pointAnnotationClick')](map-map-mapeventmanager.md#onpointannotationclick)。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| type | string | 是 | 'pointAnnotationClick'：监听点注释点击事件。 |
| callback | Callback<[PointAnnotation](map-map-pointannotation.md)> | 是 | 回调函数，返回[PointAnnotation](map-map-pointannotation.md)。 |

**示例：**

```
1. this.mapController.on("pointAnnotationClick", (pointAnnotation) => {
2. console.info("pointAnnotationClick", `on-PointAnnotationClick pointAnnotation = ${pointAnnotation.getId()}`);
3. });
```

### off('pointAnnotationClick')

PhonePC/2in1TabletWearable

off(type: 'pointAnnotationClick', callback: Callback<void>): void

取消监听点注释点击事件。使用callback异步回调。

建议使用[MapEventManager.off(type: 'pointAnnotationClick')](map-map-mapeventmanager.md#offpointannotationclick)。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| type | string | 是 | 'pointAnnotationClick'：监听点注释点击事件。 |
| callback | Callback<void> | 是 | 回调函数，无返回结果的回调函数。 |

**示例：**

```
1. this.mapController.off("pointAnnotationClick", () => {
2. console.info("pointAnnotationClick", `off-PointAnnotationClick`);
3. });
```

### on('bubbleClick')

PhonePC/2in1TabletWearable

on(type: 'bubbleClick', callback: Callback<Bubble>): void

监听气泡点击事件。使用callback异步回调。

建议使用[MapEventManager.on(type: 'bubbleClick')](map-map-mapeventmanager.md#onbubbleclick)。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| type | string | 是 | 'bubbleClick'：监听气泡点击事件。 |
| callback | Callback<[Bubble](map-map-bubble.md)> | 是 | 回调函数，返回[Bubble](map-map-bubble.md)。 |

**示例：**

```
1. this.mapController.on("bubbleClick", (bubble) => {
2. console.info("bubbleClick", `on-BubbleClick bubble = ${bubble.getId()}`);
3. });
```

### off('bubbleClick')

PhonePC/2in1TabletWearable

off(type: 'bubbleClick', callback: Callback<void>): void

取消监听气泡点击事件。使用callback异步回调。

建议使用[MapEventManager.off(type: 'bubbleClick')](map-map-mapeventmanager.md#offbubbleclick)。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| type | string | 是 | 'bubbleClick'：监听气泡点击事件。 |
| callback | Callback<void> | 是 | 回调函数，无返回结果的回调函数。 |

**示例：**

```
1. this.mapController.off("bubbleClick", () => {
2. console.info("bubbleClick", `off-BubbleClick`);
3. });
```

### on('imageOverlayClick')

PhonePC/2in1TabletWearable

on(type: 'imageOverlayClick', callback: Callback<ImageOverlay>): void

监听覆盖物点击事件。使用callback异步回调。

建议使用[MapEventManager.on(type: 'imageOverlayClick')](map-map-mapeventmanager.md#onimageoverlayclick)。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| type | string | 是 | 'imageOverlayClick'：监听覆盖物点击事件。 |
| callback | Callback<[ImageOverlay](map-map-imageoverlay.md)> | 是 | 回调函数，返回[ImageOverlay](map-map-imageoverlay.md)。 |

**示例：**

```
1. // 监听覆盖物点击事件的回调
2. let imageOverlayCallback: Callback<map.ImageOverlay> = (imageOverlay:map.ImageOverlay) => {
3. console.info("imageOverlay:" + imageOverlay?.getId());
4. };
5. this.mapController.on("imageOverlayClick", imageOverlayCallback)
```

### off('imageOverlayClick')

PhonePC/2in1TabletWearable

off(type: 'imageOverlayClick', callback?: Callback<ImageOverlay>): void

取消监听覆盖物点击事件。使用callback异步回调。

建议使用[MapEventManager.off(type: 'imageOverlayClick')](map-map-mapeventmanager.md#offimageoverlayclick)。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| type | string | 是 | 'imageOverlayClick'：监听覆盖物点击事件。 |
| callback | Callback<[ImageOverlay](map-map-imageoverlay.md)> | 否 | 回调函数，返回[ImageOverlay](map-map-imageoverlay.md)，当不填时清除所有监听回调。 |

**示例：**

```
1. let imageOverlayCallback: Callback<map.ImageOverlay> = (imageOverlay:map.ImageOverlay) => {
2. console.info("imageOverlay:" + imageOverlay?.getId());
3. };
4. this.mapController.off("imageOverlayClick", imageOverlayCallback);
```

### on('error')

PhonePC/2in1TabletWearable

on(type: 'error', callback: ErrorCallback): void

监听发生的异常。

建议使用[MapEventManager.on(type: 'error')](map-map-mapeventmanager.md#onerror)。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| type | string | 是 | 'error'：监听发生的异常。 |
| callback | [ErrorCallback](js-apis-base.md#errorcallback) | 是 | 回调函数，监听异常事件的回调。 |

**示例：**

```
1. this.mapController.on("error", (error) => {
2. console.error("error", `on-error: Code: ${error.code}, message: ${error.message}`);
3. });
```

### off('error')

PhonePC/2in1TabletWearable

off(type: 'error', callback: Callback<void>): void

取消监听发生的异常。使用callback异步回调。

建议使用[MapEventManager.off(type: 'error')](map-map-mapeventmanager.md#offerror)。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| type | string | 是 | 'error'：监听发生的异常。 |
| callback | Callback<void> | 是 | 回调函数，无返回结果的回调函数。 |

**示例：**

```
1. this.mapController.off("error", () => {
2. console.error("error", `off-error`);
3. });
```

### setIndoorMapEnabled

PhonePC/2in1TabletWearable

setIndoorMapEnabled(enabled: boolean): void

打开或关闭室内图。仅17级及以上地图层级可见室内图和楼层调节控件。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.1.1(19)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**设备行为差异：** 在API19及之后版本该接口在phone、tablet、2in1均可正常使用，在其他设备中返回801错误。

**起始版本：** 5.1.1(19)

**参数**：

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| enabled | boolean | 是 | 是否启用室内图，异常值不处理。取值范围：  - true：启用室内图  - false：关闭室内图 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-map.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |

**示例：**

```
1. // 打开室内图
2. this.mapController.setIndoorMapEnabled(true);
```

### isIndoorMapEnabled

PhonePC/2in1TabletWearable

isIndoorMapEnabled(): boolean

获取室内图开启状态。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.1.1(19)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**设备行为差异：** 在API19及之后版本该接口在phone、tablet、2in1均可正常使用，在其他设备中返回801错误。

**起始版本：** 5.1.1(19)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | - true：室内图为开启状态  - false：室内图为关闭状态 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-map.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |

**示例：**

```
1. let isIndoorMapEnabled = this.mapController.isIndoorMapEnabled();
```

### switchIndoorMapFloor

PhonePC/2in1TabletWearable

switchIndoorMapFloor(buildingId: string, floorName: string): void

切换到指定的室内建筑楼层。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.1.1(19)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**设备行为差异：** 在API19及之后版本该接口在phone、tablet、2in1均可正常使用，在其他设备中返回801错误。

**起始版本：** 5.1.1(19)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| buildingId | string | 是 | 建筑物的ID。从[on('indoorMapEnter')](map-map-mapeventmanager.md#onindoormapenter)方法的回调函数中获得，异常值不处理。 |
| floorName | string | 是 | 建筑物楼层名称（如：3F）。异常值不处理。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-map.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |

**示例：**

```
1. this.mapController?.switchIndoorMapFloor('822588304363886720', '3F');
```

### setFloorControlsPosition

PhonePC/2in1TabletWearable

setFloorControlsPosition(point: mapCommon.MapPoint): void

设置楼层调节控件的位置。需要先调用[setIndoorMapEnabled](map-map-mapcomponentcontroller.md#setindoormapenabled)方法来开启室内图功能，仅17级及以上地图层级可见室内图和楼层调节控件。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**设备行为差异：** 在API20及之后版本该接口在phone、tablet、2in1均可正常使用，在其他设备中返回801错误。

**起始版本：** 6.0.0(20)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| point | [mapCommon.MapPoint](map-common.md#mappoint) | 是 | 设置楼层调节控件的位置，单位：px，异常值不处理。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-map.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |

**示例：**

```
1. this.mapController?.setFloorControlsPosition({
2. positionX: 500,
3. positionY: 500
4. });
```

### isApproveNumberEnabled

PhonePC/2in1TabletWearable

isApproveNumberEnabled(): boolean

获取审图号显示状态。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本6.1.0(23)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 6.1.0(23)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | - true：显示审图号  - false：隐藏审图号 |

**示例：**

```
1. let isApproveNumberEnabled = this.mapController?.isApproveNumberEnabled();
```

### setApproveNumberEnabled

PhonePC/2in1TabletWearable

setApproveNumberEnabled(enabled: boolean): void

设置是否显示审图号。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本6.1.0(23)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 6.1.0(23)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| enabled | boolean | 是 | 设置是否显示审图号，只有路由地在中国才会显示，异常值不处理。  - true：显示审图号  - false：隐藏审图号 |

**示例：**

```
1. this.mapController?.setApproveNumberEnabled(true);
```
