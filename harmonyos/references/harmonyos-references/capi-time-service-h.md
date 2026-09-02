---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-time-service-h
title: time_service.h
breadcrumb: API参考 > 系统 > 基础功能 > Basic Services Kit（基础服务） > C API > 头文件 > time_service.h
category: harmonyos-references
scraped_at: 2026-09-02T15:02:05+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:5cd4b4d3e9fd8903cb61e49f38be9d8dcd5fbfccdcecb4741ba57a5f71b2e0c0
---

## 概述

声明获取时间时区信息的API。

**库：** libtime\_service\_ndk.so

**引用文件：** <BasicServicesKit/time\_service.h>

**系统能力：** SystemCapability.MiscServices.Time

**起始版本：** 12

**相关模块：** [TimeService](capi-timeservice.md)

## 汇总

### 枚举

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [TimeService\_ErrCode](capi-time-service-h.md#timeservice_errcode) | TimeService\_ErrCode | 枚举错误码。 |

### 函数

| 名称 | 描述 |
| --- | --- |
| [TimeService\_ErrCode OH\_TimeService\_GetTimeZone(char \*timeZone, uint32\_t len)](capi-time-service-h.md#oh_timeservice_gettimezone) | 获取当前系统时区。 |

## 枚举类型说明

### TimeService\_ErrCode

```c
enum TimeService_ErrCode
```

**描述**

枚举错误码。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| TIMESERVICE\_ERR\_OK = 0 | 成功。 |
| TIMESERVICE\_ERR\_INTERNAL\_ERROR = 13000001 | 获取系统参数失败。请稍后重试，若问题持续存在请检查系统服务状态。 |
| TIMESERVICE\_ERR\_INVALID\_PARAMETER = 13000002 | 无效的参数。请检查timeZone是否为NULL指针，或时区名称（不包括结束字符（'\0'））的大小是否大于或等于len。 |

## 函数说明

### OH\_TimeService\_GetTimeZone()

```c
TimeService_ErrCode OH_TimeService_GetTimeZone(char *timeZone, uint32_t len)
```

**描述**

获取当前系统时区。

**系统能力：** SystemCapability.MiscServices.Time

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| char \*timeZone | 时区ID字符数组，成功时写入当前系统时区ID字符串，当timeZone不为NULL且操作失败时写入空字符串，字符串以'\0'结尾。 |
| uint32\_t len | 时区ID字符数组分配的内存大小，当前时区字符串没有最大长度规格，建议申请足够多的内存，至少不能低于31字节。当len小于或等于实际时区字符串长度（不含结束符）时，返回TIMESERVICE\_ERR\_INVALID\_PARAMETER。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [TimeService\_ErrCode](capi-time-service-h.md#timeservice_errcode) | 返回TIMESERVICE\_ERR\_OK表示成功。  返回TIMESERVICE\_ERR\_INTERNAL\_ERROR表示获取系统参数失败，请稍后重试，若问题持续存在请检查系统服务状态。  返回TIMESERVICE\_ERR\_INVALID\_PARAMETER表示timeZone为NULL指针或时区ID（不包括结束字符（'\0'））的大小大于或等于len，请确保timeZone为有效指针且len大于时区ID的实际长度。 |
