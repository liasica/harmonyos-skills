---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-debug-arkts-evaluate-log
title: 打印表达式
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 应用调试 > 代码调试 > ArkTS代码调试 > 打印表达式
category: harmonyos-guides
scraped_at: 2026-11-14T08:48:59+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:ad1c2520cc4817fe238c91e14632d3a620ac845eefdb66bf7ebd8052f3ab25a6
---

开发者可以通过Evaluate and log能力在代码执行到断点行时打印开发者指定的表达式。

1. 在需要打印表达式结果的地方设置断点。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/3vbkdytvQWuftmHfxbOy8Q/zh-cn_image_0000002779566804.png?HW-CC-KV=V1&HW-CC-Date=20261114T004712Z&HW-CC-Expire=31536000000&HW-CC-Sign=174022A53BA5F79B173E47E99EB3993FA9411EE1088365541C4669D9190AF39E)
2. 右键断点，然后点击**More**按钮。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/4fLvqOOBQ4-tDCf429Y7KA/zh-cn_image_0000002808766389.png?HW-CC-KV=V1&HW-CC-Date=20261114T004712Z&HW-CC-Expire=31536000000&HW-CC-Sign=B50A984D94DDC84F2B98F1E843F36308585B55415096ED7FDB3A0450FF8DE829)
3. 勾选**Evaluate and log**复选框，并在下方输入框输入要打印的表达式。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/mDkJZT4eSYu5T8YjVSbXlA/zh-cn_image_0000002779566806.png?HW-CC-KV=V1&HW-CC-Date=20261114T004712Z&HW-CC-Expire=31536000000&HW-CC-Sign=E47F7D3FF07C9695D80988546A33A3DF3D782B0FD31273E2DF76E4F11E7E834F)
4. 启动调试，程序运行到断点时，切换到调试的Console窗口，表达式的打印结果将在这里展示。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/bVpNzG6OTNCZb2u4919rQA/zh-cn_image_0000002779406828.png?HW-CC-KV=V1&HW-CC-Date=20261114T004712Z&HW-CC-Expire=31536000000&HW-CC-Sign=CFDF4B1C634651A6ED6F14BDE19BDFA2E1D8EDEC3518B2678451A587E84A7FE5)
