---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___content_or_path_or_callback
title: Rcp_ContentOrPathOrCallback
breadcrumb: API参考 > 系统 > 网络 > Remote Communication Kit（远场通信服务） > C API > 结构体 > Rcp_ContentOrPathOrCallback
category: harmonyos-references
scraped_at: 2026-09-02T15:01:58+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:496b00b32fe9c2da04bdabed4336a609107f52d6ae1c80b9ba2e29f8e5957485
---

## 概述

[Rcp\_FormFieldFileValue](_rcp___form_field_file_value.md)中使用的简单表单数据字段值。

**起始版本：** 5.0.0(12)

**相关模块：** [RemoteCommunication](remote-communication-overview.md)

**所在头文件：** [rcp.h](rcp_8h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| [Rcp\_ContentOrPathOrCallbackType](remote-communication-overview.md#rcp_contentorpathorcallbacktype) [type](_rcp___content_or_path_or_callback.md#type) | 表示union中使用的数据类型。 |
| union {  [Rcp\_Buffer](_rcp___buffer.md) [content](_rcp___content_or_path_or_callback.md#content);  char [path](_rcp___content_or_path_or_callback.md#path) [[RCP\_MAX\_PATH\_LEN](remote-communication-overview.md#rcp_max_path_len)];  [Rcp\_GetDataCallback](remote-communication-overview.md#rcp_getdatacallback) [callback](_rcp___content_or_path_or_callback.md#callback);  } data | content: 文本数据。  path: 文件路径。  callback: 获取数据的回调函数。 |

## 结构体成员变量说明

### callback

```cpp
Rcp_GetDataCallback Rcp_ContentOrPathOrCallback::callback
```

**描述**

获取数据的回调。

### content

```cpp
Rcp_Buffer Rcp_ContentOrPathOrCallback::content
```

**描述**

文本数据。

### path

```cpp
char Rcp_ContentOrPathOrCallback::path[RCP_MAX_PATH_LEN]
```

**描述**

文件路径。

### type

```cpp
Rcp_ContentOrPathOrCallbackType Rcp_ContentOrPathOrCallback::type
```

**描述**

union中使用的数据类型。
