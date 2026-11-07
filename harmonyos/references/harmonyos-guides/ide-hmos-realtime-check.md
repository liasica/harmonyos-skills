---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-realtime-check
title: 代码实时检查及快速修复
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 代码编辑 > 代码检查 > 代码实时检查及快速修复
category: harmonyos-guides
scraped_at: 2026-11-07T08:02:33+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:a2c8acca154068f73fa07551900dfff48b070027b1d14868e931732b86080f9e
---

## 实时检查

编辑器会实时地进行代码分析，如果输入的语法不符合编码规范，或者出现语义或语法错误，将在代码中突出显示错误或警告，将鼠标移动到错误代码处，会提示详细的错误信息。

## 代码快速修复

鸿蒙电脑DevEco Studio支持快速修复能力，辅助开发者快速修复ArkTS、C++代码或资源文件问题。

**查看告警信息：**点击编辑器底部![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/Md0YVfe8Qe-ThN1APbRKqQ/zh-cn_image_0000002810750769.png)图标，打开问题工具面板。双击对应告警信息，可以查看警告的具体位置及原因。

**快速修复：**将光标放在错误警告的位置，可在弹出的悬浮窗中查看问题描述和对应修复方式。单击**更多操作**可查看更多修复方法，或是当页面出现灯泡图标时，点击图标并根据相应建议，实现代码快速修复。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/hSUhtiEeRXeoj_2LTAMWXA/zh-cn_image_0000002810630663.png)

### ArkTS代码快速修复使用演示

下面通过示例展示ArkTS代码中快速修复功能的使用方法。

* 光标悬浮在未引入的变量处，点击灯泡图标，在下拉菜单中选择**Add import from XXX**，完成导入语句补充。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ca/v3/e-DsYEwpTXCCn9NqxY2BvA/zh-cn_image_0000002781311178.gif)
* 光标悬浮在拼写错误的变量名处，点击灯泡图标，在下拉菜单中选择**Change spelling to XXX**，自动修复拼写错误。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b8/v3/4sipNqZwQsayfkhj1x3NbQ/zh-cn_image_0000002810750771.gif)

### .json5文件快速修复使用演示

* 在模块级build-profile.json5文件中，当输入错误的**apiType**时出现快速修复提示。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/bvHD-MBFSLalPhSZ4yavWA/zh-cn_image_0000002781311174.png)
* 在工程级build-profile.json5文件中，当输入错误的**compatibleSdkVersion**版本时出现快速修复提示。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0e/v3/78URn_FdTfiIwvKQLtP3rQ/zh-cn_image_0000002781471110.png)
