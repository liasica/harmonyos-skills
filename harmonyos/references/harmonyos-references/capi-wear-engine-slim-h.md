---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-wear-engine-slim-h
title: wear_engine_slim.h
breadcrumb: API参考 > 系统 > 硬件 > Wear Engine Kit（穿戴服务） > C API > 头文件 > wear_engine_slim.h
category: harmonyos-references
scraped_at: 2026-11-12T09:56:12+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:63c1c10a55b91c6a8cb0fa40154a6c198dc336b8da3b5c42c1c34faa1b9285eb
---

## 概述

为动态库和应用间提供数据交互能力。

**引用文件：** <wear\_engine\_slim.h>

**库：** libwear\_engine\_slim\_ndk.so

**系统能力：** SystemCapability.Health.WearEngine.Slim

**起始版本：** 26.0.1

**相关模块：** [NativeBridge](capi-nativebridge.md)

## 汇总

### 结构体

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [HMS\_NativeBridge\_OnGoingInfo](capi-nativebridge-hms-nativebridge-ongoinginfo.md) | HMS\_NativeBridge\_OnGoingInfo | 控制小图标显示状态的信息结构体。 |
| [HMS\_NativeBridge\_AddrInfo](capi-nativebridge-hms-nativebridge-addrinfo.md) | HMS\_NativeBridge\_AddrInfo | 应用的地址信息结构体。 |

### 函数

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [typedef void (\*HMS\_NativeBridge\_InstallerCallback)(const uint8\_t resultCode, const void \*resultMessage)](capi-wear-engine-slim-h.md#hms_nativebridge_installercallback) | HMS\_NativeBridge\_InstallerCallback | 当应用小图标显示时长到期后，设备将回调通知应用。 |
| [void HMS\_NativeBridge\_CallbackJs(const char\* params, uint32\_t useCallback, uint32\_t context)](capi-wear-engine-slim-h.md#hms_nativebridge_callbackjs) | - | 动态库回调至应用的函数。 |
| [void HMS\_NativeBridge\_MemoryFree(const void \*addrInfo)](capi-wear-engine-slim-h.md#hms_nativebridge_memoryfree) | - | 释放内存地址，同一地址不可重复释放。 |
| [void HMS\_NativeBridge\_SetOngoingDisplay(HMS\_NativeBridge\_OnGoingInfo info)](capi-wear-engine-slim-h.md#hms_nativebridge_setongoingdisplay) | - | 将后台运行的应用以小图标形式显示在前台，点击小图标后可拉起或进入应用。 |

## 函数说明

### HMS\_NativeBridge\_InstallerCallback()

```c
typedef void (*HMS_NativeBridge_InstallerCallback)(const uint8_t resultCode, const void *resultMessage)
```

**描述**

当应用小图标显示时长到期后，设备将回调通知应用。

**起始版本：** 26.0.1

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const uint8\_t resultCode | 错误码。 |
| const void \*resultMessage | 错误描述。 |

### HMS\_NativeBridge\_CallbackJs()

```c
void HMS_NativeBridge_CallbackJs(const char* params, uint32_t useCallback, uint32_t context)
```

**描述**

动态库回调至应用的函数。

**起始版本：** 26.0.1

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const char\* params | 动态库传递给应用的数据。 |
| uint32\_t useCallback | 动态库回调至应用的回调函数地址。 |
| uint32\_t context | 动态库回调至应用的上下文地址。 |

### HMS\_NativeBridge\_MemoryFree()

```c
void HMS_NativeBridge_MemoryFree(const void *addrInfo)
```

**描述**

释放内存地址，同一地址不可重复释放。

**起始版本：** 26.0.1

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const void \*addrInfo | HMS\_Native\_AddrInfo结构体指针，不可为空。 |

### HMS\_NativeBridge\_SetOngoingDisplay()

```c
void HMS_NativeBridge_SetOngoingDisplay(HMS_NativeBridge_OnGoingInfo info)
```

**描述**

将后台运行的应用以小图标形式显示在前台，点击小图标后可拉起或进入应用。

**起始版本：** 26.0.1

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [HMS\_NativeBridge\_OnGoingInfo](capi-nativebridge-hms-nativebridge-ongoinginfo.md) info | 用于控制小图标显示与否的结构体信息，由调用该函数的应用传入。 |
