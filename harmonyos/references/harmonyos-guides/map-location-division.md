---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/map-location-division
title: 区划选择
breadcrumb: 指南 > 应用服务 > Map Kit（地图服务） > 地图Picker > 区划选择
category: harmonyos-guides
scraped_at: 2026-11-21T09:12:31+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:daf2e94381dc676bd7c6eb934f96bcfd9b907923538b9014ebb2b93294e202b6
---

## 场景介绍

从6.1.1(24)开始，支持区划选择控件最大显示层级。

本章节将介绍如何集成区划选择控件。该控件不支持在Wearable设备中调用。

区划选择控件可加载全球或指定国家的区划信息，支持以树状结构化选择，支持功能：

* 支持查看选中区划的下级区划。
* 支持推荐热门区划。
* 支持子窗拉起区划控件，适合宽屏设备使用。

**图1** 选择国家

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/PgsB2mAKQOKMwYMf1X12xQ/zh-cn_image_0000002821758077.jpg?HW-CC-KV=V1&HW-CC-Date=20261121T011104Z&HW-CC-Expire=31536000000&HW-CC-Sign=761D56C4897354821B7E18C73D509D5D706C8C0544A09BAC1E32B65287F51716 "点击放大")

**图2** 选择省市

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/Qf1_AHi5ScuHZUTNKjiPGw/zh-cn_image_0000002793038140.jpg?HW-CC-KV=V1&HW-CC-Date=20261121T011104Z&HW-CC-Expire=31536000000&HW-CC-Sign=25E2EB266EEEBD569BD7FE462A6BCB3403C79FFDAF7F3FE7966B689CF943F6F6 "点击放大")

**图3** 搜索地区

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/lRMi1PakS8Kc8Tsy0VmwiA/zh-cn_image_0000002792878170.jpg?HW-CC-KV=V1&HW-CC-Date=20261121T011104Z&HW-CC-Expire=31536000000&HW-CC-Sign=43E1A8692AAE663B3DCFB82CF52D56C7CDE0AB8087F63D49C22AE2FA11C58805 "点击放大")

**图4** 子窗拉起区划控件

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/E2o30crjR6KwTUcvC4IUmw/zh-cn_image_0000002821838077.jpg?HW-CC-KV=V1&HW-CC-Date=20261121T011104Z&HW-CC-Expire=31536000000&HW-CC-Sign=07B2EF3C8A038F4BC4EE9C0F5CBBC26B4D4BA639DA8AAB8E0EB5E14A3839680F "点击放大")

## 约束与限制

使用该功能需满足以下条件：

* 区划选择功能支持Phone、Tablet、PC/2in1设备；从API版本26.0.1开始，新增支持Car设备。

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
