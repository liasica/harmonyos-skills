---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/map-controls-and-interaction
title: 控件交互
breadcrumb: 指南 > 应用服务 > Map Kit（地图服务） > 地图交互 > 控件交互
category: harmonyos-guides
scraped_at: 2026-11-14T08:48:24+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:5898f30abfc7436011d29994c9b5f853ec859460ca74af846ed5b26dc24b9d2f
---

## 场景介绍

从6.1.0(23)开始，支持在地图左下角设置审图号。

本章节将向您介绍如何使用地图的控件。

控件是指浮在地图组件上的一系列用于操作地图的组件，例如缩放按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/33/v3/GM1OOu0JQtuvlc1LOSe18A/zh-cn_image_0000002788468096.png?HW-CC-KV=V1&HW-CC-Date=20261114T004640Z&HW-CC-Expire=31536000000&HW-CC-Sign=7AC8D7498532D7A5ECE2AAF3C837797669C008D3A774107D5543E55465A08288)、定位按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/99/v3/Yvm6XgDMSc6nKkBdIZhMFA/zh-cn_image_0000002817507585.png?HW-CC-KV=V1&HW-CC-Date=20261114T004640Z&HW-CC-Expire=31536000000&HW-CC-Sign=6B375A57A5B6B7C4BA7CD80EF9D95185F992811E618032C52E56BF2D5FDA8D3F)、比例尺![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/pJ07s99sRx-h4URHIumt8g/zh-cn_image_0000002788308154.png?HW-CC-KV=V1&HW-CC-Date=20261114T004640Z&HW-CC-Expire=31536000000&HW-CC-Sign=A96BB6547FD6804213D606F518AABC023E2F918F6ED80B1C66F4AEDE8E28260F)等。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/SBnonPuWRFCH5CNcBoDQBA/zh-cn_image_0000002817427517.jpg?HW-CC-KV=V1&HW-CC-Date=20261114T004640Z&HW-CC-Expire=31536000000&HW-CC-Sign=8956660AD62153F818A0B57F03A51D92EDBC70FD31AA2DC005A89F10B86B7A1F "点击放大")

## 接口说明

以下是地图的控件相关接口，该功能有2种实现方式：

