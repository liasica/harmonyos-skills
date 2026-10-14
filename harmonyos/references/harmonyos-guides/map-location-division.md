---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/map-location-division
title: 区划选择
breadcrumb: 指南 > 应用服务 > Map Kit（地图服务） > 地图Picker > 区划选择
category: harmonyos-guides
scraped_at: 2026-10-15T07:05:34+08:00
doc_updated_at: 2026-09-09
content_hash: sha256:f9e8e48f2f48bd9b5f168185fdbb923780bdbfd1237a08fa7b1c9ce7349fe0bc
---

## 场景介绍

从6.1.1(24)开始，支持区划选择控件最大显示层级。

本章节将介绍如何集成区划选择控件。该控件不支持在Wearable设备中调用。

区划选择控件可加载全球或指定国家的区划信息，支持以树状结构化选择，支持功能：

* 支持查看选中区划的下级区划。
* 支持推荐热门区划。
* 支持子窗拉起区划控件，适合宽屏设备使用。

**图1** 选择国家

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/Wsk7rPzhRgOVrrwFMgYr8w/zh-cn_image_0000002762341158.jpg "点击放大")

**图2** 选择省市

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/qgC5pWbDRVSU3uw5d9hGKQ/zh-cn_image_0000002791859955.jpg "点击放大")

**图3** 搜索地区

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/dBLuEOWeSZa0mETkaB56SA/zh-cn_image_0000002762501080.jpg "点击放大")

**图4** 子窗拉起区划控件

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/qe2c3B4ORSazjkT9Cb-exw/zh-cn_image_0000002791739739.jpg "点击放大")

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
