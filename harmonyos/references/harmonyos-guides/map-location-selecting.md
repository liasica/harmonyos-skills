---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/map-location-selecting
title: 地点选取
breadcrumb: 指南 > 应用服务 > Map Kit（地图服务） > 地图Picker > 地点选取
category: harmonyos-guides
scraped_at: 2026-04-29T13:39:17+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:53ee8351ffbf233da782e2a6a09885c79b635e9a8f0e906f8004063d2b396a1a
---

## 场景介绍

本章节将向您介绍如何集成地点选取控件，您无需自己开发地图页面，可快速实现地点选取的能力。该控件不支持在智能表设备中调用。

**图1** 地点选取页

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/NpDBbyC3QhK2h_XNzMEkew/zh-cn_image_0000002558765550.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T053659Z&HW-CC-Expire=86400&HW-CC-Sign=6B013E76461049A3A67FED27E2F340B8F5A1337A7B5C79A83B1DD0FA14FCA45D "点击放大")

**图2** 地点选取

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/MDPFUh46R_S0KJLPcT1Row/zh-cn_image_0000002558605894.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T053659Z&HW-CC-Expire=86400&HW-CC-Sign=E9D08AC48DA0F18D3DB1D28B83F8ECA143F0B9859D8B4ECDA4307E3405639F25 "点击放大")

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
