---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___on_data_receive_callback
title: Rcp_OnDataReceiveCallback
breadcrumb: API参考 > 系统 > 网络 > Remote Communication Kit（远场通信服务） > C API > 结构体 > Rcp_OnDataReceiveCallback
category: harmonyos-references
scraped_at: 2026-04-28T08:09:05+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:b81a4440f1d7abad3c9f4f74dbc1972d909048e37a8dd401894a64016c845de2
---

## 概述

PhonePC/2in1TabletTVWearable

接收到数据时回调。[Rcp\_EventsHandler](_rcp___events_handler.md)中的配置。

**起始版本：** 5.0.0(12)

**相关模块：** [RemoteCommunication](remote-communication-overview.md)

**所在头文件：** [rcp.h](rcp_8h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [Rcp\_OnDataReceiveCallbackFunc](remote-communication-overview.md#rcp_ondatareceivecallbackfunc)[callback](_rcp___on_data_receive_callback.md#callback) | 接收数据回调函数。 |
| void \* [usrObject](_rcp___on_data_receive_callback.md#usrobject) | 用户定义的对象，在回调函数中使用。 |

## 结构体成员变量说明

PhonePC/2in1TabletTVWearable

### callback

PhonePC/2in1TabletTVWearable

```
1. Rcp_OnDataReceiveCallbackFunc Rcp_OnDataReceiveCallback::callback
```

**描述**

接收数据回调函数。

### usrObject

PhonePC/2in1TabletTVWearable

```
1. void* Rcp_OnDataReceiveCallback::usrObject
```

**描述**

用户定义的对象，在回调函数中使用。
