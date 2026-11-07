---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-debug-native-reverse
title: 反向调试
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 应用调试 > 代码调试 > Native代码调试 > 反向调试
category: harmonyos-guides
scraped_at: 2026-11-07T08:02:22+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:3ab3c1700c903874bf280d3a212bc385f817d1cd1076eeca5a20b00e8813d8ee
---

针对C/C++开发场景，DevEco Studio在提供基础调试能力的基础上，同时提供反向调试能力，帮助开发者更好地理解代码和更迅速定位问题。

反向调试是指在调试过程中可以回退到历史行和历史断点，查看历史调试信息，包括线程、堆栈和变量信息。支持的调试操作为：

* 进入/退出反向调试模式
* 反向Step Over回退到历史行
* 反向Resume执行到历史断点
* 在程序执行历史的记录点上查看全局、静态、局部变量值

## 前提条件

在**File > Settings**（macOS为**DevEco Studio > Preferences/Settings**） **> Build,Execution,Deployment > Debugger > C++ Debugger**设置界面，勾选**Enable time travel debug**开启C++反向调试开关。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/Pcs_krYoTeyYtkAzz_xkKA/zh-cn_image_0000002731381937.png)

## 操作步骤

1. 设置断点，进入调试模式。
2. 开启反向调试开关后，在Debugger中会出现反向调试相关按钮。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/QG7PUSXvTpO408t87bKnBg/zh-cn_image_0000002731541901.png)

   需要查看历史调试信息时，点击“Open Time Travel Debug”按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/WyXejzuSQqelQzZ6Cb-s3w/zh-cn_image_0000002731541905.png)进入反向调试模式，您可以在此模式下进行调试。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/YdJS04DAQXyYKhYb4u0Ekw/zh-cn_image_0000002731381939.png)

   其中，操作按钮说明如下：

   * ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/07/v3/za9cIYz_T1qT9FW1NgNRJg/zh-cn_image_0000002731381941.png)：退出反向调试模式。
   * ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/47tIGbYKTY-oXPrp-oKGCw/zh-cn_image_0000002731541907.png)：切换当前高亮行到下一个历史断点，并显示断点相关信息。
   * ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ca/v3/5FvwJhPIQP-D2HuDYx4nTA/zh-cn_image_0000002731381931.png)：切换当前高亮行到上一个历史断点，并显示断点相关信息。
   * ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/Y3J2F2yaSEC2TdV0OIwxSA/zh-cn_image_0000002731541903.png)：切换当前高亮行到下一个历史行，并显示历史行相关信息。
   * ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/99/v3/SW18Q1HeSHKdXGOGcFqIVw/zh-cn_image_0000002731541911.png)：切换当前高亮行到上一个历史行，并显示历史行相关信息。

**说明** 

某些功能在反向调试模式下无法使用，此时会根据您的行为进行对应提示。
