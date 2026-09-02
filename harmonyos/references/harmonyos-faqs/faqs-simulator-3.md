---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-simulator-3
title: 模拟器运行应用报错提示设备和应用的API版本不匹配
breadcrumb: FAQ > DevEco Studio > 模拟器 > 模拟器运行应用报错提示设备和应用的API版本不匹配
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:58+08:00
doc_updated_at: 2026-08-13
content_hash: sha256:307dff17a57c58bda46ad8af5eb6d99e59d02988b6cef03d9a458259cd80cb02
---

## 问题现象

新创建了工程后无法在模拟器上运行，提示Please try to match the API version of the device and the app。模拟器版本是HarmonyOS 5.0.1(13)，DevEco版本5.0.2Release，项目配置信息：

```screen
"compileSdkVersion": 14,
"compatibleSdkVersion": 12,
"runtimeOS": "OpenHarmony",
```

## 背景知识

[OpenHarmony](https://docs.openharmony.cn/pages/v5.1/zh-cn/OpenHarmony-Overview_zh.md)是一个面向全场景的开源分布式操作系统，当前OpenHarmony社区支持22款[开发板](https://docs.openharmony.cn/pages/v5.1/zh-cn/OpenHarmony-Overview_zh.md#支持的开发板)，典型应用场景包含影音娱乐、智慧出行、智能家居等。

## 解决方案

DevEco Studio提供了基础的工程模板资源，不同模板支持的设备类型、API Version不同。OpenHarmony项目不可运行在模拟器上，需在开源设备上运行。[创建和配置新工程](../harmonyos-guides/ide-create-new-project.md)文档中提供了[创建HarmonyOS工程](../harmonyos-guides/ide-create-new-project.md#section181328285169)和[创建OpenHarmony工程](../harmonyos-guides/ide-create-new-project.md#section181328285169)两种工程模板的创建方式，直接创建HarmonyOS工程即可。

## 常见FAQ

Q：工程检查报错，提示“Incorrect settings found in the build-profile.json5 file”？

A：排查工程级build-profile.json5文件配置，可根据规范检查并[修改配置](faqs-project-management-2.md)。
