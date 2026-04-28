---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-ui-liveform-sceneanimation-overview
title: 场景动效类型互动卡片概述
breadcrumb: 指南 > 应用框架 > Form Kit（卡片开发服务） > ArkTS卡片开发（推荐） > 互动卡片开发 > 场景动效类型互动卡片 > 场景动效类型互动卡片概述
category: harmonyos-guides
scraped_at: 2026-04-28T07:41:34+08:00
doc_updated_at: 2026-04-17
content_hash: sha256:2d7616d381c4b92c07fc45a2ad1696bf034cde97f3818522ffb13a09e182878a
---

从API version 20开始，场景动效类型互动卡片支持在特定场景下触发互动卡片的特有效果。例如，开发者可以选择将动效渲染区域扩展到卡片自身的渲染区域之外，营造“破框”效果。

## 基本概念

场景动效类型互动卡片主要包含两个状态：激活态和非激活态。卡片生命周期中的事件，如数据定时或定点刷新、用户点击等交互场景，可触发卡片动效，使卡片切换至激活态。动效结束后，卡片切回非激活态。

**非激活态**：在此状态下，卡片与普通卡片行为无异，遵循既有的卡片开发规范，卡片UI由卡片提供方widgetCard.ets中的内容所呈现。

**激活态**： 表示互动卡片动效渲染状态，在此状态下，卡片UI由卡片提供方所开发的[LiveFormExtensionAbility](../harmonyos-references/js-apis-app-form-liveformextensionability.md)对应page页面完成渲染。详细可参考[场景动效类型互动卡片开发指导](arkts-ui-liveform-sceneanimation-development.md)。

**图1** 互动卡片状态切换说明

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/BE4ySfp_Ru62kKdY-PEHxg/zh-cn_image_0000002583438355.png?HW-CC-KV=V1&HW-CC-Date=20260427T234133Z&HW-CC-Expire=86400&HW-CC-Sign=7FBB64E017884821FE6D72B28733E9941B1CF21C127203B1CF9B6375B2E786A2)

**图2** 互动卡片动效触发流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/d67k1BdDT2y71QHCMqL2ZA/zh-cn_image_0000002552958310.png?HW-CC-KV=V1&HW-CC-Date=20260427T234133Z&HW-CC-Expire=86400&HW-CC-Sign=B0363FE5A2E6F334D7264970E6C38FC9C0C9B7A0D9B342AB6815A5F8E534C970)

## 实现原理

开发者可以通过[formProvider.requestOverflow](../harmonyos-references/js-apis-app-form-formprovider.md#formproviderrequestoverflow20)接口触发互动卡片动效，例如在用户点击时触发，典型时序图如下。

**图3** 点击触发互动卡片动效时序图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/wFi8vBnXRguNjQYMlKgIUg/zh-cn_image_0000002583478311.png?HW-CC-KV=V1&HW-CC-Date=20260427T234133Z&HW-CC-Expire=86400&HW-CC-Sign=E4866050921038456B239B442377A9CA948E9D8E05C3F7EABF6A1DFBF94859FA)

定时定点刷新互动卡片动效的时序图如下。

**图4** 定时定点触发互动卡片动效时序图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/gtDHlwBRRzy9fWoaba5sng/zh-cn_image_0000002552798662.png?HW-CC-KV=V1&HW-CC-Date=20260427T234133Z&HW-CC-Expire=86400&HW-CC-Sign=56FCFA5385D5950C8195C7F2F24DF633A4D265922519BCD0AA5E3856038FFE19)

## 约束和限制

### 支持的场景

