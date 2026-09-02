---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___on_header_receive_callback
title: Rcp_OnHeaderReceiveCallback
breadcrumb: API参考 > 系统 > 网络 > Remote Communication Kit（远场通信服务） > C API > 结构体 > Rcp_OnHeaderReceiveCallback
category: harmonyos-references
scraped_at: 2026-09-02T15:01:59+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:0323347444bbb3cd40c9383f080bce16e604eb5d291b8877857c6dcde6870a43
---

## 概述

[Rcp\_EventsHandler](_rcp___events_handler.md)中配置的接收到的header的回调配置。

**起始版本：** 5.0.0(12)

**相关模块：** [RemoteCommunication](remote-communication-overview.md)

**所在头文件：** [rcp.h](rcp_8h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| [Rcp\_OnHeaderReceiveCallbackFunc](remote-communication-overview.md#rcp_onheaderreceivecallbackfunc) [callback](_rcp___on_header_receive_callback.md#callback) | 接收到的headers的回调函数。 |
| void \* [usrObject](_rcp___on_header_receive_callback.md#usrobject) | 用户定义的对象，在回调函数中使用。 |

## 结构体成员变量说明

### callback

```cpp
Rcp_OnHeaderReceiveCallbackFunc Rcp_OnHeaderReceiveCallback::callback
```

**描述**

接收到的headers的回调函数。

### usrObject

```cpp
void* Rcp_OnHeaderReceiveCallback::usrObject
```

**描述**

用户定义的对象，在回调函数中使用。
