---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-emulator-devicetype
title: 设备支持类型
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 使用模拟器运行应用 > 概述 > 设备支持类型
category: harmonyos-guides
scraped_at: 2026-11-12T09:53:02+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:eb7c2ca03ee9c04e1c277a06e4d3f26a61e345e2b92d21b0d5f74dc6a511d793
---

模拟器在不同系统上支持的设备类型见下表。

| 系统类型 | 设备类型 | 产品类型 | 备注 |
| --- | --- | --- | --- |
| Windows(X86)  macOS(ARM) | Phone | Phone直板机 | 仅支持中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）。  从6.1.0(23)开始，阔折叠品类下新增Pura X Max设备型号。  从26.0.1版本开始，三折叠品类下新增Mate XT2设备型号。 |
| Foldable双折叠 |
| WideFold阔折叠 |
| TripleFold三折叠 |
| Tablet | Tablet | 仅支持中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）。 |
| 2in1 | 2in1 | 仅支持中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）。 |
| 2in1 Foldable | 仅支持中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）。 |
| Wearable | Wearable | - |
| WearableKid | - |
| TV | TV | 仅支持中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）。 |
| Car | Car | 从26.0.0版本开始，仅支持中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）。 |

**说明** 

使用x86模拟器时，C++工程及三方库需要编译出x86\_64版本的so，请在工程级或模块级build-profile.json5的externalNativeOptions/abiFilters的值中增加"x86\_64"，具体编译配置请参见[externalNativeOptions](ide-hvigor-cpp.md#section0721057575)。
