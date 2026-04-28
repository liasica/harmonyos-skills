---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___on_binary_receive_callback
title: Rcp_OnBinaryReceiveCallback
breadcrumb: API参考 > 系统 > 网络 > Remote Communication Kit（远场通信服务） > C API > 结构体 > Rcp_OnBinaryReceiveCallback
category: harmonyos-references
scraped_at: 2026-04-28T08:09:11+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:f0da45d1343685f347c34a8919a90c50899755f5d2b9cc971dcda47c194a2bc2
---

## 概述

PhonePC/2in1TabletTVWearable

响应的二进制数据接收回调函数。可以通过[HMS\_Rcp\_SetRequestOnBinaryDataRecvCallback](remote-communication-overview.md#hms_rcp_setrequestonbinarydatarecvcallback)为请求设置相应回调函数。

**起始版本：** 5.0.1(13)

**相关模块：** [RemoteCommunication](remote-communication-overview.md)

**所在头文件：** [rcp.h](rcp_8h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [Rcp\_OnBinaryReceiveCallbackFunc](remote-communication-overview.md#rcp_onbinaryreceivecallbackfunc)[callback](_rcp___on_binary_receive_callback.md#callback) | 请求过程中接收二进制数据的回调函数。 |
| void \*[usrObject](_rcp___on_binary_receive_callback.md#usrobject) | 用户定义的对象，在回调函数中使用。 |

## 结构体成员变量说明

PhonePC/2in1TabletTVWearable

### callback

PhonePC/2in1TabletTVWearable

```
1. Rcp_OnBinaryReceiveCallbackFunc Rcp_OnBinaryReceiveCallback::callback
```

**描述**

二进制数据接收回调函数。

### usrObject

PhonePC/2in1TabletTVWearable

```
1. void* Rcp_OnBinaryReceiveCallback::usrObject
```

**描述**

用户定义的对象，在回调函数中使用。
