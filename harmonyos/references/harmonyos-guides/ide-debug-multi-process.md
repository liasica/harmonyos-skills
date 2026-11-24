---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-debug-multi-process
title: 多进程调试
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 应用调试 > 代码调试 > ArkTS代码调试 > 多进程调试
category: harmonyos-guides
scraped_at: 2026-11-24T12:42:30+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:ac7ca54c2d2a372009b73ed3e4260530fdb5b21f35e202bca3f8759e058eac81
---

部分设备上，UIAbility支持以独立进程的方式运行并调试，详细请参考[动态指定进程](isolation-process-development-guideline.md#动态指定进程)，可按照以下步骤对UIAbility进行调试。

## 编译构建配置

1. 新建一个Ability，该Ability继承AbilityStage，作为独立进程的入口。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/8_de_Rc6SxqerrwHaxBucg/zh-cn_image_0000002808766249.png?HW-CC-KV=V1&HW-CC-Date=20261124T044229Z&HW-CC-Expire=31536000000&HW-CC-Sign=104DF81E31AC78B2A1E548ED1D831ED49F97ADE1197A19C1E528B4323B1D0F96)
2. 右键ets目录，新建其它需要作为独立进程启动的UIAbility。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/1koitIPyRAyzmXNPtoX61Q/zh-cn_image_0000002808886329.png?HW-CC-KV=V1&HW-CC-Date=20261124T044229Z&HW-CC-Expire=31536000000&HW-CC-Sign=AC03BFDAAB4B2EF3FB366F7F18009470849C994659AA03BAFEB267A2B9FEA21E "点击放大")
3. 修改module.json5配置文件，增加独立进程入口及isolationProcess配置项。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/wJ6hvBXVSWGXZTFLdQP1ig/zh-cn_image_0000002808766245.png?HW-CC-KV=V1&HW-CC-Date=20261124T044229Z&HW-CC-Expire=31536000000&HW-CC-Sign=1A2E337AB1529DEF9C7D584FB5D6A8E0EF5FE57D932F6691070812440A95AACB)

## 调试

1. 编写跳转UIAbility的代码。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/XVJagtgWSiKhp0IC2yOxcQ/zh-cn_image_0000002808886323.png?HW-CC-KV=V1&HW-CC-Date=20261124T044229Z&HW-CC-Expire=31536000000&HW-CC-Sign=CBA80F7A661350DC09ED2B34C31942F4BEC3403FD4D026436F76EFE9A3402428)
2. 在跳转的UIAbility中或独立进程入口处设置断点，启动调试。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/N2BPzUK4Rp6NaViPKh--lg/zh-cn_image_0000002779566662.png?HW-CC-KV=V1&HW-CC-Date=20261124T044229Z&HW-CC-Expire=31536000000&HW-CC-Sign=784BD32959BD0BB86FA5114D51201AAED301C408211E1681797B7D1144C170DB)

   跳转到以独立进程启动的UIAbility时将会新启动一个调试会话窗口。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/-vmvdHN1QLqPEgXFy8yqLg/zh-cn_image_0000002808886331.png?HW-CC-KV=V1&HW-CC-Date=20261124T044229Z&HW-CC-Expire=31536000000&HW-CC-Sign=21F06ECFEC037B079D835CF66DE802C9E8825FB46D670B4F81E4F8577A444701)
