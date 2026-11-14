---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-debug-arkts-breakpoint
title: 使用断点
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 应用调试 > 代码调试 > ArkTS代码调试 > 使用断点
category: harmonyos-guides
scraped_at: 2026-11-14T08:48:59+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:74b542b9b22212b648cfc04abfa60dc5b5ebf9983a2760bd8b209ac76669b528
---

DevEco Studio ArkTS代码调试支持行断点、日志断点等多种类型的断点，这些断点可以触发不同的操作。

## 行断点

行断点是最常见的类型，用于在指定的代码行暂停应用的执行，在暂停时，可以检查变量，对表达式求值，然后逐行执行，以确定运行时错误的原因。

如需添加行断点，请按以下步骤操作：

1. 找到需要暂停执行的代码行。
2. 点击该代码行的左侧边线，或将光标置于该行上并按**Ctrl + F8**（macOS为**Command+F8**）。

   当设置断点时，相应的代码行旁边会出现一个红点，如图。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/09/v3/XvUARQL2QFyFot_7GQTlhA/zh-cn_image_0000002779567172.png?HW-CC-KV=V1&HW-CC-Date=20261114T004859Z&HW-CC-Expire=31536000000&HW-CC-Sign=7DF87AD4CAFA39D5AE424235BB9144368A7DC7F4DF20DCDF044D923FB2D9D5DF)

   在设置的断点红点处，单击鼠标右键，在Condition中可以设置条件断点，此类断点仅在满足特定条件时暂停应用。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/vR4cGPjfT8OwmRUIcylvuQ/zh-cn_image_0000002779407196.png?HW-CC-KV=V1&HW-CC-Date=20261114T004859Z&HW-CC-Expire=31536000000&HW-CC-Sign=BC07DA31F4A7DBBFB46A28BA7CE700A6803E5411EE64A883A8809D47D007032D)
3. 点击Debug图标![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/zj0cz8OfTMGMp7AsbQLzqA/zh-cn_image_0000002779567170.png?HW-CC-KV=V1&HW-CC-Date=20261114T004859Z&HW-CC-Expire=31536000000&HW-CC-Sign=879F1DFEA6FF1E3574B5011D9259C8D0389F3DF6AEB2F9635EAA4566B054DF4C)，开始调试。如果您的应用已经在运行，请点击Attach Debugger to Process图标![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/bNuyBCZTQamKgIMGm7txLQ/zh-cn_image_0000002808766749.png?HW-CC-KV=V1&HW-CC-Date=20261114T004859Z&HW-CC-Expire=31536000000&HW-CC-Sign=41C4441C3F0DEE1E64B224BBE49E1B3D6A23F301B38ACED41084A45E13E3F9E7)。

   当应用运行到断点处，会在断点处停住，并高亮显示。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/ytBOCsJ4S_-jctdOQI9kfw/zh-cn_image_0000002779407194.png?HW-CC-KV=V1&HW-CC-Date=20261114T004859Z&HW-CC-Expire=31536000000&HW-CC-Sign=10D7F981ECDF75AF6D6359E957FBC76E73E65E2FBDE89217C0ABDA0CCFEE4BBD)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/SF7yNwhlSUqln_mZXd_Y0A/zh-cn_image_0000002808886827.png?HW-CC-KV=V1&HW-CC-Date=20261114T004859Z&HW-CC-Expire=31536000000&HW-CC-Sign=78564661C6507DD6C8048F9C8EFEB2F6547669D8543332AAC220861DCA4F5D7E) ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/e3n29dmVSXKezhKKtODz-A/zh-cn_image_0000002808766747.png?HW-CC-KV=V1&HW-CC-Date=20261114T004859Z&HW-CC-Expire=31536000000&HW-CC-Sign=6A37A4AFBBFAE23EF2634E649F0AD5753D830792FE3EF604A57C546D12AB9443)

**说明** 

DevEco Studio 6.0.1 Release及以下版本，调试过程中如果命中在C++断点，则无法添加和移除ArkTS函数断点，6.0.2 Beta1及以上版本，支持添加和移除。

## 异常断点

异常断点会在应用执行时发生异常的地方暂停应用。

在[BreakPoints](ide-debug-arkts-breakpoint.md#section168791742202819)中，勾选**ArkTS/JS Exception Breakpoints**，开启异常断点。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/iu4pf90rSmG-QHja3IANww/zh-cn_image_0000002808886829.png?HW-CC-KV=V1&HW-CC-Date=20261114T004859Z&HW-CC-Expire=31536000000&HW-CC-Sign=EA1D8DAC71FC8AAB0B72F75A69D7014FD0306AE3A7F5FA71F5B1AC3AFD37945A)

当调试应用程序中出现异常时，会在异常处高亮，并且代码左侧有![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/v8YjbH1dS7aiZOrgJHK2qg/zh-cn_image_0000002779407192.png?HW-CC-KV=V1&HW-CC-Date=20261114T004859Z&HW-CC-Expire=31536000000&HW-CC-Sign=3D8170F594FAC02641EA77FD99E0331F56F2B31423C14B41F771A64A0D157BDE)标志，并展示当前Frames和Variable，以及错误信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/yF6voygYSearIKkUesNHUg/zh-cn_image_0000002808766745.png?HW-CC-KV=V1&HW-CC-Date=20261114T004859Z&HW-CC-Expire=31536000000&HW-CC-Sign=C2AD19213D66FFEA9C3A8C38F3EE09CA00059BD65B5E94B2D67FC66D68966D9A)

## 断点管理

在设置的程序断点红点处，单击鼠标右键。然后单击**More**或按快捷键**Ctrl+Shift+F8**（macOS为**Shift+Command+F8**），可以管理断点。

或者在“Debug”窗口中点击**View Breakpoints** 图标![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/aNdNesf4R9ux4nIowQNpQg/zh-cn_image_0000002808886835.png?HW-CC-KV=V1&HW-CC-Date=20261114T004859Z&HW-CC-Expire=31536000000&HW-CC-Sign=DC3C049EA8366DC5A34302CD57CD2F7872DD050E8392254E6B640E3262B76014)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/MX1-BpcPR3yDk88tlovO4w/zh-cn_image_0000002808766753.png?HW-CC-KV=V1&HW-CC-Date=20261114T004859Z&HW-CC-Expire=31536000000&HW-CC-Sign=D78D75978A7F370CE34ABEA0552B7FE790783CCDFC918E40545DFE4C3684EB6D)
