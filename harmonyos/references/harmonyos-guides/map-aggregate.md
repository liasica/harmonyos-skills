---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/map-aggregate
title: 点聚合
breadcrumb: 指南 > 应用服务 > Map Kit（地图服务） > 在地图上绘制 > 点聚合
category: harmonyos-guides
scraped_at: 2026-04-29T13:39:10+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:c3d38361dae14d7d38ca396b2005b7216d0466337c71f4ff875e4d4e9290bff9
---

## 场景介绍

本章节将详细介绍如何基于地图数据实现点聚合功能。

您可以通过比例尺缩放自适应聚合效果，聚合图标可点击。聚合支持功能：

* 支持按距离聚合[ClusterItem](../harmonyos-references/map-common.md#clusteritem)。
* 支持绘制聚合覆盖物的默认图标。
* 支持绘制聚合覆盖物的[自定义图标](../harmonyos-references/map-common.md#getcustomicon)。
* 支持监听聚合覆盖物的点击事件。
* 支持添加单个[ClusterItem](../harmonyos-references/map-common.md#clusteritem)到聚合覆盖物中。
* 支持删除聚合覆盖物。
* 支持移动地图时重绘聚合覆盖物。

5.0.3(15)开始，支持聚合标记点击事件监听功能。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/SteZ7IeuQJO_Wyk5TXar_w/zh-cn_image_0000002589245351.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T053908Z&HW-CC-Expire=86400&HW-CC-Sign=DD888B7D54504B013280109AE768AC17505B2DC1FD915BE1542C735A317818AC "点击放大")

## 接口说明

聚合功能主要由[ClusterOverlayParams](../harmonyos-references/map-common.md#clusteroverlayparams)、[addClusterOverlay](../harmonyos-references/map-map-mapcomponentcontroller.md#addclusteroverlay)、[ClusterOverlay](../harmonyos-references/map-map-clusteroverlay.md)提供，更多接口及使用方法请参见[接口文档](../harmonyos-references/map-map-clusteroverlay.md)。

| 接口名 | 描述 |
| --- | --- |
| [ClusterOverlayParams](../harmonyos-references/map-common.md#clusteroverlayparams) | 点聚合参数。 |
| [addClusterOverlay](../harmonyos-references/map-map-mapcomponentcontroller.md#addclusteroverlay)(params: [mapCommon.ClusterOverlayParams](../harmonyos-references/map-common.md#clusteroverlayparams)): Promise<[ClusterOverlay](../harmonyos-references/map-map-clusteroverlay.md)> | 聚合接口，支持节点聚合能力。 |
| [ClusterOverlay](../harmonyos-references/map-map-clusteroverlay.md) | 点聚合，支持更新和查询相关属性。 |

## 开发步骤

1. 导入相关模块。

   ```
   1. import { map, mapCommon, MapComponent } from '@kit.MapKit';
   2. import { AsyncCallback } from '@kit.BasicServicesKit';
   ```
2. 新增聚合图层。

   ```
   1. @Entry
   2. @Component
   3. struct ClusterOverlayDemo {
   4. private mapOptions?: mapCommon.MapOptions;
   5. private mapController?: map.MapComponentController;
   6. private callback?: AsyncCallback<map.MapComponentController>;

   8. aboutToAppear(): void {
   9. this.mapOptions = {
   10. position: {
   11. target: {
   12. latitude: 31.98,
   13. longitude: 118.7
   14. },
   15. zoom: 7
   16. }
   17. }

   19. this.callback = async (err, mapController) => {
   20. if (!err) {
   21. this.mapController = mapController;
   22. // 生成待聚合点
   23. let clusterItem1: mapCommon.ClusterItem = {
   24. position: {
   25. latitude: 31.98,
   26. longitude: 118.7
   27. }
   28. };
   29. let clusterItem2: mapCommon.ClusterItem = {
   30. position: {
   31. latitude: 32.99,
   32. longitude: 118.9
   33. }
   34. };
   35. let clusterItem3: mapCommon.ClusterItem = {
   36. position: {
   37. latitude: 31.5,
   38. longitude: 118.7
   39. }
   40. };
   41. let clusterItem4: mapCommon.ClusterItem = {
   42. position: {
   43. latitude: 30,
   44. longitude: 118.7
   45. }
   46. };
   47. let clusterItem5: mapCommon.ClusterItem = {
   48. position: {
   49. latitude: 29.98,
   50. longitude: 117.7
   51. }
   52. };
   53. let clusterItem6: mapCommon.ClusterItem = {
   54. position: {
   55. latitude: 31.98,
   56. longitude: 120.7
   57. }
   58. };
   59. let clusterItem7: mapCommon.ClusterItem = {
   60. position: {
   61. latitude: 25.98,
   62. longitude: 119.7
   63. }
   64. };
   65. let clusterItem8: mapCommon.ClusterItem = {
   66. position: {
   67. latitude: 30.98,
   68. longitude: 110.7
   69. }
   70. };
   71. let clusterItem9: mapCommon.ClusterItem = {
   72. position: {
   73. latitude: 30.98,
   74. longitude: 115.7
   75. }
   76. };
   77. let clusterItem10: mapCommon.ClusterItem = {
   78. position: {
   79. latitude: 28.98,
   80. longitude: 122.7
   81. }
   82. };
   83. let array: Array<mapCommon.ClusterItem> = [
   84. clusterItem1,
   85. clusterItem2,
   86. clusterItem3,
   87. clusterItem4,
   88. clusterItem5,
   89. clusterItem6,
   90. clusterItem7,
   91. clusterItem8,
   92. clusterItem9,
   93. clusterItem10
   94. ]
   95. for(let index = 0; index < 100; index++){
   96. array.push(clusterItem1)
   97. }
   98. for(let index = 0; index < 10; index++){
   99. array.push(clusterItem2)
   100. }
   101. // 生成聚合图层的入参 聚合distance设置为100vp
   102. let clusterOverlayParams: mapCommon.ClusterOverlayParams = {
   103. distance: 100,
   104. clusterItems: array
   105. };
   106. try {
   107. // 调用addClusterOverlay生成聚合图层
   108. await this.mapController.addClusterOverlay(clusterOverlayParams);
   109. } catch (e) {
   110. console.error(`code:${e.code}, message:${e.message}`);
   111. }
   112. } else {
   113. console.error(`Failed to initialize the map, code is：${err.code}, message is ${err.message}`);
   114. }
   115. }
   116. }

   118. build() {
   119. Stack() {
   120. Column() {
   121. MapComponent({ mapOptions: this.mapOptions, mapCallback: this.callback })
   122. .width('100%')
   123. .height('100%');
   124. }.width('100%')
   125. }.height('100%')
   126. }
   127. }
   ```
3. 聚合标记点击事件监听。

   ```
   1. let callback1 = (markerClusterInfo: map.MarkerClusterInfo) => {
   2. console.info("markerClusterClick", `callback1 markerClusterInfo`);
   3. };
   4. // 添加监听
   5. clusterOverlay.on("markerClusterClick", callback1);
   6. // 取消监听
   7. clusterOverlay.off("markerClusterClick", callback1);
   ```
