---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/map-camera
title: 更改地图位置
breadcrumb: 指南 > 应用服务 > Map Kit（地图服务） > 地图交互 > 更改地图位置
category: harmonyos-guides
scraped_at: 2026-04-28T07:49:48+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:99748c221ce37ad8939bece607c52fb32c18f676d428fdfce5d8a6958c11d9ce
---

## 场景介绍

华为地图的移动是通过模拟相机移动的方式实现的，该相机可称为地图相机，您可以通过改变地图相机位置，来控制地图的可见区域，效果如图所示。

本章节将向您介绍地图相机的各个属性与含义，并移动相机。

**图1** 相机移动前

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/cc2UVyTcR6SwZK-BFuZHGg/zh-cn_image_0000002583479025.jpg?HW-CC-KV=V1&HW-CC-Date=20260427T234947Z&HW-CC-Expire=86400&HW-CC-Sign=72317253F533D0CD1AC61A81250CA072223EB19B0E3D4CB9E64D67DD46A68677 "点击放大")

**图2** 相机移动后

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/vJch2bheQ2-hnljweDPKbQ/zh-cn_image_0000002552799376.jpg?HW-CC-KV=V1&HW-CC-Date=20260427T234947Z&HW-CC-Expire=86400&HW-CC-Sign=819F403345CD4846067E5CE9EB5F077C78B5FD33FAAD46C697B3441F45724051 "点击放大")

## 接口说明

