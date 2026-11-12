---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-debug-native-breakpoint
title: 使用断点
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 应用调试 > 代码调试 > Native代码调试 > 使用断点
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:d71c572effdfac1e87840272c12d0f824577e7663b306f5b411277c6195c887f
---

点击**View Breakpoints** 图标![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/61EH8xCRQe-fCAbSN4KRLA/zh-cn_image_0000002779406742.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=56B95AB203F2FE5E31252DEFC441A6C05BBF3B35D5DCE4FE00FBE1AF7E2F7DAC)可以打开断点管理界面，您可以在断点管理界面查看或更改您的断点。

* 勾选 Enable ，使能该断点。
* 勾选 Suspend execution ，使程序运行到断点时中断。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/l9SsCNZWQsWV-0T6wZFrAg/zh-cn_image_0000002808766307.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=CE18B84ECCAA029EB068014DEAE776F31FFC54734B79F4D92B3DD252CAE1BBF3)

## 条件断点

在某个断点的配置中，勾选Condition，并设置表达式作为条件，使程序运行到断点且满足设置的条件时才会中断进程。

## 日志断点

在某个断点的配置中，勾选以下类型的log，可以使进程运行到断点时在 console 窗口打印相应 log。

* 勾选“Breakpoint hit”message，程序运行到断点时，打印“Breakpoint reached”。
* 勾选 Stack trace，程序运行到断点时，打印当前线程的堆栈。
* 勾选 Evaluate and log，并添加表达式，程序运行到断点时，打印表达式的值。

**说明** 

未勾选 Enable 的断点不会打印日志，未勾选 Suspend execution 的断点会打印日志，不满足所设置的 Condition 的断点不会打印日志。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/W6c-2mMISW6c3h39XBQpgg/zh-cn_image_0000002808886387.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=1F4A888EFD24C02FD420083D81D8C714E8CC610E34B8CCFB626AFCA7DCEDDD20)

## 临时断点

在某个断点的配置中，勾选 Remove once hit，该断点只生效一次，生效后该断点会被删除。

## 函数断点

也叫方法断点或符号断点，使用函数名设置断点，当程序运行到对应函数时，中断进程。

在断点管理界面中点击“+”->“Cpp Symbolic Breakpoints”，在弹出窗口中填写函数名和模块名（模块名可缺省），添加函数断点。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/VnDRTm9WSEisOFdwWvbhHA/zh-cn_image_0000002779566726.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=39DD880A7473C7A022D7105C1E14F8AF993E43D0715E549B0E9CF8ED2363705D)

## 异常断点

异常断点可以使程序运行到抛异常或捕获异常的代码处停住。

**说明** 

其他系统异常，如 SIGSEGV 等信号异常会默认捕获并中断进程。

在断点管理界面中点选 “Cpp Exception Breakpoints” 下的 “Any exception”，勾选 Enable 使能异常断点。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/2zdu2Kz-TZSsHD8mx3VVZQ/zh-cn_image_0000002779566722.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=B3F2F67DA0950282EA09351EE6F7E4919853BD7B40D79D0D02A0A2649599FFF7)

## 数据断点

支持三种类型的数据断点，即变量被读、被写、被读写时中断进程。

在变量列表中对某一个变量右键，在菜单中选择添加数据断点。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/fk9pS0i3R6u8jk4V84z5SA/zh-cn_image_0000002779406746.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=47587125A3ED8E6BD0EAF3A35DB00C36EC059649B789EAE8A0190F18A59EA090)

在断点管理界面进行查看和修改。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0c/v3/lOuzV7PYRVGMCyHa74e5Sg/zh-cn_image_0000002808766303.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=5369A35D8F1C9FFE0D1552A431DEEB909CD125D9CF21ACD1B159956612882458)

**说明** 

1. 数据断点支持的类型受硬件限制，支持设置数据断点的变量类型 size 不能超过硬件支持的范围；
2. 受硬件限制，最多同时设置 2 个数据断点；
3. 对局部变量设置的数据断点，需要在离开作用域时手动删除，否则会由于变量地址被重用导致进程中断。
