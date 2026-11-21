---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/map-location-selecting
title: 地点选取
breadcrumb: 指南 > 应用服务 > Map Kit（地图服务） > 地图Picker > 地点选取
category: harmonyos-guides
scraped_at: 2026-11-21T09:12:31+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:349e20cff35886dd8ed59320a0fb86aafe2f55a3b243cdfd3d37081fee69762b
---

## 场景介绍

本章节将向您介绍如何集成地点选取控件，您无需自己开发地图页面，可快速实现地点选取的能力。该控件不支持在智能表设备中调用。

**图1** 地点选取页

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/F2K1cRIISoqBr0-w1wVsQw/zh-cn_image_0000002792878168.jpg?HW-CC-KV=V1&HW-CC-Date=20261121T011231Z&HW-CC-Expire=31536000000&HW-CC-Sign=00C5040BEC9C226C9560DA1E11AF4BE070E5FBB1224FC23C96288B0A91A3FC97 "点击放大")

**图2** 地点选取

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/onBwOwoRRf6uii_0tUwUSA/zh-cn_image_0000002821838075.jpg?HW-CC-KV=V1&HW-CC-Date=20261121T011231Z&HW-CC-Expire=31536000000&HW-CC-Sign=BA9BAAE22E52529110675AA16ABA96BFE47EB91AC8222A789106B0512A9826DE "点击放大")

## 约束与限制

使用该功能需满足以下条件：

* 地点选取功能仅支持Phone、Tablet、PC/2in1设备；从API版本26.0.1开始，新增支持Car设备。

## 接口说明

地点选取控件功能主要由[sceneMap](../harmonyos-references/map-scenemap.md)命名空间下的[chooseLocation](../harmonyos-references/map-scenemap.md#chooselocation)方法提供，更多接口及使用方法请参见[接口文档](../harmonyos-references/map-scenemap.md)。

| 接口名 | 描述 |
| --- | --- |
| [LocationChoosingOptions](../harmonyos-references/map-scenemap.md#locationchoosingoptions) | 地点选取的参数。 |
| [chooseLocation](../harmonyos-references/map-scenemap.md#chooselocation)(context: common.[UIAbilityContext](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md), options: [LocationChoosingOptions](../harmonyos-references/map-scenemap.md#locationchoosingoptions)): Promise<[LocationChoosingResult](../harmonyos-references/map-scenemap.md#locationchoosingresult)> | 地点选取。 |
| [LocationChoosingResult](../harmonyos-references/map-scenemap.md#locationchoosingresult) | 地点选取的返回结果。 |

## 开发步骤

1. 导入相关模块。

   ```typescript
   import { sceneMap } from '@kit.MapKit';
   import { BusinessError } from '@kit.BasicServicesKit';
   import { common } from '@kit.AbilityKit';
   ```
2. 创建地点选取参数，调用[chooseLocation](../harmonyos-references/map-scenemap.md#chooselocation)方法拉起地点选取页。

   ```typescript
   let locationChoosingOptions: sceneMap.LocationChoosingOptions = {
     // 地图中心点坐标
     location: {
       latitude: 39.91804051376904,
       longitude: 116.3970536796932
     },
     // 展示搜索控件
     searchEnabled: true,
     // 展示附近POI
     showNearbyPoi: true
   };
   // 拉起地点选取页
   sceneMap.chooseLocation(this.getUIContext().getHostContext() as common.UIAbilityContext,
     locationChoosingOptions).then((data) => {
     console.info('ChooseLocation', 'Succeeded in choosing location.');
   }).catch((err: BusinessError) => {
     console.error('ChooseLocation', `Failed to choose location, code: ${err.code}, message: ${err.message}`);
   });
   ```
