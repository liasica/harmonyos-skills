---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___tracing_configuration
title: Rcp_TracingConfiguration
breadcrumb: API参考 > 系统 > 网络 > Remote Communication Kit（远场通信服务） > C API > 结构体 > Rcp_TracingConfiguration
category: harmonyos-references
scraped_at: 2026-04-28T08:09:10+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:fbecfb9d0716a09a6e68632b7540db8a0e637aa5d6716062b2392e89473c9e4f
---

## 概述

PhonePC/2in1TabletTVWearable

请求追踪配置。

**起始版本：** 5.0.0(12)

**相关模块：** [RemoteCommunication](remote-communication-overview.md)

**所在头文件：** [rcp.h](rcp_8h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| bool [verbose](_rcp___tracing_configuration.md#verbose) | 请求运行时是否记录详细日志。默认值为false。如果设置了infoToCollect中的选项，则自动启用。 |
| [Rcp\_InfoToCollect](_rcp___info_to_collect.md)[infoToCollect](_rcp___tracing_configuration.md#infotocollect) | 指定要收集的请求处理事件。可以通过响应对象检查收集的事件。 |
| bool [collectTimeInfo](_rcp___tracing_configuration.md#collecttimeinfo) | 是否收集请求计时信息。默认值为false。 |
| [Rcp\_EventsHandler](_rcp___events_handler.md)[httpEventsHandler](_rcp___tracing_configuration.md#httpeventshandler) | 监听不同HTTP事件的回调函数。 |

## 结构体成员变量说明

PhonePC/2in1TabletTVWearable

### collectTimeInfo

PhonePC/2in1TabletTVWearable

```
1. bool Rcp_TracingConfiguration::collectTimeInfo
```

**描述**

是否收集请求计时信息。默认值为false。

### httpEventsHandler

PhonePC/2in1TabletTVWearable

```
1. Rcp_EventsHandler Rcp_TracingConfiguration::httpEventsHandler
```

**描述**

监听不同HTTP事件的回调函数。

### infoToCollect

PhonePC/2in1TabletTVWearable

```
1. Rcp_InfoToCollect Rcp_TracingConfiguration::infoToCollect
```

**描述**

指定要收集的请求处理事件。可以通过响应对象检查收集的事件。

### verbose

PhonePC/2in1TabletTVWearable

```
1. bool Rcp_TracingConfiguration::verbose
```

**描述**

请求运行时是否记录详细日志。默认值为false。如果设置了infoToCollect中的选项，则自动启用。
