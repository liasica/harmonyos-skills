---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hiappevent-event-h
title: hiappevent_event.h
breadcrumb: API参考 > 系统 > 调测调优 > Performance Analysis Kit（性能分析服务） > C API > 头文件 > hiappevent_event.h
category: harmonyos-references
scraped_at: 2026-04-28T08:11:21+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:624897635fd1e9d75d308ed12f2af1e3f8a25d6f83fb029afded88d9608f1e30
---

## 概述

PhonePC/2in1TabletTVWearable

定义所有预定义事件的事件名称。除了与特定应用关联的自定义事件之外，开发者还可以使用预定义事件进行打点。

**引用文件：** <hiappevent/hiappevent\_event.h>

**库：** libhiappevent\_ndk.z.so

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

**起始版本：** 8

**相关模块：** [HiAppEvent](capi-hiappevent.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 宏定义

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [EVENT\_USER\_LOGIN](capi-hiappevent-event-h.md#event_user_login) "hiappevent.user\_login" | 用户登录事件。  **起始版本：** 8 |
| [EVENT\_USER\_LOGOUT](capi-hiappevent-event-h.md#event_user_logout) "hiappevent.user\_logout" | 用户登出事件。  **起始版本：** 8 |
| [EVENT\_DISTRIBUTED\_SERVICE\_START](capi-hiappevent-event-h.md#event_distributed_service_start) "hiappevent.distributed\_service\_start" | 分布式服务事件。  **起始版本：** 8 |
| [EVENT\_APP\_CRASH](capi-hiappevent-event-h.md#event_app_crash) "APP\_CRASH" | 崩溃事件。  **起始版本：** 12 |
| [EVENT\_APP\_FREEZE](capi-hiappevent-event-h.md#event_app_freeze) "APP\_FREEZE" | 应用冻屏事件。  **起始版本：** 12 |
| [EVENT\_APP\_LAUNCH](capi-hiappevent-event-h.md#event_app_launch) "APP\_LAUNCH" | 启动耗时事件。  **起始版本：** 12 |
| [EVENT\_SCROLL\_JANK](capi-hiappevent-event-h.md#event_scroll_jank) "SCROLL\_JANK" | 滑动丢帧事件。  **起始版本：** 12 |
| [EVENT\_CPU\_USAGE\_HIGH](capi-hiappevent-event-h.md#event_cpu_usage_high) "CPU\_USAGE\_HIGH" | CPU高负载事件。  **起始版本：** 12 |
| [EVENT\_BATTERY\_USAGE](capi-hiappevent-event-h.md#event_battery_usage) "BATTERY\_USAGE" | 24h功耗器件分解统计事件。  **起始版本：** 12 |
| [EVENT\_RESOURCE\_OVERLIMIT](capi-hiappevent-event-h.md#event_resource_overlimit) "RESOURCE\_OVERLIMIT" | 资源泄漏事件。  **起始版本：** 12 |
| [EVENT\_ADDRESS\_SANITIZER](capi-hiappevent-event-h.md#event_address_sanitizer) "ADDRESS\_SANITIZER" | 地址越界事件。  **起始版本：** 12 |
| [EVENT\_MAIN\_THREAD\_JANK](capi-hiappevent-event-h.md#event_main_thread_jank) "MAIN\_THREAD\_JANK" | 主线程超时事件。  **起始版本：** 12 |
| [EVENT\_APP\_HICOLLIE](capi-hiappevent-event-h.md#event_app_hicollie) "APP\_HICOLLIE" | 任务执行超时事件。  **起始版本：** 18 |
| [EVENT\_APP\_KILLED](capi-hiappevent-event-h.md#event_app_killed) "APP\_KILLED" | 应用终止事件。  **起始版本：** 20 |
| [EVENT\_AUDIO\_JANK\_FRAME](capi-hiappevent-event-h.md#event_audio_jank_frame) "AUDIO\_JANK\_FRAME" | 音频卡顿事件。  **起始版本：** 21 |
| [DOMAIN\_OS](capi-hiappevent-event-h.md#domain_os) "OS" | OS作用域。  **起始版本：** 12 |
| [EVENT\_MAIN\_THREAD\_JANK\_V2](capi-hiappevent-event-h.md#event_main_thread_jank_v2) "MAIN\_THREAD\_JANK\_V2" | 用于设置主线程超时事件配置策略。  **起始版本：** 22 |

## 宏定义说明

PhonePC/2in1TabletTVWearable

### EVENT\_USER\_LOGIN

PhonePC/2in1TabletTVWearable

```
1. #define EVENT_USER_LOGIN "hiappevent.user_login"
```

**描述**

用户登录事件。

**起始版本：** 8

### EVENT\_USER\_LOGOUT

PhonePC/2in1TabletTVWearable

```
1. #define EVENT_USER_LOGOUT "hiappevent.user_logout"
```

**描述**

用户登出事件。

**起始版本：** 8

### EVENT\_DISTRIBUTED\_SERVICE\_START

PhonePC/2in1TabletTVWearable

```
1. #define EVENT_DISTRIBUTED_SERVICE_START "hiappevent.distributed_service_start"
```

**描述**

分布式服务事件。

**起始版本：** 8

### EVENT\_APP\_CRASH

PhonePC/2in1TabletTVWearable

```
1. #define EVENT_APP_CRASH "APP_CRASH"
```

**描述**

崩溃事件。

**起始版本：** 12

### EVENT\_APP\_FREEZE

PhonePC/2in1TabletTVWearable

```
1. #define EVENT_APP_FREEZE "APP_FREEZE"
```

**描述**

应用冻屏事件。

**起始版本：** 12

### EVENT\_APP\_LAUNCH

PhonePC/2in1TabletTVWearable

```
1. #define EVENT_APP_LAUNCH "APP_LAUNCH"
```

**描述**

启动耗时事件。

**起始版本：** 12

### EVENT\_SCROLL\_JANK

PhonePC/2in1TabletTVWearable

```
1. #define EVENT_SCROLL_JANK "SCROLL_JANK"
```

**描述**

滑动丢帧事件。

**起始版本：** 12

### EVENT\_CPU\_USAGE\_HIGH

PhonePC/2in1TabletTVWearable

```
1. #define EVENT_CPU_USAGE_HIGH "CPU_USAGE_HIGH"
```

**描述**

CPU高负载事件。

**起始版本：** 12

### EVENT\_BATTERY\_USAGE

PhonePC/2in1TabletTVWearable

```
1. #define EVENT_BATTERY_USAGE "BATTERY_USAGE"
```

**描述**

24h功耗器件分解统计事件。

**起始版本：** 12

### EVENT\_RESOURCE\_OVERLIMIT

PhonePC/2in1TabletTVWearable

```
1. #define EVENT_RESOURCE_OVERLIMIT "RESOURCE_OVERLIMIT"
```

**描述**

资源泄漏事件。

**起始版本：** 12

### EVENT\_ADDRESS\_SANITIZER

PhonePC/2in1TabletTVWearable

```
1. #define EVENT_ADDRESS_SANITIZER "ADDRESS_SANITIZER"
```

**描述**

地址越界事件。

**起始版本：** 12

### EVENT\_MAIN\_THREAD\_JANK

PhonePC/2in1TabletTVWearable

```
1. #define EVENT_MAIN_THREAD_JANK "MAIN_THREAD_JANK"
```

**描述**

主线程超时事件。

**起始版本：** 12

### EVENT\_APP\_HICOLLIE

PhonePC/2in1TabletTVWearable

```
1. #define EVENT_APP_HICOLLIE "APP_HICOLLIE"
```

**描述**

任务执行超时事件。

**起始版本：** 18

### EVENT\_APP\_KILLED

PhonePC/2in1TabletTVWearable

```
1. #define EVENT_APP_KILLED "APP_KILLED"
```

**描述**

应用终止事件。

**起始版本：** 20

### EVENT\_AUDIO\_JANK\_FRAME

PhonePC/2in1TabletTVWearable

```
1. #define EVENT_AUDIO_JANK_FRAME "AUDIO_JANK_FRAME"
```

**描述**

音频卡顿事件。

**起始版本：** 21

### DOMAIN\_OS

PhonePC/2in1TabletTVWearable

```
1. #define DOMAIN_OS "OS"
```

**描述**

OS作用域。

**起始版本：** 12

### EVENT\_MAIN\_THREAD\_JANK\_V2

PhonePC/2in1TabletTVWearable

```
1. #define EVENT_MAIN_THREAD_JANK_V2 "MAIN_THREAD_JANK_V2"
```

**描述**

用于设置主线程超时事件配置策略。

**起始版本：** 22
