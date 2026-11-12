---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/map-type
title: 切换地图类型
breadcrumb: 指南 > 应用服务 > Map Kit（地图服务） > 创建地图 > 切换地图类型
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-09-09
content_hash: sha256:664b0490b170e2cc7bb75e7825937f9f527e578efab5722d2284f77436d5eca8
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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/v_or1vzOT6iJiSI0XsAA2g/zh-cn_image_0000002815399913.jpg?HW-CC-KV=V1&HW-CC-Date=20261112T233234Z&HW-CC-Expire=31536000000&HW-CC-Sign=5079ECA3369E3A36BB025C5FD0164780105F0A8543B400913ECB4BCB9AF770DE "点击放大")

**图2** 空地图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/nCVocCKXQGu-Do7CEdR91g/zh-cn_image_0000002786520338.jpg?HW-CC-KV=V1&HW-CC-Date=20261112T233234Z&HW-CC-Expire=31536000000&HW-CC-Sign=34D7690B35D1B59585C708DCB204957DA0F5558CF4AEEDE5104F86666F7642E5 "点击放大")

**图3** 地形图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d/v3/qUZYcIOhQDeZNDEeveQqIg/zh-cn_image_0000002786360410.jpg?HW-CC-KV=V1&HW-CC-Date=20261112T233234Z&HW-CC-Expire=31536000000&HW-CC-Sign=41A534C4F167FC539B2988FF6C5F0980DF853C30F34FC4E7570C9180AF1438DF "点击放大")

**图4** 卫星图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/fYC5o7ykRWStxBmWjoR0Jw/zh-cn_image_0000002815559831.jpg?HW-CC-KV=V1&HW-CC-Date=20261112T233234Z&HW-CC-Expire=31536000000&HW-CC-Sign=E41A1C68DDF2D94EA84A2664C09A797D39F36069A3AE067A6D814B338FC7AF77 "点击放大")

**图5** 混合地图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/3zEkXabsTmaII2uxmA-gxg/zh-cn_image_0000002815399915.jpg?HW-CC-KV=V1&HW-CC-Date=20261112T233234Z&HW-CC-Expire=31536000000&HW-CC-Sign=AE007088C74B185B70F89502D3D4119B2818BA7727A221C814CEBC8AB5C42310 "点击放大")

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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/SqBq3QbhQO2D-wha4-X3Gw/zh-cn_image_0000002786520340.jpg?HW-CC-KV=V1&HW-CC-Date=20261112T233234Z&HW-CC-Expire=31536000000&HW-CC-Sign=0B35A7EDE2F3741336AFE151386022C06640C93094E0D09E211FB1D740F58789 "点击放大")

   方式二：地图创建后，调用[setMapType](../harmonyos-references/map-map-mapcomponentcontroller.md#setmaptype)方法设置地图类型为地形图。设置为地形图时，为了获得最佳显示效果，推荐将地图缩放层级保持在5至14之间。

   ```typescript
   this.mapController.setMapType(mapCommon.MapType.TERRAIN);
   ```

   显示效果如下：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/HV8S4CMQR0-ZV6RPKSk7cA/zh-cn_image_0000002786360412.jpg?HW-CC-KV=V1&HW-CC-Date=20261112T233234Z&HW-CC-Expire=31536000000&HW-CC-Sign=95B17002782B0E2E5301BAA00FCC9F127176C9F2ED6CD1540D4A96DF794170D2 "点击放大")
