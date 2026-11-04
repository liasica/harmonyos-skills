---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-debug-multi-process
title: 多进程调试
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 应用调试 > 代码调试 > ArkTS代码调试 > 多进程调试
category: harmonyos-guides
scraped_at: 2026-11-04T08:31:28+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:b70b77c6e2abe57772596ed302de83de0baf81056075da5e9f09e76c93123d15
---

部分设备上，UIAbility支持以独立进程的方式运行并调试，详细请参考[动态指定进程](isolation-process-development-guideline.md#动态指定进程)，可按照以下步骤对UIAbility进行调试。

## 编译构建配置

1. 新建一个Ability，该Ability继承AbilityStage，作为独立进程的入口。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/oaLCiImLQGyQMAvTlFl9gg/zh-cn_image_0000002731542065.png)
2. 右键ets目录，新建其它需要作为独立进程启动的UIAbility。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/iYKkxqUPQ4mKM4YM9g6F1w/zh-cn_image_0000002731382091.png "点击放大")
3. 修改module.json5配置文件，增加独立进程入口及isolationProcess配置项。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/WcjIJdUVTG6vAd1ivKLYAg/zh-cn_image_0000002701662864.png)

## 调试

1. 编写跳转UIAbility的代码。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/1LMleiKPTkmhNo9gtqFk2A/zh-cn_image_0000002701662868.png)
2. 在跳转的UIAbility中或独立进程入口处设置断点，启动调试。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/W3ZrKiQUQYS7Nqvn_zInlw/zh-cn_image_0000002701822790.png)

   跳转到以独立进程启动的UIAbility时将会新启动一个调试会话窗口。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3/v3/uHw74dTTQpysGYpBVETxwg/zh-cn_image_0000002701822788.png)
