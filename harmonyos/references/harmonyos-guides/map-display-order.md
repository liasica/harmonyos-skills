---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/map-display-order
title: 设置地图元素压盖顺序
breadcrumb: 指南 > 应用服务 > Map Kit（地图服务） > 在地图上绘制 > 设置地图元素压盖顺序
category: harmonyos-guides
scraped_at: 2026-04-28T07:49:51+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:9bec2aded85387afa11a3bb62503e7cbe46b641ee59640414ad19d88f11c057f
---

## 场景介绍

本章节将向您介绍如何设置地图元素的层级压盖关系。

设置地图元素的显示顺序，按照从低到高排列，即后面的地图元素会压盖前面的地图元素。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/WG8hup4MQkS3qftTgBqfDA/zh-cn_image_0000002583439089.jpg?HW-CC-KV=V1&HW-CC-Date=20260427T234950Z&HW-CC-Expire=86400&HW-CC-Sign=6E65F42B8A9E663CF8E9D758A2DBD057951129DF0E72B65104BBB58C4DA71CE3 "点击放大")

**表1** 地图元素类型压盖顺序

| 枚举 | 枚举值 | 枚举含义 |
| --- | --- | --- |
| OVERLAY | 1 | 覆盖物，包括[MapCircle](../harmonyos-references/map-map-mapcircle.md)、[MapPolygon](../harmonyos-references/map-map-mappolygon.md)、[MapPolyline](../harmonyos-references/map-map-mappolyline.md)、[MapArc](../harmonyos-references/map-map-maparc.md)、[ImageOverlay](../harmonyos-references/map-map-imageoverlay.md)、[TraceOverlay](../harmonyos-references/map-map-traceoverlay.md)。 |
| POI | 2 | 底图[Poi](../harmonyos-references/map-common.md#poi)。 |
| CUSTOM\_POI | 3 | 支持碰撞的覆盖物，包括[PointAnnotation](../harmonyos-references/map-map-pointannotation.md)、[Bubble](../harmonyos-references/map-map-bubble.md)。 |
| MARKER | 4 | 包括[Marker](../harmonyos-references/map-map-marker.md)、[ClusterOverlay](../harmonyos-references/map-map-clusteroverlay.md)。 |

## 接口说明

设置层级压盖关系功能主要由[MapElementType](../harmonyos-references/map-common.md#mapelementtype)、[setDisplayOrder](../harmonyos-references/map-map-mapcomponentcontroller.md#setdisplayorder)提供，更多接口及使用方法请参见[接口文档](../harmonyos-references/map-map-mapcomponentcontroller.md#setdisplayorder)。

| 接口名 | 描述 |
| --- | --- |
| [mapCommon.MapElementType](../harmonyos-references/map-common.md#mapelementtype) | 地图元素类型。 |
| [setDisplayOrder](../harmonyos-references/map-map-mapcomponentcontroller.md#setdisplayorder)(types: Array<[mapCommon.MapElementType](../harmonyos-references/map-common.md#mapelementtype)>): void | 设置地图元素的显示顺序。 |

## 开发步骤

1. 导入相关模块。

   ```
   1. import { mapCommon, map, MapComponent } from '@kit.MapKit';
   2. import { AsyncCallback } from '@kit.BasicServicesKit';
   ```
2. 设置地图元素层级压盖关系。

   ```
   1. @Entry
   2. @Component
   3. struct MarkerDemo {
   4. private mapOptions?: mapCommon.MapOptions;
   5. private mapController?: map.MapComponentController;
   6. private callback?: AsyncCallback<map.MapComponentController>;
   7. private mapEventManager?: map.MapEventManager;
   8. private marker?: map.Marker;
   9. private bubble?: map.Bubble;

   11. aboutToAppear(): void {
   12. // 地图初始化参数
   13. this.mapOptions = {
   14. position: {
   15. target: {
   16. latitude: 31.984410259206815,
   17. longitude: 118.26625379397866
   18. },
   19. zoom: 10
   20. }
   21. };
   22. this.callback = async (err, mapController) => {
   23. if (!err) {
   24. this.mapController = mapController;
   25. this.mapEventManager = this.mapController.getEventManager();
   26. // Marker初始化参数
   27. let markerOptions: mapCommon.MarkerOptions = {
   28. position: {
   29. latitude: 31.984410259206815,
   30. longitude: 118.26625379397866
   31. },
   32. rotation: 0,
   33. visible: true,
   34. zIndex: 0,
   35. alpha: 1,
   36. anchorU: 0.5,
   37. anchorV: 1,
   38. clickable: true,
   39. draggable: true,
   40. flat: false
   41. };
   42. // 创建Marker
   43. try {
   44. this.marker = await this.mapController.addMarker(markerOptions);
   45. } catch (e) {
   46. console.error(`Failed to create the marker, code is：${e.code}, message is ${e.message}`);
   47. }
   48. let bubbleOptions: mapCommon.BubbleParams = {
   49. // 气泡位置
   50. positions: [[{
   51. latitude: 32.384410259206815,
   52. longitude: 118.26625379397866
   53. }]],
   54. // 设置图标，必须提供4个方向的图标，图标存放在resources/rawfile
   55. icons: [
   56. 'speed_limit_10.png',
   57. 'speed_limit_20.png',
   58. 'speed_limit_30.png',
   59. 'speed_limit_40.png'
   60. ],
   61. // 定义气泡的显示属性，为true时，在被碰撞后仍能显示
   62. forceVisible: true,
   63. // 定义气泡碰撞优先级，数值越大，优先级越低
   64. priority: 3,
   65. // 定义气泡展示的最小层级
   66. minZoom: 2,
   67. // 定义气泡展示的最大层级
   68. maxZoom: 20,
   69. // 定义气泡是否可见
   70. visible: true,
   71. // 定义气泡叠加层级属性
   72. zIndex: 1
   73. }
   74. // 添加气泡
   75. try {
   76. this.bubble = await this.mapController.addBubble(bubbleOptions);
   77. } catch (e) {
   78. console.error(`Failed to create the bubble, code is：${e.code}, message is ${e.message}`);
   79. }
   80. let imageOverlayParams: mapCommon.ImageOverlayParams = {
   81. // 覆盖物范围
   82. bounds: {
   83. southwest: {
   84. latitude: 32,
   85. longitude: 118
   86. },
   87. northeast: {
   88. latitude: 32.4,
   89. longitude: 118.4
   90. }
   91. },
   92. // 覆盖物图片
   93. image: 'icon/icon.png',
   94. transparency: 0.3,
   95. zIndex: 101,
   96. anchorU: 0.5,
   97. anchorV: 0.5,
   98. clickable: true,
   99. visible: true,
   100. bearing: 0
   101. };
   102. // 添加覆盖物
   103. try {
   104. await this.mapController?.addImageOverlay(imageOverlayParams);
   105. } catch (e) {
   106. console.error(`Failed to create the imageOverlay, code is：${e.code}, message is ${e.message}`);
   107. }

   109. // 设置压盖顺序，最底层的是覆盖物，后面依次是POI、支持碰撞的覆盖物和Marker，Marker在最表面一层
   110. let mapElementTypeArr: Array<mapCommon.MapElementType> = [
   111. mapCommon.MapElementType.OVERLAY,
   112. mapCommon.MapElementType.POI,
   113. mapCommon.MapElementType.CUSTOM_POI,
   114. mapCommon.MapElementType.MARKER];
   115. this.mapController.setDisplayOrder(mapElementTypeArr);
   116. } else {
   117. console.error(`Failed to initialize the map, code is：${err.code}, message is ${err.message}`);
   118. }
   119. }
   120. }

   122. build() {
   123. Stack() {
   124. Column() {
   125. MapComponent({ mapOptions: this.mapOptions, mapCallback: this.callback });
   126. }.width('100%')
   127. }.height('100%')
   128. }
   129. }
   ```
