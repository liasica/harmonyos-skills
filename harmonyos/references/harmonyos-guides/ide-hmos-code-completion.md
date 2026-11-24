---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-code-completion
title: 代码生成/补全
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 代码编辑 > 代码生成/补全
category: harmonyos-guides
scraped_at: 2026-11-24T12:42:41+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:8fe792ace7182976725f8b66c4f63750986a393ba796e14bee40942e3544bcb1
---

## 代码自动补全

提供代码的自动补全能力，编辑器工具会分析上下文，并根据输入的内容，提示可补全的类、方法、字段和关键字的名称等，支持模糊匹配。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/VBu3-T4CQ6OUtxYrxNnVAA/zh-cn_image_0000002791841074.gif?HW-CC-KV=V1&HW-CC-Date=20261124T044241Z&HW-CC-Expire=31536000000&HW-CC-Sign=8F4C09B1DA5459C1DE411682A7F204CD2EAEFFC76245B23F29683206D74223CE)

## 快速生成get/set方法

编辑器支持为类成员变量快速生成get和set方法。

将光标放置在当前类中，单击右键选择**生成...** **>** **Getter and Setter**，完成方法的快速生成。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/21OdNgo2Sa6h6q50sQ6HBg/zh-cn_image_0000002820681011.gif?HW-CC-KV=V1&HW-CC-Date=20261124T044241Z&HW-CC-Expire=31536000000&HW-CC-Sign=D68780CFCBEE2FAACADEA2C03E1C52598F94FD9166AF3F2BA85F8AAA5FBA73E7)

## 代码后缀补全

进入**设置> 扩展> 代码补全**界面，勾选开启代码后缀补全功能。

编辑器支持代码后缀补全功能，在语句末尾输入'**.**'和特定的后缀字符进行联想补全。

当前后缀补全支持arg、await、else、fori、forin、forof、forr、if、instanceof、itin、log、not、notnull、null、par、return、switch、throw、try、typeof、typeofif、undef的联想。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/XUSuHTKAT8WfoSt3iokYyw/zh-cn_image_0000002820721015.png?HW-CC-KV=V1&HW-CC-Date=20261124T044241Z&HW-CC-Expire=31536000000&HW-CC-Sign=BD70571BE4B56159366ECCE5AFEDC449B8E5E06EA1235821E17B1D4CAD1670D2)

例如在ArkTS代码的语句末尾输入.try并选择**try补全项**，可将语句自动添加到try代码块中，并生成catch代码块。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/m8XbkpeJShq7yy4p6Q5e4Q/zh-cn_image_0000002792001050.gif?HW-CC-KV=V1&HW-CC-Date=20261124T044241Z&HW-CC-Expire=31536000000&HW-CC-Sign=1F20277A1F01B5A663FFE14DBDB1C7718CA83EA771C452A3163945AB1890E38A)

## 生成版权

编辑器支持为.ets文件快速添加版权信息。在文件任意位置单击右键并选择**生成...**，在弹窗中选择**版权**。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/aJdQkSm4QuGZkTTceunj7g/zh-cn_image_0000002792001048.png?HW-CC-KV=V1&HW-CC-Date=20261124T044241Z&HW-CC-Expire=31536000000&HW-CC-Sign=63F91F50124244C34869EE25B0ABC006104CCE8F4961B1B88BED3BFE94B3CE3C)

若未配置版权模板信息，请按照提示信息，在设置下的**编辑器 > 版权**面板中，勾选**版权文本**并填写版权信息，返回文件鼠标右键选择**生成 > 版权**，则会在当前文件上方生成版权信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/CW2I-CQKS0qJnWlzjXWG7A/zh-cn_image_0000002820681009.png?HW-CC-KV=V1&HW-CC-Date=20261124T044241Z&HW-CC-Expire=31536000000&HW-CC-Sign=0E3DA43BA4ABD1120E10222D84E774F6CDF3F092E619D988EB1D7775691A8DCE)
