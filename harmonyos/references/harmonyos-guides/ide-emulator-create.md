---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-emulator-create
title: 创建模拟器
breadcrumb: 指南 > 编写与调试应用 > 使用模拟器运行应用 > 管理模拟器 > 创建模拟器
category: harmonyos-guides
scraped_at: 2026-04-28T07:56:42+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:c19cd55bcf44bf7589d5c3ddc1ac2d517dad9f386219d716f1402b4298939e38
---

有网络环境可参考以下步骤创建模拟器，如果是无网络环境，请查看[离线部署模拟器](ide-emulator-no-network.md)。

说明

在macOS中，您可能在活动监视器中发现模拟器进程占用的内存超过设置的内存。实际上，活动监视器中的**Memory**并不代表模拟器进程实际使用的物理内存，更多详情请参考[macOS上活动监视器中显示模拟器内存偏高](../harmonyos-faqs/faqs-app-running-23.md)。

## 使用预置的模拟器

从DevEco Studio 6.1.0 Beta2版本开始，如果本地没有模拟器，DevEco Studio会预置模拟器，开发者无需创建即可快速使用。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/DpzGmgslRiytyqDpA4zcnA/zh-cn_image_0000002561831007.png?HW-CC-KV=V1&HW-CC-Date=20260427T235641Z&HW-CC-Expire=86400&HW-CC-Sign=B407E4B712795131F10CD352C54F4559C28F5385B52ECFFD7DAB9C5900B4FCB2)

在设备选择框中，选择预置的模拟器并点击运行按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/-CClN3P4SyqqMC0B9WsN6g/zh-cn_image_0000002561751019.png?HW-CC-KV=V1&HW-CC-Date=20260427T235641Z&HW-CC-Expire=86400&HW-CC-Sign=59F36E74635C367295F9150FFE67161B8D800A47D27CAFBBDD83B408CDD9E92C)后，根据界面提示下载镜像，或点击菜单栏**Tools > Device Manager** >![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/ZeNSiZQvTaCkS6rouXESVw/zh-cn_image_0000002561751017.png?HW-CC-KV=V1&HW-CC-Date=20260427T235641Z&HW-CC-Expire=86400&HW-CC-Sign=72EC04E66AF30D97ACD1726019F09B63C794AF6B68EF677D9E4ACFEAC8D3A601)下载镜像后，即可快捷使用模拟器。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/q5l3U-yURvCvbiDWrCbdHA/zh-cn_image_0000002561831025.png?HW-CC-KV=V1&HW-CC-Date=20260427T235641Z&HW-CC-Expire=86400&HW-CC-Sign=0949AEB671F716CEC1504441F08C32507C78119EA8EC4707D7F24A114B330F05)

## 创建新的模拟器

