---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-debug-arkts-breakpoint
title: 使用断点
breadcrumb: 指南 > 编写与调试应用 > 应用调试 > 代码调试 > ArkTS代码调试 > 使用断点
category: harmonyos-guides
scraped_at: 2026-04-28T07:56:46+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:82fa462af44c4890af1881c721d7c96200f3c8fd158598103a34ee76e385a8a7
---

DevEco Studio ArkTS支持行断点、日志断点等多种不同类型的断点，这些断点可以触发不同的操作。

## 行断点

行断点是最常见的类型，用于在指定的代码行暂停应用的执行，在暂停时，您可以检查变量，对表达式求值，然后逐行执行，以确定运行时错误的原因。

如需添加行断点，请按以下步骤操作：

1. 找到您要暂停执行的代码行。
2. 点击该代码行的左侧边线，或将光标置于该行上并按**Ctrl + F8**（macOS为**Command+F8**）。

   当您设置断点时，相应的代码行旁边会出现一个红点，如图。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/aNwpHJInR9m5Yif4bmpuxw/zh-cn_image_0000002530913040.png?HW-CC-KV=V1&HW-CC-Date=20260427T235645Z&HW-CC-Expire=86400&HW-CC-Sign=861900F05401CBEB227FE5924A4558BC406C20DB0181E2B0BF50D1CBBD045F98)

   在设置的断点红点处，单击鼠标右键，在Condition中可以设置条件断点，此类断点仅会在满足特定条件时才会暂停应用。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1f/v3/Vyq6rQMMS9mvCwYGQWWAPg/zh-cn_image_0000002561832977.png?HW-CC-KV=V1&HW-CC-Date=20260427T235645Z&HW-CC-Expire=86400&HW-CC-Sign=C2347F196DD1AA433BA4F901550F180BF4BBD4F4FB0B6DF548C801F687C66A04)
3. 点击Debug图标![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/tYUCQtTaRVyJyGbk4Hp_iw/zh-cn_image_0000002561832959.png?HW-CC-KV=V1&HW-CC-Date=20260427T235645Z&HW-CC-Expire=86400&HW-CC-Sign=641D2FD4B266BF758F5BFDE4E8C0C8DF1C68E08FECA7C8B7FA7C2F933299912D)，开始调试。如果您的应用已经在运行，请点击Attach Debugger to Process图标![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/0WmkSy6qSsCtRYS1V2ESrA/zh-cn_image_0000002530913032.png?HW-CC-KV=V1&HW-CC-Date=20260427T235645Z&HW-CC-Expire=86400&HW-CC-Sign=8950BCFCDA586B3D889C6F2ACF2FA5CD5748C6489892951BA29C6701371F8DB2)。

   当应用运行到代码处，会在代码处停住，并高亮显示。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/bIfYJ7vdQfaNQbWi-WPYMQ/zh-cn_image_0000002530913048.png?HW-CC-KV=V1&HW-CC-Date=20260427T235645Z&HW-CC-Expire=86400&HW-CC-Sign=4D45DC049666CCDACB2075C7AD77F46ED74E8518DCA9544CED9455C3A9C72658)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/zGvtKmd3QRSvb9lmhVNMyA/zh-cn_image_0000002530753034.png?HW-CC-KV=V1&HW-CC-Date=20260427T235645Z&HW-CC-Expire=86400&HW-CC-Sign=E42BEBF770EEB12CE5C6B3E70211FEA4F62509F105A8609AC89D29599F599B11) ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f2/v3/p6Pz9gbRT0mOwZOGl3sNnw/zh-cn_image_0000002530913028.png?HW-CC-KV=V1&HW-CC-Date=20260427T235645Z&HW-CC-Expire=86400&HW-CC-Sign=77BE9CCC10BCF6716E6A518FED3520105D2F37D4A39E01E8F23E2772ED49F894)

说明

DevEco Studio 6.0.1 Release及以下版本，调试过程中如果命中在C++断点，则无法添加和移除ArkTS函数断点，6.0.2 Beta1及以上版本，支持添加和移除。

## 异常断点

异常断点会在应用执行时发生异常的地方暂停应用。

在[BreakPoints](ide-debug-arkts-breakpoint.md#section168791742202819)中，勾选**ArkTS/Js Exception Breakpoints**，开启异常断点。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/45PooyE-RTuo4zBGUMEmAw/zh-cn_image_0000002561752997.png?HW-CC-KV=V1&HW-CC-Date=20260427T235645Z&HW-CC-Expire=86400&HW-CC-Sign=CE53B5CF543D1E47B8D7E9F8BD990103F4E801CEF454FC325AF5B3ECF2B117D2)

当调试应用程序中出现异常时，会在异常处高亮，并且代码左侧有![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/D8-bMZgAQSiUFdcSPmzLXA/zh-cn_image_0000002530753044.png?HW-CC-KV=V1&HW-CC-Date=20260427T235645Z&HW-CC-Expire=86400&HW-CC-Sign=D7F47F6FABB10CF9BA73D091B770C480CA728B271ED02B6F094584042E1E76AB)标志，并展示当前Frames和Variable，以及错误信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/Od2FHmoRQgC9xZk_flQ7zg/zh-cn_image_0000002561832951.png?HW-CC-KV=V1&HW-CC-Date=20260427T235645Z&HW-CC-Expire=86400&HW-CC-Sign=8E2CFEE276FEDC87F491B34E4089F4F9C18ED5459F678D131D44C8E787B873A3)

## 断点管理

在设置的程序断点红点处，单击鼠标右键。然后单击**More**或按快捷键**Ctrl+Shift+F8**（macOS为**Shift+Command+F8**），可以管理断点。

或者在“Debug”窗口中点击**View Breakpoints** 图标![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/rwTlizNyT9q_s1vidjNaSQ/zh-cn_image_0000002530913050.png?HW-CC-KV=V1&HW-CC-Date=20260427T235645Z&HW-CC-Expire=86400&HW-CC-Sign=4063DB63519EEC875596F172F2E567B051496FCCF20BDA31F79DA239CA1CC443)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/eCOMabBhRiya4-xvjcIxbw/zh-cn_image_0000002561832969.png?HW-CC-KV=V1&HW-CC-Date=20260427T235645Z&HW-CC-Expire=86400&HW-CC-Sign=75712B78D397CB971A6A7B54698189AE276DE0BE90F3B08BBE0B553085843346)
