---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/init
title: Init
breadcrumb: API参考 > 公共基础能力 > C API > 模块 > Init
category: harmonyos-references
scraped_at: 2026-09-02T15:03:13+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:edae419e8292679a68ec8d11cf09930c0128c03e52b404224576e3bf767957aa
---

## 概述

提供系统能力查询接口。

通过读取系统能力参数文件，返回指定的某个系统能力是否被支持。

**起始版本：** 8

## 文件汇总

| 名称 | 描述 |
| --- | --- |
| [syscap\_ndk.h](syscap__ndk_8h.md) | 查询单个系统能力是否被支持的API。  **引用文件**：<syscap\_ndk.h>  **库**：libdeviceinfo\_ndk.z.so |

### 函数

| 名称 | 描述 |
| --- | --- |
| [canIUse](syscap__ndk_8h.md#caniuse) (const char \*cap) | 查询指定的系统能力是否被支持。 系统能力（SystemCapability，简称SysCap），指操作系统中每一个相对独立的特性。不同的设备对应不同的系统能力集，每个系统能力对应一个或多个API。开发者可根据系统能力来判断是否可以使用某接口。 |
