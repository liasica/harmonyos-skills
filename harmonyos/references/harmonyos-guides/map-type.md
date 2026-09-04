---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/map-type
title: 切换地图类型
breadcrumb: 指南 > 应用服务 > Map Kit（地图服务） > 创建地图 > 切换地图类型
category: harmonyos-guides
scraped_at: 2026-09-05T06:15:12+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:c6cdcdf81253dc023e328326305ad880fb758597668a239b551bc44c89eb25ca
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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/zqn0rIX_RgC_gKWrAbJnsg/zh-cn_image_0000002742124177.jpg "点击放大")

**图2** 空地图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f7/v3/mPWUxSqeSKa8Wd8zgM3Now/zh-cn_image_0000002712245270.jpg "点击放大")

**图3** 地形图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/lId7186iTceV218joQxEnA/zh-cn_image_0000002742004219.jpg "点击放大")

**图4** 卫星图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/A-zR61M0RSuHoowG1bbtoA/zh-cn_image_0000002712405230.jpg "点击放大")

**图5** 混合地图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/_cDcBY4LRn6Hq5B2mRV4tA/zh-cn_image_0000002742124179.jpg "点击放大")

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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/g8CwFAkbSv-YqOQrWJyYjw/zh-cn_image_0000002712245272.jpg "点击放大")

   方式二：地图创建后，调用[setMapType](../harmonyos-references/map-map-mapcomponentcontroller.md#setmaptype)方法设置地图类型为地形图。设置为地形图时，为了获得最佳显示效果，推荐将地图缩放层级保持在5至14之间。

   ```typescript
   this.mapController.setMapType(mapCommon.MapType.TERRAIN);
   ```

   显示效果如下：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/uyBAdO1NTIWyx8InuyejPQ/zh-cn_image_0000002742004221.jpg "点击放大")
