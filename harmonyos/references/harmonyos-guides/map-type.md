---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/map-type
title: 切换地图类型
breadcrumb: 指南 > 应用服务 > Map Kit（地图服务） > 创建地图 > 切换地图类型
category: harmonyos-guides
scraped_at: 2026-11-14T08:48:24+08:00
doc_updated_at: 2026-09-09
content_hash: sha256:e2c46486c8cc6aac65be34dc261172e2d9dc2afdda74c91b2a505b0da3861a39
---

## 场景介绍

从6.0.0(20)开始，支持卫星图和混合地图功能。

Map Kit支持以下地图类型：

* STANDARD：标准地图，展示道路、建筑物以及河流等重要的自然特征。
* NONE：空地图，没有加载任何数据的地图。
* TERRAIN：地形图，在保留了行政区划边界、POI、楼块等地图要素的基础上，呈现完整清晰描绘地形走势的标准地图。
* SATELLITE：卫星图，显示卫星照片的地图，只支持中国。适用于需要高精度地理信息的场景。
* HYBRID：混合地图，在显示卫星照片的同时也显示路网信息。适用于需要结合卫星图像与路网信息的导航应用等，以增强实用性与指导性。

**图1** 标准地图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/meusJootQ7S8bhcauHO1Rg/zh-cn_image_0000002817507573.jpg?HW-CC-KV=V1&HW-CC-Date=20261114T004823Z&HW-CC-Expire=31536000000&HW-CC-Sign=6712B4D067F1B7182EADD5F5339C406346DCE6EB8E80649C3A77411B0474E735 "点击放大")

**图2** 空地图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/CvavFLQsSkSkBJWe_zDN2w/zh-cn_image_0000002788308142.jpg?HW-CC-KV=V1&HW-CC-Date=20261114T004823Z&HW-CC-Expire=31536000000&HW-CC-Sign=C13A3B858C4418CC2597333B57E4A48122F00C82A7840CBEB7A1B20B9052B834 "点击放大")

**图3** 地形图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/bSwcwWVtRLKsvASxmJM66A/zh-cn_image_0000002817427505.jpg?HW-CC-KV=V1&HW-CC-Date=20261114T004823Z&HW-CC-Expire=31536000000&HW-CC-Sign=49A3A043EF106CA6349D5638275BA523CB6C7FF62B11C4FF7762DB8E0B48BC6E "点击放大")

**图4** 卫星图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/wZuO2rm7SVub4fwCbmRO8g/zh-cn_image_0000002788468086.jpg?HW-CC-KV=V1&HW-CC-Date=20261114T004823Z&HW-CC-Expire=31536000000&HW-CC-Sign=F374D31B6E8C076618D1F9E1A4427EAB8D1115D8CFE04F65CD814C184689267C "点击放大")

**图5** 混合地图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/5e8GdW1GRCmKUWnAgxEPlA/zh-cn_image_0000002817507575.jpg?HW-CC-KV=V1&HW-CC-Date=20261114T004823Z&HW-CC-Expire=31536000000&HW-CC-Sign=0CA39BA29AF4E7249FBD96E9BE9FB81B99A20585CC4C3452D560E2ADF6DAADF7 "点击放大")

## 接口说明

Map Kit提供2种方式设置地图类型：

方式一：在初始化的时候，通过设置[MapOptions](../harmonyos-references/map-common.md#mapoptions)中的mapType属性来控制展示不同地图类型。

| 属性名 | 描述 |
| --- | --- |
| mapCommon.MapOptions.mapType | 地图初始化参数中的MapType地图类型。 |

方式二：地图创建后，可通过[setMapType](../harmonyos-references/map-map-mapcomponentcontroller.md#setmaptype)方法动态设置地图类型。

| 接口名 | 描述 |
| --- | --- |
| [setMapType](../harmonyos-references/map-map-mapcomponentcontroller.md#setmaptype)(mapType: [mapCommon.MapType](../harmonyos-references/map-common.md#maptype)): void | 设置地图类型。 |

## 开发步骤

1. 导入相关模块。

   ```typescript
   import { mapCommon } from '@kit.MapKit';
   ```
2. 设置地图类型。

   方式一：

   在地图初始化的时候，在mapOptions参数中新增mapType属性：[mapCommon.MapType](../harmonyos-references/map-common.md#maptype).STANDARD（标准地图）。

   ```typescript
   this.mapOptions = {
     position: {
       target: {
         latitude: 31.984410259206815,
         longitude: 118.76625379397866
       },
       zoom: 15
     },
     mapType: mapCommon.MapType.STANDARD
   };
   ```

   显示效果如下：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/_YCBxsQhTme3VfPtowgPxQ/zh-cn_image_0000002788308144.jpg?HW-CC-KV=V1&HW-CC-Date=20261114T004823Z&HW-CC-Expire=31536000000&HW-CC-Sign=92FB6ACFE35E756CD8CA146EDF0F8FB7F87C6385DF2B29DABE504A2695A8AFE1 "点击放大")

   方式二：地图创建后，调用[setMapType](../harmonyos-references/map-map-mapcomponentcontroller.md#setmaptype)方法设置地图类型为地形图。设置为地形图时，为了获得最佳显示效果，推荐将地图缩放层级保持在5至14之间。

   ```typescript
   this.mapController.setMapType(mapCommon.MapType.TERRAIN);
   ```

   显示效果如下：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/vclzQnSFTTeyc8uEyCFmPg/zh-cn_image_0000002817427507.jpg?HW-CC-KV=V1&HW-CC-Date=20261114T004823Z&HW-CC-Expire=31536000000&HW-CC-Sign=86C8199FBCA2C0EE48B234B4E6F256CB589827783CFEDACBDA79DBD049E26C8D "点击放大")
