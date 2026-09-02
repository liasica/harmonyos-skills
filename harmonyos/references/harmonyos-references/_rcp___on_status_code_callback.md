---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___on_status_code_callback
title: Rcp_OnStatusCodeReceiveCallback
breadcrumb: API参考 > 系统 > 网络 > Remote Communication Kit（远场通信服务） > C API > 结构体 > Rcp_OnStatusCodeReceiveCallback
category: harmonyos-references
scraped_at: 2026-09-02T15:01:59+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:e3ced3ccbd231e1c055e2263654829c15a19bc0a62f5205d3f136407ed5682c0
---

## 概述

响应的状态码接收回调函数。可以通过[HMS\_Rcp\_SetRequestOnStatusCodeReceiveCallback](remote-communication-overview.md#hms_rcp_setrequestonstatuscodereceivecallback)为请求设置相应回调函数。

**起始版本：** 6.0.1(21)

**相关模块：** [RemoteCommunication](remote-communication-overview.md)

**所在头文件：** [rcp.h](rcp_8h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| [Rcp\_OnStatusCodeReceiveCallbackFunc](remote-communication-overview.md#rcp_onstatuscodereceivecallbackfunc) [callback](_rcp___on_status_code_callback.md#callback) | 请求过程中接收响应状态码的回调函数。 |
| void \*[usrObject](_rcp___on_status_code_callback.md#usrobject) | 用户定义的对象，在回调函数中使用。 |

## 结构体成员变量说明

### callback

```cpp
Rcp_OnStatusCodeReceiveCallbackFunc Rcp_OnStatusCodeReceiveCallback::callback
```

**描述**

响应状态码接收回调函数。

### usrObject

```cpp
void* Rcp_OnStatusCodeReceiveCallback::usrObject
```

**描述**

用户定义的对象，在回调函数中使用。
