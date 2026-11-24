---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-debug-arkts-evaluate-log
title: 打印表达式
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 应用调试 > 代码调试 > ArkTS代码调试 > 打印表达式
category: harmonyos-guides
scraped_at: 2026-11-24T12:42:30+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:a2ea87d2d1551deb9d202a628fab85d44f9b620d879f56d6fbf2e072b565c5b4
---

开发者可以通过Evaluate and log能力在代码执行到断点行时打印开发者指定的表达式。

1. 在需要打印表达式结果的地方设置断点。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/zCW-64uVSdOHY0qeHaSNAA/zh-cn_image_0000002779566804.png?HW-CC-KV=V1&HW-CC-Date=20261124T044229Z&HW-CC-Expire=31536000000&HW-CC-Sign=F9F5EAF8CE94F03DCC661DC7ACF969BA5AB11D808D467E231838728A0CE885B9)
2. 右键断点，然后点击**More**按钮。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/BpyV_FFMQBmFZDMWmQoOcA/zh-cn_image_0000002808766389.png?HW-CC-KV=V1&HW-CC-Date=20261124T044229Z&HW-CC-Expire=31536000000&HW-CC-Sign=6673342EAEDFBDFE920022039F2936A8E21437608E9B98C1EA381BF19C878E65)
3. 勾选**Evaluate and log**复选框，并在下方输入框输入要打印的表达式。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/xXDKSXGmSIi_Gu9Y5qPC0Q/zh-cn_image_0000002779566806.png?HW-CC-KV=V1&HW-CC-Date=20261124T044229Z&HW-CC-Expire=31536000000&HW-CC-Sign=50FE68657275FF6F3D71A1EA0C07577B28DF7777A405548E7884B8B8AEFEF956)
4. 启动调试，程序运行到断点时，切换到调试的Console窗口，表达式的打印结果将在这里展示。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/Zvbzgg7eRze1GNS4UYxYlg/zh-cn_image_0000002779406828.png?HW-CC-KV=V1&HW-CC-Date=20261124T044229Z&HW-CC-Expire=31536000000&HW-CC-Sign=C2A0164B7E16662A8ED27E84D9C593CF740269A6842FCF64667D623D0ABED197)
