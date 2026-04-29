---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-debug-multi-process
title: 多进程调试
breadcrumb: 指南 > 编写与调试应用 > 应用调试 > 代码调试 > ArkTS代码调试 > 多进程调试
category: harmonyos-guides
scraped_at: 2026-04-29T13:46:44+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:ea88e44441794e2cae4f6277390e37347f978d1b99de550bac131d116addd3d0
---

部分设备上，UIAbility支持以独立进程的方式运行并调试，详细请参考[进程模型](process-model-stage.md#其他进程类型)，可按照以下步骤对UIAbility进行调试。

## 编译构建配置

1. 新建一个Ability，该Ability继承AbilityStage，作为独立进程的入口。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/u59Py-bwS_KdVUcDwHLdHA/zh-cn_image_0000002561832779.png?HW-CC-KV=V1&HW-CC-Date=20260429T054642Z&HW-CC-Expire=86400&HW-CC-Sign=0BD9C03CAE541C152DE4BA4374134166FF066802310D99E2C27035254DA3CD0F)
2. 右键ets目录，新建其它需要作为独立进程启动的UIAbility。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/37/v3/w1MSksEQTiCrbVIjZ050xQ/zh-cn_image_0000002530912852.png?HW-CC-KV=V1&HW-CC-Date=20260429T054642Z&HW-CC-Expire=86400&HW-CC-Sign=6B1593E1240ADC92FF60B755537929D5A06C886CEF8B436D394EAB6548F08E16 "点击放大")
3. 修改module.json5配置文件，增加独立进程入口及isolationProcess配置项。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/f9smVoq8T5mDSng5p7ai4Q/zh-cn_image_0000002561752793.png?HW-CC-KV=V1&HW-CC-Date=20260429T054642Z&HW-CC-Expire=86400&HW-CC-Sign=242A356512B394063596F0295379851AE4387FCE9A6A69BDAC424420CB929E41)

## 调试

1. 编写跳转UIAbility的代码。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/lJO7uFjPQ3WrQsDZpTOXWQ/zh-cn_image_0000002561832771.png?HW-CC-KV=V1&HW-CC-Date=20260429T054642Z&HW-CC-Expire=86400&HW-CC-Sign=8C08B9567A06E48097805D4F4DD0693AC72636A4DDB4D3E0ABBF0BDC3F579036)
2. 在跳转的UIAbility中或独立进程入口处设置断点，启动调试。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/G9hUQV8zTHuNnA60VIjKWA/zh-cn_image_0000002561752791.png?HW-CC-KV=V1&HW-CC-Date=20260429T054642Z&HW-CC-Expire=86400&HW-CC-Sign=2FAB12160FC2A066340130A70AC59DC9CF3F809C4C962E02B24D1FA2A6FED7C6)

   跳转到以独立进程启动的UIAbility时将会新启动一个调试会话窗口。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/2uThORL1SRC9XLa4tuBAHw/zh-cn_image_0000002530752862.png?HW-CC-KV=V1&HW-CC-Date=20260429T054642Z&HW-CC-Expire=86400&HW-CC-Sign=B52E85D4AB32A6F134917011E00D2120D8D90CAAF9BD1ECB2C9960C877AB8E75)
