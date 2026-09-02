---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-debugging-66
title: 如何搭建远程真机平台
breadcrumb: FAQ > DevEco Studio > 应用调试 > 如何搭建远程真机平台
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:57+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:8d8dc7d6dca93ba035b3ba18d3bb7bc5765b13b62b99950bf03efc04f7ea247c
---

## 问题现象

开发者在内网环境下，无法连接远程真机，需要搭建远程真机平台，实现类似于华为对外提供的云调试能力，开发者如何搭建远程真机平台？

## 解决方案

[远程真机工具](https://gitcode.com/OpenHarmonyToolkitsPlaza/HOScrcpy)：该工具主要提供HarmonyOS NEXT系统下基于视频流的投屏功能，帧率基本持平真机帧率，达到远程真机的效果。

* SDK使用指南：开发者使用[hoscrcpy API](https://gitcode.com/OpenHarmonyToolkitsPlaza/HOScrcpy/blob/main/hoscrcpy API介绍.md)可以实现HarmonyOS NEXT设备投屏工具、远程真机平台等能力。
* [hosscrcpy-1.0.13-beta.jar](https://gitcode.com/OpenHarmonyToolkitsPlaza/HOScrcpy/releases)：获取Harmony NEXT设备屏幕数据SDK，支持开发者集成。
