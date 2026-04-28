---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-previewer-profile-manager
title: Profile Manager
breadcrumb: 指南 > 编写与调试应用 > 界面预览 > Profile Manager
category: harmonyos-guides
scraped_at: 2026-04-28T07:56:37+08:00
doc_updated_at: 2026-03-17
content_hash: sha256:58ec4effa62391efa82a69f31a4bf27ef2618dddf0c77e96388d0e816b1a1838
---

由于真机设备型号众多，不同设备型号的屏幕分辨率可能各不相同。因此，在HarmonyOS应用/元服务开发过程中，为了适配多种设备型号，可能需要查看不同设备上的界面显示效果。对此，DevEco Studio的预览器提供了Profile Manager功能，支持开发者自定义预览设备Profile（包含分辨率和语言），从而可以通过定义不同的预览设备Profile，查看HarmonyOS应用/元服务在不同设备上的预览显示效果。当前支持自定义设备分辨率及系统语言。

定义设备后，可以在Previewer右上角，单击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/BWgJTwCzTQi2vsB5I8Ioqw/zh-cn_image_0000002561832605.png?HW-CC-KV=V1&HW-CC-Date=20260427T235636Z&HW-CC-Expire=86400&HW-CC-Sign=440A0917B0081BE438DBCEB7295391CFF5EA6DAE5DFCDFCD28D4FC8B5A65FD57)按钮，打开Profile管理器，切换预览设备。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ca/v3/A0Zc2q1cRVWwkYRLmAXLzg/zh-cn_image_0000002530912682.png?HW-CC-KV=V1&HW-CC-Date=20260427T235636Z&HW-CC-Expire=86400&HW-CC-Sign=05265783264BD3358D6B5E497EF030FC79C10B76B856991DD4C320B6B652DFEC)

同时，Profile Manager还支持多设备预览功能，具体请参考[查看多端设备预览效果](ide-previewer-multi-profile.md)。

下面以自定义一款Phone设备为例，介绍设备Profile Manager的使用方法。

1. 在预览器界面，打开Profile Manager界面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/s1KofIZ4RkaU6mFwXVR0mw/zh-cn_image_0000002530912680.png?HW-CC-KV=V1&HW-CC-Date=20260427T235636Z&HW-CC-Expire=86400&HW-CC-Sign=A8DDA4B52619469656232FB77388C9929F839B8DFA419F8BE2C633618B31D5D9)
2. 在Profile Manager界面，单击**+ New Profile**按钮，添加设备。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/iAUs_czYSoimXTwX2LVs-A/zh-cn_image_0000002561832603.png?HW-CC-KV=V1&HW-CC-Date=20260427T235636Z&HW-CC-Expire=86400&HW-CC-Sign=C90FCD5F6A5B775E55953BEB85DF47CF0EFE7CA7D6756681D799A3DAF0DE2353)
3. 在**Create Profile**界面，填写新增设备的信息，如**Profile ID**（设备型号）、**Device type**（设备类型）、**Resolution**（分辨率）和**Language and region**（语言和区域）等。其中Device type只能选择module.json5中deviceTypes字段已定义的设备。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ca/v3/pulrkMMKRYW-wvuX9wWkCQ/zh-cn_image_0000002561752621.png?HW-CC-KV=V1&HW-CC-Date=20260427T235636Z&HW-CC-Expire=86400&HW-CC-Sign=F730F860FFDD81F9CFDA6D272B500C471FB0F9F5FE753FDED291546AF287B9B1)
4. 设备信息填写完成后，单击**OK**完成创建。
