---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xeg-extensionproperties
title: XEG_ExtensionProperties
breadcrumb: API参考 > 图形 > XEngine Kit（GPU加速引擎服务） > C API > 头文件和结构体 > 结构体 > XEG_ExtensionProperties
category: harmonyos-references
scraped_at: 2026-09-02T15:02:49+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:90bfc25ce6742972cace1795bc6e76925c2e586012bc2d2a607f2469a283f4c6
---

## 概述

此结构体描述通过[HMS\_XEG\_EnumerateDeviceExtensionProperties](xengine-kit-xengine.md#hms_xeg_enumeratedeviceextensionproperties)接口查询到的XEngine扩展特性集合。

**起始版本：** 5.0.0(12)

**相关模块：** [XEngine](xengine-kit-xengine.md)

**所在头文件：** [xeg\_vulkan\_extension.h](xengine-kit-xeg-vulkan-extension-8h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| char [extensionName](xengine-kit-xeg-extensionproperties.md#extensionname) [[XEG\_MAX\_EXTENSION\_NAME\_SIZE](xengine-kit-xengine.md#xeg_max_extension_name_size)] | XEngine支持的扩展特性名称。 |
| uint32\_t [version](xengine-kit-xeg-extensionproperties.md#version) | XEngine支持的扩展特性版本号。 |

## 结构体成员变量说明

### extensionName

```cpp
char XEG_ExtensionProperties::extensionName[XEG_MAX_EXTENSION_NAME_SIZE]
```

**描述**

XEngine支持的扩展特性名称。

### version

```cpp
uint32_t XEG_ExtensionProperties::version
```

**描述**

XEngine支持的扩展特性版本号。
