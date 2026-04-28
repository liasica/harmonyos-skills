---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/map-type
title: 切换地图类型
breadcrumb: 指南 > 应用服务 > Map Kit（地图服务） > 创建地图 > 切换地图类型
category: harmonyos-guides
scraped_at: 2026-04-28T07:49:43+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:c650df818576d7acb4bfe51714683a34ecd181675e817c3a892d59d0de13f7a3
---

## 场景介绍

从6.0.0(20)开始，支持卫星图和混合地图功能。

Map Kit支持以下地图类型：

* STANDARD：标准地图，展示道路、建筑物以及河流等重要的自然特征。
* NONE：空地图，没有加载任何数据的地图。
* TERRAIN：地形图，在保留了行政区划边界、POI、楼块等地图要素的基础上，呈现完整清晰描绘地形走势的标准地图。
* SATELLITE：卫星图，显示卫星照片的地图，只支持中国。
* HYBRID：混合地图，在显示卫星照片的同时也显示路网信息。

**图1** 标准地图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/F5bjqR-sQg-tYebIhu0PRQ/zh-cn_image_0000002552799358.jpg?HW-CC-KV=V1&HW-CC-Date=20260427T234942Z&HW-CC-Expire=86400&HW-CC-Sign=10B077843D702248A21BF4EF5CFF4B05C3A967360913F6C4CD3D64B3B119D917 "点击放大")

**图2** 空地图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/kmvUm4CbQ6muxUeZgn1vgw/zh-cn_image_0000002583439053.jpg?HW-CC-KV=V1&HW-CC-Date=20260427T234942Z&HW-CC-Expire=86400&HW-CC-Sign=8884E97AE116777E75D058CF2B272F6CB60794A30741822388A7D13225DFDACC "点击放大")

**图3** 地形图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/M4XZqoJ0QZaxZMGZNmLXRg/zh-cn_image_0000002552959008.jpg?HW-CC-KV=V1&HW-CC-Date=20260427T234942Z&HW-CC-Expire=86400&HW-CC-Sign=69211642C2100CBC332222F9DBDBF3740434138FD6C2F816A777A23799C5E497 "点击放大")

**图4** 卫星图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/GDuFA-R1SBi-KJ0sbXyANw/zh-cn_image_0000002583479009.jpg?HW-CC-KV=V1&HW-CC-Date=20260427T234942Z&HW-CC-Expire=86400&HW-CC-Sign=73D618CDC7B1D3E6A25D0985643A08768247772989A989432568638AA9CBE20A "点击放大")

**图5** 混合地图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/35/v3/1XD-b0O_TFyQA6b5NpA_Rg/zh-cn_image_0000002552799360.jpg?HW-CC-KV=V1&HW-CC-Date=20260427T234942Z&HW-CC-Expire=86400&HW-CC-Sign=12F33EFB783A0D290CAB7A8BA807228DB55ED6B998F2D6646C3F18DE2A9EA8EE "点击放大")

## 接口说明

Map Kit提供2种方式设置地图类型：

方式一：在初始化的时候，通过设置[MapOptions](../harmonyos-references/map-common.md#mapoptions)中的mapType属性来控制展示不同地图类型。

| 属性名 | 描述 |
| --- | --- |
| mapCommon.MapOptions.mapType | 地图初始化参数中的MapType地图类型。 |

方式二：地图创建后，可通过[setMapType](../harmonyos-references/map-map-mapcomponentcontroller.md#setmaptype)方法动态设置地图类型。

| 方法名 | 描述 |
| --- | --- |
| [setMapType](../harmonyos-references/map-map-mapcomponentcontroller.md#setmaptype)(mapType: [mapCommon.MapType](../harmonyos-references/map-common.md#maptype)): void | 设置地图类型。 |

## 开发步骤

1. 导入相关模块。

   ```
   1. import { mapCommon } from '@kit.MapKit';
   ```
2. 设置地图类型。

   方式一：

   在地图初始化的时候，在mapOptions参数中新增mapType属性：[mapCommon.MapType](../harmonyos-references/map-common.md#maptype).STANDARD（标准地图）。

   ```
   1. this.mapOptions = {
   2. position: {
   3. target: {
   4. latitude: 31.984410259206815,
   5. longitude: 118.76625379397866
   6. },
   7. zoom: 15
   8. },
   9. mapType: mapCommon.MapType.STANDARD
   10. };
   ```

   显示效果如下：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/5L-MS-TKRjKwpEMIYDVISg/zh-cn_image_0000002583439055.jpg?HW-CC-KV=V1&HW-CC-Date=20260427T234942Z&HW-CC-Expire=86400&HW-CC-Sign=D2141423F7D567D3D609809118D1FE4902814DE689BABAFCB5376F428F08C1AE "点击放大")

   方式二：地图创建后，调用[setMapType](../harmonyos-references/map-map-mapcomponentcontroller.md#setmaptype)方法设置地图类型为地形图。设置为地形图时，为了获得最佳显示效果，推荐将地图缩放层级保持在5至14之间。

   ```
   1. this.mapController.setMapType(mapCommon.MapType.TERRAIN);
   ```

   显示效果如下：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/QK48YnumSLaa3u5X5wfRtA/zh-cn_image_0000002552959010.jpg?HW-CC-KV=V1&HW-CC-Date=20260427T234942Z&HW-CC-Expire=86400&HW-CC-Sign=267DBBE2EEA34509665BAF94C5B118F0E19B2048A6B3271B541E9BB38509E2F2 "点击放大")
