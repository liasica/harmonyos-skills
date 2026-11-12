---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-code-completion
title: 代码生成/补全
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 代码编辑 > 代码生成/补全
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:c7e78917fba87df0b90e2201a9118d2678a64d30359aeed12bf47b72824664c0
---

## 代码自动补全

提供代码的自动补全能力，编辑器工具会分析上下文，并根据输入的内容，提示可补全的类、方法、字段和关键字的名称等，支持模糊匹配。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/37/v3/daS3bLdUSIqVNXhiy75qRQ/zh-cn_image_0000002810630735.gif?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=B45C8BCAB1CFA2489390FE245C11396DA9309F36700EDB69C78DD0332D10744F)

## 快速生成get/set方法

编辑器支持为类成员变量快速生成get和set方法。

将光标放置在当前类中，单击右键选择**生成...** **>** **Getter and Setter**，完成方法的快速生成。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8/v3/E-x-_mfeQwawgIdSe5eozQ/zh-cn_image_0000002810630733.gif?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=443F442699A13813A98CC6E2E763CB688FBB50E19778B88F50AB48A0E7D9C3E5)

## 代码后缀补全

进入**设置> 扩展> 代码补全**界面，勾选开启代码后缀补全功能。

编辑器支持代码后缀补全功能，在语句末尾输入'**.**'和特定的后缀字符进行联想补全。

当前后缀补全支持arg、await、else、fori、forin、forof、forr、if、instanceof、itin、log、not、notnull、null、par、return、switch、throw、try、typeof、typeofif、undef的联想。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/gyVHe74MRhOJdes77--Yrg/zh-cn_image_0000002781471180.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=754440CAD05C5EED053679CAC24B99CFED156F6BAE82A4E10FBD4C25F7963243)

例如在ArkTS代码的语句末尾输入.try并选择**try补全项**，可将语句自动添加到try代码块中，并生成catch代码块。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b8/v3/pI65SLJjTjC6dtyf0-qTpQ/zh-cn_image_0000002781471182.gif?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=D114D27A11C0F1AADF24280AD445F25DC38DA5DF125701B3F1FA1BFBC1E5B051)

## 生成版权

编辑器支持为.ets文件快速添加版权信息。在文件任意位置单击右键并选择**生成...**，在弹窗中选择**版权**。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/Hk2OjqOgTtCU74_8HEjZRg/zh-cn_image_0000002810750841.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=3B979442A079E4EE8F4967B409E9F56B51E5340B532985A245B85E2F11E1E92D)

若未配置版权模板信息，请按照提示信息，在设置下的**编辑器 > 版权**面板中，勾选**版权文本**并填写版权信息，返回文件鼠标右键选择**生成 > 版权**，则会在当前文件上方生成版权信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/f3jksU0jRMetHuTMgFx-nw/zh-cn_image_0000002781311248.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=20D1711AEE01032ECFA30799510602D9396ED93A69EC2583491335512801760F)
