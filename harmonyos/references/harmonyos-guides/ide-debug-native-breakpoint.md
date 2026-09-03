---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-debug-native-breakpoint
title: 使用断点
breadcrumb: 指南 > 编写与调试应用 > 应用调试 > 代码调试 > Native代码调试 > 使用断点
category: harmonyos-guides
scraped_at: 2026-09-04T06:27:17+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:9061677843ebd2c6b98817cc973d6071d261c49630df797d72072fa92004fb6a
---

点击**View Breakpoints** 图标![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/DTcvxeAIT_6ZV65ZZk2ghg/zh-cn_image_0000002731542099.png)可以打开断点管理界面，您可以在断点管理界面查看或更改您的断点。

* 勾选 Enable ，使能该断点。
* 勾选 Suspend execution ，使程序运行到断点时中断。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/CwMM6zJyQKmIws6mt2F4TQ/zh-cn_image_0000002731542093.png)

## 条件断点

在某个断点的配置中，勾选 Condition ，并设置表达式作为条件，使程序运行到断点且满足设置的条件时才会中断进程。

## 日志断点

在某个断点的配置中，勾选以下类型的log，可以使进程运行到断点时在 console 窗口打印相应 log。

* 勾选“Breakpoint hit”message，程序运行到断点时，打印“Breakpoint reached”。
* 勾选 Stack trace，程序运行到断点时，打印当前线程的堆栈。
* 勾选 Evaluate and log，并添加表达式，程序运行到断点时，打印表达式的值。

**说明** 

未勾选 Enable 的断点不会打印日志，未勾选 Suspend execution 的断点会打印日志，不满足所设置的 Condition 的断点不会打印日志。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/tsOBnGbbTUCSDjsd4yh58w/zh-cn_image_0000002701822830.png)

## 临时断点

在某个断点的配置中，勾选 Remove once hit，该断点只生效一次，生效后该断点会被删除。

## 函数断点

也叫方法断点或符号断点，使用函数名设置断点，当程序运行到对应函数时，中断进程。

在断点管理界面中点击“+”->“Cpp Symbolic Breakpoints”，在弹出窗口中填写函数名和模块名（模块名可缺省），添加函数断点。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/tdk3cZ8mSBiV_Kuefa4hhw/zh-cn_image_0000002701822824.png)

## 异常断点

异常断点可以使程序运行到抛异常或捕获异常的代码处停住。

**说明** 

其他系统异常，如 SIGSEGV 等信号异常会默认捕获并中断进程。

在断点管理界面中点选 “Cpp Exception Breakpoints” 下的 “Any exception”，勾选 Enable 使能异常断点。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/GswGsf5ESu6oj0EFSsU6dg/zh-cn_image_0000002701662902.png)

## 数据断点

支持三种类型的数据断点，即变量被读、被写、被读写时中断进程。

在变量列表中对某一个变量右键，在菜单中选择添加数据断点。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/Yb6bUTjgT1K28NFxlGAUXA/zh-cn_image_0000002701822826.png)

在断点管理界面进行查看和修改。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/_11Dk_NHQ027bmk_m8jEsQ/zh-cn_image_0000002731382121.png)

**说明** 

1. 数据断点支持的类型受硬件限制，支持设置数据断点的变量类型 size 不能超过硬件支持的范围；
2. 受硬件限制，最多同时设置 2 个数据断点；
3. 对局部变量设置的数据断点，需要在离开作用域时手动删除，否则会由于变量地址被重用导致进程中断。
