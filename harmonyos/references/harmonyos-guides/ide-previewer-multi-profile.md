---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-previewer-multi-profile
title: 查看多端设备预览效果
breadcrumb: 指南 > 编写与调试应用 > 界面预览 > 查看多端设备预览效果
category: harmonyos-guides
scraped_at: 2026-04-28T07:56:37+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:85c957e3a9127bdd7f5ebacda15400490f31bb31fb3733e8e5f3662cb5f44ba1
---

DevEco Studio支持HarmonyOS分布式应用/元服务开发，同一个应用/元服务可以运行在多个设备上。在HarmonyOS分布式应用/元服务的开发阶段，因不同设备的屏幕分辨率、形状、大小等不同，开发者需要在不同的设备上查看应用/元服务的UI布局和交互效果，此时便可以使用多端设备预览器功能，方便开发者在应用/元服务开发过程中，随时查看不同设备上的界面显示效果。

说明

多端设备预览最多同时支持4个设备的预览。

前面介绍了DevEco Studio支持ArkTS、JS应用/元服务的预览器功能，多端设备预览器支持ArkTS、JS应用/元服务在不同设备上的同时预览。如果两个设备支持的编码语言不同，就不能使用多端设备预览功能。

下面以ArkTS应用/元服务为例，介绍多端设备预览器的使用方法，JS应用/元服务的多端设备预览器使用方法相同。

1. 在工程目录中，打开任意一个ets文件（JS请打开hml/css/js文件）。
2. 可以通过如下任意一种方式打开预览器开关，显示效果如下图所示：
   * 通过菜单栏，单击**View > Tool Windows > Previewer**，打开预览器。
   * 在编辑窗口右上角的侧边工具栏，单击**Previewer**，打开预览器。
3. 在Previewer窗口中，打开Profile Manager中的**Multi-profile preview**开关，同时查看多设备上的应用/元服务运行效果。

   说明

   多端设备预览不支持动画的预览，如果需要查看动画在设备上的预览效果，请关闭Multi-profile preview功能后在单设备预览界面进行查看。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/TYGkJ3byQ-6hutr_KU6Oeg/zh-cn_image_0000002561752931.png?HW-CC-KV=V1&HW-CC-Date=20260427T235636Z&HW-CC-Expire=86400&HW-CC-Sign=71D9E55F5E78C1C8474B6A7195AE055ADBB0DE450C40FCE3EEED26F3B269A470)

   多设备预览效果如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/iiOy9rzuR2anuX741kMskQ/zh-cn_image_0000002530912994.gif?HW-CC-KV=V1&HW-CC-Date=20260427T235636Z&HW-CC-Expire=86400&HW-CC-Sign=E750B1E4908A53911425C904CF13ED0ADEE3C19E37F06ACC990EED78736669DD "点击放大")
