---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-debug-native-reverse
title: 反向调试
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 应用调试 > 代码调试 > Native代码调试 > 反向调试
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:a2f0e96f5a47232028d7ff38521db080eb01466a649368c735dd78ec14bd3fc4
---

针对C/C++开发场景，DevEco Studio在提供基础调试能力的基础上，同时提供反向调试能力，帮助开发者更好地理解代码和更迅速定位问题。

反向调试是指在调试过程中可以回退到历史行和历史断点，查看历史调试信息，包括线程、堆栈和变量信息。支持的调试操作为：

* 进入/退出反向调试模式
* 反向Step Over回退到历史行
* 反向Resume执行到历史断点
* 在程序执行历史的记录点上查看全局、静态、局部变量值

## 前提条件

在**File > Settings**（macOS为**DevEco Studio > Preferences/Settings**） **> Build,Execution,Deployment > Debugger > C++ Debugger**设置界面，勾选**Enable time travel debug**开启C++反向调试开关。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/11M-DCRAR0KNVG82dscviA/zh-cn_image_0000002808886189.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=4F5E5CCF5504BC7090663F4A6D8471AAD94ECD584269FC2A463280D8770C6A05)

## 操作步骤

1. 设置断点，进入调试模式。
2. 开启反向调试开关后，在Debugger中会出现反向调试相关按钮。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/0aRu1xudQAG01k01EsJ2Fw/zh-cn_image_0000002808766105.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=8034A696B841CE4CFBF82E36BC7691DD4A77FE10D44AC4291B7094CFAE704F6D)

   需要查看历史调试信息时，点击“Open Time Travel Debug”按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/wHdKfGJATwa899z6IiYFjw/zh-cn_image_0000002808766109.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=584BA2F69E68180A3A8D0CB9A2E86E2DA7DD0011F90F9760F7365D9D08E6EF61)进入反向调试模式，您可以在此模式下进行调试。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/pnLYDJkVQTOVKMPvrVPyIg/zh-cn_image_0000002779406548.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=75A0B4C7165C190C23435D982E24050140B9277FB72B78341299091CEBCA18D5)

   其中，操作按钮说明如下：

   * ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/ZvgH0SkaRW6OsAWJp1NLJg/zh-cn_image_0000002779406552.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=615D69C835A8073F596AB10A1FA05BD3F7A2FA86E4C2C0E8539A5C8DCDE96023)：退出反向调试模式。
   * ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/UD0KsMg5SO6P5WvxamVpzQ/zh-cn_image_0000002808886193.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=23F5EAFC7B5FC92285D7C0A661F78FEF3243FC83604316BD52E231BBD70910C8)：切换当前高亮行到下一个历史断点，并显示断点相关信息。
   * ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/agXzKT8mRSqj-UiAYVb70g/zh-cn_image_0000002779566532.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=DBF3C98B063939E68DEF82D32D7DAB6CABA9B2C2CE726EDCE67BFC9C4773E4FB)：切换当前高亮行到上一个历史断点，并显示断点相关信息。
   * ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b8/v3/seLfOwFvQZmdS3afEALHjA/zh-cn_image_0000002808886185.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=C50D4B3031E1D693A0FC3949E51086CCA73793A51C90F6B17AF162EE77740F31)：切换当前高亮行到下一个历史行，并显示历史行相关信息。
   * ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/iP-Uv2GZQ3arf9AIlzTuoQ/zh-cn_image_0000002779566528.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=EF9CAB3ACAD5DAB1DD2ADB6EDD35BFBB116CAAD2F52C9D310447CBE98A395D68)：切换当前高亮行到上一个历史行，并显示历史行相关信息。

**说明** 

某些功能在反向调试模式下无法使用，此时会根据您的行为进行对应提示。
