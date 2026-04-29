---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/map-polygon
title: 多边形
breadcrumb: 指南 > 应用服务 > Map Kit（地图服务） > 在地图上绘制 > 多边形
category: harmonyos-guides
scraped_at: 2026-04-29T13:39:10+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:6ef04a802a2dc500aa76b48085d882877c6387b206bc5ba6bafebf1463610b56
---

## 场景介绍

本章节将向您介绍如何在地图上绘制多边形。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/MUjwkhcuQn2pYbgPviY6BQ/zh-cn_image_0000002558605882.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T053907Z&HW-CC-Expire=86400&HW-CC-Sign=C117712054F8A064097BA0B479DB9E24E7456185B775A2DD801BF5ED3E5628A3 "点击放大")

## 接口说明

添加多边形功能主要由[MapPolygonOptions](../harmonyos-references/map-common.md#mappolygonoptions)、[addPolygon](../harmonyos-references/map-map-mapcomponentcontroller.md#addpolygon)和[MapPolygon](../harmonyos-references/map-map-mappolygon.md)提供，更多接口及使用方法请参见[接口文档](../harmonyos-references/map-map-mappolygon.md)。

| 接口名 | 描述 |
| --- | --- |
| [MapPolygonOptions](../harmonyos-references/map-common.md#mappolygonoptions) | 多边形参数。 |
| [addPolygon](../harmonyos-references/map-map-mapcomponentcontroller.md#addpolygon)(options: [mapCommon.MapPolygonOptions](../harmonyos-references/map-common.md#mappolygonoptions)): Promise<[MapPolygon](../harmonyos-references/map-map-mappolygon.md)> | 在地图上添加一个多边形。 |
| [MapPolygon](../harmonyos-references/map-map-mappolygon.md) | 多边形，支持更新和查询相关属性。 |

## 开发步骤

1. 导入相关模块。

   ```
   1. import { MapComponent, mapCommon, map } from '@kit.MapKit';
   2. import { AsyncCallback } from '@kit.BasicServicesKit';
   ```
2. 添加多边形，在callback方法中创建初始化参数并新建polygon。

   ```
   1. @Entry
   2. @Component
   3. struct MapPolygonDemo {
   4. private mapOptions?: mapCommon.MapOptions;
   5. private mapController?: map.MapComponentController;
   6. private callback?: AsyncCallback<map.MapComponentController>;
   7. private mapPolygon?: map.MapPolygon;

   9. aboutToAppear(): void {
   10. // 地图初始化参数
   11. this.mapOptions = {
   12. position: {
   13. target: {
   14. latitude: 31.98,
   15. longitude: 118.78
   16. },
   17. zoom: 14
   18. }
   19. };
   20. this.callback = async (err, mapController) => {
   21. if (!err) {
   22. this.mapController = mapController;
   23. // 多边形初始化参数
   24. let polygonOptions: mapCommon.MapPolygonOptions = {
   25. points: [
   26. { longitude: 118.78, latitude: 31.975 },
   27. { longitude: 118.78, latitude: 31.985 },
   28. { longitude: 118.79, latitude: 31.985 },
   29. { longitude: 118.79, latitude: 31.975 }
   30. ],
   31. clickable: true,
   32. fillColor: 0xff00DE00,
   33. geodesic: false,
   34. strokeColor: 0xff000000,
   35. jointType: mapCommon.JointType.DEFAULT,
   36. strokeWidth: 10,
   37. visible: true,
   38. zIndex: 10
   39. }
   40. // 创建多边形
   41. try {
   42. this.mapPolygon = await this.mapController.addPolygon(polygonOptions);
   43. } catch (e) {
   44. console.error(`Failed to create the mapPolygon, code is：${e.code}, message is ${e.message}`);
   45. }
   46. } else {
   47. console.error(`Failed to initialize the map, code is：${err.code}, message is ${err.message}`);
   48. }
   49. };
   50. }

   52. build() {
   53. Stack() {
   54. Column() {
   55. MapComponent({ mapOptions: this.mapOptions, mapCallback: this.callback });
   56. }.width('100%')
   57. }.height('100%')
   58. }
   59. }
   ```

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/L43hp1GdSsqrGReoW0TKAw/zh-cn_image_0000002589325409.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T053907Z&HW-CC-Expire=86400&HW-CC-Sign=40E8F9028E2B181028FF547CE79106080659F7FC056505372EC9482105D27AEC "点击放大")
