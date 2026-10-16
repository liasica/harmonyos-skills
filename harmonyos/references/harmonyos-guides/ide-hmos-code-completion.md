---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-code-completion
title: 代码生成/补全
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 代码编辑 > 代码生成/补全
category: harmonyos-guides
scraped_at: 2026-10-17T06:43:41+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:c9c626f921f7f2c77780aa37e6e06f115e8321f8e3be648cd06e8dafc647ae7a
---

## 代码自动补全

提供代码的自动补全能力，编辑器工具会分析上下文，并根据输入的内容，提示可补全的类、方法、字段和关键字的名称等，支持模糊匹配。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9/v3/o3zaZ6OZQOuy7jKVlvDwwQ/zh-cn_image_0000002779728877.gif)

## 快速生成get/set方法

编辑器支持为类成员变量快速生成get和set方法。

将光标放置在当前类中，单击右键选择**生成...** **>** **Getter and Setter**，完成方法的快速生成。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/NNrTJEcDT4-zlzzpiSyJgQ/zh-cn_image_0000002779728875.gif)

## 代码后缀补全

进入**设置> 扩展> 代码补全**界面，勾选开启代码后缀补全功能。

编辑器支持代码后缀补全功能，在语句末尾输入'**.**'和特定的后缀字符进行联想补全。

当前后缀补全支持arg、await、else、fori、forin、forof、forr、if、instanceof、itin、log、not、notnull、null、par、return、switch、throw、try、typeof、typeofif、undef的联想。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/1MNSjcHbTbGVGlb2qpK-qQ/zh-cn_image_0000002750009812.png)

例如在ArkTS代码的语句末尾输入.try并选择**try补全项**，可将语句自动添加到try代码块中，并生成catch代码块。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/MNcp_YzUQfWBx_tKfifAZQ/zh-cn_image_0000002750009814.gif)

## 生成版权

编辑器支持为.ets文件快速添加版权信息。在文件任意位置单击右键并选择**生成...**，在弹窗中选择**版权**。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/WVEXifVURyKIZOmA4rlG6g/zh-cn_image_0000002750169702.png)

若未配置版权模板信息，请按照提示信息，在设置下的**编辑器 > 版权**面板中，勾选**版权文本**并填写版权信息，返回文件鼠标右键选择**生成 > 版权**，则会在当前文件上方生成版权信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/uw7wGxfYQ3aS-LhypViYfg/zh-cn_image_0000002779608725.png)
