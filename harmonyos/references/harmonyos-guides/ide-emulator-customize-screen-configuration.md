---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-emulator-customize-screen-configuration
title: 自定义屏幕配置
breadcrumb: 指南 > 编写与调试应用 > 使用模拟器运行应用 > 修改模拟器 > 自定义屏幕配置
category: harmonyos-guides
scraped_at: 2026-04-29T13:46:38+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:b1b56b297a54c60786e40e455d356bd3df943e4cbd7ead5510f562d9e1152f17
---

从DevEco Studio 6.0.0 Beta1版本开始，模拟器支持自定义屏幕配置，支持在创建新的模拟器时自定义，具体请参考[创建模拟器](ide-emulator-create.md)，或者对已创建的模拟器进行修改，具体参考以下步骤。

## 使用约束

* phone类型的模拟器支持自定义屏幕配置。
* 从DevEco Studio 6.0.1 Beta1版本开始，新增foldable、tablet和2in1类型的模拟器支持自定义屏幕配置。

## 操作步骤

1. 在模拟器关闭状态下，点击模拟器的修改按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/ENf7ZnElSqCAnEL6XLUlKQ/zh-cn_image_0000002561830993.png?HW-CC-KV=V1&HW-CC-Date=20260429T054637Z&HW-CC-Expire=86400&HW-CC-Sign=45327969BA098379B2C7BE59A9A77F7494DB24BAF8A79A535857F51F0E8688A2)，进入Virtual Device Configure界面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6a/v3/bgYDkgBrTm69EWD9XsNsFQ/zh-cn_image_0000002561830999.png?HW-CC-KV=V1&HW-CC-Date=20260429T054637Z&HW-CC-Expire=86400&HW-CC-Sign=F5263BF253C4688A7053B7AAADAE67164411FF40BD2F48BE1527B921CAE28644 "点击放大")
2. 点击**Customize**按钮，可以自定义设备的屏幕尺寸、分辨率和DPI配置，取值范围参考界面提示。
   * **Screen size：**屏幕的对角线长度，单位为inch。
   * **Resolution**：分辨率，宽度和高度，单位为px。
   * **DPI**：像素密度，DPI 越高，UI组件占用的像素点越多，从而提供更精细的显示效果。

   确认所有参数后，点击**Finish**完成修改，并保存为新的预置配置。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/xLXmeEcRQdSVafRtqjEshg/zh-cn_image_0000002530911070.png?HW-CC-KV=V1&HW-CC-Date=20260429T054637Z&HW-CC-Expire=86400&HW-CC-Sign=638437E245D4A893B414AA9338FD7EE246F1995BDD03FFCA922F36AC4CB0A759 "点击放大")
