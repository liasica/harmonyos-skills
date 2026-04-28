---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-debug-native-reverse
title: 反向调试
breadcrumb: 指南 > 编写与调试应用 > 应用调试 > 代码调试 > Native代码调试 > 反向调试
category: harmonyos-guides
scraped_at: 2026-04-28T07:56:50+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:9e6593c479db93f81f7e9ee952eb82f228bb4f5a4601f7c3272466a6af368b37
---

针对C/C++开发场景，DevEco Studio在提供基础调试能力的基础上，同时提供反向调试能力，帮助开发者更好地理解代码和更迅速定位问题。

反向调试是指在调试过程中可以回退到历史行和历史断点，查看历史调试信息，包括线程、堆栈和变量信息。支持的调试操作为：

* 进入/退出反向调试模式
* 反向Step Over回退到历史行
* 反向Resume执行到历史断点
* 在程序执行历史的记录点上查看全局、静态、局部变量值

## 前提条件

在**File > Settings**（macOS为**DevEco Studio > Preferences/Settings**） **> Build,Execution,Deployment > Debugger > C++ Debugger**设置界面，勾选**Enable time travel debug**开启C++反向调试开关。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/8ZB1pT8AQ5ywZOgTbjsWqQ/zh-cn_image_0000002561752669.png?HW-CC-KV=V1&HW-CC-Date=20260427T235649Z&HW-CC-Expire=86400&HW-CC-Sign=685BB6C31F69CA86EB0AE729A3F95D6BB8C47F596B5665E39A40AD3B1AB5FBBC)

## 操作步骤

1. 设置断点，进入调试模式。
2. 开启反向调试开关后，在Debugger中会出现反向调试相关按钮。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/qcqGVIN3S028Mwec0Gailw/zh-cn_image_0000002561752665.png?HW-CC-KV=V1&HW-CC-Date=20260427T235649Z&HW-CC-Expire=86400&HW-CC-Sign=58E54D908BD577A0C12D938D72E8B65284783195BACCED50543C09F6515241C7)

   需要查看历史调试信息时，点击“Open Time Travel Debug”按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/EZsI8P5PQVGca0mLFrV_Sw/zh-cn_image_0000002561752673.png?HW-CC-KV=V1&HW-CC-Date=20260427T235649Z&HW-CC-Expire=86400&HW-CC-Sign=FCD49142FC25B4F8A9219E7A46DA4C2E2A90515627DFCBBD38577E8B9C2CFD18)进入反向调试模式，您可以在此模式下进行调试。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/iOqelmwHSv2JqH_ieVAa4Q/zh-cn_image_0000002530752728.png?HW-CC-KV=V1&HW-CC-Date=20260427T235649Z&HW-CC-Expire=86400&HW-CC-Sign=080C58FD1B86AE586A525C1458003838559223E4E6F930142301444AA3A8E31D)

   其中，操作按钮说明如下：

   * ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/AROU4Eg4QLKxt4pbzxpdLQ/zh-cn_image_0000002561752677.png?HW-CC-KV=V1&HW-CC-Date=20260427T235649Z&HW-CC-Expire=86400&HW-CC-Sign=B89530330C764978F9314E5BEA057B1EC38E2101BE6F3BC7FE485CB7670C7A81)：退出反向调试模式。
   * ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/VNWYh00ARaqnKXzTdQauIw/zh-cn_image_0000002530912734.png?HW-CC-KV=V1&HW-CC-Date=20260427T235649Z&HW-CC-Expire=86400&HW-CC-Sign=E518B69CDF9AD94F7E366934F75B251BA822C29BF32D0417C342D9F4BF69920E)：切换当前高亮行到下一个历史断点，并显示断点相关信息。
   * ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a7/v3/moCMTjwJSfGZyKOJjULqBQ/zh-cn_image_0000002530752742.png?HW-CC-KV=V1&HW-CC-Date=20260427T235649Z&HW-CC-Expire=86400&HW-CC-Sign=FEAC47B420387C9DBF5D15684FABF297425F0AD5DB3FA80E1023C18329A3801E)：切换当前高亮行到上一个历史断点，并显示断点相关信息。
   * ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/ju5YKU0ZRue44LwQ0XMrOQ/zh-cn_image_0000002561832645.png?HW-CC-KV=V1&HW-CC-Date=20260427T235649Z&HW-CC-Expire=86400&HW-CC-Sign=164888E6DCEE1EDF5A194B664F5F9DEB3A3C61EB07C069B340E1062BB5C64CE2)：切换当前高亮行到下一个历史行，并显示历史行相关信息。
   * ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/jz2TEz6zSQaQbiPkLL2zlg/zh-cn_image_0000002561752671.png?HW-CC-KV=V1&HW-CC-Date=20260427T235649Z&HW-CC-Expire=86400&HW-CC-Sign=88ED80B9F589F245BF1097838C19EE88A2C1CCC0F7A466D4AE6574AB4B00E24E)：切换当前高亮行到上一个历史行，并显示历史行相关信息。

说明

某些功能在反向调试模式下无法使用，此时会根据您的行为进行对应提示。
