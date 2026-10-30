---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/map-location-division
title: 区划选择
breadcrumb: 指南 > 应用服务 > Map Kit（地图服务） > 地图Picker > 区划选择
category: harmonyos-guides
scraped_at: 2026-10-31T07:33:07+08:00
doc_updated_at: 2026-09-09
content_hash: sha256:9ae00396acc957524096608df7ea42b4c934091dde630605c529d43af67e663d
---

## 场景介绍

从6.1.1(24)开始，支持区划选择控件最大显示层级。

本章节将介绍如何集成区划选择控件。该控件不支持在Wearable设备中调用。

区划选择控件可加载全球或指定国家的区划信息，支持以树状结构化选择，支持功能：

* 支持查看选中区划的下级区划。
* 支持推荐热门区划。
* 支持子窗拉起区划控件，适合宽屏设备使用。

**图1** 选择国家

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/qevS1-pKR_2xrXG3Elti6A/zh-cn_image_0000002776910022.jpg "点击放大")

**图2** 选择省市

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/5mnloWZ5TaS4HkBVxe8q_g/zh-cn_image_0000002776750036.jpg "点击放大")

**图3** 搜索地区

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/N7mAmz_2RrCMDPcRyL8dEw/zh-cn_image_0000002806029753.jpg "点击放大")

**图4** 子窗拉起区划控件

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/itbW8EsORh6aHlZZgsiX3Q/zh-cn_image_0000002806109643.jpg "点击放大")

## 约束与限制

使用该功能需满足以下条件：

* 仅支持手机、平板和PC/2in1设备。

## 接口说明

区划选择控件功能主要由[sceneMap](../harmonyos-references/map-scenemap.md)命名空间下的[selectDistrict](../harmonyos-references/map-scenemap.md#selectdistrict)方法提供，更多接口及使用方法请参见[接口文档](../harmonyos-references/map-scenemap.md)。

| 接口名 | 描述 |
| --- | --- |
| [DistrictSelectOptions](../harmonyos-references/map-scenemap.md#districtselectoptions) | 区划选择页面初始选项。 |
| [selectDistrict](../harmonyos-references/map-scenemap.md#selectdistrict)(context: [common.Context](../harmonyos-references/js-apis-inner-application-context.md), options: [DistrictSelectOptions](../harmonyos-references/map-scenemap.md#districtselectoptions)): Promise<[DistrictSelectResult](../harmonyos-references/map-scenemap.md#districtselectresult)> | 调出区划选择页面。 |
| [DistrictSelectResult](../harmonyos-references/map-scenemap.md#districtselectresult) | 区划选择结果。 |

## 开发步骤

1. 导入相关模块。

   ```typescript
   import { sceneMap } from '@kit.MapKit';
   import { BusinessError } from '@kit.BasicServicesKit';
   ```
2. 创建区划选择请求参数，调用[selectDistrict](../harmonyos-references/map-scenemap.md#selectdistrict)方法拉起区划选择页。

   ```typescript
   let districtSelectOptions: sceneMap.DistrictSelectOptions = {
     countryCode: "CN",
     // 使用子窗拉起方式
     subWindowEnabled: true,
     // 区划选择控件的最大显示层级
     maxAdminLevel: 3
   };
   // 拉起区划选择页
   sceneMap.selectDistrict(this.getUIContext().getHostContext(), districtSelectOptions).then((data) => {
     console.info("SelectDistrict", "Succeeded in selecting district.");
   }).catch((err: BusinessError) => {
     console.error("SelectDistrict", `Failed to select district, code: ${err.code}, message: ${err.message}`);
   });
   ```
