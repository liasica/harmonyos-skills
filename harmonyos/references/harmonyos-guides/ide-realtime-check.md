---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-realtime-check
title: 代码实时检查及快速修复
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 代码编辑 > 代码检查 > 代码实时检查及快速修复
category: harmonyos-guides
scraped_at: 2026-11-28T10:34:29+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:d01862f25f00fa04219f310f8753036a425a5f377a8aed7f27d5800aff5f5702
---

## 实时检查

编辑器会实时地进行代码分析，如果输入的语法不符合编码规范，或者出现语义语法错误，将在代码中突出显示错误或警告，将鼠标放置在错误代码处，会提示详细的错误信息。

对于ArkTS代码，从DevEco Studio 4.0 Release版本开始，当compileSdkVersion≥10时，编辑器代码实时检查支持ArkTS性能语法规范检查。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/RBTuQiGJQm6uvgdzUCkbYA/zh-cn_image_0000002808766455.png?HW-CC-KV=V1&HW-CC-Date=20261128T023429Z&HW-CC-Expire=31536000000&HW-CC-Sign=5B64E53B47082497B268E7B9DD4C7BE58CA8FEBB00E1CA2F274D77337B890D56)

**说明** 

当前compileSdkVersion≥10且arkTSVersion≥1.1（默认）时，ArkTS严格类型检查支持实时检查。

对于C/C++代码，可通过内置的Clang-Tidy或自定义的Clang-Tidy对代码进行实时检查，实时检查前需完成选项配置，配置操作请参考[Clang-Tidy代码检查（C/C++）](ide-clang-tidy.md)。

## 代码快速修复

DevEco Studio支持代码快速修复能力，辅助开发者快速修复ArkTS或C++代码问题。

**查看告警信息：**使用双击**Shift**快捷键打开文件查询框，输入**problems**打开问题工具面板；双击对应告警信息，可以查看告警的具体位置及原因。

**快速修复：**将光标放在错误告警的位置，可在弹出的悬浮窗中查看问题描述和对应修复方式；单击**M****ore actions**可查看更多修复方法。或是在页面出现灯泡图标时，可点击图标并根据相应建议，实现代码快速修复。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/K57rOV18TeacJTs8ItIukg/zh-cn_image_0000002779406900.png?HW-CC-KV=V1&HW-CC-Date=20261128T023429Z&HW-CC-Expire=31536000000&HW-CC-Sign=F1C6ABB9EFF2B3A79284A199FDC5165AA580CF0C53BBCCF14EF6271BE377BAD4)

**C++快速修复使用演示**

下面通过示例展示C++代码中快速修复功能的使用方法。

* 光标悬浮在switch表达式的条件变量处，点击灯泡图标，在下拉菜单中选择**Create missing switch cases**，完成缺失的case条件补充。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/HqlPgyfASsCuo3EbZJRyhg/zh-cn_image_0000002779566874.gif?HW-CC-KV=V1&HW-CC-Date=20261128T023429Z&HW-CC-Expire=31536000000&HW-CC-Sign=0A07734A23FAFEFBB8EC0C48B3EF999C619D11467BC521AF26777F2F46AEF042)
* 点击构造函数名称，左侧出现红色灯泡后，点击灯泡图标选择**Create new constructor 'xxx'**生成构造函数。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/lMueUO5_TKu6jcYuNS9htQ/zh-cn_image_0000002808886539.gif?HW-CC-KV=V1&HW-CC-Date=20261128T023429Z&HW-CC-Expire=31536000000&HW-CC-Sign=AE96D89F24ACE9DE037FF2D69EC14FF17791DF6540865E60AEE2E5392CD825C8)
