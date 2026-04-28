---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/map-controls-and-gestures
title: 手势交互
breadcrumb: 指南 > 应用服务 > Map Kit（地图服务） > 地图交互 > 手势交互
category: harmonyos-guides
scraped_at: 2026-04-28T07:49:48+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:a23e6d1ab3193d29bec4cf5f7e1bc9fba1d2a3d42403ea9b93296bec4391421e
---

## 场景介绍

本章节将向您介绍如何使用地图的手势。

Map Kit提供了多种手势供用户与地图之间进行交互，如缩放、滚动、旋转和倾斜。这些手势默认开启，如果想要关闭某些手势，可以通过[MapComponentController](../harmonyos-references/map-map-mapcomponentcontroller.md)类提供的接口来控制手势的开关。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/uhHuD0ENSb-gZmMP3JbH0w/zh-cn_image_0000002552959024.jpg?HW-CC-KV=V1&HW-CC-Date=20260427T234946Z&HW-CC-Expire=86400&HW-CC-Sign=11EA09871238106E75E56C03028C925C3797DFE8C920DEA1B1FA7192FA57817F "点击放大")

## 接口说明

以下是地图手势相关接口，该功能有2种实现方式：

* 地图初始化时，可在初始化参数[MapOptions](../harmonyos-references/map-common.md#mapoptions)中设置是否启用手势功能，详细讲解见[显示地图](map-presenting.md)章节。
* 通过调用[MapComponentController](../harmonyos-references/map-map-mapcomponentcontroller.md)提供的set方法实现相关手势的开启或关闭。

| 接口名 | 描述 |
| --- | --- |
| [setZoomGesturesEnabled](../harmonyos-references/map-map-mapcomponentcontroller.md#setzoomgesturesenabled)(enabled: boolean): void | 设置是否启用缩放手势。  默认值为true。 |
| [setScrollGesturesEnabled](../harmonyos-references/map-map-mapcomponentcontroller.md#setscrollgesturesenabled)(enabled: boolean): void | 设置是否启用滚动手势。  默认值为true。 |
| [setRotateGesturesEnabled](../harmonyos-references/map-map-mapcomponentcontroller.md#setrotategesturesenabled)(enabled: boolean): void | 设置是否启用旋转手势。  默认值为true。 |
| [setTiltGesturesEnabled](../harmonyos-references/map-map-mapcomponentcontroller.md#settiltgesturesenabled)(enabled: boolean): void | 设置是否启用倾斜手势。  默认值为true。 |
| [setAllGesturesEnabled](../harmonyos-references/map-map-mapcomponentcontroller.md#setallgesturesenabled)(enabled: boolean): void | 设置手势是否可用。  默认值为true。 |

## 开发步骤

mapController对象在初始化地图时获取，初始化地图功能在[显示地图](map-presenting.md)章节中有详细讲解。

### 地图手势控制

您可以通过mapController对象来启用或禁止相关的地图手势。

**缩放手势：**

用户可以通过用双指捏合，实现放大缩小地图。

```
1. this.mapController.setZoomGesturesEnabled(true);
```

**滚动平移手势：**

用户可以通过用手指拖动地图来进行移动。

```
1. this.mapController.setScrollGesturesEnabled(true);
```

**旋转手势：**

用户可以通过将两个手指放在地图上旋转来旋转地图。

```
1. this.mapController.setRotateGesturesEnabled(true);
```

**倾斜手势：**

用户可以通过将两个手指放在地图上下滑动来倾斜地图。

```
1. this.mapController.setTiltGesturesEnabled(true);
```

**启用或禁止所有手势：**

通过调用[setAllGesturesEnabled](../harmonyos-references/map-map-mapcomponentcontroller.md#setallgesturesenabled)方法，可启用或禁止所有手势。

```
1. // 禁止所有手势
2. this.mapController.setAllGesturesEnabled(false);
```
