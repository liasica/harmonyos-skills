---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/map-mvt-overlay
title: 矢量图层
breadcrumb: 指南 > 应用服务 > Map Kit（地图服务） > 在地图上绘制 > 矢量图层
category: harmonyos-guides
scraped_at: 2026-04-28T07:49:52+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:5ca420e05cf3216d25ccc27d4ea4e9b1b5e07d92a437347bc141ecba87eddd7d
---

## 场景介绍

新增矢量图层，用于在基础地图之上叠加矢量数据。通过矢量图层可对基础底层地图添加额外的特性，如：实时展示全球或区域的天气状况等。

6.0.0(20)开始，支持矢量图层功能。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/luYk_BOnT4y-99iUmS95jA/zh-cn_image_0000002552799396.gif?HW-CC-KV=V1&HW-CC-Date=20260427T234950Z&HW-CC-Expire=86400&HW-CC-Sign=4C79CBE9A94010F90D47D1E38F71D5B16114356BAE508BFFD33F6AB832676DD8 "点击放大")

## 接口说明

矢量图层功能主要由[MvtOverlayParams](../harmonyos-references/map-common.md#mvtoverlayparams)、[addMvtOverlay](../harmonyos-references/map-map-mapcomponentcontroller.md#addmvtoverlay)和[MvtOverlay](../harmonyos-references/map-map-mvtoverlay.md)提供，更多接口及使用方法请参见[接口文档](../harmonyos-references/map-map-mvtoverlay.md)。

| 接口名 | 描述 |
| --- | --- |
| [MvtOverlayParams](../harmonyos-references/map-common.md#mvtoverlayparams) | 矢量图层的参数。 |
| [addMvtOverlay](../harmonyos-references/map-map-mapcomponentcontroller.md#addmvtoverlay)(params: [mapCommon.MvtOverlayParams](../harmonyos-references/map-common.md#mvtoverlayparams)): [MvtOverlay](../harmonyos-references/map-map-mvtoverlay.md) | 添加矢量图层。 |
| [MvtOverlay](../harmonyos-references/map-map-mvtoverlay.md) | 矢量图层管理对象，支持添加和删除图层。 |

## 开发步骤

矢量图层的绘制方式提供两种方式：在线下载和本地加载。

### 在线下载

1. 使用在线下载绘制矢量图层之前，请在应用的module.json5文件中配置访问网络的权限。

   ```
   1. {
   2. "module" : {
   3. // ...
   4. "requestPermissions":[
   5. {
   6. // 允许应用使用Internet网络。
   7. "name": "ohos.permission.INTERNET",
   8. "usedScene": {
   9. "when": "always"
   10. }
   11. }
   12. ]
   13. }
   14. }
   ```
2. 导入相关模块。

   ```
   1. import { mapCommon, map, MapComponent } from '@kit.MapKit';
   2. import { AsyncCallback } from '@kit.BasicServicesKit';
   ```
3. 绘制矢量图层。

   矢量图层支持的数据源类型为通用矢量瓦片格式（PBF/MVT）。[MvtOverlayParams](../harmonyos-references/map-common.md#mvtoverlayparams)类中的layers参数，其中sourceLayer、fillColor/fillOpacity默认值从矢量数据里获取，也可自己设置。

   ```
   1. @Entry
   2. @Component
   3. struct MvtOverlayDemo {
   4. private TAG = 'OHMapSDK_MvtOverlayDemo';
   5. private mapOption?: mapCommon.MapOptions;
   6. private mapController?: map.MapComponentController;
   7. private callback?: AsyncCallback<map.MapComponentController>;
   8. aboutToAppear(): void {
   9. this.mapOption = {
   10. position: {
   11. target: {
   12. latitude: 35.899780,
   13. longitude: 107.766172
   14. },
   15. zoom: 6
   16. },
   17. scaleControlsEnabled: true
   18. }
   19. this.callback = async (err, mapController) => {
   20. if (!err) {
   21. this.mapController = mapController;
   22. let params: mapCommon.MvtOverlayParams = {
   23. source: {
   24. // 设置矢量图层的地址,必须是以http或者https开头的URL且包含占位符{x}、{y}和{z}
   25. tileUrl: 'http://xxx/tiles/{z}/{x}/{y}.pbf',
   26. minZoom: 2,
   27. maxZoom: 15
   28. },
   29. layers: [{
   30. id: 'layer-map',
   31. type: mapCommon.MvtLayerType.FILL,
   32. // 对应矢量图层数据中图层的name字段
   33. sourceLayer: 'XX',
   34. paint: {
   35. fillColor: {
   36. operator: mapCommon.Operator.GET,
   37. args: 'fill'
   38. },
   39. fillOpacity: {
   40. operator: mapCommon.Operator.GET,
   41. args: 'fill-opacity'
   42. }
   43. }
   44. }]
   45. }
   46. try {
   47. this.mapController?.addMvtOverlay(params);
   48. } catch (e) {
   49. console.error(this.TAG, `code:${e.code}, message:${e.message}`);
   50. }
   51. } else {
   52. console.error(`Failed to initialize the map, code is：${err.code}, message is ${err.message}`);
   53. }
   54. }
   55. }
   56. build() {
   57. Stack() {
   58. Column() {
   59. MapComponent({ mapOptions: this.mapOption, mapCallback: this.callback })
   60. .width('100%')
   61. .height('100%')
   62. }.width('100%')
   63. }.height('100%')
   64. }
   65. }
   ```

### 本地加载

1. 导入相关模块。

   ```
   1. import { mapCommon, map, MapComponent } from '@kit.MapKit';
   2. import { AsyncCallback } from '@kit.BasicServicesKit';
   ```
2. 增加本地矢量图层。

   ```
   1. @Entry
   2. @Component
   3. struct MvtOverlayDemo {
   4. private TAG = 'OHMapSDK_MvtOverlayDemo';
   5. private mapOption?: mapCommon.MapOptions;
   6. private mapController?: map.MapComponentController;
   7. private callback?: AsyncCallback<map.MapComponentController>;
   8. aboutToAppear(): void {
   9. this.mapOption = {
   10. position: {
   11. target: {
   12. latitude: 35.899780,
   13. longitude: 107.766172
   14. },
   15. zoom: 6
   16. },
   17. scaleControlsEnabled: true
   18. }
   19. this.callback = async (err, mapController) => {
   20. if (!err) {
   21. this.mapController = mapController;
   22. let params: mapCommon.MvtOverlayParams = {
   23. source: {
   24. // 根据矢量坐标获取矢量图层，本地获取矢量图层方式需开发者自行实现tileProvider方法
   25. tileProvider: this.tileProviderMethod,
   26. minZoom: 2,
   27. maxZoom: 15
   28. },
   29. layers: [{
   30. id: 'layer-map',
   31. type: mapCommon.MvtLayerType.FILL,
   32. // 对应矢量图层数据中图层的name字段
   33. sourceLayer: 'XX',
   34. paint: {
   35. fillColor: {
   36. operator: mapCommon.Operator.GET,
   37. args: 'fill'
   38. },
   39. fillOpacity: {
   40. operator: mapCommon.Operator.GET,
   41. args: 'fill-opacity'
   42. }
   43. }
   44. }]
   45. }
   46. try {
   47. this.mapController?.addMvtOverlay(params);
   48. } catch (e) {
   49. console.error(this.TAG, `code:${e.code}, message:${e.message}`);
   50. }
   51. } else {
   52. console.error(`Failed to initialize the map, code is：${err.code}, message is ${err.message}`);
   53. }
   54. }
   55. }

   57. // 需要开发者自行实现tileProviderMethod方法，负责加载本地项目中的矢量图层资源
   58. private tileProviderMethod(x: number, y: number, z: number): Promise<ArrayBuffer> {
   59. return new Promise((resolve, reject) => {});
   60. }

   62. build() {
   63. Stack() {
   64. Column() {
   65. MapComponent({ mapOptions: this.mapOption, mapCallback: this.callback })
   66. .width('100%')
   67. .height('100%')
   68. }.width('100%')
   69. }.height('100%')
   70. }
   71. }
   ```
