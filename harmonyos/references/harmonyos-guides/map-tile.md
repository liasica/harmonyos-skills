---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/map-tile
title: 瓦片图层
breadcrumb: 指南 > 应用服务 > Map Kit（地图服务） > 在地图上绘制 > 瓦片图层
category: harmonyos-guides
scraped_at: 2026-04-28T07:49:52+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:3af9687adaa9ef138eb39bd9af867c72cf01bbb4b1b90b35191527ccf8c6f359
---

## 场景介绍

新增瓦片图层（TileOverlay）, 该图层支持添加自有瓦片数据，包括在线下载和本地加载两种方式。该图层可随地图的平移、缩放、旋转等操作做相应的变换，它仅位于底图之上（即瓦片图层将会遮挡底图，不遮挡其他图层），瓦片图层的添加顺序不会影响其他图层的叠加关系。

通过瓦片图层可对基础底层地图添加额外的特性，如：某个商场的室内信息、某个景区的详情等等。适用于开发者拥有某一区域的地图，并希望使用此区域地图覆盖相应位置的华为地图。

5.0.3(15)开始，支持瓦片图层功能。

6.0.0(20)开始，支持瓦片数据缓存功能。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/xQHD1_abRlObOD6uo7-XZA/zh-cn_image_0000002552959044.jpg?HW-CC-KV=V1&HW-CC-Date=20260427T234950Z&HW-CC-Expire=86400&HW-CC-Sign=034643F3C8F01397154594A21E8AF4D108010A6AF08B9FA4EDA9705F058375E7 "点击放大")

## 接口说明