1. 点击菜单栏的**Tools > Device Manager**，点击右下角的**Edit**设置模拟器实例的存储路径**Local Emulator Location**，Mac默认存储在~/.Huawei/Emulator/deployed下，Windows默认存储在C:\Users\xxx\AppData\Local\Huawei\Emulator\deployed下。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/elyVpVjfRvWdhK8euJIJgg/zh-cn_image_0000002530911088.png?HW-CC-KV=V1&HW-CC-Date=20260427T235641Z&HW-CC-Expire=86400&HW-CC-Sign=DF0740B42BB75E9AB7BD11DBA795D919B53A3AD066408B6C7245632487D6B490 "点击放大")
2. 在**Local Emulator**页签中，单击右下角的**New Emulator**按钮，创建一个模拟器。

   在模拟器配置界面，可以选择一个默认的设备模板，首次使用时请点击设备右侧的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/oy2v0RcdSwWvqpE-RqvHbQ/zh-cn_image_0000002561831017.png?HW-CC-KV=V1&HW-CC-Date=20260427T235641Z&HW-CC-Expire=86400&HW-CC-Sign=B1483EA94695A83647CD93659B1C8C9B9747FFEB8781D94562B0BE903D762256)下载模拟器镜像，您也可以在该界面更新或删除不同设备的模拟器镜像。

   单击**Edit**可以设置镜像文件的存储路径。macOS默认存储在~/Library/Huawei/Sdk下，Windows默认存储在C:\Users\xxx\AppData\Local\Huawei\Sdk下。

   说明

   如果配置界面显示异常，例如设备列表为空等，可先关闭DevEco Studio，并进入~/Library/Huawei（Windows路径为C:\Users\xxx\AppData\Local\Huawei）目录，删除DevEcoStudiox.x文件夹（如DevEcoStudio6.0，具体文件夹名称和安装的DevEco Studio版本相关）以清理缓存。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/3ZtV0eSoQtCmc1iJSu-w8Q/zh-cn_image_0000002561751027.png?HW-CC-KV=V1&HW-CC-Date=20260427T235641Z&HW-CC-Expire=86400&HW-CC-Sign=A081DFDDBDB41205FA0862B09D3B6B64306DACD14041BA5DD6E770EE9CAD8D0E)
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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/syUWeKDBTomAuNZyEJSXOA/zh-cn_image_0000002530751096.png?HW-CC-KV=V1&HW-CC-Date=20260427T235641Z&HW-CC-Expire=86400&HW-CC-Sign=8A2A3AB626F6EE86945F5B9A2A2A06C9729C3AAEE55E278429CB461D5CE49816)
4. 启动模拟器，有两种方式。
   * 从DevEco Studio 6.1.0 Beta2版本开始，创建后的模拟器会展示在设备列表中（最多10个），选择模拟器后，点击运行按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/cfq4lfMTSxGCABcKWLVH0g/zh-cn_image_0000002561831021.png?HW-CC-KV=V1&HW-CC-Date=20260427T235641Z&HW-CC-Expire=86400&HW-CC-Sign=92914C98D0D2926482AD1D85C197924525928E33337454067291BFEE7FD30843)，即可一键完成启动模拟器、编译构建、推包运行操作。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/csxwsMApRoufdJF9g9nWmg/zh-cn_image_0000002561831023.png?HW-CC-KV=V1&HW-CC-Date=20260427T235641Z&HW-CC-Expire=86400&HW-CC-Sign=DCB33EC60AF8E1231B4AE20963DD86FB196C98F22CFE8F429932609AE2D310CE)
   * 在设备管理器页面，单击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/ByEgM05VScCagOHCsGHZ5Q/zh-cn_image_0000002561751047.png?HW-CC-KV=V1&HW-CC-Date=20260427T235641Z&HW-CC-Expire=86400&HW-CC-Sign=95B327C12352BCF2D15375AC5E1BEC2C4B27D023D731E0E85962D8FE3FB3D607)启动模拟器。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/6MvK_zDtRF20fAlMQ_05uA/zh-cn_image_0000002530751084.png?HW-CC-KV=V1&HW-CC-Date=20260427T235641Z&HW-CC-Expire=86400&HW-CC-Sign=53F598ADCC401AE9F33F0848FC2F7AF5016706A6138FEF15A0A3F88DC4C541CA "点击放大")
5. 单击DevEco Studio的**Run > Run'模块名称'**或![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/NzC_qYm0SNSCS_0WZ0yvtQ/zh-cn_image_0000002530911078.png?HW-CC-KV=V1&HW-CC-Date=20260427T235641Z&HW-CC-Expire=86400&HW-CC-Sign=6328C9A6384C035BFAA0F98C55ED6B30B4655474024BDD95CCB88AF0F7240595)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/BSsw-w0vTgSVU-PT2niHSQ/zh-cn_image_0000002530751074.png?HW-CC-KV=V1&HW-CC-Date=20260427T235641Z&HW-CC-Expire=86400&HW-CC-Sign=F3E6CAF40B1031F934712EEB8940147B9E1C19FE5F74533DA9D4022752E3EB5F)
6. DevEco Studio会启动应用/元服务的编译构建与推包，完成后应用/元服务即可运行在模拟器上。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/6HHiXIR3Qeq-liNsInAoZQ/zh-cn_image_0000002530911086.png?HW-CC-KV=V1&HW-CC-Date=20260427T235641Z&HW-CC-Expire=86400&HW-CC-Sign=74AE6ACBDDBA7C51732AC69CAEBD73FA5EB558BEE5A975CBDB9856F514AE823D)
