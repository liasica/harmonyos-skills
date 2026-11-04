---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-realtime-check
title: 代码实时检查及快速修复
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 代码编辑 > 代码检查 > 代码实时检查及快速修复
category: harmonyos-guides
scraped_at: 2026-11-04T08:31:42+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:f2b4868b1795d7b0b7c4e82cb6688067f6c1b53b0d7ced2b5d830d668389f12a
---

## 实时检查

编辑器会实时地进行代码分析，如果输入的语法不符合编码规范，或者出现语义或语法错误，将在代码中突出显示错误或警告，将鼠标移动到错误代码处，会提示详细的错误信息。

## 代码快速修复

鸿蒙电脑DevEco Studio支持快速修复能力，辅助开发者快速修复ArkTS、C++代码或资源文件问题。

**查看告警信息：**点击编辑器底部![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/XYK0ZAx6ThaH8roJfUEnBA/zh-cn_image_0000002750169636.png)图标，打开问题工具面板。双击对应告警信息，可以查看警告的具体位置及原因。

**快速修复：**将光标放在错误警告的位置，可在弹出的悬浮窗中查看问题描述和对应修复方式。单击**更多操作**可查看更多修复方法，或是当页面出现灯泡图标时，点击图标并根据相应建议，实现代码快速修复。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/8J4teu_JQs-FQeHepmlGbw/zh-cn_image_0000002779728811.png)

### ArkTS代码快速修复使用演示

下面通过示例展示ArkTS代码中快速修复功能的使用方法。

* 光标悬浮在未引入的变量处，点击灯泡图标，在下拉菜单中选择**Add import from XXX**，完成导入语句补充。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fb/v3/5wZUzizjThy65Jtyqq-Bhg/zh-cn_image_0000002779608661.gif)
* 光标悬浮在拼写错误的变量名处，点击灯泡图标，在下拉菜单中选择**Change spelling to XXX**，自动修复拼写错误。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ca/v3/rUmvFPDSSQ6-Ggh8jszntw/zh-cn_image_0000002750169638.gif)

### .json5文件快速修复使用演示

* 在模块级build-profile.json5文件中，当输入错误的**apiType**时出现快速修复提示。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/54/v3/CwLchiXlSEer-iZANfVh9A/zh-cn_image_0000002779608659.png)
* 在工程级build-profile.json5文件中，当输入错误的**compatibleSdkVersion**版本时出现快速修复提示。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/ARicD135QRSca5ACUFvMug/zh-cn_image_0000002750009748.png)
