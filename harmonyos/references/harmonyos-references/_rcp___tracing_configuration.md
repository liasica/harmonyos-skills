---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___tracing_configuration
title: Rcp_TracingConfiguration
breadcrumb: API参考 > 系统 > 网络 > Remote Communication Kit（远场通信服务） > C API > 结构体 > Rcp_TracingConfiguration
category: harmonyos-references
scraped_at: 2026-09-02T15:01:59+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:7d59599f72aba8b002ad007c25ef3c07fb88a496790f237936bafa2cf7623a1e
---

## 概述

请求追踪配置。

**起始版本：** 5.0.0(12)

**相关模块：** [RemoteCommunication](remote-communication-overview.md)

**所在头文件：** [rcp.h](rcp_8h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| bool [verbose](_rcp___tracing_configuration.md#verbose) | 请求运行时是否记录详细日志。true表示开启捕获，false表示不开启。默认值为false。如果设置了infoToCollect中的选项，则自动启用。 |
| [Rcp\_InfoToCollect](_rcp___info_to_collect.md) [infoToCollect](_rcp___tracing_configuration.md#infotocollect) | 指定要收集的请求处理事件。可以通过响应对象检查收集的事件。 |
| bool [collectTimeInfo](_rcp___tracing_configuration.md#collecttimeinfo) | 是否收集请求计时信息。true代表收集，false代表不收集。默认值为false。 |
| [Rcp\_EventsHandler](_rcp___events_handler.md) [httpEventsHandler](_rcp___tracing_configuration.md#httpeventshandler) | 监听不同HTTP事件的回调函数。 |

## 结构体成员变量说明

### collectTimeInfo

```cpp
bool Rcp_TracingConfiguration::collectTimeInfo
```

**描述**

是否收集请求计时信息。true代表收集，false代表不收集。默认值为false。

### httpEventsHandler

```cpp
Rcp_EventsHandler Rcp_TracingConfiguration::httpEventsHandler
```

**描述**

监听不同HTTP事件的回调函数。

### infoToCollect

```cpp
Rcp_InfoToCollect Rcp_TracingConfiguration::infoToCollect
```

**描述**

指定要收集的请求处理事件。可以通过响应对象检查收集的事件。

### verbose

```cpp
bool Rcp_TracingConfiguration::verbose
```

**描述**

请求运行时是否记录详细日志。true表示开启捕获，false表示不开启。默认值为false。如果设置了infoToCollect中的选项，则自动启用。
