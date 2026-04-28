---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___form_field_file_value
title: Rcp_FormFieldFileValue
breadcrumb: API参考 > 系统 > 网络 > Remote Communication Kit（远场通信服务） > C API > 结构体 > Rcp_FormFieldFileValue
category: harmonyos-references
scraped_at: 2026-04-28T08:09:03+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:70ee87e53c2e88291c2cb0d0c77dc2be014149641b42575e15d7db40cbaf8771
---

## 概述

PhonePC/2in1TabletTVWearable

表单字段文件值。

**起始版本：** 5.0.0(12)

**相关模块：** [RemoteCommunication](remote-communication-overview.md)

**所在头文件：** [rcp.h](rcp_8h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| char [contentType](_rcp___form_field_file_value.md#contenttype) [[RCP\_MAX\_CONTENT\_TYPE\_LEN](remote-communication-overview.md#rcp_max_content_type_len)] | 多部分表单数据内容类型。 |
| char [remoteFileName](_rcp___form_field_file_value.md#remotefilename) [[RCP\_MAX\_FILENAME\_LEN](remote-communication-overview.md#rcp_max_filename_len)] | 多部分表单数据远程文件名。 |
| [Rcp\_ContentOrPathOrCallback](_rcp___content_or_path_or_callback.md)[contentOrPathOrCb](_rcp___form_field_file_value.md#contentorpathorcb) | 多部分表单数据内容。 |

## 结构体成员变量说明

PhonePC/2in1TabletTVWearable

### contentOrPathOrCb

PhonePC/2in1TabletTVWearable

```
1. Rcp_ContentOrPathOrCallback Rcp_FormFieldFileValue::contentOrPathOrCb
```

**描述**

多部分表单数据内容。

### contentType

PhonePC/2in1TabletTVWearable

```
1. char Rcp_FormFieldFileValue::contentType[RCP_MAX_CONTENT_TYPE_LEN]
```

**描述**

多部分表单数据内容类型。

### remoteFileName

PhonePC/2in1TabletTVWearable

```
1. char Rcp_FormFieldFileValue::remoteFileName[RCP_MAX_FILENAME_LEN]
```

**描述**

多部分表单数据远程文件名。
