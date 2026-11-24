---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-debug-native-breakpoint
title: 使用断点
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 应用调试 > 代码调试 > Native代码调试 > 使用断点
category: harmonyos-guides
scraped_at: 2026-11-24T12:42:30+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:ddf203731a54345be8e9663764a00cc14c569a2e8aeadefadf1d15c448688e3d
---

点击**View Breakpoints** 图标![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/tWzTNhmVTD-MERo1SYwEOQ/zh-cn_image_0000002779406742.png?HW-CC-KV=V1&HW-CC-Date=20261124T044229Z&HW-CC-Expire=31536000000&HW-CC-Sign=D0FCE5EF2F9F8FC844DDD8860E9E412EBEC551789F0D3B6FB0DA37691ADCEA23)可以打开断点管理界面，您可以在断点管理界面查看或更改您的断点。

* 勾选 Enable ，使能该断点。
* 勾选 Suspend execution ，使程序运行到断点时中断。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ac/v3/3Q7wKsnQS6eb5WSLYxcEPw/zh-cn_image_0000002808766307.png?HW-CC-KV=V1&HW-CC-Date=20261124T044229Z&HW-CC-Expire=31536000000&HW-CC-Sign=5111403FCC52E840BD68C37F9909A67CBF0E88F8C8128198AF0181318BDF6F59)

## 条件断点

在某个断点的配置中，勾选Condition，并设置表达式作为条件，使程序运行到断点且满足设置的条件时才会中断进程。

## 日志断点

在某个断点的配置中，勾选以下类型的log，可以使进程运行到断点时在 console 窗口打印相应 log。

* 勾选“Breakpoint hit”message，程序运行到断点时，打印“Breakpoint reached”。
* 勾选 Stack trace，程序运行到断点时，打印当前线程的堆栈。
* 勾选 Evaluate and log，并添加表达式，程序运行到断点时，打印表达式的值。

**说明** 

未勾选 Enable 的断点不会打印日志，未勾选 Suspend execution 的断点会打印日志，不满足所设置的 Condition 的断点不会打印日志。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/Xkd3VEA5T0uRWRjGx17Osw/zh-cn_image_0000002808886387.png?HW-CC-KV=V1&HW-CC-Date=20261124T044229Z&HW-CC-Expire=31536000000&HW-CC-Sign=3993F1994DDC346E92566302F6B8601B8F520F13A3D60BA5773994F08CE328F2)

## 临时断点

在某个断点的配置中，勾选 Remove once hit，该断点只生效一次，生效后该断点会被删除。

## 函数断点

也叫方法断点或符号断点，使用函数名设置断点，当程序运行到对应函数时，中断进程。

在断点管理界面中点击“+”->“Cpp Symbolic Breakpoints”，在弹出窗口中填写函数名和模块名（模块名可缺省），添加函数断点。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/wcvIiiQXS9uRuQNekz7aMA/zh-cn_image_0000002779566726.png?HW-CC-KV=V1&HW-CC-Date=20261124T044229Z&HW-CC-Expire=31536000000&HW-CC-Sign=C10D8960DCF1A2A890F47AE90673BD2C9825A946671CD46F5E52CB3A115FBF14)

## 异常断点

异常断点可以使程序运行到抛异常或捕获异常的代码处停住。

**说明** 

其他系统异常，如 SIGSEGV 等信号异常会默认捕获并中断进程。

在断点管理界面中点选 “Cpp Exception Breakpoints” 下的 “Any exception”，勾选 Enable 使能异常断点。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/X5gnXyAIS4a0Qql2eXzgGQ/zh-cn_image_0000002779566722.png?HW-CC-KV=V1&HW-CC-Date=20261124T044229Z&HW-CC-Expire=31536000000&HW-CC-Sign=0C9A09CD1E01D103F7E91F31F4F406EC2CEC74467BB0DE38A530B1EAF6B3D1CF)

## 数据断点

支持三种类型的数据断点，即变量被读、被写、被读写时中断进程。

在变量列表中对某一个变量右键，在菜单中选择添加数据断点。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/XJi_i5PETOGmbwHgx7e77w/zh-cn_image_0000002779406746.png?HW-CC-KV=V1&HW-CC-Date=20261124T044229Z&HW-CC-Expire=31536000000&HW-CC-Sign=78E711BEEF58A6E32B211C414595F2D50717E584CDD0F4E6B87FF15D5A69CFCD)

在断点管理界面进行查看和修改。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/bDIODZv6R_a9LxfRasUV5g/zh-cn_image_0000002808766303.png?HW-CC-KV=V1&HW-CC-Date=20261124T044229Z&HW-CC-Expire=31536000000&HW-CC-Sign=8B6E0F37C109F531BA2637E2E7ABC195A512D771BE16D4A1817272A8AD6BC0BD)

**说明** 

1. 数据断点支持的类型受硬件限制，支持设置数据断点的变量类型 size 不能超过硬件支持的范围；
2. 受硬件限制，最多同时设置 2 个数据断点；
3. 对局部变量设置的数据断点，需要在离开作用域时手动删除，否则会由于变量地址被重用导致进程中断。
