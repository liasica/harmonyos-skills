---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-debug-arkts-evaluate-log
title: 打印表达式
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 应用调试 > 代码调试 > ArkTS代码调试 > 打印表达式
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:0916cdb86f8aec90a5994ac9d624cfc79ad757cce89bd0dcea8dc0c339ce5ff3
---

开发者可以通过Evaluate and log能力在代码执行到断点行时打印开发者指定的表达式。

1. 在需要打印表达式结果的地方设置断点。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/5G4bcr08RzmixowGK9Oo5w/zh-cn_image_0000002779566804.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=496BC80BB52310057ED179B8655E5ADFDB9EE506FE4043D6D3DD9AF9657CF225)
2. 右键断点，然后点击**More**按钮。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b/v3/fT8yBaoyT16O7inaWCq5_g/zh-cn_image_0000002808766389.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=A6B8C19C6D07565964DA5483DDEC0AF90836C4D56075236F5F7917EBDDC7BB15)
3. 勾选**Evaluate and log**复选框，并在下方输入框输入要打印的表达式。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/xRRAjEklRjy8JZxgSDYO0g/zh-cn_image_0000002779566806.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=678FEC4185FCBB5669F2A797274E9AFC4039FC774428AEC2FA9966981D3E9A13)
4. 启动调试，程序运行到断点时，切换到调试的Console窗口，表达式的打印结果将在这里展示。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/xUKaIYGlRneJKdVPvTqVXQ/zh-cn_image_0000002779406828.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=53719AE7B434D60D3C4C5B44FF30A0A64F7761E84310056D818EDB7CDF393BC1)
