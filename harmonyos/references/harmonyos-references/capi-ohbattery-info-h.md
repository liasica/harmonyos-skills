---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohbattery-info-h
title: ohbattery_info.h
breadcrumb: API参考 > 系统 > 基础功能 > Basic Services Kit（基础服务） > C API > 头文件 > ohbattery_info.h
category: harmonyos-references
scraped_at: 2026-04-28T08:09:48+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:b731cd3cb8665fdbed15d772adb0913375463c5398a899462a8896c000027abb
---

## 概述

PhonePC/2in1TabletWearable

声明电池API以获取当前电池容量和电源类型的信息，定义电池相应常见事件。

**引用文件：** <BasicServicesKit/ohbattery\_info.h>

**库：** libohbattery\_info.so

**系统能力：** SystemCapability.PowerManager.BatteryManager.Core

**起始版本：** 13

**相关模块：** [OH\_BatteryInfo](capi-oh-batteryinfo.md)

## 汇总

PhonePC/2in1TabletWearable

### 枚举

PhonePC/2in1TabletWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [BatteryInfo\_BatteryPluggedType](capi-ohbattery-info-h.md#batteryinfo_batterypluggedtype) | BatteryInfo\_BatteryPluggedType | 定义插入类型。 |

### 函数

PhonePC/2in1TabletWearable

| 名称 | 描述 |
| --- | --- |
| [int32\_t OH\_BatteryInfo\_GetCapacity()](capi-ohbattery-info-h.md#oh_batteryinfo_getcapacity) | 返回当前电池容量。 |
| [BatteryInfo\_BatteryPluggedType OH\_BatteryInfo\_GetPluggedType()](capi-ohbattery-info-h.md#oh_batteryinfo_getpluggedtype) | 返回当前插入的类型。 |

### 变量

PhonePC/2in1TabletWearable

| 名称 | 描述 |
| --- | --- |
| static const char \* COMMON\_EVENT\_KEY\_CAPACITY = "soc" | 标识电池容量变化后发送的常见事件。  **起始版本：** 13 |
| static const char \* COMMON\_EVENT\_KEY\_CHARGE\_STATE = "chargeState" | 标识充电状态更改后发送的常见事件。  **起始版本：** 13 |
| static const char \* COMMON\_EVENT\_KEY\_PLUGGED\_TYPE = "pluggedType" | 标识插入类型更改后发送的常见事件。  **起始版本：** 13 |

## 枚举类型说明

PhonePC/2in1TabletWearable

### BatteryInfo\_BatteryPluggedType

PhonePC/2in1TabletWearable

```
1. enum BatteryInfo_BatteryPluggedType
```

**描述**

定义插入类型。

**起始版本：** 13

| 枚举项 | 描述 |
| --- | --- |
| PLUGGED\_TYPE\_NONE = 0 | 电源已拔下。 |
| PLUGGED\_TYPE\_AC = 1 | 电源是交流充电。 |
| PLUGGED\_TYPE\_USB = 2 | 电源是USB DC充电。 |
| PLUGGED\_TYPE\_WIRELESS = 3 | 电源为无线充电。 |
| PLUGGED\_TYPE\_BUTT = 4 | 预留枚举 |

## 函数说明

PhonePC/2in1TabletWearable

### OH\_BatteryInfo\_GetCapacity()

PhonePC/2in1TabletWearable

```
1. int32_t OH_BatteryInfo_GetCapacity()
```

**描述**

返回当前电池容量。

**系统能力：** SystemCapability.PowerManager.BatteryManager.Core

**起始版本：** 13

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回介于0和100之间的数字。 |

### OH\_BatteryInfo\_GetPluggedType()

PhonePC/2in1TabletWearable

```
1. BatteryInfo_BatteryPluggedType OH_BatteryInfo_GetPluggedType()
```

**描述**

返回当前插入的类型。

**系统能力：** SystemCapability.PowerManager.BatteryManager.Core

**起始版本：** 13

**返回：**

| 类型 | 说明 |
| --- | --- |
| [BatteryInfo\_BatteryPluggedType](capi-ohbattery-info-h.md#batteryinfo_batterypluggedtype) | [PLUGGED\_TYPE\_NONE](capi-ohbattery-info-h.md#batteryinfo_batterypluggedtype) 如果电源被拔下。  [PLUGGED\_TYPE\_AC](capi-ohbattery-info-h.md#batteryinfo_batterypluggedtype) 如果电源是AC充电。  [PLUGGED\_TYPE\_USB](capi-ohbattery-info-h.md#batteryinfo_batterypluggedtype) 如果电源是USB DC充电。  [PLUGGED\_TYPE\_WIRELESS](capi-ohbattery-info-h.md#batteryinfo_batterypluggedtype) 如果电源是无线充电。  [PLUGGED\_TYPE\_BUTT](capi-ohbattery-info-h.md#batteryinfo_batterypluggedtype) 如果类型未知。 |
