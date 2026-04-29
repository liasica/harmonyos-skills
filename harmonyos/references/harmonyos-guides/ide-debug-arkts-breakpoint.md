---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-debug-arkts-breakpoint
title: 使用断点
breadcrumb: 指南 > 编写与调试应用 > 应用调试 > 代码调试 > ArkTS代码调试 > 使用断点
category: harmonyos-guides
scraped_at: 2026-04-29T13:46:43+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:a88d5fda036cee097a990a847a68225d5fff8a21279ac4a736ff52349b416c6c
---

DevEco Studio ArkTS支持行断点、日志断点等多种不同类型的断点，这些断点可以触发不同的操作。

## 行断点

行断点是最常见的类型，用于在指定的代码行暂停应用的执行，在暂停时，您可以检查变量，对表达式求值，然后逐行执行，以确定运行时错误的原因。

如需添加行断点，请按以下步骤操作：

1. 找到您要暂停执行的代码行。
2. 点击该代码行的左侧边线，或将光标置于该行上并按**Ctrl + F8**（macOS为**Command+F8**）。

   当您设置断点时，相应的代码行旁边会出现一个红点，如图。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/IPby4ahyQxCOFckEoe2a9Q/zh-cn_image_0000002530913040.png?HW-CC-KV=V1&HW-CC-Date=20260429T054642Z&HW-CC-Expire=86400&HW-CC-Sign=ADEE3CE3028884395A1A9F1A9BF4B26C11F197B009AA74B070772BC7DE937DB3)

   在设置的断点红点处，单击鼠标右键，在Condition中可以设置条件断点，此类断点仅会在满足特定条件时才会暂停应用。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/OJy1FyneQZOjwd2QTk5aRQ/zh-cn_image_0000002561832977.png?HW-CC-KV=V1&HW-CC-Date=20260429T054642Z&HW-CC-Expire=86400&HW-CC-Sign=400C878C1C7459A2AD2B7A3372354A51D13F9462C7FCD9DD0A2197A2C1FEBD98)
3. 点击Debug图标![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/PgIllHfZSXi7gz5jjeFsjg/zh-cn_image_0000002561832959.png?HW-CC-KV=V1&HW-CC-Date=20260429T054642Z&HW-CC-Expire=86400&HW-CC-Sign=665E0E9D8CEA6694D8465FAD9C93621611A868F5CC467304F7B2068CEED7538E)，开始调试。如果您的应用已经在运行，请点击Attach Debugger to Process图标![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/0mXLgwVvRKC8TpLzazIzTQ/zh-cn_image_0000002530913032.png?HW-CC-KV=V1&HW-CC-Date=20260429T054642Z&HW-CC-Expire=86400&HW-CC-Sign=FB8E4D645F935906ACD52339B92D0D542B73C5DA2EE3127D5EA96E6A06C9EAD6)。

   当应用运行到代码处，会在代码处停住，并高亮显示。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/EAb-vHXxThaKl1LlgRwDuQ/zh-cn_image_0000002530913048.png?HW-CC-KV=V1&HW-CC-Date=20260429T054642Z&HW-CC-Expire=86400&HW-CC-Sign=F98B8BF16C8D77480B53007A85ABADAE8ACB6D12636FC03832E23D3CEC5130EB)

## 日志断点

