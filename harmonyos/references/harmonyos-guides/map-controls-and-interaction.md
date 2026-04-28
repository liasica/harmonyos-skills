---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/map-controls-and-interaction
title: 控件交互
breadcrumb: 指南 > 应用服务 > Map Kit（地图服务） > 地图交互 > 控件交互
category: harmonyos-guides
scraped_at: 2026-04-28T07:49:47+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:1c41a46bc46585557339ceba34404b9df6a2cf5e76bf06fa42d0b6f95fd7f304
---

## 场景介绍

从6.1.0(23)开始，支持在地图左下角设置审图号。

本章节将向您介绍如何使用地图的控件。

控件是指浮在地图组件上的一系列用于操作地图的组件，例如缩放按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/02/v3/f5Av5ilpQRWxlRK6579JAA/zh-cn_image_0000002583479019.png?HW-CC-KV=V1&HW-CC-Date=20260427T234946Z&HW-CC-Expire=86400&HW-CC-Sign=F0EEA7E0A895A958C329E34F3FBCCF31932348DA426D872EE6D89E0D915C35A1)、定位按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/-hoI1IVvQc6wFf2C4Pbi9A/zh-cn_image_0000002552799370.png?HW-CC-KV=V1&HW-CC-Date=20260427T234946Z&HW-CC-Expire=86400&HW-CC-Sign=680067D17402EB0B64BB1D1256062F59EC8BEC3CD37804AB29FC95CDE5C3F379)、比例尺![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/37/v3/uh7qYR5GTzSxCryKc4dXiw/zh-cn_image_0000002583439065.png?HW-CC-KV=V1&HW-CC-Date=20260427T234946Z&HW-CC-Expire=86400&HW-CC-Sign=2B375FA88E7353251B97EF185FC60C8DDA3E12E049206BA78A6C747157C1790A)等。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/popMAPfxR0aJeyHIg07Pbw/zh-cn_image_0000002552959020.jpg?HW-CC-KV=V1&HW-CC-Date=20260427T234946Z&HW-CC-Expire=86400&HW-CC-Sign=28C190A4330AAFC37BAF3155D934CC567D9BB1AD3FBC7A1CD3531CA38AFB5A2E "点击放大")

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

```
1. // 开启缩放控件
2. this.mapController.setZoomControlsEnabled(true);
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/5Jv8dVNdQ0-GZboTncKWoA/zh-cn_image_0000002583479021.jpg?HW-CC-KV=V1&HW-CC-Date=20260427T234946Z&HW-CC-Expire=86400&HW-CC-Sign=661CD13E530F3C154A58BD0CE016308CE3C711B52FD223FAD8A3907FD9A9A45F "点击放大")

### 比例尺

Map Kit提供了内置的比例尺控件，默认情况下是关闭的。

```
1. // 开启比例尺控件
2. this.mapController.setScaleControlsEnabled(true);
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/LwywQu4VTXWF7lUPMVMGtg/zh-cn_image_0000002552799372.jpg?HW-CC-KV=V1&HW-CC-Date=20260427T234946Z&HW-CC-Expire=86400&HW-CC-Sign=87091C1BA9FACBAC03B28756EE3969F8CD5BD9C522DA475EA5330940334DD36F "点击放大")

**调整比例尺位置：**

