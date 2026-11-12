---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-debug-multi-process
title: 多进程调试
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 应用调试 > 代码调试 > ArkTS代码调试 > 多进程调试
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:798dad73bcea1e6ed453acb8cbaa55a1ecd80a83a758b429d1c8d341d0bd084b
---

部分设备上，UIAbility支持以独立进程的方式运行并调试，详细请参考[动态指定进程](isolation-process-development-guideline.md#动态指定进程)，可按照以下步骤对UIAbility进行调试。

## 编译构建配置

1. 新建一个Ability，该Ability继承AbilityStage，作为独立进程的入口。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/B9I8kxduTQyZKH_27OsFxQ/zh-cn_image_0000002808766249.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=EC3290BD409D27A0B1CC5CBF241CEBC9689F02A4249440CB113B2A08F68DAB0A)
2. 右键ets目录，新建其它需要作为独立进程启动的UIAbility。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/y8jTzRPWSZydHvJLQAkvYg/zh-cn_image_0000002808886329.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=C1AEE3C16B15CBDCEA68666EF4D3E9A08F630F4ADA9ED9E6423473AF977973D7 "点击放大")
3. 修改module.json5配置文件，增加独立进程入口及isolationProcess配置项。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/A3bHkPXoQtSLzr0kjpUEiw/zh-cn_image_0000002808766245.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=DBA4DCC4344B5CEA3ABCBEE7FBF8B320B1FB350318AD054DD809353AA32DEB4A)

## 调试

1. 编写跳转UIAbility的代码。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/Lca3KPI-TUWDXQYKzkSfQg/zh-cn_image_0000002808886323.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=79C046E0F5C4F652B0A6675CA338B28635F60CF49A618547D5359F566D7EB2CC)
2. 在跳转的UIAbility中或独立进程入口处设置断点，启动调试。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/Hr7kUDxvQ4Gazn5bqtroCw/zh-cn_image_0000002779566662.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=7139366C1AA4272BB753797812C64FAF41DBEB68DC0E1E1C8E5BA53580372AB0)

   跳转到以独立进程启动的UIAbility时将会新启动一个调试会话窗口。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/ewdqgygMRR2_-VEfjz2aVg/zh-cn_image_0000002808886331.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=DE264474641A1D9CB3CFC5542A12517CE75A5E55F30E7CA36210E8D9DA8D485B)
