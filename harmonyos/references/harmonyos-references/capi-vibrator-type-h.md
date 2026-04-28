---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-vibrator-type-h
title: vibrator_type.h
breadcrumb: API参考 > 系统 > 硬件 > Sensor Service Kit（传感器服务） > C API > 头文件 > vibrator_type.h
category: harmonyos-references
scraped_at: 2026-04-28T08:11:08+08:00
doc_updated_at: 2026-03-19
content_hash: sha256:a6f6031b665f94ed9f0b85bf15c5c182f17f08daa570f5f6a002298972aa6cfa
---

## 概述

PhonePC/2in1TabletTVWearable

为您提供标准的开放API，用于控制马达振动的启停

**引用文件：** <sensors/vibrator\_type.h>

**库：** libohvibrator.z.so

**系统能力：** SystemCapability.Sensors.MiscDevice

**起始版本：** 11

**相关模块：** [Vibrator](capi-vibrator.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 结构体

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [Vibrator\_Attribute](capi-vibrator-vibrator-attribute.md) | Vibrator\_Attribute | 马达属性。 |
| [Vibrator\_FileDescription](capi-vibrator-vibrator-filedescription.md) | Vibrator\_FileDescription | 振动文件描述。 |

### 枚举

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [Vibrator\_ErrorCode](capi-vibrator-type-h.md#vibrator_errorcode) | Vibrator\_ErrorCode | 为用户定义错误码。 |
| [Vibrator\_Usage](capi-vibrator-type-h.md#vibrator_usage) | Vibrator\_Usage | 振动优先级。 |

## 枚举类型说明

PhonePC/2in1TabletTVWearable

### Vibrator\_ErrorCode

PhonePC/2in1TabletTVWearable

```
1. enum Vibrator_ErrorCode
```

**描述**

为用户定义错误码。

**起始版本：** 11

| 枚举项 | 描述 |
| --- | --- |
| PERMISSION\_DENIED = 201 | 权限校验失败。 |
| PARAMETER\_ERROR = 401 | 参数检查失败，包括必选参数没有传入，参数类型错误等。 |
| UNSUPPORTED = 801 | 该设备不支持此 API，通常用于在设备已支持该 SysCap 时，针对其少量的 API 的支持处理。 |
| DEVICE\_OPERATION\_FAILED = 14600101 | 设备操作失败。 |

### Vibrator\_Usage

PhonePC/2in1TabletTVWearable

```
1. enum Vibrator_Usage
```

**描述**

振动优先级。

**起始版本：** 11

| 枚举项 | 描述 |
| --- | --- |
| VIBRATOR\_USAGE\_UNKNOWN = 0 | 未知场景 |
| VIBRATOR\_USAGE\_ALARM = 1 | 报警 |
| VIBRATOR\_USAGE\_RING = 2 | 铃声 |
| VIBRATOR\_USAGE\_NOTIFICATION = 3 | 通知 |
| VIBRATOR\_USAGE\_COMMUNICATION = 4 | 通信 |
| VIBRATOR\_USAGE\_TOUCH = 5 | 触摸 |
| VIBRATOR\_USAGE\_MEDIA = 6 | 媒体 |
| VIBRATOR\_USAGE\_PHYSICAL\_FEEDBACK = 7 | 物理反馈 |
| VIBRATOR\_USAGE\_SIMULATED\_REALITY = 8 | 模拟现实 |
