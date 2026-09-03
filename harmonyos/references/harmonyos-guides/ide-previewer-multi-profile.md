---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-previewer-multi-profile
title: 查看多端设备预览效果
breadcrumb: 指南 > 编写与调试应用 > 界面预览 > 查看多端设备预览效果
category: harmonyos-guides
scraped_at: 2026-09-04T06:27:15+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:2215febb0ef56b0cfb71c280ddf28bfcb207fe654ca33f680104f6d7fc606076
---

DevEco Studio支持HarmonyOS分布式应用/元服务开发，同一个应用/元服务可以运行在多个设备上。在HarmonyOS分布式应用/元服务的开发阶段，因不同设备的屏幕分辨率、形状、大小等不同，开发者需要在不同的设备上查看应用/元服务的UI布局和交互效果，此时便可以使用多端设备预览器功能，方便开发者在应用/元服务开发过程中，随时查看不同设备上的界面显示效果。

**说明** 

多端设备预览最多同时支持4个设备的预览。

前面介绍了DevEco Studio支持ArkTS、JS应用/元服务的预览器功能，多端设备预览器支持ArkTS、JS应用/元服务在不同设备上的同时预览。如果两个设备支持的编码语言不同，就不能使用多端设备预览功能。

下面以ArkTS应用/元服务为例，介绍多端设备预览器的使用方法，JS应用/元服务的多端设备预览器使用方法相同。

1. 在工程目录中，打开任意一个ets文件（JS请打开hml/css/js文件）。
2. 可以通过如下任意一种方式打开预览器开关，显示效果如下图所示：
   * 通过菜单栏，单击**View > Tool Windows > Previewer**，打开预览器。
   * 在编辑窗口右上角的侧边工具栏，单击**Previewer**，打开预览器。
3. 在Previewer窗口中，打开Profile Manager中的**Multi-profile preview**开关，同时查看多设备上的应用/元服务运行效果。

   **说明** 

   多端设备预览不支持动画的预览，如果需要查看动画在设备上的预览效果，请关闭Multi-profile preview功能后在单设备预览界面进行查看。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/UccrWrT5T_G0G7YVDjjMDQ/zh-cn_image_0000002731542459.png "点击放大")

   多设备预览效果如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/hAeS9aXrQS2YKOKhYsaKGA/zh-cn_image_0000002731382487.gif "点击放大")