您可以通过[map](../harmonyos-references/map-module-desc.md)命名空间下的[moveCamera](../harmonyos-references/map-map-mapcomponentcontroller.md#movecamera)方法、[animateCamera](../harmonyos-references/map-map-mapcomponentcontroller.md#animatecamera)方法和[animateCameraStatus](../harmonyos-references/map-map-mapcomponentcontroller.md#animatecamerastatus)实现移动地图相机。方法入参[CameraUpdate](../harmonyos-references/map-map-cameraupdate.md)可通过以下方法创建。

| 接口名 | 描述 |
| --- | --- |
| [zoomTo](../harmonyos-references/map-map-zoomto.md)(zoom: number): [CameraUpdate](../harmonyos-references/map-map-cameraupdate.md) | 设置地图缩放级别。 |
| [zoomOut](../harmonyos-references/map-map-zoomout.md)(): [CameraUpdate](../harmonyos-references/map-map-cameraupdate.md) | 缩小地图缩放级别，在当前地图显示的级别基础上减1。 |
| [zoomIn](../harmonyos-references/map-map-zoomin.md)(): [CameraUpdate](../harmonyos-references/map-map-cameraupdate.md) | 放大地图缩放级别，在当前地图显示的级别基础上加1。 |
| [zoomBy](../harmonyos-references/map-map-zoomby.md)(amount: number, focus?: [mapCommon.MapPoint](../harmonyos-references/map-common.md#mappoint)): [CameraUpdate](../harmonyos-references/map-map-cameraupdate.md) | 根据给定增量并以给定的屏幕像素点为中心点缩放地图级别。 |
| [scrollBy](../harmonyos-references/map-map-scrollby.md)(x: number, y: number): [CameraUpdate](../harmonyos-references/map-map-cameraupdate.md) | 按像素移动地图中心点。 |
| [newLatLngBounds](../harmonyos-references/map-map-newlatlngbounds.md#newlatlngbounds-1)(bounds: [mapCommon.LatLngBounds](../harmonyos-references/map-common.md#latlngbounds), padding?: number): [CameraUpdate](../harmonyos-references/map-map-cameraupdate.md) | 设置地图经纬度范围、设置地图区域和边界之间的距离。 |
| [newLatLngBounds](../harmonyos-references/map-map-newlatlngbounds.md#newlatlngbounds-2)(bounds: [mapCommon.LatLngBounds](../harmonyos-references/map-common.md#latlngbounds), width: number, height: number, padding: number): [CameraUpdate](../harmonyos-references/map-map-cameraupdate.md) | 设置地图经纬度范围、设置经纬度矩形范围的高和宽、设置地图区域和边界之间的距离。 |
| [newLatLngBounds](../harmonyos-references/map-map-newlatlngbounds.md#newlatlngbounds-3)(bounds: [mapCommon.LatLngBounds](../harmonyos-references/map-common.md#latlngbounds), padding: [mapCommon.Padding](../harmonyos-references/map-common.md#padding)): [CameraUpdate](../harmonyos-references/map-map-cameraupdate.md) | 支持设置地图经纬度范围和4个方向与边界之间的距离。 |
| [newLatLng](../harmonyos-references/map-map-newlatlng.md)(latLng: [mapCommon.LatLng](../harmonyos-references/map-common.md#latlng), zoom?: number): [CameraUpdate](../harmonyos-references/map-map-cameraupdate.md) | 设置地图的中心点和缩放层级。 |
| [newCameraPosition](../harmonyos-references/map-map-newcameraposition.md)(cameraPosition: [mapCommon.CameraPosition](../harmonyos-references/map-common.md#cameraposition)): [CameraUpdate](../harmonyos-references/map-map-cameraupdate.md) | 更新地图状态。 |

## 开发步骤

### 相机移动

1. 初始化地图并获取[MapComponentController](../harmonyos-references/map-map-mapcomponentcontroller.md)地图操作类对象。[显示地图](map-presenting.md)章节中有详细讲解。
2. 导入模块。

   ```
   1. import { MapComponent, mapCommon, map } from '@kit.MapKit';
   ```
3. 通过调用[MapComponentController](../harmonyos-references/map-map-mapcomponentcontroller.md)的[moveCamera](../harmonyos-references/map-map-mapcomponentcontroller.md#movecamera)方法、[animateCamera](../harmonyos-references/map-map-mapcomponentcontroller.md#animatecamera)方法和[animateCameraStatus](../harmonyos-references/map-map-mapcomponentcontroller.md#animatecamerastatus)方法，可实现移动地图相机。

   您可以选择以动画方式或非动画方式移动相机。

   * 动画方式移动相机时，您可以设置动画持续的时间。
   * 非动画方式移动相机是瞬时完成的。

   ```
   1. // 创建CameraUpdate对象
   2. let cameraPosition: mapCommon.CameraPosition = {
   3. target: {
   4. latitude: 32.0,
   5. longitude: 118.0
   6. },
   7. zoom: 10,
   8. tilt: 0,
   9. bearing: 0
   10. };
   11. let cameraUpdate = map.newCameraPosition(cameraPosition);
   12. // 以非动画方式移动地图相机
   13. this.mapController.moveCamera(cameraUpdate);

   15. // 以动画方式移动地图相机
   16. this.mapController.animateCamera(cameraUpdate, 1000);

   18. // 以动画方式移动地图相机，并返回动画结果
   19. let animateResult = await this.mapController.animateCameraStatus(cameraUpdate, 1000);
   ```

   **图3** 相机移动前

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9/v3/L80EJPbTTGG3tZTr6Ay4Pw/zh-cn_image_0000002583439071.jpg?HW-CC-KV=V1&HW-CC-Date=20260427T234947Z&HW-CC-Expire=86400&HW-CC-Sign=966A75584F215DE229A2D1FD967B57ACF1C0A060147D6FB627A13E83765D4972 "点击放大")

   **图4** 相机移动后

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/nuQ1qTOZRIWq90ZYpTl2Ow/zh-cn_image_0000002552959026.jpg?HW-CC-KV=V1&HW-CC-Date=20260427T234947Z&HW-CC-Expire=86400&HW-CC-Sign=33EBD7F5D44A0001825B0036894463873179535DB76BFE83A23A95D156BD60AB "点击放大")
4. 您还可以通过以下方式创建[CameraUpdate](../harmonyos-references/map-map-cameraupdate.md)对象。

   ```
   1. // 方式1：相机放大级数加1，保持其他属性不变
   2. let cameraUpdate = map.zoomIn();

   4. // 方式2：相机放大级数减1，保持其他属性不变
   5. let cameraUpdate1 = map.zoomOut();

   7. // 方式3：指定相机缩放级数zoom值，其他属性不变
   8. let zoom1 = 8.0;
   9. let cameraUpdate2 = map.zoomTo(zoom1);

   11. // 方式4：
   12. // a、指定相机缩放级别增量amount，您调用此方法可以在原来相机的缩放级别之上，进行适当的缩放
   13. // b、指定缩放级别增量和一个中心点，您调用此API可以移动相机至中心点位置，并进行缩放
   14. // 以屏幕左顶点为（0, 0）点，positionX正值代表可视区域向右移动，负值代表可视区域向左移动
   15. // positionY正值代表可视区域向下移动，负值代表可视区域向上移动
   16. let point: mapCommon.MapPoint = {
   17. positionX: 31,
   18. positionY: 118
   19. };
   20. let amount = 2.0;
   21. let cameraUpdate3 = map.zoomBy(amount, point);

   23. // 方式5：设置相机的经纬度和地图层级
   24. // a、仅指定相机的经纬度，实现中心点的移动
   25. // b、指定相机的经纬度和地图层级，您调用此API可以移动相机至中心点位置，并进行缩放
   26. let latLng: mapCommon.LatLng = {
   27. latitude: 31.5,
   28. longitude: 118.9
   29. };
   30. let zoom2 = 10;
   31. let cameraUpdate4 = map.newLatLng(latLng, zoom2);

   33. // 方式6：设置相机的可见区域
   34. let latLngBounds: mapCommon.LatLngBounds = {
   35. northeast: {
   36. latitude: 32.5,
   37. longitude: 119.9
   38. },
   39. southwest: {
   40. latitude: 31.5,
   41. longitude: 118.9
   42. }
   43. };
   44. // 设置地图显示经纬度范围，设置地图区域和边界之间的距离为5像素
   45. let cameraUpdate5 = map.newLatLngBounds(latLngBounds, 5);
   46. // 方式7：设置相机的可见区域
   47. // 设置地图显示经纬度范围，设置经纬度矩形范围的宽为1000像素，设置经纬度矩形范围的高为1000像素，设置地图区域和边界之间的距离为100像素
   48. let cameraUpdate6 = map.newLatLngBounds(latLngBounds, 1000, 1000, 100);
   49. // 方式8：设置地图显示经纬度范围，设置地图区域和4个方向的边界之间的距离分别为5、6、7、8像素
   50. let paddings: mapCommon.Padding = {
   51. left:5,
   52. top: 6,
   53. right: 7,
   54. bottom: 8
   55. };
   56. let cameraUpdate7 = map.newLatLngBounds(latLngBounds, paddings);

   58. // 方式9：滚动相机，将相机按照指定的像素点移动
   59. let x = 100.0;
   60. let y = 100.0;
   61. let cameraUpdate8 = map.scrollBy(x, y);
   ```

### 设置相机最大/最小偏好缩放级别

```
1. // 设置最小偏好缩放级别，范围为[2, 20]
2. this.mapController.setMinZoom(6);
3. // 设置最大偏好缩放级别，范围为[2, 20]
4. this.mapController.setMaxZoom(14);
```

### 设置地图相机的边界

Map Kit支持设置地图相机的边界。通过[setLatLngBounds](../harmonyos-references/map-map-mapcomponentcontroller.md#setlatlngbounds)接口指定一个[LatLngBounds](../harmonyos-references/map-common.md#latlngbounds)来约束相机目标，使用户移动地图时，相机目标不会移出此边界。当设置参数为空时，地图相机的边界清除。

```
1. let bounds: mapCommon.LatLngBounds = {
2. northeast: {
3. latitude: 31,
4. longitude: 118
5. },
6. southwest: {
7. latitude: 30,
8. longitude: 113
9. }
10. };
11. this.mapController.setLatLngBounds(bounds);
```
