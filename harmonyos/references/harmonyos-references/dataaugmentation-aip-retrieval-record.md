---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/dataaugmentation-aip-retrieval-record
title: aip_retrieval_record.h
breadcrumb: API参考 > 应用框架 > Data Augmentation Kit（数据增强服务） > C API > 头文件 > aip_retrieval_record.h
category: harmonyos-references
scraped_at: 2026-09-02T15:01:33+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:a4549584f7df79b41d8f214166428dc67240df65cc3194e078df973842039d49
---

## 概述

提供与检索结果相关的接口。

检索结果（OH\_Retrieval\_Record）是知识检索操作的返回数据，包含从知识库中检索到的字段和字段取值。检索结果由多个数据库bucket数组（OH\_Retrieval\_RecordItem）组成，每个bucket数组对应一条匹配的记录，其中包含该记录各字段的名称和值。

适用于需要从知识库中获取相关信息并进行展示的应用场景，例如：知识问答系统中获取检索结果、智能推荐中提取匹配记录等。

**引用文件：** #include "dataaugmentation/retrieval/aip\_retrieval\_record.h"

**库：** libretrieval\_ndk.so

**系统能力：** SystemCapability.DataAugmentation.Retrieval

**起始版本：** 6.0.0(20)

**相关模块：** [Retrieval](dataaugmentation-capi-retrieval.md)

## 汇总

### 类型定义

| 名称 | 描述 |
| --- | --- |
| typedef struct [OH\_Retrieval\_Record](dataaugmentation-capi-retrieval.md#oh_retrieval_record) [OH\_Retrieval\_Record](dataaugmentation-capi-retrieval.md#oh_retrieval_record) | 定义检索结果，包含检索知识库得到的字段和字段取值。 |
| typedef struct [OH\_Retrieval\_RecordItem](dataaugmentation-capi-retrieval.md#oh_retrieval_recorditem) [OH\_Retrieval\_RecordItem](dataaugmentation-capi-retrieval.md#oh_retrieval_recorditem) | 定义检索结果中的数据库bucket数组。 |

### 函数

| 名称 | 描述 |
| --- | --- |
| int [OH\_Retrieval\_DestroyRecord](dataaugmentation-capi-retrieval.md#oh_retrieval_destroyrecord) ([OH\_Retrieval\_Record](dataaugmentation-capi-retrieval.md#oh_retrieval_record) \*record) | 销毁通过检索接口[OH\_Retrieval\_Retrieve](dataaugmentation-capi-retrieval.md#oh_retrieval_retrieve)获得的检索结果。 |
| int [OH\_Retrieval\_GetRecordLength](dataaugmentation-capi-retrieval.md#oh_retrieval_getrecordlength) (const [OH\_Retrieval\_Record](dataaugmentation-capi-retrieval.md#oh_retrieval_record) \*record, uint32\_t \*length) | 获取检索结果[OH\_Retrieval\_Record](dataaugmentation-capi-retrieval.md#oh_retrieval_record)中的数据库bucket数组长度。 |
| int [OH\_Retrieval\_GetRecordItem](dataaugmentation-capi-retrieval.md#oh_retrieval_getrecorditem) (const [OH\_Retrieval\_Record](dataaugmentation-capi-retrieval.md#oh_retrieval_record) \*record, uint32\_t index, const [OH\_Retrieval\_RecordItem](dataaugmentation-capi-retrieval.md#oh_retrieval_recorditem) \*\*item) | 获取检索结果[OH\_Retrieval\_Record](dataaugmentation-capi-retrieval.md#oh_retrieval_record)中的数据库bucket数组。 |
| int [OH\_Retrieval\_GetItemSize](dataaugmentation-capi-retrieval.md#oh_retrieval_getitemsize) (const [OH\_Retrieval\_RecordItem](dataaugmentation-capi-retrieval.md#oh_retrieval_recorditem) \*items, const char \*fieldName, size\_t \*size) | 获取数据库bucket数组[OH\_Retrieval\_RecordItem](dataaugmentation-capi-retrieval.md#oh_retrieval_recorditem)中指定字段的值的size。size值包含结束符。 |
| int [OH\_Retrieval\_GetItemText](dataaugmentation-capi-retrieval.md#oh_retrieval_getitemtext) (const [OH\_Retrieval\_RecordItem](dataaugmentation-capi-retrieval.md#oh_retrieval_recorditem) \*items, const char \*fieldName, char \*value, size\_t size) | 获取数据库bucket数组[OH\_Retrieval\_RecordItem](dataaugmentation-capi-retrieval.md#oh_retrieval_recorditem)中指定字段的值。 |
