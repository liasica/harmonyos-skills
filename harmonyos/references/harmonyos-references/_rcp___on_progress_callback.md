---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___on_progress_callback
title: Rcp_OnProgressCallback
breadcrumb: API参考 > 系统 > 网络 > Remote Communication Kit（远场通信服务） > C API > 结构体 > Rcp_OnProgressCallback
category: harmonyos-references
scraped_at: 2026-04-28T08:09:06+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:c3beb6d0c660b2b5b07b77407f92decc63e4e17d4796c2fc9ec0964237ccad56
---

## 概述

PhonePC/2in1TabletTVWearable

收发时回调配置，在[Rcp\_EventsHandler](_rcp___events_handler.md)中配置。

**起始版本：** 5.0.0(12)

**相关模块：** [RemoteCommunication](remote-communication-overview.md)

**所在头文件：** [rcp.h](rcp_8h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [Rcp\_OnProgressCallbackFunc](remote-communication-overview.md#rcp_onprogresscallbackfunc)[callback](_rcp___on_progress_callback.md#callback) | 收发过程中的回调函数。 |
| void \* [usrObject](_rcp___on_progress_callback.md#usrobject) | 用户定义的对象，在回调函数中使用。 |

## 结构体成员变量说明

PhonePC/2in1TabletTVWearable

### callback

PhonePC/2in1TabletTVWearable

```
1. Rcp_OnProgressCallbackFunc Rcp_OnProgressCallback::callback
```

**描述**

收发过程中的回调函数。

### usrObject

PhonePC/2in1TabletTVWearable

```
1. void* Rcp_OnProgressCallback::usrObject
```

**描述**

用户定义的对象，在回调函数中使用。
