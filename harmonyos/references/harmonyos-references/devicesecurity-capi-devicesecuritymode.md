---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/devicesecurity-capi-devicesecuritymode
title: DeviceSecurityMode
breadcrumb: API参考 > 系统 > 安全 > Device Security Kit（设备安全服务） > C API > 模块 > DeviceSecurityMode
category: harmonyos-references
scraped_at: 2026-04-28T08:07:17+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:7a18435369cdf6045e4216f22c4b0b894a8fed248222aaa516d1091fe0c13777
---

## 概述

PhonePC/2in1TabletWearable

DeviceSecurityMode模块用于管理设备安全模式。

**系统能力：** SystemCapability.Security.SafetyDetect

**起始版本：** 5.0.1(13)

## 汇总

PhonePC/2in1TabletWearable

### 文件

PhonePC/2in1TabletWearable

| 名称 | 描述 |
| --- | --- |
| [device\_security\_mode.h](devicesecurity-capi-device-security-mode-8h.md) | 定义与设备安全模式相关的函数。 |

### 类型定义

PhonePC/2in1TabletWearable

| 名称 | 描述 |
| --- | --- |
| typedef enum [DSM\_DeviceSecurityMode](devicesecurity-capi-devicesecuritymode.md#dsm_devicesecuritymode-1) [DSM\_DeviceSecurityMode](devicesecurity-capi-devicesecuritymode.md#dsm_devicesecuritymode) | 设备安全模式枚举类型定义。 |

### 枚举

PhonePC/2in1TabletWearable

| 名称 | 描述 |
| --- | --- |
| [DSM\_DeviceSecurityMode](devicesecurity-capi-devicesecuritymode.md#dsm_devicesecuritymode-1) {  DSM\_NORMAL\_MODE = 0,  DSM\_SECURE\_SHIELD\_MODE = 1  } | 设备安全模式枚举值。 |

### 函数

PhonePC/2in1TabletWearable

| 名称 | 描述 |
| --- | --- |
| [DSM\_DeviceSecurityMode](devicesecurity-capi-devicesecuritymode.md#dsm_devicesecuritymode-1) [HMS\_DSM\_GetDeviceSecurityMode()](devicesecurity-capi-devicesecuritymode.md#hms_dsm_getdevicesecuritymode) | 查询当前设备安全模式。 |

## 类型定义说明

PhonePC/2in1TabletWearable

### DSM\_DeviceSecurityMode

PhonePC/2in1TabletWearable

```
1. typedef enum DSM_DeviceSecurityMode DSM_DeviceSecurityMode
```

**描述**

设备安全模式枚举类型定义。

**起始版本：** 5.0.1(13)

## 枚举说明

PhonePC/2in1TabletWearable

### DSM\_DeviceSecurityMode

PhonePC/2in1TabletWearable

```
1. enum DSM_DeviceSecurityMode
```

**描述**

枚举设备安全模式。

**起始版本：** 5.0.1(13)

| 枚举值 | 描述 |
| --- | --- |
| DSM\_NORMAL\_MODE | 一般模式，为设备默认的安全模式。 |
| DSM\_SECURE\_SHIELD\_MODE | 坚盾守护模式，坚盾守护模式用于保护设备不被复杂网络攻击，此模式下部分网页的浏览功能和网络技术会受到限制。 |

## 函数说明

PhonePC/2in1TabletWearable

### HMS\_DSM\_GetDeviceSecurityMode()

PhonePC/2in1TabletWearable

```
1. DSM_DeviceSecurityMode HMS_DSM_GetDeviceSecurityMode(void)
```

**描述**

查询当前设备的安全模式。

**起始版本：** 5.0.1(13)

**返回：**

返回结果参见枚举类型[DSM\_DeviceSecurityMode](devicesecurity-capi-devicesecuritymode.md#dsm_devicesecuritymode-1)。
