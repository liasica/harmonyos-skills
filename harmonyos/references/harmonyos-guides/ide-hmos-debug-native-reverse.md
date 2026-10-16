---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-debug-native-reverse
title: 反向调试
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 应用调试 > 代码调试 > Native代码调试 > 反向调试
category: harmonyos-guides
scraped_at: 2026-10-17T06:43:47+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:267a44dab1a5113d968f86cd31be9cb36431427657a80bea9ccf40976e035116
---

针对C/C++开发场景，鸿蒙电脑DevEco Studio在提供基础调试能力的基础上，同时提供反向调试能力，帮助开发者更好地理解代码和更迅速定位问题。

反向调试是指在调试过程中可以回退到历史行和历史断点，查看历史调试信息，包括线程、堆栈和变量信息。支持的调试操作为：

* 进入/退出反向调试模式。
* 反向Step Over回退到历史行。
* 反向Resume执行到历史断点。
* 在程序执行历史的记录点上查看全局、静态、局部变量值。

## 前提条件

在**文件 > 设置 > 扩展 > C++调试**界面，勾选**开启反向调试**后点击**应用**，开启C++反向调试开关。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/JrXoUW-WQ5a0BHuXPqW5Vw/zh-cn_image_0000002779728843.png)

## 操作步骤

1. 设置断点，进入调试模式。
2. 开启反向调试开关后，在调试器中会出现反向调试相关按钮。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/SBd4fnQ9QPyt5qUb9SOvlA/zh-cn_image_0000002779608691.png "点击放大")

   需要查看历史调试信息时，点击“Open Reverse Mode”按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/nZOVklz_SmabSMFDsnqblQ/zh-cn_image_0000002750169668.png "点击放大")进入反向调试模式，您可以在此模式下进行调试。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/qmis5IGoTEC6xawUQKPvdg/zh-cn_image_0000002750009786.png)

   其中，操作按钮说明如下：
   * ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/6mvtmV7WSgSlwReLwT7i8A/zh-cn_image_0000002779608699.png)：退出反向调试模式。
   * ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/aw-0Ad6FSrSuwKvKsYa4Iw/zh-cn_image_0000002750009784.png "点击放大")：切换当前高亮行到下一个历史断点，并显示断点相关信息。
   * ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/kT4pXauISyysreTyVCahVQ/zh-cn_image_0000002750009788.png "点击放大")：切换当前高亮行到上一个历史断点，并显示断点相关信息。
   * ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/0lDAfMAJRaudpQ7Hp_O-Qw/zh-cn_image_0000002779608695.png "点击放大")：切换当前高亮行到下一个历史行，并显示历史行相关信息。
   * ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/04/v3/hoI43I3WQIe13EnOQ6QqEA/zh-cn_image_0000002750009782.png)：切换当前高亮行到上一个历史行，并显示历史行相关信息。

## 时间线视图

进入反向调试模式后，支持C++调试流程中停留过的历史断点和历史行之间的跳转和调试信息查看。

图中的红点表示历史停留过的断点或行，点击跳转到对应断点或行，并显示相关栈帧信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/Tudnio4KRw-rgxysGOaAVQ/zh-cn_image_0000002779608697.png)
