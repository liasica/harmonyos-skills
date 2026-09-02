---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faq-stability-53
title: Attach Debugger调试失效，无法正常拦截断点
breadcrumb: FAQ > 应用质量 > 技术质量 > 稳定性 > Attach Debugger调试失效，无法正常拦截断点
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:50+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:1358da0ba915c4f8d5b8df87d299ffb312b62937264f6b3eaaa1f0fa29bca602
---

## 问题现象

使用IDE工具进行Attach启动调试时，断点可以正常打，运行之后会出现Native调试器和ArkTS调试器两个窗口，因项目未使用Native相关代码，将Native调试窗口关闭后，只调试ArkTS。ArkTS窗口未显示将文件加入到调试进程的信息，且触发断点没有正常拦截到，断点调试失效。

## 背景知识

Attach调试是一种在应用运行时连接到应用的调试方法，主要用于在应用部署后发现和修复问题。在HarmonyOS开发中，如果你需要调试一个已经运行的应用，可以通过[Attach](../harmonyos-guides/ide-debug-arkts-attach.md)进行调试。

## 问题定位

在进行Attach调试或者Debug调试时，如果[设置调试代码类型](../harmonyos-guides/ide-run-debug-configurations.md#section1170735241213)为Detect Automatically，则会根据工程模块及其依赖的模块涉及的编程语言，自动启动对应的调试器。项目工程较大时，调试器启动也会相对较慢，如果在Native调试器未启动完成时将其关闭，也会影响到ArkTS调试器的启动，可能会导致调试功能失效。

## 分析结论

项目启动Attach调试时，分别启动了Native调试器和ArkTS调试器，在Native调试器未启动完成时将其关闭，导致ArkTS调试器也启动失败，从而无法正常拦截断点，调试功能失效。

## 修改建议

1. 如果出现Native调试器和ArkTS调试器两个窗口，需要等待两个窗口都加载完成，才能进行调试。
2. 可以在调试之前编辑调试配置，在Debugger页签中设置Debug type为ArkTS/JS或Native，只启动自己需要的调试器。可参考文档：[自定义运行/调试配置](../harmonyos-guides/ide-run-debug-configurations.md)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/fwLSRtroQNOGYdOyzb2Ryw/zh-cn_image_0000002658794255.png "点击放大")
