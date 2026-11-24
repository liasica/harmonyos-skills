---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-realtime-check
title: 代码实时检查及快速修复
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 代码编辑 > 代码检查 > 代码实时检查及快速修复
category: harmonyos-guides
scraped_at: 2026-11-24T12:42:41+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:0b847e2a1d3a31800fe667290051b18c0287b81153c2e91d2a37e37645cf9ce1
---

## 实时检查

编辑器会实时地进行代码分析，如果输入的语法不符合编码规范，或者出现语义或语法错误，将在代码中突出显示错误或警告，将鼠标移动到错误代码处，会提示详细的错误信息。

## 代码快速修复

鸿蒙电脑DevEco Studio支持快速修复能力，辅助开发者快速修复ArkTS、C++代码或资源文件问题。

**查看告警信息：**点击编辑器底部![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/RlztUJYpTsG4NOXXTFk1ng/zh-cn_image_0000002820680979.png?HW-CC-KV=V1&HW-CC-Date=20261124T044241Z&HW-CC-Expire=31536000000&HW-CC-Sign=1A810F8C3E115DB4999DE69E4CCC3DE592B1921D83AC2C30B285BCCAEB7BDB25)图标，打开问题工具面板。双击对应告警信息，可以查看警告的具体位置及原因。

**快速修复：**将光标放在错误警告的位置，可在弹出的悬浮窗中查看问题描述和对应修复方式。单击**更多操作**可查看更多修复方法，或是当页面出现灯泡图标时，点击图标并根据相应建议，实现代码快速修复。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/JILZ6uKjQmKIiL6NR7Cmwg/zh-cn_image_0000002820720983.png?HW-CC-KV=V1&HW-CC-Date=20261124T044241Z&HW-CC-Expire=31536000000&HW-CC-Sign=BBF308D93E325BEC94133801064F3C8891152F9013B692FF9DB78E95963B2C00)

### ArkTS代码快速修复使用演示

下面通过示例展示ArkTS代码中快速修复功能的使用方法。

* 光标悬浮在未引入的变量处，点击灯泡图标，在下拉菜单中选择**Add import from XXX**，完成导入语句补充。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/54jQoXenRD-KfJiq8mF9fA/zh-cn_image_0000002791841046.gif?HW-CC-KV=V1&HW-CC-Date=20261124T044241Z&HW-CC-Expire=31536000000&HW-CC-Sign=149044ACF5B5DB7B72C764D5291CF54D54E0AF62B052756437BF01139491716F)
* 光标悬浮在拼写错误的变量名处，点击灯泡图标，在下拉菜单中选择**Change spelling to XXX**，自动修复拼写错误。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/10JJ964BRUmEsUTpSe4Sig/zh-cn_image_0000002820680981.gif?HW-CC-KV=V1&HW-CC-Date=20261124T044241Z&HW-CC-Expire=31536000000&HW-CC-Sign=669B35F1AD1C2C08B9002015AEA165EB7C99A3DDC70C296B719DB33A97730E6C)

### .json5文件快速修复使用演示

* 在模块级build-profile.json5文件中，当输入错误的**apiType**时出现快速修复提示。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/CxlxB6pfRliuCv9R3v9kAw/zh-cn_image_0000002791841048.png?HW-CC-KV=V1&HW-CC-Date=20261124T044241Z&HW-CC-Expire=31536000000&HW-CC-Sign=FEED5023179E4FAF8D1CDD4813C0D52E0F8C443261DD94E4D4F40357A2C56ACE)
* 在工程级build-profile.json5文件中，当输入错误的**compatibleSdkVersion**版本时出现快速修复提示。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/DduEXm8JRZCfjxliAIDtwQ/zh-cn_image_0000002791841044.png?HW-CC-KV=V1&HW-CC-Date=20261124T044241Z&HW-CC-Expire=31536000000&HW-CC-Sign=32DB590E0DFA6C235677ACA852E14E65E573650E676632BC47BBD383F01D060C)
