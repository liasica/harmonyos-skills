---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-resmgr-common-h
title: resmgr_common.h
breadcrumb: API参考 > 应用框架 > Localization Kit（本地化开发服务） > C API > 头文件 > resmgr_common.h
category: harmonyos-references
scraped_at: 2026-04-28T08:06:33+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:0536555d1e994d94aaa1741dc0b3f7d9a9255ad83521979657ac2eedb715b982
---

## 概述

PhonePC/2in1TabletTVWearable

提供接口所需要的枚举类型和结构体。

**引用文件：** <resourcemanager/resmgr\_common.h>

**库：** libohresmgr.so

**系统能力：** SystemCapability.Global.ResourceManager

**起始版本：** 12

**相关模块：** [resourcemanager](capi-resourcemanager.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 结构体

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [ResourceManager\_Configuration](capi-resourcemanager-resourcemanager-configuration.md) | ResourceManager\_Configuration | 设备状态的枚举。 |

### 枚举

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [ResourceManager\_ErrorCode](capi-resmgr-common-h.md#resourcemanager_errorcode) | - | 资源管理错误码。 |
| [ScreenDensity](capi-resmgr-common-h.md#screendensity) | - | 屏幕密度类型的枚举。 |
| [ResourceManager\_Direction](capi-resmgr-common-h.md#resourcemanager_direction) | ResourceManager\_Direction | 屏幕方向的枚举。 |
| [ResourceManager\_ColorMode](capi-resmgr-common-h.md#resourcemanager_colormode) | ResourceManager\_ColorMode | 颜色模式的枚举。 |
| [ResourceManager\_DeviceType](capi-resmgr-common-h.md#resourcemanager_devicetype) | ResourceManager\_DeviceType | 设备类型的枚举。 |

## 枚举类型说明

PhonePC/2in1TabletTVWearable

### ResourceManager\_ErrorCode

PhonePC/2in1TabletTVWearable

```
1. enum ResourceManager_ErrorCode
```

**描述**

资源管理错误码。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| SUCCESS = 0 | 成功。 |
| ERROR\_CODE\_INVALID\_INPUT\_PARAMETER = 401 | 输入参数无效。 |
| ERROR\_CODE\_RES\_ID\_NOT\_FOUND = 9001001 | 无效的资源ID。 |
| ERROR\_CODE\_RES\_NOT\_FOUND\_BY\_ID = 9001002 | 无效的资源名称。 |
| ERROR\_CODE\_RES\_NAME\_NOT\_FOUND = 9001003 | 没有根据资源ID找到匹配的资源。 |
| ERROR\_CODE\_RES\_NOT\_FOUND\_BY\_NAME = 9001004 | 没有根据资源名称找到匹配的资源。 |
| ERROR\_CODE\_RES\_PATH\_INVALID = 9001005 | 无效的相对路径。 |
| ERROR\_CODE\_RES\_REF\_TOO\_MUCH = 9001006 | 资源被循环引用。 |
| ERROR\_CODE\_RES\_ID\_FORMAT\_ERROR = 9001007 | 无法格式化基于资源ID获得的资源。 |
| ERROR\_CODE\_RES\_NAME\_FORMAT\_ERROR = 9001008 | 无法格式化基于资源名称获得的资源。 |
| ERROR\_CODE\_SYSTEM\_RES\_MANAGER\_GET\_FAILED = 9001009 | 访问系统资源失败。 |
| ERROR\_CODE\_OVERLAY\_RES\_PATH\_INVALID = 9001010 | 无效的overlay路径。 |
| ERROR\_CODE\_OUT\_OF\_MEMORY = 9001100 | 内存溢出。 |

### ScreenDensity

PhonePC/2in1TabletTVWearable

```
1. enum ScreenDensity
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

### ResourceManager\_Direction

PhonePC/2in1TabletTVWearable

```
1. enum ResourceManager_Direction
```

**描述**

屏幕方向的枚举。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| DIRECTION\_VERTICAL = 0 | 表示垂直方向。 |
| DIRECTION\_HORIZONTAL = 1 | 表示水平方向。 |

### ResourceManager\_ColorMode

PhonePC/2in1TabletTVWearable

```
1. enum ResourceManager_ColorMode
```

**描述**

颜色模式的枚举。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| COLOR\_MODE\_DARK = 0 | 表示深色模式。 |
| COLOR\_MODE\_LIGHT = 1 | 表示浅色模式。 |

### ResourceManager\_DeviceType

PhonePC/2in1TabletTVWearable

```
1. enum ResourceManager_DeviceType
```

**描述**

设备类型的枚举。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| DEVICE\_TYPE\_PHONE = 0X00 | 手机。 |
| DEVICE\_TYPE\_TABLET = 0x01 | 平板。 |
| DEVICE\_TYPE\_CAR = 0x02 | 汽车。 |
| DEVICE\_TYPE\_PC = 0x03 | 电脑。 |
| DEVICE\_TYPE\_TV = 0x04 | 电视。 |
| DEVICE\_TYPE\_WEARABLE = 0x06 | 穿戴。 |
| DEVICE\_TYPE\_2IN1 = 0x07 | 2in1设备。 |
