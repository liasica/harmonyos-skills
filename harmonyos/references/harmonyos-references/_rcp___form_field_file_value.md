---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___form_field_file_value
title: Rcp_FormFieldFileValue
breadcrumb: API参考 > 系统 > 网络 > Remote Communication Kit（远场通信服务） > C API > 结构体 > Rcp_FormFieldFileValue
category: harmonyos-references
scraped_at: 2026-09-02T15:01:58+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:665061c09073b5edf64660ef070fae2d5079b655a33ee6ea6b446477f722b71b
---

## 概述

表单字段文件值。

**起始版本：** 5.0.0(12)

**相关模块：** [RemoteCommunication](remote-communication-overview.md)

**所在头文件：** [rcp.h](rcp_8h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| char [contentType](_rcp___form_field_file_value.md#contenttype) [[RCP\_MAX\_CONTENT\_TYPE\_LEN](remote-communication-overview.md#rcp_max_content_type_len)] | 多部分表单数据内容类型。 |
| char [remoteFileName](_rcp___form_field_file_value.md#remotefilename) [[RCP\_MAX\_FILENAME\_LEN](remote-communication-overview.md#rcp_max_filename_len)] | 多部分表单数据远程文件名。 |
| [Rcp\_ContentOrPathOrCallback](_rcp___content_or_path_or_callback.md) [contentOrPathOrCb](_rcp___form_field_file_value.md#contentorpathorcb) | 多部分表单数据内容。 |

## 结构体成员变量说明

### contentOrPathOrCb

```cpp
Rcp_ContentOrPathOrCallback Rcp_FormFieldFileValue::contentOrPathOrCb
```

**描述**

多部分表单数据内容。

### contentType

```cpp
char Rcp_FormFieldFileValue::contentType[RCP_MAX_CONTENT_TYPE_LEN]
```

**描述**

多部分表单数据内容类型。

### remoteFileName

```cpp
char Rcp_FormFieldFileValue::remoteFileName[RCP_MAX_FILENAME_LEN]
```

**描述**

多部分表单数据远程文件名。
