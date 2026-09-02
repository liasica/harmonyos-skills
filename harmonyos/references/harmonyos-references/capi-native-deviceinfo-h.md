---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-deviceinfo-h
title: native_deviceinfo.h
breadcrumb: API参考 > 媒体 > AVSession Kit（音视频播控服务） > C API > 头文件 > native_deviceinfo.h
category: harmonyos-references
scraped_at: 2026-09-02T15:02:25+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:de3f9050c1e9a444fbe94480c4dac6f50490c5647e87d3d774e6115064a08fe8
---

## 概述

提供播控设备信息的定义。

**引用文件：** <multimedia/av\_session/native\_deviceinfo.h>

**库：** libohavsession.so

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**起始版本：** 23

**相关模块：** [OHAVSession](capi-ohavsession.md)

## 汇总

### 结构体

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [AVSession\_OutputDeviceInfo](capi-ohavsession-avsession-outputdeviceinfo.md) | AVSession\_OutputDeviceInfo | 目标设备信息的定义。 |
| [AVSession\_DeviceInfo](capi-ohavsession-avsession-deviceinfo.md) | AVSession\_DeviceInfo | 设备信息的声明。该实例用于获取更多的设备信息及其详细属性。 |

### 函数

| 名称 | 描述 |
| --- | --- |
| [AVSession\_ErrCode OH\_DeviceInfo\_GetAVCastCategory(AVSession\_DeviceInfo \*deviceInfo, AVSession\_AVCastCategory \*aVCastCategory)](capi-native-deviceinfo-h.md#oh_deviceinfo_getavcastcategory) | 获取目标设备的投播类别。 |
| [AVSession\_ErrCode OH\_DeviceInfo\_GetDeviceId(AVSession\_DeviceInfo \*deviceInfo, char \*\*deviceId)](capi-native-deviceinfo-h.md#oh_deviceinfo_getdeviceid) | 获取目标设备的设备ID。 |
| [AVSession\_ErrCode OH\_DeviceInfo\_GetDeviceName(AVSession\_DeviceInfo \*deviceInfo, char \*\*deviceName)](capi-native-deviceinfo-h.md#oh_deviceinfo_getdevicename) | 获取目标设备的设备名称。 |
| [AVSession\_ErrCode OH\_DeviceInfo\_GetDeviceType(AVSession\_DeviceInfo \*deviceInfo, AVSession\_DeviceType \*deviceType)](capi-native-deviceinfo-h.md#oh_deviceinfo_getdevicetype) | 获取目标设备的设备类型。 |
| [AVSession\_ErrCode OH\_DeviceInfo\_GetSupportedProtocols(AVSession\_DeviceInfo \*deviceInfo, uint32\_t \*deviceProtocolType)](capi-native-deviceinfo-h.md#oh_deviceinfo_getsupportedprotocols) | 获取目标设备支持的协议。 |

## 函数说明

### OH\_DeviceInfo\_GetAVCastCategory()

```c
AVSession_ErrCode OH_DeviceInfo_GetAVCastCategory(AVSession_DeviceInfo *deviceInfo, AVSession_AVCastCategory *aVCastCategory)
```

**描述**

获取目标设备的投播类别。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [AVSession\_DeviceInfo](capi-ohavsession-avsession-deviceinfo.md) \*deviceInfo | 表示设备信息实例指针。 |
| [AVSession\_AVCastCategory](capi-native-avsession-base-h.md#avsession_avcastcategory) \*aVCastCategory | 输出参数，用于接收投播类别的指针变量。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [AVSession\_ErrCode](capi-native-avsession-errors-h.md#avsession_errcode) | AV\_SESSION\_ERR\_SUCCESS：函数执行成功。  AV\_SESSION\_ERR\_INVALID\_PARAMETER：  1. 参数deviceInfo为nullptr。  2. 参数aVCastCategory为nullptr。 |

### OH\_DeviceInfo\_GetDeviceId()

```c
AVSession_ErrCode OH_DeviceInfo_GetDeviceId(AVSession_DeviceInfo *deviceInfo, char **deviceId)
```

**描述**

获取目标设备的设备ID。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [AVSession\_DeviceInfo](capi-ohavsession-avsession-deviceinfo.md) \*deviceInfo | 表示设备信息实例指针。 |
| char \*\*deviceId | 输出参数，用于存储获取到的设备ID字符串指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [AVSession\_ErrCode](capi-native-avsession-errors-h.md#avsession_errcode) | AV\_SESSION\_ERR\_SUCCESS：函数执行成功。  AV\_SESSION\_ERR\_INVALID\_PARAMETER：  1. 参数deviceInfo为nullptr。  2. 参数deviceId为nullptr。 |

### OH\_DeviceInfo\_GetDeviceName()

```c
AVSession_ErrCode OH_DeviceInfo_GetDeviceName(AVSession_DeviceInfo *deviceInfo, char **deviceName)
```

**描述**

获取目标设备的设备名称。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [AVSession\_DeviceInfo](capi-ohavsession-avsession-deviceinfo.md) \*deviceInfo | 表示设备信息实例指针。 |
| char \*\*deviceName | 输出参数，用于存储获取到的设备名称字符串指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [AVSession\_ErrCode](capi-native-avsession-errors-h.md#avsession_errcode) | AV\_SESSION\_ERR\_SUCCESS：函数执行成功。  AV\_SESSION\_ERR\_INVALID\_PARAMETER：  1. 参数deviceInfo为nullptr。  2. 参数deviceName为nullptr。 |

### OH\_DeviceInfo\_GetDeviceType()

```c
AVSession_ErrCode OH_DeviceInfo_GetDeviceType(AVSession_DeviceInfo *deviceInfo, AVSession_DeviceType *deviceType)
```

**描述**

获取目标设备的设备类型。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [AVSession\_DeviceInfo](capi-ohavsession-avsession-deviceinfo.md) \*deviceInfo | 表示设备信息实例指针。 |
| [AVSession\_DeviceType](capi-native-avsession-base-h.md#avsession_devicetype) \*deviceType | 输出参数，用于接收设备类型的指针，具体枚举值含义见AVSession\_DeviceType。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [AVSession\_ErrCode](capi-native-avsession-errors-h.md#avsession_errcode) | AV\_SESSION\_ERR\_SUCCESS：函数执行成功。  AV\_SESSION\_ERR\_INVALID\_PARAMETER：  1. 参数deviceInfo为nullptr。  2. 参数deviceType为nullptr。 |

### OH\_DeviceInfo\_GetSupportedProtocols()

```c
AVSession_ErrCode OH_DeviceInfo_GetSupportedProtocols(AVSession_DeviceInfo *deviceInfo, uint32_t *deviceProtocolType)
```

**描述**

获取目标设备支持的协议。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [AVSession\_DeviceInfo](capi-ohavsession-avsession-deviceinfo.md) \*deviceInfo | 表示设备信息实例指针。 |
| uint32\_t \*deviceProtocolType | 输出参数，用于接收设备支持的协议类型的指针，返回值为协议类型的位掩码组合。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [AVSession\_ErrCode](capi-native-avsession-errors-h.md#avsession_errcode) | AV\_SESSION\_ERR\_SUCCESS：函数执行成功。  AV\_SESSION\_ERR\_INVALID\_PARAMETER：  1. 参数deviceInfo为nullptr。  2. 参数deviceProtocolType为nullptr。 |
