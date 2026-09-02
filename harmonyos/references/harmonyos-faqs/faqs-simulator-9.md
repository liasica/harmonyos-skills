---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-simulator-9
title: 模拟器创建和启动失败的原因有哪些
breadcrumb: FAQ > DevEco Studio > 模拟器 > 模拟器创建和启动失败的原因有哪些
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:58+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:5d04bdb4c8c0e8ead6fe2f69f539c56d5fdc0a944a2c5adf48e160d95fdd61be
---

## 问题现象

在创建或启动模拟器时失败，失败的原因有哪些，如何解决？

## 背景知识

* 创建模拟器的步骤可参考[创建模拟器](../harmonyos-guides/ide-emulator-create.md)。
* 常见模拟器错误码参考：[模拟器错误码](../harmonyos-guides/ide-emulator-faqs.md)。

## 问题定位

* 创建或启动模拟器时失败，可能有多种现象和原因，汇总如下：

  | 问题场景 | 问题原因 |
  | --- | --- |
  | 模拟器因中文路径问题导致启动崩溃。 | AppData路径中带有中文名称。 |
  | API14版本模拟器在RTX 3060系列上启动崩溃。 | 系统问题。 |
  | 电脑内存不足导致模拟器启动失败。 | 内存不足。 |
  | 电脑GPU版本过低导致模拟器启动失败。 | GPU版本过低。 |
  | Windows句柄占用过多导致模拟器启动崩溃。 | Windows句柄占用过多。 |
  | Mac x86 PC模拟器启动黑屏或提示：模拟器不支持Mac x86 PC。 | 新版本模拟器已不再支持对x86架构Mac电脑的支持。 |
  | 当前CPU不支持AES指令导致模拟器启动失败。 | CPU不支持AES指令。 |
  | 使用命令行启动模拟器失败。 | 当前DevEco Studio版本不支持命令行拉起模拟器。 |
  | SDK路径变化导致模拟器启动失败。 | SDK路径变化。 |
* **场景一**：模拟器因中文路径问题导致启动崩溃。
  + 现象：

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/7tyXMrUkQuCpmvR-9OiK8w/zh-cn_image_0000002628569678.png "点击放大")
  + 定位：点击上图报错弹窗的发送报告按钮，将报错日志下载到本地进行分析。如果日志中出现如下报错，是因为AppData路径中带有中文名称，导致模拟器某些文件无法找到，最终导致模拟器启动失败。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/7YA-hNSMRfyUm-dK8x7Kcg/zh-cn_image_0000002658928991.png "点击放大")
* **场景二**：API14版本模拟器在RTX 3060系列上启动崩溃。

  定位：排查IDE版本是否是API14的DevEco Studio 5.0.2 Release（5.0.7.210）版本，并且排查用户的GPU是否是RTX 3060系列，因系统问题该版本在RTX 3060系列上运行会导致模拟器崩溃。
* **场景三**：电脑内存不足导致模拟器启动失败。
  + 现象：启动报错弹窗提示“当前系统可申请的内存不足XXGB”。
  + 定位：通过报错弹窗信息或在日志中搜索memory is low，如果有如下对应日志，说明是电脑内存不足导致模拟器闪退：

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2/v3/yuNprTCcTem_rUu4fPt_9A/zh-cn_image_0000002628409778.png "点击放大")
* **场景四**：电脑GPU版本过低导致模拟器启动失败。
  + 现象：启动模拟器失败报错：The graphics card in use does not support OpenGL 4.1 or later. Update the graphics card driver or use another graphics card.
  + 定位：当前显卡驱动版本过低，或不支持OpenGL4.1或以上版本。参考：[00801013 显卡驱动版本过低](../harmonyos-guides/ide-emulator-faqs.md#section73144516710)。
* **场景五**：Windows句柄占用过多导致模拟器启动崩溃。

  定位：如果有如下对应日志，说明是Windows句柄占用过多导致模拟器启动崩溃。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/VPasWk9YQtSf5gPvLwNeNA/zh-cn_image_0000002658809045.png "点击放大")
