---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/map-circle
title: 圆形
breadcrumb: 指南 > 应用服务 > Map Kit（地图服务） > 在地图上绘制 > 圆形
category: harmonyos-guides
scraped_at: 2026-04-28T07:49:50+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:f5f79d7b1f6f59f500cb24a00e528a380e54c9829928c7b41a2ac75edcf410a3
---

## 场景介绍

本章节将向您介绍如何在地图上绘制圆形。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/_hfPFOMVQM2lIAoN0hh0yA/zh-cn_image_0000002583439083.jpg?HW-CC-KV=V1&HW-CC-Date=20260427T234949Z&HW-CC-Expire=86400&HW-CC-Sign=F3DD5E2F4C80455B253DD5F87B15EE6F2B26D3E344AC765DA3338CA764E3C9E3 "点击放大")

## 接口说明

添加圆形功能主要由[MapCircleOptions](../harmonyos-references/map-common.md#mapcircleoptions)、[addCircle](../harmonyos-references/map-map-mapcomponentcontroller.md#addcircle)和[MapCircle](../harmonyos-references/map-map-mapcircle.md)提供，更多接口及使用方法请参见[接口文档](../harmonyos-references/map-map-mapcircle.md)。

| 接口名 | 描述 |
| --- | --- |
| [MapCircleOptions](../harmonyos-references/map-common.md#mapcircleoptions) | 圆形参数。 |
| [addCircle](../harmonyos-references/map-map-mapcomponentcontroller.md#addcircle)(options: [mapCommon.MapCircleOptions](../harmonyos-references/map-common.md#mapcircleoptions)): Promise<[MapCircle](../harmonyos-references/map-map-mapcircle.md)> | 在地图上添加一个圆，指定圆心经纬度和圆的半径，用于表示某个位置的周边范围。 |
| [MapCircle](../harmonyos-references/map-map-mapcircle.md) | 圆形，支持更新和查询相关属性。 |

## 开发步骤

1. 导入相关模块。

   ```
   1. import { MapComponent, mapCommon, map } from '@kit.MapKit';
   2. import { AsyncCallback } from '@kit.BasicServicesKit';
   ```
2. 添加圆，在callback方法中创建初始化参数并新建Circle。

   ```
   1. @Entry
   2. @Component
   3. struct MapCircleDemo {
   4. private mapOptions?: mapCommon.MapOptions;
   5. private mapController?: map.MapComponentController;
   6. private callback?: AsyncCallback<map.MapComponentController>;
   7. private mapCircle?: map.MapCircle;

   9. aboutToAppear(): void {
   10. // 地图初始化参数
   11. this.mapOptions = {
   12. position: {
   13. target: {
   14. latitude: 39.918,
   15. longitude: 116.397
   16. },
   17. zoom: 14
   18. }
   19. };

   21. this.callback = async (err, mapController) => {
   22. if (!err) {
   23. this.mapController = mapController;
   24. // Circle初始化参数
   25. let mapCircleOptions: mapCommon.MapCircleOptions = {
   26. center: {
   27. latitude: 39.918,
   28. longitude: 116.397
   29. },
   30. radius: 500,
   31. clickable: true,
   32. fillColor: 0xFFFFC100,
   33. strokeColor: 0xFFFF0000,
   34. strokeWidth: 10,
   35. visible: true,
   36. zIndex: 15
   37. }
   38. // 创建Circle
   39. try {
   40. this.mapCircle = await this.mapController.addCircle(mapCircleOptions);
   41. } catch (e) {
   42. console.error(`Failed to create the mapCircle, code is：${e.code}, message is ${e.message}`);
   43. }
   44. } else {
   45. console.error(`Failed to initialize the map, code is：${err.code}, message is ${err.message}`);
   46. }
   47. };
   48. }

   50. build() {
   51. Stack() {
   52. Column() {
   53. MapComponent({ mapOptions: this.mapOptions, mapCallback: this.callback });
   54. }.width('100%')
   55. }.height('100%')
   56. }
   57. }
   ```

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/Tl0eFuthRiaRUaiXgU5nLA/zh-cn_image_0000002552959038.jpg?HW-CC-KV=V1&HW-CC-Date=20260427T234949Z&HW-CC-Expire=86400&HW-CC-Sign=21BEAFFE2D6B7FEB22B5FB0C905385602741BF5442E0812E6DAEEA082DBC672B "点击放大")
