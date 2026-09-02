---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___multipart_form_field_value
title: Rcp_MultipartFormFieldValue
breadcrumb: API参考 > 系统 > 网络 > Remote Communication Kit（远场通信服务） > C API > 结构体 > Rcp_MultipartFormFieldValue
category: harmonyos-references
scraped_at: 2026-09-02T15:01:59+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:8097151c4299e63b7336be14d460c010f953800840351cea5bade77713161414
---

## 概述

多部分表单域值，在[Rcp\_MultipartForm](remote-communication-overview.md#rcp_multipartform)中使用。

**起始版本：** 5.0.0(12)

**相关模块：** [RemoteCommunication](remote-communication-overview.md)

**所在头文件：** [rcp.h](rcp_8h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| [Rcp\_MultipartValueType](remote-communication-overview.md#rcp_multipartvaluetype) [type](_rcp___multipart_form_field_value.md#type) | 表示union中使用的数据类型。 |
| union {  [Rcp\_FormFieldValue](_rcp___form_field_value.md) [formValue](_rcp___multipart_form_field_value.md#formvalue);  [Rcp\_FormFieldFileValue](_rcp___form_field_file_value.md) [formFileValue](_rcp___multipart_form_field_value.md#formfilevalue);  } data | formValue：简单表单数据字段值。  formFileValue：简单表单数据字段文件值。 |
| struct [Rcp\_MultipartFormFieldValue](_rcp___multipart_form_field_value.md) \* [next](_rcp___multipart_form_field_value.md#next) | 指向下一个[Rcp\_MultipartFormFieldValue](_rcp___multipart_form_field_value.md)。链式存储。 |

## 结构体成员变量说明

### formFileValue

```cpp
Rcp_FormFieldFileValue Rcp_MultipartFormFieldValue::formFileValue
```

**描述**

简单表单数据字段文件值。

### formValue

```cpp
Rcp_FormFieldValue Rcp_MultipartFormFieldValue::formValue
```

**描述**

简单表单数据字段值。

### next

```cpp
struct Rcp_MultipartFormFieldValue* Rcp_MultipartFormFieldValue::next
```

**描述**

指向下一个[Rcp\_MultipartFormFieldValue](_rcp___multipart_form_field_value.md)。链式存储。

### type

```cpp
Rcp_MultipartValueType Rcp_MultipartFormFieldValue::type
```

**描述**

表示union中使用的数据类型。
