---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/map-location-division
title: 区划选择
breadcrumb: 指南 > 应用服务 > Map Kit（地图服务） > 地图Picker > 区划选择
category: harmonyos-guides
scraped_at: 2026-04-28T07:49:55+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:9317bc8148d92ec77fd640f308abb3f172826d820b06b85a78df877322790ed5
---

## 场景介绍

本章节将介绍如何集成区划选择控件。该控件不支持在智能表设备中调用。

区划选择控件可加载全球或指定国家的区划信息，支持以树状结构化选择，支持功能：

* 支持查看选中区划的下级区划。
* 支持推荐热门区划。
* 支持子窗拉起区划控件，适合宽屏设备使用。

**图1** 选择国家

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/6S7DalimTqS5v6sr67_Fvw/zh-cn_image_0000002552799400.jpg?HW-CC-KV=V1&HW-CC-Date=20260427T234954Z&HW-CC-Expire=86400&HW-CC-Sign=B37A075FA15D317AF5293992898DC9652C36A6EE9AE5916A62C6353C65A648E1 "点击放大")

**图2** 选择省市

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/M9D7khs-Ta6AM5pzNZmryg/zh-cn_image_0000002583439095.jpg?HW-CC-KV=V1&HW-CC-Date=20260427T234954Z&HW-CC-Expire=86400&HW-CC-Sign=B118E17019CB967FFB8FE4F6F3AD32411E606309B73DE2C6509C037AF07BCC25 "点击放大")

**图3** 搜索地区

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/qbslDMf5RPyW9sMCJBJV1A/zh-cn_image_0000002552959050.jpg?HW-CC-KV=V1&HW-CC-Date=20260427T234954Z&HW-CC-Expire=86400&HW-CC-Sign=D8AC136AC8BB259C0320BAB6C888B537DE9A697AF264A83DF1D7726476AD7F00 "点击放大")

**图4** 子窗拉起区划控件

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/2W_rlCMPSNmjnyVwKXHwOg/zh-cn_image_0000002583479051.jpg?HW-CC-KV=V1&HW-CC-Date=20260427T234954Z&HW-CC-Expire=86400&HW-CC-Sign=FCAB046D9E0302B5DD3708B81A8154689F5828E2D180F67225B6D2C8CF033B69 "点击放大")

## 约束与限制

使用该功能需满足以下条件：

* 仅支持手机、平板和2in1设备。

## 接口说明

区划选择控件功能主要由[sceneMap](../harmonyos-references/map-scenemap.md)命名空间下的[selectDistrict](../harmonyos-references/map-scenemap.md#selectdistrict)方法提供，更多接口及使用方法请参见[接口文档](../harmonyos-references/map-scenemap.md)。

| 接口名 | 描述 |
| --- | --- |
| [DistrictSelectOptions](../harmonyos-references/map-scenemap.md#districtselectoptions) | 区划选择页面初始选项。 |
| [selectDistrict](../harmonyos-references/map-scenemap.md#selectdistrict)(context: [common.Context](../harmonyos-references/js-apis-inner-application-context.md), options: [DistrictSelectOptions](../harmonyos-references/map-scenemap.md#districtselectoptions)): Promise<[DistrictSelectResult](../harmonyos-references/map-scenemap.md#districtselectresult)> | 调出区划选择页面。 |
| [DistrictSelectResult](../harmonyos-references/map-scenemap.md#districtselectresult) | 区划选择结果。 |

## 开发步骤

1. 导入相关模块。

   ```
   1. import { sceneMap } from '@kit.MapKit';
   2. import { BusinessError } from '@kit.BasicServicesKit';
   ```
2. 创建区划选择请求参数，调用[selectDistrict](../harmonyos-references/map-scenemap.md#selectdistrict)方法拉起区划选择页。

   ```
   1. let districtSelectOptions: sceneMap.DistrictSelectOptions = {
   2. countryCode: "CN",
   3. // 使用子窗拉起方式
   4. subWindowEnabled: true
   5. };
   6. // 拉起区划选择页
   7. sceneMap.selectDistrict(this.getUIContext().getHostContext(), districtSelectOptions).then((data) => {
   8. console.info("SelectDistrict", "Succeeded in selecting district.");
   9. }).catch((err: BusinessError) => {
   10. console.error("SelectDistrict", `Failed to select district, code: ${err.code}, message: ${err.message}`);
   11. });
   ```
