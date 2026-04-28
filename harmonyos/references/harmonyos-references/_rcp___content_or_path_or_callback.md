---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___content_or_path_or_callback
title: Rcp_ContentOrPathOrCallback
breadcrumb: API参考 > 系统 > 网络 > Remote Communication Kit（远场通信服务） > C API > 结构体 > Rcp_ContentOrPathOrCallback
category: harmonyos-references
scraped_at: 2026-04-28T08:09:01+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:597539bffa243e40070c62d35655a261cf2687b03b67e50890d98943c1025608
---

## 概述

PhonePC/2in1TabletTVWearable

[Rcp\_FormFieldFileValue](_rcp___form_field_file_value.md)中使用的简单表单数据字段值。

**起始版本：** 5.0.0(12)

**相关模块：** [RemoteCommunication](remote-communication-overview.md)

**所在头文件：** [rcp.h](rcp_8h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [Rcp\_ContentOrPathOrCallbackType](remote-communication-overview.md#rcp_contentorpathorcallbacktype)[type](_rcp___content_or_path_or_callback.md#type) | 表示union中使用的数据类型。 |
| union {  [Rcp\_Buffer](_rcp___buffer.md) [content](_rcp___content_or_path_or_callback.md#content)  char [path](_rcp___content_or_path_or_callback.md#path) [[RCP\_MAX\_PATH\_LEN](remote-communication-overview.md#rcp_max_path_len)]  [Rcp\_GetDataCallback](remote-communication-overview.md#rcp_getdatacallback) [callback](_rcp___content_or_path_or_callback.md#callback)  } | content: 文本数据。  path: 文件路径。  callback: 获取数据的回调函数。 |

## 结构体成员变量说明

PhonePC/2in1TabletTVWearable

### callback

PhonePC/2in1TabletTVWearable

```
1. Rcp_GetDataCallback Rcp_ContentOrPathOrCallback::callback
```

**描述**

获取数据的回调。

### content

PhonePC/2in1TabletTVWearable

```
1. Rcp_Buffer Rcp_ContentOrPathOrCallback::content
```

**描述**

文本数据。

### path

PhonePC/2in1TabletTVWearable

```
1. char Rcp_ContentOrPathOrCallback::path[RCP_MAX_PATH_LEN]
```

**描述**

文件路径。

### type

PhonePC/2in1TabletTVWearable

```
1. Rcp_ContentOrPathOrCallbackType Rcp_ContentOrPathOrCallback::type
```

**描述**

union中使用的数据类型。
