---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___on_get_data_callback
title: Rcp_OnGetDataCallback
breadcrumb: API参考 > 系统 > 网络 > Remote Communication Kit（远场通信服务） > C API > 结构体 > Rcp_OnGetDataCallback
category: harmonyos-references
scraped_at: 2026-09-02T15:01:59+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:e859dfaf864f536ae15359e0e64def441dd43bce3a86d3392ac69dbe2a2152fe
---

## 概述

获取数据的回调。可以通过[HMS\_Rcp\_SetRequestGetDataCallback](remote-communication-overview.md#hms_rcp_setrequestgetdatacallback)为请求设置相应回调函数。

**起始版本：** 26.0.0

**相关模块：** [RemoteCommunication](remote-communication-overview.md)

**所在头文件：** [rcp.h](rcp_8h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| [Rcp\_GetDataCallbackFunc](remote-communication-overview.md#rcp_ongetdatacallback) [callback](_rcp___on_get_data_callback.md#callback) | 请求过程中获取数据的回调函数。 |
| void \*[userObject](_rcp___on_get_data_callback.md#userobject) | 用户定义的对象，在回调函数中使用。 |

## 结构体成员变量说明

### callback

```cpp
Rcp_GetDataCallbackFunc Rcp_OnGetDataCallback::callback
```

**描述**

获取数据的回调函数。

### userObject

```cpp
void* Rcp_OnGetDataCallback::userObject
```

**描述**

用户定义的对象，在回调函数中使用。
