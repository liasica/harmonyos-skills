---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-debug-arkts-breakpoint
title: 使用断点
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 应用调试 > 代码调试 > ArkTS代码调试 > 使用断点
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:bbf968924aeb4e15e2d8a77cb9bf2a96626dcc8d04259a138796d762986b6bef
---

DevEco Studio ArkTS代码调试支持行断点、日志断点等多种类型的断点，这些断点可以触发不同的操作。

## 行断点

行断点是最常见的类型，用于在指定的代码行暂停应用的执行，在暂停时，可以检查变量，对表达式求值，然后逐行执行，以确定运行时错误的原因。

如需添加行断点，请按以下步骤操作：

1. 找到需要暂停执行的代码行。
2. 点击该代码行的左侧边线，或将光标置于该行上并按**Ctrl + F8**（macOS为**Command+F8**）。

   当设置断点时，相应的代码行旁边会出现一个红点，如图。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/3G59XbQzRHGPCYbPJq5D9Q/zh-cn_image_0000002779567172.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=9F50071353D47F00E731836CFD6E1D677C3BE965E6C0F869AC70510E07443BEC)

   在设置的断点红点处，单击鼠标右键，在Condition中可以设置条件断点，此类断点仅在满足特定条件时暂停应用。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/_rNYYKC-TMGW9mUyAh66vw/zh-cn_image_0000002779407196.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=340E8F9DBEC820F125993CA80E34D59911DE3FB1A7F8F6A9123A873FC73060EE)
3. 点击Debug图标![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6f/v3/0JNk07vfSrOqqlEsrcr9Hg/zh-cn_image_0000002779567170.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=BD9DFE5C1DFA83CE5DD1A8AE63179E2C8158D7D479A93AFC04341844D4405068)，开始调试。如果您的应用已经在运行，请点击Attach Debugger to Process图标![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/RsoAd_SVTkmp4SbO8QL0PA/zh-cn_image_0000002808766749.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=864D7FE7A4CA296F2DA3E39D04B28562B3BB6A0DFDF90233F8926AA180D2894A)。

   当应用运行到断点处，会在断点处停住，并高亮显示。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/TFAvF1M9STqI1fBDnEa77A/zh-cn_image_0000002779407194.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=1C1D11737A57CE71026B64C2E11256E51DCA574CA695A4D74E45460C676A94F3)

## 日志断点

在[BreakPoints](ide-debug-arkts-breakpoint.md#section168791742202819)某个断点的配置中，勾选以下类型的Log，可以使进程运行到断点时在Console窗口打印相应日志。

* 勾选**"Breakpoint hit"message**，程序运行到断点时，打印“Breakpoint reached”。
* 勾选**Stack trace**，程序运行到断点时，打印当前线程的堆栈。
* 勾选**Evaluate and log**，并添加表达式，程序运行到断点时，打印表达式的值。

**说明** 

未勾选Enable的断点不会打印日志，未勾选Suspend execution的断点会打印日志，不满足所设置的Condition的断点不会打印日志。

## 临时断点

在[BreakPoints](ide-debug-arkts-breakpoint.md#section168791742202819)某个断点的配置中，勾选**Remove once hit**，该断点只生效一次，生效后该断点会被删除。

## 函数断点

从DevEco Studio 6.0.0 Beta2版本开始，支持在ArkTS代码中设置函数断点。

函数断点也叫方法断点或符号断点，使用函数名设置断点，当程序运行到对应函数时，中断进程。

在[BreakPoints](ide-debug-arkts-breakpoint.md#section168791742202819)中，点击**+ > ArkTS Symbolic Breakpoints**，在弹出窗口中填写函数名，添加函数断点。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/RvaCGOGdR0aTtkU8ehFVeg/zh-cn_image_0000002808886827.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=6968DA157B025CBDB5A93670DA40E49793A11D755FB957EFA994F9399DC313B7) ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/RMccpBkmSmChgeM353STWg/zh-cn_image_0000002808766747.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=5C001ECB00B9B170EBF17E5E45F9C1EF8EEE418F019E0D0CE46D4B1D4390BE92)

**说明** 

DevEco Studio 6.0.1 Release及以下版本，调试过程中如果命中在C++断点，则无法添加和移除ArkTS函数断点，6.0.2 Beta1及以上版本，支持添加和移除。

## 异常断点

异常断点会在应用执行时发生异常的地方暂停应用。

在[BreakPoints](ide-debug-arkts-breakpoint.md#section168791742202819)中，勾选**ArkTS/JS Exception Breakpoints**，开启异常断点。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/XmIKnmrwSDOLP-jrNRraHg/zh-cn_image_0000002808886829.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=8F1AF06248BBF230B00579EE7216E5C8F30AFE2B312FF3CBD2E1D717DB4A98B8)

当调试应用程序中出现异常时，会在异常处高亮，并且代码左侧有![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/rHeKrYPIQ7iRUe9sBKVzcA/zh-cn_image_0000002779407192.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=0601803568343702E5C822BB3D16B6B3CB3FB43AC54F7C7F76A5503F9B44A480)标志，并展示当前Frames和Variable，以及错误信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/Fvo1wGUgStaAV-BE7BSNxA/zh-cn_image_0000002808766745.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=3136EFA745EBE208FCD75957DBD23C05F31C5BD9CEBB70869EA5C4E8E2C55028)

## 断点管理

在设置的程序断点红点处，单击鼠标右键。然后单击**More**或按快捷键**Ctrl+Shift+F8**（macOS为**Shift+Command+F8**），可以管理断点。

或者在“Debug”窗口中点击**View Breakpoints** 图标![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/AtBGH0OuRE-jO0bCDi7gAQ/zh-cn_image_0000002808886835.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=6912F64225CBFD23DDEE41C8B1B066A81940CFB561151FF324808607EF17C108)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/Jay4d4MQTwmtAB64OMGziA/zh-cn_image_0000002808766753.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=8DF3A4C8E0A2BF964872ED8695CF4954962D6E8F8C3937F4722D5107AAC54773)