在[BreakPoints](ide-debug-arkts-breakpoint.md#section168791742202819)某个断点的配置中，勾选以下类型的Log，可以使进程运行到断点时在Console窗口打印相应日志。

* 勾选**"Breakpoint hit"message**，程序运行到断点时，打印“Breakpoint reached”。
* 勾选**Stack trace**，程序运行到断点时，打印当前线程的堆栈。
* 勾选**Evaluate and log**，并添加表达式，程序运行到断点时，打印表达式的值。

说明

未勾选Enable的断点不会打印日志，未勾选Suspend execution的断点会打印日志，不满足所设置的Condition的断点不会打印日志。

## 临时断点

在[BreakPoints](ide-debug-arkts-breakpoint.md#section168791742202819)某个断点的配置中，勾选**Remove once hit**，该断点只生效一次，生效后该断点会被删除。

## 函数断点

从DevEco Studio 6.0.0 Beta2版本开始，支持在ArkTS代码中设置函数断点。

函数断点也叫方法断点或符号断点，使用函数名设置断点，当程序运行到对应函数时，中断进程。

在[BreakPoints](ide-debug-arkts-breakpoint.md#section168791742202819)中，点击**+ > ArkTS Symbolic Breakpoints**，在弹出窗口中填写函数名，添加函数断点。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/emeNn1Z1SP2M64z_e--mXg/zh-cn_image_0000002530753034.png?HW-CC-KV=V1&HW-CC-Date=20260429T054642Z&HW-CC-Expire=86400&HW-CC-Sign=C5C062439B2941A0A8CC5D2A27945DA9CFE45B10171FD0C0611D6FE5C412F119) ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/weOYWr-AQUuAdUYRDJizgA/zh-cn_image_0000002530913028.png?HW-CC-KV=V1&HW-CC-Date=20260429T054642Z&HW-CC-Expire=86400&HW-CC-Sign=C2BFE94FA1A58A6509EC1682B0A5480D84629BD89883E616A77DFC98939C81F3)

说明

DevEco Studio 6.0.1 Release及以下版本，调试过程中如果命中在C++断点，则无法添加和移除ArkTS函数断点，6.0.2 Beta1及以上版本，支持添加和移除。

## 异常断点

异常断点会在应用执行时发生异常的地方暂停应用。

在[BreakPoints](ide-debug-arkts-breakpoint.md#section168791742202819)中，勾选**ArkTS/Js Exception Breakpoints**，开启异常断点。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/iGiSpRrLR22JW4jYoFhKWQ/zh-cn_image_0000002561752997.png?HW-CC-KV=V1&HW-CC-Date=20260429T054642Z&HW-CC-Expire=86400&HW-CC-Sign=B084B4927F6695CB717DC85B4AE25A14EAA962AD56481C355CA1B975917AA199)

当调试应用程序中出现异常时，会在异常处高亮，并且代码左侧有![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f7/v3/peLLqkBsRdiqHWQA73ONTw/zh-cn_image_0000002530753044.png?HW-CC-KV=V1&HW-CC-Date=20260429T054642Z&HW-CC-Expire=86400&HW-CC-Sign=5A6F2A23A314038E0CE28E2A9E7159676E09BBC9D83F3C4F1412A3FC21DFCE79)标志，并展示当前Frames和Variable，以及错误信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/noFoaa7LQaurTRHWWbC-uA/zh-cn_image_0000002561832951.png?HW-CC-KV=V1&HW-CC-Date=20260429T054642Z&HW-CC-Expire=86400&HW-CC-Sign=F9EB8F87D1D22CFFC7900774F1926C841CD92570A424A4482F6BC58216223C90)

## 断点管理

在设置的程序断点红点处，单击鼠标右键。然后单击**More**或按快捷键**Ctrl+Shift+F8**（macOS为**Shift+Command+F8**），可以管理断点。

或者在“Debug”窗口中点击**View Breakpoints** 图标![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/QPrzbgJeT2qgLgxhK72gSg/zh-cn_image_0000002530913050.png?HW-CC-KV=V1&HW-CC-Date=20260429T054642Z&HW-CC-Expire=86400&HW-CC-Sign=AA4B6952A67D0A201C8DB1FA665D17623B487BC6B79404843A1E170BD0D400BC)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/ive7NjH6TuaOeA5_jbuBzg/zh-cn_image_0000002561832969.png?HW-CC-KV=V1&HW-CC-Date=20260429T054642Z&HW-CC-Expire=86400&HW-CC-Sign=2396F997AE42C3C6AC56053DA7ED277DC0271FC57C1B06E43075BA696D87FE68)
