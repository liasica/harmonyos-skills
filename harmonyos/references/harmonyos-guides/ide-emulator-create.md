---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-emulator-create
title: 创建模拟器
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 使用模拟器运行应用 > 管理模拟器 > 创建模拟器
category: harmonyos-guides
scraped_at: 2026-11-28T10:34:38+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:6a843c0ac437c41f7de9a9dc9cc136411805e555bd5dd305962157f10c2be13c
---

有网络环境可参考以下步骤创建模拟器，如果是无网络环境，请查看[离线部署模拟器](ide-emulator-no-network.md)。

**说明** 

在macOS中，您可能在活动监视器中发现模拟器进程占用的内存超过设置的内存。实际上，活动监视器中的**Memory**并不代表模拟器进程实际使用的物理内存，更多详情请参考[本地模拟器启动与运行问题排查常见问题](../harmonyos-faqs/app-running-faq-0003.md)。

## 使用预置的模拟器

从DevEco Studio 6.1.0 Beta2版本开始，如果本地没有模拟器，DevEco Studio会预置模拟器，开发者无需创建即可快速使用。

**说明** 

该功能仅支持中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）。

1. 选择预置模拟器：在设备选择框中，选择预置的模拟器。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/PvQc8RP_T0uS0b5ImMB0oA/zh-cn_image_0000002808884763.png?HW-CC-KV=V1&HW-CC-Date=20261128T023437Z&HW-CC-Expire=31536000000&HW-CC-Sign=3C8ED7E12B01B01ABDCE38BE479915AFDB26DD0E74C15A202A3784B9D58BA64B)
2. 下载镜像：首次使用时需要下载模拟器镜像，可通过以下任一方式完成。
   * 方式一：点击运行按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/2iw27SnISfyy4xklD1aqaQ/zh-cn_image_0000002808884769.png?HW-CC-KV=V1&HW-CC-Date=20261128T023437Z&HW-CC-Expire=31536000000&HW-CC-Sign=EBC5EC2B9EE3864C154D092C0A34498087CF7BE49AAF7B4884F8536762A94D32)，根据界面提示下载镜像。
   * 方式二：点击菜单栏**Tools > Device Manager** >![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/3kaBZbM-Sh6VPl9QgQdJ4Q/zh-cn_image_0000002779565100.png?HW-CC-KV=V1&HW-CC-Date=20261128T023437Z&HW-CC-Expire=31536000000&HW-CC-Sign=6693AC5A53B1C5FB6E762F7DF4E1A976D9D286E9C454142730AB9A2D5FD6993C)下载镜像。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/1HcfrmGGQtiMW2I44wwEvQ/zh-cn_image_0000002808764691.png?HW-CC-KV=V1&HW-CC-Date=20261128T023437Z&HW-CC-Expire=31536000000&HW-CC-Sign=C7FA3CD59D76CC592D3DFB89F5623B473362C8FA108B8CA8DE941F6714150593 "点击放大")
3. 运行使用：镜像下载完成后，点击运行按钮，即可一键完成启动模拟器、编译构建、推包运行操作。

## 创建新的模拟器

**说明** 

创建模拟器时，如果无法选择模拟器支持的设备类型，请排查当前电脑环境或华为账号是否在模拟器支持的国家/地区内，或DevEco Studio是否升级到对应版本，模拟器支持的国家/地区、设备类型的起始版本号请参考[设备支持类型](ide-emulator-devicetype.md)。

1. 点击菜单栏的**Tools > Device Manager**，点击右下角的**Edit**设置模拟器实例的存储路径**Local Emulator Location**，Mac默认存储在~/.Huawei/Emulator/deployed下，Windows默认存储在C:\Users\xxx\AppData\Local\Huawei\Emulator\deployed下。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/09/v3/wU1vlDJ0RbqvuZw-XFfO6w/zh-cn_image_0000002779565106.png?HW-CC-KV=V1&HW-CC-Date=20261128T023437Z&HW-CC-Expire=31536000000&HW-CC-Sign=80A7C638693EA6B7CE4E09D130C9310F7F4DBE2F53D59E13F9B741B5687B3987 "点击放大")
2. 在**Local Emulator**页签中，单击右下角的**New Emulator**按钮，创建一个模拟器。

   在模拟器配置界面，可以选择一个默认的设备模板，首次使用时需点击设备右侧的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/Z7rO6Ls-S5S5MNYKq0Qp6w/zh-cn_image_0000002779405106.png?HW-CC-KV=V1&HW-CC-Date=20261128T023437Z&HW-CC-Expire=31536000000&HW-CC-Sign=0A91468C2A15EB78A8681A36DBC12BB39FBEFD0A9EE70C48A50E0BF365D0C408)下载模拟器镜像，您也可以在该界面更新或删除不同设备的模拟器镜像。

   单击**Edit**可以设置镜像文件的存储路径。macOS默认存储在~/Library/Huawei/Sdk下，Windows默认存储在C:\Users\xxx\AppData\Local\Huawei\Sdk下。

   **说明** 

   如果配置界面显示异常，例如设备列表为空等，可先关闭DevEco Studio，并进入~/Library/Huawei（Windows路径为C:\Users\xxx\AppData\Local\Huawei）目录，删除DevEcoStudiox.x文件夹（如DevEcoStudio6.0，具体文件夹名称和安装的DevEco Studio版本相关）以清理缓存。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/6i-d5AsWRqew5mfT3yK2OQ/zh-cn_image_0000002808764687.png?HW-CC-KV=V1&HW-CC-Date=20261128T023437Z&HW-CC-Expire=31536000000&HW-CC-Sign=DE0F07A438DB4E3C50989F334FA9CB503CB3F788ED0D8B7A3EBA242E05945CB9)
