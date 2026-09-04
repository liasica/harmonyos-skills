---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/map-location-selecting
title: 地点选取
breadcrumb: 指南 > 应用服务 > Map Kit（地图服务） > 地图Picker > 地点选取
category: harmonyos-guides
scraped_at: 2026-09-05T06:15:13+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:345cee21bab4ed70a020907402e4890dccc2f9a90a63c71b27f22c83ee3389f4
---

## 场景介绍

本章节将向您介绍如何集成地点选取控件，您无需自己开发地图页面，可快速实现地点选取的能力。该控件不支持在智能表设备中调用。

**图1** 地点选取页

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/YLSXKTykRtW6xKzsspuZ9Q/zh-cn_image_0000002742004263.jpg "点击放大")

**图2** 地点选取

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/bPesuoOKTsSuG9wA6tdMJQ/zh-cn_image_0000002712405274.jpg "点击放大")

## 约束与限制

使用该功能需满足以下条件：

* 仅支持手机、平板和PC/2in1设备。

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
