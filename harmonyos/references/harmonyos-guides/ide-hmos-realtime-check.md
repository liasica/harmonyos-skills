---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-realtime-check
title: 代码实时检查及快速修复
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 代码编辑 > 代码检查 > 代码实时检查及快速修复
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:d7eb739116c0478ef7d84fb6252b91a2b41a0a3e84ac3a86f47061e0aa6b2427
---

## 实时检查

编辑器会实时地进行代码分析，如果输入的语法不符合编码规范，或者出现语义或语法错误，将在代码中突出显示错误或警告，将鼠标移动到错误代码处，会提示详细的错误信息。

## 代码快速修复

鸿蒙电脑DevEco Studio支持快速修复能力，辅助开发者快速修复ArkTS、C++代码或资源文件问题。

**查看告警信息：**点击编辑器底部![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/Z7hpIJg4S7CYF4oUCJ4gvw/zh-cn_image_0000002810750769.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=88B26FD40A80B2A2B87CF56E0342B0C260152F6FE4600A920529F754090C8928)图标，打开问题工具面板。双击对应告警信息，可以查看警告的具体位置及原因。

**快速修复：**将光标放在错误警告的位置，可在弹出的悬浮窗中查看问题描述和对应修复方式。单击**更多操作**可查看更多修复方法，或是当页面出现灯泡图标时，点击图标并根据相应建议，实现代码快速修复。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/j56ssGHAT_qEeMnnaXU0UQ/zh-cn_image_0000002810630663.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=78544E96CD51191E3503974F871FC13EBBF090926898C68C187879E6EB51EA78)

### ArkTS代码快速修复使用演示

下面通过示例展示ArkTS代码中快速修复功能的使用方法。

* 光标悬浮在未引入的变量处，点击灯泡图标，在下拉菜单中选择**Add import from XXX**，完成导入语句补充。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/3r717e_1Q2mOw6us0ibSJQ/zh-cn_image_0000002781311178.gif?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=4ACE832F9D56A7E2FD448CDCEEC24BF190B86CD84E9CC09AA4CB649819DF64F2)
* 光标悬浮在拼写错误的变量名处，点击灯泡图标，在下拉菜单中选择**Change spelling to XXX**，自动修复拼写错误。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/6UNFBp9mQl2fJAbtEPf4zQ/zh-cn_image_0000002810750771.gif?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=4818C6208D8B3B4AA255A522EF9001D93E511562E19068739EA128D35939DD3E)

### .json5文件快速修复使用演示

* 在模块级build-profile.json5文件中，当输入错误的**apiType**时出现快速修复提示。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/EbdYlWsJSrOoLQ_ijZnEdA/zh-cn_image_0000002781311174.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=836D2928E14BCD2FC663F2A1E4F40D66B4EB2D774CCA7EC9FF0D12BA0AE31E54)
* 在工程级build-profile.json5文件中，当输入错误的**compatibleSdkVersion**版本时出现快速修复提示。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/mF33hfDuTLOLNsnoso9hEQ/zh-cn_image_0000002781471110.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=00C5B16AB9E98FF8A417A3332B1EA10F79BFFEA175BAC38FB65ACD0CCCCC6341)
