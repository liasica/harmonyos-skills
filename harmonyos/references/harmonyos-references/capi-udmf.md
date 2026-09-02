---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-udmf
title: UDMF
breadcrumb: API参考 > 应用框架 > ArkData（方舟数据管理） > C API > 模块 > UDMF
category: harmonyos-references
scraped_at: 2026-09-02T14:51:11+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:a586eb04ac7cc5f92a36baf9f374d44886d35ab7c7cc4bc793ffc2f6c4a890c8
---

## 概述

统一数据管理框架旨在定义数据跨应用、跨设备以及跨平台过程中的各项标准，提供统一的HarmonyOS数据语言和标准化的数据接入与读取通路。

**起始版本：** 12

## 文件汇总

| 名称 | 描述 |
| --- | --- |
| [udmf.h](capi-udmf-h.md) | 提供访问统一数据管理框架数据的接口、数据结构、枚举类型。当参数类型为char\*时，字符串必须以空字符（'\0'）结尾，否则可能导致未定义行为或函数返回错误。 |
| [udmf\_err\_code.h](capi-udmf-err-code-h.md) | 声明统一数据管理框架错误码定义和错误描述信息。 |
| [udmf\_meta.h](capi-udmf-meta-h.md) | 声明统一类型数据信息。 |
| [uds.h](capi-uds-h.md) | 提供标准化数据结构相关接口函数、结构体定义。当参数类型为char\*时，字符串必须以空字符（'\0'）结尾，否则可能导致未定义行为或函数返回错误。 |
| [utd.h](capi-utd-h.md) | 提供标准化数据类型描述相关接口和数据结构。当参数类型为char\*时，字符串必须以空字符（'\0'）结尾，否则可能导致未定义行为或函数返回错误。 |
