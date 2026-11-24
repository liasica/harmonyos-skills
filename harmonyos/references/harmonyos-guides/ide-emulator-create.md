---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-emulator-create
title: 创建模拟器
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 使用模拟器运行应用 > 管理模拟器 > 创建模拟器
category: harmonyos-guides
scraped_at: 2026-11-24T12:42:29+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:f1fccc30f70be5e9bba5ecd5a04c1421138ecf833d91b12c9f3d6ec79d755b40
---

有网络环境可参考以下步骤创建模拟器，如果是无网络环境，请查看[离线部署模拟器](ide-emulator-no-network.md)。

**说明** 

在macOS中，您可能在活动监视器中发现模拟器进程占用的内存超过设置的内存。实际上，活动监视器中的**Memory**并不代表模拟器进程实际使用的物理内存，更多详情请参考[本地模拟器启动与运行问题排查常见问题](../harmonyos-faqs/app-running-faq-0003.md)。

## 使用预置的模拟器

从DevEco Studio 6.1.0 Beta2版本开始，如果本地没有模拟器，DevEco Studio会预置模拟器，开发者无需创建即可快速使用。

**说明** 

该功能仅支持中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）。

1. 选择预置模拟器：在设备选择框中，选择预置的模拟器。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/7uAao3hSQcSY5o5vtQumNA/zh-cn_image_0000002808884763.png?HW-CC-KV=V1&HW-CC-Date=20261124T044229Z&HW-CC-Expire=31536000000&HW-CC-Sign=67F34BB60C176856A23F20557C01393565594C332ADF868ACD14D7D22D40A880)
2. 下载镜像：首次使用时需要下载模拟器镜像，可通过以下任一方式完成。
   * 方式一：点击运行按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/No2YfJ6ERvC21d1YYW314w/zh-cn_image_0000002808884769.png?HW-CC-KV=V1&HW-CC-Date=20261124T044229Z&HW-CC-Expire=31536000000&HW-CC-Sign=B8D307F0F53DEB822E584CF77711346C652E5E2835286D63A43BAE7CD64EB266)，根据界面提示下载镜像。
   * 方式二：点击菜单栏**Tools > Device Manager** >![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/KNkfIGDVQUa1GjDoXyEXCA/zh-cn_image_0000002779565100.png?HW-CC-KV=V1&HW-CC-Date=20261124T044229Z&HW-CC-Expire=31536000000&HW-CC-Sign=1653B9F342C413774D5D5AA55D1EDA07F9A91EB47AD0617C17C95556F5EB2BCE)下载镜像。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/ve5enLlFSv6bLhj5Kc3STQ/zh-cn_image_0000002808764691.png?HW-CC-KV=V1&HW-CC-Date=20261124T044229Z&HW-CC-Expire=31536000000&HW-CC-Sign=9DD06DA60890D16EBAC7336BC486BAAA1CAC47A8E8B01A021E34E7A2FE3A0F5F "点击放大")
3. 运行使用：镜像下载完成后，点击运行按钮，即可一键完成启动模拟器、编译构建、推包运行操作。

## 创建新的模拟器

**说明** 

创建模拟器时，如果无法选择模拟器支持的设备类型，请排查当前电脑环境或华为账号是否在模拟器支持的国家/地区内，或DevEco Studio是否升级到对应版本，模拟器支持的国家/地区、设备类型的起始版本号请参考[设备支持类型](ide-emulator-devicetype.md)。

