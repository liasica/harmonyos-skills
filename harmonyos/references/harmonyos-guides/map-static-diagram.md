---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/map-static-diagram
title: 静态图
breadcrumb: 指南 > 应用服务 > Map Kit（地图服务） > 静态图
category: harmonyos-guides
scraped_at: 2026-04-28T07:49:54+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:a7ab580547c429933ff01f53e3b58110c375e58482ad7729c295022fe48739c0
---

## 场景介绍

本章节将向您介绍如何使用静态图功能。静态图功能会返回一张地图图片，您可以将地图以图片形式嵌入自己的应用/元服务中。在使用时，您可以指定请求的地图位置、图片大小。

**图1** 静态图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/wBO8ePrRRvSGYdCwH2InBg/zh-cn_image_0000002583479047.jpg?HW-CC-KV=V1&HW-CC-Date=20260427T234953Z&HW-CC-Expire=86400&HW-CC-Sign=75162CD4CB0081FB2701DCA69A131F841015A5FBA97640405713D4406F1EC95E "点击放大")

## 接口说明

以下是地图静态图相关接口，获取静态图功能主要由[staticMap](../harmonyos-references/map-staticmap.md)命名空间下的方法提供，更多接口及使用方法请参见[接口文档](../harmonyos-references/map-staticmap.md)。

| 接口名 | 描述 |
| --- | --- |
| [StaticMapOptions](../harmonyos-references/map-staticmap.md#staticmapoptions) | 用于描述静态图属性。 |
| [getMapImage](../harmonyos-references/map-staticmap.md#getmapimage)(options: [StaticMapOptions](../harmonyos-references/map-staticmap.md#staticmapoptions)): Promise<[image.PixelMap](../harmonyos-references/arkts-apis-image-pixelmap.md)> | 根据提供的参数创建静态图。 |
| [getMapImage](../harmonyos-references/map-staticmap.md#getmapimage-1)(context: [common.Context](../harmonyos-references/js-apis-inner-application-context.md), options: [StaticMapOptions](../harmonyos-references/map-staticmap.md#staticmapoptions)): Promise<[image.PixelMap](../harmonyos-references/arkts-apis-image-pixelmap.md)> | 根据提供的参数创建静态图。支持上传Context上下文。 |

## 开发步骤

1. 导入相关模块。

   ```
   1. import { staticMap } from '@kit.MapKit';
   2. import { BusinessError } from '@kit.BasicServicesKit';
   ```
2. 创建静态图初始化参数，调用[getMapImage](../harmonyos-references/map-staticmap.md#getmapimage)方法获取静态图，效果如下图。

   ```
   1. @Entry
   2. @Component
   3. struct StaticMapDemo {
   4. @State image?: PixelMap = undefined;

   6. build() {
   7. Column() {
   8. this.buildDemoUI();
   9. }.width('100%')
   10. .margin({ bottom: 48 })
   11. .backgroundColor(0xf2f2f2)
   12. .height('100%')
   13. }

   15. @Builder
   16. buildDemoUI() {
   17. // 展示获取的静态图
   18. Image(this.image)
   19. .width('100%')
   20. .fitOriginalSize(false)
   21. .border({ width: 1 })
   22. .borderStyle(BorderStyle.Dashed)
   23. .objectFit(ImageFit.Contain)
   24. .height("90%")

   26. Row() {
   27. Button("getStaticMap")
   28. .fontSize(12)
   29. .onClick(async () => {
   30. // 设置静态图标记参数
   31. let markers: Array<staticMap.StaticMapMarker> = [{
   32. location: {
   33. latitude: 50,
   34. longitude: 126.3
   35. },
   36. font: 'statics',
   37. defaultIconSize: staticMap.IconSize.TINY
   38. }];

   40. // 设置静态图绘制路径参数
   41. let path: staticMap.StaticMapPath = {
   42. locations: [
   43. {
   44. latitude: 50,
   45. longitude: 126
   46. },
   47. {
   48. latitude: 50.3,
   49. longitude: 126
   50. },
   51. {
   52. latitude: 50.3,
   53. longitude: 126.3
   54. },
   55. {
   56. latitude: 49.7,
   57. longitude: 126
   58. },
   59. {
   60. latitude: 50,
   61. longitude: 126
   62. }
   63. ],
   64. width: 3
   65. };

   67. // 拼装静态图参数
   68. let option: staticMap.StaticMapOptions = {
   69. location: {
   70. latitude: 50,
   71. longitude: 126
   72. },
   73. zoom: 10,
   74. imageWidth: 1024,
   75. imageHeight: 1024,
   76. scale: 1,
   77. markers: markers,
   78. path: path
   79. };

   81. try {
   82. // 获取静态图
   83. this.image = await staticMap.getMapImage(option);
   84. console.info("Succeeded in getting image.");
   85. } catch (error) {
   86. const err: BusinessError = error as BusinessError;
   87. console.error(`Failed in getting image, code: ${err.code}, message: ${err.message}`);
   88. }
   89. })
   90. }.margin({ top: 12 })
   91. }
   92. }
   ```

   **图2** 调用getMapImage方法获取静态图

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/85_fdR09SgOfPmJPGayx7w/zh-cn_image_0000002552799398.jpg?HW-CC-KV=V1&HW-CC-Date=20260427T234953Z&HW-CC-Expire=86400&HW-CC-Sign=2FC27E6D55F45EE23205BBEC4200FA4FF52ECC427165ECD0C6DE156CC78830E8 "点击放大")
