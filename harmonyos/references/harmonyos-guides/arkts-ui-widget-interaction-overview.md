---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-ui-widget-interaction-overview
title: ArkTS卡片页面刷新概述
breadcrumb: 指南 > 应用框架 > Form Kit（卡片开发服务） > ArkTS卡片开发（推荐） > ArkTS卡片提供方开发指导 > ArkTS卡片页面刷新 > ArkTS卡片页面刷新概述
category: harmonyos-guides
scraped_at: 2026-04-29T13:29:55+08:00
doc_updated_at: 2026-03-20
content_hash: sha256:b803924f3aecbe88808e6c6176ee01d7d907544cb5f922da0ce49df9e355626e
---

卡片使用方（例如：桌面）和卡片提供方均可主动触发卡片页面刷新。此外，卡片管理服务会根据开发者声明的定时信息，按需通知卡片提供方进行卡片刷新。因此，卡片刷新方式包括：卡片提供方主动触发刷新、卡片使用方主动触发刷新以及卡片定时定点刷新。这些刷新方式均需由卡片提供方推送需要刷新的卡片数据。

## 卡片数据交互

ArkTS卡片管理服务支持卡片提供方（例如：应用）和卡片之间的数据交互。卡片通过[postCardAction](../harmonyos-references/js-apis-postcardaction.md#postcardaction-1)传递数据给卡片提供方，卡片提供方则通过[updateForm](../harmonyos-references/js-apis-app-form-formprovider.md#formproviderupdateform)接口传递数据给卡片。卡片提供方将数据提供给卡片后，可以用于卡片页面刷新等。

由于卡片提供方和卡片为相互独立的进程，两者间的数据共享只能通过[LocalStorageProp](arkts-localstorage.md#localstorageprop)传递，不能使用getContext方法。因此卡片提供方推送数据后，卡片UI需要通过LocalStorageProp接收数据，且接收数据时，卡片数据会被转换成string类型。

## 页面刷新分类

根据触发方式的差异，卡片刷新分为主动刷新和被动刷新。

### 主动刷新

主动刷新包括卡片提供方主动刷新卡片和卡片使用方主动刷新卡片。开发指导请参考[ArkTS卡片主动刷新](arkts-ui-widget-active-refresh.md)。

**图1 卡片提供方主动刷新卡片流程图**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/D7H9SGNuTEKcwgJ48z4ZXQ/zh-cn_image_0000002558605136.png?HW-CC-KV=V1&HW-CC-Date=20260429T052954Z&HW-CC-Expire=86400&HW-CC-Sign=0C5ACA90C5023E0BC35054D58E7FEF1FF1EA3004DE4BE45D8EBD95A5D05EA241)

卡片提供方应用运行过程中，如果识别到有要更新卡片数据的诉求，可以主动通过formProvider提供的[updateForm](../harmonyos-references/js-apis-app-form-formprovider.md#formproviderupdateform)接口更新卡片。

**图2 卡片使用方主动刷新卡片流程图**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/KcW_AP2SR-uH-8gf2L0x2w/zh-cn_image_0000002589324661.png?HW-CC-KV=V1&HW-CC-Date=20260429T052954Z&HW-CC-Expire=86400&HW-CC-Sign=8E607A3EA7A65484D1A3D4AAFDB07185DAC0723809B595CE912C33DED89D09CC)

当卡片使用方检测到系统语言或主题模式（如深浅色）发生变化时，可以主动通过formHost提供的requestForm（仅支持系统应用使用）接口请求更新卡片，卡片管理服务会进而通知卡片提供方完成卡片更新。

### 被动刷新

被动刷新包括定时刷新、定点刷新。开发指导请参考[ArkTS卡片被动刷新](arkts-ui-widget-passive-refresh.md)。

卡片定时刷新：表示在一定时间间隔内调用[onUpdateForm](../harmonyos-references/js-apis-app-form-formextensionability.md#formextensionabilityonupdateform)的生命周期回调函数自动刷新卡片内容。

卡片定点刷新：表示在每天的某个特定时间点自动刷新卡片内容。

**图3 卡片管理服务通知卡片提供方定时定点刷新卡片流程图**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/HWMQ7qHRRdiR5ZFUIeEWxA/zh-cn_image_0000002589244599.png?HW-CC-KV=V1&HW-CC-Date=20260429T052954Z&HW-CC-Expire=86400&HW-CC-Sign=D421CFD3D145EA346F3785AD0BB90932D2B7C982562D996FCD2456A8462FD87B)

根据卡片提供方开发者提前配置声明的定时刷新信息，卡片管理服务会根据定时信息、卡片可见状态、刷新次数等因素综合判断是否需要通知卡片提供方更新卡片。

## 约束与限制

1. 卡片提供方仅允许刷新自己的卡片，其他提供方的卡片无法刷新。
2. 卡片使用方仅允许刷新添加到自己的卡片，添加到其他使用方的卡片无法刷新。
3. 从API version 20开始，如果卡片刷新的数据通过共享内存更新，刷新数据总大小不超过10MB，刷新图片数量不超过20张。API version 19及之前的版本，图片文件数量上限为5张，每张限制内存2MB，超出限制的图片会显示异常。
