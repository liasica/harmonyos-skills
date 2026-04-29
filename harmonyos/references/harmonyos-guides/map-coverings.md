---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/map-coverings
title: 覆盖物
breadcrumb: 指南 > 应用服务 > Map Kit（地图服务） > 在地图上绘制 > 覆盖物
category: harmonyos-guides
scraped_at: 2026-04-29T13:39:11+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:4c505b6bcbd6217e39f77519a4047e009ec5185dbf6e90c12c296789386008e8
---

## 场景介绍

地图覆盖物是固定在地图上的图片，本章节将向您介绍如何为地图增加覆盖物。

覆盖物，是一种位于底图和底图标注层之间的特殊Overlay，该图层不会遮挡地图标注信息。通过[ImageOverlayParams](../harmonyos-references/map-common.md#imageoverlayparams)类来设置，开发者可以通过[ImageOverlayParams](../harmonyos-references/map-common.md#imageoverlayparams)类设置一张图片，该图片可随地图的平移、缩放、旋转等操作做相应的变换。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/LSqmlX6tS0qhVQMt0--f8g/zh-cn_image_0000002558765544.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T053910Z&HW-CC-Expire=86400&HW-CC-Sign=94F0B2BB85BF26E16A8657540B0AFDE4AB261606A9C35873721EF94E1CBEAC18 "点击放大")

## 接口说明

增加覆盖物功能主要由[ImageOverlayParams](../harmonyos-references/map-common.md#imageoverlayparams)、[addImageOverlay](../harmonyos-references/map-map-mapcomponentcontroller.md#addimageoverlay)、[ImageOverlay](../harmonyos-references/map-map-imageoverlay.md)提供，更多接口及使用方法请参见[接口文档](../harmonyos-references/map-map-imageoverlay.md)。

| 接口名 | 描述 |
| --- | --- |
| [ImageOverlayParams](../harmonyos-references/map-common.md#imageoverlayparams) | 覆盖物参数。 |
| [addImageOverlay](../harmonyos-references/map-map-mapcomponentcontroller.md#addimageoverlay)(params: [mapCommon.ImageOverlayParams](../harmonyos-references/map-common.md#imageoverlayparams)): Promise<[ImageOverlay](../harmonyos-references/map-map-imageoverlay.md)> | 为地图增加覆盖物。 |
| [ImageOverlay](../harmonyos-references/map-map-imageoverlay.md) | 覆盖物，支持更新和查询相关属性。 |

## 开发步骤

1. 导入相关模块。

   ```
   1. import { map, mapCommon, MapComponent } from '@kit.MapKit';
   2. import { AsyncCallback } from '@kit.BasicServicesKit';
   ```
2. 增加覆盖物。

   ```
   1. @Entry
   2. @Component
   3. struct ImageOverlayDemo {
   4. private mapOptions?: mapCommon.MapOptions;
   5. private mapController?: map.MapComponentController;
   6. private callback?: AsyncCallback<map.MapComponentController>;
   7. private mapEventManager?: map.MapEventManager;

   9. aboutToAppear(): void {
   10. this.mapOptions = {
   11. position: {
   12. target: {
   13. latitude: 32.2,
   14. longitude: 118.2
   15. },
   16. zoom: 10
   17. }
   18. }

   20. this.callback = async (err, mapController) => {
   21. if (!err) {
   22. this.mapController = mapController;
   23. this.mapEventManager = this.mapController.getEventManager();
   24. let imageOverlayParams: mapCommon.ImageOverlayParams = {
   25. // 覆盖物范围
   26. bounds: {
   27. southwest: {
   28. latitude: 32,
   29. longitude: 118
   30. },
   31. northeast: {
   32. latitude: 32.4,
   33. longitude: 118.4
   34. }
   35. },
   36. // 覆盖物图片，图标需存放在resources/rawfile目录下
   37. image: 'icon/icon.png',
   38. transparency: 0.3,
   39. zIndex: 101,
   40. anchorU: 0.5,
   41. anchorV: 0.5,
   42. clickable: true,
   43. visible: true,
   44. bearing: 0
   45. };
   46. // 添加覆盖物
   47. try {
   48. let imageOverlay = await this.mapController?.addImageOverlay(imageOverlayParams);
   49. } catch (e) {
   50. console.error(`Failed to create the imageOverlay, code is：${e.code}, message is ${e.message}`);
   51. }
   52. } else {
   53. console.error(`Failed to initialize the map, code is：${err.code}, message is ${err.message}`);
   54. }
   55. }
   56. }
   57. build() {
   58. Stack() {
   59. Column() {
   60. MapComponent({
   61. mapOptions: this.mapOptions,
   62. mapCallback: this.callback,
   63. })
   64. .width('100%')
   65. .height('100%');
   66. }.width('100%')
   67. }.height('100%')
   68. }
   69. }
   ```
3. 设置覆盖物点击监听事件。

   ```
   1. let imageOverlayCallback: Callback<map.ImageOverlay> = (imageOverlay: map.ImageOverlay) => {
   2. console.info("imageOverlay callback");
   3. }
   4. // 打开覆盖物的点击监听
   5. this.mapEventManager.on("imageOverlayClick", imageOverlayCallback);
   6. // 关闭覆盖物的点击监听
   7. this.mapEventManager.off("imageOverlayClick", imageOverlayCallback);
   ```
