---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-debug-multi-process
title: 多进程调试
breadcrumb: 指南 > 编写与调试应用 > 应用调试 > 代码调试 > ArkTS代码调试 > 多进程调试
category: harmonyos-guides
scraped_at: 2026-04-28T07:56:47+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:018e60e0560db31378118a7b323233676317d5c0a2ab5fc6eb6dff321eb80258
---

部分设备上，UIAbility支持以独立进程的方式运行并调试，详细请参考[进程模型](process-model-stage.md#其他进程类型)，可按照以下步骤对UIAbility进行调试。

## 编译构建配置

1. 新建一个Ability，该Ability继承AbilityStage，作为独立进程的入口。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/S38aX0SQSWGclRaaclextw/zh-cn_image_0000002561832779.png?HW-CC-KV=V1&HW-CC-Date=20260427T235647Z&HW-CC-Expire=86400&HW-CC-Sign=72C28EC24F030F65A16086ECA4EB5497D8115F4A12586186BE38DB33086D09C8)
2. 右键ets目录，新建其它需要作为独立进程启动的UIAbility。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/l3_YqWHuQ_mMGJTjKr0Qfg/zh-cn_image_0000002530912852.png?HW-CC-KV=V1&HW-CC-Date=20260427T235647Z&HW-CC-Expire=86400&HW-CC-Sign=921AD07A872816701EB0880BD2EB482E0E562540F56CE78DF5DEA61F247D755B "点击放大")
3. 修改module.json5配置文件，增加独立进程入口及isolationProcess配置项。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/V5SpVE68SxqjCrSRoTo3gQ/zh-cn_image_0000002561752793.png?HW-CC-KV=V1&HW-CC-Date=20260427T235647Z&HW-CC-Expire=86400&HW-CC-Sign=0A70A1EA80593731D64CB24FAB79B3DFC5C2855C6FFDCEE7C9EC03218D152C3C)

## 调试

1. 编写跳转UIAbility的代码。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/LPVc5eEyQgKA7PriPGUe5A/zh-cn_image_0000002561832771.png?HW-CC-KV=V1&HW-CC-Date=20260427T235647Z&HW-CC-Expire=86400&HW-CC-Sign=ADFF019FA493432C744536D2437387849027702974680EB57438A26C4B907F0A)
2. 在跳转的UIAbility中或独立进程入口处设置断点，启动调试。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/Mz5I-pevQnCJ_cOts1GB-Q/zh-cn_image_0000002561752791.png?HW-CC-KV=V1&HW-CC-Date=20260427T235647Z&HW-CC-Expire=86400&HW-CC-Sign=C20D809B38AE8EEF4AFB05A7D1B49202072D3480462C3B0F63A3C5A81BF0D1FE)

   跳转到以独立进程启动的UIAbility时将会新启动一个调试会话窗口。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/37/v3/nbssZkG5RVSwOHlB-Jy2JA/zh-cn_image_0000002530752862.png?HW-CC-KV=V1&HW-CC-Date=20260427T235647Z&HW-CC-Expire=86400&HW-CC-Sign=345B50388F76CF09B8260FEAEEE0BAD7F075BC21B17E8FE7224B0FB28F1596D5)
