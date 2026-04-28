---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-data-type-h
title: data_type.h
breadcrumb: API参考 > AI > MindSpore Lite Kit（昇思推理框架服务） > C API > 头文件 > data_type.h
category: harmonyos-references
scraped_at: 2026-04-28T08:19:02+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:e8b22563a2a2ade64362437e9ae595d56604cc3a8a984eb79c19ae597a1f95d8
---

## 概述

PhonePC/2in1TabletTVWearable

声明了张量的数据的类型。

**引用文件：** <mindspore/data\_type.h>

**库：** libmindspore\_lite\_ndk.so

**系统能力：** SystemCapability.Ai.MindSpore

**起始版本：** 9

**相关模块：** [MindSpore](capi-mindspore.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 枚举

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [OH\_AI\_DataType](capi-data-type-h.md#oh_ai_datatype) | OH\_AI\_DataType | MSTensor保存的数据支持的类型。 |

## 枚举类型说明

PhonePC/2in1TabletTVWearable

### OH\_AI\_DataType

PhonePC/2in1TabletTVWearable

```
1. enum OH_AI_DataType
```

**描述**

MSTensor保存的数据支持的类型。

**起始版本：** 9

| 枚举项 | 描述 |
| --- | --- |
| OH\_AI\_DATATYPE\_UNKNOWN = 0 | 未知的数据类型。 |
| OH\_AI\_DATATYPE\_OBJECTTYPE\_STRING = 12 | String数据类型。 |
| OH\_AI\_DATATYPE\_OBJECTTYPE\_LIST = 13 | List数据类型。 |
| OH\_AI\_DATATYPE\_OBJECTTYPE\_TUPLE = 14 | Tuple数据类型。 |
| OH\_AI\_DATATYPE\_OBJECTTYPE\_TENSOR = 17 | TensorList数据类型。 |
| OH\_AI\_DATATYPE\_NUMBERTYPE\_BEGIN = 29 | Number类型的起始。 |
| OH\_AI\_DATATYPE\_NUMBERTYPE\_BOOL = 30 | Bool数据类型。 |
| OH\_AI\_DATATYPE\_NUMBERTYPE\_INT8 = 32 | Int8数据类型。 |
| OH\_AI\_DATATYPE\_NUMBERTYPE\_INT16 = 33 | Int16数据类型。 |
| OH\_AI\_DATATYPE\_NUMBERTYPE\_INT32 = 34 | Int32数据类型。 |
| OH\_AI\_DATATYPE\_NUMBERTYPE\_INT64 = 35 | Int64数据类型。 |
| OH\_AI\_DATATYPE\_NUMBERTYPE\_UINT8 = 37 | UInt8数据类型。 |
| OH\_AI\_DATATYPE\_NUMBERTYPE\_UINT16 = 38 | UInt16数据类型。 |
| OH\_AI\_DATATYPE\_NUMBERTYPE\_UINT32 = 39 | UInt32数据类型。 |
| OH\_AI\_DATATYPE\_NUMBERTYPE\_UINT64 = 40 | UInt64数据类型。 |
| OH\_AI\_DATATYPE\_NUMBERTYPE\_FLOAT16 = 42 | Float16数据类型。 |
| OH\_AI\_DATATYPE\_NUMBERTYPE\_FLOAT32 = 43 | Float32数据类型。 |
| OH\_AI\_DATATYPE\_NUMBERTYPE\_FLOAT64 = 44 | Float64数据类型。 |
| OH\_AI\_DATATYPE\_NUMBERTYPE\_END = 46 | Number类型的结尾。 |
| OH\_AI\_DataTypeInvalid = INT32\_MAX | 无效的数据类型。 |
