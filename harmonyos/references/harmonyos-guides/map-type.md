---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/map-type
title: 切换地图类型
breadcrumb: 指南 > 应用服务 > Map Kit（地图服务） > 创建地图 > 切换地图类型
category: harmonyos-guides
scraped_at: 2026-11-19T09:49:05+08:00
doc_updated_at: 2026-09-09
content_hash: sha256:6828a784e1609d11e08fcd5cb984b710c6ee281d746b28c06c17713c4a9eb0bc
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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/B9yQAx_2T3WE9U2e5bT9Gw/zh-cn_image_0000002820526423.jpg?HW-CC-KV=V1&HW-CC-Date=20261119T014904Z&HW-CC-Expire=31536000000&HW-CC-Sign=B53DACDA6BCDC06F1B366FB838240DF0F0293BF312F71E9F388927B12CD97217 "点击放大")

**图2** 空地图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/bme7ZwQQQcunCLIWsZUZEA/zh-cn_image_0000002820406423.jpg?HW-CC-KV=V1&HW-CC-Date=20261119T014904Z&HW-CC-Expire=31536000000&HW-CC-Sign=112261EAD15FC632788D4BBC271FDB5B6D203C9BF86058D86E6EC7095B72E018 "点击放大")

**图3** 地形图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/XI-lYfgEQ7a2dnYtU8GxmA/zh-cn_image_0000002791726444.jpg?HW-CC-KV=V1&HW-CC-Date=20261119T014904Z&HW-CC-Expire=31536000000&HW-CC-Sign=3F88DAD8B5F41015EAC974260352AE85A2CA36695D071BD00C535BED6161DD47 "点击放大")

**图4** 卫星图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/M5XZAvUkTkKzkPxCveLfgA/zh-cn_image_0000002791566472.jpg?HW-CC-KV=V1&HW-CC-Date=20261119T014904Z&HW-CC-Expire=31536000000&HW-CC-Sign=D3BC65FB3474030B223BD64B0EA09B5283F7B9AA5639547B8E1D3CFF791192F1 "点击放大")

**图5** 混合地图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/jTrdBImoQkuDFAfXZ9mi5g/zh-cn_image_0000002820526425.jpg?HW-CC-KV=V1&HW-CC-Date=20261119T014904Z&HW-CC-Expire=31536000000&HW-CC-Sign=C70E297B585E62795D129DFAFFBB997249B49607C811B021A40ABB9C99C276CA "点击放大")

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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/hon42uYgTMib69IYbFW5KQ/zh-cn_image_0000002820406425.jpg?HW-CC-KV=V1&HW-CC-Date=20261119T014904Z&HW-CC-Expire=31536000000&HW-CC-Sign=ABE47568A6837AFC1A12F1FDD96C5969A1439C75A6655539532652430CDFBC0D "点击放大")

   方式二：地图创建后，调用[setMapType](../harmonyos-references/map-map-mapcomponentcontroller.md#setmaptype)方法设置地图类型为地形图。设置为地形图时，为了获得最佳显示效果，推荐将地图缩放层级保持在5至14之间。

   ```typescript
   this.mapController.setMapType(mapCommon.MapType.TERRAIN);
   ```

   显示效果如下：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/01/v3/o3SAYFZ2TQCInhePgq5OSQ/zh-cn_image_0000002791726446.jpg?HW-CC-KV=V1&HW-CC-Date=20261119T014904Z&HW-CC-Expire=31536000000&HW-CC-Sign=37557F0A8223FD682D43C4670E35526FDA82400077D1AB0B20CB8CA15581602D "点击放大")
