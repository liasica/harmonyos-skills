---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/map-arc
title: 弧线
breadcrumb: 指南 > 应用服务 > Map Kit（地图服务） > 在地图上绘制 > 弧线
category: harmonyos-guides
scraped_at: 2026-04-29T13:39:10+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:8147dd759ba0043776753fb429df9b50ecb07ed5af0f3d8ed2169134c4abb120
---

## 场景介绍

本章节将向您介绍如何在地图上绘制弧线，通过[MapArcParams](../harmonyos-references/map-common.md#maparcparams)类设置弧线的位置、宽度、颜色等参数。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/Wl09QgbKTWeHostP573a1g/zh-cn_image_0000002589245345.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T053903Z&HW-CC-Expire=86400&HW-CC-Sign=38D73BC7BE228F552226703D94AD1B705CF0E6C8706D6E0F35288D1D7C6BBA99 "点击放大")

## 接口说明

添加弧线功能主要由[MapArcParams](../harmonyos-references/map-common.md#maparcparams)、[addArc](../harmonyos-references/map-map-mapcomponentcontroller.md#addarc)和[MapArc](../harmonyos-references/map-map-maparc.md)提供，更多接口及使用方法请参见[接口文档](../harmonyos-references/map-map-maparc.md)。

| 接口名 | 描述 |
| --- | --- |
| [MapArcParams](../harmonyos-references/map-common.md#maparcparams) | 弧线参数。 |
| [addArc](../harmonyos-references/map-map-mapcomponentcontroller.md#addarc)(params: [mapCommon.MapArcParams](../harmonyos-references/map-common.md#maparcparams)): [MapArc](../harmonyos-references/map-map-maparc.md) | 添加一条弧线。 |
| [MapArc](../harmonyos-references/map-map-maparc.md) | 弧线，支持更新和查询相关属性。 |

## 开发步骤

### 添加弧线

1. 导入相关模块。

   ```
   1. import { map, mapCommon, MapComponent } from '@kit.MapKit';
   2. import { AsyncCallback } from '@kit.BasicServicesKit';
   ```
2. 添加弧线，在callback方法中创建初始化参数并新建MapArc。

   ```
   1. @Entry
   2. @Component
   3. struct MapArcDemo {
   4. private TAG = "OHMapSDK_MapArcDemo";
   5. private mapOptions?: mapCommon.MapOptions;
   6. private mapController?: map.MapComponentController;
   7. private callback?: AsyncCallback<map.MapComponentController>;
   8. private mapArc?: map.MapArc;

   10. aboutToAppear(): void {
   11. this.mapOptions = {
   12. position: {
   13. target: {
   14. latitude: 34.757975,
   15. longitude: 113.665412
   16. },
   17. zoom: 6
   18. }
   19. }

   21. this.callback = async (err, mapController) => {
   22. if (!err) {
   23. this.mapController = mapController;
   24. if (!this.mapController) {
   25. console.error(this.TAG, "mapController is null");
   26. return;
   27. }
   28. // 设置弧线参数
   29. let mapArcParams: mapCommon.MapArcParams = {
   30. // 弧线起点坐标
   31. startPoint: {
   32. latitude: 39.913138,
   33. longitude: 116.415112
   34. },
   35. // 弧线终点坐标
   36. endPoint: {
   37. latitude: 28.239473,
   38. longitude: 112.954094
   39. },
   40. // 弧线中心点坐标
   41. centerPoint: {
   42. latitude: 33.86970399048567,
   43. longitude: 112.08633528544145
   44. },
   45. width: 10,
   46. color: 0xffff0000,
   47. visible: true,
   48. zIndex: 100
   49. };
   50. // 添加弧线
   51. try {
   52. this.mapArc = await this.mapController.addArc(mapArcParams);
   53. } catch (e) {
   54. console.error(`Failed to create the mapArc, code is：${e.code}, message is ${e.message}`);
   55. }
   56. } else {
   57. console.error(`Failed to initialize the map, code is：${err.code}, message is ${err.message}`);
   58. }
   59. }
   60. }

   62. build() {
   63. Stack() {
   64. Column() {
   65. MapComponent({
   66. mapOptions: this.mapOptions,
   67. mapCallback: this.callback
   68. })
   69. .width('100%')
   70. .height('100%');
   71. }.width('100%')
   72. }.height('100%')
   73. }
   74. }
   ```

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/89c11aTORiKFt_1HbtSR3w/zh-cn_image_0000002558765538.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T053903Z&HW-CC-Expire=86400&HW-CC-Sign=B43484BC61FFCC5268D37A7181BEFDAC814E0997E6ACC56123F1F406F6FC0517 "点击放大")
