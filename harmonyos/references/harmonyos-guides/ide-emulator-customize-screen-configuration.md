---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-emulator-customize-screen-configuration
title: 自定义屏幕配置
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 使用模拟器运行应用 > 修改模拟器 > 自定义屏幕配置
category: harmonyos-guides
scraped_at: 2026-11-24T12:42:29+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:af06036123eba26b3b9ca8e4fe7216530087f4949f47904e5c665450627c78b0
---

从DevEco Studio 6.0.0 Beta1版本开始，模拟器支持自定义屏幕配置，支持在创建新的模拟器时自定义，具体请参考[创建模拟器](ide-emulator-create.md)，或者对已创建的模拟器进行修改，具体参考以下步骤。

## 使用约束

* Phone类型的模拟器支持自定义屏幕配置。
* 从DevEco Studio 6.0.1 Beta1版本开始，新增Foldable、Tablet和2in1类型的模拟器支持自定义屏幕配置。
* 从26.0.0版本开始，新增Car类型的模拟器支持自定义屏幕配置。

## 操作步骤

1. 在模拟器关闭状态下，点击模拟器的修改按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/vWKDI4gDRJmIbiiFYgw9iA/zh-cn_image_0000002808884717.png?HW-CC-KV=V1&HW-CC-Date=20261124T044229Z&HW-CC-Expire=31536000000&HW-CC-Sign=96EB94DCD05A90D96349B4B929D76C8DFB36D385A7C1243A6473C021E9670173)，进入Virtual Device Configure界面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/BeiRRErFTL2ASQTL9uccyA/zh-cn_image_0000002779405086.png?HW-CC-KV=V1&HW-CC-Date=20261124T044229Z&HW-CC-Expire=31536000000&HW-CC-Sign=B81FE2EF9B8E6652737DC18F93038BF73F8409735FBB26316C8862716C01297F "点击放大")
2. 点击**Customize**按钮，可以自定义设备的屏幕尺寸、分辨率和DPI配置，取值范围参考界面提示。
   * **Screen size：**屏幕的对角线长度，单位为inch。
   * **Resolution**：分辨率，宽度和高度，单位为px。
   * **DPI**：像素密度，DPI 越高，UI组件占用的像素点越多，从而提供更精细的显示效果。

   确认所有参数后，点击**Finish**完成修改，并保存为新的预置配置。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/93soZZiaQemtn3Oq-R6UqA/zh-cn_image_0000002779565060.png?HW-CC-KV=V1&HW-CC-Date=20261124T044229Z&HW-CC-Expire=31536000000&HW-CC-Sign=4B414963F9D4C68724A9C353BB0C7D24A93AA82454526CA933BBEDC4471AF8DD "点击放大")
