---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-previewer-profile-manager
title: Profile Manager
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 界面预览 > Profile Manager
category: harmonyos-guides
scraped_at: 2026-11-14T08:48:58+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:3fe8f0382adefca7318379e99a4481402566f34f8a4d356f1cfe10052b3c2afb
---

由于真机设备型号众多，不同设备型号的屏幕分辨率可能各不相同。因此，在HarmonyOS应用/元服务开发过程中，为了适配多种设备型号，可能需要查看不同设备上的界面显示效果。对此，DevEco Studio的预览器提供了Profile Manager功能，支持开发者自定义预览设备Profile（包含分辨率和语言），从而可以查看HarmonyOS应用/元服务在不同设备上的预览显示效果。当前支持自定义设备分辨率及系统语言。

定义设备后，可以在Previewer右上角，单击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/p5LPL8U3TByTHkiDg8hqxg/zh-cn_image_0000002808765995.png?HW-CC-KV=V1&HW-CC-Date=20261114T004711Z&HW-CC-Expire=31536000000&HW-CC-Sign=6EA71D32EE055145BF00BEB8D1E6BD880A4455FB034ACCD2387260F15F0B0714 "点击放大")按钮，打开Profile Manager，切换预览设备。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/J4djagNMSG-z0dkNZSCvmw/zh-cn_image_0000002808886075.png?HW-CC-KV=V1&HW-CC-Date=20261114T004711Z&HW-CC-Expire=31536000000&HW-CC-Sign=9ACB7DE369264A929240CD39A54DEF4AB7AADD333460BA8F3782F6943F688351 "点击放大")

同时，Profile Manager还支持多设备预览功能，具体请参考[查看多端设备预览效果](ide-previewer-multi-profile.md)。

下面以自定义一款Phone设备为例，介绍设备Profile Manager的使用方法。

1. 在预览器界面，打开Profile Manager界面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/fGAv31auQCG9sDhlY4LfDQ/zh-cn_image_0000002808765991.png?HW-CC-KV=V1&HW-CC-Date=20261114T004711Z&HW-CC-Expire=31536000000&HW-CC-Sign=460532BA6821804DB79C860B5845C79CACB3198649F0C06401295418C9156DD2)
2. 在Profile Manager界面，单击**+ New Profile**按钮，添加设备。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f8/v3/Hobk9C8KR165O6jhPS914A/zh-cn_image_0000002808886071.png?HW-CC-KV=V1&HW-CC-Date=20261114T004711Z&HW-CC-Expire=31536000000&HW-CC-Sign=6D29EE5A96A04767BA7D421A034593F06D2D6385BDE36DDABE13D47677FC2494)
3. 在**Create Profile**界面，填写新增设备的信息，如**Profile ID**（设备型号）、**Device type**（设备类型）、**Resolution**（分辨率）和**Language and region**（语言和区域）等。其中Device type只能选择module.json5中deviceTypes字段已定义的设备。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/pyEPQb0DSRiGHoph_JddFQ/zh-cn_image_0000002779406438.png?HW-CC-KV=V1&HW-CC-Date=20261114T004711Z&HW-CC-Expire=31536000000&HW-CC-Sign=8213D9B5AB36BF6D1EDE6FFBCA2220F55333DA7049E1EF353745B84B21C1BBC1)
4. 设备信息填写完成后，单击**OK**完成创建。
