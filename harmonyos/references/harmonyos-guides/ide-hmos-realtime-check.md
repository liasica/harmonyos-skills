---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-realtime-check
title: 代码实时检查及快速修复
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 代码编辑 > 代码检查 > 代码实时检查及快速修复
category: harmonyos-guides
scraped_at: 2026-11-14T08:49:11+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:bf0539857143f5b07c23e0aadcdf9b7b5f9043541e2160b06100cc4493d178ef
---

## 实时检查

编辑器会实时地进行代码分析，如果输入的语法不符合编码规范，或者出现语义或语法错误，将在代码中突出显示错误或警告，将鼠标移动到错误代码处，会提示详细的错误信息。

## 代码快速修复

鸿蒙电脑DevEco Studio支持快速修复能力，辅助开发者快速修复ArkTS、C++代码或资源文件问题。

**查看告警信息：**点击编辑器底部![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/vm86QBU9Rny7SQKq_TRMuA/zh-cn_image_0000002810750769.png?HW-CC-KV=V1&HW-CC-Date=20261114T004911Z&HW-CC-Expire=31536000000&HW-CC-Sign=9F9B0A6E555476771925B557ADDDF671428A5BFE0B3C3072B8DAE8C3BEBEB2CC)图标，打开问题工具面板。双击对应告警信息，可以查看警告的具体位置及原因。

**快速修复：**将光标放在错误警告的位置，可在弹出的悬浮窗中查看问题描述和对应修复方式。单击**更多操作**可查看更多修复方法，或是当页面出现灯泡图标时，点击图标并根据相应建议，实现代码快速修复。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f8/v3/ymZqV2zRTs2q7m2EJvCFtw/zh-cn_image_0000002810630663.png?HW-CC-KV=V1&HW-CC-Date=20261114T004911Z&HW-CC-Expire=31536000000&HW-CC-Sign=1BAC12AE278AEB69C695AB045CE03B3BE30F5F1B0B17E30671DD1E51BA733284)

### ArkTS代码快速修复使用演示

下面通过示例展示ArkTS代码中快速修复功能的使用方法。

* 光标悬浮在未引入的变量处，点击灯泡图标，在下拉菜单中选择**Add import from XXX**，完成导入语句补充。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/kDZrID0VSYmjW0p-dTXrkw/zh-cn_image_0000002781311178.gif?HW-CC-KV=V1&HW-CC-Date=20261114T004911Z&HW-CC-Expire=31536000000&HW-CC-Sign=6E7F10E481F40DC49258C94A413AABD12EEE7871FF9EE32531843C1F8C96A3D0)
* 光标悬浮在拼写错误的变量名处，点击灯泡图标，在下拉菜单中选择**Change spelling to XXX**，自动修复拼写错误。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/ZdR8FygZQ3-sLoHKG1VpSw/zh-cn_image_0000002810750771.gif?HW-CC-KV=V1&HW-CC-Date=20261114T004911Z&HW-CC-Expire=31536000000&HW-CC-Sign=AA5696888D2DD8E9FF1E6AF690D90A6A0809C4E887F0AD3251874D0A9E686758)

### .json5文件快速修复使用演示

* 在模块级build-profile.json5文件中，当输入错误的**apiType**时出现快速修复提示。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/X2dwUCzBTciLEkUMZvRMoA/zh-cn_image_0000002781311174.png?HW-CC-KV=V1&HW-CC-Date=20261114T004911Z&HW-CC-Expire=31536000000&HW-CC-Sign=468393722821C6D715B67E5079B71A4C8086F47992B48B4E7EB46C804EAD6C7D)
* 在工程级build-profile.json5文件中，当输入错误的**compatibleSdkVersion**版本时出现快速修复提示。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/75s4lx6ETVi-iNaQ1Zby8Q/zh-cn_image_0000002781471110.png?HW-CC-KV=V1&HW-CC-Date=20261114T004911Z&HW-CC-Expire=31536000000&HW-CC-Sign=A4A5E007FA760FB562A33F9AF3D217DB9BFE71F5E1F958AC5B6BE485B8011018)
