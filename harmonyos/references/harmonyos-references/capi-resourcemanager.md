---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-resourcemanager
title: resourcemanager
breadcrumb: API参考 > 应用框架 > Localization Kit（本地化开发服务） > C API > 模块 > resourcemanager
category: harmonyos-references
scraped_at: 2026-09-02T14:52:04+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:5c7d8b1b94d6c7a8a13b455ffdde415c1a63413c5718202a81800472e32d4133
---

## 概述

通过resourcemanager模块，开发者可以在Native层通过资源ID或资源名称获取应用资源或系统资源，实现多语言、多设备和多屏幕密度的资源适配。具体包括：

- 获取基础类型资源：获取颜色值（ARGB格式）、整数、浮点数、布尔值等基础类型资源。

- 获取字符串资源：获取普通字符串、格式化字符串（支持%d、%s、%f占位符）、字符串数组、复数字符串。

- 获取媒体资源：获取媒体资源的原始二进制数据或Base64编码。

- 资源覆盖：运行时动态加载和移除overlay资源，实现主题切换或资源覆盖。

本模块依赖rawfile模块，需先通过rawfile模块获取[NativeResourceManager](capi-rawfile-nativeresourcemanager.md)对象。

**起始版本：** 12

## 文件汇总

| 名称 | 描述 |
| --- | --- |
| [resmgr\_common.h](capi-resmgr-common-h.md) | 提供resourcemanager模块所需的枚举类型和结构体定义。  本头文件定义了错误码、屏幕方向、颜色模式、设备类型、屏幕密度等枚举，以及设备配置结构体，为ohresmgr.h中的资源获取函数提供数据类型支持。 |
| [ohresmgr.h](capi-ohresmgr-h.md) | 提供资源管理Native层获取资源的能力。 |
