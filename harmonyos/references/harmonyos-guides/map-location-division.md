---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/map-location-division
title: 区划选择
breadcrumb: 指南 > 应用服务 > Map Kit（地图服务） > 地图Picker > 区划选择
category: harmonyos-guides
scraped_at: 2026-04-29T13:39:18+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:058c360ff360bd3ef527d92c1693a967420ebce55f254e50aca3d11f008e9f19
---

## 场景介绍

本章节将介绍如何集成区划选择控件。该控件不支持在智能表设备中调用。

区划选择控件可加载全球或指定国家的区划信息，支持以树状结构化选择，支持功能：

* 支持查看选中区划的下级区划。
* 支持推荐热门区划。
* 支持子窗拉起区划控件，适合宽屏设备使用。

**图1** 选择国家

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/PFvB3fyGSXa8qxFbGKXY7A/zh-cn_image_0000002589325421.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T053916Z&HW-CC-Expire=86400&HW-CC-Sign=908CF3A92B50DA3C3A9FBB1C2DBDEB32FE86FD20085FA10588C606074C7A8650 "点击放大")

**图2** 选择省市

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/AcK91eAJTBWcTMTLd6YO6A/zh-cn_image_0000002589245359.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T053916Z&HW-CC-Expire=86400&HW-CC-Sign=DABF97CEE1D67709E667B15A8A71D9FDB8A34AA59F3C6184A73382064B946270 "点击放大")

**图3** 搜索地区

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b8/v3/AAMP0revTN-bnJOs6KvZWQ/zh-cn_image_0000002558765552.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T053916Z&HW-CC-Expire=86400&HW-CC-Sign=2451C05A238C68D6BF20C64AED87F65740C59DC1602DD018D945CDFBF8D53B2A "点击放大")

**图4** 子窗拉起区划控件

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/sAb2cUFjQTC26Nl8xKMg6w/zh-cn_image_0000002558605896.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T053916Z&HW-CC-Expire=86400&HW-CC-Sign=C3E8BD8CBAA3AF2006546812F5040C4A76A7973F35995C0A30D59097479D9F31 "点击放大")

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
