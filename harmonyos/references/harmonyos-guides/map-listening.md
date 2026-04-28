---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/map-listening
title: 事件交互
breadcrumb: 指南 > 应用服务 > Map Kit（地图服务） > 地图交互 > 事件交互
category: harmonyos-guides
scraped_at: 2026-04-28T07:49:47+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:d159e5387abb6b686808178ff9138be31ed42615cb1bcc8fde9d6c3275a6bcc3
---

本章节包含地图的点击和长按、相机移动（华为地图的移动是通过模拟相机移动的方式实现的）、以及“我的位置”按钮点击等事件监听。

## 接口说明

以下是地图监听事件相关接口，以下功能主要由[MapEventManager](../harmonyos-references/map-map-mapeventmanager.md)提供，可通过[getEventManager](../harmonyos-references/map-map-mapcomponentcontroller.md#geteventmanager)方法获得[MapEventManager](../harmonyos-references/map-map-mapeventmanager.md)，更多接口及使用方法请参见[接口文档](../harmonyos-references/map-map-mapeventmanager.md)。

| 接口名 | 描述 |
| --- | --- |
| [on](../harmonyos-references/map-map-mapeventmanager.md#onmapclick)(type: 'mapClick', callback: Callback<[mapCommon.LatLng](../harmonyos-references/map-common.md#latlng)>): void | 设置地图点击事件监听器。 |
| [on](../harmonyos-references/map-map-mapeventmanager.md#onmaplongclick)(type: 'mapLongClick', callback: Callback<[mapCommon.LatLng](../harmonyos-references/map-common.md#latlng)>): void | 设置地图长按事件监听器。 |
| [on](../harmonyos-references/map-map-mapeventmanager.md#oncameramovestart)(type: 'cameraMoveStart', callback: Callback<number>): void | 设置相机开始移动事件监听器。 |
| [on](../harmonyos-references/map-map-mapeventmanager.md#oncameramove)(type: 'cameraMove', callback: Callback<void>): void | 设置相机移动事件监听器。 |
| [on](../harmonyos-references/map-map-mapeventmanager.md#oncameraidle)(type: 'cameraIdle', callback: Callback<void>): void | 设置相机移动结束事件监听器。 |
| [on](../harmonyos-references/map-map-mapeventmanager.md#onmarkerclick)(type: 'markerClick' , callback: Callback<[Marker](../harmonyos-references/map-map-marker.md)>): void | 设置标记点击事件监听器。 |
| [on](../harmonyos-references/map-map-mapeventmanager.md#onmylocationbuttonclick)(type: 'myLocationButtonClick', callback: Callback<void>): void | 设置我的位置按钮点击事件监听器。 |
| [on](../harmonyos-references/map-map-mapeventmanager.md#onpointannotationclick)(type: 'pointAnnotationClick', callback: Callback<[PointAnnotation](../harmonyos-references/map-map-pointannotation.md)>): void | 设置点注释点击事件监听器。 |

## 开发步骤

### 初始化地图组件的事件管理接口

```
1. this.mapEventManager = this.mapController.getEventManager();
```

### 地图点击事件监听

```
1. let callback = (position: mapCommon.LatLng) => {
2. console.info("mapClick", `on-mapClick position = ${position.longitude}`);
3. };
4. this.mapEventManager.on("mapClick", callback);
```

### 地图长按事件监听

```
1. let callback = (position: mapCommon.LatLng) => {
2. console.info("mapLongClick", `on-mapLongClick position = ${position.longitude}`);
3. };
4. this.mapEventManager.on("mapLongClick", callback);
```

### 相机移动监听

相机移动时（华为地图的移动是通过模拟相机移动的方式实现的），通过设置监听器，能够对相机移动状态进行监听。

* 当相机开始移动时，会回调cameraMoveStart。

```
1. let callback = (reason: number) => {
2. console.info("cameraMoveStart", `on-cameraMoveStart reason = ${reason}`);
3. };
4. this.mapEventManager.on("cameraMoveStart", callback);
```

* 当相机移动或用户与触摸屏交互时，会多次调用cameraMove。

```
1. let callback = () => {
2. console.info("cameraMove", `on-cameraMove`);
3. };
4. this.mapEventManager.on("cameraMove", callback);
```

* 当相机停止移动时，会回调cameraIdle。

```
1. let callback = () => {
2. console.info("cameraIdle", `on-cameraIdle`);
3. };
4. this.mapEventManager.on("cameraIdle", callback);
```

### 标记点击事件监听

标记是指在地图的指定位置添加标记以标识位置、商家、建筑等。详情请参见[标记](map-marker.md)。

```
1. let callback = (marker: map.Marker) => {
2. console.info("markerClick", `markerClick: ${marker.getId()}`);
3. };
4. this.mapEventManager.on("markerClick", callback);
```

### 我的位置监听

详情请参见[显示我的位置](map-location.md)。

```
1. let callback = () => {
2. console.info("myLocationButtonClick", `myLocationButtonClick`);
3. };
4. this.mapEventManager.on("myLocationButtonClick", callback);
```

### 点注释事件监听

点注释是指在地图的指定位置添加点注释以标识位置、商家、建筑等，并可以通过信息窗口展示详细信息。详情请参见[点注释](map-annotation.md)。

```
1. let callback = (pointAnnotation: map.PointAnnotation) => {
2. console.info("pointAnnotationClick", `pointAnnotationClick: ${pointAnnotation.getId()}`);
3. };
4. this.mapEventManager.on("pointAnnotationClick", callback);
```