1. 当前互动卡片动效只有在[FormLocation](../harmonyos-references/js-apis-app-form-forminfo.md#formlocation20)为“DESKTOP”的单张卡片上面才能生效。
2. 由于性能功耗影响只支持部分机型，在不支持的机型会报[801](../harmonyos-references/errorcode-universal.md#section801-该设备不支持此api)错误码。

### 请求参数约束

1. 互动卡片申请动效的最大合法动效时长：3500ms，倒计时结束时，卡片将切换回非激活态。
2. 由卡片定时定点刷新触发的互动卡片动效，一天内单张卡片最多触发50次。
3. 最大可申请动效区域：如下图，矩形ABCD表示卡片自身渲染区域，矩形IJKL表示卡片最大可申请动效区域。两个矩形中心对齐。尺寸满足以下表格描述。

| 卡片样式 | JK 边长 | IJ 边长 |
| --- | --- | --- |
| 1 \* 2 | 不超过AD边长的150%。 | 不超过AB边长的200%。 |
| 2 \* 2 | 不超过AD边长的150%。 | 不超过AB边长的150%。 |
| 2 \* 4 | 不超过AD边长的125%。 | 不超过AB边长的150%。 |
| 4 \* 4 | 不超过AD边长的125%。 | 不超过AB边长的125%。 |
| 6 \* 4 | 不超过AD边长的125%。 | 不超过AB边长的110%。 |

**图5** 互动卡片动效区域申请规则说明

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/IihkQSanR_aBLNxYIySxhw/zh-cn_image_0000002583438357.png?HW-CC-KV=V1&HW-CC-Date=20260427T234133Z&HW-CC-Expire=86400&HW-CC-Sign=57EE9BC4F1E7FB252A1283FCF8697A08C2170D13D02005BD4394CDD3E873D208)

例如：某设备上一个2\*2卡片宽度为158vp，高度为158vp。对应上图则有：

（1）AD=158vp，AB=158vp，IJ=158\*1.5=237vp，IL=158\*1.5=237vp。

（2）IA两点水平相距39.5vp，垂直相距39.5vp。

因此，以A点为原点，向右为X轴正方向，向下为Y轴正方向，图5中E点的合法坐标可以是（-20，-20），EF边长合法值可以是200vp，EH边长合法值可以是200vp。

互动卡片可以通过调用[formProvider.getFormRect](../harmonyos-references/js-apis-app-form-formprovider.md#formprovidergetformrect20)接口获取卡片在窗口中的尺寸及相对坐标位置信息。卡片提供方以此计算动效申请范围，坐标计算时，以上图A点为（0,0）点，计算矩形EFGH对应参数，单位为vp。

调用[formProvider.requestOverflow](../harmonyos-references/js-apis-app-form-formprovider.md#formproviderrequestoverflow20)接口时，[overflowInfo](../harmonyos-references/js-apis-app-form-forminfo.md#overflowinfo20)中描述的互动卡片动效渲染区域（矩形EFGH）需要满足：

1. 包含了卡片（矩形ABCD）的全部区域。
2. 不超过矩形IJKL（矩形IJKL完整包含矩形EFGH）。

具体可参考[场景动效类型互动卡片开发指导](arkts-ui-liveform-sceneanimation-development.md)。

### 功耗约束

1. 设备进入省电模式时，互动卡片不响应动效请求。
2. 当设备热档位进入HOT时，不再响应非点击触发的动效请求；当热档位进入OVERHEATED时，不再响应所有动效请求。具体可参考[热档位信息](../harmonyos-references/js-apis-thermal.md#thermallevel)。

### 动效请求约束

1. 同一时刻，全局只有一个卡片执行互动卡片动效。
2. 当用户通过点击等方式主动触发互动卡片动效时，优先响应此次请求。此时，当前卡片切换到激活态，执行动效，其他卡片切换到非激活态。
3. 其他触发方式，例如通过卡片定时定点数据刷新机制触发动效，遵循先到先得原则。系统只处理第一个合法动效请求。其他请求返回失败，同时不做缓存。
4. 用户在桌面的其他有效操作（点击应用、卡片等，滑动翻页，下拉进入全搜、双中心、拖动卡片、长按卡片等）均会打断当前动效，卡片重新变成非激活态。
5. 互动卡片执行动效期间，超过卡片自身渲染范围（对应图5中的矩形ABCD）的交互事件，互动卡片不做响应。
6. 更多场景动效类型互动卡片激活态能力约束，可参考[LiveFormExtensionAbility](../harmonyos-references/js-apis-app-form-liveformextensionability.md)中说明。
