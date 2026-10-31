---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-debug-arkts-extension
title: extension调试
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 应用调试 > 代码调试 > ArkTS代码调试 > extension调试
category: harmonyos-guides
scraped_at: 2026-11-01T07:12:54+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:d4e38e3ba880ad308e659a408d92f67a4810520e74cbaadbfb7ff324e033848e
---

开发者可通过两种方式对[Extension Ability](extensionability-overview.md)生命周期函数进行调试。

* 应用安装到设备上后，通过等待调试方式进行调试。
* 修改运行调试配置项，指定当前运行或调试的Ability为Extension Ability。

## 等待调试方式

1. 参考[等待调试](ide-debug-arkts-attach-to-process.md)对当前调试工程进行调试。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/5SHr2GKMRmOnYNiy-r4yQg/zh-cn_image_0000002731383071.png)
2. 在Extension Ability生命周期内设置断点。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/4lTPQ5AQTkauYRS3su1BkQ/zh-cn_image_0000002731543045.png)
3. 等待Extension Ability生命周期函数代码调用从而命中断点。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/64aq36aEQmerveG1xFhY5g/zh-cn_image_0000002731543041.png)

## 修改运行配置方式

1. 在运行调试窗口，运行配置项**Launch Options**选择**Specified Ability**。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/ZsMBNq1vQUOkyIj4jlVAog/zh-cn_image_0000002701823784.png)
2. 选择需要进行调试的Extension Ability。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/_U1WQVS4QuqqQpyFryfYWQ/zh-cn_image_0000002731383077.png)
3. 点击**OK**保存配置后，点击调试按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/ykC3qL7cTxmIzh83namsDg/zh-cn_image_0000002701663862.png)，启动调试即可命中 Extension Ability 中的生命周期函数断点。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/M9RE7J6FTbOhpnySZFaZgQ/zh-cn_image_0000002731543053.png)
