---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-emulator-create
title: 创建模拟器
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 使用模拟器运行应用 > 管理模拟器 > 创建模拟器
category: harmonyos-guides
scraped_at: 2026-11-14T08:48:58+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:da80866b8daa1088005b8d3cab979e02408206e5b0848a7c241de3702b45499f
---

有网络环境可参考以下步骤创建模拟器，如果是无网络环境，请查看[离线部署模拟器](ide-emulator-no-network.md)。

**说明** 

在macOS中，您可能在活动监视器中发现模拟器进程占用的内存超过设置的内存。实际上，活动监视器中的**Memory**并不代表模拟器进程实际使用的物理内存，更多详情请参考[本地模拟器启动与运行问题排查常见问题](../harmonyos-faqs/app-running-faq-0003.md)。

## 使用预置的模拟器

从DevEco Studio 6.1.0 Beta2版本开始，如果本地没有模拟器，DevEco Studio会预置模拟器，开发者无需创建即可快速使用。

**说明** 

该功能仅支持中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）。

1. 选择预置模拟器：在设备选择框中，选择预置的模拟器。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/Ge5ZBVrJQSG5eOn0pUhHNA/zh-cn_image_0000002808884763.png?HW-CC-KV=V1&HW-CC-Date=20261114T004711Z&HW-CC-Expire=31536000000&HW-CC-Sign=605D28C2E696ECD6921C053068E19291A25F3E20EDDB331B090A2E8B7AFA15ED)
2. 下载镜像：首次使用时需要下载模拟器镜像，可通过以下任一方式完成。
   * 方式一：点击运行按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d4/v3/TLXvYW2sQJmnCkcoIBBrow/zh-cn_image_0000002808884769.png?HW-CC-KV=V1&HW-CC-Date=20261114T004711Z&HW-CC-Expire=31536000000&HW-CC-Sign=F60D2DF7D92CB343572F1DE1C975CD3957D15820D95EB2C517B0CFFBCF39C080)，根据界面提示下载镜像。
   * 方式二：点击菜单栏**Tools > Device Manager** >![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1/v3/r5GoJNn_QjqN0rYJTyDDdw/zh-cn_image_0000002779565100.png?HW-CC-KV=V1&HW-CC-Date=20261114T004711Z&HW-CC-Expire=31536000000&HW-CC-Sign=DD0204C379484DF3C9DE105E627307850578CBC5A14270A84F43E013EA8FE8D5)下载镜像。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/1i6FCzjQQu2ePu0RPvX4yg/zh-cn_image_0000002808764691.png?HW-CC-KV=V1&HW-CC-Date=20261114T004711Z&HW-CC-Expire=31536000000&HW-CC-Sign=7CAF61D6ED43E4D1DFB8E9DC89002BEF2235B1B0BF3CC76FE16AE7603F8FBF86 "点击放大")
3. 运行使用：镜像下载完成后，点击运行按钮，即可一键完成启动模拟器、编译构建、推包运行操作。

## 创建新的模拟器

**说明** 

创建模拟器时，如果无法选择模拟器支持的设备类型，请排查当前电脑环境或华为账号是否在模拟器支持的国家/地区内，或DevEco Studio是否升级到对应版本，模拟器支持的国家/地区、设备类型的起始版本号请参考[设备支持类型](ide-emulator-devicetype.md)。

