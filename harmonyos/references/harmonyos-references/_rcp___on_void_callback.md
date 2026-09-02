---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___on_void_callback
title: Rcp_OnVoidCallback
breadcrumb: API参考 > 系统 > 网络 > Remote Communication Kit（远场通信服务） > C API > 结构体 > Rcp_OnVoidCallback
category: harmonyos-references
scraped_at: 2026-09-02T15:01:59+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:e5f9e20c784cd07f0d6bb1c24928f3f533872dc36a8056321d8660d06e41957a
---

## 概述

在[Rcp\_EventsHandler](_rcp___events_handler.md)中配置的数据结束或已取消事件的回调配置。

**起始版本：** 5.0.0(12)

**相关模块：** [RemoteCommunication](remote-communication-overview.md)

**所在头文件：** [rcp.h](rcp_8h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| [Rcp\_OnVoidCallbackFunc](remote-communication-overview.md#rcp_onvoidcallbackfunc) [callback](_rcp___on_void_callback.md#callback) | DataEnd或Canceled事件回调函数。 |
| void \* [usrObject](_rcp___on_void_callback.md#usrobject) | 用户定义的对象，在回调函数中使用。 |

## 结构体成员变量说明

### callback

```cpp
Rcp_OnVoidCallbackFunc Rcp_OnVoidCallback::callback
```

**描述**

DataEnd或Canceled事件回调函数。

### usrObject

```cpp
void* Rcp_OnVoidCallback::usrObject
```

**描述**

用户定义的对象，在回调函数中使用。
