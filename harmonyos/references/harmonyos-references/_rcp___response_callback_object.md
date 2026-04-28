---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___response_callback_object
title: Rcp_ResponseCallbackObject
breadcrumb: API参考 > 系统 > 网络 > Remote Communication Kit（远场通信服务） > C API > 结构体 > Rcp_ResponseCallbackObject
category: harmonyos-references
scraped_at: 2026-04-28T08:09:07+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:028ca606b791c28f68d7ee5fd6f3530ca6f5a35a3a0ed3d358b22065a0036987
---

## 概述

PhonePC/2in1TabletTVWearable

响应回调结构体。

**起始版本：** 5.0.0(12)

**相关模块：** [RemoteCommunication](remote-communication-overview.md)

**所在头文件：** [rcp.h](rcp_8h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [Rcp\_ResponseCallback](remote-communication-overview.md#rcp_responsecallback)[callback](_rcp___response_callback_object.md#callback) | 响应回调函数。 |
| void \* [usrCtx](_rcp___response_callback_object.md#usrctx) | 用户上下文。 |

## 结构体成员变量说明

PhonePC/2in1TabletTVWearable

### callback

PhonePC/2in1TabletTVWearable

```
1. Rcp_ResponseCallback Rcp_ResponseCallbackObject::callback
```

**描述**

响应回调函数。

### usrCtx

PhonePC/2in1TabletTVWearable

```
1. void* Rcp_ResponseCallbackObject::usrCtx
```

**描述**

用户上下文。
