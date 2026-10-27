---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-development-environment-31
title: IDE编写C++代码时没有提示
breadcrumb: FAQ > DevEco Studio > 环境准备 > IDE编写C++代码时没有提示
category: harmonyos-faqs
scraped_at: 2026-10-28T07:48:49+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:14c2308375bfb873cd92d10f64147de9bc4d05d6c68b1cf7d1b33c75af41479f
---

## 问题现象

IDE编写C++代码没有自动补全提示，点击变量名也无法快速定位或者跳转，且IDE右下角服务点为红色。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/nTvT4X9kQc6waJB_W8ggog/zh-cn_image_0000002658924309.png "点击放大")

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/LN6XFpmcRRuSyT3ftzRDFQ/zh-cn_image_0000002658804363.png "点击放大")

## 背景知识

[DevEco Studio](faqs-development-environment.md)是基于IntelliJ IDEA Community开源版本打造，面向HarmonyOS应用/元服务开发场景的一站式集成开发环境。提供AI辅助编程、编译构建、UI实时预览、代码调试、性能调优、模拟器等功能，帮助高效开发HarmonyOS应用及元服务。

## 问题定位

进入IDE安装目录例如：“C:\Program Files\Huawei\DevEco Studio\tools\llvm\server\lsp\win”，点击clangd.exe文件，看下是否有报错vcruntime140.dll文件缺失。

## 分析结论

由于vcruntime140.dll文件缺失导致IDE服务无法正常拉起，编写代码没有提示也无法快速定位或者跳转。

## 修改建议

在网上下载vcruntime140.dll文件并放入：“C:\Windows\System32”下，重新运行clangd.exe成功后，再重启IDE后问题解决。
