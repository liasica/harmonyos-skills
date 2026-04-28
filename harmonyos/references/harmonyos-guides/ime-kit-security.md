---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ime-kit-security
title: 输入法安全模式介绍
breadcrumb: 指南 > 应用框架 > IME Kit（输入法开发服务） > 输入法安全模式介绍
category: harmonyos-guides
scraped_at: 2026-04-28T07:41:37+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:3fd803dba156d960a99be2375892260e4d8ceef1c7d6559e7a037b26c9aa4208
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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/SxTed27FTnK-lH8OsC-uxQ/zh-cn_image_0000002552798668.png?HW-CC-KV=V1&HW-CC-Date=20260427T234136Z&HW-CC-Expire=86400&HW-CC-Sign=72786A11CE842CF896F549F7658160A45AD4902DED0967006F15A934FC31C54D)
3. 共享沙箱的配置流程。

   当应用主入口的[profile](../app/agc-help-add-releaseprofile-0000001914714796.md)和输入法扩展的[dataGroupIds](module-configuration-file.md#extensionabilities标签)中包含相同的data-group-id时，他们就可以使用这个data-group-id对应的共享沙箱。

   为了使用共享沙箱，需要先申请一个data-group-id，并将其分别配置到应用主入口的[profile](../app/agc-help-add-releaseprofile-0000001914714796.md)和输入法扩展的[dataGroupIds](module-configuration-file.md#extensionabilities标签)中。具体流程如下：

   1. 申请data-group-id，申请流程如下。

      1. 按照如下格式发送邮件到agconnect@huawei.com。
         1. 邮件标题格式：【输入法应用申请应用内数据共享】xxx应用
         2. 邮件内容：

            应用appid：xxx

            应用名称：xxx

            开发者id：xxx

            邮件附件中提供：

            ①输入法应用安装至系统后，在设置的输入法列表中显示该应用的截图。

            ②输入法应用中module.json5文件的InputMethodExtensionAbility相关配置截图。
      2. 我们收到邮件后，3个工作日内会答复审核结果。
   2. 待您收到data-group-id申请成功的邮件回复后，重新生成[应用的profile](../app/agc-help-add-releaseprofile-0000001914714796.md)，新生成的profile里面包含本次申请到的data-group-id；并使用DevEco Studio[配置工程的签名信息](ide-publish-app.md#section280162182818)，将新的profile配置到工程中。
   3. 按照data-group-id申请成功的回复邮件指导，获取到您本次申请到的data-group-id，并在InputMethodExtensionAbility所在的module.json5中配置[dataGroupIds](module-configuration-file.md#extensionabilities标签)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/IqA-GgUXTL2AFysMDs4SqQ/zh-cn_image_0000002583438363.png?HW-CC-KV=V1&HW-CC-Date=20260427T234136Z&HW-CC-Expire=86400&HW-CC-Sign=62827226649053EC47ED94D7E13BB3A42466B47FEA732FB28F143283C4C2B958)
4. 共享沙箱使用流程。

   a. 分别在输入法扩展和应用主入口通过[getGroupDir](../harmonyos-references/js-apis-inner-application-context.md#getgroupdir10)获取共享沙箱路径。

   说明

   接口入参dataGroupID应该填写您本次申请到的data-group-id。

   b. 如果接口调用成功，且能够返回共享沙箱路径，说明您申请并配置的data-group-id已生效，此时您可通过共享沙箱在应用主入口和输入法扩展之间进行数据共享。

   说明

   基础模式下输入法扩展对共享沙箱是只读权限，不可写入数据；完整体验模式下可读写。
