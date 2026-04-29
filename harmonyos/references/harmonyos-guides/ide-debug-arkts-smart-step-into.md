---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-debug-arkts-smart-step-into
title: 智能步入
breadcrumb: 指南 > 编写与调试应用 > 应用调试 > 代码调试 > ArkTS代码调试 > 智能步入
category: harmonyos-guides
scraped_at: 2026-04-29T13:46:43+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:5dae70f0374da1121796b4d948b0cc68d09275a7280418c8ee935828f283ef55
---

当编辑器上一行存在多个函数嵌套或调用时，开发者可以通过Smart Step Into的能力来步入到想要调试的函数内，如果在调试时想跳过某些文件，也可以自定义需要跳过的文件列表。

## 智能步入

1. 启动调试，如果断点所在的一行内存在多个方法调用，可以通过点击调试窗口的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/y6lRfU25RPWUlxyD-VicqQ/zh-cn_image_0000002530753744.png?HW-CC-KV=V1&HW-CC-Date=20260429T054642Z&HW-CC-Expire=86400&HW-CC-Sign=8108F7627D011C028D31EA0BD5DD91AD8F4E3B35C4D105B12DBFD93667CFD3AF)按钮或快捷键Shift + F7高亮展示可进入函数。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/KpzWkeDPQZy9oHiJCsIIZg/zh-cn_image_0000002561833657.png?HW-CC-KV=V1&HW-CC-Date=20260429T054642Z&HW-CC-Expire=86400&HW-CC-Sign=CD61B8A24A08F471F493FA43E877C6438811CE8C852AB73E71F7D55AEBE0F98F)
2. 点击其中一个函数即可步入。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/WDSVN42aR5y7zt4FTAayRg/zh-cn_image_0000002561753685.png?HW-CC-KV=V1&HW-CC-Date=20260429T054642Z&HW-CC-Expire=86400&HW-CC-Sign=F6C4D1FE2AA19EC30CA250074398FDEBF2635AC35756D3F1C393BA673FCA7A67)

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/o7ttmdKPQ8G-skCAdJv1_w/zh-cn_image_0000002561753681.png?HW-CC-KV=V1&HW-CC-Date=20260429T054642Z&HW-CC-Expire=86400&HW-CC-Sign=AC7E221693CBFAB0F85CD8535D3ACFAEED505FA350C0856FA344712E79630A91)

## 过滤脚本文件

1. 点击**File > Settings**（macOS为**DevEco Studio > Preferences/Settings**） **>** **Build, Execution, Deployment > Debugger > Stepping**，勾选**Do not step into ArkTS scripts**， 可在调试时禁止智能步入某些脚本。使用工具栏按钮管理要跳过的脚本列表。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/d6Uy0_e1TICVDowtzMBFaw/zh-cn_image_0000002530913738.png?HW-CC-KV=V1&HW-CC-Date=20260429T054642Z&HW-CC-Expire=86400&HW-CC-Sign=235EF13EA52A95F44291B482785F860C5AEF192C2E0096365E5671184609FC3E)
2. 单击 **+** 按钮可添加新的脚本过滤器。在打开的对话框中，输入要跳过的文件名称或使用通配符。例如，如果要始终跳过 JavaScript文件，请输入 \*.js。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/O0Priy-0Qku5cqzXBxaivA/zh-cn_image_0000002561833665.png?HW-CC-KV=V1&HW-CC-Date=20260429T054642Z&HW-CC-Expire=86400&HW-CC-Sign=F580A0586BEC6BFF620E7F3B000B5649B487794301B6D7ABEC4DA2F0D5EB76F6)