1. 点击菜单栏的**Tools > Device Manager**，点击右下角的**Edit**设置模拟器实例的存储路径**Local Emulator Location**，Mac默认存储在~/.Huawei/Emulator/deployed下，Windows默认存储在C:\Users\xxx\AppData\Local\Huawei\Emulator\deployed下。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/11/v3/_22EaTGETKuMHmNJK-cKaA/zh-cn_image_0000002779565106.png?HW-CC-KV=V1&HW-CC-Date=20261114T004711Z&HW-CC-Expire=31536000000&HW-CC-Sign=8ECDC5D9496B790C91D2081F27F8EA7CEA400B8623900B97DE33C65AFFDA0FF7 "点击放大")
2. 在**Local Emulator**页签中，单击右下角的**New Emulator**按钮，创建一个模拟器。

   在模拟器配置界面，可以选择一个默认的设备模板，首次使用时需点击设备右侧的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/y5Ycpxq3RZKsMymxxwIhAQ/zh-cn_image_0000002779405106.png?HW-CC-KV=V1&HW-CC-Date=20261114T004711Z&HW-CC-Expire=31536000000&HW-CC-Sign=56B1E7B47CEE3ED78E809AB403B169D447805C353D35AFE2D5D13F5C577CEDFC)下载模拟器镜像，您也可以在该界面更新或删除不同设备的模拟器镜像。

   单击**Edit**可以设置镜像文件的存储路径。macOS默认存储在~/Library/Huawei/Sdk下，Windows默认存储在C:\Users\xxx\AppData\Local\Huawei\Sdk下。

   **说明** 

   如果配置界面显示异常，例如设备列表为空等，可先关闭DevEco Studio，并进入~/Library/Huawei（Windows路径为C:\Users\xxx\AppData\Local\Huawei）目录，删除DevEcoStudiox.x文件夹（如DevEcoStudio6.0，具体文件夹名称和安装的DevEco Studio版本相关）以清理缓存。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/yuqLq8HPQcO-QKKTzrsfzw/zh-cn_image_0000002808764687.png?HW-CC-KV=V1&HW-CC-Date=20261114T004711Z&HW-CC-Expire=31536000000&HW-CC-Sign=B9892C1033EC9495F5D1F3CC741A3910127750898EE51C5FCBD19C0E2FE439FD)
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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/y8VA31ICRl24lhrhLqPElA/zh-cn_image_0000002808884767.png?HW-CC-KV=V1&HW-CC-Date=20261114T004711Z&HW-CC-Expire=31536000000&HW-CC-Sign=E853F038EDDD554782DB01056CFE6149D60CD7FAF9C9A5FA09322CB27C390AD8)
4. 启动模拟器，有两种方式。
   * 从DevEco Studio 6.1.0 Beta2版本开始，创建后的模拟器会展示在设备列表中（最多10个），选择模拟器后，点击运行按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/PzG5NYhlSJChx16K-arLtQ/zh-cn_image_0000002808764695.png?HW-CC-KV=V1&HW-CC-Date=20261114T004711Z&HW-CC-Expire=31536000000&HW-CC-Sign=D987BE82C1CA2E0B57327FC92E041225895C882FDAA12E6304CB634EC524A0B6)，即可一键完成启动模拟器、编译构建、推包运行操作。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b/v3/FZFatSV6SQqI-NiBfy1EkQ/zh-cn_image_0000002779405118.png?HW-CC-KV=V1&HW-CC-Date=20261114T004711Z&HW-CC-Expire=31536000000&HW-CC-Sign=2C6F189AB3E4F0F727C277AE57BAE06CB768CB157D5380FF2C205FF59931D240)
   * 在设备管理器页面，单击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0e/v3/o0VvcF49TbOhnIUWcCyK2A/zh-cn_image_0000002808884743.png?HW-CC-KV=V1&HW-CC-Date=20261114T004711Z&HW-CC-Expire=31536000000&HW-CC-Sign=9B2F224CDBE55CDA865F2C4F7CDA7C7A1F7EC3EE79363BD50D275C5DB7E43BF6)启动模拟器。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/ZYXbzipnR8ePPyB2i0YaUg/zh-cn_image_0000002779565104.png?HW-CC-KV=V1&HW-CC-Date=20261114T004711Z&HW-CC-Expire=31536000000&HW-CC-Sign=D3C4F7DB8DCFAEA05468C71568F33463827325E118C1542556FB023E0B3303A1 "点击放大")
5. 单击DevEco Studio的**Run > Run '模块名称'**或![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/YnxgQTwhSB6RhNrEdqG-Xg/zh-cn_image_0000002779405110.png?HW-CC-KV=V1&HW-CC-Date=20261114T004711Z&HW-CC-Expire=31536000000&HW-CC-Sign=DE686450155DAFEC241A627A3766509F7C49BA12A36FE75D0860ED9440E180E0)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/_GMsLZ7LSjiaJPYC22E4rA/zh-cn_image_0000002779565114.png?HW-CC-KV=V1&HW-CC-Date=20261114T004711Z&HW-CC-Expire=31536000000&HW-CC-Sign=A99942670856464E0206418A912FE8E3F3F2D82946590C3D29CFFD3BFDD13F16)
6. DevEco Studio会启动应用/元服务的编译构建与推包，完成后应用/元服务即可运行在模拟器上。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/FDhFeqoOR3mmcrKokV_IoA/zh-cn_image_0000002808884749.png?HW-CC-KV=V1&HW-CC-Date=20261114T004711Z&HW-CC-Expire=31536000000&HW-CC-Sign=5A89EC39EFF257D2D5EDED48A43F04FADD7EC38D2FC93C996F3A73F18FD6A9EB)
