---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/map-controls-and-interaction
title: 控件交互
breadcrumb: 指南 > 应用服务 > Map Kit（地图服务） > 地图交互 > 控件交互
category: harmonyos-guides
scraped_at: 2026-11-19T09:49:05+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:313f6bf56a6fc27f57752a428b19710c8cb6b20e781863d77b08ca462464f532
---

## 场景介绍

从6.1.0(23)开始，支持在地图左下角设置审图号。

本章节将向您介绍如何使用地图的控件。

控件是指浮在地图组件上的一系列用于操作地图的组件，例如缩放按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/awCfugc-T9ybQXO5p6Zi1A/zh-cn_image_0000002791566482.png?HW-CC-KV=V1&HW-CC-Date=20261119T014810Z&HW-CC-Expire=31536000000&HW-CC-Sign=550D325000CC6AF26DD7A30C3CC885FD78C0BEB3B9E5E76A2E8634AEC522B57B)、定位按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/8EOnr2QdSb-fB-8Px9i8vQ/zh-cn_image_0000002820526435.png?HW-CC-KV=V1&HW-CC-Date=20261119T014810Z&HW-CC-Expire=31536000000&HW-CC-Sign=CCEAE0D573FE6E2797A2208D35F97AB85B75607F51F2E4E00B968A9792988F54)、比例尺![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/b-jxHOCHTz2z-WB_eJQROg/zh-cn_image_0000002820406435.png?HW-CC-KV=V1&HW-CC-Date=20261119T014810Z&HW-CC-Expire=31536000000&HW-CC-Sign=FBA4FF32BE134099C615B75BFB64AE65B00A7110428FBC70BCB07511CACC24FC)等。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/_wjHnPt8Q4OAUJp6h5RIqw/zh-cn_image_0000002791726456.jpg?HW-CC-KV=V1&HW-CC-Date=20261119T014810Z&HW-CC-Expire=31536000000&HW-CC-Sign=D4E317183F226971CDB10BAF73DFA5CD2889DA22DC8F744A7AE9F9D0EBC18AFA "点击放大")

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/1wLePq_vTiWvaf_BcSkuZw/zh-cn_image_0000002791566484.jpg?HW-CC-KV=V1&HW-CC-Date=20261119T014810Z&HW-CC-Expire=31536000000&HW-CC-Sign=E0AD0F2CC4BA3446080A95088E4C94CD11C22BA63556BB5108999C2F4466AC4E "点击放大")

### 比例尺

Map Kit提供了内置的比例尺控件，默认情况下是关闭的。

```typescript
// 开启比例尺控件
this.mapController.setScaleControlsEnabled(true);
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/B8k7ZjvmSIi5R66m9RR8IA/zh-cn_image_0000002820526437.jpg?HW-CC-KV=V1&HW-CC-Date=20261119T014810Z&HW-CC-Expire=31536000000&HW-CC-Sign=FD878BB37BD06AEF262568E5F05F61C3582410A61A4BD03B5620E4780376EA58 "点击放大")

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/S1Pjm2Y1SIukpXKzxMeM6g/zh-cn_image_0000002820406437.jpg?HW-CC-KV=V1&HW-CC-Date=20261119T014810Z&HW-CC-Expire=31536000000&HW-CC-Sign=A5CE6A0F560FA3BACBA49BCC5A0BCC610BA83C5D7C9F89649DC02C01A9242E1E "点击放大")

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/03/v3/UDT5a0OmS3qGSrIcnJuovw/zh-cn_image_0000002791726458.jpg?HW-CC-KV=V1&HW-CC-Date=20261119T014810Z&HW-CC-Expire=31536000000&HW-CC-Sign=3C1A629A0D5D096C405ADEF6B8BAC086D77ADCBB13E23F9F14D51E85F8BAA9F9 "点击放大")

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/Gp_51ugkRKOM6X2GX_Xz6A/zh-cn_image_0000002791566486.jpg?HW-CC-KV=V1&HW-CC-Date=20261119T014810Z&HW-CC-Expire=31536000000&HW-CC-Sign=39C6004EC4F8EFA167E6A41AEDD1910BC1781FC1D77DCB3EFEA45E6CE89C411B "点击放大")

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/88Swt9xNTquKVsvmGMX5Vw/zh-cn_image_0000002820526439.jpg?HW-CC-KV=V1&HW-CC-Date=20261119T014810Z&HW-CC-Expire=31536000000&HW-CC-Sign=F45C6FC25EFF72B0DF5DBD0BEE62994C29ADED6C9F339F9D76C734BD5028FB9A "点击放大")

### 审图号

审图号是指国家对地图产品进行审核并颁发的编号，用于标识地图已通过国家测绘地理信息局的审查。

Map Kit通过方法[setApproveNumberEnabled](../harmonyos-references/map-map-mapcomponentcontroller.md#setapprovenumberenabled)展示审图号。如图左下角：

```typescript
// 显示审图号
this.mapController.setApproveNumberEnabled(true);
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/VLzHX8I6RiCU7EbrrSjpzQ/zh-cn_image_0000002820406439.png?HW-CC-KV=V1&HW-CC-Date=20261119T014810Z&HW-CC-Expire=31536000000&HW-CC-Sign=267C797FF4C0A303BCE0C91E42E8A7242EFD90E31D32A94D2E8FCE540034806D "点击放大")
