---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___session_listener
title: Rcp_SessionListener
breadcrumb: API参考 > 系统 > 网络 > Remote Communication Kit（远场通信服务） > C API > 结构体 > Rcp_SessionListener
category: harmonyos-references
scraped_at: 2026-09-02T15:01:59+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:0cf5048269e17708fa99be5a17df1e6caf83315b250e3a6b611dae837c51a3aa
---

## 概述

关闭或取消会话事件的回调函数。

**起始版本：** 5.0.0(12)

**相关模块：** [RemoteCommunication](remote-communication-overview.md)

**所在头文件：** [rcp.h](rcp_8h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| void(\* [onClosed](_rcp___session_listener.md#onclosed) )(void) | 此函数在[Rcp\_Session](remote-communication-overview.md#rcp_session)关闭时调用此函数。 |
| void(\* [onCanceled](_rcp___session_listener.md#oncanceled) )(void) | 此函数在[Rcp\_Session](remote-communication-overview.md#rcp_session)取消时调用此函数。 |

## 结构体成员变量说明

### onCanceled

```cpp
void(* Rcp_SessionListener::onCanceled) (void)
```

**描述**

此函数在[Rcp\_Session](remote-communication-overview.md#rcp_session)取消时调用此函数。

### onClosed

```cpp
void(* Rcp_SessionListener::onClosed) (void)
```

**描述**

此函数在[Rcp\_Session](remote-communication-overview.md#rcp_session)关闭时调用此函数。
