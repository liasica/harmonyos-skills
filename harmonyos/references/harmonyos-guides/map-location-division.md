---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/map-location-division
title: 区划选择
breadcrumb: 指南 > 应用服务 > Map Kit（地图服务） > 地图Picker > 区划选择
category: harmonyos-guides
scraped_at: 2026-11-19T09:49:06+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:7a6d467e615017546ababa8215492cf7bce6e447eb5c8fb52bf42cd9ac43cc4c
---

## 场景介绍

从6.1.1(24)开始，支持区划选择控件最大显示层级。

本章节将介绍如何集成区划选择控件。该控件不支持在Wearable设备中调用。

区划选择控件可加载全球或指定国家的区划信息，支持以树状结构化选择，支持功能：

* 支持查看选中区划的下级区划。
* 支持推荐热门区划。
* 支持子窗拉起区划控件，适合宽屏设备使用。

**图1** 选择国家

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/td4tk3-VSG-PKKkZPw4kWA/zh-cn_image_0000002791566516.jpg?HW-CC-KV=V1&HW-CC-Date=20261119T014905Z&HW-CC-Expire=31536000000&HW-CC-Sign=8904C99C0D19EA043D3CC27EC04BC07D50EC5121C160D1BFFBD3ECBB9B86F45F "点击放大")

**图2** 选择省市

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9/v3/Vi5kQxN5RjeJ7hIYzQ2xJA/zh-cn_image_0000002820526469.jpg?HW-CC-KV=V1&HW-CC-Date=20261119T014905Z&HW-CC-Expire=31536000000&HW-CC-Sign=690A5D5C54FD48A55929AC3A7B507339056B09F85556D8EE42AB5FB51DCC7957 "点击放大")

**图3** 搜索地区

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/aE5vEDoZT-GRrlVH3FcZ0w/zh-cn_image_0000002820406469.jpg?HW-CC-KV=V1&HW-CC-Date=20261119T014905Z&HW-CC-Expire=31536000000&HW-CC-Sign=8EC996281F30F759B539A028A388479C03D6280231EE2FA0B1E7949A9CB2FEE6 "点击放大")

**图4** 子窗拉起区划控件

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/N7JvHBODTpS25ohx42LATg/zh-cn_image_0000002791726490.jpg?HW-CC-KV=V1&HW-CC-Date=20261119T014905Z&HW-CC-Expire=31536000000&HW-CC-Sign=8686A01A77E22A8C4E0BFA17C1DB24B196B7D89EA5912F8485FFD61B9A12D1F2 "点击放大")

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
