---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/map-location-selecting
title: 地点选取
breadcrumb: 指南 > 应用服务 > Map Kit（地图服务） > 地图Picker > 地点选取
category: harmonyos-guides
scraped_at: 2026-04-28T07:49:54+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:74fd4f2ed807039ed5c5882e4d34cba0b206b0f890aa1a67dc9c2464821064c3
---

## 场景介绍

本章节将向您介绍如何集成地点选取控件，您无需自己开发地图页面，可快速实现地点选取的能力。该控件不支持在智能表设备中调用。

**图1** 地点选取页

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/O7ORDZt-THKuLpHXdH6Amw/zh-cn_image_0000002552959048.jpg?HW-CC-KV=V1&HW-CC-Date=20260427T234953Z&HW-CC-Expire=86400&HW-CC-Sign=4737A49584EEC7127DB20E5BBD47898D1BFEEBA4922CF30E012710C7FD9BB658 "点击放大")

**图2** 地点选取

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/74zRujqQS-WKwd25H39Q8Q/zh-cn_image_0000002583479049.jpg?HW-CC-KV=V1&HW-CC-Date=20260427T234953Z&HW-CC-Expire=86400&HW-CC-Sign=25F3B26F45185B3A6FB3F66684DB36F1516807DC3D03884467FFFB45414C6872 "点击放大")

## 约束与限制

使用该功能需满足以下条件：

* 仅支持手机、平板和2in1设备。

## 接口说明

地点选取控件功能主要由[sceneMap](../harmonyos-references/map-scenemap.md)命名空间下的[chooseLocation](../harmonyos-references/map-scenemap.md#chooselocation)方法提供，更多接口及使用方法请参见[接口文档](../harmonyos-references/map-scenemap.md)。

| 接口名 | 描述 |
| --- | --- |
| [LocationChoosingOptions](../harmonyos-references/map-scenemap.md#locationchoosingoptions) | 地点选取的参数。 |
| [chooseLocation](../harmonyos-references/map-scenemap.md#chooselocation)(context: common.[UIAbilityContext](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md), options: [LocationChoosingOptions](../harmonyos-references/map-scenemap.md#locationchoosingoptions)): Promise<[LocationChoosingResult](../harmonyos-references/map-scenemap.md#locationchoosingresult)> | 地点选取。 |
| [LocationChoosingResult](../harmonyos-references/map-scenemap.md#locationchoosingresult) | 地点选取的返回结果。 |

## 开发步骤

1. 导入相关模块。

   ```
   1. import { sceneMap } from '@kit.MapKit';
   2. import { BusinessError } from '@kit.BasicServicesKit';
   3. import { common } from '@kit.AbilityKit';
   ```
2. 创建地点选取参数，调用[chooseLocation](../harmonyos-references/map-scenemap.md#chooselocation)方法拉起地点选取页。

   ```
   1. let locationChoosingOptions: sceneMap.LocationChoosingOptions = {
   2. // 地图中心点坐标
   3. location: {
   4. latitude: 39.91804051376904,
   5. longitude: 116.3970536796932
   6. },
   7. // 展示搜索控件
   8. searchEnabled: true,
   9. // 展示附近POI
   10. showNearbyPoi: true
   11. };
   12. // 拉起地点选取页
   13. sceneMap.chooseLocation(this.getUIContext().getHostContext() as common.UIAbilityContext,
   14. locationChoosingOptions).then((data) => {
   15. console.info("ChooseLocation", "Succeeded in choosing location.");
   16. }).catch((err: BusinessError) => {
   17. console.error("ChooseLocation", `Failed to choose location, code: ${err.code}, message: ${err.message}`);
   18. });
   ```
