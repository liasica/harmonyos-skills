---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-previewer-profile-manager
title: Profile Manager
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 界面预览 > Profile Manager
category: harmonyos-guides
scraped_at: 2026-11-28T10:34:37+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:46b9fca72b5fcc0b816b1ee26fb3fb4013a2133a0d516780e687aaa285cccca8
---

由于真机设备型号众多，不同设备型号的屏幕分辨率可能各不相同。因此，在HarmonyOS应用/元服务开发过程中，为了适配多种设备型号，可能需要查看不同设备上的界面显示效果。对此，DevEco Studio的预览器提供了Profile Manager功能，支持开发者自定义预览设备Profile（包含分辨率和语言），从而可以查看HarmonyOS应用/元服务在不同设备上的预览显示效果。当前支持自定义设备分辨率及系统语言。

定义设备后，可以在Previewer右上角，单击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/nn8PUhxYSDeZrJhZO5GFlw/zh-cn_image_0000002808765995.png?HW-CC-KV=V1&HW-CC-Date=20261128T023437Z&HW-CC-Expire=31536000000&HW-CC-Sign=E33CF118986D31B56778094D47EE7070E853D517995774C8CD9D131353546687 "点击放大")按钮，打开Profile Manager，切换预览设备。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ca/v3/XI3nN-OKRg6S5GGvkeMvzg/zh-cn_image_0000002808886075.png?HW-CC-KV=V1&HW-CC-Date=20261128T023437Z&HW-CC-Expire=31536000000&HW-CC-Sign=EF1A7626547C54B0E63811C98201FFF4967A9E44F2B7F9F62A74EBF3829CCF43 "点击放大")

同时，Profile Manager还支持多设备预览功能，具体请参考[查看多端设备预览效果](ide-previewer-multi-profile.md)。

下面以自定义一款Phone设备为例，介绍设备Profile Manager的使用方法。

1. 在预览器界面，打开Profile Manager界面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/KjjP8EPWR8eCtqS9uWcE3w/zh-cn_image_0000002808765991.png?HW-CC-KV=V1&HW-CC-Date=20261128T023437Z&HW-CC-Expire=31536000000&HW-CC-Sign=B257DEEF1C33A03FFFCC59EE7AA037BBA2D3E5CC2CCB37F22B9CEB1CCB7A60DF)
2. 在Profile Manager界面，单击**+ New Profile**按钮，添加设备。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/zd_QixwfTpOiInSECcWUZQ/zh-cn_image_0000002808886071.png?HW-CC-KV=V1&HW-CC-Date=20261128T023437Z&HW-CC-Expire=31536000000&HW-CC-Sign=9E5DB93A23E2D61B9AB58D67840FB7E0850505D1E66DD8A151BCB598E8BB0A0C)
3. 在**Create Profile**界面，填写新增设备的信息，如**Profile ID**（设备型号）、**Device type**（设备类型）、**Resolution**（分辨率）和**Language and region**（语言和区域）等。其中Device type只能选择module.json5中deviceTypes字段已定义的设备。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/02/v3/3lqA6x1FTJ6cL2_1frjPlA/zh-cn_image_0000002779406438.png?HW-CC-KV=V1&HW-CC-Date=20261128T023437Z&HW-CC-Expire=31536000000&HW-CC-Sign=2F910D77E629E5D2685FA2567C1586F4FDA2592F949D265C1B4F8860BFA6B92A)
4. 设备信息填写完成后，单击**OK**完成创建。
