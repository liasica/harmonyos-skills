---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-debug-device
title: 调试概述
breadcrumb: 指南 > 编写与调试应用 > 应用调试 > 调试概述
category: harmonyos-guides
scraped_at: 2026-04-28T07:56:44+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:78f00ff5e68ba5f3cf527f5896b696abef3f9b3ce1576c909de8b861dc2e48e2
---

DevEco Studio提供了丰富的HarmonyOS应用/元服务调试能力，支持JS、ArkTS、C/C++单语言调试和ArkTS/JS+C/C++跨语言调试能力，并且支持三方库源码调试，帮助开发者更方便、高效地调试应用/元服务。

HarmonyOS应用/元服务调试支持使用真机设备、模拟器、预览器调试。接下来以使用真机设备为例进行说明，详细的调试流程如下图所示。关于模拟器和预览器的调试请参考[使用模拟器运行应用](ide-run-emulator.md)和[使用预览器调试应用](ide-previewer-debug.md)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/jq3IgRUGTj-fvNBqIoAb1Q/zh-cn_image_0000002561753041.png?HW-CC-KV=V1&HW-CC-Date=20260427T235644Z&HW-CC-Expire=86400&HW-CC-Sign=9766AB867603ACDFED27EA11FCC1CCE0398BE69C40D8690C1006CD2D2E8F3CA9)

1. [配置签名信息](ide-signing.md)：使用真机设备进行调试前需要对HAP进行签名。
2. [设置调试代码类型](ide-run-debug-configurations.md#section1170735241213)：调试类型默认为Detect Automatically**。**
3. [设置HAP安装方式](ide-run-debug-configurations.md#section531811771410)：选择先卸载应用/元服务后再重新安装或覆盖安装。
4. [启动调试](ide-debug-arkts-debug.md)：启动debug调试或attach调试。
