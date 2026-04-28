---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-70
title: 如何进行DevEco Studio编译构建初步性能分析
breadcrumb: FAQ > DevEco Studio > 编译构建 > 如何进行DevEco Studio编译构建初步性能分析
category: harmonyos-faqs
scraped_at: 2026-04-28T08:29:22+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:a3163a63ea0fc500d85d1bbcb908ed667c841956707d3ea5fea1ec2d789d2f83
---

Build Analyzer工具显示编译构建的重要信息，帮助开发者分析和排查性能问题。

构建完成后，通过以下方式打开Build Analyzer窗口：

* 在底部的工具栏区域，单击Build Analyzer窗口进行查看。
* 在左侧边栏单击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/tdXpfARhTweQkD7amOYE1g/zh-cn_image_0000002229758897.png?HW-CC-KV=V1&HW-CC-Date=20260428T002921Z&HW-CC-Expire=86400&HW-CC-Sign=BC05852CC8E7AA792974B6A7BCDC76A14C2B9D95C094D90DDDB0C400E8700629)，打开Build Analyzer窗口。
* 完成构建后首次打开Build Analyzer时，窗口显示构建分析概览，如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f8/v3/Kyz5mjkNSOG9stZqlB3D5w/zh-cn_image_0000002229604409.png?HW-CC-KV=V1&HW-CC-Date=20260428T002921Z&HW-CC-Expire=86400&HW-CC-Sign=7889BAEF18D56D1DB28811ED2D25814F92E800796F4E20341879FF639818986B "点击放大")

如需查看构建任务时间图谱，从下拉菜单中点击Tasks，默认进入时间图谱界面。该界面分块显示构建历史记录、构建任务时长图谱、构建日志及日志详情信息，如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d6/v3/KlVqll1KR0S8hnI7kTiYWg/zh-cn_image_0000002194159012.png?HW-CC-KV=V1&HW-CC-Date=20260428T002921Z&HW-CC-Expire=86400&HW-CC-Sign=F19E8810B94A0AF8D27AA6D7C2FCD5788C740BB366D26E59528A92318D7F3AC4 "点击放大")

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
