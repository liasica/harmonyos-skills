---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-debug-multi-process
title: 多进程调试
breadcrumb: 指南 > 编写与调试应用 > 应用调试 > 代码调试 > ArkTS代码调试 > 多进程调试
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:54+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:be050b605fbe42c594e89f82d568a4a32a4dd04caed34e5f5db0c0ad967e3781
---

部分设备上，UIAbility支持以独立进程的方式运行并调试，详细请参考[进程模型](process-model-stage.md#其他进程类型)，可按照以下步骤对UIAbility进行调试。

## 编译构建配置

1. 新建一个Ability，该Ability继承AbilityStage，作为独立进程的入口。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/lBfwnCG1T22-sUYcGO2Y1g/zh-cn_image_0000002731542065.png)
2. 右键ets目录，新建其它需要作为独立进程启动的UIAbility。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/dFzB7SOuTHyQ5aParSJqlg/zh-cn_image_0000002731382091.png "点击放大")
3. 修改module.json5配置文件，增加独立进程入口及isolationProcess配置项。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/WkNkiAVCTzSzlillPq5Hrg/zh-cn_image_0000002701662864.png)

## 调试

1. 编写跳转UIAbility的代码。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/WQzhAyW8QqSEWCvjQEuBvQ/zh-cn_image_0000002701662868.png)
2. 在跳转的UIAbility中或独立进程入口处设置断点，启动调试。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/Nz8dEp2sRxe8w6o_cl1oNQ/zh-cn_image_0000002701822790.png)

   跳转到以独立进程启动的UIAbility时将会新启动一个调试会话窗口。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/ojHNeN_kRViFsQjFM5y_Bg/zh-cn_image_0000002701822788.png)
