---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/map-type
title: 切换地图类型
breadcrumb: 指南 > 应用服务 > Map Kit（地图服务） > 创建地图 > 切换地图类型
category: harmonyos-guides
scraped_at: 2026-04-29T13:39:01+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:c8bff3002c7404024724f8b667a2bedc7ca57bdd9dd89700f5d1578ed398ff24
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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/Wz3HvvvETb2aYXzStcbthw/zh-cn_image_0000002589325379.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T053859Z&HW-CC-Expire=86400&HW-CC-Sign=BE7D47FCCE101A84225BB81D56DA358CBF72409E081571C10DBA0A38EC9205AD "点击放大")

**图2** 空地图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/tOmcFEIfRMa-zW9ibVgOFw/zh-cn_image_0000002589245315.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T053859Z&HW-CC-Expire=86400&HW-CC-Sign=239A8BBDF8B20D2DFA77E3961CBC2C3DB592FB216121710CEEFB9C3310E8181C "点击放大")

**图3** 地形图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/R6Jc-f2UT7K9pK2yzreJHg/zh-cn_image_0000002558765510.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T053859Z&HW-CC-Expire=86400&HW-CC-Sign=0A3DE697AE922FC4EE375B8147E0B2798178D0B4D7609D292CEDEC5F39661892 "点击放大")

**图4** 卫星图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/eHexRAf_QKKqFqE3tbUM-w/zh-cn_image_0000002558605854.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T053859Z&HW-CC-Expire=86400&HW-CC-Sign=103CA1F81FCD811FE87662270A27B68BE8D0256BDBEB80CBF9F5E0C7B3C87424 "点击放大")

**图5** 混合地图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/rHyIYoD8Qtq28wTHBpxJLA/zh-cn_image_0000002589325381.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T053859Z&HW-CC-Expire=86400&HW-CC-Sign=CB3067FF9B19E8AF56050833209D018EEB2F7DC675D712966FE6E06DDF278F6B "点击放大")

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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/y-ucjhbwTcmTSAJbQTW2Kg/zh-cn_image_0000002589245317.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T053859Z&HW-CC-Expire=86400&HW-CC-Sign=E97BC4CFB25A215C50AF7277FDB116D57E4C3164668E4DDE0ACCD6F517BDAD1E "点击放大")

   方式二：地图创建后，调用[setMapType](../harmonyos-references/map-map-mapcomponentcontroller.md#setmaptype)方法设置地图类型为地形图。设置为地形图时，为了获得最佳显示效果，推荐将地图缩放层级保持在5至14之间。

   ```
   1. this.mapController.setMapType(mapCommon.MapType.TERRAIN);
   ```

   显示效果如下：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/8bv4PbRJS3iWjqs7vNPRDw/zh-cn_image_0000002558765512.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T053859Z&HW-CC-Expire=86400&HW-CC-Sign=2DC16AAD038FB7706785CBA3633250E281342E8CA13AA77CF9ECE8AA5824064E "点击放大")