* **场景六**：Mac x86 PC模拟器启动黑屏或提示：模拟器不支持Mac x86 PC。
  + 现象：Mac x86 PC模拟器启动黑屏，如下图所示：

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/8e8vC-iKS_-oz7PNpbvHqg/zh-cn_image_0000002628569680.png "点击放大")

    或者在创建模拟器时提示：The local emulator does not support Mac x86 PCs. Please use the emulator on Mac ARM and Windows PCs，如下图所示：

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/DlbGwhwfTkqJqJt0g7xE2A/zh-cn_image_0000002658928993.png "点击放大")
  + 定位：参考[设备支持类型](../harmonyos-guides/ide-emulator-devicetype.md)，明确指出模拟器支持系统类型为Windows(X86)和macOS(ARM)，HarmonyOS新版本模拟器已不再支持对x86架构Mac电脑的支持，无法直接创建新模拟器。
* **场景七**：当前CPU不支持AES指令导致模拟器启动失败。
  + 现象：启动报错弹窗提示“模拟器启动失败，当前CPU不支持AES指令”。
  + 定位：参考[00801004 CPU不支持AES指令](../harmonyos-guides/ide-emulator-faqs.md#section29911463342)可知，当前CPU不支持AES指令。
* **场景八**：使用命令行启动模拟器失败。
  + 现象：使用命令行方式启动模拟器报错：模拟器启动失败。请在DevEco Studio中登录华为账号，并从设备管理中启动模拟器。
  + 定位：根据[启动模拟器](../harmonyos-guides/ide-emulator-command-line.md#section1986131715236)章节的说明可知，该版本的模拟器无法通过命令行启动。
* **场景九**：SDK路径变化导致模拟器启动失败。
  + 现象：启动模拟器失败，提示“SDK Path has been changed to xxx”，如下图：

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0f/v3/4rcNmupZS9aC4WM8qZlflg/zh-cn_image_0000002628409780.png "点击放大")
  + 定位：参考[00801014 SDK路径更改](../harmonyos-guides/ide-emulator-faqs.md#section19375152318218)可知，SDK路径更改导致模拟器启动失败。

## 分析结论

* **场景一**：AppData路径中带有中文名称会导致模拟器拉起失败。
* **场景二**：因系统问题API14版本运行在RTX 3060系列上会导致模拟器闪退。
* **场景三**：内存不足导致模拟器失败。
* **场景四**：GPU版本过低会导致模拟器闪退。
* **场景五**：Windows句柄占用过多会导致模拟器崩溃。
* **场景六**：HarmonyOS新版本模拟器已不再支持对x86架构Mac电脑的支持。
* **场景七**：当前CPU不支持AES指令导致模拟器启动失败。
* **场景八**：当前DevEco Studio版本不支持命令行拉起模拟器。
* **场景九**：SDK路径更改导致模拟器启动失败。

## 修改建议

* **场景一**：把AppData路径修改为英文路径。
* **场景二**：DevEco Studio升级到最新的Release版本，下载地址：[最新版本](https://developer.huawei.com/consumer/cn/download/)。
* **场景三**：清理电脑运行内存并重启IDE。或参考：[00801005 可申请内存不足](../harmonyos-guides/ide-emulator-faqs.md#section4348205417203)中的处理步骤。
* **场景四**：升级显卡驱动，如果原显卡不支持OpenGL则需要更换显卡，具体要求请参考[使用环境](../harmonyos-guides/ide-emulator-requirements.md)。
* **场景五**：将DevEco Studio升级到5.1.0 Release版本及以上，模拟器版本更新到API18及以上即可解决。
* **场景六**：
  + **方案一**：使用Windows(X86)版本或macOS(ARM)版本电脑进行开发。
  + **方案二**：使用[云调试](https://developer.huawei.com/consumer/cn/agconnect/cloud-adjust/)进行开发调试。
* **场景七**：使用真机调试或[云调试](https://developer.huawei.com/consumer/cn/agconnect/cloud-adjust/)进行开发调试。
* **场景八**：DevEco Studio升级到最新的Release版本，下载地址：[最新版本](https://developer.huawei.com/consumer/cn/download/)。
* **场景九**：参考[00801014 SDK路径更改](../harmonyos-guides/ide-emulator-faqs.md#section19375152318218)章节的处理步骤如下。
  1. 在Local Emulator的设备列表窗口，点击“Wipe User Data”清除模拟器数据，然后重新启动模拟器。
  2. 重新创建一个模拟器，然后启动新建的模拟器。

## 常见FAQ

Q：模拟器运行闪退是否可以提供具体的错误码提示及修复手段？

A：目前DevEco Studio 6.0.0.858版本基本已经支持错误码提示或弹窗提示说明具体原因及处理步骤，具体错误码参考[模拟器错误码](../harmonyos-guides/ide-emulator-faqs.md)。
