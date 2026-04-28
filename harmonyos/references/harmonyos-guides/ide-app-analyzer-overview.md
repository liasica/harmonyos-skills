---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-app-analyzer-overview
title: 体检概述
breadcrumb: 指南 > 编写与调试应用 > 开发自测试 > 应用与元服务体检 > 体检概述
category: harmonyos-guides
scraped_at: 2026-04-28T07:57:03+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:2e966f7179310119d232f962d5d149024affc7a7d9482fb46577bb6e95a0d6a0
---

DevEco Studio提供了应用与元服务体检工具AppAnalyzer，用于对应用和元服务进行本地测试体检，并给出体检报告、分析指导以及修改建议，帮助开发者提升应用与元服务质量。在体检过程中，工具会收集应用或元服务的trace信息、代码栈、内存快照以及应用或元服务页面的截屏，并保存在本地工程目录.appanalyzer下，帮助开发者快速进行问题分析定位。

开发者可以通过DevEco Studio连接本地设备，自主遍历HarmonyOS应用或元服务的功能，快速进行自测试，查看测试结果。

如果没有本地设备，从DevEco Studio 6.1.0 Beta2版本开始，可以通过[云测试](../app/agc-help-cloudtest-introduction-0000002255036400.md)选择远程真机进行体检。在AppAnalyzer上进行云测试时，操作步骤和其他体检模式类似，仅需将设备改为远程真机。

当前支持以下体检模式。

* **场景化体检**：支持页面滑动、页面间转场、冷启动、UX多设备适配等多种测试场景，开发者可以基于实际的应用场景进行测试，具体请参考[场景化体检](ide-app-analyzer-scenes.md)。

* **规则体检**：支持兼容性、性能、功耗等多种测试类型，开发者可自主选择不同的规则进行测试，具体请参考[规则体检](ide-app-analyzer-rules.md)。
* **上架前体检**：针对上架阻塞问题进行快速检测，提前发现可能影响上架的问题，检测完成之后可以上传检测结果，用于应用市场上架参考，提升上架效率，具体请参考[上架前体检](ide-app-analyzer-before-appgallery.md)。该功能从DevEco Studio 6.0.0 Beta1版本开始支持。
* **上架合规体检**：针对AppGallery应用的上架合规要求进行检测，提前发现需要重点关注的合规事项，了解应做和不应做的事项，避免常见误区，具体请参考[上架合规体检](ide-app-analyzer-ag-policy.md)。该功能从DevEco Studio 6.1.0 Beta1版本开始支持。

以上体检模式都是在AppAnalyzer中进行测试并生成体检报告，从DevEco Studio 6.0.0 Beta3版本开始，支持在DevEco Testing中进行[性能基础质量测试](specialized-testing.md#section12324184817324)或[场景化性能测试](specialized-testing.md#section8642101711299)生成检测报告后，导入到AppAnalyzer进行诊断和分析，获得可能的故障原因并生成体检报告，具体请参考[导入DevEco Testing的检测报告进行诊断](ide-app-analyzer-testing.md)。

## 使用约束

### 支持的设备

| 能力 | 支持设备 | 备注 |
| --- | --- | --- |
| [功能兼容性](ide-app-analyzer-all-rules.md#section202813103565)的部分规则 | API 20及以上的双折叠手机 | - |
| 规则体检下的[UX测试](ide-app-analyzer-all-rules.md#section68461625141414) | * API 20及以上的双折叠、三折叠手机和模拟器 * API 20及以上的Pura X Max手机和模拟器 | 从DevEco Studio 6.0.2 Beta1版本开始，支持三折叠模拟器。  从DevEco Studio 6.1.0 Release版本开始，支持双折叠模拟器。 |
| 场景化体检下的[多设备测试](ide-app-analyzer-scenes.md#section15619191841215) |
| 云测试 | 远程真机 | 如果没有本地设备，从DevEco Studio 6.1.0 Beta2版本开始，支持选择远程真机进行云测试，关于云测试的介绍、支持测试的范围请参考[云测试](../app/agc-help-cloudtest-introduction-0000002255036400.md)。  在AppAnalyzer上进行云测试时，操作步骤和其他体检模式类似，仅需将设备改为远程真机，具体可参考[场景化体检](ide-app-analyzer-scenes.md)。  AppAnalyzer会将APP包上传至AppGallery，测试完成后，可在[历史报告](ide-app-analyzer-history-reports.md)中查看检测结果，报告的内容请参考[查看测试报告](../app/agc-help-cloudtest-viewreport-0000002289646669.md)。 |
| 其他能力 | 直板机 | - |

### 支持的国家/地区

仅支持在中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）使用。
