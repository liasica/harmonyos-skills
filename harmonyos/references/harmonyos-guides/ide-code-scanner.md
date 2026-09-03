---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-scanner
title: Code Scanner代码检查
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Scanner代码检查
category: harmonyos-guides
scraped_at: 2026-09-04T06:27:15+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:4fed652519303c71750e0b3e74b2d559bc0d8a2a4e05e0e755edfbba31431c92
---

从26.0.0版本开始，DevEco Studio新增Code Scanner功能，用于检查整个项目的资源泄漏问题。开发者可根据扫描结果中的告警提示，手动修复代码缺陷，在代码开发阶段，确保代码质量。

## 操作步骤

1. 在菜单栏点击**Code > Code Scanner >** **Config**，勾选所需的扫描规则，扫描规则包括ARKTS和CPP两种。

   点击扫描规则名称可在右侧查看规则功能描述和**Code Example**（包括正例和反例），可根据其中的建议修改工程代码，在**Severity**处可设置规则的告警级别（error，warn，fatal），默认为**error**。

   勾选和设置完成后，点击**OK**保存规则配置，或点击**Save and Run**保存规则配置并开始代码扫描。

   **说明** 

   * 对于ArkTS工程，需勾选ARKTS下的扫描规则；对于C++工程，需勾选CPP下的扫描规则。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/33/v3/7kRHBKIOSaSUCLtkXpTArw/zh-cn_image_0000002731541919.png)
2. 在菜单栏点击**Code > Code Scanner >** **Scan**，开始全量代码扫描。
3. 扫描完成后，在底部工具面板查看检查结果。

   Severity统计了所有告警数量，点击**All**、**Fatal**、**Error**、**Warn**可分别查看对应告警级别的具体信息。点击**Filter by scene**下拉菜单，可以筛选不同规则的检查结果。单击告警文件可以查看告警信息和对应配置的规则。双击某条告警结果，可以跳转到对应代码缺陷位置；选中告警结果时，可以在右侧Execution Trace窗口查看告警原因和问题的来源到问题的发生点的可能的执行流。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/iV3e2oL9RT-XdgUimJraFA/zh-cn_image_0000002701822650.png)
