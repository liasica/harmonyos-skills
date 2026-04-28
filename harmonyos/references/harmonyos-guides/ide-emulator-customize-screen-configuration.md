---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-emulator-customize-screen-configuration
title: 自定义屏幕配置
breadcrumb: 指南 > 编写与调试应用 > 使用模拟器运行应用 > 修改模拟器 > 自定义屏幕配置
category: harmonyos-guides
scraped_at: 2026-04-28T07:56:44+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:068bf1800250f3b6e288f133d841f7aaed0735b2242be664dcdd2f89f62d6e4b
---

从DevEco Studio 6.0.0 Beta1版本开始，模拟器支持自定义屏幕配置，支持在创建新的模拟器时自定义，具体请参考[创建模拟器](ide-emulator-create.md)，或者对已创建的模拟器进行修改，具体参考以下步骤。

## 使用约束

* phone类型的模拟器支持自定义屏幕配置。
* 从DevEco Studio 6.0.1 Beta1版本开始，新增foldable、tablet和2in1类型的模拟器支持自定义屏幕配置。

## 操作步骤

1. 在模拟器关闭状态下，点击模拟器的修改按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/47Emi_4VTh-EU3uyVzdwRg/zh-cn_image_0000002561830993.png?HW-CC-KV=V1&HW-CC-Date=20260427T235643Z&HW-CC-Expire=86400&HW-CC-Sign=8023F00E39C246CF435EB6EF986034543701A05B918898203779861F64306228)，进入Virtual Device Configure界面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/fWLj7fDMSOGvyEr5n4Mkug/zh-cn_image_0000002561830999.png?HW-CC-KV=V1&HW-CC-Date=20260427T235643Z&HW-CC-Expire=86400&HW-CC-Sign=8A2060AE31F8A3CD2894150EBDCC6B987A1F82CF1039AFA3FF5947ACF513D19E "点击放大")
2. 点击**Customize**按钮，可以自定义设备的屏幕尺寸、分辨率和DPI配置，取值范围参考界面提示。
   * **Screen size：**屏幕的对角线长度，单位为inch。
   * **Resolution**：分辨率，宽度和高度，单位为px。
   * **DPI**：像素密度，DPI 越高，UI组件占用的像素点越多，从而提供更精细的显示效果。

   确认所有参数后，点击**Finish**完成修改，并保存为新的预置配置。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/p16agZuLQpukpd4mBRKe_w/zh-cn_image_0000002530911070.png?HW-CC-KV=V1&HW-CC-Date=20260427T235643Z&HW-CC-Expire=86400&HW-CC-Sign=155FF30C586D49E5941B030C0905F799EEBAF6202D256CFCE243389641022471 "点击放大")
