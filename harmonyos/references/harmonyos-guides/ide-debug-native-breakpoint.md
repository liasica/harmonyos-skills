---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-debug-native-breakpoint
title: 使用断点
breadcrumb: 指南 > 编写与调试应用 > 应用调试 > 代码调试 > Native代码调试 > 使用断点
category: harmonyos-guides
scraped_at: 2026-04-29T13:46:45+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:4f19cb62326796f5126a0a99714333d3b791a76ab6a15d0d6f1a21745ac9ad8f
---

点击**View Breakpoints** 图标![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/stV8UeHcQnWKg5nsnuF8Wg/zh-cn_image_0000002530752820.png?HW-CC-KV=V1&HW-CC-Date=20260429T054644Z&HW-CC-Expire=86400&HW-CC-Sign=7703DBE910321629DCA53267F8E144BE64276BDF839E2BF8497AA18AEF32A92C)可以打开断点管理界面，您可以在断点管理界面查看或更改您的断点。

* 勾选 Enable ，使能该断点。
* 勾选 Suspend execution ，使程序运行到断点时中断。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/eTxr0d2wTOigjazX4Rbyeg/zh-cn_image_0000002530752834.png?HW-CC-KV=V1&HW-CC-Date=20260429T054644Z&HW-CC-Expire=86400&HW-CC-Sign=A3091C6C10D004C5E569F9B0CDE923F4D78CF88925EA22728EDE775398492AE6)

## 条件断点

在某个断点的配置中，勾选 Condition ，并设置表达式作为条件，使程序运行到断点且满足设置的条件时才会中断进程。

## 日志断点

在某个断点的配置中，勾选以下类型的log，可以使进程运行到断点时在 console 窗口打印相应 log。

* 勾选“Breakpoint hit”message，程序运行到断点时，打印“Breakpoint reached”。
* 勾选 Stack trace，程序运行到断点时，打印当前线程的堆栈。
* 勾选 Evaluate and log，并添加表达式，程序运行到断点时，打印表达式的值。

说明

未勾选 Enable 的断点不会打印日志，未勾选 Suspend execution 的断点会打印日志，不满足所设置的 Condition 的断点不会打印日志。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/nS4mVPsmT9aa5VQiOvCu6Q/zh-cn_image_0000002530912824.png?HW-CC-KV=V1&HW-CC-Date=20260429T054644Z&HW-CC-Expire=86400&HW-CC-Sign=67C20E0551CEDF5C41F2FA9EAB632E5CDD3E6533D4C4909A65F33B421BBC3B26)

## 临时断点

在某个断点的配置中，勾选 Remove once hit，该断点只生效一次，生效后该断点会被删除。

## 函数断点

也叫方法断点或符号断点，使用函数名设置断点，当程序运行到对应函数时，中断进程。

在断点管理界面中点击“+”->“Cpp Symbolic Breakpoints”，在弹出窗口中填写函数名和模块名（模块名可缺省），添加函数断点。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/kfknKNY9RnOi5eYmuSAH0A/zh-cn_image_0000002530752832.png?HW-CC-KV=V1&HW-CC-Date=20260429T054644Z&HW-CC-Expire=86400&HW-CC-Sign=88D33C54882DEED5F153E12B864A0162555859A06719419EA2C820088EE9802C)

## 异常断点

异常断点可以使程序运行到抛异常或捕获异常的代码处停住。

说明

其他系统异常，如 SIGSEGV 等信号异常会默认捕获并中断进程。

在断点管理界面中点选 “Cpp Exception Breakpoints” 下的 “Any exception”，勾选 Enable 使能异常断点。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/63Emat7XRHOVwqbzPV0d3A/zh-cn_image_0000002561832743.png?HW-CC-KV=V1&HW-CC-Date=20260429T054644Z&HW-CC-Expire=86400&HW-CC-Sign=2C02D21FE40E43702C032EE89F23A5221E98F173A704B0D1FF0959BBFC03FE5F)

## 数据断点

支持三种类型的数据断点，即变量被读、被写、被读写时中断进程。

在变量列表中对某一个变量右键，在菜单中选择添加数据断点。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0b/v3/0BvAoTyFQaiF91T4-LDKVg/zh-cn_image_0000002561752767.png?HW-CC-KV=V1&HW-CC-Date=20260429T054644Z&HW-CC-Expire=86400&HW-CC-Sign=94810963E8B8C5B2DC157195CEB02FB7C4D9977F5D16E9E6A4C42AE1F5CB3D43)

在断点管理界面进行查看和修改。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/Kl0xAog6QeC9rJ5xpEDJcA/zh-cn_image_0000002561752763.png?HW-CC-KV=V1&HW-CC-Date=20260429T054644Z&HW-CC-Expire=86400&HW-CC-Sign=3F4E3E56C6D159AC823A4361D9D0C5426BCE468A7D496915497A35F4A318B38E)

说明

1. 数据断点支持的类型受硬件限制，支持设置数据断点的变量类型 size 不能超过硬件支持的范围；
2. 受硬件限制，最多同时设置 2 个数据断点；
3. 对局部变量设置的数据断点，需要在离开作用域时手动删除，否则会由于变量地址被重用导致进程中断。
