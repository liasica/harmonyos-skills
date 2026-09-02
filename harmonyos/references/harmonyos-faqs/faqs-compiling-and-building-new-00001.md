---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-new-00001
title: 新建OpenHarmony工程仅修改打包方式未改配置导致加载so库闪退
breadcrumb: FAQ > DevEco Studio > 编译构建 > 新建OpenHarmony工程仅修改打包方式未改配置导致加载so库闪退
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:56+08:00
doc_updated_at: 2026-07-22
content_hash: sha256:90035aa800bc8d8c4135013c9809c7a92d26a10bf5e9cad8d574912226b7da3d
---

## 问题现象

在HarmonyOS应用开发中，新建工程并将打包方式调整为OpenHarmony后直接运行，应用安装成功但在调用加载so库的函数时发生闪退。

## 背景知识

新版本DevEco Studio默认创建HarmonyOS工程。若开发者需要创建OpenHarmony工程，需要按照官方指南修改相应的工程配置，以确保编译运行环境与目标系统匹配。打包方式通常指在工程根目录或模块的build-profile.json5文件中，将targets节点的runtimeOS字段配置为"OpenHarmony"。更多参考请参见[创建OpenHarmony工程](../harmonyos-guides/ide-create-new-project.md#section93301245101612)。

## 问题定位

1.确认工程创建方式：新版本DevEco Studio默认创建的是HarmonyOS工程。

2.确认打包方式调整：开发者将build-profile.json5文件中的runtimeOS字段调整为"OpenHarmony"后直接运行，但未检查并修改其他必要的工程配置文件。

3.确认工程配置修改情况：在调整打包方式后，未按照OpenHarmony工程的要求修改对应的工程配置，导致编译产物与目标运行环境不匹配。

4.定位闪退原因：应用安装成功后，在调用加载so库的函数时发生闪退。通过查看应用崩溃日志（如HiLog或DevEco Studio的Log窗口），可发现包含类似dlopen failed: library "xxx.so" not found的错误信息，表明so库加载失败。该日志特征可直接定位为运行环境与编译配置不匹配导致so库无法被正确解析和加载。

## 分析结论

根本原因是工程配置未正确修改。新版本DevEco Studio默认创建HarmonyOS工程，若需开发OpenHarmony工程，仅修改build-profile.json5中的runtimeOS打包方式而不修改其他工程配置会导致环境不匹配。在运行时加载so库，因配置不符导致加载失败并引发应用闪退，可通过崩溃日志中的dlopen failed特征进行识别。

## 修改建议

按照官方指南修改工程配置。

在新版本DevEco Studio中，若需创建OpenHarmony工程，不能仅调整打包方式，必须检查并修改build-profile.json5等配置文件，参考[创建OpenHarmony工程](../harmonyos-guides/ide-create-new-project.md#section93301245101612)修改工程配置，确保工程配置与OpenHarmony环境匹配，从而正常加载so库。
