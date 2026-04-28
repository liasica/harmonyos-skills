---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___on_void_callback
title: Rcp_OnVoidCallback
breadcrumb: API参考 > 系统 > 网络 > Remote Communication Kit（远场通信服务） > C API > 结构体 > Rcp_OnVoidCallback
category: harmonyos-references
scraped_at: 2026-04-28T08:09:06+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:28a11d98b825291e323658e5e92cfc0b84ba012b44b2db225a05bbe2893bbe82
---

## 概述

PhonePC/2in1TabletTVWearable

在[Rcp\_EventsHandler](_rcp___events_handler.md)中配置的数据结束或已取消事件的回调配置。

**起始版本：** 5.0.0(12)

**相关模块：** [RemoteCommunication](remote-communication-overview.md)

**所在头文件：** [rcp.h](rcp_8h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [Rcp\_OnVoidCallbackFunc](remote-communication-overview.md#rcp_onvoidcallbackfunc)[callback](_rcp___on_void_callback.md#callback) | DataEnd或Canceled事件回调函数。 |
| void \* [usrObject](_rcp___on_void_callback.md#usrobject) | 用户定义的对象，在回调函数中使用。 |

## 结构体成员变量说明

PhonePC/2in1TabletTVWearable

### callback

PhonePC/2in1TabletTVWearable

```
1. Rcp_OnVoidCallbackFunc Rcp_OnVoidCallback::callback
```

**描述**

DataEnd或Canceled事件回调函数。

### usrObject

PhonePC/2in1TabletTVWearable

```
1. void* Rcp_OnVoidCallback::usrObject
```

**描述**

用户定义的对象，在回调函数中使用。
