---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-debug-native-breakpoint
title: 使用断点
breadcrumb: 指南 > 编写与调试应用 > 应用调试 > 代码调试 > Native代码调试 > 使用断点
category: harmonyos-guides
scraped_at: 2026-04-28T07:56:49+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:3395315cabd98e4b8871329f01f25180e1752eefce662bb44c7ae6aa3c78d7b4
---

点击**View Breakpoints** 图标![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/LjEvFHzcRNOKnlrRtvoQPw/zh-cn_image_0000002530752820.png?HW-CC-KV=V1&HW-CC-Date=20260427T235648Z&HW-CC-Expire=86400&HW-CC-Sign=1F7752482A80AD4B526EAFD44F6F6F74EB0308B51BB7B7642E2CE5CFEB59A053)可以打开断点管理界面，您可以在断点管理界面查看或更改您的断点。

* 勾选 Enable ，使能该断点。
* 勾选 Suspend execution ，使程序运行到断点时中断。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/C7bulyZjSXeJ3IgMDmdatQ/zh-cn_image_0000002530752834.png?HW-CC-KV=V1&HW-CC-Date=20260427T235648Z&HW-CC-Expire=86400&HW-CC-Sign=B8C4A44F59E9A70C0CDFE4A5F9F3A5FA59FFE1A2B1DDCD748C16E8FFB6F48008)

## 条件断点

在某个断点的配置中，勾选 Condition ，并设置表达式作为条件，使程序运行到断点且满足设置的条件时才会中断进程。

## 日志断点

在某个断点的配置中，勾选以下类型的log，可以使进程运行到断点时在 console 窗口打印相应 log。

* 勾选“Breakpoint hit”message，程序运行到断点时，打印“Breakpoint reached”。
* 勾选 Stack trace，程序运行到断点时，打印当前线程的堆栈。
* 勾选 Evaluate and log，并添加表达式，程序运行到断点时，打印表达式的值。

说明

未勾选 Enable 的断点不会打印日志，未勾选 Suspend execution 的断点会打印日志，不满足所设置的 Condition 的断点不会打印日志。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/bI6BTT0qQb294CuBgVncHw/zh-cn_image_0000002530912824.png?HW-CC-KV=V1&HW-CC-Date=20260427T235648Z&HW-CC-Expire=86400&HW-CC-Sign=D5BFA952FE5F73345CC886A3ACB8C9162CABB1B52BFE62DC89B35B459458C85B)

## 临时断点

在某个断点的配置中，勾选 Remove once hit，该断点只生效一次，生效后该断点会被删除。

## 函数断点

也叫方法断点或符号断点，使用函数名设置断点，当程序运行到对应函数时，中断进程。

在断点管理界面中点击“+”->“Cpp Symbolic Breakpoints”，在弹出窗口中填写函数名和模块名（模块名可缺省），添加函数断点。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/RX_o5ZvjTruKt7HL3veL9A/zh-cn_image_0000002530752832.png?HW-CC-KV=V1&HW-CC-Date=20260427T235648Z&HW-CC-Expire=86400&HW-CC-Sign=D60BC5733108465D9396146BC87E31329B7E30232B892910E415B11E48567815)

## 异常断点

异常断点可以使程序运行到抛异常或捕获异常的代码处停住。

说明

其他系统异常，如 SIGSEGV 等信号异常会默认捕获并中断进程。

在断点管理界面中点选 “Cpp Exception Breakpoints” 下的 “Any exception”，勾选 Enable 使能异常断点。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/t3cYoiv9SIm4VU4t_KIm0g/zh-cn_image_0000002561832743.png?HW-CC-KV=V1&HW-CC-Date=20260427T235648Z&HW-CC-Expire=86400&HW-CC-Sign=76B6CB47021EA4ED26A8EB2453CA12A2B47F69168CE7E8AEC01267E5A170D2E7)

## 数据断点

支持三种类型的数据断点，即变量被读、被写、被读写时中断进程。

在变量列表中对某一个变量右键，在菜单中选择添加数据断点。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/Ri7vYhvvTm-GxWFulmYbLg/zh-cn_image_0000002561752767.png?HW-CC-KV=V1&HW-CC-Date=20260427T235648Z&HW-CC-Expire=86400&HW-CC-Sign=046F089EE1CDFE10188F5FD6C8A2F297021BE7735BDD84D5FE00C94AB4EA6434)

在断点管理界面进行查看和修改。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/8c90m6VIR0SY0mlkjIquSg/zh-cn_image_0000002561752763.png?HW-CC-KV=V1&HW-CC-Date=20260427T235648Z&HW-CC-Expire=86400&HW-CC-Sign=876A9444159A23465F6C93671DC9C5A5F184A631EC42F2F1F79ED03552C5CB82)

说明

1. 数据断点支持的类型受硬件限制，支持设置数据断点的变量类型 size 不能超过硬件支持的范围；
2. 受硬件限制，最多同时设置 2 个数据断点；
3. 对局部变量设置的数据断点，需要在离开作用域时手动删除，否则会由于变量地址被重用导致进程中断。
