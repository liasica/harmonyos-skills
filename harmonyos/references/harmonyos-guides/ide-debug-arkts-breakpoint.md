---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-debug-arkts-breakpoint
title: 使用断点
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 应用调试 > 代码调试 > ArkTS代码调试 > 使用断点
category: harmonyos-guides
scraped_at: 2026-11-24T12:42:29+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:c1a988db2607246909b89178edcf46e767ad264b81df56c4f34eb9ce1ea5b574
---

DevEco Studio ArkTS代码调试支持行断点、日志断点等多种类型的断点，这些断点可以触发不同的操作。

## 行断点

行断点是最常见的类型，用于在指定的代码行暂停应用的执行，在暂停时，可以检查变量，对表达式求值，然后逐行执行，以确定运行时错误的原因。

如需添加行断点，请按以下步骤操作：

1. 找到需要暂停执行的代码行。
2. 点击该代码行的左侧边线，或将光标置于该行上并按**Ctrl + F8**（macOS为**Command+F8**）。

   当设置断点时，相应的代码行旁边会出现一个红点，如图。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/wkwbIFkNRPyMd-t4jfwNnw/zh-cn_image_0000002779567172.png?HW-CC-KV=V1&HW-CC-Date=20261124T044229Z&HW-CC-Expire=31536000000&HW-CC-Sign=04E0AE729F5B7C09E38CBDC5B3E4F1A3E40A90F55DCEC74E44359B379D75B4DC)

   在设置的断点红点处，单击鼠标右键，在Condition中可以设置条件断点，此类断点仅在满足特定条件时暂停应用。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/eHBOpt82TpO2Vo62ryln8A/zh-cn_image_0000002779407196.png?HW-CC-KV=V1&HW-CC-Date=20261124T044229Z&HW-CC-Expire=31536000000&HW-CC-Sign=DF1859D409E07175BCE4FAA34834617CE7EA93B7CF2A916E576E0E164439C45A)
3. 点击Debug图标![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/Lzf-D_-uR9uFbD9iFwl9hw/zh-cn_image_0000002779567170.png?HW-CC-KV=V1&HW-CC-Date=20261124T044229Z&HW-CC-Expire=31536000000&HW-CC-Sign=9B3FBBA000AD2D8A6E20045732E996357DC1573F422CBF7B2FC0C9E268654185)，开始调试。如果您的应用已经在运行，请点击Attach Debugger to Process图标![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/PyBUNB3FTn6fwHdeH8NV0A/zh-cn_image_0000002808766749.png?HW-CC-KV=V1&HW-CC-Date=20261124T044229Z&HW-CC-Expire=31536000000&HW-CC-Sign=5674C0EF1620DE05C766D2E2223D9F9A7F0E9B01F313E984C4C943DA3245914D)。

   当应用运行到断点处，会在断点处停住，并高亮显示。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/AE5WDpTvR52mGUXxfu3A-A/zh-cn_image_0000002779407194.png?HW-CC-KV=V1&HW-CC-Date=20261124T044229Z&HW-CC-Expire=31536000000&HW-CC-Sign=5FF5FF804A58383E73EB1D2CA08AB8EEDFFEB833F7344ADE9C0428DFE955B093)

## 日志断点

