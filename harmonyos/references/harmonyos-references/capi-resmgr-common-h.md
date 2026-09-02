---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-resmgr-common-h
title: resmgr_common.h
breadcrumb: API参考 > 应用框架 > Localization Kit（本地化开发服务） > C API > 头文件 > resmgr_common.h
category: harmonyos-references
scraped_at: 2026-09-02T15:01:38+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:850f83c1cb1ea4c7af086b0be0c5e2d44a8e04bec4be5ab123b577f67b52518e
---

## 概述

提供resourcemanager模块所需的枚举类型和结构体定义。

本头文件定义了错误码、屏幕方向、颜色模式、设备类型、屏幕密度等枚举，以及设备配置结构体，为ohresmgr.h中的资源获取函数提供数据类型支持。

**引用文件：** <resourcemanager/resmgr\_common.h>

**库：** libohresmgr.so

**系统能力：** SystemCapability.Global.ResourceManager

**起始版本：** 12

**相关模块：** [resourcemanager](capi-resourcemanager.md)

## 汇总

### 结构体

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [ResourceManager\_Configuration](capi-resourcemanager-resourcemanager-configuration.md) | ResourceManager\_Configuration | 设备状态的结构体。 |

### 枚举

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [ResourceManager\_ErrorCode](capi-resmgr-common-h.md#resourcemanager_errorcode) | ResourceManager\_ErrorCode | 资源管理错误码。 |
| [ResourceManager\_Direction](capi-resmgr-common-h.md#resourcemanager_direction) | ResourceManager\_Direction | 屏幕方向的枚举。 |
| [ResourceManager\_ColorMode](capi-resmgr-common-h.md#resourcemanager_colormode) | ResourceManager\_ColorMode | 颜色模式的枚举。 |
| [ResourceManager\_DeviceType](capi-resmgr-common-h.md#resourcemanager_devicetype) | ResourceManager\_DeviceType | 设备类型的枚举。 |
| [ScreenDensity](capi-resmgr-common-h.md#screendensity) | ScreenDensity | 屏幕密度类型的枚举。 |

## 枚举类型说明

### ResourceManager\_ErrorCode

```c
enum ResourceManager_ErrorCode
```

**描述**

资源管理错误码。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| SUCCESS = 0 | 成功。 |
| ERROR\_CODE\_INVALID\_INPUT\_PARAMETER = 401 | 输入参数无效。 |
| ERROR\_CODE\_RES\_ID\_NOT\_FOUND = 9001001 | 无效的资源ID。 |
| ERROR\_CODE\_RES\_NOT\_FOUND\_BY\_ID = 9001002 | 根据资源ID未找到匹配的资源。 |
| ERROR\_CODE\_RES\_NAME\_NOT\_FOUND = 9001003 | 无效的资源名称。 |
| ERROR\_CODE\_RES\_NOT\_FOUND\_BY\_NAME = 9001004 | 根据资源名称未找到匹配的资源。 |
| ERROR\_CODE\_RES\_PATH\_INVALID = 9001005 | 无效的相对路径。 |
| ERROR\_CODE\_RES\_REF\_TOO\_MUCH = 9001006 | 资源存在循环引用。 |
| ERROR\_CODE\_RES\_ID\_FORMAT\_ERROR = 9001007 | 根据资源ID获得的资源格式化失败。 |
| ERROR\_CODE\_RES\_NAME\_FORMAT\_ERROR = 9001008 | 根据资源名称获得的资源格式化失败。 |
| ERROR\_CODE\_SYSTEM\_RES\_MANAGER\_GET\_FAILED = 9001009 | 访问系统资源失败。 |
| ERROR\_CODE\_OVERLAY\_RES\_PATH\_INVALID = 9001010 | 无效的overlay路径。 |
| ERROR\_CODE\_OUT\_OF\_MEMORY = 9001100 | 内存溢出。 |

### ResourceManager\_Direction

```c
enum ResourceManager_Direction
```

**描述**

屏幕方向的枚举。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| DIRECTION\_VERTICAL = 0 | 表示竖屏。 |
| DIRECTION\_HORIZONTAL = 1 | 表示横屏。 |

### ResourceManager\_ColorMode

```c
enum ResourceManager_ColorMode
```

**描述**

颜色模式的枚举。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| COLOR\_MODE\_DARK = 0 | 表示深色模式。 |
| COLOR\_MODE\_LIGHT = 1 | 表示浅色模式。 |

### ResourceManager\_DeviceType

```c
enum ResourceManager_DeviceType
```

**描述**

设备类型的枚举。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| DEVICE\_TYPE\_PHONE = 0X00 | 手机。 |
| DEVICE\_TYPE\_TABLET = 0x01 | 平板。 |
| DEVICE\_TYPE\_CAR = 0x02 | 车机。 |
| DEVICE\_TYPE\_PC = 0x03 | PC设备。 |
| DEVICE\_TYPE\_TV = 0x04 | 智慧屏。 |
| DEVICE\_TYPE\_WEARABLE = 0x06 | 穿戴。 |
| DEVICE\_TYPE\_2IN1 = 0x07 | 2in1设备。 |

### ScreenDensity

```c
enum ScreenDensity
```

**描述**

屏幕密度类型的枚举。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| SCREEN\_SDPI = 120 | 表示小屏幕密度。 |
| SCREEN\_MDPI = 160 | 表示中屏幕密度。 |
| SCREEN\_LDPI = 240 | 表示大屏幕密度。 |
| SCREEN\_XLDPI = 320 | 表示特大屏幕密度。 |
| SCREEN\_XXLDPI = 480 | 表示超大屏幕密度。 |
| SCREEN\_XXXLDPI = 640 | 表示超特大屏幕密度。 |
