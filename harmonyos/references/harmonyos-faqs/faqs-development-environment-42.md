---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-development-environment-42
title: DevEco Studio如何调整页面窗口布局
breadcrumb: FAQ > DevEco Studio > 环境准备 > DevEco Studio如何调整页面窗口布局
category: harmonyos-faqs
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:2b276fed5b400fe31fbae14beb37be7baec0c3a394709acc39f4a9597d0813d3
---

## 问题现象

* 问题一：侧边按键被删除后如何恢复？例如日志按钮。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/SNcbBfFfTCqvOXF6TTVQOw/zh-cn_image_0000002628565334.png?HW-CC-KV=V1&HW-CC-Date=20261112T233212Z&HW-CC-Expire=31536000000&HW-CC-Sign=F451B9BD61AFD4DDB10365AEBA619852575CF5210B14296D7A91132ED6EF7AF9 "点击放大")
* 问题二：日志窗口侧边功能按钮被删除后如何恢复？

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/hHXeKYaFRCOO7p98l6DI6A/zh-cn_image_0000002628405432.png?HW-CC-KV=V1&HW-CC-Date=20261112T233212Z&HW-CC-Expire=31536000000&HW-CC-Sign=FBF3533B78E0FC70C9A19AA9D5D659DFEC672464CDB433004312DD4C2BC288EC "点击放大")
* 问题三：需要结合断点和日志信息进行调试，如何设置调试界面和日志输出界面同时在底部展示？
  + 调试窗口：

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/n6nQJSrMSuOr2ifeUnRgAQ/zh-cn_image_0000002658924639.png?HW-CC-KV=V1&HW-CC-Date=20261112T233212Z&HW-CC-Expire=31536000000&HW-CC-Sign=D4DAAFC38FA93B9131263EE72D0C6FDB9F04A1B0A0E55F3C82B8BC5A9290D423 "点击放大")
  + 日志窗口：

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/YZgdCKg_QBupqyn9vFUoZA/zh-cn_image_0000002658804703.png?HW-CC-KV=V1&HW-CC-Date=20261112T233212Z&HW-CC-Expire=31536000000&HW-CC-Sign=28ADDC659C0CAC535142234E8859D4062B3BC3EDDA62B162115B41AFC68A1986 "点击放大")
* 问题四：日志窗口中按键分别对应什么能力？

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/DBwUpA0zR5CwFENUAI6jTg/zh-cn_image_0000002628565336.png?HW-CC-KV=V1&HW-CC-Date=20261112T233212Z&HW-CC-Expire=31536000000&HW-CC-Sign=3D1108BD914343C0DB1600778803FFB357926257D888993F19E8B94F675A3827)

## 背景知识

[DevEco Studio集成开发环境](../harmonyos-guides/ide-tools-overview.md#section268251193716)：HUAWEI DevEco Studio（获取工具请单击链接下载，以下简称DevEco Studio）是基于IntelliJ IDEA Community开源版本打造，面向HarmonyOS应用/元服务开发场景的一站式集成开发环境。提供AI辅助编程、编译构建、UI实时预览、代码调试、性能调优、模拟器等功能，帮助你高效开发HarmonyOS应用/元服务。

## 解决方案

* 问题一：通过**视图**-**工具窗口**-**日志**或者**Ctrl+Alt+5**重新打开日志窗口。
  + 操作：

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/HDx7ZaQ5RHmexM0jbdbUrw/zh-cn_image_0000002628405434.png?HW-CC-KV=V1&HW-CC-Date=20261112T233212Z&HW-CC-Expire=31536000000&HW-CC-Sign=C6FC3C5E5172D0E78DD01D2A280230B9AF4A61BE4D37737CC17D2A3790883CD7 "点击放大")
  + 效果：

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/q2tMSaNMQeK8QfYixyH5Sw/zh-cn_image_0000002658924641.png?HW-CC-KV=V1&HW-CC-Date=20261112T233212Z&HW-CC-Expire=31536000000&HW-CC-Sign=46C7D66822219678562E277ABF834AE087B3B8BFE01BD6D228834F5EFCCB983C "点击放大")
* 问题二：通过将鼠标移动至日志窗口内，点击右上角三点显示菜单选项图标，或者鼠标右键点击日志窗口顶部，选中**显示工具栏**。
  + 操作：

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/jUIljK9EQNChD_LlRDQ98A/zh-cn_image_0000002658804705.png?HW-CC-KV=V1&HW-CC-Date=20261112T233212Z&HW-CC-Expire=31536000000&HW-CC-Sign=B63AC11EA3D1C6388A09662B575DFBF9D56BAB24DB4EBB7B442EA56F046026A1 "点击放大")
  + 效果：

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1f/v3/9B_p9l83Rc2OxILEuVtH-w/zh-cn_image_0000002628565338.png?HW-CC-KV=V1&HW-CC-Date=20261112T233212Z&HW-CC-Expire=31536000000&HW-CC-Sign=069DFC015897CE313DD85B5F8CB0A74AE34A54DD3905714E52BCA0AECE818A6D "点击放大")
* 问题三：通过将鼠标移动至日志窗口内，点击右上角三点显示菜单选项图标，或者鼠标右键点击日志窗口顶部，选中**移动到**，调整窗口位置，可选择**底部 右**。
  + 操作：

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/LYBLBvpdR_CSl-XugfHuGA/zh-cn_image_0000002628405436.png?HW-CC-KV=V1&HW-CC-Date=20261112T233212Z&HW-CC-Expire=31536000000&HW-CC-Sign=89F62B793AF75AD631E6EF9F58000DB2A63813441D752E527D6CBD2BB4B1BE84 "点击放大")
  + 效果：

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/Xg6nM-S5QzaAiAvUFVIexw/zh-cn_image_0000002658924643.png?HW-CC-KV=V1&HW-CC-Date=20261112T233212Z&HW-CC-Expire=31536000000&HW-CC-Sign=4B4E8C0DDCCD1B44AFF828C95886E36D12900DFAEE1B6E10E9D6573C8CE43F09 "点击放大")
* 问题四：通过将鼠标移动至日志窗口内，点击右上角三点显示菜单选项图标，或者鼠标右键点击日志窗口顶部，点击\*\*？帮助\*\*，即可跳转至文档介绍。
  + 操作：

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/VKf6Z-3OQ2K5cRxWER5ozg/zh-cn_image_0000002658804707.png?HW-CC-KV=V1&HW-CC-Date=20261112T233212Z&HW-CC-Expire=31536000000&HW-CC-Sign=D46376B8AA11DD8C0F6C036130A523DE18E14B2670C07FB27A161E9FE0C9D525 "点击放大")
  + 效果：

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b8/v3/fdHGr_KvTguKLvATl-SAyg/zh-cn_image_0000002628565340.png?HW-CC-KV=V1&HW-CC-Date=20261112T233212Z&HW-CC-Expire=31536000000&HW-CC-Sign=0B931A3E1137B27F46FC5823C656143F32234922143793A5B235C33A8BF35D5D "点击放大")
