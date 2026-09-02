---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___response_callback_object
title: Rcp_ResponseCallbackObject
breadcrumb: API参考 > 系统 > 网络 > Remote Communication Kit（远场通信服务） > C API > 结构体 > Rcp_ResponseCallbackObject
category: harmonyos-references
scraped_at: 2026-09-02T15:01:59+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:73c6fe539494ce83a8f754af9a8735e93d86a20d7b9658f12633ddb497cb7a33
---

## 概述

响应回调结构体。

**起始版本：** 5.0.0(12)

**相关模块：** [RemoteCommunication](remote-communication-overview.md)

**所在头文件：** [rcp.h](rcp_8h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| [Rcp\_ResponseCallback](remote-communication-overview.md#rcp_responsecallback) [callback](_rcp___response_callback_object.md#callback) | 响应回调函数。 |
| void \* [usrCtx](_rcp___response_callback_object.md#usrctx) | 用户上下文。 |

## 结构体成员变量说明

### callback

```cpp
Rcp_ResponseCallback Rcp_ResponseCallbackObject::callback
```

**描述**

响应回调函数。

### usrCtx

```cpp
void* Rcp_ResponseCallbackObject::usrCtx
```

**描述**

用户上下文。
