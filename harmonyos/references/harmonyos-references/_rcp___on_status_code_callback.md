---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___on_status_code_callback
title: Rcp_OnStatusCodeReceiveCallback
breadcrumb: API参考 > 系统 > 网络 > Remote Communication Kit（远场通信服务） > C API > 结构体 > Rcp_OnStatusCodeReceiveCallback
category: harmonyos-references
scraped_at: 2026-04-28T08:09:11+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:102afd2cd03fa0b414219df3dda39cdeafe4ddeb3e640a7c89d9ca57c39ed96c
---

## 概述

PhonePC/2in1TabletTVWearable

响应的状态码接收回调函数。可以通过[HMS\_Rcp\_SetRequestOnStatusCodeReceiveCallback](remote-communication-overview.md#hms_rcp_setrequestonstatuscodereceivecallback)为请求设置相应回调函数。

**起始版本：** 6.0.1(21)

**相关模块：** [RemoteCommunication](remote-communication-overview.md)

**所在头文件：** [rcp.h](rcp_8h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [Rcp\_OnStatusCodeReceiveCallbackFunc](remote-communication-overview.md#rcp_onstatuscodereceivecallbackfunc) | 请求过程中接收响应状态码的回调函数。 |
| void \*[usrObject](_rcp___on_status_code_callback.md#usrobject) | 用户定义的对象，在回调函数中使用。 |

## 结构体成员变量说明

PhonePC/2in1TabletTVWearable

### callback

PhonePC/2in1TabletTVWearable

```
1. Rcp_OnStatusCodeReceiveCallbackFunc Rcp_OnStatusCodeReceiveCallback::callback
```

**描述**

响应状态码接收回调函数。

### usrObject

PhonePC/2in1TabletTVWearable

```
1. void* Rcp_OnStatusCodeReceiveCallback::usrObject
```

**描述**

用户定义的对象，在回调函数中使用。
