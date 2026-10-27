---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-test-23
title: Hypium是否支持在模拟器上执行测试用例
breadcrumb: FAQ > DevEco Studio > 应用测试 > Hypium是否支持在模拟器上执行测试用例
category: harmonyos-faqs
scraped_at: 2026-10-28T07:49:01+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:194cf7c17a5f07c5cdde53fd8e0deddf944e8fbe06187169fbe546493da581ce
---

## 问题现象

Hypium自动化的测试用例是否支持在模拟器上运行以及如何操作。

## 背景知识

* [DevEco Studio](https://developer.huawei.com/consumer/cn/deveco-studio/)提供[使用模拟器](../harmonyos-guides/ide-emulator-use.md)（Emulator），为开发者提供了运行和调试HarmonyOS应用/元服务的便捷方式。模拟器还原了真实设备的基本功能，如屏幕旋转、音量调节、模拟的硬件传感器和指定设备的位置等。这使得您无需拥有不同类型的物理设备，就可以在各种虚拟环境中轻松测试您的应用程序。
* [DevEco Testing Hypium](../harmonyos-guides/hypium-python-guidelines.md#section16890204264419)以下简称（Hypium）是HarmonyOS平台的UI自动化测试框架，支持开发者使用python语言为应用编写UI自动化测试脚本。

## 解决方案

Hypium自动化测试用例支持在模拟器中运行。步骤如下：

1. 步骤一：DevEco Studio启动模拟器。

   点击菜单栏的Tools > Device Manager > Run如图：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/zCEy2FAPS12KOAs-eY-sjw/zh-cn_image_0000002658808819.png "点击放大")

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/KVzivaURR26NhSl71C7yPA/zh-cn_image_0000002628409552.png "点击放大")
2. 步骤二：PyCharm运行用例。

   模拟器启动后PyCharm可以查看本地模拟器已连接。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/flS6nxRLQlOsWL0l9wft1w/zh-cn_image_0000002628569450.png "点击放大")

   单台设备直接执行用例正常运行成功，同时模拟器正常展示用例运行过程。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0b/v3/FK5yh0ICR4uP7SUHhAN8pA/zh-cn_image_0000002658928767.png "点击放大")

   多台设备需在user\_config.xml指定运行设备的sn，若指定运行设备是模拟器配置如下：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/8yTC9h5eRhudJm-w5T7cAQ/zh-cn_image_0000002658808821.png "点击放大")
