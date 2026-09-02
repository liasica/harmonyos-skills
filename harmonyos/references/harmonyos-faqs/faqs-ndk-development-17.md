---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-development-17
title: 元服务/智能表应用能否使用NDK开发
breadcrumb: FAQ > 应用框架开发 > NDK开发 > NDK开发 > 元服务/智能表应用能否使用NDK开发
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:57+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:54dc997f141bde12d4dfc96ed4f41a2a47c0a178114ed1be7e708aac109b0c98
---

## 问题现象

HarmonyOS是否支持在元服务/智能穿戴应用中使用NDK进行开发？

## 背景知识

* [元服务](../atomic-guides/atomic-service-definition.md)：元服务是HarmonyOS提供的一种轻量应用程序形态，与传统应用相比，具备免安装、秒开直达、自动更新、开发成本较低等特点。
* [穿戴应用](../best-practices/bpta-wear.md)：穿戴应用分为[智能穿戴应用](../best-practices/bpta-smartwatch.md)和[轻量级智能穿戴应用](../best-practices/bpta-lite-wearable-guide.md)。相比手机应用，穿戴应用具备屏幕尺寸较小、随腕携带，查看表盘屏幕更为便捷、支持更为丰富的传感器等特点。
* [NDK](../harmonyos-guides/ndk-development-overview.md)：NDK是HarmonyOS SDK提供的Native API、相应编译脚本和编译工具链的集合，方便开发者使用C或C++语言实现应用的关键功能。

## 解决方案

* 元服务不支持Native开发方式，因此无法使用NDK开发元服务。
* 轻量级智能穿戴应用仅支持JS开发语言，不支持使用C/C++以及ArkTS语言，因此无法使用NDK开发轻量级穿戴应用。
* 智能穿戴应用与普通手机应用的开发过程一致，支持C/C++、JS、ArkTS多语言开发，可以使用NDK进行智能穿戴应用开发。
