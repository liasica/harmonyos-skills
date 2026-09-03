---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-debug-device
title: 调试概述
breadcrumb: 指南 > 编写与调试应用 > 应用调试 > 调试概述
category: harmonyos-guides
scraped_at: 2026-09-04T06:27:16+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:b533028e31df9f1900452bbecaa8a19e6edbddbda1d6c8b7564f4c2cad3ce354
---

DevEco Studio提供了丰富的HarmonyOS应用/元服务调试能力，支持JS、ArkTS、C/C++单语言调试和ArkTS/JS+C/C++跨语言调试能力，并且支持三方库源码调试，帮助开发者更方便、高效地调试应用/元服务。

HarmonyOS应用/元服务调试支持使用真机设备、模拟器、预览器调试。接下来以使用真机设备为例进行说明，详细的调试流程如下图所示。关于模拟器和预览器的调试请参考[使用模拟器运行应用](ide-run-emulator.md)和[使用预览器调试应用](ide-previewer-debug.md)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/-e0dYx2WQBqinU5GYIsyDA/zh-cn_image_0000002731382373.png)

1. [配置签名信息](ide-signing.md)：使用真机设备进行调试前需要对HAP进行签名。
2. [设置调试代码类型](ide-run-debug-configurations.md#section1170735241213)：调试类型默认为Detect Automatically**。**
3. [设置HAP安装方式](ide-run-debug-configurations.md#section531811771410)：选择先卸载应用/元服务后再重新安装或覆盖安装。
4. [启动调试](ide-debug-arkts-debug.md)：启动debug调试或attach调试。
