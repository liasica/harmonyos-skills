---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/map-type
title: 切换地图类型
breadcrumb: 指南 > 应用服务 > Map Kit（地图服务） > 创建地图 > 切换地图类型
category: harmonyos-guides
scraped_at: 2026-11-21T09:12:30+08:00
doc_updated_at: 2026-09-09
content_hash: sha256:7d4a5a3ac2f99fd8a15378f231f7eab905dcd70e2161957a1a399cf12cf0eab2
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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/1KN7W98dTdyowoSI0zmSyg/zh-cn_image_0000002793038094.jpg?HW-CC-KV=V1&HW-CC-Date=20261121T011230Z&HW-CC-Expire=31536000000&HW-CC-Sign=2E89B503670D0C62B192A10CCCD0A980E5EDB8065563B6B476A1B4BC87F96425 "点击放大")

**图2** 空地图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/17djQj6US1SACxVHkGz6Cg/zh-cn_image_0000002792878124.jpg?HW-CC-KV=V1&HW-CC-Date=20261121T011230Z&HW-CC-Expire=31536000000&HW-CC-Sign=276A249A86A34769DAEFD2BD75824120A65035D652BDF86643A496AE94257304 "点击放大")

**图3** 地形图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/ql2Mgd9cQ9K3-U-SlxnNrg/zh-cn_image_0000002821838031.jpg?HW-CC-KV=V1&HW-CC-Date=20261121T011230Z&HW-CC-Expire=31536000000&HW-CC-Sign=6E7801BE83DE1FCCD80F0EA02CA04F8EE7950969860E0A2CF400C1FABCC9E9BC "点击放大")

**图4** 卫星图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/8Su0yroARwiX9ACZCC9l2w/zh-cn_image_0000002821758033.jpg?HW-CC-KV=V1&HW-CC-Date=20261121T011230Z&HW-CC-Expire=31536000000&HW-CC-Sign=DA9EC126F8FE1229F27E5B0C2923BC9FFC9250FFF53BEF6E2DBFF9A33E88B56B "点击放大")

**图5** 混合地图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/v6_nyhFoQUmJ7R1ouc6_cw/zh-cn_image_0000002793038096.jpg?HW-CC-KV=V1&HW-CC-Date=20261121T011230Z&HW-CC-Expire=31536000000&HW-CC-Sign=FEA061FC9D8FC566E387CE1EF27141D85D39504EA4FD6126B9CF4F607D7AA4F9 "点击放大")

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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/44U7N8R_RcmeH0CdCxcmXQ/zh-cn_image_0000002792878126.jpg?HW-CC-KV=V1&HW-CC-Date=20261121T011230Z&HW-CC-Expire=31536000000&HW-CC-Sign=1191C30B746A139FA997F3E69A33ECA8E8F78EE2060555C9D1DF90961008D226 "点击放大")

   方式二：地图创建后，调用[setMapType](../harmonyos-references/map-map-mapcomponentcontroller.md#setmaptype)方法设置地图类型为地形图。设置为地形图时，为了获得最佳显示效果，推荐将地图缩放层级保持在5至14之间。

   ```typescript
   this.mapController.setMapType(mapCommon.MapType.TERRAIN);
   ```

   显示效果如下：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/xM3GwxfoREGy-6B0IobuwA/zh-cn_image_0000002821838033.jpg?HW-CC-KV=V1&HW-CC-Date=20261121T011230Z&HW-CC-Expire=31536000000&HW-CC-Sign=85EF97D5011E74F37E3A6B952357887911B49731043C9FC6DC12540CEAC48AE4 "点击放大")
