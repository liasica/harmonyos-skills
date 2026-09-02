---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-emulator-devicetype
title: 设备支持类型
breadcrumb: 指南 > 编写与调试应用 > 使用模拟器运行应用 > 概述 > 设备支持类型
category: harmonyos-guides
scraped_at: 2026-09-02T15:00:24+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:de835017705ce63d8a02e3d67e22f1d67c388ada8796efa7d36bc21fef25d4d7
---

模拟器在不同系统上支持的设备类型见下表。

| 系统类型 | 设备类型 | 产品类型 | 备注 |
| --- | --- | --- | --- |
| Windows(X86)  macOS(ARM) | Phone | Phone直板机 | 仅支持在中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）使用。  从6.1.0(23)开始，阔折叠品类下新增Pura X Max设备型号。 |
| Foldable双折叠 |
| WideFold阔折叠 |
| TripleFold三折叠 |
| Tablet | Tablet | 仅支持在中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）使用。 |
| 2in1 | 2in1 | 仅支持在中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）使用。 |
| 2in1 Foldable | 仅支持在中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）使用。 |
| Wearable | Wearable | - |
| WearableKid | - |
| TV | TV | 仅支持在中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）使用。 |
| Car | Car | 从26.0.0版本开始，支持在中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）使用。 |

**说明** 

使用x86模拟器时，C++工程及三方库需要编译出x86\_64版本的so，请在工程级或模块级build-profile.json5的externalNativeOptions/abiFilters的值中增加"x86\_64"，具体编译配置请参见[externalNativeOptions](ide-hvigor-cpp.md#section0721057575)。