在[BreakPoints](ide-debug-arkts-breakpoint.md#section168791742202819)某个断点的配置中，勾选以下类型的Log，可以使进程运行到断点时在Console窗口打印相应日志。

* 勾选**"Breakpoint hit"message**，程序运行到断点时，打印“Breakpoint reached”。
* 勾选**Stack trace**，程序运行到断点时，打印当前线程的堆栈。
* 勾选**Evaluate and log**，并添加表达式，程序运行到断点时，打印表达式的值。

**说明** 

未勾选Enable的断点不会打印日志，未勾选Suspend execution的断点会打印日志，不满足所设置的Condition的断点不会打印日志。

## 临时断点

在[BreakPoints](ide-debug-arkts-breakpoint.md#section168791742202819)某个断点的配置中，勾选**Remove once hit**，该断点只生效一次，生效后该断点会被删除。

## 函数断点

从DevEco Studio 6.0.0 Beta2版本开始，支持在ArkTS代码中设置函数断点。

函数断点也叫方法断点或符号断点，使用函数名设置断点，当程序运行到对应函数时，中断进程。

在[BreakPoints](ide-debug-arkts-breakpoint.md#section168791742202819)中，点击**+ > ArkTS Symbolic Breakpoints**，在弹出窗口中填写函数名，添加函数断点。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/Hf8MHlt7QnqpaMAG5BeZZQ/zh-cn_image_0000002808886827.png?HW-CC-KV=V1&HW-CC-Date=20261124T044229Z&HW-CC-Expire=31536000000&HW-CC-Sign=CB85796F9F02712BFD74DB9D448E685CD7BFF0C13FBAB5473D8D306631AA6795) ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/9rugmY-jRPWfAchHY9hPag/zh-cn_image_0000002808766747.png?HW-CC-KV=V1&HW-CC-Date=20261124T044229Z&HW-CC-Expire=31536000000&HW-CC-Sign=D5D81EB1B35609A34573DDC1DB2A23B031785DD220E0193F0463380DAAC1EE5F)

**说明** 

DevEco Studio 6.0.1 Release及以下版本，调试过程中如果命中在C++断点，则无法添加和移除ArkTS函数断点，6.0.2 Beta1及以上版本，支持添加和移除。

## 异常断点

异常断点会在应用执行时发生异常的地方暂停应用。

在[BreakPoints](ide-debug-arkts-breakpoint.md#section168791742202819)中，勾选**ArkTS/JS Exception Breakpoints**，开启异常断点。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/9jn5l-cURHOiHTUWlfZgRg/zh-cn_image_0000002808886829.png?HW-CC-KV=V1&HW-CC-Date=20261124T044229Z&HW-CC-Expire=31536000000&HW-CC-Sign=460890CB8DBF496DDF6AC9D144D596B7490233A6B62EF23562CDF49DE24651CD)

当调试应用程序中出现异常时，会在异常处高亮，并且代码左侧有![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/tTvIwJJ7SvGV82IJUp0n6w/zh-cn_image_0000002779407192.png?HW-CC-KV=V1&HW-CC-Date=20261124T044229Z&HW-CC-Expire=31536000000&HW-CC-Sign=94F7C93869E7A08C41AB0897D35F9F6E848127347E4A6F8E6862BF24B46489C6)标志，并展示当前Frames和Variable，以及错误信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/11/v3/f11IA2a1TDmr8-N2f6tAEg/zh-cn_image_0000002808766745.png?HW-CC-KV=V1&HW-CC-Date=20261124T044229Z&HW-CC-Expire=31536000000&HW-CC-Sign=6AA80B75B1AEC615EC0237AC59220D72705E142EC3C8FE74FE595FB91D73D9C9)

## 断点管理

在设置的程序断点红点处，单击鼠标右键。然后单击**More**或按快捷键**Ctrl+Shift+F8**（macOS为**Shift+Command+F8**），可以管理断点。

或者在“Debug”窗口中点击**View Breakpoints** 图标![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/P0aqqxsvRyynNJScrPqj9A/zh-cn_image_0000002808886835.png?HW-CC-KV=V1&HW-CC-Date=20261124T044229Z&HW-CC-Expire=31536000000&HW-CC-Sign=69AFF6736FC3571F812C9C79FA9EC7F3D8EA4C19FE9FFCD376F0E10484CCAEDB)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/DmNk8kYCROmVfCX0kyYB0g/zh-cn_image_0000002808766753.png?HW-CC-KV=V1&HW-CC-Date=20261124T044229Z&HW-CC-Expire=31536000000&HW-CC-Sign=81B3B1FCB35D00AA675124BD7270913C5A2A1D7D2480B582AE3755A1F3D42F84)
