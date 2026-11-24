---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-debug-arkts-breakpoint
title: 使用断点
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 应用调试 > 代码调试 > ArkTS代码调试 > 使用断点
category: harmonyos-guides
scraped_at: 2026-11-24T12:42:46+08:00
doc_updated_at: 2026-10-10
content_hash: sha256:f2b07cfc5480f4061663e8117835a7e774bb1d171b949b69d3c9ec7d3c137b79
---

鸿蒙电脑DevEco Studio ArkTS代码调试支持行断点、日志断点等多种不同类型的断点，这些断点可以触发不同的操作。

## 行断点

行断点是最常见的类型，用于在指定的代码行暂停应用的执行。在暂停时，可以检查变量，对表达式求值。然后逐行执行，以确定运行时错误的原因。

如需添加行断点，请按以下步骤操作：

1. 找到需要暂停执行的代码行。
2. 点击该代码行的左侧边线。当设置断点后，相应的代码行旁会出现断点图标，如图。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/oCR89b3fTu-VtSTrFOH2Ww/zh-cn_image_0000002820681095.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=F1BF5D44A1988BDFE2A68E2FB648852E90A6BB18AF4F7721863E6B0F11513026)

   在设置的断点红点处，鼠标右键选择**编辑断点**，在表达式输入框中设置表达式作为条件。此类断点仅在满足特定条件时暂停应用。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/lVBVWsccTZa85m3mNLwEMw/zh-cn_image_0000002820721101.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=0D2B1FD6F08B6E3EAC9EF1227FF579476DDE9432F44EA361DB45CCEE7B5876B2)
3. 点击调试图标 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/7m5ZJKCKT_Osoh9SAjEWMQ/zh-cn_image_0000002791841160.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=CB756C85CBA226E3FD294EA4939D4263C7D06CD55E9824C1D0572E93E26CE867 "点击放大")，开始调试。如果应用已经在运行，请点击附加调试图标![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/stzEUB03Q3e0f_XrPQmDWg/zh-cn_image_0000002820681099.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=63CB74FCB89E45666AC6B5A5721C4356FE0FEC6C744E7A4E34EF872294BE6E44)。

   当应用运行到断点处，会在断点处停住，并高亮显示。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6a/v3/a44CIIQSTP6WVQgE75xqng/zh-cn_image_0000002792001140.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=59F195FA298967748FD22C22E9F27E06AC736B8769E900072D76EE197463D42C)

## 日志断点

日志断点可以帮助开发者减少在业务代码中添加额外的日志代码。在编辑器行号侧边栏单击鼠标右键，选择**添加记录点**设置日志断点。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b8/v3/_oWe3IgoQzGgPmr-xGw8Lw/zh-cn_image_0000002791841162.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=DD026E0A3D26B262FAE3428FF41DB27779400683E6F6B548B95393726669B5BB)

在日志消息输入框中添加需要记录的模板字符串表达式。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/sNm7V1TaT5qZzoj90_gxgA/zh-cn_image_0000002820721105.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=EC1FBB00D5145983F7B6A3C0342DEAC787F101C4C7D1D2A8DCA2D5EE702D6428)

## 临时断点

临时断点允许开发者在光标停留处设置断点，点击调试器![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/mRgmBX4SSHS4g_FWgs6Wyw/zh-cn_image_0000002820681093.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=DFB4A6678D002B7D9E4F2ABA946F849ED2A2E25C2DA104399A47204583B44402 "点击放大")图标，断点运行至光标停留处。该断点只生效一次，生效后该断点会被删除。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/TbVJPSZPT7C8ze74Jml5JQ/zh-cn_image_0000002791841158.gif?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=2948B0A85AFF25C35827C63A0AAB49DD87AB891F010F87C5AC3950ED9B19EB06 "点击放大")

## 命中数断点

命中数断点允许开发者设置断点命中次数，当达到命中次数时才会触发断点。在编辑器行号侧边栏单击鼠标右键，选择**添加命中数断点**，在输入框中输入命中次数。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/y4V1GXLIR02AiIU7VFpOog/zh-cn_image_0000002791841164.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=843C93E3FF4C2F4BC28D7777F08E6EAACE2A06C7433849C3DF1E910AD0991455)

## 异常断点

异常断点会在应用执行时发生异常的地方暂停应用。在[断点管理](ide-hmos-debug-arkts-breakpoint.md#section168791742202819)中，勾选**Caught Exceptions/Uncaught Exceptions**，开启异常断点。

* **Caught Exceptions**："caught" 表示已被捕获的异常。当程序执行到已捕获的异常时，它会被捕获并由catch语句块进行处理，程序可以继续执行。
* **Uncaught Exceptions**："uncaught" 表示未捕获的异常，当程序执行到未捕获的异常时，它会停止运行并抛出错误。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/06/v3/DaAyicvKSO-FqeLp_g81mA/zh-cn_image_0000002792001136.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=E7F16A004A2900EB53A63AE0A8BD201858020EAA33AC7C5CF548AAE7DD4CB136)

## 断点管理

点击编辑器左侧![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/K9sla0TRRJScVeDTHxjBcw/zh-cn_image_0000002820681101.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=143BAA2020940A27BB373FD8924B2A993E6F1396937559D3D6EB7EF8508F39CC "点击放大")图标，打开断点管理界面进行断点管理。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/_zQ8Vmn8TgOGk0pcmmcCzA/zh-cn_image_0000002792001134.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=86ED0916156EFE15DCDEC030E4F092F1D61D19F5B0E1590B691650FE4B6AABF4)

### 批量操作断点

在断点管理窗口中，**Ctrl + 鼠标左键**可以选择多个断点。选中后点击鼠标右键，选择**全部禁用**、**全部启用**或**全部删除**可对断点批量禁用、使能或移除。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/3YsAxWJ0TM-4AE1g6RsPuQ/zh-cn_image_0000002792001132.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=97251F86DC4E4DC9AEBBE626BA0EDE73E28FF21A37E109ACD5F286C5C9C8D1A3)
