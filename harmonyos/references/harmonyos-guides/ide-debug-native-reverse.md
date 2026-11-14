---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-debug-native-reverse
title: 反向调试
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 应用调试 > 代码调试 > Native代码调试 > 反向调试
category: harmonyos-guides
scraped_at: 2026-11-14T08:48:59+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:c764b515ce259a714090c01624c73304c88f51c1e2ccc97d0f6a6b2285b530dc
---

针对C/C++开发场景，DevEco Studio在提供基础调试能力的基础上，同时提供反向调试能力，帮助开发者更好地理解代码和更迅速定位问题。

反向调试是指在调试过程中可以回退到历史行和历史断点，查看历史调试信息，包括线程、堆栈和变量信息。支持的调试操作为：

* 进入/退出反向调试模式
* 反向Step Over回退到历史行
* 反向Resume执行到历史断点
* 在程序执行历史的记录点上查看全局、静态、局部变量值

## 前提条件

在**File > Settings**（macOS为**DevEco Studio > Preferences/Settings**） **> Build,Execution,Deployment > Debugger > C++ Debugger**设置界面，勾选**Enable time travel debug**开启C++反向调试开关。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/k-VKNdY1QOS3EYhnH_a7Ug/zh-cn_image_0000002808886189.png?HW-CC-KV=V1&HW-CC-Date=20261114T004859Z&HW-CC-Expire=31536000000&HW-CC-Sign=391A6DB9C84F779F432C5C9DFA51A10B66849541695A0D9D40098AB6C61F06F7)

## 操作步骤

1. 设置断点，进入调试模式。
2. 开启反向调试开关后，在Debugger中会出现反向调试相关按钮。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/qDXQHi7aShuhXqLXqor8VA/zh-cn_image_0000002808766105.png?HW-CC-KV=V1&HW-CC-Date=20261114T004859Z&HW-CC-Expire=31536000000&HW-CC-Sign=F835AD266A231667DD711CB7D0AC670F8C37C055363E1482A3C5891798D92C2B)

   需要查看历史调试信息时，点击“Open Time Travel Debug”按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/QSz8KbjPQ0KLrc7qiMolTA/zh-cn_image_0000002808766109.png?HW-CC-KV=V1&HW-CC-Date=20261114T004859Z&HW-CC-Expire=31536000000&HW-CC-Sign=D833E5F3D186ED15D24BA2858620DBC3B718CF01E6CA715EA42B3325A6E29E2C)进入反向调试模式，您可以在此模式下进行调试。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/MEG9gPqpTaagW1bESRG3AQ/zh-cn_image_0000002779406548.png?HW-CC-KV=V1&HW-CC-Date=20261114T004859Z&HW-CC-Expire=31536000000&HW-CC-Sign=91D21FCD074C07662AC09F88B16D51E08657072E4A121D93DE0638309429DD63)

   其中，操作按钮说明如下：

   * ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/G0rLJDLlRtiH_kNBwDJHnQ/zh-cn_image_0000002779406552.png?HW-CC-KV=V1&HW-CC-Date=20261114T004859Z&HW-CC-Expire=31536000000&HW-CC-Sign=E5F3CB2EDB2FEAB662D5C3B959AC3D65318CD66DE82DD8B08BE9E0A6E8B28100)：退出反向调试模式。
   * ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/Pwg2uGy1T0qQivu8vIwzEw/zh-cn_image_0000002808886193.png?HW-CC-KV=V1&HW-CC-Date=20261114T004859Z&HW-CC-Expire=31536000000&HW-CC-Sign=3FB25386889E79640910700D4A350495382122D61C73E1C4920ACA2563E5DE77)：切换当前高亮行到下一个历史断点，并显示断点相关信息。
   * ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/9t8iX3bPStqepQYMJ4dnJQ/zh-cn_image_0000002779566532.png?HW-CC-KV=V1&HW-CC-Date=20261114T004859Z&HW-CC-Expire=31536000000&HW-CC-Sign=327093FC6FA04EDE2485CF3BD91B7461A01CA83FBD93CB948D9F1F2BA51CB39B)：切换当前高亮行到上一个历史断点，并显示断点相关信息。
   * ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/Hy7t_HoLQzmzBt8SxBncMQ/zh-cn_image_0000002808886185.png?HW-CC-KV=V1&HW-CC-Date=20261114T004859Z&HW-CC-Expire=31536000000&HW-CC-Sign=32164EE7FB98D6264EE2A933AE27EF2831AD8A80A764CAE9FBA2DE3378D6FBB6)：切换当前高亮行到下一个历史行，并显示历史行相关信息。
   * ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/npywIof0SLyz0SvWJ6WHKA/zh-cn_image_0000002779566528.png?HW-CC-KV=V1&HW-CC-Date=20261114T004859Z&HW-CC-Expire=31536000000&HW-CC-Sign=C579FC41247935D28CEA5EE39308014FF334B6788BDCFA705514F27C16808368)：切换当前高亮行到上一个历史行，并显示历史行相关信息。

**说明** 

某些功能在反向调试模式下无法使用，此时会根据您的行为进行对应提示。
