---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-project-management-37
title: 使用了新API打包的APP包如何兼容安装在老系统和其他不兼容该API的设备
breadcrumb: FAQ > DevEco Studio > 工程管理 > 使用了新API打包的APP包如何兼容安装在老系统和其他不兼容该API的设备
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:53+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:7b72f9cc191e125da508f25079cece93653da65ce1efe6fbdb400b195272a5f0
---

## 问题现象

应用使用了新的API，如6.0.0(20)的hdsEffect，根据“一次开发，多端部署”规范，将手机/平板/电脑/手表打包进同一个APP内供上架审核。

1. 在同一个APP包中只能有一个targetSdkVersion和compatibleSdkVersion，直接修改compatibleSdkVersion为17/18/19版本会导致应用闪退。
2. 若手表等设备不支持该API，则应用分发到手表后也会导致无法使用。

## 背景知识

1. [影响应用兼容性的关键信息](../harmonyos-releases/app-compatibility-influence-factor.md)：
   * compileSdkVersion：编译应用的SDK版本。
   * targetSdkVersion：应用运行的目标SDK版本。
   * compatibleSdkVersion：应用运行的最低SDK版本。

   在应用的工程配置中，三个SDK版本属性之间的大小关系为：compatibleSdkVersion值≤targetSdkVersion值≤compileSdkVersion值，如果配置不符合这个规则，会有报错提示。
2. [应用和设备系统兼容性原则说明](../harmonyos-releases/app-compatibility-intro.md#section144051257332)：
   * 基于老版本HarmonyOS SDK开发的应用，在上架华为应用市场后，默认可分发到新版本的HarmonyOS设备，并正常运行。

     例外情况：API在不断演进迭代过程中，因体验优化或安全等因素，可能会发生行为变更，并对已上架应用产生影响，针对这部分变更会专门在版本说明中详细阐述，请开发者在升级API版本时候，关注版本说明。
   * 针对基于新版本HarmonyOS SDK开发的应用，使用了新版本API，开发者对这些新版本API进行兼容性判断保护后，应用在老HarmonyOS设备上使用新API部分功能降级，并运行正常。
3. [什么是SystemCapability（SysCap）](../harmonyos-references/syscap.md#什么是systemcapabilitysyscap)：
   * SysCap，全称SystemCapability，即系统能力，指操作系统中每一个相对独立的特性，如蓝牙，WIFI，NFC，摄像头等，都是系统能力之一。
   * HarmonyOS定义了API接口canIUse[判断SysCap是否可调用](../harmonyos-references/syscap.md#使用caniuse判断syscap是否可调用)，帮助开发者来判断该设备是否支持某个特定的SysCap。

## 解决方案

1. 配置build-profile.json5设置[应用开发过程使用的SDK版本](../harmonyos-releases/app-compatibility-influence-factor.md#section99881928838)：

   假如应用使用并适配了API版本6.0.0(20)，同时希望应用能够运行5.0.5(17)，那么可以在应用工程的build-profile.json5文件中设置“targetSdkVersion": "6.0.0(20)”，“compatibleSdkVersion": "5.0.5(17)”。
2. [通过distributionOSApiVersion和sdkApiVersion接口消除](../harmonyos-releases/arkts-api-compatibility-warning-elim.md)：

   假如某个新特性的API是在SDK版本6.0.0(20)提供，为了让应用兼容在基于API版本5.0.5(17)的老设备正常运行，开发者可以使用如下兼容性判断。

   * 针对HarmonyOS设备独有特性接口，即接口标记为since M.F.S(N)（文档中标记“起始版本：M.F.S(N)”, SDK物理包中hms路径下所包含的接口），使用distributionOSApiVersion接口进行兼容性判断保护。例如判断“deviceInfo.distributionOSApiVersion >= 60000”时，调用6.0.0(20)的API新接口，否则使用降级方案，其中“60000”是由新接口的since字段“M\*10000+F\*100+S”转换而来，即60000=6\*10000+0\*100+0。
   * 针对OpenHarmony底座接口，即接口标记为since N（文档中标记“起始版本：N”，SDK物理包中openharmony路径下所包含的接口），使用sdkApiVersion接口进行兼容性判断保护。例如判断“deviceInfo.sdkApiVersion >= 20”时，调用6.0.0(20)的API新接口，否则使用降级方案。
3. [使用canIUse判断SysCap是否可调用](../harmonyos-references/syscap.md#使用caniuse判断syscap是否可调用)：

   HarmonyOS定义了API接口canIUse帮助开发者来判断该设备是否支持某个特定的SysCap。
   * 查询[hdsEffect](../harmonyos-references/ui-design-hdseffect.md)接口的API文档，查出其系统能力为“SystemCapability.UIDesign.HDSComponent.Core”；
   * 通过判断“canIUse('SystemCapability.UIDesign.HDSComponent.Core')”检查该设备是否可以使用hdsEffect接口。

## 总结

通过build-profile.json5可以配置APP运行的目标SDK版本和运行要求的最低SDK版本，通过deviceInfo.distributionOSApiVersion或deviceInfo.sdkApiVersion接口帮助开发者进行API兼容性判断保护，通过canIUse接口帮助开发者来判断该设备是否支持某个特定的SysCap。
