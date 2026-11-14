---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-debug-device
title: 调试概述
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 应用调试 > 调试概述
category: harmonyos-guides
scraped_at: 2026-11-14T08:49:16+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:4898a94fa6b4e37717efe65a73bf61e028cd38f600ff2fafd578c48598550022
---

鸿蒙电脑DevEco Studio提供了丰富的HarmonyOS应用/元服务调试能力，支持JS、ArkTS、C/C++调试，帮助开发者更方便、高效地调试应用/元服务。

HarmonyOS应用/元服务调试支持使用本机、真机设备、多设备预览器调试。接下来以使用真机设备为例进行说明，详细的调试流程如下图所示。关于本机和多设备预览器的调试请参考[使用本地真机运行应用](ide-hmos-run-device.md)和[使用多设备预览器运行应用](ide-hmos-run-previewer.md)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/gLZWQ041RDCgp-6lNKy8sQ/zh-cn_image_0000002781311196.png?HW-CC-KV=V1&HW-CC-Date=20261114T004727Z&HW-CC-Expire=31536000000&HW-CC-Sign=3E466DA77754E16DF4A427C28C6AB674C2C61B7849F00912A63D48E1BD67ABEA)

1. [配置签名信息](ide-hmos-signing.md)：使用真机设备进行调试前需要对HAP进行签名。
2. [设置调试代码类型](ide-hmos-run-debug-configurations.md#section1170735241213)：调试类型默认为Detect Automatically**。**
3. [设置HAP安装方式](ide-hmos-run-debug-configurations.md#section531811771410)：选择先卸载应用/元服务后再重新安装或覆盖安装。
4. [启动调试](ide-hmos-debug-arkts-debug.md)：启动debug调试或attach调试。
