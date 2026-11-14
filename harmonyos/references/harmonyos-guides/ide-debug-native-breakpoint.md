---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-debug-native-breakpoint
title: 使用断点
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 应用调试 > 代码调试 > Native代码调试 > 使用断点
category: harmonyos-guides
scraped_at: 2026-11-14T08:48:59+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:27edca303063beb8531c481e70482a47343c04941ae34fb72719cdbedd0f8a35
---

点击**View Breakpoints** 图标![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/ew6EwibGT1SAHPFO19YMWw/zh-cn_image_0000002779406742.png?HW-CC-KV=V1&HW-CC-Date=20261114T004712Z&HW-CC-Expire=31536000000&HW-CC-Sign=78DE5DD5630944E574D0E7E151AECA01F6CD77C768B6DC40942B376F582CA903)可以打开断点管理界面，您可以在断点管理界面查看或更改您的断点。

* 勾选 Enable ，使能该断点。
* 勾选 Suspend execution ，使程序运行到断点时中断。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cd/v3/d0U3yTvKRcu0ET9HNVsVSQ/zh-cn_image_0000002808766307.png?HW-CC-KV=V1&HW-CC-Date=20261114T004712Z&HW-CC-Expire=31536000000&HW-CC-Sign=0C191E78B5ACE82F667A16A62D70770C7723AC1FC6863C2CA6E29BD8BA6A36F8)

## 条件断点

在某个断点的配置中，勾选Condition，并设置表达式作为条件，使程序运行到断点且满足设置的条件时才会中断进程。

## 日志断点

在某个断点的配置中，勾选以下类型的log，可以使进程运行到断点时在 console 窗口打印相应 log。

* 勾选“Breakpoint hit”message，程序运行到断点时，打印“Breakpoint reached”。
* 勾选 Stack trace，程序运行到断点时，打印当前线程的堆栈。
* 勾选 Evaluate and log，并添加表达式，程序运行到断点时，打印表达式的值。

**说明** 

未勾选 Enable 的断点不会打印日志，未勾选 Suspend execution 的断点会打印日志，不满足所设置的 Condition 的断点不会打印日志。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/VfUxjuATSUim1_A8mG2VXA/zh-cn_image_0000002808886387.png?HW-CC-KV=V1&HW-CC-Date=20261114T004712Z&HW-CC-Expire=31536000000&HW-CC-Sign=6376F4F254F0A4279F1FC6C3ECE45A6BA376CB63950ED7F04782324CEE0DBE95)

## 临时断点

在某个断点的配置中，勾选 Remove once hit，该断点只生效一次，生效后该断点会被删除。

## 函数断点

也叫方法断点或符号断点，使用函数名设置断点，当程序运行到对应函数时，中断进程。

在断点管理界面中点击“+”->“Cpp Symbolic Breakpoints”，在弹出窗口中填写函数名和模块名（模块名可缺省），添加函数断点。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/3BbQFj_FTZ2kXnnUextazg/zh-cn_image_0000002779566726.png?HW-CC-KV=V1&HW-CC-Date=20261114T004712Z&HW-CC-Expire=31536000000&HW-CC-Sign=0E51265B7A626998B23A8BE834D96AD9A91C869DC68BC151BF4F18A496BC33D3)

## 异常断点

异常断点可以使程序运行到抛异常或捕获异常的代码处停住。

**说明** 

其他系统异常，如 SIGSEGV 等信号异常会默认捕获并中断进程。

在断点管理界面中点选 “Cpp Exception Breakpoints” 下的 “Any exception”，勾选 Enable 使能异常断点。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/ddbdqrGKTyqr6l64h0nKVg/zh-cn_image_0000002779566722.png?HW-CC-KV=V1&HW-CC-Date=20261114T004712Z&HW-CC-Expire=31536000000&HW-CC-Sign=880A35F2C41C63A20F0BCC35CA4BD14A3B5D1DB678631C7B4BAFE54BAD9BA1D0)

## 数据断点

支持三种类型的数据断点，即变量被读、被写、被读写时中断进程。

在变量列表中对某一个变量右键，在菜单中选择添加数据断点。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/d-_c_N6ZRhuD7cSflqiGwA/zh-cn_image_0000002779406746.png?HW-CC-KV=V1&HW-CC-Date=20261114T004712Z&HW-CC-Expire=31536000000&HW-CC-Sign=A31AEE3B27F5B5A579C32430E6313032DAD1F71EAD7E6D5B9A26B7676717EA64)

在断点管理界面进行查看和修改。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/D8uVJAXySzW3bGO8eo3CXQ/zh-cn_image_0000002808766303.png?HW-CC-KV=V1&HW-CC-Date=20261114T004712Z&HW-CC-Expire=31536000000&HW-CC-Sign=C5FF3336BA3EAA6B7CA7BE3C2809C9BE6D1BE1E1A048EC725B15523F10129D36)

**说明** 

1. 数据断点支持的类型受硬件限制，支持设置数据断点的变量类型 size 不能超过硬件支持的范围；
2. 受硬件限制，最多同时设置 2 个数据断点；
3. 对局部变量设置的数据断点，需要在离开作用域时手动删除，否则会由于变量地址被重用导致进程中断。
