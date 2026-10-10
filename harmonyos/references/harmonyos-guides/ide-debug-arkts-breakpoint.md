---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-debug-arkts-breakpoint
title: 使用断点
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 应用调试 > 代码调试 > ArkTS代码调试 > 使用断点
category: harmonyos-guides
scraped_at: 2026-10-11T07:23:03+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:dac76161c67f15356447ae3341f7905bf0cbcfb2272a6b7a02b0628132bb6127
---

DevEco Studio ArkTS代码调试支持行断点、日志断点等多种类型的断点，这些断点可以触发不同的操作。

## 行断点

行断点是最常见的类型，用于在指定的代码行暂停应用的执行，在暂停时，您可以检查变量，对表达式求值，然后逐行执行，以确定运行时错误的原因。

如需添加行断点，请按以下步骤操作：

1. 找到您要暂停执行的代码行。
2. 点击该代码行的左侧边线，或将光标置于该行上并按**Ctrl + F8**（macOS为**Command+F8**）。

   当您设置断点时，相应的代码行旁边会出现一个红点，如图。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/6SUtB7nZTSiWSjXc--1_HA/zh-cn_image_0000002701823344.png)

   在设置的断点红点处，单击鼠标右键，在Condition中可以设置条件断点，此类断点仅在满足特定条件时暂停应用。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/U6v_v3D2Q8KThVIBFny8Eg/zh-cn_image_0000002701823346.png)
3. 点击Debug图标![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/DzZNpN7yR0GykXmu7xplCw/zh-cn_image_0000002701663422.png)，开始调试。如果您的应用已经在运行，请点击Attach Debugger to Process图标![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/DapBTufgSfmviiBZqW_Q8w/zh-cn_image_0000002731542615.png)。

   当应用运行到代码处，会在代码处停住，并高亮显示。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/Fz8081cKTPqdcNoIK_TMSQ/zh-cn_image_0000002701663424.png)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b8/v3/cciOlsf-T6iUWCZeonHvoA/zh-cn_image_0000002701663420.png) ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/iBXFSs3oSAaQCxcn-V9NjQ/zh-cn_image_0000002731382641.png)

**说明** 

DevEco Studio 6.0.1 Release及以下版本，调试过程中如果命中在C++断点，则无法添加和移除ArkTS函数断点，6.0.2 Beta1及以上版本，支持添加和移除。

## 异常断点

异常断点会在应用执行时发生异常的地方暂停应用。

在[BreakPoints](ide-debug-arkts-breakpoint.md#section168791742202819)中，勾选**ArkTS/JS Exception Breakpoints**，开启异常断点。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cd/v3/zJ1ar2LYRguPKDcFuFOUtQ/zh-cn_image_0000002731382643.png)

当调试应用程序中出现异常时，会在异常处高亮，并且代码左侧有![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fb/v3/n8qHq3ZoRf-zBMIqYXKS9A/zh-cn_image_0000002731382647.png)标志，并展示当前Frames和Variable，以及错误信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/QUpvb2Q9QBS2rXZIax5dEA/zh-cn_image_0000002701823340.png)

## 断点管理

在设置的程序断点红点处，单击鼠标右键。然后单击**More**或按快捷键**Ctrl+Shift+F8**（macOS为**Shift+Command+F8**），可以管理断点。

或者在“Debug”窗口中点击**View Breakpoints** 图标![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/83xBSRvIQTOFblw122mOsw/zh-cn_image_0000002731542613.png)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/E0CFbf8gSgarb_b_pY-kUA/zh-cn_image_0000002731542617.png)
