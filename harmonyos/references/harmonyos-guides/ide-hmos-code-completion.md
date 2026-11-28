---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-code-completion
title: 代码生成/补全
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 代码编辑 > 代码生成/补全
category: harmonyos-guides
scraped_at: 2026-11-28T10:34:50+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:d8c20fd71a7aee1d96956257e01f31af7ce96f80de3eae08c6572e12029bc71a
---

## 代码自动补全

提供代码的自动补全能力，编辑器工具会分析上下文，并根据输入的内容，提示可补全的类、方法、字段和关键字的名称等，支持模糊匹配。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/ofwyUI44S5yBJH_mktyiVg/zh-cn_image_0000002791841074.gif?HW-CC-KV=V1&HW-CC-Date=20261128T023449Z&HW-CC-Expire=31536000000&HW-CC-Sign=25AE8426AAAD53A6826D4E9A36FCFBA52596EC24541C18DE9ADE5F60681FBEDE)

## 快速生成get/set方法

编辑器支持为类成员变量快速生成get和set方法。

将光标放置在当前类中，单击右键选择**生成...** **>** **Getter and Setter**，完成方法的快速生成。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/MPWw1R5UQNuWXTQRbBFMOQ/zh-cn_image_0000002820681011.gif?HW-CC-KV=V1&HW-CC-Date=20261128T023449Z&HW-CC-Expire=31536000000&HW-CC-Sign=88075A84223AC7ECA2BFA168B5A610F26C0EF7D5D4CFA0BF216B9E0B75E62ED1)

## 代码后缀补全

进入**设置> 扩展> 代码补全**界面，勾选开启代码后缀补全功能。

编辑器支持代码后缀补全功能，在语句末尾输入'**.**'和特定的后缀字符进行联想补全。

当前后缀补全支持arg、await、else、fori、forin、forof、forr、if、instanceof、itin、log、not、notnull、null、par、return、switch、throw、try、typeof、typeofif、undef的联想。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/HEMd1GMySXO8TjIYNxAXqg/zh-cn_image_0000002820721015.png?HW-CC-KV=V1&HW-CC-Date=20261128T023449Z&HW-CC-Expire=31536000000&HW-CC-Sign=21522EFCA59DF9DFB67FE90E3BB24F531EFFAD64B1806F44A3700B45F6483CD3)

例如在ArkTS代码的语句末尾输入.try并选择**try补全项**，可将语句自动添加到try代码块中，并生成catch代码块。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/xcXtQv32QaKDnNh9os43zA/zh-cn_image_0000002792001050.gif?HW-CC-KV=V1&HW-CC-Date=20261128T023449Z&HW-CC-Expire=31536000000&HW-CC-Sign=829D41336475B4C05A493FA3728A1D991AF62FDEE7A820145F828FB310A92F4B)

## 生成版权

编辑器支持为.ets文件快速添加版权信息。在文件任意位置单击右键并选择**生成...**，在弹窗中选择**版权**。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/lfCgC8GDRFKtUvTeOOoroQ/zh-cn_image_0000002792001048.png?HW-CC-KV=V1&HW-CC-Date=20261128T023449Z&HW-CC-Expire=31536000000&HW-CC-Sign=62F3051FAB870B918D8774F4F1C916F9F4E0A76538E1590C8E84E5A1B8F2E93C)

若未配置版权模板信息，请按照提示信息，在设置下的**编辑器 > 版权**面板中，勾选**版权文本**并填写版权信息，返回文件鼠标右键选择**生成 > 版权**，则会在当前文件上方生成版权信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/g6OHlVFoRBWSWan3OFcqtw/zh-cn_image_0000002820681009.png?HW-CC-KV=V1&HW-CC-Date=20261128T023449Z&HW-CC-Expire=31536000000&HW-CC-Sign=E33E5BEC6B8FD0288935CF56A1C73FCF2DAF3ACDA83CF8945E5E6D689F3FAF5D)
