---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-previewer-profile-manager
title: Profile Manager
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 界面预览 > Profile Manager
category: harmonyos-guides
scraped_at: 2026-11-24T12:42:28+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:fec4a6b48327c8e853671c08fdf256ffd16c7f932ed1a22300877e19e2bdc743
---

由于真机设备型号众多，不同设备型号的屏幕分辨率可能各不相同。因此，在HarmonyOS应用/元服务开发过程中，为了适配多种设备型号，可能需要查看不同设备上的界面显示效果。对此，DevEco Studio的预览器提供了Profile Manager功能，支持开发者自定义预览设备Profile（包含分辨率和语言），从而可以查看HarmonyOS应用/元服务在不同设备上的预览显示效果。当前支持自定义设备分辨率及系统语言。

定义设备后，可以在Previewer右上角，单击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/21xhrG9hSkGS9vqEo9eK2w/zh-cn_image_0000002808765995.png?HW-CC-KV=V1&HW-CC-Date=20261124T044228Z&HW-CC-Expire=31536000000&HW-CC-Sign=11CC47C72104767BCAE86CB10293FAF968603F5BEBE0E1E7E23FE997311498FC "点击放大")按钮，打开Profile Manager，切换预览设备。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/SJDOpStHTEu48rlKWplL0Q/zh-cn_image_0000002808886075.png?HW-CC-KV=V1&HW-CC-Date=20261124T044228Z&HW-CC-Expire=31536000000&HW-CC-Sign=7960D5B101EEDFC6BDE4EE0C4FFEB13E721CD033F92F4CCA7EF7FEC99F47D20F "点击放大")

同时，Profile Manager还支持多设备预览功能，具体请参考[查看多端设备预览效果](ide-previewer-multi-profile.md)。

下面以自定义一款Phone设备为例，介绍设备Profile Manager的使用方法。

1. 在预览器界面，打开Profile Manager界面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6a/v3/6Ea-CwVcTJCX7SYON5hLQw/zh-cn_image_0000002808765991.png?HW-CC-KV=V1&HW-CC-Date=20261124T044228Z&HW-CC-Expire=31536000000&HW-CC-Sign=9C269C07C06D2D3BED4498C2BDA200DDFA71C62AE2D02473FFEEDB56D58D1FDE)
2. 在Profile Manager界面，单击**+ New Profile**按钮，添加设备。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/7tlK9_lyTgm5W7--8TTakA/zh-cn_image_0000002808886071.png?HW-CC-KV=V1&HW-CC-Date=20261124T044228Z&HW-CC-Expire=31536000000&HW-CC-Sign=2D138378D38C2BEACB713AA0C788CC4FA30BC94DBF29A3501BEB7CF42EBFDB7F)
3. 在**Create Profile**界面，填写新增设备的信息，如**Profile ID**（设备型号）、**Device type**（设备类型）、**Resolution**（分辨率）和**Language and region**（语言和区域）等。其中Device type只能选择module.json5中deviceTypes字段已定义的设备。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/ERgpVlKpS1m3_594KEfc_A/zh-cn_image_0000002779406438.png?HW-CC-KV=V1&HW-CC-Date=20261124T044228Z&HW-CC-Expire=31536000000&HW-CC-Sign=6EEBE4B2E4F7A0E669BD8DBA5DC5F05603B8E75736583351946BD58053909B73)
4. 设备信息填写完成后，单击**OK**完成创建。
