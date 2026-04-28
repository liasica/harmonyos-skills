---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/account-overview-minorsprotection
title: 概述
breadcrumb: 指南 > 应用服务 > Account Kit（华为账号服务） > 未成年人模式 > 概述
category: harmonyos-guides
scraped_at: 2026-04-28T07:48:01+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:4a7127a20fdaa46d2aefb0a591ee3edcd51dc6f01cfe725005d7eef3a6345bf9
---

未成年人模式用于帮助应用与系统联动，提供未成年人网络保护。应用通过接入Account Kit提供的[未成年人模式能力](../harmonyos-references/account-api-minorsprotection.md)与系统联动，可快速实现自动切换未成年人模式状态，简化了家长用户的设置步骤，为未成年人提供安全、健康的网络环境。

## 基本概念

* 未成年人

  本章节中所指未成年人，即中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）未满十八周岁的公民。
* 开启系统未成年人模式后的限制项目

  1. 使用时长限制：针对16周岁及以上不满18周岁的未成年人使用者，默认每日可使用时长2小时，其他年龄的未成年人使用者，默认每日可使用时长为1小时。
  2. 应用安装限制：默认仅允许安装适龄应用。
  3. 应用打开限制：默认仅允许打开已[接入未成年人模式](account-overview-minorsprotection.md#接入规范)且配置minors\_mode值为"1"的应用（游戏类应用要求满足“适龄应用”条件），家长可对应用进行豁免，允许本次使用。
  4. 内容访问限制：接入未成年人模式的应用默认随系统切换至未成年人模式，在应用内展示适龄内容。
  5. 其他系统功能限制：部分系统功能将受限使用，包括部分应用的卸载更新，退出系统华为账号登录，USB调试功能等，更多限制请进入“设置 > 健康使用设备”查看。
* 适龄应用

  适龄应用指在华为应用市场中的应用分级小于或等于未成年使用者的年龄的应用。例如：

  1. 某应用在华为应用市场的年龄分级为年满12周岁（12+），未成年使用者为13周岁，则该应用为适龄应用。
  2. 某应用在华为应用市场的年龄分级为年满18周岁（18+），未成年使用者为7周岁，则该应用为非适龄应用。
* 远程守护

  开发者可在“设置 > 华为账号 > 家人共享 > 远程守护”开启远程守护。开启远程守护后，未成年人的设备上的未成年人模式会自动退出。

## 未成年人模式能力介绍

系统提供的未成年人模式能力如下：

* [获取系统未成年人模式开启状态和年龄段信息](../harmonyos-references/account-api-minorsprotection.md#getminorsprotectioninfosync)：开发者可读取当前系统未成年人模式的开启和关闭状态，并根据此状态对应开启或退出应用的未成年人模式。开启系统未成年人模式时，家长会设置未成年人的年龄信息。在未成年人模式开启时，开发者可读取当前系统未成年人模式下未成年人的年龄段，并向未成年人提供符合该年龄段的内容和服务。当前可获取的年龄段划分如下：

  + 不满3周岁；
  + 3周岁及以上不满8周岁；
  + 8周岁及以上不满12周岁；
  + 12周岁及以上不满16周岁；
  + 16周岁及以上不满18周岁。
* [开启系统未成年人模式](../harmonyos-references/account-api-minorsprotection.md#leadtoturnonminorsmode)：开发者可以调用此接口拉起系统未成年人模式引导页，引导用户开启系统的未成年人模式。
* [关闭系统未成年人模式](../harmonyos-references/account-api-minorsprotection.md#leadtoturnoffminorsmode)：开发者可以调用此接口拉起关闭系统未成年人模式页面，引导用户关闭系统的未成年人模式。
* [系统家长身份验证能力](../harmonyos-references/account-api-minorsprotection.md#verifyminorsprotectioncredential)：开启系统未成年人模式时，家长会设置六位数字密码作为未成年人模式状态的指令依据。在未成年人模式开启时，开发者可按需调用系统家长身份验证接口，以验证家长身份。

## 场景分析

| 场景名称 | 场景介绍 | 子场景名称 | 实现方案思路 |
| --- | --- | --- | --- |
| [应用与系统联动切换未成年人模式](account-system-minorsprotection.md) | 应用与系统未成年人模式进行联动切换未成年人模式。 | 获取系统未成年人模式开启状态。 | 通过[查询系统未成年人模式开启状态](../harmonyos-references/account-api-minorsprotection.md#getminorsprotectioninfosync)或[订阅未成年人模式公共事件](account-system-minorsprotection.md#事件说明)来获取系统未成年人模式开启状态，应用的未成年人模式状态需和系统未成年人模式的状态保持一致。 |
| [应用内开启未成年人模式](account-app-turn-on-minorsprotection.md) | 在应用内开启系统未成年人模式。 | 引导用户开启系统未成年人模式。 | 调用系统未成年人模式的开启接口[leadToTurnOnMinorsMode](../harmonyos-references/account-api-minorsprotection.md#leadtoturnonminorsmode)，拉起系统未成年人模式开启流程。系统未成年人模式开启后，应用需跟随同步开启。 |
| [关闭应用的未成年人模式](account-appself-turn-off-minorsprotection.md) | 应用可单独关闭应用的未成年人模式。 | 用户操作关闭应用的未成年人模式。 | 调用家长身份验证接口[verifyMinorsProtectionCredential](../harmonyos-references/account-api-minorsprotection.md#verifyminorsprotectioncredential)，验证通过后，可关闭应用的未成年人模式，同时需要记录单独关闭的标记为true，表明当前用户操作单独关闭应用的未成年人模式。 |
| [关闭应用的未成年人模式（查询或订阅方式）](account-appself-turn-off-minorsprotection.md) | 应用可单独关闭应用的未成年人模式。 | 查询或订阅到未成年人模式已开启/关闭。 | 当查询或订阅到未成年人模式已开启，如单独关闭的标记为true，则应用不开启未成年人模式，否则需要开启未成年人模式。  当查询或订阅到未成年人模式已关闭，需设置单独关闭的标记为false，且关闭应用的未成年人模式。 |
| [关闭系统的未成年人模式](account-system-turn-off-minorsprotection.md) | 在应用内关闭系统未成年人模式。 | 引导用户关闭系统未成年人模式。 | 调用系统未成年人模式的关闭接口[leadToTurnOffMinorsMode](../harmonyos-references/account-api-minorsprotection.md#leadtoturnoffminorsmode)，拉起系统的未成年人模式关闭流程，系统未成年人模式关闭后，应用需跟随同步关闭。 |
| [应用内调整未成年人模式设置](account-password-minorsprotection.md) | 用户调整内容偏好、使用时长等设置，验证家长身份。 | 拉起验证未成年人模式密码页面，验证家长身份。 | 调用家长身份验证接口[verifyMinorsProtectionCredential](../harmonyos-references/account-api-minorsprotection.md#verifyminorsprotectioncredential)，拉起验证未成年人模式密码页面。 |

建议开发者组合使用[应用与系统联动切换未成年人模式](account-system-minorsprotection.md)、[应用内开启未成年人模式](account-app-turn-on-minorsprotection.md)、[关闭应用的未成年人模式](account-appself-turn-off-minorsprotection.md)章节，构建应用的未成年人模式。

未成年人模式详细接入体验可参考Account Kit提供的[SampleCode示例工程](https://gitcode.com/HarmonyOS_Samples/accountkit-samplecode-clientdemo-arkts)。

说明

1. 开发者可在“设置 > 健康使用设备”中点击“开启未成年人模式”按钮，进行开启未成年人模式。
2. 根据《中华人民共和国未成年人保护法》、《中华人民共和国网络安全法》、《中华人民共和国个人信息保护法》、《未成年人网络保护条例》、《移动互联网未成年人模式建设指南》等相关法规及文件，为强化未成年人网络保护，华为提供“未成年人模式”，为未成年人营造安全健康的网络环境。
3. 与系统联动后，**建议应用将模式名称变更为“未成年人模式”**，便于用户理解。
4. 与系统联动后，如应用自动将未成年人模式开启状态同步至其它终端，可能导致用户无法在其它终端上关闭未成年人模式，应用需充分考虑该场景下的用户体验。

## 约束与限制

1. 未成年人模式支持Phone、Tablet、PC/2in1设备。并且从5.1.1(19)版本开始，新增支持TV设备。
2. 以下场景暂不支持开启或关闭未成年人模式：

   1. 系统版本低于HarmonyOS NEXT/5.0.x版本。
   2. 系统登录的账号是海外华为账号。
   3. 当系统切换至隐私空间。

说明

针对上述场景，建议先调用[canIUse](../harmonyos-references/syscap.md#判断-api-是否可以使用)接口和[supportMinorsMode](../harmonyos-references/account-api-minorsprotection.md#supportminorsmode)接口来判断当前设备环境是否支持系统的未成年人模式，否则在不支持的设备环境上调用未成年人模式相关接口，可能会造成程序崩溃：

1. 当[canIUse](../harmonyos-references/syscap.md#判断-api-是否可以使用)接口和[supportMinorsMode](../harmonyos-references/account-api-minorsprotection.md#supportminorsmode)接口返回均为true时，表明该设备支持系统的未成年人模式，应用可通过本章节描述的相关能力，与系统进行未成年人模式联动。
2. 当[canIUse](../harmonyos-references/syscap.md#判断-api-是否可以使用)接口或[supportMinorsMode](../harmonyos-references/account-api-minorsprotection.md#supportminorsmode)接口返回为false时，表明该设备暂未支持系统的未成年人模式以及相关联动能力，应用需构建自己的未成年人模式或关闭应用的未成年人模式入口。

## 接入规范

应用在接入未成年人模式时，需要遵循以下规范：

1. 当应用接入未成年人模式后，开发者需要在应用中声明已经支持未成年人模式：

   通过在工程中entry模块的module.json5文件中module属性下配置metadata字段并且配置minors\_mode值为"1"，表示当前应用已接入未成年人模式，如果开发者没有配置相关字段，或配置值不为"1"，则表示该应用不支持未成年人模式，当系统开启未成年人模式时，不支持未成年人模式的应用会被默认禁用。

   json "module": { "name": "<name>", "type": "entry", "description": "<description>", "mainElement": "<mainElement>", "deviceTypes": [], "pages": "<pages>", "abilities": [], "metadata": [ { "name": "minors\_mode", "value": "1" } ], "extensionAbilities": [] }

   > **注意：**

   >

   > 1. 开发者如果声明应用支持未成年人模式，则建议接入系统提供的未成年人模式，跟随系统状态进行切换，并提供适龄内容。不能随同系统切换而切换的，应用责任自负。开发者需确保应用提供的未成年人模式内容符合相关法律法规及监管要求。因违反规定而导致的一切后果由开发者自行负责。

   >

   > 2. 如果开发者修改过该应用在健康使用设备中的管控规则，则以修改过的最新规则为准。
2. 应用需主动跟随系统切换未成年人模式的状态。（用户操作关闭应用的未成年人模式场景除外）
3. 开发者需为未成年人提供分龄内容服务，并打造专属内容池，获取系统中未成年人的年龄段信息作为分级依据，推荐适龄内容，保障未成年人接触的信息内容适龄，同时应用也需屏蔽未成年人不可使用的功能。

   示例：应用A查询或订阅到了系统未成年人模式已开启，且未成年人模式的年龄段为3周岁及以上不满8周岁，则应用A自动切换至未成年人模式，并向未成年人用户推荐适合3周岁及以上不满8周岁年龄段的适龄内容，并屏蔽不适龄的功能。

## 用户体验设计

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/SezGjG2QR5W3q7TehEEWkQ/zh-cn_image_0000002583478759.png?HW-CC-KV=V1&HW-CC-Date=20260427T234801Z&HW-CC-Expire=86400&HW-CC-Sign=572FEDCE0E69D1EAE1C6436F1BD039BB95B3D80ECC433910E1864BC5CDD294F2 "点击放大")

当应用开启未成年人模式后，建议应用主页样式参考以上UX设计，保障用户体验的一致性。
