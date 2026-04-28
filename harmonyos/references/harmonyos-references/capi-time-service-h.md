---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-time-service-h
title: time_service.h
breadcrumb: API参考 > 系统 > 基础功能 > Basic Services Kit（基础服务） > C API > 头文件 > time_service.h
category: harmonyos-references
scraped_at: 2026-04-28T08:09:50+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:eb11ce014b8eaccbd1394234808ec0c91ca27125034e77da124ac9f7cfd61a90
---

## 概述

PhonePC/2in1TabletTVWearable

声明获取时间时区信息的API。

**库：** libtime\_service\_ndk.so

**引用文件：** <BasicServicesKit/time\_service.h>

**系统能力：** SystemCapability.MiscServices.Time

**起始版本：** 12

**相关模块：** [TimeService](capi-timeservice.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 枚举

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [TimeService\_ErrCode](capi-time-service-h.md#timeservice_errcode) | TimeService\_ErrCode | 枚举错误码。 |

### 函数

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [TimeService\_ErrCode OH\_TimeService\_GetTimeZone(char \*timeZone, uint32\_t len)](capi-time-service-h.md#oh_timeservice_gettimezone) | 获取当前系统时区。 |

## 枚举类型说明

PhonePC/2in1TabletTVWearable

### TimeService\_ErrCode

PhonePC/2in1TabletTVWearable

```
1. enum TimeService_ErrCode
```

**描述**

枚举错误码。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| TIMESERVICE\_ERR\_OK = 0 | 成功。 |
| TIMESERVICE\_ERR\_INTERNAL\_ERROR = 13000001 | 获取系统参数失败。 |
| TIMESERVICE\_ERR\_INVALID\_PARAMETER = 13000002 | 无效的参数。 |

## 函数说明

PhonePC/2in1TabletTVWearable

### OH\_TimeService\_GetTimeZone()

PhonePC/2in1TabletTVWearable

```
1. TimeService_ErrCode OH_TimeService_GetTimeZone(char *timeZone, uint32_t len)
```

**描述**

获取当前系统时区。

**系统能力：** SystemCapability.MiscServices.Time

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| char \*timeZone | 时区ID字符数组，成功时写入当前系统时区ID字符串，失败时写入空字符串，字符串以'\0'结尾。 |
| uint32\_t len | 时区ID字符数组分配的内存大小，当前时区字符串没有最大长度规格，建议申请足够多的内存，至少不能低于31字节。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [TimeService\_ErrCode](capi-time-service-h.md#timeservice_errcode) | 返回TIMESERVICE\_ERR\_OK表示成功。  返回TIMESERVICE\_ERR\_INTERNAL\_ERROR表示获取系统参数失败。  返回TIMESERVICE\_ERR\_INVALID\_PARAMETER表示timeZone为NULL指针或时区名称（不包括结束字符（'\0'））的大小大于或等于len。 |
