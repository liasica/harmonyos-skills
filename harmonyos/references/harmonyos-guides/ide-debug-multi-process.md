---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-debug-multi-process
title: 多进程调试
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 应用调试 > 代码调试 > ArkTS代码调试 > 多进程调试
category: harmonyos-guides
scraped_at: 2026-11-28T10:34:38+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:00d1649364393aa75a339c09c5708c9b981a99c6ecc896657bd47bd94c854a54
---

部分设备上，UIAbility支持以独立进程的方式运行并调试，详细请参考[动态指定进程](isolation-process-development-guideline.md#动态指定进程)，可按照以下步骤对UIAbility进行调试。

## 编译构建配置

1. 新建一个Ability，该Ability继承AbilityStage，作为独立进程的入口。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/CnoK9abySpOgus6sDlwL_A/zh-cn_image_0000002808766249.png?HW-CC-KV=V1&HW-CC-Date=20261128T023438Z&HW-CC-Expire=31536000000&HW-CC-Sign=9F43483FD3A16627A392312EE7D891CC3B516341570ADF55479234208190913D)
2. 右键ets目录，新建其它需要作为独立进程启动的UIAbility。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/N0DwijgUT5CtBmtMgVuOig/zh-cn_image_0000002808886329.png?HW-CC-KV=V1&HW-CC-Date=20261128T023438Z&HW-CC-Expire=31536000000&HW-CC-Sign=7B7645A62E7ED1B5E2FC534FC12309FBFFABA0D6D14C23D8ACE99D3C02F3A041 "点击放大")
3. 修改module.json5配置文件，增加独立进程入口及isolationProcess配置项。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/gsSWosISQjC6F99zQFnP1w/zh-cn_image_0000002808766245.png?HW-CC-KV=V1&HW-CC-Date=20261128T023438Z&HW-CC-Expire=31536000000&HW-CC-Sign=3D7B4A2DFC8A017D6245B82EE54E9FEF639F59FF438CDD6A2FC02AC95FA6C51B)

## 调试

1. 编写跳转UIAbility的代码。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/NMO0HlxXSbOMgrTpPAQg9w/zh-cn_image_0000002808886323.png?HW-CC-KV=V1&HW-CC-Date=20261128T023438Z&HW-CC-Expire=31536000000&HW-CC-Sign=C42E33D8D8651EF3615D8B1EC50AB9676074F91192E6C18CCAED5840390FD665)
2. 在跳转的UIAbility中或独立进程入口处设置断点，启动调试。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/M0uSx6ERQ7-48Y3Wl6XUBA/zh-cn_image_0000002779566662.png?HW-CC-KV=V1&HW-CC-Date=20261128T023438Z&HW-CC-Expire=31536000000&HW-CC-Sign=A8CC2985D8943D723DD157D630887B226A76CB22AE2BC401CD0375518F94D28D)

   跳转到以独立进程启动的UIAbility时将会新启动一个调试会话窗口。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/zdVa6H5zTZG_kWXDKe6uDg/zh-cn_image_0000002808886331.png?HW-CC-KV=V1&HW-CC-Date=20261128T023438Z&HW-CC-Expire=31536000000&HW-CC-Sign=BF6664119BC9381C8F072AAB49A73BDACF44D075BA437715BC571C528505FCAA)
