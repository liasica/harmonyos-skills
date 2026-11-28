---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-debug-native-reverse
title: 反向调试
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 应用调试 > 代码调试 > Native代码调试 > 反向调试
category: harmonyos-guides
scraped_at: 2026-11-28T10:34:55+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:80d885381e21b48e68435747f7096ebb814a11aea000e44ccf6e0ae302cdf7e8
---

针对C/C++开发场景，鸿蒙电脑DevEco Studio在提供基础调试能力的基础上，同时提供反向调试能力，帮助开发者更好地理解代码和更迅速定位问题。

反向调试是指在调试过程中可以回退到历史行和历史断点，查看历史调试信息，包括线程、堆栈和变量信息。支持的调试操作为：

* 进入/退出反向调试模式。
* 反向Step Over回退到历史行。
* 反向Resume执行到历史断点。
* 在程序执行历史的记录点上查看全局、静态、局部变量值。

## 前提条件

在**文件 > 设置 > 扩展 > C++调试**界面，勾选**开启反向调试**后点击**应用**，开启C++反向调试开关。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/t4Nfsf9RRMKVP5p2Ju_h7g/zh-cn_image_0000002820680965.png?HW-CC-KV=V1&HW-CC-Date=20261128T023455Z&HW-CC-Expire=31536000000&HW-CC-Sign=784B27EEE9C9ED0E3DF487B968DB50AE7EB87CF14CD7BFBB39DBB91067CEC150)

## 操作步骤

1. 设置断点，进入调试模式。
2. 开启反向调试开关后，在调试器中会出现反向调试相关按钮。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/W7d6HIh3SHaGU8o9iXyYwg/zh-cn_image_0000002820720977.png?HW-CC-KV=V1&HW-CC-Date=20261128T023455Z&HW-CC-Expire=31536000000&HW-CC-Sign=EF0529399EBF7DFE68B7DBC82533B05EF729C909A3608936E4F4A87447AAD389 "点击放大")

   需要查看历史调试信息时，点击“Open Reverse Mode”按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f7/v3/4_7syzL6SUWB5vOhhWNI-A/zh-cn_image_0000002792001014.png?HW-CC-KV=V1&HW-CC-Date=20261128T023455Z&HW-CC-Expire=31536000000&HW-CC-Sign=4A4143AE3348EF005E1B0A984A41083F2A529E0CAFE0B2F8BD36B1850ED65175 "点击放大")进入反向调试模式，您可以在此模式下进行调试。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/udIYWb6WR0Wby01F2lqLsw/zh-cn_image_0000002791841030.png?HW-CC-KV=V1&HW-CC-Date=20261128T023455Z&HW-CC-Expire=31536000000&HW-CC-Sign=0DF92A37BCC9AC49476A9C409EEF5FF07DF27474A47E56EA12BC6FF193E65C67)

   其中，操作按钮说明如下：
   * ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/ZK-B3OZaSe-VuTusUtqNDw/zh-cn_image_0000002791841038.png?HW-CC-KV=V1&HW-CC-Date=20261128T023455Z&HW-CC-Expire=31536000000&HW-CC-Sign=91A391F964A0AF269B19ED81371547C7CBB240787762B86F484B110E277F084D)：退出反向调试模式。
   * ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/ZWLq7mcsRpSKOxub83Unlg/zh-cn_image_0000002820680967.png?HW-CC-KV=V1&HW-CC-Date=20261128T023455Z&HW-CC-Expire=31536000000&HW-CC-Sign=21BF86892A8BFCE81DE00F78AE59EA9B9D3EE49B5BF1A69AEEAE2D836AD3D6FD "点击放大")：切换当前高亮行到下一个历史断点，并显示断点相关信息。
   * ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/GS9TL2c9TfOQ1O1oaG2qSg/zh-cn_image_0000002791841034.png?HW-CC-KV=V1&HW-CC-Date=20261128T023455Z&HW-CC-Expire=31536000000&HW-CC-Sign=C3CE81F273376B191DECEC25F93C10D001B6B417794EBDCDD9F57B5BD76D65D5 "点击放大")：切换当前高亮行到上一个历史断点，并显示断点相关信息。
   * ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/d4HtAlsfTzuTmEqhf-PpHQ/zh-cn_image_0000002820680971.png?HW-CC-KV=V1&HW-CC-Date=20261128T023455Z&HW-CC-Expire=31536000000&HW-CC-Sign=E67BEECD1A71865994E2DDF3791BBE70987388FE42E5A3B8751DBB55A085C8C2 "点击放大")：切换当前高亮行到下一个历史行，并显示历史行相关信息。
   * ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/P9kYtqjPTEajSkVvgeyfAw/zh-cn_image_0000002791841036.png?HW-CC-KV=V1&HW-CC-Date=20261128T023455Z&HW-CC-Expire=31536000000&HW-CC-Sign=FCF384E008DE445A4DCB0FE53375BA6565F6861C2C7A6D0B258DABA7047B172C)：切换当前高亮行到上一个历史行，并显示历史行相关信息。

## 时间线视图

进入反向调试模式后，支持C++调试流程中停留过的历史断点和历史行之间的跳转和调试信息查看。

图中的红点表示历史停留过的断点或行，点击跳转到对应断点或行，并显示相关栈帧信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/kciaZKTMSyme8f7ug9KAzQ/zh-cn_image_0000002792001012.png?HW-CC-KV=V1&HW-CC-Date=20261128T023455Z&HW-CC-Expire=31536000000&HW-CC-Sign=42772B30EB8EC26BEA7D0AA8B35F1D3AD2FF2C50DFC146586D65AAA13A0E65D2)
