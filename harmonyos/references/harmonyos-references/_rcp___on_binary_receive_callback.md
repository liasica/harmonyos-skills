---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___on_binary_receive_callback
title: Rcp_OnBinaryReceiveCallback
breadcrumb: API参考 > 系统 > 网络 > Remote Communication Kit（远场通信服务） > C API > 结构体 > Rcp_OnBinaryReceiveCallback
category: harmonyos-references
scraped_at: 2026-09-02T15:01:59+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:83af4c6e5a29bf37280ead35eb7be9dd557f87294e2a05f3d85f98f173dce431
---

## 概述

响应的二进制数据接收回调函数。可以通过[HMS\_Rcp\_SetRequestOnBinaryDataRecvCallback](remote-communication-overview.md#hms_rcp_setrequestonbinarydatarecvcallback)为请求设置相应回调函数。

**起始版本：** 5.0.1(13)

**相关模块：** [RemoteCommunication](remote-communication-overview.md)

**所在头文件：** [rcp.h](rcp_8h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| [Rcp\_OnBinaryReceiveCallbackFunc](remote-communication-overview.md#rcp_onbinaryreceivecallbackfunc) [callback](_rcp___on_binary_receive_callback.md#callback) | 请求过程中接收二进制数据的回调函数。 |
| void \*[usrObject](_rcp___on_binary_receive_callback.md#usrobject) | 用户定义的对象，在回调函数中使用。 |

## 结构体成员变量说明

### callback

```cpp
Rcp_OnBinaryReceiveCallbackFunc Rcp_OnBinaryReceiveCallback::callback
```

**描述**

二进制数据接收回调函数。

### usrObject

```cpp
void* Rcp_OnBinaryReceiveCallback::usrObject
```

**描述**

用户定义的对象，在回调函数中使用。
