---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-debug-arkts-smart-step-into
title: 智能步入
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 应用调试 > 代码调试 > ArkTS代码调试 > 智能步入
category: harmonyos-guides
scraped_at: 2026-11-14T08:48:59+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:2b3be31e87710e3e56acade415989c3c1621867329647a04c40441b1d8da23a0
---

当代码行存在多个函数嵌套或调用时，开发者可以通过Smart Step Into的能力来步入到想要调试的函数内，如果在调试时想跳过某些文件，也可以自定义需要跳过的文件列表。

## 智能步入

1. 启动调试，如果断点所在的一行内存在多个方法调用，可以通过点击调试窗口的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/e1lg_gMFSh-0BEmHEFoD8Q/zh-cn_image_0000002808887071.png?HW-CC-KV=V1&HW-CC-Date=20261114T004712Z&HW-CC-Expire=31536000000&HW-CC-Sign=2453173C24176EF7C8E9EF67FBF691430ACB443B6A646CE3707EE1847078177A)按钮或快捷键Shift + F7高亮展示可步入的函数。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/-onkH6sKQ4ekM5l4hfqAMQ/zh-cn_image_0000002808766987.png?HW-CC-KV=V1&HW-CC-Date=20261114T004712Z&HW-CC-Expire=31536000000&HW-CC-Sign=73FD2AD8785B36CB79C31CFE83C4A8B61E20E5B2FB71E985A7F16140FEDB01CD)
2. 点击其中一个函数即可步入。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ca/v3/F4HgUMmzREaRK2uPGTrXXw/zh-cn_image_0000002808766993.png?HW-CC-KV=V1&HW-CC-Date=20261114T004712Z&HW-CC-Expire=31536000000&HW-CC-Sign=6D8CA94E9B0DB202E0EB68C5A8BD5E64FAD4D177944B3A6B8A10027AF1AB916F)

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/R4TJOxQ-RwaxhZXdQZY14w/zh-cn_image_0000002779567408.png?HW-CC-KV=V1&HW-CC-Date=20261114T004712Z&HW-CC-Expire=31536000000&HW-CC-Sign=1EC318FAF486581D0192768B8FCDE0F6715712FD332BB59F79DD3773A085199B)

## 过滤脚本文件

1. 点击**File > Settings**（macOS为**DevEco Studio > Preferences/Settings**） **>** **Build, Execution, Deployment > Debugger > Stepping**，勾选**Do not step into ArkTS scripts**， 可在调试时禁止智能步入某些脚本。使用工具栏按钮管理要跳过的脚本列表。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/HIMrpJfvT-2MNl3rNwvNbQ/zh-cn_image_0000002779407434.png?HW-CC-KV=V1&HW-CC-Date=20261114T004712Z&HW-CC-Expire=31536000000&HW-CC-Sign=2CC1F7C09DC505CD7F3B5F6820879E1B1D37EEF06B8574AA7479A92E16619AD9)
2. 单击 **+** 按钮可添加新的脚本过滤器。在打开的对话框中，输入要跳过的文件名称或使用通配符。例如，如果要始终跳过 JavaScript文件，请输入 \*.js。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/Yf23Krd1RuCewnUqP02Hyg/zh-cn_image_0000002779567414.png?HW-CC-KV=V1&HW-CC-Date=20261114T004712Z&HW-CC-Expire=31536000000&HW-CC-Sign=46FB1A76BD3002C1CB7277683B72F5C9E6DA540C4EEC50306E7CD7E121F68B3B)
