---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-emulator-customize-screen-configuration
title: 自定义屏幕配置
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 使用模拟器运行应用 > 修改模拟器 > 自定义屏幕配置
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:a3c2273828543d542ba7816936b52491e490bc7941e2167f0c0e7e833a85f8be
---

从DevEco Studio 6.0.0 Beta1版本开始，模拟器支持自定义屏幕配置，支持在创建新的模拟器时自定义，具体请参考[创建模拟器](ide-emulator-create.md)，或者对已创建的模拟器进行修改，具体参考以下步骤。

## 使用约束

* Phone类型的模拟器支持自定义屏幕配置。
* 从DevEco Studio 6.0.1 Beta1版本开始，新增Foldable、Tablet和2in1类型的模拟器支持自定义屏幕配置。
* 从26.0.0版本开始，新增Car类型的模拟器支持自定义屏幕配置。

## 操作步骤

1. 在模拟器关闭状态下，点击模拟器的修改按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/LJ1OjrzgTQqRkhb5mAAQug/zh-cn_image_0000002808884717.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=49E4C44B1CA8E50F2CDB3B643DB2E0403AF6E4259AB4F5AC1647951BD4F082F1)，进入Virtual Device Configure界面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a/v3/HPh6jw35Slmjq-974Fz-qA/zh-cn_image_0000002779405086.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=1A218EF377257AF0310D36C2AD481A34CEE48F76F49F9CB2A43721DE0F437B8C "点击放大")
2. 点击**Customize**按钮，可以自定义设备的屏幕尺寸、分辨率和DPI配置，取值范围参考界面提示。
   * **Screen size：**屏幕的对角线长度，单位为inch。
   * **Resolution**：分辨率，宽度和高度，单位为px。
   * **DPI**：像素密度，DPI 越高，UI组件占用的像素点越多，从而提供更精细的显示效果。

   确认所有参数后，点击**Finish**完成修改，并保存为新的预置配置。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/K1UUl73lRhKKwZe4OA0AbQ/zh-cn_image_0000002779565060.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=A9AE4EBC43568B93577CCC9D69E40BFB5328AAEB8B8F9AA47CB1661849E2424B "点击放大")
