---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/map-location-division
title: 区划选择
breadcrumb: 指南 > 应用服务 > Map Kit（地图服务） > 地图Picker > 区划选择
category: harmonyos-guides
scraped_at: 2026-11-14T08:48:25+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:d9d7d0c09f15bb34f1724834110ad92244d7e823699fa5773b9cb8977f83d1d2
---

## 场景介绍

从6.1.1(24)开始，支持区划选择控件最大显示层级。

本章节将介绍如何集成区划选择控件。该控件不支持在Wearable设备中调用。

区划选择控件可加载全球或指定国家的区划信息，支持以树状结构化选择，支持功能：

* 支持查看选中区划的下级区划。
* 支持推荐热门区划。
* 支持子窗拉起区划控件，适合宽屏设备使用。

**图1** 选择国家

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/XVTZ3VHCQumqF_egaS8XWA/zh-cn_image_0000002788468130.jpg?HW-CC-KV=V1&HW-CC-Date=20261114T004824Z&HW-CC-Expire=31536000000&HW-CC-Sign=601C56162ECDCAFF1AE0F730AF2EB7546DB0215B5216A5DC382C5068E2229289 "点击放大")

**图2** 选择省市

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/0e8u-vbOSZG0f4fMXnRK0Q/zh-cn_image_0000002817507619.jpg?HW-CC-KV=V1&HW-CC-Date=20261114T004824Z&HW-CC-Expire=31536000000&HW-CC-Sign=BB5BE1EA619977EEFEE00E886FC39CE70A1BC86D222F1AB0D445B75FDEFFC97A "点击放大")

**图3** 搜索地区

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/dsfpazJlSWKWfNkLYdhavw/zh-cn_image_0000002788308188.jpg?HW-CC-KV=V1&HW-CC-Date=20261114T004824Z&HW-CC-Expire=31536000000&HW-CC-Sign=598885E38DB798ABED8BD7D05A84864B4956D1DE45C836A7E70B050E5B58B0F8 "点击放大")

**图4** 子窗拉起区划控件

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/LSiJA7xhQI2RcqBpYSvkKQ/zh-cn_image_0000002817427551.jpg?HW-CC-KV=V1&HW-CC-Date=20261114T004824Z&HW-CC-Expire=31536000000&HW-CC-Sign=D9B47BED54B240D36D98339EC8D1B563E3B384279F45846110381EE0454265C9 "点击放大")

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
