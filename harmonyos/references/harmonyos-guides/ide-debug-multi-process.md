---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-debug-multi-process
title: 多进程调试
breadcrumb: 指南 > 编写与调试应用 > 应用调试 > 代码调试 > ArkTS代码调试 > 多进程调试
category: harmonyos-guides
scraped_at: 2026-04-29T13:46:44+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:58ad6dd541306ab6a840479b30274788a754ee86db2f71aa5b6ffe901742e142
---

部分设备上，UIAbility支持以独立进程的方式运行并调试，详细请参考[进程模型](process-model-stage.md#其他进程类型)，可按照以下步骤对UIAbility进行调试。

## 编译构建配置

1. 新建一个Ability，该Ability继承AbilityStage，作为独立进程的入口。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/u59Py-bwS_KdVUcDwHLdHA/zh-cn_image_0000002561832779.png)
2. 右键ets目录，新建其它需要作为独立进程启动的UIAbility。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/37/v3/w1MSksEQTiCrbVIjZ050xQ/zh-cn_image_0000002530912852.png "点击放大")
3. 修改module.json5配置文件，增加独立进程入口及isolationProcess配置项。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/f9smVoq8T5mDSng5p7ai4Q/zh-cn_image_0000002561752793.png)

## 调试

1. 编写跳转UIAbility的代码。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/lJO7uFjPQ3WrQsDZpTOXWQ/zh-cn_image_0000002561832771.png)
2. 在跳转的UIAbility中或独立进程入口处设置断点，启动调试。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/G9hUQV8zTHuNnA60VIjKWA/zh-cn_image_0000002561752791.png)

   跳转到以独立进程启动的UIAbility时将会新启动一个调试会话窗口。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/2uThORL1SRC9XLa4tuBAHw/zh-cn_image_0000002530752862.png)
