---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-debug-device
title: 调试概述
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 应用调试 > 调试概述
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:029852d2563ccc482eb8329df5a41eab4fd43f392c4aac8045d10e57f0474241
---

鸿蒙电脑DevEco Studio提供了丰富的HarmonyOS应用/元服务调试能力，支持JS、ArkTS、C/C++调试，帮助开发者更方便、高效地调试应用/元服务。

HarmonyOS应用/元服务调试支持使用本机、真机设备、多设备预览器调试。接下来以使用真机设备为例进行说明，详细的调试流程如下图所示。关于本机和多设备预览器的调试请参考[使用本地真机运行应用](ide-hmos-run-device.md)和[使用多设备预览器运行应用](ide-hmos-run-previewer.md)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/2irYVGi3RtOCkzng2fCiRw/zh-cn_image_0000002781311196.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=39CB80DCE18E356B91662DE7B40C90652BA2EF307E0466FCD50A842ABC58A248)

1. [配置签名信息](ide-hmos-signing.md)：使用真机设备进行调试前需要对HAP进行签名。
2. [设置调试代码类型](ide-hmos-run-debug-configurations.md#section1170735241213)：调试类型默认为Detect Automatically**。**
3. [设置HAP安装方式](ide-hmos-run-debug-configurations.md#section531811771410)：选择先卸载应用/元服务后再重新安装或覆盖安装。
4. [启动调试](ide-hmos-debug-arkts-debug.md)：启动debug调试或attach调试。