1. 点击菜单栏的**Tools > Device Manager**，点击右下角的**Edit**设置模拟器实例的存储路径**Local Emulator Location**，Mac默认存储在~/.Huawei/Emulator/deployed下，Windows默认存储在C:\Users\xxx\AppData\Local\Huawei\Emulator\deployed下。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/nDp1T5SHRgCy8fHhrBGHug/zh-cn_image_0000002779565106.png?HW-CC-KV=V1&HW-CC-Date=20261124T044229Z&HW-CC-Expire=31536000000&HW-CC-Sign=E602BAED77C273452E6B3C63109792DB5F38A104FF1D9B2F5EDDB9C65F903FC9 "点击放大")
2. 在**Local Emulator**页签中，单击右下角的**New Emulator**按钮，创建一个模拟器。

   在模拟器配置界面，可以选择一个默认的设备模板，首次使用时需点击设备右侧的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/wYjc7SnPQ0C3yu-tvGQYLQ/zh-cn_image_0000002779405106.png?HW-CC-KV=V1&HW-CC-Date=20261124T044229Z&HW-CC-Expire=31536000000&HW-CC-Sign=8C42D15AD1CE4B8E96B55FB7272CBDC7775C540B1EEBCCCEBFCB684F381B086E)下载模拟器镜像，您也可以在该界面更新或删除不同设备的模拟器镜像。

   单击**Edit**可以设置镜像文件的存储路径。macOS默认存储在~/Library/Huawei/Sdk下，Windows默认存储在C:\Users\xxx\AppData\Local\Huawei\Sdk下。

   **说明** 

   如果配置界面显示异常，例如设备列表为空等，可先关闭DevEco Studio，并进入~/Library/Huawei（Windows路径为C:\Users\xxx\AppData\Local\Huawei）目录，删除DevEcoStudiox.x文件夹（如DevEcoStudio6.0，具体文件夹名称和安装的DevEco Studio版本相关）以清理缓存。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f2/v3/jBEUj6n2TGqVSUkNFSDqNQ/zh-cn_image_0000002808764687.png?HW-CC-KV=V1&HW-CC-Date=20261124T044229Z&HW-CC-Expire=31536000000&HW-CC-Sign=E567BE1EBBE66E6F45080BB76C63BADEB72B1F9628B6A950A408109D1F9CC9CB)
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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/MMFbX4x3TGKYvKBe0t4FpA/zh-cn_image_0000002808884767.png?HW-CC-KV=V1&HW-CC-Date=20261124T044229Z&HW-CC-Expire=31536000000&HW-CC-Sign=CB2EA8B01C946986FBB4A859716C6AFDC07CF8FC95BDA8F2FC54B6E6428EC833)
4. 启动模拟器，有两种方式。
   * 从DevEco Studio 6.1.0 Beta2版本开始，创建后的模拟器会展示在设备列表中（最多10个），选择模拟器后，点击运行按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/A1r1_lK2SPuuEM9PmqPqWQ/zh-cn_image_0000002808764695.png?HW-CC-KV=V1&HW-CC-Date=20261124T044229Z&HW-CC-Expire=31536000000&HW-CC-Sign=28EA3E20AB3D5501CC6BC2763E667E1AC8A66F39AD9C3ED0F92948370AF15288)，即可一键完成启动模拟器、编译构建、推包运行操作。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/aR8uezswTfCchcwYrc2nrw/zh-cn_image_0000002779405118.png?HW-CC-KV=V1&HW-CC-Date=20261124T044229Z&HW-CC-Expire=31536000000&HW-CC-Sign=06644997441CB718BFBFF97FED168589C19BF4F0C75BB756BF02F5331035412A)
   * 在设备管理器页面，单击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/auFej9T0RVGqEgtZh0LkTg/zh-cn_image_0000002808884743.png?HW-CC-KV=V1&HW-CC-Date=20261124T044229Z&HW-CC-Expire=31536000000&HW-CC-Sign=EC3F07A58E9A333663BFDC75B27EC98ECB77503D8D006190B44246659C57B151)启动模拟器。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/jWGFhFBKR0KsFzs8PWJDHA/zh-cn_image_0000002779565104.png?HW-CC-KV=V1&HW-CC-Date=20261124T044229Z&HW-CC-Expire=31536000000&HW-CC-Sign=311C3FA85FCA5ADE0E31178B4714FB7CD8D444AD08CE8E43529036503347E235 "点击放大")
5. 单击DevEco Studio的**Run > Run '模块名称'**或![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/YXbuBiVrTFOEATLEH2fRMA/zh-cn_image_0000002779405110.png?HW-CC-KV=V1&HW-CC-Date=20261124T044229Z&HW-CC-Expire=31536000000&HW-CC-Sign=B1534DDA2A24D7181772749D9DB51894BABFF6F167C7529D333A97D0C4B00131)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/jJYH6MNZQRGUqPkER5ePaA/zh-cn_image_0000002779565114.png?HW-CC-KV=V1&HW-CC-Date=20261124T044229Z&HW-CC-Expire=31536000000&HW-CC-Sign=D6825500970FE003B15AF22B833C0CDCE239B1324F900CF39252BA5B417EEBF3)
6. DevEco Studio会启动应用/元服务的编译构建与推包，完成后应用/元服务即可运行在模拟器上。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/MuHmN2sEQJiD0r1HAT2T_A/zh-cn_image_0000002808884749.png?HW-CC-KV=V1&HW-CC-Date=20261124T044229Z&HW-CC-Expire=31536000000&HW-CC-Sign=537B626DBF46F6E73F9240C160A72CF932EBCE196FE6536EAF128168073AD0C1)
