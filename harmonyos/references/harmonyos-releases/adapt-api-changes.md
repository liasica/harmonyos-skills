---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/adapt-api-changes
title: 评估API版本变化的影响并适配
breadcrumb: 版本说明 > 应用升级适配指导-向6.0.0(20)升级 > 评估API版本变化的影响并适配
category: harmonyos-releases
scraped_at: 2026-04-29T13:25:23+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:86e89b841e1c8a3b709a7e660f4fe715daf574def3086313dc0276473ac27227
---

DevEco Studio升级到6.0.0(20)配套版本后，如果应用工程中未显式配置[targetSdkVersion](../harmonyos-guides/ide-hvigor-build-profile-app.md#section45865492619)版本，targetSdkVersion版本会同步升级为6.0.0(20)。同时，编译应用默认使用的[compileSdkVersion](../harmonyos-guides/ide-hvigor-build-profile-app.md#section45865492619)也将会同步升级为6.0.0(20)，如果希望应用兼容老版本SDK，可通过compatibleSdkVersion配置能够兼容的最低SDK版本，此时需要注意高于应用运行设备ROM的SDK版本的API需要进行版本判断以便保证应用运行正常，详情请阅读[应用开发中的兼容性场景开发指导](app-compatibility-scenarios.md)。

由于默认使用的SDK版本发生了变更，开发者在升级后需要对API的行为变更进行评估，确认是否对应用的兼容性产生了影响。部分API的行为变更可能会通过targetSdkVersion字段进行API版本隔离，以便提供前向兼容手段，详情请阅读[应用兼容性说明](app-compatibility.md)。

对于具体的API行为变更对应用带来的影响，开发者可通过以下两种手段来识别，并参考变更说明文档进行适配。

## 通过DevEco Studio的API变更助手检测

开发者可以通过DevEco Studio的API变更助手查看当前工程中使用到的ArkTS API/C API是否存在行为变更，并根据工具提供的适配指导链接完成工程代码适配修改。步骤如下：

1. 在DevEco Studio菜单栏点击“**Tools > API Change Assistant**”打开API变更助手，此时编辑区下方的API Change Assistant页签中，支持按模块查看API变更情况。选择需要对比的SDK版本号范围，点击**Start Scan**开始扫描。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/hbmJxdPURuqeiSCrcOxOHQ/zh-cn_image_0000002428969272.png?HW-CC-KV=V1&HW-CC-Date=20260429T052522Z&HW-CC-Expire=86400&HW-CC-Sign=869BDFF1AE937E3110340DAD290B3230C42F281676811AA1B117676861518FBC)
2. 扫描完成将展示当前工程中使用的API是否在选择比较的SDK版本之间发生行为变更。点击Code Location中的代码地址，跳转到相应的代码编写位置；如需更多指导，可点击Guidance link中的链接，跳转至版本说明文档中查看详情。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/5yoLs2ckQ5-FUUsGlDDrhA/zh-cn_image_0000002429129228.png?HW-CC-KV=V1&HW-CC-Date=20260429T052522Z&HW-CC-Expire=86400&HW-CC-Sign=9E192BB022B0E1BAF2B9B633346F11AE99A3D2F36E99D143229FED294FD1A0BD)
3. 点击**Export**，选择API变更的存放位置后导出变更数据；点击**Scan Again**可重新进行扫描。通过右侧Setting按钮，可以设置在扫描API时，可使用的最大堆内存的大小，默认值为3072MB，当工程代码量较大导致扫描缓慢时，可以适当调大该参数。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/qcRlGgV_RpK1HriV__U8tw/zh-cn_image_0000002454883025.png?HW-CC-KV=V1&HW-CC-Date=20260429T052522Z&HW-CC-Expire=86400&HW-CC-Sign=B61FEA6DE4B72BFA3100D506C0F0A240BDEB21174FCE2070E35C8542FE0A5CA7 "点击放大")

## 查看官网发布的全量变更

如果需要了解HarmonyOS在历次版本迭代中产生的所有变更清单，可参见[HarmonyOS行为变更汇总](../harmonyos-roadmap/all-changelogs-600.md)。
