---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-70
title: 如何进行DevEco Studio编译构建初步性能分析
breadcrumb: FAQ > DevEco Studio > 编译构建 > 如何进行DevEco Studio编译构建初步性能分析
category: harmonyos-faqs
scraped_at: 2026-10-28T07:48:53+08:00
doc_updated_at: 2026-10-27
content_hash: sha256:6fd0cd24a297d5de9941e49a3a9ca7ab516ca6510aaf1f881a77b099e34e45a5
---

Build Analyzer工具显示编译构建的重要信息，帮助开发者分析和排查性能问题。

构建完成后，通过以下方式打开Build Analyzer窗口：

* 在底部的工具栏区域，单击Build Analyzer窗口进行查看。
* 在左侧边栏单击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/Xd10NvTdTDav9RAwxY-h_A/zh-cn_image_0000002624638434.png)，打开Build Analyzer窗口。
* 完成构建后首次打开Build Analyzer时，窗口显示构建分析概览，如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/Z5X318GaQcGm6pJq7Tc-Ig/zh-cn_image_0000002654837845.png "点击放大")

如需查看构建任务时间图谱，从下拉菜单中点击Tasks，默认进入时间图谱界面。该界面分块显示构建历史记录、构建任务时长图谱、构建日志及日志详情信息，如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/3WbCJyy8Tlqt-lJvcdnHTA/zh-cn_image_0000002624478534.png "点击放大")

事件信息：

|  |  |  |
| --- | --- | --- |
| 事件 | 子事件 | 业务 |
| CompileResource |  | 资源编译 |
| PackageHap |  | 打包工具 |
| SignHap |  | 签名工具 |
| BuildNativeWithCmake |  | cpp编译工具链 |
| CompileArkTS | watchChangedFiles | ArkUI |
| invalidCachePlugin | 编译构建 |
| oh-resolve | 编译构建 |
| moduleInfoMetaPlugin | 编译构建 |
| commonjs | 编译构建 |
| 语言和类型编译器 | ArkUI  语言和类型编译器 |
| ArkUI | ArkUI |
| buildInstrument | 测试框架 |
| 模块化，es2abc | 模块化，es2abc  语言和类型编译器 |
| 编译构建 | 编译构建 |
| 编译构建 | 编译构建 |
| ignorePlugin：编译构建工具 | 编译构建 |
| api范式 | api范式 |
|  | commonPlugin：编译构建工具 | 编译构建 |

参考链接：

[分析构建性能](../harmonyos-guides/ide-hvigor-build-analyzer.md)
