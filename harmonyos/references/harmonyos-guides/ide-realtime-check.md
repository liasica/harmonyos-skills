---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-realtime-check
title: 代码实时检查及快速修复
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > 代码实时检查及快速修复
category: harmonyos-guides
scraped_at: 2026-04-28T07:55:20+08:00
doc_updated_at: 2026-03-24
content_hash: sha256:9b9a75d87bc20e3e6f55cec279538f18ada45a9f8616a7e8822ed2005be5c16d
---

## 实时检查

编辑器会实时地进行代码分析，如果输入的语法不符合编码规范，或者出现语义语法错误，将在代码中突出显示错误或警告，将鼠标放置在错误代码处，会提示详细的错误信息。

从DevEco Studio 4.0 Release版本开始，当compileSdkVersion≥10时，编辑器代码实时检查支持ArkTS性能语法规范检查。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/XGFTbC3AT6Kv-8sSe6PmgA/zh-cn_image_0000002561752973.png?HW-CC-KV=V1&HW-CC-Date=20260427T235519Z&HW-CC-Expire=86400&HW-CC-Sign=0EF027E6CC0D5C8EE6B9702090CB0A510B67E3948A5458974577561257B1FA47)

说明

当前compileSdkVersion≥10且arkTSVersion≥1.1（默认）时，ArkTS严格类型检查支持实时检查。

## 代码快速修复

DevEco Studio支持代码快速修复能力，辅助开发者快速修复ArkTS或C++代码问题。

**查看告警信息：**使用双击**Shift**快捷键打开文件查询框，输入**problems**打开问题工具面板；双击对应告警信息，可以查看告警的具体位置及原因。

**快速修复：**将光标放在错误告警的位置，可在弹出的悬浮窗中查看问题描述和对应修复方式；单击**M****ore actions**可查看更多修复方法。或是在页面出现灯泡图标时，可点击图标并根据相应建议，实现代码快速修复。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/jj3xZaTOQyS2bc5mA6zkBA/zh-cn_image_0000002561832975.png?HW-CC-KV=V1&HW-CC-Date=20260427T235519Z&HW-CC-Expire=86400&HW-CC-Sign=400706E73903CA163FEBAC69683DF47A815B1C504382689CD6D6B948A3BE9DE6)

## C++快速修复使用演示

下面通过示例展示C++代码中快速修复功能的使用方法。

### 填充switch语句

编辑器支持快速修复方式，对C++代码自动补齐switch条件表达式缺失的case条件，提升编码效率。

光标悬浮在switch表达式的条件变量处，点击灯泡图标，在下拉菜单中选择**Create missing switch cases**，完成缺失的case条件补充。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/io66Yr-rQE27WcomJSMUhA/zh-cn_image_0000002530753042.gif?HW-CC-KV=V1&HW-CC-Date=20260427T235519Z&HW-CC-Expire=86400&HW-CC-Sign=EE8B2082AD54755C10CE601129FD2A2E1783A2C17A4363925FC36D3302F5BD63)

### 使用auto替换类型

编辑器中可以用 auto 替换 iterator，new expression，cast expression的声明类型。光标悬浮在类型名称处，点击灯泡图标，在下拉菜单中选择**Replace the type with 'auto****'**完成替换。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/S4LmhAVFS4aBF6g5wXMKsA/zh-cn_image_0000002561752971.gif?HW-CC-KV=V1&HW-CC-Date=20260427T235519Z&HW-CC-Expire=86400&HW-CC-Sign=152B69191DF126C8A81C02797A00DB86928FC7C0F9D99B90B5DE9F81A2500930)

### 用?:三元操作符替换if-else

编辑器中支持将if-else语句替换为?:三元操作符。光标放在if表达式的条件处，左侧出现黄色灯泡图标，点击灯泡图标，在下拉菜单中选择**Replace 'if else' with '?:'**完成替换。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/iwPnTnApRS-rVA3BqoEj9w/zh-cn_image_0000002561752981.gif?HW-CC-KV=V1&HW-CC-Date=20260427T235519Z&HW-CC-Expire=86400&HW-CC-Sign=382ECE1331E6F10F1F8A9E0428D87B8709DC6C98DFBC52CA4CA78E6E5DB28247)

### 从使用处生成构造函数

如使用了未定义的构造函数，可通过quickfix方式快速生成相应的构造函数定义。点击构造函数名称，左侧出现红色灯泡后，点击灯泡图标选择**Create new constructor 'xxx'**生成构造函数。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1/v3/SsW63b5FTOeI5p3Ka-WWsw/zh-cn_image_0000002561832967.gif?HW-CC-KV=V1&HW-CC-Date=20260427T235519Z&HW-CC-Expire=86400&HW-CC-Sign=E0B8BD26DFB19864541B1076C8060E49110DB7D47375A9CC26F12A1272BD613C)

### 将变量拆分为声明和赋值

光标点击需要拆分的变量，左侧出现黄色灯泡后，点击灯泡图标选择**Split into declaration and assignment**，将变量的声明赋值语句拆分成声明语句和赋值语句。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/wY36caEVQk64wNgJim_PmQ/zh-cn_image_0000002530913046.gif?HW-CC-KV=V1&HW-CC-Date=20260427T235519Z&HW-CC-Expire=86400&HW-CC-Sign=742979CAD6A71405A332B68386E4AF685A7CBAD3950371F5C5241A03B888AE28)
