---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-debug-multi-process
title: 多进程调试
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 应用调试 > 代码调试 > ArkTS代码调试 > 多进程调试
category: harmonyos-guides
scraped_at: 2026-11-14T08:48:59+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:97cdf3f850749636f7c8fda17be0e84e45b618af1a246926769083cd3583ff65
---

部分设备上，UIAbility支持以独立进程的方式运行并调试，详细请参考[动态指定进程](isolation-process-development-guideline.md#动态指定进程)，可按照以下步骤对UIAbility进行调试。

## 编译构建配置

1. 新建一个Ability，该Ability继承AbilityStage，作为独立进程的入口。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/ykKne8txSSmnM8IFcTBcNA/zh-cn_image_0000002808766249.png?HW-CC-KV=V1&HW-CC-Date=20261114T004712Z&HW-CC-Expire=31536000000&HW-CC-Sign=51094A136E5EBB8940067ABF8F6ACD70D1367074553998750C01A103EB008DE9)
2. 右键ets目录，新建其它需要作为独立进程启动的UIAbility。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c/v3/w6v-huEjTu2kQPcO9bl4Iw/zh-cn_image_0000002808886329.png?HW-CC-KV=V1&HW-CC-Date=20261114T004712Z&HW-CC-Expire=31536000000&HW-CC-Sign=75B28A178F080C45CC6EC72EFBAA28337C000728C8BA9D5118576A73339194E6 "点击放大")
3. 修改module.json5配置文件，增加独立进程入口及isolationProcess配置项。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/N3nVK6OLQ5G5_uMECuOqWA/zh-cn_image_0000002808766245.png?HW-CC-KV=V1&HW-CC-Date=20261114T004712Z&HW-CC-Expire=31536000000&HW-CC-Sign=0CF348A47BC57C89BAE2C88D8423A58E80E4DCF5534F364C1E0D69E701E29509)

## 调试

1. 编写跳转UIAbility的代码。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/e8isvFV1TZ25KC9_76PW6g/zh-cn_image_0000002808886323.png?HW-CC-KV=V1&HW-CC-Date=20261114T004712Z&HW-CC-Expire=31536000000&HW-CC-Sign=7179552F0A243CB7A959CECD223F21A6D949534A0C29FA4A60BFC280550A1A89)
2. 在跳转的UIAbility中或独立进程入口处设置断点，启动调试。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/ktsiqgBbRVSt0ewLBCchUw/zh-cn_image_0000002779566662.png?HW-CC-KV=V1&HW-CC-Date=20261114T004712Z&HW-CC-Expire=31536000000&HW-CC-Sign=BDDB6B4FF635EF4CC5234705368809ACD3BC6DB2B3D4EE9CCFDBF93BD6228679)

   跳转到以独立进程启动的UIAbility时将会新启动一个调试会话窗口。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/D1ztBgqiSY69U-4NS74aMA/zh-cn_image_0000002808886331.png?HW-CC-KV=V1&HW-CC-Date=20261114T004712Z&HW-CC-Expire=31536000000&HW-CC-Sign=E273BFD032FB6704FF40B70F62CB12030D7350E96D8F4C6D9B4FE5955F9C8322)
