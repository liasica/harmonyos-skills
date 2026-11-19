---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ime-kit-security
title: 输入法安全模式介绍
breadcrumb: 指南 > 应用框架 > IME Kit（输入法开发服务） > 输入法安全模式介绍
category: harmonyos-guides
scraped_at: 2026-11-19T09:47:57+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:7f842c6ad1b8fa5b79cca17a11a88c46122237bc3ff243cfe8c9f3789fe99653
---

为了保护用户数据安全，系统增加了输入法安全模式功能，包括基础模式和完整体验模式。在基础模式下，输入法扩展无法调用任何可能涉及访问或泄漏用户隐私数据的系统能力；而在完整体验模式下，则没有该限制。

用户可以在设置应用中切换基础模式和完整体验模式。

## 基础模式介绍

1. 基础模式下，输入法扩展（InputMethodExtensionAbility）进程无法拉起其他UIAbility或ExtensionAbility。
2. 基础模式下，输入法扩展会受到系统管控，不能使用涉及访问或泄漏用户个人数据的各种接口，同时无法将数据传递出进程。管控功能包括但不限于：网络、短信、电话、麦克风、定位、相机、蓝牙、壁纸、支付、日历、游戏、扬声器、Wi-Fi、剪切板、多媒体、联系人、公共事件、系统账号、健康数据、地图服务、推送服务、融合搜索、共享内存、分布式特性、广告设备标识、振动等。
3. 基础模式下，输入法扩展可以使用基础输入功能必要的系统能力，例如，IME Kit、ArkUI、窗口、图形、屏幕管理等。
4. 基础模式下，输入法扩展对[共享沙箱](ime-kit-security.md#共享沙箱介绍)只读，对输入法扩展独立沙箱可读写；应用主入口可以对[共享沙箱](ime-kit-security.md#共享沙箱介绍)及其独立沙箱读写。

## 完整体验模式介绍

1. 完整体验模式下，输入法扩展不受基础模式相关限制，例如可以拉起其他UIAbility或ExtensionAbility、以调用访问用户数据的接口等。
2. 完整体验模式下，输入法扩展可以对[共享沙箱](ime-kit-security.md#共享沙箱介绍)读写。

## 开发指导

[onCreate](../harmonyos-references/js-apis-inputmethod-extension-ability.md#oncreate)在输入法扩展的 [onCreate](../harmonyos-references/js-apis-inputmethod-extension-ability.md#oncreate)生命周期回调函数中通过[getSecurityMode](../harmonyos-references/js-apis-inputmethodengine.md#getsecuritymode11)接口查询当前输入法应用的安全模式。

* 如果当前处于基础模式，开发者需要调整内部功能的呈现情况，以避免出现功能不可用的情况。
* 当处于完整体验模式时，开发者可以使用访问用户数据的接口，但这些接口的使用仅限于提升输入法的用户体验。

为了确保输入法功能的稳定性，开发者应当在基础模式下仅使用与基础输入功能相关的能力，并且不得试图绕过系统机制将数据传递到输入法扩展之外。

## 共享沙箱介绍

1. 输入法扩展使用独立沙箱，与应用主入口不可互相访问对方的独立沙箱。
2. 为方便输入法扩展和应用主入口之间数据传递和共享，提供了共享沙箱机制。输入法扩展和应用主入口都能够访问共享沙箱。

   **图1** 共享沙箱

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/_NQJLTp-T-iIxXOJPdM48Q/zh-cn_image_0000002791725618.png?HW-CC-KV=V1&HW-CC-Date=20261119T014757Z&HW-CC-Expire=31536000000&HW-CC-Sign=DCEF3B229E340BC9B290DF589158BBC7BF089776D1A475353278CB0BB484D72A)
3. 共享沙箱的配置流程。

   当应用主入口的[profile](../app/agc-help-add-releaseprofile-0000001914714796.md)和输入法扩展的[dataGroupIds](module-configuration-file.md#extensionabilities标签)中包含相同的data-group-id时，他们就可以使用这个data-group-id对应的共享沙箱。

   为了使用共享沙箱，需要先申请一个data-group-id，并将其分别配置到应用主入口的[profile](../app/agc-help-add-releaseprofile-0000001914714796.md)和输入法扩展的[dataGroupIds](module-configuration-file.md#extensionabilities标签)中。申请与配置流程如下：

   1. 审核规则。

      1. 输入法应用安装至系统后，在系统“设置 > 系统 > 输入法”的输入法列表中可以显示该应用。
      2. InputMethodExtensionAbility所在的module.json5配置信息中，该ability在[extensionAbilities标签](module-configuration-file.md#extensionabilities标签)下配置的type字段应为inputMethod。
   2. 申请步骤。

      1. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)，选择“APP与元服务”，选择要配置的应用，在应用信息中[配置应用分类、标签](../doccenter-submission/agc-help-release-app-class-tag-0000002271695234.md)为工具、输入法。

         ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ac/v3/Gh6QSJkSR0aZ3LCT_zLDtQ/zh-cn_image_0000002791565646.png?HW-CC-KV=V1&HW-CC-Date=20261119T014757Z&HW-CC-Expire=31536000000&HW-CC-Sign=488B1D5DF90C780E94BD61C71A7C9B18FD2807FB4550E859486492A9641FC671)
      2. 选择“开发与服务”，在项目列表选择项目，并在应用列表下选择需要申请共享沙箱的应用。
      3. 进入“项目设置 > 开放能力管理”页面，点击“输入法应用内数据共享”对应的“申请”。

         ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/LluFAZJ5S6SpocN2IlHCPQ/zh-cn_image_0000002820525599.png?HW-CC-KV=V1&HW-CC-Date=20261119T014757Z&HW-CC-Expire=31536000000&HW-CC-Sign=A54165185D7874E7D78EC61E2B8DC17255D32E8E664A5D9662B8197D075ECA5B)
      4. 参考“申请原因”中的模板，提供申请必需的相关信息，包括应用名称、应用appId、开发者Id，并参考样例提供附件材料，然后点击“提交”按钮。

         ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/MjKccB5eRy23COxq2obZOg/zh-cn_image_0000002820405599.png?HW-CC-KV=V1&HW-CC-Date=20261119T014757Z&HW-CC-Expire=31536000000&HW-CC-Sign=D424D956A35E3AD32E01C434047810C6734C191AFCCAEFCA033FEA57B85C0130)

         返回“开放能力管理”页面，原“申请”变为“申请中”，1~3个工作日内反馈申请结果，请留意互动中心的“服务开通申请”信息。

         ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/2jS-kewCRxKlI_28SiwHig/zh-cn_image_0000002791725620.png?HW-CC-KV=V1&HW-CC-Date=20261119T014757Z&HW-CC-Expire=31536000000&HW-CC-Sign=5EE63D8712179B44319F18496C51C2BA027D8B93C7C9608A252A87BFBB4E5C1D)

         申请通过后，互动中心会发送通知给您，“申请中”会变为置灰显示的“申请”，同时，您将收到一个data-group-id。

         ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/OsJr0IkKR4GzNtx-TEijBA/zh-cn_image_0000002791565648.png?HW-CC-KV=V1&HW-CC-Date=20261119T014757Z&HW-CC-Expire=31536000000&HW-CC-Sign=E4D2C62A93D3D531EBA83CCBD6400CFB9BFF93BFBBE6337BB917E0F4EED8F373)
   3. 待您收到data-group-id申请成功的回复后，重新生成[应用的profile](../app/agc-help-add-releaseprofile-0000001914714796.md)，新生成的profile里面包含本次申请到的data-group-id；并使用DevEco Studio[配置工程的签名信息](ide-publish-app.md#section945904791115)，将新的profile配置到工程中。
   4. 将您本次申请获取到的data-group-id，配置到InputMethodExtensionAbility所在的module.json5中的[dataGroupIds](module-configuration-file.md#extensionabilities标签)中。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/ti1kGkt_TCqhF_2IrB_wWw/zh-cn_image_0000002820525601.png?HW-CC-KV=V1&HW-CC-Date=20261119T014757Z&HW-CC-Expire=31536000000&HW-CC-Sign=10602354299B208130508B834E64FB6550D798961A5EDB7AF2A10580795CA970)
4. 共享沙箱使用流程。

   a. 分别在输入法扩展和应用主入口通过[getGroupDir](../harmonyos-references/js-apis-inner-application-context.md#getgroupdir10)获取共享沙箱路径。

   **说明** 

   接口入参dataGroupID应该填写您本次申请到的data-group-id。

   b. 如果接口调用成功，且能够返回共享沙箱路径，说明您申请并配置的data-group-id已生效，此时您可通过共享沙箱在应用主入口和输入法扩展之间进行数据共享。

   **说明** 

   基础模式下输入法扩展对共享沙箱是只读权限，不可写入数据；完整体验模式下可读写。
