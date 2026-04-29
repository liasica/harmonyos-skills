---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-previewer-profile-manager
title: Profile Manager
breadcrumb: 指南 > 编写与调试应用 > 界面预览 > Profile Manager
category: harmonyos-guides
scraped_at: 2026-04-29T13:46:32+08:00
doc_updated_at: 2026-03-17
content_hash: sha256:ba2800f149f4b5bc7a56bbaeb38f5bfd28131263b276204375152c0f52a2fb91
---

由于真机设备型号众多，不同设备型号的屏幕分辨率可能各不相同。因此，在HarmonyOS应用/元服务开发过程中，为了适配多种设备型号，可能需要查看不同设备上的界面显示效果。对此，DevEco Studio的预览器提供了Profile Manager功能，支持开发者自定义预览设备Profile（包含分辨率和语言），从而可以通过定义不同的预览设备Profile，查看HarmonyOS应用/元服务在不同设备上的预览显示效果。当前支持自定义设备分辨率及系统语言。

定义设备后，可以在Previewer右上角，单击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/JugOyTnwTZyjJtP5t4rO_w/zh-cn_image_0000002561832605.png?HW-CC-KV=V1&HW-CC-Date=20260429T054632Z&HW-CC-Expire=86400&HW-CC-Sign=3B10C82DA402D802BFE699180BA73B5705C17E0F9C8C1F64ED3F4CD97FEE134B)按钮，打开Profile管理器，切换预览设备。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/BeLr1nRrSI2uIqq6O17A1g/zh-cn_image_0000002530912682.png?HW-CC-KV=V1&HW-CC-Date=20260429T054632Z&HW-CC-Expire=86400&HW-CC-Sign=1DA924F57ECCF3302700A7182D68782D5557A25938E963D8A5FAB26FE87638CD)

同时，Profile Manager还支持多设备预览功能，具体请参考[查看多端设备预览效果](ide-previewer-multi-profile.md)。

下面以自定义一款Phone设备为例，介绍设备Profile Manager的使用方法。

1. 在预览器界面，打开Profile Manager界面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/G-q_qqKhRp6UqNtLoE2Nnw/zh-cn_image_0000002530912680.png?HW-CC-KV=V1&HW-CC-Date=20260429T054632Z&HW-CC-Expire=86400&HW-CC-Sign=810212B00A447733CBA14CCEF30E715FD06E81C295CA2D73D0A9DD5281A56081)
2. 在Profile Manager界面，单击**+ New Profile**按钮，添加设备。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/02/v3/h7IbIWzbROCLTq6Myc8Nmw/zh-cn_image_0000002561832603.png?HW-CC-KV=V1&HW-CC-Date=20260429T054632Z&HW-CC-Expire=86400&HW-CC-Sign=B29BD732A5D45AABE43C9176889CB768092EE22C3B181AC7C77F0B795B6F50A3)
3. 在**Create Profile**界面，填写新增设备的信息，如**Profile ID**（设备型号）、**Device type**（设备类型）、**Resolution**（分辨率）和**Language and region**（语言和区域）等。其中Device type只能选择module.json5中deviceTypes字段已定义的设备。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/6wnk5z-qQTWyk9fRMg-paA/zh-cn_image_0000002561752621.png?HW-CC-KV=V1&HW-CC-Date=20260429T054632Z&HW-CC-Expire=86400&HW-CC-Sign=9016A6E701E265DE8C2DC758B4788CF3FFF5B239F8220ACF9EFEF9B6A4A84C7D)
4. 设备信息填写完成后，单击**OK**完成创建。