3. 单击**Next**，设置设备相关的参数。
   * **Name**：设置模拟器的名称。
   * **Screen Profile**：从DevEco Studio 6.0.0 Beta1版本开始，部分设备支持选择预置的机型配置或自定义屏幕配置，具体支持的设备请参考[自定义屏幕配置](ide-emulator-customize-screen-configuration.md)。可点击下拉框选择预置的机型配置，也可点击**Customize**自定义配置，在自定义配置的情况下可以对屏幕尺寸、分辨率和DPI进行修改，取值范围参考界面提示。

     如果是Car设备，还支持新增或删除屏幕，关于多屏能力的介绍请参考[Car设备多屏能力](ide-emulator-more-features.md#section5710121118389)。

     + **Screen size：**屏幕的对角线长度，单位为inch。
     + **Resolution**：分辨率，包括宽度和高度，单位为px。
     + **DPI**：像素密度，DPI 越高，UI组件占用的像素点越多，从而提供更精细的显示效果。
   * **Boot options**：模拟器启动方式。从DevEco Studio 6.1.0 Beta1版本开始支持。
     + **Cold boot**：冷启动，以开机启动的方式重新启动。
     + **Quick boot**：热启动，启动时加载上次关闭时保存的快照，启动后会恢复至上次关闭时的状态。
   * **Memory**：设置模拟器的内存。
   * **Storage**：设置模拟器的存储空间。

   确认所有参数后，点击**Finish**创建模拟器。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/o3EJWUPqQkywmEQWXwu2qQ/zh-cn_image_0000002808884767.png?HW-CC-KV=V1&HW-CC-Date=20261128T023437Z&HW-CC-Expire=31536000000&HW-CC-Sign=3018DF57EEED37690A951B544EE79DF8A3944869FE868A6E5C0AFFFED4915787)
4. 启动模拟器，有两种方式。
   * 从DevEco Studio 6.1.0 Beta2版本开始，创建后的模拟器会展示在设备列表中（最多10个），选择模拟器后，点击运行按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/C_acrD9dSdmvKQlflvanVw/zh-cn_image_0000002808764695.png?HW-CC-KV=V1&HW-CC-Date=20261128T023437Z&HW-CC-Expire=31536000000&HW-CC-Sign=0DD1090A4BCE0356EFB32CFCB01B9502CC68AEDFD7B1A1444F8E6568C6D95B2E)，即可一键完成启动模拟器、编译构建、推包运行操作。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/twSVCi3lTAe3KFgaolsuag/zh-cn_image_0000002779405118.png?HW-CC-KV=V1&HW-CC-Date=20261128T023437Z&HW-CC-Expire=31536000000&HW-CC-Sign=7E41EB50355DD741C123D9A38E90D9B7A8A44B0B158334F9643CE3ED17865E52)
   * 在设备管理器页面，单击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/ZUIJ-jCPSLmqNQZGwPyeQQ/zh-cn_image_0000002808884743.png?HW-CC-KV=V1&HW-CC-Date=20261128T023437Z&HW-CC-Expire=31536000000&HW-CC-Sign=5C9DF9CC9C85FE5D3A11E59349AD0830B0B533F0323F360D8905516A4BC9CAA3)启动模拟器。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b8/v3/s6aVwdrxTgSYKfBD2U8Ojg/zh-cn_image_0000002779565104.png?HW-CC-KV=V1&HW-CC-Date=20261128T023437Z&HW-CC-Expire=31536000000&HW-CC-Sign=633DBDC4E98B1C792BAF5FC150BADAFDCD1318F1CDAB1377FD23F9B5EF5494CB "点击放大")
5. 单击DevEco Studio的**Run > Run '模块名称'**或![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6a/v3/UGb-1zxdTTSChnDQLsN9tw/zh-cn_image_0000002779405110.png?HW-CC-KV=V1&HW-CC-Date=20261128T023437Z&HW-CC-Expire=31536000000&HW-CC-Sign=E1681D31ECEFC579B763FE2961E6C75F39AD3EE0E6BC417575788A4F7DEAF0D0)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/vmlDcjhwRKiaT_Avz7bUJw/zh-cn_image_0000002779565114.png?HW-CC-KV=V1&HW-CC-Date=20261128T023437Z&HW-CC-Expire=31536000000&HW-CC-Sign=267D40B1B80FBF09CC6C05059F058B006A464741184C62DC3B1B3C0ED09DC804)
6. DevEco Studio会启动应用/元服务的编译构建与推包，完成后应用/元服务即可运行在模拟器上。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/3p2hBJhSSNmaIHa2_V6O1A/zh-cn_image_0000002808884749.png?HW-CC-KV=V1&HW-CC-Date=20261128T023437Z&HW-CC-Expire=31536000000&HW-CC-Sign=B6B7B231958224D7F5B3602D43850B1F2E76BC4A9EAFFADEDE0AB1DDE48196CE)