可通过[setScalePosition](../harmonyos-references/map-map-mapcomponentcontroller.md#setscaleposition)方法设置比例尺控件的位置。

```
1. let point: mapCommon.MapPoint = {
2. // 以当前地图组件左上角为原点，向右移动1000px
3. positionX: 1000,
4. // 以当前地图组件左上角为原点，向下移动1000px
5. positionY: 1000
6. };
7. this.mapController.setScalePosition(point);
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f8/v3/mao9tcl2SamRF6Lxs0Ku2A/zh-cn_image_0000002583439067.jpg?HW-CC-KV=V1&HW-CC-Date=20260427T234946Z&HW-CC-Expire=86400&HW-CC-Sign=A1147A1AB948D6D96DF37761D6A1D7954DD1B8B3206575073628FE77DBFD60AC "点击放大")

**获取当前层级的比例尺大小：**

可通过[getScaleLevel](../harmonyos-references/map-map-mapcomponentcontroller.md#getscalelevel)方法获取当前层级比例尺大小。

```
1. let level = this.mapController.getScaleLevel();
```

**获取比例尺控件宽高：**

可通过[getScaleControlsHeight](../harmonyos-references/map-map-mapcomponentcontroller.md#getscalecontrolsheight)和[getScaleControlsWidth](../harmonyos-references/map-map-mapcomponentcontroller.md#getscalecontrolswidth)方法获取当前比例尺控件宽高。

```
1. // 获取比例尺控件的高度
2. let height = this.mapController.getScaleControlsHeight();
3. // 获取比例尺控件的宽度
4. let width = this.mapController.getScaleControlsWidth();
```

**设置比例尺控件常显：**

可通过[setAlwaysShowScaleEnabled](../harmonyos-references/map-map-mapcomponentcontroller.md#setalwaysshowscaleenabled)方法设置比例尺控件常显，通过[isAlwaysShowScaleEnabled](../harmonyos-references/map-map-mapcomponentcontroller.md#isalwaysshowscaleenabled)方法查询比例尺控件是否常显。

```
1. // 设置比例尺控件常显
2. this.mapController.setAlwaysShowScaleEnabled(true);
3. // 查询比例尺控件是否常显
4. let scaleEnabled: boolean = this.mapController.isAlwaysShowScaleEnabled();
```

### 指南针

Map Kit提供了内置的指南针控件，默认情况下是开启的，控件位置默认显示在地图的右上角。如果是启用状态，当地图不是指向正北方向或者发生倾斜时，地图右上角会显示一个指南针图标，点击指南针可使地图旋转为正北方向并且取消倾斜；当地图为正北方向且未发生倾斜时，指南针图标隐藏。如果是禁用状态，将不会显示指南针图标。

```
1. // 开启指南针控件
2. this.mapController.setCompassControlsEnabled(true);
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/vTnzjDmKSOiMKIUk_2FVNQ/zh-cn_image_0000002552959022.jpg?HW-CC-KV=V1&HW-CC-Date=20260427T234946Z&HW-CC-Expire=86400&HW-CC-Sign=EB07AEFEFA29A206036CA0ECFEAC011AC85186974CFB21C1EA844FC10B1FFD6B "点击放大")

**调整指南针位置：**

可通过[setCompassPosition](../harmonyos-references/map-map-mapcomponentcontroller.md#setcompassposition)方法设置指南针控件的位置。

```
1. let point: mapCommon.MapPoint = {
2. // 以当前地图组件左上角为原点，向右移动1000px
3. positionX: 1000,
4. // 以当前地图组件左上角为原点，向下移动1000px
5. positionY: 1000
6. };
7. this.mapController.setCompassPosition(point);
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/Xp_eeE6XQ8OpVfBOKAMsng/zh-cn_image_0000002583479023.jpg?HW-CC-KV=V1&HW-CC-Date=20260427T234946Z&HW-CC-Expire=86400&HW-CC-Sign=4CA3F0FEB2C8070D94C63FC8F0B81E5BEBD8EB832FFAA21E1DD7F526EB72D02F "点击放大")

### 地图Logo

Map Kit提供了调整地图Logo对齐方式的方法[setLogoAlignment](../harmonyos-references/map-map-mapcomponentcontroller.md#setlogoalignment)和调整地图边界与Logo之间的间距的方法[setLogoPadding](../harmonyos-references/map-map-mapcomponentcontroller.md#setlogopadding)。需注意，地图Logo不允许被遮挡，可通过[setLogoPadding](../harmonyos-references/map-map-mapcomponentcontroller.md#setlogopadding)方法设置地图边界区域，来避免logo被遮挡。

```
1. // 将Logo放置在右下角位置
2. this.mapController.setLogoAlignment(mapCommon.LogoAlignment.BOTTOM_END);
3. // 设置地图边界与Logo之间的间距，单位：px
4. let padding: mapCommon.Padding = {
5. right: 50,
6. bottom: 50
7. };
8. this.mapController.setLogoPadding(padding);
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/9UCK_dpPQLCGjIO2yLiZcg/zh-cn_image_0000002552799374.jpg?HW-CC-KV=V1&HW-CC-Date=20260427T234946Z&HW-CC-Expire=86400&HW-CC-Sign=6E6A4602B8745C969082A528714E698C32C5196D24BB243534D6A2A687CA7845 "点击放大")

### 审图号

审图号是指国家对地图产品进行审核并颁发的编号，用于标识地图已通过国家测绘地理信息局的审查。

Map Kit通过方法[setApproveNumberEnabled](../harmonyos-references/map-map-mapcomponentcontroller.md#setapprovenumberenabled)展示审图号。如图左下角：

```
1. // 显示审图号
2. this.mapController?.setApproveNumberEnabled(true);
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/-pB-8cFqS_yXp2lEuGnMVg/zh-cn_image_0000002583439069.jpg?HW-CC-KV=V1&HW-CC-Date=20260427T234946Z&HW-CC-Expire=86400&HW-CC-Sign=B51ED7AE1E092EDC9BA4926FB3B5B3E87F3E83BBB755E0324BE9F7911CA8BD5E "点击放大")
