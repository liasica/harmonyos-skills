---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-code-completion
title: 代码生成/补全
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 代码编辑 > 代码生成/补全
category: harmonyos-guides
scraped_at: 2026-11-14T08:49:11+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:b4fcaa77a954ef14923d9ca0e6a20a72018164d1a4b21f16fabbe293e8bee2fd
---

## 代码自动补全

提供代码的自动补全能力，编辑器工具会分析上下文，并根据输入的内容，提示可补全的类、方法、字段和关键字的名称等，支持模糊匹配。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/nnbikNSjRvyb4oOq1oqHZA/zh-cn_image_0000002810630735.gif?HW-CC-KV=V1&HW-CC-Date=20261114T004910Z&HW-CC-Expire=31536000000&HW-CC-Sign=0C34EB99942EFC7A98EF729A86122548109528B7B6529CCFFBB2C89FAB740C7A)

## 快速生成get/set方法

编辑器支持为类成员变量快速生成get和set方法。

将光标放置在当前类中，单击右键选择**生成...** **>** **Getter and Setter**，完成方法的快速生成。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/OJMqg6abRD2cEFm4K_XHZA/zh-cn_image_0000002810630733.gif?HW-CC-KV=V1&HW-CC-Date=20261114T004910Z&HW-CC-Expire=31536000000&HW-CC-Sign=8D03FA6095FB84E4F3CCE5318C8F500B65A1A415730203307B3632DF2C294807)

## 代码后缀补全

进入**设置> 扩展> 代码补全**界面，勾选开启代码后缀补全功能。

编辑器支持代码后缀补全功能，在语句末尾输入'**.**'和特定的后缀字符进行联想补全。

当前后缀补全支持arg、await、else、fori、forin、forof、forr、if、instanceof、itin、log、not、notnull、null、par、return、switch、throw、try、typeof、typeofif、undef的联想。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/4Hho5_CPS7OjpH6MhuqYLA/zh-cn_image_0000002781471180.png?HW-CC-KV=V1&HW-CC-Date=20261114T004910Z&HW-CC-Expire=31536000000&HW-CC-Sign=7DE66E5860B59A47FADA2405C09B5BC01FF8F6D1A9B07C2F46BD52179FFBD9AC)

例如在ArkTS代码的语句末尾输入.try并选择**try补全项**，可将语句自动添加到try代码块中，并生成catch代码块。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/IKRqnAJYRlieoRqdMTjKZQ/zh-cn_image_0000002781471182.gif?HW-CC-KV=V1&HW-CC-Date=20261114T004910Z&HW-CC-Expire=31536000000&HW-CC-Sign=1846C5E681408757AE01D6E5236FEDCFEDA6DCA31CA03FE6F763499C51C09313)

## 生成版权

编辑器支持为.ets文件快速添加版权信息。在文件任意位置单击右键并选择**生成...**，在弹窗中选择**版权**。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/mB1k7t5qSgK45zC3bL4arw/zh-cn_image_0000002810750841.png?HW-CC-KV=V1&HW-CC-Date=20261114T004910Z&HW-CC-Expire=31536000000&HW-CC-Sign=60B096B2EA0B8383962F7BA2E0F60DC32356449258BC800055900E1E7375E185)

若未配置版权模板信息，请按照提示信息，在设置下的**编辑器 > 版权**面板中，勾选**版权文本**并填写版权信息，返回文件鼠标右键选择**生成 > 版权**，则会在当前文件上方生成版权信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/uELpZH2iRJelPCz1N8-I7Q/zh-cn_image_0000002781311248.png?HW-CC-KV=V1&HW-CC-Date=20261114T004910Z&HW-CC-Expire=31536000000&HW-CC-Sign=E32657E3525291DC078616D78D930D6D1AE64158BF2CBB91BAAB0300248E0774)
