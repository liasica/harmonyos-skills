---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/app-compatibility-intro
title: 关于应用兼容性的介绍
breadcrumb: 版本说明 > 应用兼容性说明 > 关于应用兼容性的介绍
category: harmonyos-releases
scraped_at: 2026-04-28T07:37:16+08:00
doc_updated_at: 2026-01-19
content_hash: sha256:b1853a64704d21aa04261fb9def03300e811b64b46f63501c656007c1133cdd9
---

HarmonyOS应用和元服务（为方便描述，下文简称为应用）的开发者通过开发套件所提供的HarmonyOS SDK进行功能开发，调用HarmonyOS SDK中的API来实现业务功能逻辑。终端用户从华为应用市场获取应用，并安装到终端设备的系统（即ROM）上，系统运行应用后将功能呈现给消费者。

在这一流程中，开发应用时所使用的HarmonyOS SDK版本（简称SDK版本）、运行应用的设备ROM所搭载的API版本（可在HarmonyOS设备的“设置 > 点击设备名称 > 关于本机 > API版本”中查看）、以及应用中所定义的API/SDK版本兼容信息（如编译应用的SDK版本、应用运行的目标SDK版本、应用运行的最低SDK版本等，详见[影响应用兼容性的关键信息](app-compatibility-influence-factor.md)），共同决定了应用在现网不同设备上的运行情况。

这其中，对应用兼容性起到决定因素的是API版本。API版本是贯穿开发态和运行态非常关键的信息，也是HarmonyOS能力提供者和开发者之间的纽带。

## API版本号说明

API版本取值的格式为：M.S.F(N) Stage， 其中：

* M取值为1-99，表示API大版本更新。
* S和F取值都为0-99，表示API小版本更新。
* N为OpenHarmony底座的API level，取值为1-99。
* Stage为当前SDK的发布阶段，仅在SDK的版本号中可见，取值为CanaryN/BetaN/[Release]， N为正整数，Release版本发布时可省略Release。

应用兼容性主要是通过API版本信息进行兼容性处理，下图简要说明API版本在各个环节的关键作用：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/oGUokvH5T7KzOmajaADzOg/zh-cn_image_0000002379126752.png?HW-CC-KV=V1&HW-CC-Date=20260427T233715Z&HW-CC-Expire=86400&HW-CC-Sign=5DB2B134CEC2AC13E04612B00C08C0E00D68719B076822616DD17705A1A7F65C "点击放大")

说明

本文所描述的SDK版本和API版本两者本质上是一个版本号，取值格式一致，两者配套使用。 SDK版本是提供给开发者使用的接口和工具集合；API版本是指设备侧支持的最高的API能力集合。

## 应用和设备系统兼容性原则说明

1. 基于老版本HarmonyOS SDK开发的应用，在上架华为应用市场后，默认可分发到新版本的HarmonyOS设备，并正常运行。

   例外情况：API在不断演进迭代过程中，因体验优化或安全等因素，可能会发生行为变更，并对已上架应用产生影响，针对这部分变更会专门在版本说明中详细阐述，请开发者在升级API版本时，关注版本说明。
2. 针对基于新版本HarmonyOS SDK开发的应用，使用了新版本API，开发者对这些新版本API进行兼容性判断保护后，应用在老HarmonyOS设备上使用新API部分功能降级，并运行正常。

### 示例说明

App1是基于SDK版本5.0.2(14）开发的应用，则默认可以在后续API版本为5.0.3(15)和5.0.4(16)的HarmonyOS现网设备正常运行；

App2是基于SDK版本5.0.3(15）开发的应用，并且使用了新API D， 则默认可以在后续的API版本为5.0.4(16)的HarmonyOS现网设备正常运行；但如果要在API版本为5.0.2(14)的HarmonyOS现网老设备正常运行，则开发者需对D进行条件判断保护。

App3是基于SDK版本5.0.4(16）开发的应用，并且使用了API D和E ， 默认可以在API版本为5.0.4(16)的HarmonyOS现网设备正常运行；如果要在API版本为5.0.2(14)的HarmonyOS现网老设备正常运行，则开发者需对D和E进行条件判断保护；如果要在API版本为5.0.3(15)的HarmonyOS现网老设备正常运行，则开发者需对E进行条件判断保护。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/vIReFxBCSIiQXBZUUdb3SA/zh-cn_image_0000002441209013.png?HW-CC-KV=V1&HW-CC-Date=20260427T233715Z&HW-CC-Expire=86400&HW-CC-Sign=4D01382C863FC1258CF733E5C5E1126D558EE8E3D7F1C59AEC50BD657B4EAC1A "点击放大")

本文旨在阐述应用兼容性的原理以及影响兼容性的因素，希望开发者在了解这些内容后能正确配置应用兼容性的参数，或者提前识别兼容性风险，保障终端用户的使用体验。
