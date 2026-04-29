---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-emulator-create
title: 创建模拟器
breadcrumb: 指南 > 编写与调试应用 > 使用模拟器运行应用 > 管理模拟器 > 创建模拟器
category: harmonyos-guides
scraped_at: 2026-04-29T13:46:36+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:5f02dfd0a35222c43a4bb2d3289eb106c635f7768cb172f7c4e86344b9b27099
---

有网络环境可参考以下步骤创建模拟器，如果是无网络环境，请查看[离线部署模拟器](ide-emulator-no-network.md)。

说明

在macOS中，您可能在活动监视器中发现模拟器进程占用的内存超过设置的内存。实际上，活动监视器中的**Memory**并不代表模拟器进程实际使用的物理内存，更多详情请参考[macOS上活动监视器中显示模拟器内存偏高](../harmonyos-faqs/faqs-app-running-23.md)。

## 使用预置的模拟器

从DevEco Studio 6.1.0 Beta2版本开始，如果本地没有模拟器，DevEco Studio会预置模拟器，开发者无需创建即可快速使用。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/qPAdNx0qRom0gS00wLwc1g/zh-cn_image_0000002561831007.png?HW-CC-KV=V1&HW-CC-Date=20260429T054635Z&HW-CC-Expire=86400&HW-CC-Sign=71E2A7DD8E84E148DA0A7DC7B73DC29D2E9D1D0512664C10DF422B45F08C1C52)

在设备选择框中，选择预置的模拟器并点击运行按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/eIQSt-gcR2aX9S-5pgAPhg/zh-cn_image_0000002561751019.png?HW-CC-KV=V1&HW-CC-Date=20260429T054635Z&HW-CC-Expire=86400&HW-CC-Sign=1E2A6222CB540421CEE8FF2399CD20378621A8BB531990724CF02B9D0C072DF6)后，根据界面提示下载镜像，或点击菜单栏**Tools > Device Manager** >![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b3/v3/YYmsC0E5RqS7qOxh-sQUBw/zh-cn_image_0000002561751017.png?HW-CC-KV=V1&HW-CC-Date=20260429T054635Z&HW-CC-Expire=86400&HW-CC-Sign=F669852640AC8FF8E589B6EE65360D7A03F405BB95CF153F67A3BC91FE54FBF2)下载镜像后，即可快捷使用模拟器。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/paShhekJRj2CCXXOWj4xOw/zh-cn_image_0000002561831025.png?HW-CC-KV=V1&HW-CC-Date=20260429T054635Z&HW-CC-Expire=86400&HW-CC-Sign=0D11D780C1A58752BB8D37ED4CCA9BEAF108D187C84E6A8CB2A86A6B36A811F8)

## 创建新的模拟器

1. 点击菜单栏的**Tools > Device Manager**，点击右下角的**Edit**设置模拟器实例的存储路径**Local Emulator Location**，Mac默认存储在~/.Huawei/Emulator/deployed下，Windows默认存储在C:\Users\xxx\AppData\Local\Huawei\Emulator\deployed下。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f2/v3/wIceH6KOSai6du2xqzAD9g/zh-cn_image_0000002530911088.png?HW-CC-KV=V1&HW-CC-Date=20260429T054635Z&HW-CC-Expire=86400&HW-CC-Sign=4C89A57831695584219A9444B43480D1DAA59CD61387A746C1B1C768C8037C3D "点击放大")
2. 在**Local Emulator**页签中，单击右下角的**New Emulator**按钮，创建一个模拟器。

   在模拟器配置界面，可以选择一个默认的设备模板，首次使用时请点击设备右侧的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/NsQkAtZuT1Wep-l-eibeBw/zh-cn_image_0000002561831017.png?HW-CC-KV=V1&HW-CC-Date=20260429T054635Z&HW-CC-Expire=86400&HW-CC-Sign=6D2EE25B76E60873657ABC84E0DF177C46547A79A39F100DAEC48F24908522F6)下载模拟器镜像，您也可以在该界面更新或删除不同设备的模拟器镜像。

   单击**Edit**可以设置镜像文件的存储路径。macOS默认存储在~/Library/Huawei/Sdk下，Windows默认存储在C:\Users\xxx\AppData\Local\Huawei\Sdk下。

   说明

   如果配置界面显示异常，例如设备列表为空等，可先关闭DevEco Studio，并进入~/Library/Huawei（Windows路径为C:\Users\xxx\AppData\Local\Huawei）目录，删除DevEcoStudiox.x文件夹（如DevEcoStudio6.0，具体文件夹名称和安装的DevEco Studio版本相关）以清理缓存。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/54/v3/v9vajSoFTgOc6oUqKqisGA/zh-cn_image_0000002561751027.png?HW-CC-KV=V1&HW-CC-Date=20260429T054635Z&HW-CC-Expire=86400&HW-CC-Sign=7848CF46EF668E9E4F16C1B7383DB8260714B55A66D2125FAF31B2D5BCA8F6E4)
