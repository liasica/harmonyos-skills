---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___form_field_value
title: Rcp_FormFieldValue
breadcrumb: API参考 > 系统 > 网络 > Remote Communication Kit（远场通信服务） > C API > 结构体 > Rcp_FormFieldValue
category: harmonyos-references
scraped_at: 2026-04-28T08:09:03+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:51838b31d395ad9df6dcc290ca05ad41a5e3097e86015c04463bb5ca1702afbf
---

## 概述

PhonePC/2in1TabletTVWearable

简单表单数据字段值，参见[Rcp\_Form](remote-communication-overview.md#rcp_form)和[Rcp\_MultipartFormFieldValue](_rcp___multipart_form_field_value.md)。

**起始版本：** 5.0.0(12)

**相关模块：** [RemoteCommunication](remote-communication-overview.md)

**所在头文件：** [rcp.h](rcp_8h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [Rcp\_FormValueType](remote-communication-overview.md#rcp_formvaluetype)[type](_rcp___form_field_value.md#type) | 表示union中使用的数据类型。 |
| union {  uint8\_t [varBool](_rcp___form_field_value.md#varbool)  int32\_t [varInt32](_rcp___form_field_value.md#varint32)  int64\_t [varInt64](_rcp___form_field_value.md#varint64)  double [varDouble](_rcp___form_field_value.md#vardouble)  [Rcp\_Buffer](_rcp___buffer.md) [varStr](_rcp___form_field_value.md#varstr)  } | bool类型。  int32类型。  int64类型。  double类型。  string类型。 |
| struct [Rcp\_FormFieldValue](_rcp___form_field_value.md) \* [next](_rcp___form_field_value.md#next) | 指向下一个[Rcp\_FormFieldValue](_rcp___form_field_value.md)。链式存储。 |

## 结构体成员变量说明

PhonePC/2in1TabletTVWearable

### next

PhonePC/2in1TabletTVWearable

```
1. struct Rcp_FormFieldValue* Rcp_FormFieldValue::next
```

**描述**

指向下一个[Rcp\_FormFieldValue](_rcp___form_field_value.md)。链式存储。

### type

PhonePC/2in1TabletTVWearable

```
1. Rcp_FormValueType Rcp_FormFieldValue::type
```

**描述**

表示union中使用的数据类型。

### varBool

PhonePC/2in1TabletTVWearable

```
1. uint8_t Rcp_FormFieldValue::varBool
```

**描述**

bool类型。

### varDouble

PhonePC/2in1TabletTVWearable

```
1. double Rcp_FormFieldValue::varDouble
```

**描述**

double类型。

### varInt32

PhonePC/2in1TabletTVWearable

```
1. int32_t Rcp_FormFieldValue::varInt32
```

**描述**

int32类型。

### varInt64

PhonePC/2in1TabletTVWearable

```
1. int64_t Rcp_FormFieldValue::varInt64
```

**描述**

int64类型。

### varStr

PhonePC/2in1TabletTVWearable

```
1. Rcp_Buffer Rcp_FormFieldValue::varStr
```

**描述**

string类型。
