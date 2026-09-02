---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/devicesecurity-capi-device-security-mode-8h
title: device_security_mode.h
breadcrumb: API参考 > 系统 > 安全 > Device Security Kit（设备安全服务） > C API > 头文件 > device_security_mode.h
category: harmonyos-references
scraped_at: 2026-09-02T15:01:43+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:6cf3a8cf10a7412a768e85b1afdcbc4910267338eeb158c2480adc7a7e141c4a
---

## 概述

文件中定义了与设备安全模式相关的函数。

**引用文件：** <DeviceSecurityKit/device\_security\_mode.h>

**库：** libdevice\_security\_mode.z.so

**系统能力：** SystemCapability.Security.SafetyDetect

**起始版本：** 5.0.1(13)

**相关模块：** [DeviceSecurityMode](devicesecurity-capi-devicesecuritymode.md)

## 汇总

### 类型定义

| 名称 | 描述 |
| --- | --- |
| typedef enum [DSM\_DeviceSecurityMode](devicesecurity-capi-devicesecuritymode.md#dsm_devicesecuritymode-1) [DSM\_DeviceSecurityMode](devicesecurity-capi-devicesecuritymode.md#dsm_devicesecuritymode) | 设备安全模式枚举类型定义。 |

### 枚举

| 名称 | 描述 |
| --- | --- |
| [DSM\_DeviceSecurityMode](devicesecurity-capi-devicesecuritymode.md#dsm_devicesecuritymode-1) {  DSM\_NORMAL\_MODE = 0,  DSM\_SECURE\_SHIELD\_MODE = 1  } | 设备安全模式枚举值。 |

### 函数

| 名称 | 描述 |
| --- | --- |
| [DSM\_DeviceSecurityMode](devicesecurity-capi-devicesecuritymode.md#dsm_devicesecuritymode-1) [HMS\_DSM\_GetDeviceSecurityMode(void)](devicesecurity-capi-devicesecuritymode.md#hms_dsm_getdevicesecuritymode) | 查询当前设备安全模式。 |
