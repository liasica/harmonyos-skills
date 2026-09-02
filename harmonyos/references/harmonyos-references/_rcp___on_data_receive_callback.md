---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___on_data_receive_callback
title: Rcp_OnDataReceiveCallback
breadcrumb: API参考 > 系统 > 网络 > Remote Communication Kit（远场通信服务） > C API > 结构体 > Rcp_OnDataReceiveCallback
category: harmonyos-references
scraped_at: 2026-09-02T15:01:59+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:0afa408b0688bc94dc669e3889a46a1be10096a117f37b13b0cd1a9050270b05
---

## 概述

接收到数据时回调。[Rcp\_EventsHandler](_rcp___events_handler.md)中的配置。

**起始版本：** 5.0.0(12)

**相关模块：** [RemoteCommunication](remote-communication-overview.md)

**所在头文件：** [rcp.h](rcp_8h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| [Rcp\_OnDataReceiveCallbackFunc](remote-communication-overview.md#rcp_ondatareceivecallbackfunc) [callback](_rcp___on_data_receive_callback.md#callback) | 接收数据回调函数。 |
| void \* [usrObject](_rcp___on_data_receive_callback.md#usrobject) | 用户定义的对象，在回调函数中使用。 |

## 结构体成员变量说明

### callback

```cpp
Rcp_OnDataReceiveCallbackFunc Rcp_OnDataReceiveCallback::callback
```

**描述**

接收数据回调函数。

### usrObject

```cpp
void* Rcp_OnDataReceiveCallback::usrObject
```

**描述**

用户定义的对象，在回调函数中使用。
