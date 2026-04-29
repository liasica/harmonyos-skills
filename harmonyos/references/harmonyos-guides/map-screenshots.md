---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/map-screenshots
title: 地图截图
breadcrumb: 指南 > 应用服务 > Map Kit（地图服务） > 地图交互 > 地图截图
category: harmonyos-guides
scraped_at: 2026-04-29T13:39:07+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:5fa09f1c7c0c9f86dc1c4ee25649534edd207be617b6bee6fc3675684901628c
---

本章节将向您介绍如何实现地图截图功能。

地图截图指对当前屏幕显示区域进行截屏，支持对地图、覆盖物、Logo进行屏幕截图。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/v_GgJ7P5QYqyOSNoiXVI7A/zh-cn_image_0000002558605872.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T053813Z&HW-CC-Expire=86400&HW-CC-Sign=EE0EE7C0D6985CB4749DB9D4CB5F91FB05BA5854D89CF75AA4A048276902C9A8 "点击放大")

## 接口说明

以下是地图截图相关接口，以下功能主要由[snapshot](../harmonyos-references/map-map-mapcomponentcontroller.md#snapshot)提供，更多接口及使用方法请参见[接口文档](../harmonyos-references/map-map-mapcomponentcontroller.md#snapshot)。

| 接口名 | 描述 |
| --- | --- |
| [snapshot](../harmonyos-references/map-map-mapcomponentcontroller.md#snapshot)(): Promise<[image.PixelMap](../harmonyos-references/arkts-apis-image-pixelmap.md)> | 地图截图。 |

## 开发步骤

1. 导入相关模块。

   ```
   1. import { MapComponent, mapCommon, map } from '@kit.MapKit';
   2. import { AsyncCallback } from '@kit.BasicServicesKit';
   3. import { image } from '@kit.ImageKit';
   ```
2. 调用[snapshot](../harmonyos-references/map-map-mapcomponentcontroller.md#snapshot)方法对当前屏幕进行截图。

   ```
   1. @Entry
   2. @Component
   3. struct HuaweiMapDemo {
   4. private mapOptions?: mapCommon.MapOptions;
   5. private callback?: AsyncCallback<map.MapComponentController>;
   6. private mapController?: map.MapComponentController;
   7. @State image?: image.PixelMap = undefined;

   9. aboutToAppear(): void {
   10. // 地图初始化参数，设置地图中心点坐标及层级
   11. this.mapOptions = {
   12. position: {
   13. target: {
   14. latitude: 39.9,
   15. longitude: 116.4
   16. },
   17. zoom: 10
   18. }
   19. };

   21. // 地图初始化的回调
   22. this.callback = async (err, mapController) => {
   23. if (!err) {
   24. // 获取地图的控制器类，用来操作地图
   25. this.mapController = mapController;
   26. } else {
   27. console.error(`Failed to initialize the map, code is：${err.code}, message is ${err.message}`);
   28. }
   29. };
   30. }

   32. build() {
   33. Stack() {
   34. Column() {
   35. MapComponent({ mapOptions: this.mapOptions, mapCallback: this.callback })
   36. .width('100%')
   37. .height('50%');

   39. Scroll(new Scroller()) {
   40. Column() {
   41. Image(this.image)
   42. .objectFit(ImageFit.Auto)
   43. .border({ width: 1, color: Color.Red }).width("100%")
   44. Button("获取截图")
   45. .margin({ left: 10 })
   46. .fontSize(12)
   47. .onClick(async () => {
   48. if (this.mapController) {
   49. let pixelMap = await this.mapController.snapshot();
   50. this.image = pixelMap;
   51. }
   52. });
   53. }
   54. }.width('70%').height("50%")
   55. }.width('100%')
   56. }.height('100%')
   57. }
   58. }
   ```
