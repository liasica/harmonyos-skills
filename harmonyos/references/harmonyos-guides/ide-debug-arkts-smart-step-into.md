---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-debug-arkts-smart-step-into
title: 智能步入
breadcrumb: 指南 > 编写与调试应用 > 应用调试 > 代码调试 > ArkTS代码调试 > 智能步入
category: harmonyos-guides
scraped_at: 2026-04-28T07:56:48+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:1c81e1d9994e1b2c6aecd95876e0646abd1f5a9788890e61f3d6cf8333471ab5
---

当编辑器上一行存在多个函数嵌套或调用时，开发者可以通过Smart Step Into的能力来步入到想要调试的函数内，如果在调试时想跳过某些文件，也可以自定义需要跳过的文件列表。

## 智能步入

1. 启动调试，如果断点所在的一行内存在多个方法调用，可以通过点击调试窗口的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/XwCE_7Y6R3itCsEM618bjA/zh-cn_image_0000002530753744.png?HW-CC-KV=V1&HW-CC-Date=20260427T235647Z&HW-CC-Expire=86400&HW-CC-Sign=A7F680701D005097293963E0C1D4AB645AC58AC946C32F814DD6F359FAB1F992)按钮或快捷键Shift + F7高亮展示可进入函数。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/0IpNfiDWROuqwY4sJEQVeA/zh-cn_image_0000002561833657.png?HW-CC-KV=V1&HW-CC-Date=20260427T235647Z&HW-CC-Expire=86400&HW-CC-Sign=C32DFC4121141CB538132AB1EE0A5CAE6888569B20BA143529B0661130CFED95)
2. 点击其中一个函数即可步入。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d/v3/kJkP-YKuShKX4tvZiB-39g/zh-cn_image_0000002561753685.png?HW-CC-KV=V1&HW-CC-Date=20260427T235647Z&HW-CC-Expire=86400&HW-CC-Sign=A5BC17E810BF3C71425AAFD87164B9FFD74B1E82FE6174FA05DAD11D7FDFB5E1)

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/35/v3/jzz97_0gQJGlcqpx1Fk5cw/zh-cn_image_0000002561753681.png?HW-CC-KV=V1&HW-CC-Date=20260427T235647Z&HW-CC-Expire=86400&HW-CC-Sign=0C1EA86E2B4DD666DA56231FA20B17D6F20A3A2292538A9FCB5323E62755121A)

## 过滤脚本文件

1. 点击**File > Settings**（macOS为**DevEco Studio > Preferences/Settings**） **>** **Build, Execution, Deployment > Debugger > Stepping**，勾选**Do not step into ArkTS scripts**， 可在调试时禁止智能步入某些脚本。使用工具栏按钮管理要跳过的脚本列表。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/TKpWCsDVR1a8OdAN7nAuTg/zh-cn_image_0000002530913738.png?HW-CC-KV=V1&HW-CC-Date=20260427T235647Z&HW-CC-Expire=86400&HW-CC-Sign=5677666A8B9E8F89E7EFCCC6990D03C0F95B7D2B18A15E4F145ED094E8968DEB)
2. 单击 **+** 按钮可添加新的脚本过滤器。在打开的对话框中，输入要跳过的文件名称或使用通配符。例如，如果要始终跳过 JavaScript文件，请输入 \*.js。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/lgMpQfg2T4WCORG1TuUFaQ/zh-cn_image_0000002561833665.png?HW-CC-KV=V1&HW-CC-Date=20260427T235647Z&HW-CC-Expire=86400&HW-CC-Sign=EE1AB4DA5B2028AE939BD773BB0DC7D8060896C6427D0A94D7B3683F414F33A1)