* 地图初始化时，可在初始化参数[MapOptions](../harmonyos-references/map-common.md#mapoptions)中设置是否启用控件功能，详细讲解见[显示地图](map-presenting.md)章节。
* 通过调用[MapComponentController](../harmonyos-references/map-map-mapcomponentcontroller.md)提供的set方法实现相关控件的开启或关闭。

| 接口名 | 描述 |
| --- | --- |
| [setZoomControlsEnabled](../harmonyos-references/map-map-mapcomponentcontroller.md#setzoomcontrolsenabled)(enabled: boolean): void | 设置是否启用缩放控制器。 |
| [setMyLocationEnabled](../harmonyos-references/map-map-mapcomponentcontroller.md#setmylocationenabled)(myLocationEnabled: boolean): void | 设置是否启用我的位置图层。 |
| [setMyLocationControlsEnabled](../harmonyos-references/map-map-mapcomponentcontroller.md#setmylocationcontrolsenabled)(enabled: boolean): void | 设置是否启用我的位置按钮。 |
| [setScaleControlsEnabled](../harmonyos-references/map-map-mapcomponentcontroller.md#setscalecontrolsenabled)(enabled: boolean): void | 设置是否启用比例尺。 |
| [setScalePosition](../harmonyos-references/map-map-mapcomponentcontroller.md#setscaleposition)(point: [mapCommon.MapPoint](../harmonyos-references/map-common.md#mappoint)): void | 设置比例尺控件的位置。 |
| [setAlwaysShowScaleEnabled](../harmonyos-references/map-map-mapcomponentcontroller.md#setalwaysshowscaleenabled)(enabled: boolean): void | 设置是否始终显示比例尺。 |
| [setCompassControlsEnabled](../harmonyos-references/map-map-mapcomponentcontroller.md#setcompasscontrolsenabled)(enabled: boolean): void | 设置是否启用指南针。 |
| [setLogoAlignment](../harmonyos-references/map-map-mapcomponentcontroller.md#setlogoalignment)(alignment: [mapCommon.LogoAlignment](../harmonyos-references/map-common.md#logoalignment)): void | 设置地图Logo的对齐方式。 |
| [setApproveNumberEnabled](../harmonyos-references/map-map-mapcomponentcontroller.md#setapprovenumberenabled)(enabled: boolean): void | 设置是否显示审图号，只有路由地在中国才会显示。 |

## 开发步骤

mapController对象在初始化地图时获取，初始化地图功能在[显示地图](map-presenting.md)章节中有详细讲解。

### 缩放控件

Map Kit提供了内置的缩放控件，默认情况下是开启的。

```typescript
// 开启缩放控件
this.mapController.setZoomControlsEnabled(true);
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/7jwN9vrRT32cH0LMJFwhIA/zh-cn_image_0000002788468098.jpg?HW-CC-KV=V1&HW-CC-Date=20261114T004640Z&HW-CC-Expire=31536000000&HW-CC-Sign=4708992110F6AB3E1C82553FC4E33A5E55E07841DD6BF110FE68C905AE516A26 "点击放大")

### 比例尺

Map Kit提供了内置的比例尺控件，默认情况下是关闭的。

```typescript
// 开启比例尺控件
this.mapController.setScaleControlsEnabled(true);
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/iM56A0TSQ9-i4xCPSagVxA/zh-cn_image_0000002817507587.jpg?HW-CC-KV=V1&HW-CC-Date=20261114T004640Z&HW-CC-Expire=31536000000&HW-CC-Sign=030B323A5CEB52BA7833F477BB02790867187CA3CC969592452D0EAC39804455 "点击放大")

**调整比例尺位置：**

可通过[setScalePosition](../harmonyos-references/map-map-mapcomponentcontroller.md#setscaleposition)方法设置比例尺控件的位置。

```typescript
let point: mapCommon.MapPoint = {
  // 以当前地图组件左上角为原点，向右移动1000px
  positionX: 1000,
  // 以当前地图组件左上角为原点，向下移动1000px
  positionY: 1000
};
this.mapController.setScalePosition(point);
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/2ybgfrj7RBmdCDOee_Vj3Q/zh-cn_image_0000002788308156.jpg?HW-CC-KV=V1&HW-CC-Date=20261114T004640Z&HW-CC-Expire=31536000000&HW-CC-Sign=4F771A3000B4E73CC3544ED5B91D1E0362285B043A56DA3232189208259840DD "点击放大")

**获取当前层级的比例尺大小：**

可通过[getScaleLevel](../harmonyos-references/map-map-mapcomponentcontroller.md#getscalelevel)方法获取当前层级比例尺大小。

```typescript
let level = this.mapController.getScaleLevel();
```

**获取比例尺控件宽高：**

可通过[getScaleControlsHeight](../harmonyos-references/map-map-mapcomponentcontroller.md#getscalecontrolsheight)和[getScaleControlsWidth](../harmonyos-references/map-map-mapcomponentcontroller.md#getscalecontrolswidth)方法获取当前比例尺控件宽高。

```typescript
// 获取比例尺控件的高度
let height = this.mapController.getScaleControlsHeight();
// 获取比例尺控件的宽度
let width = this.mapController.getScaleControlsWidth();
```

**设置比例尺控件常显：**

可通过[setAlwaysShowScaleEnabled](../harmonyos-references/map-map-mapcomponentcontroller.md#setalwaysshowscaleenabled)方法设置比例尺控件常显，通过[isAlwaysShowScaleEnabled](../harmonyos-references/map-map-mapcomponentcontroller.md#isalwaysshowscaleenabled)方法查询比例尺控件是否常显。

```typescript
// 设置比例尺控件常显
this.mapController.setAlwaysShowScaleEnabled(true);
// 查询比例尺控件是否常显
let scaleEnabled: boolean = this.mapController.isAlwaysShowScaleEnabled();
```

### 指南针

Map Kit提供了内置的指南针控件，默认情况下是开启的，控件位置默认显示在地图的右上角。如果是启用状态，当地图不是指向正北方向或者发生倾斜时，地图右上角会显示一个指南针图标，点击指南针可使地图旋转为正北方向并且取消倾斜；当地图为正北方向且未发生倾斜时，指南针图标隐藏。如果是禁用状态，将不会显示指南针图标。

```typescript
// 开启指南针控件
this.mapController.setCompassControlsEnabled(true);
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/hnLBhOJxQkqaHHBDlDAlWQ/zh-cn_image_0000002817427519.jpg?HW-CC-KV=V1&HW-CC-Date=20261114T004640Z&HW-CC-Expire=31536000000&HW-CC-Sign=F429DB1F520615581A03A8BF673C2269661D366E21E1FB596B0BE79D0E4C2388 "点击放大")

**调整指南针位置：**

可通过[setCompassPosition](../harmonyos-references/map-map-mapcomponentcontroller.md#setcompassposition)方法设置指南针控件的位置。

```typescript
let point: mapCommon.MapPoint = {
  // 以当前地图组件左上角为原点，向右移动1000px
  positionX: 1000,
  // 以当前地图组件左上角为原点，向下移动1000px
  positionY: 1000
};
this.mapController.setCompassPosition(point);
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/wzHUf67sRQaU82agw6KNAQ/zh-cn_image_0000002788468100.jpg?HW-CC-KV=V1&HW-CC-Date=20261114T004640Z&HW-CC-Expire=31536000000&HW-CC-Sign=ADB2AB86D01C975A5D3FF9BC05F7D4173189E1CCB109D4B487313B1A77F6C78E "点击放大")

### 地图Logo

Map Kit提供了调整地图Logo对齐方式的方法[setLogoAlignment](../harmonyos-references/map-map-mapcomponentcontroller.md#setlogoalignment)和调整地图边界与Logo之间的间距的方法[setLogoPadding](../harmonyos-references/map-map-mapcomponentcontroller.md#setlogopadding)。需注意，地图Logo不允许被遮挡，可通过[setLogoPadding](../harmonyos-references/map-map-mapcomponentcontroller.md#setlogopadding)方法设置地图边界区域，来避免logo被遮挡。

```typescript
// 将Logo放置在右下角位置
this.mapController.setLogoAlignment(mapCommon.LogoAlignment.BOTTOM_END);
// 设置地图边界与Logo之间的间距，单位：px
let padding: mapCommon.Padding = {
  right: 50,
  bottom: 50
};
this.mapController.setLogoPadding(padding);
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/bspRLiFYS1K9mKaOE8kVcw/zh-cn_image_0000002817507589.jpg?HW-CC-KV=V1&HW-CC-Date=20261114T004640Z&HW-CC-Expire=31536000000&HW-CC-Sign=A124AF8047E82B2A2CD538FFA2C67A9DBFB649D7232F3DC390B544D0945C6504 "点击放大")

### 审图号

审图号是指国家对地图产品进行审核并颁发的编号，用于标识地图已通过国家测绘地理信息局的审查。

Map Kit通过方法[setApproveNumberEnabled](../harmonyos-references/map-map-mapcomponentcontroller.md#setapprovenumberenabled)展示审图号。如图左下角：

```typescript
// 显示审图号
this.mapController.setApproveNumberEnabled(true);
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/mMVmVRbuRKCWuNKOmOZ-vA/zh-cn_image_0000002788308158.png?HW-CC-KV=V1&HW-CC-Date=20261114T004640Z&HW-CC-Expire=31536000000&HW-CC-Sign=6980803777601F5A09A411D464271221163E427C72D0EAEAB85E0E2403403A48 "点击放大")
