---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-debug-native-breakpoint
title: 使用断点
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 应用调试 > 代码调试 > Native代码调试 > 使用断点
category: harmonyos-guides
scraped_at: 2026-11-28T10:34:38+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:5fcd2e105af43c343ef7d7068ea25394a8c66a464f88362f62a3adc54f269274
---

点击**View Breakpoints** 图标![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/54/v3/4j_CUXY8SVG6oVUCPG5q9w/zh-cn_image_0000002779406742.png?HW-CC-KV=V1&HW-CC-Date=20261128T023438Z&HW-CC-Expire=31536000000&HW-CC-Sign=B786166DE6C16B96652157FDC466096BF56BB6D12A445F052B7648484B31A716)可以打开断点管理界面，您可以在断点管理界面查看或更改您的断点。

* 勾选 Enable ，使能该断点。
* 勾选 Suspend execution ，使程序运行到断点时中断。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/35/v3/gOJYAIn9Rk-xsKvTBzJfzw/zh-cn_image_0000002808766307.png?HW-CC-KV=V1&HW-CC-Date=20261128T023438Z&HW-CC-Expire=31536000000&HW-CC-Sign=06F2E39A55FCD5EF821E2849EFF3BACF27520F45714F4A488740997462A1261A)

## 条件断点

在某个断点的配置中，勾选Condition，并设置表达式作为条件，使程序运行到断点且满足设置的条件时才会中断进程。

## 日志断点

在某个断点的配置中，勾选以下类型的log，可以使进程运行到断点时在 console 窗口打印相应 log。

* 勾选“Breakpoint hit”message，程序运行到断点时，打印“Breakpoint reached”。
* 勾选 Stack trace，程序运行到断点时，打印当前线程的堆栈。
* 勾选 Evaluate and log，并添加表达式，程序运行到断点时，打印表达式的值。

**说明** 

未勾选 Enable 的断点不会打印日志，未勾选 Suspend execution 的断点会打印日志，不满足所设置的 Condition 的断点不会打印日志。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/tjkPs18_S_iCkmMKqt2ieg/zh-cn_image_0000002808886387.png?HW-CC-KV=V1&HW-CC-Date=20261128T023438Z&HW-CC-Expire=31536000000&HW-CC-Sign=F94D3288291DDA982254B8D2B6B0C187BE330AF0B1BD80DABE851B26C39AE6BA)

## 临时断点

在某个断点的配置中，勾选 Remove once hit，该断点只生效一次，生效后该断点会被删除。

## 函数断点

也叫方法断点或符号断点，使用函数名设置断点，当程序运行到对应函数时，中断进程。

在断点管理界面中点击“+”->“Cpp Symbolic Breakpoints”，在弹出窗口中填写函数名和模块名（模块名可缺省），添加函数断点。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/R8qEcf0KSmawSVfgquc89A/zh-cn_image_0000002779566726.png?HW-CC-KV=V1&HW-CC-Date=20261128T023438Z&HW-CC-Expire=31536000000&HW-CC-Sign=37511E7BF5BEC4C384E2AEFF3DF5E6E2E412F6CB621A1EC54034FDC5718EBAB9)

## 异常断点

异常断点可以使程序运行到抛异常或捕获异常的代码处停住。

**说明** 

其他系统异常，如 SIGSEGV 等信号异常会默认捕获并中断进程。

在断点管理界面中点选 “Cpp Exception Breakpoints” 下的 “Any exception”，勾选 Enable 使能异常断点。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/zUe9mlpmTo63rF8BThL39A/zh-cn_image_0000002779566722.png?HW-CC-KV=V1&HW-CC-Date=20261128T023438Z&HW-CC-Expire=31536000000&HW-CC-Sign=4703375AEBA096727E14D172034BB037AE78A16F3D409242584A2AC828D2E57E)

## 数据断点

支持三种类型的数据断点，即变量被读、被写、被读写时中断进程。

在变量列表中对某一个变量右键，在菜单中选择添加数据断点。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8/v3/qavOCFKuRBKctynP9jziTw/zh-cn_image_0000002779406746.png?HW-CC-KV=V1&HW-CC-Date=20261128T023438Z&HW-CC-Expire=31536000000&HW-CC-Sign=BEA37E330D8C158E0F06338A59AA66FD62644D6566070FF90DDE5E22EA0EEE75)

在断点管理界面进行查看和修改。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/0tG9aoQ6RBCJILQOMDk96w/zh-cn_image_0000002808766303.png?HW-CC-KV=V1&HW-CC-Date=20261128T023438Z&HW-CC-Expire=31536000000&HW-CC-Sign=125611E472160B94E55B69CF5326AD838C49343FAE1FFD164157E0551B6DE52D)

**说明** 

1. 数据断点支持的类型受硬件限制，支持设置数据断点的变量类型 size 不能超过硬件支持的范围；
2. 受硬件限制，最多同时设置 2 个数据断点；
3. 对局部变量设置的数据断点，需要在离开作用域时手动删除，否则会由于变量地址被重用导致进程中断。
