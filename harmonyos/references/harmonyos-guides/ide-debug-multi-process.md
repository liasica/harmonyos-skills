---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-debug-multi-process
title: 多进程调试
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 应用调试 > 代码调试 > ArkTS代码调试 > 多进程调试
category: harmonyos-guides
scraped_at: 2026-10-17T06:43:27+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:4e526fdce6e5dc6c20df64d15adeb75406be7d8ce32c497defc93eb13a99658b
---

部分设备上，UIAbility支持以独立进程的方式运行并调试，详细请参考[动态指定进程](isolation-process-development-guideline.md#动态指定进程)，可按照以下步骤对UIAbility进行调试。

## 编译构建配置

1. 新建一个Ability，该Ability继承AbilityStage，作为独立进程的入口。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/s2vaBH8fRuiiGqdOna-p1Q/zh-cn_image_0000002731542065.png)
2. 右键ets目录，新建其它需要作为独立进程启动的UIAbility。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0d/v3/OnfEUHhYR0-ssp9GaUoKUA/zh-cn_image_0000002731382091.png "点击放大")
3. 修改module.json5配置文件，增加独立进程入口及isolationProcess配置项。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/35/v3/WiEEkSTcQHWt9Vkrm7bRwQ/zh-cn_image_0000002701662864.png)

## 调试

1. 编写跳转UIAbility的代码。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/zPH4cKd8SQaO1ZcYQaLXyA/zh-cn_image_0000002701662868.png)
2. 在跳转的UIAbility中或独立进程入口处设置断点，启动调试。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/eyHu5K_-SkOKE4T_h5qLBw/zh-cn_image_0000002701822790.png)

   跳转到以独立进程启动的UIAbility时将会新启动一个调试会话窗口。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/4CWP7nICT-CkaOJvdWVXsA/zh-cn_image_0000002701822788.png)
