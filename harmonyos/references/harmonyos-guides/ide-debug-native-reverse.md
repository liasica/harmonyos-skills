---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-debug-native-reverse
title: 反向调试
breadcrumb: 指南 > 编写与调试应用 > 应用调试 > 代码调试 > Native代码调试 > 反向调试
category: harmonyos-guides
scraped_at: 2026-04-29T13:46:46+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:703886ccba24f463ec981125113a8f6ee8f75c646151d2f01142d1b148f46d88
---

针对C/C++开发场景，DevEco Studio在提供基础调试能力的基础上，同时提供反向调试能力，帮助开发者更好地理解代码和更迅速定位问题。

反向调试是指在调试过程中可以回退到历史行和历史断点，查看历史调试信息，包括线程、堆栈和变量信息。支持的调试操作为：

* 进入/退出反向调试模式
* 反向Step Over回退到历史行
* 反向Resume执行到历史断点
* 在程序执行历史的记录点上查看全局、静态、局部变量值

## 前提条件

在**File > Settings**（macOS为**DevEco Studio > Preferences/Settings**） **> Build,Execution,Deployment > Debugger > C++ Debugger**设置界面，勾选**Enable time travel debug**开启C++反向调试开关。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/kgBBPJDtQ_e2-yaMReTpiA/zh-cn_image_0000002561752669.png?HW-CC-KV=V1&HW-CC-Date=20260429T054645Z&HW-CC-Expire=86400&HW-CC-Sign=A06E9B847BA7C04067CE5FA09BAA06275D0977FEC334DE0D6B4F41DACA5E4EFF)

## 操作步骤

1. 设置断点，进入调试模式。
2. 开启反向调试开关后，在Debugger中会出现反向调试相关按钮。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/3rQplvcWSvGCyfp-dK5htw/zh-cn_image_0000002561752665.png?HW-CC-KV=V1&HW-CC-Date=20260429T054645Z&HW-CC-Expire=86400&HW-CC-Sign=AE50800F15F2367C0B357C4A3EF01BBE3B4BEFD960A02B7F0452119E7B5EA861)

   需要查看历史调试信息时，点击“Open Time Travel Debug”按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/h7kPaiN_QhuyMJqqCap3gA/zh-cn_image_0000002561752673.png?HW-CC-KV=V1&HW-CC-Date=20260429T054645Z&HW-CC-Expire=86400&HW-CC-Sign=2446E4917B7673E5F9639139FCDBFF67B23C26340DDD8687F6DD35DABC430C89)进入反向调试模式，您可以在此模式下进行调试。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/05/v3/jwXheCIHTAC6xDxqv4Rnkw/zh-cn_image_0000002530752728.png?HW-CC-KV=V1&HW-CC-Date=20260429T054645Z&HW-CC-Expire=86400&HW-CC-Sign=238D5D316250EA20AFA9265801907290669B040049F0E539A40BB702BEB0F542)

   其中，操作按钮说明如下：

   * ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/CFHIALkUQq-cBqF0N1npZw/zh-cn_image_0000002561752677.png?HW-CC-KV=V1&HW-CC-Date=20260429T054645Z&HW-CC-Expire=86400&HW-CC-Sign=679879D5DB06DFB768EB95FFCAACEAD5E67E545649ADEE4AB3F5808685D5C37E)：退出反向调试模式。
   * ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/sXbkG9CCTJSWdDXFm-rxGg/zh-cn_image_0000002530912734.png?HW-CC-KV=V1&HW-CC-Date=20260429T054645Z&HW-CC-Expire=86400&HW-CC-Sign=97780DFE727BA6C67CD3CD0363348E22BDE2ED591DF86AB75E735A67EB9E4720)：切换当前高亮行到下一个历史断点，并显示断点相关信息。
   * ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/7B_XBHieSPeEAOtvueUirg/zh-cn_image_0000002530752742.png?HW-CC-KV=V1&HW-CC-Date=20260429T054645Z&HW-CC-Expire=86400&HW-CC-Sign=4097636A3194DC0176E5F2DCFEE5CB251395D758C3C224952636F4C794D3BB12)：切换当前高亮行到上一个历史断点，并显示断点相关信息。
   * ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/260jvH2NS2-TztgqRs_70w/zh-cn_image_0000002561832645.png?HW-CC-KV=V1&HW-CC-Date=20260429T054645Z&HW-CC-Expire=86400&HW-CC-Sign=A7BD3DA14645907107705F969B543ED787DAFB66481DE9E6F803AF5E09DB301F)：切换当前高亮行到下一个历史行，并显示历史行相关信息。
   * ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/HSCtWO3IRZC-CISiV-GJYA/zh-cn_image_0000002561752671.png?HW-CC-KV=V1&HW-CC-Date=20260429T054645Z&HW-CC-Expire=86400&HW-CC-Sign=27083B151B8E3F285EB915F7FE7CEC2D777A5296B920A2528E06F1EC66FE84AC)：切换当前高亮行到上一个历史行，并显示历史行相关信息。

说明

某些功能在反向调试模式下无法使用，此时会根据您的行为进行对应提示。
