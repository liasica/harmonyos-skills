---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-debug-native-reverse
title: 反向调试
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 应用调试 > 代码调试 > Native代码调试 > 反向调试
category: harmonyos-guides
scraped_at: 2026-11-24T12:42:30+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:60cd98d69cfc019cc807c9c09119cf766e36f39a305f8c03cf98503451caf56d
---

针对C/C++开发场景，DevEco Studio在提供基础调试能力的基础上，同时提供反向调试能力，帮助开发者更好地理解代码和更迅速定位问题。

反向调试是指在调试过程中可以回退到历史行和历史断点，查看历史调试信息，包括线程、堆栈和变量信息。支持的调试操作为：

* 进入/退出反向调试模式
* 反向Step Over回退到历史行
* 反向Resume执行到历史断点
* 在程序执行历史的记录点上查看全局、静态、局部变量值

## 前提条件

在**File > Settings**（macOS为**DevEco Studio > Preferences/Settings**） **> Build,Execution,Deployment > Debugger > C++ Debugger**设置界面，勾选**Enable time travel debug**开启C++反向调试开关。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f/v3/sfO51oJ2Q6ugu_gsoCV84A/zh-cn_image_0000002808886189.png?HW-CC-KV=V1&HW-CC-Date=20261124T044230Z&HW-CC-Expire=31536000000&HW-CC-Sign=9343D863D06FB883AD87AF83C81D01A47EC972F11845DE0458CDA80D0D73070A)

## 操作步骤

1. 设置断点，进入调试模式。
2. 开启反向调试开关后，在Debugger中会出现反向调试相关按钮。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/gqfYctOVSJ2Gso_MOO3Jvg/zh-cn_image_0000002808766105.png?HW-CC-KV=V1&HW-CC-Date=20261124T044230Z&HW-CC-Expire=31536000000&HW-CC-Sign=DB653662447E82A2793C4D80B8481A8E423F4EB07DE3CF65348ED6533B9A1085)

   需要查看历史调试信息时，点击“Open Time Travel Debug”按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9/v3/C4BhXS7mRb-V-QUBcl24EQ/zh-cn_image_0000002808766109.png?HW-CC-KV=V1&HW-CC-Date=20261124T044230Z&HW-CC-Expire=31536000000&HW-CC-Sign=3448E5F6444F9D74FE2FE5CD37BA8848CD9F4D9782A1931F64985492B5EE5A8E)进入反向调试模式，您可以在此模式下进行调试。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/44SUk8W6S9WGpwJu0e2GBw/zh-cn_image_0000002779406548.png?HW-CC-KV=V1&HW-CC-Date=20261124T044230Z&HW-CC-Expire=31536000000&HW-CC-Sign=25BF23D5552175C61F7526609A582D23D72A5A0585BEAAB1A7909D1FFB1D1C27)

   其中，操作按钮说明如下：

   * ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/vHIYNK1mQYeTh_IZn7NStQ/zh-cn_image_0000002779406552.png?HW-CC-KV=V1&HW-CC-Date=20261124T044230Z&HW-CC-Expire=31536000000&HW-CC-Sign=B77C82D9B33E950026298FE0F7464E1A4BDCCCFE9AE730112700175C67415E0F)：退出反向调试模式。
   * ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/bDLstn-TT4KdJrz9o36Bcg/zh-cn_image_0000002808886193.png?HW-CC-KV=V1&HW-CC-Date=20261124T044230Z&HW-CC-Expire=31536000000&HW-CC-Sign=84DC39561E7C2E36785932C550229D19409497AF0E9B4E155BEBFEE56E4A70C8)：切换当前高亮行到下一个历史断点，并显示断点相关信息。
   * ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/8XyQS4hIQuKO5ZWIMUe31A/zh-cn_image_0000002779566532.png?HW-CC-KV=V1&HW-CC-Date=20261124T044230Z&HW-CC-Expire=31536000000&HW-CC-Sign=E3E12ABF25262908452E977E72E2EBFAF98AB05DE63C566A35731C4A5DCF7DEC)：切换当前高亮行到上一个历史断点，并显示断点相关信息。
   * ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/Tx_-fNlCTP6ya5zEpsuluA/zh-cn_image_0000002808886185.png?HW-CC-KV=V1&HW-CC-Date=20261124T044230Z&HW-CC-Expire=31536000000&HW-CC-Sign=35BDA3F9EBB032CF3769155AF24640DF12EA9CFC4CC43E1F12CCBD39FADB183F)：切换当前高亮行到下一个历史行，并显示历史行相关信息。
   * ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/sKJ4OBbzQKCiwnMmneZEjQ/zh-cn_image_0000002779566528.png?HW-CC-KV=V1&HW-CC-Date=20261124T044230Z&HW-CC-Expire=31536000000&HW-CC-Sign=6B753F2EE996F4F776A1448F28F64322F0E57CE92491C66981A82F53D3762A31)：切换当前高亮行到上一个历史行，并显示历史行相关信息。

**说明** 

某些功能在反向调试模式下无法使用，此时会根据您的行为进行对应提示。