3. 单击**Next**，设置设备相关的参数。从DevEco Studio 6.0.0 Beta1版本开始，部分设备支持自定义屏幕配置，具体支持的设备请参考[自定义屏幕配置](ide-emulator-customize-screen-configuration.md)，下面以Phone为例。
   * **Name**：设置模拟器的名称。
   * **Screen Profile**：模拟器屏幕配置参数，可点击下拉框选择预置的机型配置，也可点击**Customize**自定义配置，在自定义配置的情况下可以对屏幕尺寸、分辨率和DPI进行修改，取值范围参考界面提示。
     + **Screen size：**屏幕的对角线长度，单位为inch。
     + **Resolution**：分辨率，包括宽度和高度，单位为px。
     + **DPI**：像素密度，DPI 越高，UI组件占用的像素点越多，从而提供更精细的显示效果。
   * **Boot options**：模拟器启动方式。从DevEco Studio 6.1.0 Beta1版本开始支持。
     + **Cold boot**：以开机启动的方式重新启动。
     + **Quick boot**：启动时加载上次关闭时保存的快照，启动后会恢复至上次关闭时的状态。
   * **Memory**：设置模拟器的内存。
   * **Storage**：设置模拟器的存储空间。

   确认所有参数后，点击**Finish**创建模拟器。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/XGkK0--1Rky_9OQFYXnLOQ/zh-cn_image_0000002530751096.png?HW-CC-KV=V1&HW-CC-Date=20260429T054635Z&HW-CC-Expire=86400&HW-CC-Sign=27E09BC4E1A0BF30811982BE3A5042492E25FFEDCA0A043DCD5771C542D6C8E4)
4. 启动模拟器，有两种方式。
   * 从DevEco Studio 6.1.0 Beta2版本开始，创建后的模拟器会展示在设备列表中（最多10个），选择模拟器后，点击运行按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/-7mdxjQ4QRG_6ikMC4C5wA/zh-cn_image_0000002561831021.png?HW-CC-KV=V1&HW-CC-Date=20260429T054635Z&HW-CC-Expire=86400&HW-CC-Sign=D1B4E92AAC976A199E75EE3CA9099A3666876948CBED5A6BA7072592923B9905)，即可一键完成启动模拟器、编译构建、推包运行操作。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fb/v3/xeLkLQguSu2kfOrV_sq5kg/zh-cn_image_0000002561831023.png?HW-CC-KV=V1&HW-CC-Date=20260429T054635Z&HW-CC-Expire=86400&HW-CC-Sign=2A2D9EB74AF7CA8731B130A5AD5E3CF0BE4D59A08F77F45D1F5A93FDB2CEE638)
   * 在设备管理器页面，单击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/0YcyFfWbQP-3-4b33mIw-w/zh-cn_image_0000002561751047.png?HW-CC-KV=V1&HW-CC-Date=20260429T054635Z&HW-CC-Expire=86400&HW-CC-Sign=6E55F962B7EE2DB22C066807CD9CB8E05D8D0A06A232FC9C1A121E3D0AEC2516)启动模拟器。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/5fnsqnddTIqEWfU3JJyC2g/zh-cn_image_0000002530751084.png?HW-CC-KV=V1&HW-CC-Date=20260429T054635Z&HW-CC-Expire=86400&HW-CC-Sign=C042AF264F7BEEB5F28AFF2CBD961449497AE9530825ABEC2D141E57401DC590 "点击放大")
5. 单击DevEco Studio的**Run > Run'模块名称'**或![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/QdYhQSUYSUeKcjt5BXSDKg/zh-cn_image_0000002530911078.png?HW-CC-KV=V1&HW-CC-Date=20260429T054635Z&HW-CC-Expire=86400&HW-CC-Sign=757522E5AA26E3AC65F5E5ECCA07B33072B83FE8FD452ADC3A2199DC6B4AEE1A)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/RCteNBfaQmm3718-W0aefg/zh-cn_image_0000002530751074.png?HW-CC-KV=V1&HW-CC-Date=20260429T054635Z&HW-CC-Expire=86400&HW-CC-Sign=1121E10D67ED02B2FB97D0FF521C1CFC5820A1EA734F8CCDE8B1D4251BFF0E7E)
6. DevEco Studio会启动应用/元服务的编译构建与推包，完成后应用/元服务即可运行在模拟器上。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/7Ui1i9Z_Rk-hEP1KODIeSQ/zh-cn_image_0000002530911086.png?HW-CC-KV=V1&HW-CC-Date=20260429T054635Z&HW-CC-Expire=86400&HW-CC-Sign=F270690A59D2CACB358CBCD7BE8696CCA958F94C039DE53E070A8DC16B3724A6)
