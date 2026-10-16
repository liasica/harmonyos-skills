---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-debug-native-breakpoint
title: 使用断点
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 应用调试 > 代码调试 > Native代码调试 > 使用断点
category: harmonyos-guides
scraped_at: 2026-10-17T06:43:46+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:2a93d1e4ff3c37460f078010a4eea759557bfa09b59085d26dced7eb912c6908
---

点击编辑器左侧![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/i7pAcHHRSv2N8o2sv_09fg/zh-cn_image_0000002750009770.png "点击放大")图标，打开断点管理界面进行断点管理。

* 勾选复选框，使能该断点。
* 取消勾选复选框，禁用该断点。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/AKOYTjncTJK8RoKcCEp0gg/zh-cn_image_0000002779608677.png)

## 条件断点

在编辑器行号侧边栏单击鼠标右键，选择**添加条件****断点**并在输入框中设置表达式作为条件，使程序运行到断点且满足设置的条件时才会中断进程。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/EWQK18CHSCGLn9DdSkD9-g/zh-cn_image_0000002750169662.png)

## 日志断点

在编辑器行号侧边栏单击鼠标右键，选择**添加记录点**设置日志断点，在输入框中添加表达式，可以使进程运行到断点时在console窗口打印相应日志。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/5SBzejg-TH6NXLD4S4udBQ/zh-cn_image_0000002779608683.png)

**说明** 

未勾选**启用**的断点不会打印日志。

## 临时断点

临时断点允许开发者在光标停留处设置断点，点击调试器![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/h3fRFda1TUa9Cvd_-JQu9g/zh-cn_image_0000002750169654.png "点击放大")图标，断点运行至光标停留处。该断点只生效一次，生效后该断点会被删除。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/JH8VYAAFQJ2sGhRc7nIjwg/zh-cn_image_0000002750009772.gif "点击放大")

## 函数断点

也称为方法断点或符号断点，使用函数名设置断点，当程序运行到对应函数时，中断进程。

在断点管理界面中点击“+”，在弹出窗口中填写函数名，添加函数断点。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/11/v3/HBuuupa1T3Kw2Nl2UFPNwg/zh-cn_image_0000002779728827.png)

## 异常断点

异常断点可以使程序运行到抛异常或捕获异常的代码处停住。

**说明** 

其他系统异常，如SIGSEGV等信号量异常会默认捕获并中断进程。

在断点管理界面中勾选**catch catch**和**catch throw**。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/YG1RJEukQ-WuEilB2J2UoQ/zh-cn_image_0000002750009774.png)

## 数据断点

支持三种类型的数据断点，即变量被读、被写、被读写时中断进程。

在变量列表中对某一个变量右键，在菜单中选择添加数据断点。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/1PCBG1bOTrmIvOEAiWZzdA/zh-cn_image_0000002779608679.png)

在断点管理界面进行查看和禁用/使能。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/21jvepF9R66D5gvQabx3ew/zh-cn_image_0000002779728831.png)

**说明** 

1. 数据断点支持的类型受硬件限制，支持设置数据断点的变量类型size不能超过硬件支持的范围；
2. 受硬件限制，最多同时设置2个数据断点；
3. 对局部变量设置的数据断点，需要在离开作用域时手动删除，否则会由于变量地址被重用导致进程中断。