瓦片图层功能主要由[TileOverlayParams](../harmonyos-references/map-common.md#tileoverlayparams)、[TileOverlayOptions](../harmonyos-references/map-common.md#tileoverlayoptions)、[addTileOverlay](../harmonyos-references/map-map-mapcomponentcontroller.md#addtileoverlay)和[TileOverlay](../harmonyos-references/map-map-tileoverlay.md)提供，更多接口及使用方法请参见[接口文档](../harmonyos-references/map-map-tileoverlay.md)。

| 接口名 | 描述 |
| --- | --- |
| [TileOverlayParams](../harmonyos-references/map-common.md#tileoverlayparams) | 瓦片图层参数。 |
| [TileOverlayOptions](../harmonyos-references/map-common.md#tileoverlayoptions) | 瓦片图层参数。 |
| [addTileOverlay](../harmonyos-references/map-map-mapcomponentcontroller.md#addtileoverlay)(params: [mapCommon.TileOverlayParams](../harmonyos-references/map-common.md#tileoverlayparams) | [mapCommon.TileOverlayOptions](../harmonyos-references/map-common.md#tileoverlayoptions)): [TileOverlay](../harmonyos-references/map-map-tileoverlay.md) | 为地图增加瓦片图层。 |
| [TileOverlay](../harmonyos-references/map-map-tileoverlay.md) | 瓦片图层，支持更新和查询相关属性。 |

## 开发步骤

瓦片图层的绘制方式提供两种方式：在线下载和本地加载。

### 在线下载

1. 导入相关模块。

   ```
   1. import { map, mapCommon, MapComponent } from '@kit.MapKit';
   2. import { AsyncCallback } from '@kit.BasicServicesKit';
   ```
2. 增加瓦片图层，在线下载方式需要设置在线瓦片的URL地址。

   ```
   1. @Entry
   2. @Component
   3. struct TileOverlayDemo {
   4. private mapOptions?: mapCommon.MapOptions;
   5. private mapController?: map.MapComponentController;
   6. private callback?: AsyncCallback<map.MapComponentController>;
   7. private tileOverlay?: map.TileOverlay;

   9. aboutToAppear(): void {
   10. this.mapOptions = {
   11. position: {
   12. target: {
   13. latitude: 31.98,
   14. longitude: 118.7
   15. },
   16. zoom: 7
   17. }
   18. }

   20. this.callback = async (err, mapController) => {
   21. if (!err) {
   22. this.mapController = mapController;
   23. let params: mapCommon.TileOverlayOptions = {
   24. // 设置地图瓦片图层的地址，必须是以http或者https开头的URL且包含占位符{x}、{y}和{z}
   25. // 需要替换为开发者自己的在线地址
   26. tileUrl: "https://xxx/xxx?x={x}&y={y}&z={z}",
   27. // 透明度
   28. transparency: 0.5,
   29. // 开启瓦片图层淡入
   30. fadeIn: true
   31. };
   32. try {
   33. this.tileOverlay = this.mapController?.addTileOverlay(params);
   34. } catch (e) {
   35. console.error(`code:${e.code}, message:${e.message}`);
   36. }
   37. } else {
   38. console.error(`Failed to initialize the map, code is：${err.code}, message is ${err.message}`);
   39. }
   40. }
   41. }

   43. build() {
   44. Stack() {
   45. Column() {
   46. MapComponent({ mapOptions: this.mapOptions, mapCallback: this.callback })
   47. .width('100%')
   48. .height('100%')
   49. }.width('100%')
   50. }.height('100%')
   51. }
   52. }
   ```

### 本地加载

1. 导入相关模块。

   ```
   1. import { mapCommon, map, MapComponent } from '@kit.MapKit';
   2. import { AsyncCallback } from '@kit.BasicServicesKit';
   ```
2. 增加本地瓦片图层。

   ```
   1. @Entry
   2. @Component
   3. struct TileOverlayDemo {
   4. private mapOption?: mapCommon.MapOptions;
   5. private mapController?: map.MapComponentController;
   6. private callback?: AsyncCallback<map.MapComponentController>;
   7. private tileOverlay?: map.TileOverlay;

   9. aboutToAppear(): void {
   10. this.mapOption = {
   11. position: {
   12. target: {
   13. latitude: 31.98,
   14. longitude: 118.7
   15. },
   16. zoom: 7
   17. },
   18. scaleControlsEnabled: true
   19. }

   21. this.callback = async (err, mapController) => {
   22. if (!err) {
   23. this.mapController = mapController;
   24. let tileOverlayOption: mapCommon.TileOverlayOptions = {
   25. // 根据瓦片坐标获取瓦片，本地获取瓦片方式需开发者自行实现tileProvider方法
   26. tileProvider: this.tileProviderMethod,
   27. // 淡入淡出效果 true: 开启, false: 关闭
   28. fadeIn: true,
   29. // 透明度, 取值范围 0-1
   30. transparency: 0.5,
   31. // 可见性, true: 可见 false: 不可见
   32. visible: true
   33. }
   34. if (this.mapController !== undefined) {
   35. try {
   36. this.tileOverlay = this.mapController.addTileOverlay(tileOverlayOption);
   37. } catch (e) {
   38. console.error(`code:${e.code}, message:${e.message}`);
   39. }
   40. }
   41. } else {
   42. console.error(`Failed to initialize the map, code is：${err.code}, message is ${err.message}`);
   43. }
   44. }
   45. }

   47. // 需要开发者自实现tileProviderMethod方法，负责加载本地项目中的瓦片图资源
   48. private tileProviderMethod(x: number, y: number, z: number): Promise<ArrayBuffer> {
   49. return new Promise((resolve, reject) => {});
   50. }

   52. build() {
   53. Stack() {
   54. Column() {
   55. MapComponent({ mapOptions: this.mapOption, mapCallback: this.callback })
   56. .width('100%')
   57. .height('100%');
   58. }.width('100%')
   59. }.height('100%')
   60. }
   61. }
   ```

### 支持瓦片数据缓存

1. 导入相关模块。

   ```
   1. import { mapCommon, map, MapComponent } from '@kit.MapKit';
   2. import { AsyncCallback } from '@kit.BasicServicesKit';
   ```
2. 增加瓦片图层。

   ```
   1. @Entry
   2. @Component
   3. struct TileOverlayDemo {
   4. private mapOption?: mapCommon.MapOptions;
   5. private mapController?: map.MapComponentController;
   6. private callback?: AsyncCallback<map.MapComponentController>;
   7. private tileOverlay?: map.TileOverlay;

   9. aboutToAppear(): void {
   10. this.mapOption = {
   11. position: {
   12. target: {
   13. latitude: 48.87278,
   14. longitude: 2.33016
   15. },
   16. zoom: 4
   17. },
   18. scaleControlsEnabled: true
   19. }

   21. this.callback = async (err, mapController) => {
   22. if (!err) {
   23. this.mapController = mapController;
   24. let options: mapCommon.TileOverlayOptions = {
   25. // 设置地图瓦片图层的地址，必须是以http或者https开头的URL且包含占位符{x}、{y}和{z}
   26. // 需要替换为开发者自己的在线地址
   27. tileUrl: "https://xxx/xxx?x={x}&y={y}&z={z}",
   28. // 是否开启磁盘缓存 true: 开启, false: 关闭
   29. diskCacheEnabled: true,
   30. // 磁盘缓存大小 默认大小 20480KB, 单位KB
   31. diskCacheSize: 20480,
   32. // 存放磁盘缓存的沙箱路径
   33. diskCachePath: this.getUIContext().getHostContext()?.databaseDir
   34. };
   35. if (this.mapController !== undefined) {
   36. try {
   37. this.tileOverlay = this.mapController.addTileOverlay(options);
   38. } catch (e) {
   39. console.error(`code:${e.code}, message:${e.message}`);
   40. }
   41. }
   42. } else {
   43. console.error(`Failed to initialize the map, code is：${err.code}, message is ${err.message}`);
   44. }
   45. }
   46. }

   48. aboutToDisappear(): void {
   49. if (this.tileOverlay) {
   50. this.tileOverlay.remove();
   51. // 清除内存缓存
   52. this.tileOverlay.clearTileCache();
   53. // 清除磁盘和内存缓存
   54. this.tileOverlay.clearDiskCache();
   55. }
   56. }

   58. build() {
   59. Stack() {
   60. Column() {
   61. MapComponent({ mapOptions: this.mapOption, mapCallback: this.callback })
   62. .width('100%')
   63. .height('100%');
   64. }.width('100%')
   65. }.height('100%')
   66. }
   67. }
   ```
