---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___form_field_value
title: Rcp_FormFieldValue
breadcrumb: API参考 > 系统 > 网络 > Remote Communication Kit（远场通信服务） > C API > 结构体 > Rcp_FormFieldValue
category: harmonyos-references
scraped_at: 2026-09-02T15:01:58+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:2d952e008c68046d0830947947c43838373d4fd086660ecfaf00bad6fd6b13be
---

## 概述

简单表单数据字段值，参见[Rcp\_Form](remote-communication-overview.md#rcp_form)和[Rcp\_MultipartFormFieldValue](_rcp___multipart_form_field_value.md)。

**起始版本：** 5.0.0(12)

**相关模块：** [RemoteCommunication](remote-communication-overview.md)

**所在头文件：** [rcp.h](rcp_8h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| [Rcp\_FormValueType](remote-communication-overview.md#rcp_formvaluetype) [type](_rcp___form_field_value.md#type) | 表示union中使用的数据类型。 |
| union {  uint8\_t [varBool](_rcp___form_field_value.md#varbool);  int32\_t [varInt32](_rcp___form_field_value.md#varint32);  int64\_t [varInt64](_rcp___form_field_value.md#varint64);  double [varDouble](_rcp___form_field_value.md#vardouble);  [Rcp\_Buffer](_rcp___buffer.md) [varStr](_rcp___form_field_value.md#varstr);  } data | bool类型。值为0表示false，值大于0表示true。  int32类型。  int64类型。  double类型。  string类型。 |
| struct [Rcp\_FormFieldValue](_rcp___form_field_value.md) \* [next](_rcp___form_field_value.md#next) | 指向下一个[Rcp\_FormFieldValue](_rcp___form_field_value.md)。链式存储。 |

## 结构体成员变量说明

### next

```cpp
struct Rcp_FormFieldValue* Rcp_FormFieldValue::next
```

**描述**

指向下一个[Rcp\_FormFieldValue](_rcp___form_field_value.md)。链式存储。

### type

```cpp
Rcp_FormValueType Rcp_FormFieldValue::type
```

**描述**

表示union中使用的数据类型。

### varBool

```cpp
uint8_t Rcp_FormFieldValue::varBool
```

**描述**

bool类型。值为0表示false，值大于0表示true。

### varDouble

```cpp
double Rcp_FormFieldValue::varDouble
```

**描述**

double类型。

### varInt32

```cpp
int32_t Rcp_FormFieldValue::varInt32
```

**描述**

int32类型。

### varInt64

```cpp
int64_t Rcp_FormFieldValue::varInt64
```

**描述**

int64类型。

### varStr

```cpp
Rcp_Buffer Rcp_FormFieldValue::varStr
```

**描述**

string类型。
