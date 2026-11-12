---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-previewer-profile-manager
title: Profile Manager
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 界面预览 > Profile Manager
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:f1bac0a418d7b4ee2404eb3b71a5b3e93e30c14d2afce1f2c3f4abf1517b0970
---

由于真机设备型号众多，不同设备型号的屏幕分辨率可能各不相同。因此，在HarmonyOS应用/元服务开发过程中，为了适配多种设备型号，可能需要查看不同设备上的界面显示效果。对此，DevEco Studio的预览器提供了Profile Manager功能，支持开发者自定义预览设备Profile（包含分辨率和语言），从而可以查看HarmonyOS应用/元服务在不同设备上的预览显示效果。当前支持自定义设备分辨率及系统语言。

定义设备后，可以在Previewer右上角，单击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/za-btFG5T3err9CDLsPDEg/zh-cn_image_0000002808765995.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=BE7B8D49FDC0F3FDE5A87FF72E6FE399E21A282BFD9D61003D21DD20D0D83A1D "点击放大")按钮，打开Profile Manager，切换预览设备。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/jDJY3XXzSiGlbEBOumrVqA/zh-cn_image_0000002808886075.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=9B294A425A25BED07ED4231ABE647B039A07D2B434A4B197BB153337A1CC34F5 "点击放大")

同时，Profile Manager还支持多设备预览功能，具体请参考[查看多端设备预览效果](ide-previewer-multi-profile.md)。

下面以自定义一款Phone设备为例，介绍设备Profile Manager的使用方法。

1. 在预览器界面，打开Profile Manager界面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/kq8LZZ4KQuOcrp8BWBjd7g/zh-cn_image_0000002808765991.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=E8D0EE562F70851EE902534CE8D240292E501A59503B0B9348C051E6439486F4)
2. 在Profile Manager界面，单击**+ New Profile**按钮，添加设备。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/3VtQ-MfGQE6Ovb9ySIHNww/zh-cn_image_0000002808886071.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=003E84F35C9A69351934127C039E4665A50AFA7B6D3FDD71EFA020890D366C06)
3. 在**Create Profile**界面，填写新增设备的信息，如**Profile ID**（设备型号）、**Device type**（设备类型）、**Resolution**（分辨率）和**Language and region**（语言和区域）等。其中Device type只能选择module.json5中deviceTypes字段已定义的设备。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c/v3/TsZb2JhIS0GQEgiXj0H5vw/zh-cn_image_0000002779406438.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=F7BF7A6CC627D5D5E5E2ED21C64901D3EC10F804B52603287D68C79A7BA3E56F)
4. 设备信息填写完成后，单击**OK**完成创建。
