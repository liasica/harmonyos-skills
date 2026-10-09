---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-debug-arkts-breakpoint
title: 使用断点
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 应用调试 > 代码调试 > ArkTS代码调试 > 使用断点
category: harmonyos-guides
scraped_at: 2026-10-09T08:15:33+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:48ba211f44373a6d4f7458721fa17d7b345697a53c1e6df9f5eb20e1b9d5c28d
---

鸿蒙电脑DevEco Studio ArkTS代码调试支持行断点、日志断点等多种不同类型的断点，这些断点可以触发不同的操作。

## 行断点

行断点是最常见的类型，用于在指定的代码行暂停应用的执行。在暂停时，可以检查变量，对表达式求值。然后逐行执行，以确定运行时错误的原因。

如需添加行断点，请按以下步骤操作：

1. 找到需要暂停执行的代码行。
2. 点击该代码行的左侧边线。当设置断点后，相应的代码行旁会出现断点图标，如图。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d4/v3/dr6ru38uRNujPuCtagY0vA/zh-cn_image_0000002778922941.png)

   在设置的断点红点处，鼠标右键选择**编辑断点**，在表达式输入框中设置表达式作为条件。此类断点仅在满足特定条件时暂停应用。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/vP_Itus3Sfm1P6avPe0Y3A/zh-cn_image_0000002779082789.png)
3. 点击调试图标 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/6Bd0rY7lQ_muj0YqSRnUeA/zh-cn_image_0000002749323852.png "点击放大")，开始调试。如果应用已经在运行，请点击附加调试图标![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/70oxcAT_QLe_YLALIAwGrw/zh-cn_image_0000002749483728.png)。

   当应用运行到断点处，会在断点处停住，并高亮显示。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/_SJzAdqtQqKOZE9wFhaiSQ/zh-cn_image_0000002779082791.png)

## 日志断点

日志断点可以帮助开发者减少在业务代码中添加额外的日志代码。在编辑器行号侧边栏单击鼠标右键，选择**添加记录点**设置日志断点。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/5JNszDYKTluYs0np4HQ04g/zh-cn_image_0000002749483724.png)

在日志消息输入框中添加需要记录的模板字符串表达式。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/fx63YAaaTcW8apv_GzCefA/zh-cn_image_0000002749323854.png)

## 临时断点

临时断点允许开发者在光标停留处设置断点，点击调试器![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/W4Zvj5VMR_CxsHe-S3bHpg/zh-cn_image_0000002778922939.png "点击放大")图标，断点运行至光标停留处。该断点只生效一次，生效后该断点会被删除。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b/v3/2u-GE9wQTQ2mjlhcCP40OQ/zh-cn_image_0000002778922943.gif "点击放大")

## 命中数断点

命中数断点允许开发者设置断点命中次数，当达到命中次数时才会触发断点。在编辑器行号侧边栏单击鼠标右键，选择**添加命中数断点**，在输入框中输入命中次数。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/WVavdtTcSlCQGEhTPfefKQ/zh-cn_image_0000002779082787.png)

## 异常断点

异常断点会在应用执行时发生异常的地方暂停应用。在[断点管理](ide-hmos-debug-arkts-breakpoint.md#section168791742202819)中，勾选**Caught Exceptions/Uncaught Exceptions**，开启异常断点。

* **Caught Exceptions**："caught" 表示已被捕获的异常。当程序执行到已捕获的异常时，它会被捕获并由catch语句块进行处理，程序可以继续执行。
* **Uncaught Exceptions**："uncaught" 表示未捕获的异常，当程序执行到未捕获的异常时，它会停止运行并抛出错误。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/IJaHoAC3RHiP5RnfEmYyAQ/zh-cn_image_0000002749483732.png)

## 断点管理

点击编辑器左侧![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/V0T_7tdnRhS6ajEEqiu67g/zh-cn_image_0000002778922937.png "点击放大")图标，打开断点管理界面进行断点管理。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/0HVMCgpqRYmJAdIAyQRYog/zh-cn_image_0000002749483730.png)

### 批量操作断点

在断点管理窗口中，**Ctrl + 鼠标左键**可以选择多个断点。选中后点击鼠标右键，选择**全部禁用**、**全部启用**或**全部删除**可对断点批量禁用、使能或移除。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/y_FM3HnxRA-RWoDRinDqcw/zh-cn_image_0000002749323850.png)
