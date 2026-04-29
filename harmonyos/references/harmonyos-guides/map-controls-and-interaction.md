---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/map-controls-and-interaction
title: 控件交互
breadcrumb: 指南 > 应用服务 > Map Kit（地图服务） > 地图交互 > 控件交互
category: harmonyos-guides
scraped_at: 2026-04-29T13:39:07+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:9944573c2fbbb2d80953498fa4fa8a4c8935fd07b0f1ada0d9eb950007a8c945
---

## 场景介绍

从6.1.0(23)开始，支持在地图左下角设置审图号。

本章节将向您介绍如何使用地图的控件。

控件是指浮在地图组件上的一系列用于操作地图的组件，例如缩放按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/Mda6SYk_SSC4ye5Surd7Aw/zh-cn_image_0000002558605864.png?HW-CC-KV=V1&HW-CC-Date=20260429T053900Z&HW-CC-Expire=86400&HW-CC-Sign=F80373FD055D4C45355B0E2EE662DB6E4C83E523C72B3F275973902FE3FF859D)、定位按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/sY2ukDdhTIGuVqctpMKdqQ/zh-cn_image_0000002589325391.png?HW-CC-KV=V1&HW-CC-Date=20260429T053900Z&HW-CC-Expire=86400&HW-CC-Sign=F73AED27814487CB850AD4315FD019D1DAD08D851A92D6E358BD5533EF5DC05C)、比例尺![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/ScwuuJ4PRny4pYlla9FRGg/zh-cn_image_0000002589245329.png?HW-CC-KV=V1&HW-CC-Date=20260429T053900Z&HW-CC-Expire=86400&HW-CC-Sign=59ED255E12D4452AEEE20C2CE082B72863E787CBB72A1A65232CD6A3C59C1152)等。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/3h8oJhgJQj28HSQNEGtNaQ/zh-cn_image_0000002558765522.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T053900Z&HW-CC-Expire=86400&HW-CC-Sign=0AE90869E2438EF2FF417F89527645896CA8808DB6EFC01C12A4D86D4DAC7BAD "点击放大")

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/wWE8pdZ3Ss6VOmZOhyMPsw/zh-cn_image_0000002558605866.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T053900Z&HW-CC-Expire=86400&HW-CC-Sign=3E7B430C7CE4C4796EE3AB60148831B91E94E3ED9E4532E37042893E9D25B734 "点击放大")

### 比例尺

Map Kit提供了内置的比例尺控件，默认情况下是关闭的。

```
1. // 开启比例尺控件
2. this.mapController.setScaleControlsEnabled(true);
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/MrRLqyRjQ2ynTX0hXoyC7w/zh-cn_image_0000002589325393.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T053900Z&HW-CC-Expire=86400&HW-CC-Sign=26D48562E911489ECA0A0F1099921EC7A02B720F5A96A52F97CDC78FC1FB568E "点击放大")

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/VjkTpa0YSAefo6c9HpFAdA/zh-cn_image_0000002589245331.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T053900Z&HW-CC-Expire=86400&HW-CC-Sign=F79968E6FC0530A90047BEC6E019DA624ABD7E0BBBE0D905B5B3BCDB7DBECF9C "点击放大")

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/47LpJoiDTba9U991FEZ7IA/zh-cn_image_0000002558765524.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T053900Z&HW-CC-Expire=86400&HW-CC-Sign=41B518403A1B57AE255899359A62325D1C871AF0727DEB1E6C4C6CAE65E33666 "点击放大")

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/8PDsUdTaSOKxyOXmNdVgsw/zh-cn_image_0000002558605868.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T053900Z&HW-CC-Expire=86400&HW-CC-Sign=15C2E275D87CFEF5FA797B19CF180C90F7CD99E8940E6827C2B38B28821D68ED "点击放大")

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6a/v3/07JvZwozQSSXKBkDtYCPkQ/zh-cn_image_0000002589325395.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T053900Z&HW-CC-Expire=86400&HW-CC-Sign=C5900AB07D457B33E004829B759FA9546150E7AE79C1DAA2B052EA80D443A938 "点击放大")

### 审图号

审图号是指国家对地图产品进行审核并颁发的编号，用于标识地图已通过国家测绘地理信息局的审查。

Map Kit通过方法[setApproveNumberEnabled](../harmonyos-references/map-map-mapcomponentcontroller.md#setapprovenumberenabled)展示审图号。如图左下角：

```
1. // 显示审图号
2. this.mapController?.setApproveNumberEnabled(true);
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/33/v3/IbPcM7jZQc6jW-o3ceHPtw/zh-cn_image_0000002589245333.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T053900Z&HW-CC-Expire=86400&HW-CC-Sign=7C630626E66D6A3BB528396465C1DCFECE16C2BC46863D3C28F0833148C3FABA "点击放大")
