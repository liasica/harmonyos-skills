---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___session_listener
title: Rcp_SessionListener
breadcrumb: API参考 > 系统 > 网络 > Remote Communication Kit（远场通信服务） > C API > 结构体 > Rcp_SessionListener
category: harmonyos-references
scraped_at: 2026-04-28T08:09:08+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:ac359f59d489f05bf5615324a24bb434119dca5ab8ae5bb6983ea0a980cca587
---

## 概述

PhonePC/2in1TabletTVWearable

关闭或取消会话事件的回调函数。

**起始版本：** 5.0.0(12)

**相关模块：** [RemoteCommunication](remote-communication-overview.md)

**所在头文件：** [rcp.h](rcp_8h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| void(\* [onClosed](_rcp___session_listener.md#onclosed) )(void) | 此函数在[Rcp\_Session](remote-communication-overview.md#rcp_session)关闭时调用此函数。 |
| void(\* [onCanceled](_rcp___session_listener.md#oncanceled) )(void) | 此函数在[Rcp\_Session](remote-communication-overview.md#rcp_session)取消时调用此函数。 |

## 结构体成员变量说明

PhonePC/2in1TabletTVWearable

### onCanceled

PhonePC/2in1TabletTVWearable

```
1. void(* Rcp_SessionListener::onCanceled) (void)
```

**描述**

此函数在[Rcp\_Session](remote-communication-overview.md#rcp_session)取消时调用此函数。

### onClosed

PhonePC/2in1TabletTVWearable

```
1. void(* Rcp_SessionListener::onClosed) (void)
```

**描述**

此函数在[Rcp\_Session](remote-communication-overview.md#rcp_session)关闭时调用此函数。
