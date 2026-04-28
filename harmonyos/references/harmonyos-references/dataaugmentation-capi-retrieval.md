---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/dataaugmentation-capi-retrieval
title: Retrieval
breadcrumb: API参考 > 应用框架 > Data Augmentation Kit（数据增强服务） > C API > 模块 > Retrieval
category: harmonyos-references
scraped_at: 2026-04-28T08:05:58+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:7e2b0d283b71f9ad7b2c011b600fcbb710d40f88f3f167d9163119d72307789e
---

## 概述

PhonePC/2in1Tablet

智慧化数据平台（AIP）为应用提供构建端侧智慧化解决方案，提供向量化、知识检索和知识问答的能力。

**起始版本：** 6.0.0(20)

## 汇总

PhonePC/2in1Tablet

### 文件

PhonePC/2in1Tablet

| 名称 | 描述 |
| --- | --- |
| [aip\_retrieval.h](dataaugmentation-aip-retrieval.md) | 提供知识检索相关的接口。 |
| [aip\_retrieval\_condition.h](dataaugmentation-aip-retrieval-condition.md) | 提供与检索条件相关的接口。 |
| [aip\_retrieval\_condition\_vector.h](dataaugmentation-aip-retrieval-condition-vector.md) | 提供与向量条件相关的接口。 |
| [aip\_retrieval\_query.h](dataaugmentation-aip-retrieval-query.md) | 提供与检索查询相关的接口。 |
| [aip\_retrieval\_record.h](dataaugmentation-aip-retrieval-record.md) | 提供与检索结果相关的接口。 |

### 类型定义

PhonePC/2in1Tablet

| 名称 | 描述 |
| --- | --- |
| typedef struct [OH\_Retrieval\_Retriever](dataaugmentation-capi-retrieval.md#oh_retrieval_retriever) [OH\_Retrieval\_Retriever](dataaugmentation-capi-retrieval.md#oh_retrieval_retriever) | 定义检索器类型，检索器是进行检索的句柄。 |
| typedef struct [OH\_Retrieval\_Config](dataaugmentation-capi-retrieval.md#oh_retrieval_config) [OH\_Retrieval\_Config](dataaugmentation-capi-retrieval.md#oh_retrieval_config) | 定义检索器配置。 |
| typedef struct [OH\_Retrieval\_DbConfig](dataaugmentation-capi-retrieval.md#oh_retrieval_dbconfig) [OH\_Retrieval\_DbConfig](dataaugmentation-capi-retrieval.md#oh_retrieval_dbconfig) | 定义一个用于打开数据库存储的数据库配置。 |
| typedef enum [Retrieval\_Channel\_Type](dataaugmentation-capi-retrieval.md#retrieval_channel_type) [Retrieval\_Channel\_Type](dataaugmentation-capi-retrieval.md#retrieval_channel_type) | 定义数据索引类型，目前仅包括向量索引数据。 |
| typedef void(\* [OH\_Retrieval\_Callback](dataaugmentation-capi-retrieval.md#oh_retrieval_callback)) (void \*context, [OH\_Retrieval\_Record](dataaugmentation-capi-retrieval.md#oh_retrieval_record) \*record, int errCode) | 检索结果记录的回调函数。 |
| typedef struct [OH\_Retrieval\_Condition](dataaugmentation-capi-retrieval.md#oh_retrieval_condition) [OH\_Retrieval\_Condition](dataaugmentation-capi-retrieval.md#oh_retrieval_condition) | 定义检索条件，可包含多个子检索条件等。 |
| typedef struct [OH\_Retrieval\_SubCondition](dataaugmentation-capi-retrieval.md#oh_retrieval_subcondition) [OH\_Retrieval\_SubCondition](dataaugmentation-capi-retrieval.md#oh_retrieval_subcondition) | 定义子检索条件，可以是向量检索。 |
| typedef struct [OH\_Retrieval\_SubCondition](dataaugmentation-capi-retrieval.md#oh_retrieval_subcondition) [OH\_Retrieval\_VectorCondition](dataaugmentation-capi-retrieval.md#oh_retrieval_vectorcondition) | 定义向量检索条件，包含检索的字段、检索参数、过滤条件等。 |
| typedef struct [OH\_Retrieval\_Query](dataaugmentation-capi-retrieval.md#oh_retrieval_query) [OH\_Retrieval\_Query](dataaugmentation-capi-retrieval.md#oh_retrieval_query) | 定义检索词，当前只支持纯文本检索。 |
| typedef struct [OH\_Retrieval\_Record](dataaugmentation-capi-retrieval.md#oh_retrieval_record) [OH\_Retrieval\_Record](dataaugmentation-capi-retrieval.md#oh_retrieval_record) | 定义检索结果，包含检索知识库得到的字段和字段取值。 |
| typedef struct [OH\_Retrieval\_RecordItem](dataaugmentation-capi-retrieval.md#oh_retrieval_recorditem) [OH\_Retrieval\_RecordItem](dataaugmentation-capi-retrieval.md#oh_retrieval_recorditem) | 定义检索结果中的数据库bucket数组。 |

### 枚举

PhonePC/2in1Tablet

| 名称 | 描述 |
| --- | --- |
| [Retrieval\_Channel\_Type](dataaugmentation-capi-retrieval.md#retrieval_channel_type) { Retrieval\_TYPE\_VECTOR = 1 } | 定义数据索引类型，目前仅包括向量索引数据。 |

### 函数

PhonePC/2in1Tablet

| 名称 | 描述 |
| --- | --- |
| int [OH\_Retrieval\_CreateRetriever](dataaugmentation-capi-retrieval.md#oh_retrieval_createretriever) (const [OH\_Retrieval\_Config](dataaugmentation-capi-retrieval.md#oh_retrieval_config) \*config, [OH\_Retrieval\_Retriever](dataaugmentation-capi-retrieval.md#oh_retrieval_retriever) \*\*retriever) | 获取检索器。 |
| int [OH\_Retrieval\_DestroyRetriever](dataaugmentation-capi-retrieval.md#oh_retrieval_destroyretriever) ([OH\_Retrieval\_Retriever](dataaugmentation-capi-retrieval.md#oh_retrieval_retriever) \*retriever) | 销毁通过[OH\_Retrieval\_CreateRetriever](dataaugmentation-capi-retrieval.md#oh_retrieval_createretriever)获得的检索器。 |
| [OH\_Retrieval\_Config](dataaugmentation-capi-retrieval.md#oh_retrieval_config) \* [OH\_Retrieval\_CreateConfig](dataaugmentation-capi-retrieval.md#oh_retrieval_createconfig) () | 获取检索器配置。 |
| int [OH\_Retrieval\_DestroyConfig](dataaugmentation-capi-retrieval.md#oh_retrieval_destroyconfig) ([OH\_Retrieval\_Config](dataaugmentation-capi-retrieval.md#oh_retrieval_config) \*config) | 销毁通过[OH\_Retrieval\_CreateConfig](dataaugmentation-capi-retrieval.md#oh_retrieval_createconfig)获得的检索配置。 |
| [OH\_Retrieval\_DbConfig](dataaugmentation-capi-retrieval.md#oh_retrieval_dbconfig) \* [OH\_Retrieval\_CreateDbConfig](dataaugmentation-capi-retrieval.md#oh_retrieval_createdbconfig) () | 创建一个配置项以打开数据库。 |
| int [OH\_Retrieval\_DestroyDbConfig](dataaugmentation-capi-retrieval.md#oh_retrieval_destroydbconfig) ([OH\_Retrieval\_DbConfig](dataaugmentation-capi-retrieval.md#oh_retrieval_dbconfig) \*dbConfig) | 销毁[OH\_Retrieval\_CreateDbConfig](dataaugmentation-capi-retrieval.md#oh_retrieval_createdbconfig)创建的[OH\_Retrieval\_DbConfig](dataaugmentation-capi-retrieval.md#oh_retrieval_dbconfig)。 |
| int [OH\_Retrieval\_SetDbConfig](dataaugmentation-capi-retrieval.md#oh_retrieval_setdbconfig) ([OH\_Retrieval\_DbConfig](dataaugmentation-capi-retrieval.md#oh_retrieval_dbconfig) \*dbConfig, [OH\_Rdb\_ConfigV2](capi-rdb-oh-rdb-configv2.md)\*rdbConfig) | 设置[OH\_Retrieval\_DbConfig](dataaugmentation-capi-retrieval.md#oh_retrieval_dbconfig)中的数据库配置。 |
| int [OH\_Retrieval\_AddConfig](dataaugmentation-capi-retrieval.md#oh_retrieval_addconfig) ([OH\_Retrieval\_Config](dataaugmentation-capi-retrieval.md#oh_retrieval_config) \*config, [Retrieval\_Channel\_Type](dataaugmentation-capi-retrieval.md#retrieval_channel_type) channelType, [OH\_Retrieval\_DbConfig](dataaugmentation-capi-retrieval.md#oh_retrieval_dbconfig) \*dbConfig) | 设置[OH\_Retrieval\_Config](dataaugmentation-capi-retrieval.md#oh_retrieval_config)中的数据库配置。 |
| int [OH\_Retrieval\_Retrieve](dataaugmentation-capi-retrieval.md#oh_retrieval_retrieve) (const [OH\_Retrieval\_Retriever](dataaugmentation-capi-retrieval.md#oh_retrieval_retriever) \*retriever, const [OH\_Retrieval\_Query](dataaugmentation-capi-retrieval.md#oh_retrieval_query) \*query, const [OH\_Retrieval\_Condition](dataaugmentation-capi-retrieval.md#oh_retrieval_condition) \*condition, void \*context, const [OH\_Retrieval\_Callback](dataaugmentation-capi-retrieval.md#oh_retrieval_callback) \*callback) | 执行检索。获得检索器句柄后，输入检索查询词，根据检索条件执行检索，得到检索结果。 |
| [OH\_Retrieval\_Condition](dataaugmentation-capi-retrieval.md#oh_retrieval_condition) \* [OH\_Retrieval\_CreateCondition](dataaugmentation-capi-retrieval.md#oh_retrieval_createcondition) () | 创建检索条件，作为检索接口的入参。 |
| int [OH\_Retrieval\_DestroyCondition](dataaugmentation-capi-retrieval.md#oh_retrieval_destroycondition) ([OH\_Retrieval\_Condition](dataaugmentation-capi-retrieval.md#oh_retrieval_condition) \*condition) | 销毁通过[OH\_Retrieval\_CreateCondition](dataaugmentation-capi-retrieval.md#oh_retrieval_createcondition)获得的检索条件。 |
| int [OH\_Retrieval\_DestroySubCondition](dataaugmentation-capi-retrieval.md#oh_retrieval_destroysubcondition) ([OH\_Retrieval\_SubCondition](dataaugmentation-capi-retrieval.md#oh_retrieval_subcondition) \*condition) | 销毁[OH\_Retrieval\_SubCondition](dataaugmentation-capi-retrieval.md#oh_retrieval_subcondition)对象。 |
| int [OH\_Retrieval\_AddSubCondition](dataaugmentation-capi-retrieval.md#oh_retrieval_addsubcondition) ([OH\_Retrieval\_Condition](dataaugmentation-capi-retrieval.md#oh_retrieval_condition) \*condition, [OH\_Retrieval\_SubCondition](dataaugmentation-capi-retrieval.md#oh_retrieval_subcondition) \*subCondition) | 在检索条件中，增加子检索条件。 |
| [OH\_Retrieval\_VectorCondition](dataaugmentation-capi-retrieval.md#oh_retrieval_vectorcondition) \* [OH\_Retrieval\_CreateVectorCondition](dataaugmentation-capi-retrieval.md#oh_retrieval_createvectorcondition) () | 创建向量检索条件。 |
| int [OH\_Retrieval\_DestroyVectorCondition](dataaugmentation-capi-retrieval.md#oh_retrieval_destroyvectorcondition) ([OH\_Retrieval\_VectorCondition](dataaugmentation-capi-retrieval.md#oh_retrieval_vectorcondition) \*condition) | 销毁通过[OH\_Retrieval\_CreateVectorCondition](dataaugmentation-capi-retrieval.md#oh_retrieval_createvectorcondition)获得的检索条件。 |
| int [OH\_Retrieval\_SetVectorRecallLimit](dataaugmentation-capi-retrieval.md#oh_retrieval_setvectorrecalllimit) ([OH\_Retrieval\_VectorCondition](dataaugmentation-capi-retrieval.md#oh_retrieval_vectorcondition) \*condition, uint32\_t limit) | 在检索条件中，设置向量检索结果数量上限1000。 |
| int [OH\_Retrieval\_SetSimilarityThreshold](dataaugmentation-capi-retrieval.md#oh_retrieval_setsimilaritythreshold) ([OH\_Retrieval\_VectorCondition](dataaugmentation-capi-retrieval.md#oh_retrieval_vectorcondition) \*condition, double threshold) | 在检索条件中，设置向量检索的相似度阈值。 |
| [OH\_Retrieval\_Query](dataaugmentation-capi-retrieval.md#oh_retrieval_query) \* [OH\_Retrieval\_CreateQuery](dataaugmentation-capi-retrieval.md#oh_retrieval_createquery) () | 创建检索词，作为检索接口的入参。 |
| int [OH\_Retrieval\_DestroyQuery](dataaugmentation-capi-retrieval.md#oh_retrieval_destroyquery) ([OH\_Retrieval\_Query](dataaugmentation-capi-retrieval.md#oh_retrieval_query) \*query) | 销毁通过[OH\_Retrieval\_CreateQuery](dataaugmentation-capi-retrieval.md#oh_retrieval_createquery)获得的检索词。 |
| int [OH\_Retrieval\_SetOriginalQuestion](dataaugmentation-capi-retrieval.md#oh_retrieval_setoriginalquestion) ([OH\_Retrieval\_Query](dataaugmentation-capi-retrieval.md#oh_retrieval_query) \*query, const char \*question) | 设置[OH\_Retrieval\_Query](dataaugmentation-capi-retrieval.md#oh_retrieval_query)中的检索词。 |
| int [OH\_Retrieval\_DestroyRecord](dataaugmentation-capi-retrieval.md#oh_retrieval_destroyrecord) ([OH\_Retrieval\_Record](dataaugmentation-capi-retrieval.md#oh_retrieval_record) \*record) | 销毁通过检索接口[OH\_Retrieval\_Retrieve](dataaugmentation-capi-retrieval.md#oh_retrieval_retrieve)获得的检索结果。 |
| int [OH\_Retrieval\_GetRecordLength](dataaugmentation-capi-retrieval.md#oh_retrieval_getrecordlength) (const [OH\_Retrieval\_Record](dataaugmentation-capi-retrieval.md#oh_retrieval_record) \*record, uint32\_t \*length) | 获取检索结果[OH\_Retrieval\_Record](dataaugmentation-capi-retrieval.md#oh_retrieval_record)中的数据库bucket数组长度。 |
| int [OH\_Retrieval\_GetRecordItem](dataaugmentation-capi-retrieval.md#oh_retrieval_getrecorditem) (const [OH\_Retrieval\_Record](dataaugmentation-capi-retrieval.md#oh_retrieval_record) \*record, uint32\_t index, const [OH\_Retrieval\_RecordItem](dataaugmentation-capi-retrieval.md#oh_retrieval_recorditem) \*\*item) | 获取检索结果[OH\_Retrieval\_Record](dataaugmentation-capi-retrieval.md#oh_retrieval_record)中的数据库bucket数组。 |
| int [OH\_Retrieval\_GetItemSize](dataaugmentation-capi-retrieval.md#oh_retrieval_getitemsize) (const [OH\_Retrieval\_RecordItem](dataaugmentation-capi-retrieval.md#oh_retrieval_recorditem) \*items, const char \*fieldName, size\_t \*size) | 获取数据库bucket数组[OH\_Retrieval\_RecordItem](dataaugmentation-capi-retrieval.md#oh_retrieval_recorditem)中指定字段的值的size。size值包含结束符。 |
| int [OH\_Retrieval\_GetItemText](dataaugmentation-capi-retrieval.md#oh_retrieval_getitemtext) (const [OH\_Retrieval\_RecordItem](dataaugmentation-capi-retrieval.md#oh_retrieval_recorditem) \*items, const char \*fieldName, char \*value, size\_t size) | 获取数据库bucket数组[OH\_Retrieval\_RecordItem](dataaugmentation-capi-retrieval.md#oh_retrieval_recorditem)中指定字段的值。 |

## 类型定义说明

PhonePC/2in1Tablet

### OH\_Retrieval\_Callback

PhonePC/2in1Tablet

```
1. typedef void(* OH_Retrieval_Callback) (void *context, OH_Retrieval_Record *record, int errCode)
```

**描述**

检索结果记录的回调函数。

**起始版本：** 6.0.0(20)

**参数:**

| 名称 | 描述 |
| --- | --- |
| context | 表示用户提供的上下文数据。 |
| record | 表示指向 [OH\_Retrieval\_Record](dataaugmentation-capi-retrieval.md#oh_retrieval_record) 实例的指针。 |
| errCode | 表示返回的错误码。 |

### OH\_Retrieval\_Condition

PhonePC/2in1Tablet

```
1. typedef struct OH_Retrieval_Condition OH_Retrieval_Condition
```

**描述**

定义检索条件，可包含多个子检索条件。

**起始版本：** 6.0.0(20)

### OH\_Retrieval\_Config

PhonePC/2in1Tablet

```
1. typedef struct OH_Retrieval_Config OH_Retrieval_Config
```

**描述**

定义检索器配置，包括数据库路径、数据库名称、包名等。

**起始版本：** 6.0.0(20)

### OH\_Retrieval\_DbConfig

PhonePC/2in1Tablet

```
1. typedef struct OH_Retrieval_DbConfig OH_Retrieval_DbConfig
```

**描述**

定义一个用于打开数据库存储的数据库配置。

**起始版本：** 6.0.0(20)

### OH\_Retrieval\_Query

PhonePC/2in1Tablet

```
1. typedef struct OH_Retrieval_Query OH_Retrieval_Query
```

**描述**

定义检索词，当前只支持纯文本检索，不支持图片、视频等。

**起始版本：** 6.0.0(20)

### OH\_Retrieval\_Record

PhonePC/2in1Tablet

```
1. typedef struct OH_Retrieval_Record OH_Retrieval_Record
```

**描述**

定义检索结果，包含检索知识库得到的字段和字段取值。

**起始版本：** 6.0.0(20)

### OH\_Retrieval\_RecordItem

PhonePC/2in1Tablet

```
1. typedef struct OH_Retrieval_RecordItem OH_Retrieval_RecordItem
```

**描述**

定义检索结果中的数据库bucket数组。

**起始版本：** 6.0.0(20)

### OH\_Retrieval\_Retriever

PhonePC/2in1Tablet

```
1. typedef struct OH_Retrieval_Retriever OH_Retrieval_Retriever
```

**描述**

定义检索器类型，检索器是进行检索的句柄。

**起始版本：** 6.0.0(20)

### OH\_Retrieval\_SubCondition

PhonePC/2in1Tablet

```
1. typedef struct OH_Retrieval_SubCondition OH_Retrieval_SubCondition
```

**描述**

定义子检索条件，目前支持向量检索。

**起始版本：** 6.0.0(20)

### OH\_Retrieval\_VectorCondition

PhonePC/2in1Tablet

```
1. typedef struct OH_Retrieval_SubCondition OH_Retrieval_VectorCondition
```

**描述**

定义向量检索条件，包含检索的字段、检索参数、过滤条件等。

**起始版本：** 6.0.0(20)

### Retrieval\_Channel\_Type

PhonePC/2in1Tablet

```
1. typedef enum Retrieval_Channel_Type Retrieval_Channel_Type
```

**描述**

定义数据索引类型，目前仅包括向量索引数据。

**起始版本：** 6.0.0(20)

## 枚举类型说明

PhonePC/2in1Tablet

### Retrieval\_Channel\_Type

PhonePC/2in1Tablet

```
1. enum Retrieval_Channel_Type
```

**描述**

定义数据索引类型，目前仅包括向量索引数据。

**起始版本：** 6.0.0(20)

| 枚举值 | 描述 |
| --- | --- |
| Retrieval\_TYPE\_VECTOR | 表示向量索引。 |

## 函数说明

PhonePC/2in1Tablet

### OH\_Retrieval\_AddConfig()

PhonePC/2in1Tablet

```
1. int OH_Retrieval_AddConfig (OH_Retrieval_Config * config, Retrieval_Channel_Type channelType, OH_Retrieval_DbConfig * dbConfig )
```

**描述**

设置[OH\_Retrieval\_Config](dataaugmentation-capi-retrieval.md#oh_retrieval_config)中的数据库配置。

**起始版本：** 6.0.0(20)

**参数:**

| 名称 | 描述 |
| --- | --- |
| config | 指向检索配置 [OH\_Retrieval\_Config](dataaugmentation-capi-retrieval.md#oh_retrieval_config) 实例的指针。 |
| channelType | 表示一种数据索引类型，目前仅支持向量查询。 |
| dbConfig | 指向数据库配置实例的指针。 |

**返回：**

返回函数的执行状态。执行成功返回AIP\_OK。

| 错误码ID | 错误信息 |
| --- | --- |
| 0 | 操作成功 |
| 1021200010 | 无效参数 |

**参见：**

[OH\_Retrieval\_Config](dataaugmentation-capi-retrieval.md#oh_retrieval_config)、[Retrieval\_Channel\_Type](dataaugmentation-capi-retrieval.md#retrieval_channel_type)、[OH\_Retrieval\_DbConfig](dataaugmentation-capi-retrieval.md#oh_retrieval_dbconfig)、[OH\_Aip\_ErrCode](dataaugmentation-capi-aip.md#oh_aip_errcode-1)

### OH\_Retrieval\_AddSubCondition()

PhonePC/2in1Tablet

```
1. int OH_Retrieval_AddSubCondition (OH_Retrieval_Condition * condition, OH_Retrieval_SubCondition * subCondition )
```

**描述**

在检索条件中，增加子检索条件。当前仅支持增加一个子检索条件。

**起始版本：** 6.0.0(20)

**参数:**

| 名称 | 描述 |
| --- | --- |
| condition | 指向检索条件[OH\_Retrieval\_Condition](dataaugmentation-capi-retrieval.md#oh_retrieval_condition)实例的指针。 |
| subCondition | 指向子检索条件实例的指针，可以是向量检索条件[OH\_Retrieval\_VectorCondition](dataaugmentation-capi-retrieval.md#oh_retrieval_vectorcondition)。 |

**返回：**

返回函数的执行状态。执行成功返回AIP\_OK。

| 错误码ID | 错误信息 |
| --- | --- |
| 0 | 操作成功 |
| 1021200009 | 条件数量超过上限1 |
| 1021200010 | 无效参数 |

**参见：**

[OH\_Retrieval\_Condition](dataaugmentation-capi-retrieval.md#oh_retrieval_condition)、[OH\_Retrieval\_SubCondition](dataaugmentation-capi-retrieval.md#oh_retrieval_subcondition)、[OH\_Retrieval\_VectorCondition](dataaugmentation-capi-retrieval.md#oh_retrieval_vectorcondition)、[OH\_Aip\_ErrCode](dataaugmentation-capi-aip.md#oh_aip_errcode-1)

### OH\_Retrieval\_CreateCondition()

PhonePC/2in1Tablet

```
1. OH_Retrieval_Condition* OH_Retrieval_CreateCondition ()
```

**描述**

创建检索条件，作为检索接口的入参。

**起始版本：** 6.0.0(20)

**返回：**

函数执行成功时，返回指向检索条件[OH\_Retrieval\_Condition](dataaugmentation-capi-retrieval.md#oh_retrieval_condition)实例的指针。当函数执行失败时，该指针为空指针。

**参见：**

[OH\_Retrieval\_Condition](dataaugmentation-capi-retrieval.md#oh_retrieval_condition)

### OH\_Retrieval\_CreateConfig()

PhonePC/2in1Tablet

```
1. OH_Retrieval_Config* OH_Retrieval_CreateConfig ()
```

**描述**

获取检索器配置。用于初始化检索器。

**起始版本：** 6.0.0(20)

**返回：**

函数执行成功时，返回指向检索器配置[OH\_Retrieval\_Config](dataaugmentation-capi-retrieval.md#oh_retrieval_config)实例的指针。当函数执行失败时，该指针为空指针。

**参见：**

[OH\_Retrieval\_Config](dataaugmentation-capi-retrieval.md#oh_retrieval_config)、[OH\_Aip\_ErrCode](dataaugmentation-capi-aip.md#oh_aip_errcode-1)

### OH\_Retrieval\_CreateDbConfig()

PhonePC/2in1Tablet

```
1. OH_Retrieval_DbConfig* OH_Retrieval_CreateDbConfig ()
```

**描述**

创建一个数据库相关配置项。

**起始版本：** 6.0.0(20)

**返回：**

返回指向[OH\_Retrieval\_DbConfig](dataaugmentation-capi-retrieval.md#oh_retrieval_dbconfig)实例的指针。当函数执行失败时，该指针为空指针。

**参见：**

[OH\_Retrieval\_DbConfig](dataaugmentation-capi-retrieval.md#oh_retrieval_dbconfig)、[OH\_Aip\_ErrCode](dataaugmentation-capi-aip.md#oh_aip_errcode-1)

### OH\_Retrieval\_CreateQuery()

PhonePC/2in1Tablet

```
1. OH_Retrieval_Query* OH_Retrieval_CreateQuery ()
```

**描述**

创建检索词，作为检索接口的入参。

**起始版本：** 6.0.0(20)

**返回：**

函数执行成功时，返回指向[OH\_Retrieval\_Query](dataaugmentation-capi-retrieval.md#oh_retrieval_query)实例的指针。当函数执行失败时，该指针为空指针。

**参见：**

[OH\_Retrieval\_Query](dataaugmentation-capi-retrieval.md#oh_retrieval_query)

### OH\_Retrieval\_CreateRetriever()

PhonePC/2in1Tablet

```
1. int OH_Retrieval_CreateRetriever (const OH_Retrieval_Config * config, OH_Retrieval_Retriever ** retriever )
```

**描述**

读取检索配置，初始化检索器。

**起始版本：** 6.0.0(20)

**参数:**

| 名称 | 描述 |
| --- | --- |
| config | 创建检索器时，需要输入检索器的配置项[OH\_Retrieval\_Config](dataaugmentation-capi-retrieval.md#oh_retrieval_config)。 |
| retriever | 返回指向检索器[OH\_Retrieval\_Retriever](dataaugmentation-capi-retrieval.md#oh_retrieval_retriever)实例的指针。 |

**返回：**

返回函数的执行状态。执行成功返回AIP\_OK。

| 错误码ID | 错误信息 |
| --- | --- |
| 0 | 操作成功 |
| 1021200010 | 无效参数 |

**参见：**

[OH\_Retrieval\_Retriever](dataaugmentation-capi-retrieval.md#oh_retrieval_retriever)、[OH\_Retrieval\_Config](dataaugmentation-capi-retrieval.md#oh_retrieval_config)、[OH\_Aip\_ErrCode](dataaugmentation-capi-aip.md#oh_aip_errcode-1)

### OH\_Retrieval\_CreateVectorCondition()

PhonePC/2in1Tablet

```
1. OH_Retrieval_VectorCondition* OH_Retrieval_CreateVectorCondition ()
```

**描述**

创建向量检索条件。

**起始版本：** 6.0.0(20)

**返回：**

函数执行成功时，返回指向检索条件[OH\_Retrieval\_VectorCondition](dataaugmentation-capi-retrieval.md#oh_retrieval_vectorcondition)实例的指针。当函数执行失败时，该指针为空指针。

**参见：**

[OH\_Retrieval\_VectorCondition](dataaugmentation-capi-retrieval.md#oh_retrieval_vectorcondition)

### OH\_Retrieval\_DestroyCondition()

PhonePC/2in1Tablet

```
1. int OH_Retrieval_DestroyCondition (OH_Retrieval_Condition * condition)
```

**描述**

销毁通过[OH\_Retrieval\_CreateCondition](dataaugmentation-capi-retrieval.md#oh_retrieval_createcondition)获得的检索条件。

**起始版本：** 6.0.0(20)

**参数:**

| 名称 | 描述 |
| --- | --- |
| condition | 指向检索条件[OH\_Retrieval\_Condition](dataaugmentation-capi-retrieval.md#oh_retrieval_condition)的指针。 |

**返回：**

返回函数的执行状态。执行成功返回AIP\_OK。

| 错误码ID | 错误信息 |
| --- | --- |
| 0 | 操作成功 |
| 1021200010 | 无效参数 |

**参见：**

[OH\_Retrieval\_Condition](dataaugmentation-capi-retrieval.md#oh_retrieval_condition)、[OH\_Aip\_ErrCode](dataaugmentation-capi-aip.md#oh_aip_errcode-1)、[OH\_Retrieval\_CreateCondition](dataaugmentation-capi-retrieval.md#oh_retrieval_createcondition)

### OH\_Retrieval\_DestroyConfig()

PhonePC/2in1Tablet

```
1. int OH_Retrieval_DestroyConfig (OH_Retrieval_Config * config)
```

**描述**

销毁通过OH\_Retriever\_CreateConfig获得的检索配置。

**起始版本：** 6.0.0(20)

**参数:**

| 名称 | 描述 |
| --- | --- |
| config | 指向检索配置[OH\_Retrieval\_Config](dataaugmentation-capi-retrieval.md#oh_retrieval_config)的指针。 |

**返回：**

返回函数的执行状态。执行成功返回AIP\_OK。

| 错误码ID | 错误信息 |
| --- | --- |
| 0 | 操作成功 |
| 1021200010 | 无效参数 |

**参见：**

[OH\_Retrieval\_Config](dataaugmentation-capi-retrieval.md#oh_retrieval_config)、[OH\_Aip\_ErrCode](dataaugmentation-capi-aip.md#oh_aip_errcode-1)、[OH\_Retrieval\_CreateConfig](dataaugmentation-capi-retrieval.md#oh_retrieval_createconfig)

### OH\_Retrieval\_DestroyDbConfig()

PhonePC/2in1Tablet

```
1. int OH_Retrieval_DestroyDbConfig (OH_Retrieval_DbConfig * dbConfig)
```

**描述**

销毁[OH\_Retrieval\_CreateDbConfig](dataaugmentation-capi-retrieval.md#oh_retrieval_createdbconfig)创建的[OH\_Retrieval\_DbConfig](dataaugmentation-capi-retrieval.md#oh_retrieval_dbconfig)。

**起始版本：** 6.0.0(20)

**参数:**

| 名称 | 描述 |
| --- | --- |
| dbConfig | 表示指向[OH\_Retrieval\_DbConfig](dataaugmentation-capi-retrieval.md#oh_retrieval_dbconfig)实例的指针。 |

**返回：**

返回函数的执行状态。执行成功返回AIP\_OK。

| 错误码ID | 错误信息 |
| --- | --- |
| 0 | 操作成功 |
| 1021200010 | 无效参数 |

**参见：**

[OH\_Retrieval\_DbConfig](dataaugmentation-capi-retrieval.md#oh_retrieval_dbconfig)、[OH\_Aip\_ErrCode](dataaugmentation-capi-aip.md#oh_aip_errcode-1)、[OH\_Retrieval\_CreateDbConfig](dataaugmentation-capi-retrieval.md#oh_retrieval_createdbconfig)

### OH\_Retrieval\_DestroyQuery()

PhonePC/2in1Tablet

```
1. int OH_Retrieval_DestroyQuery (OH_Retrieval_Query * query)
```

**描述**

销毁通过[OH\_Retrieval\_CreateQuery](dataaugmentation-capi-retrieval.md#oh_retrieval_createquery)获得的检索词。

**起始版本：** 6.0.0(20)

**参数:**

| 名称 | 描述 |
| --- | --- |
| query | 指向检索词[OH\_Retrieval\_Query](dataaugmentation-capi-retrieval.md#oh_retrieval_query)的指针。 |

**返回：**

返回函数的执行状态。执行成功返回AIP\_OK。

| 错误码ID | 错误信息 |
| --- | --- |
| 0 | 操作成功 |
| 1021200010 | 无效参数 |

**参见：**

[OH\_Retrieval\_Query](dataaugmentation-capi-retrieval.md#oh_retrieval_query)、[OH\_Aip\_ErrCode](dataaugmentation-capi-aip.md#oh_aip_errcode-1)、[OH\_Retrieval\_CreateQuery](dataaugmentation-capi-retrieval.md#oh_retrieval_createquery)

### OH\_Retrieval\_DestroyRecord()

PhonePC/2in1Tablet

```
1. int OH_Retrieval_DestroyRecord (OH_Retrieval_Record * record)
```

**描述**

销毁通过检索接口[OH\_Retrieval\_Retrieve](dataaugmentation-capi-retrieval.md#oh_retrieval_retrieve)获得的检索结果。

**起始版本：** 6.0.0(20)

**参数:**

| 名称 | 描述 |
| --- | --- |
| record | 指向检索结果[OH\_Retrieval\_Record](dataaugmentation-capi-retrieval.md#oh_retrieval_record)的指针。 |

**返回：**

返回函数的执行状态。执行成功返回AIP\_OK。

| 错误码ID | 错误信息 |
| --- | --- |
| 0 | 操作成功 |
| 1021200010 | 无效参数 |

**参见：**

[OH\_Retrieval\_Record](dataaugmentation-capi-retrieval.md#oh_retrieval_record)、[OH\_Aip\_ErrCode](dataaugmentation-capi-aip.md#oh_aip_errcode-1)、[OH\_Retrieval\_Retrieve](dataaugmentation-capi-retrieval.md#oh_retrieval_retrieve)

### OH\_Retrieval\_DestroyRetriever()

PhonePC/2in1Tablet

```
1. int OH_Retrieval_DestroyRetriever (OH_Retrieval_Retriever * retriever)
```

**描述**

销毁通过[OH\_Retrieval\_CreateRetriever](dataaugmentation-capi-retrieval.md#oh_retrieval_createretriever)获得的检索器。

**起始版本：** 6.0.0(20)

**参数:**

| 名称 | 描述 |
| --- | --- |
| retriever | 指向检索器[OH\_Retrieval\_Retriever](dataaugmentation-capi-retrieval.md#oh_retrieval_retriever)的指针。 |

**返回：**

返回函数的执行状态。执行成功返回AIP\_OK。

| 错误码ID | 错误信息 |
| --- | --- |
| 0 | 操作成功 |
| 1021200010 | 无效参数 |

**参见：**

[OH\_Retrieval\_Retriever](dataaugmentation-capi-retrieval.md#oh_retrieval_retriever)、[OH\_Aip\_ErrCode](dataaugmentation-capi-aip.md#oh_aip_errcode-1)、[OH\_Retrieval\_CreateRetriever](dataaugmentation-capi-retrieval.md#oh_retrieval_createretriever)

### OH\_Retrieval\_DestroySubCondition()

PhonePC/2in1Tablet

```
1. int OH_Retrieval_DestroySubCondition (OH_Retrieval_SubCondition * condition)
```

**描述**

销毁通过[OH\_Retrieval\_SubCondition](dataaugmentation-capi-retrieval.md#oh_retrieval_subcondition)。

**起始版本：** 6.0.0(20)

**参数:**

| 名称 | 描述 |
| --- | --- |
| condition | 指向检索条件[OH\_Retrieval\_SubCondition](dataaugmentation-capi-retrieval.md#oh_retrieval_subcondition)的指针。 |

**返回：**

返回函数的执行状态。执行成功返回AIP\_OK。

| 错误码ID | 错误信息 |
| --- | --- |
| 0 | 操作成功 |
| 1021200010 | 无效参数 |

**参见：**

[OH\_Retrieval\_SubCondition](dataaugmentation-capi-retrieval.md#oh_retrieval_subcondition)、[OH\_Aip\_ErrCode](dataaugmentation-capi-aip.md#oh_aip_errcode-1)

### OH\_Retrieval\_DestroyVectorCondition()

PhonePC/2in1Tablet

```
1. int OH_Retrieval_DestroyVectorCondition (OH_Retrieval_VectorCondition * condition)
```

**描述**

销毁通过[OH\_Retrieval\_CreateVectorCondition](dataaugmentation-capi-retrieval.md#oh_retrieval_createvectorcondition)获得的检索条件。

**起始版本：** 6.0.0(20)

**参数:**

| 名称 | 描述 |
| --- | --- |
| condition | 指向向量检索条件[OH\_Retrieval\_VectorCondition](dataaugmentation-capi-retrieval.md#oh_retrieval_vectorcondition)的指针。 |

**返回：**

返回函数的执行状态。执行成功返回AIP\_OK。

| 错误码ID | 错误信息 |
| --- | --- |
| 0 | 操作成功 |
| 1021200010 | 无效参数 |

**参见：**

[OH\_Retrieval\_VectorCondition](dataaugmentation-capi-retrieval.md#oh_retrieval_vectorcondition)、[OH\_Aip\_ErrCode](dataaugmentation-capi-aip.md#oh_aip_errcode-1)、[OH\_Retrieval\_CreateVectorCondition](dataaugmentation-capi-retrieval.md#oh_retrieval_createvectorcondition)

### OH\_Retrieval\_GetItemSize()

PhonePC/2in1Tablet

```
1. int OH_Retrieval_GetItemSize (const OH_Retrieval_RecordItem * items, const char * fieldName, size_t * size )
```

**描述**

获取数据库bucket数组[OH\_Retrieval\_RecordItem](dataaugmentation-capi-retrieval.md#oh_retrieval_recorditem)中指定字段的值的size。size值包含结束符。

**起始版本：** 6.0.0(20)

**参数:**

| 名称 | 描述 |
| --- | --- |
| items | 指向数据库bucket数组[OH\_Retrieval\_RecordItem](dataaugmentation-capi-retrieval.md#oh_retrieval_recorditem)实例的指针。 |
| fieldName | 数据库bucket的字段名。 |
| size | 数据库bucket相应字段的值的大小。 |

**返回：**

返回函数的执行状态。执行成功返回AIP\_OK。

| 错误码ID | 错误信息 |
| --- | --- |
| 0 | 操作成功 |
| 1021200007 | 不存在该字段 |
| 1021200010 | 无效参数 |

**参见：**

[OH\_Retrieval\_RecordItem](dataaugmentation-capi-retrieval.md#oh_retrieval_recorditem)、[OH\_Aip\_ErrCode](dataaugmentation-capi-aip.md#oh_aip_errcode-1)

### OH\_Retrieval\_GetItemText()

PhonePC/2in1Tablet

```
1. int OH_Retrieval_GetItemText (const OH_Retrieval_RecordItem * items, const char * fieldName, char * value, size_t size )
```

**描述**

获取数据库bucket数组[OH\_Retrieval\_RecordItem](dataaugmentation-capi-retrieval.md#oh_retrieval_recorditem)中指定字段的值。

**起始版本：** 6.0.0(20)

**参数:**

| 名称 | 描述 |
| --- | --- |
| items | 指向数据库bucket数组[OH\_Retrieval\_RecordItem](dataaugmentation-capi-retrieval.md#oh_retrieval_recorditem)实例的指针。 |
| fieldName | 数据库bucket的字段名。 |
| value | 数据库bucket相应字段的值。 |
| size | 数据库bucket相应字段的值的大小。 |

**返回：**

返回函数的执行状态。执行成功返回AIP\_OK。

| 错误码ID | 错误信息 |
| --- | --- |
| 0 | 操作成功 |
| 1021200007 | 不存在该字段 |
| 1021200010 | 无效参数 |

**参见：**

[OH\_Retrieval\_RecordItem](dataaugmentation-capi-retrieval.md#oh_retrieval_recorditem)、[OH\_Aip\_ErrCode](dataaugmentation-capi-aip.md#oh_aip_errcode-1)

### OH\_Retrieval\_GetRecordItem()

PhonePC/2in1Tablet

```
1. int OH_Retrieval_GetRecordItem (const OH_Retrieval_Record * record, uint32_t index, const OH_Retrieval_RecordItem ** item )
```

**描述**

获取检索结果[OH\_Retrieval\_Record](dataaugmentation-capi-retrieval.md#oh_retrieval_record)中的数据库bucket数组。

**起始版本：** 6.0.0(20)

**参数:**

| 名称 | 描述 |
| --- | --- |
| record | 指向检索结果[OH\_Retrieval\_Record](dataaugmentation-capi-retrieval.md#oh_retrieval_record)实例的指针。 |
| index | record数组的索引值。最大值为999。 |
| item | 指向record数组中单个元素[OH\_Retrieval\_RecordItem](dataaugmentation-capi-retrieval.md#oh_retrieval_recorditem)的指针。 |

**返回：**

返回函数的执行状态。执行成功返回AIP\_OK。

| 错误码ID | 错误信息 |
| --- | --- |
| 0 | 操作成功 |
| 1021200006 | 下标越界 |
| 1021200010 | 无效参数 |

**参见：**

[OH\_Retrieval\_Record](dataaugmentation-capi-retrieval.md#oh_retrieval_record)、[OH\_Retrieval\_RecordItem](dataaugmentation-capi-retrieval.md#oh_retrieval_recorditem)、[OH\_Aip\_ErrCode](dataaugmentation-capi-aip.md#oh_aip_errcode-1)

### OH\_Retrieval\_GetRecordLength()

PhonePC/2in1Tablet

```
1. int OH_Retrieval_GetRecordLength (const OH_Retrieval_Record * record, uint32_t * length )
```

**描述**

获取检索结果[OH\_Retrieval\_Record](dataaugmentation-capi-retrieval.md#oh_retrieval_record)中的数据库bucket数组。

**起始版本：** 6.0.0(20)

**参数:**

| 名称 | 描述 |
| --- | --- |
| record | 指向检索结果[OH\_Retrieval\_Record](dataaugmentation-capi-retrieval.md#oh_retrieval_record)实例的指针。 |
| length | 数据库bucket数组的长度。 |

**返回：**

返回函数的执行状态。执行成功返回AIP\_OK。

| 错误码ID | 错误信息 |
| --- | --- |
| 0 | 操作成功 |
| 1021200010 | 无效参数 |

**参见：**

[OH\_Retrieval\_Record](dataaugmentation-capi-retrieval.md#oh_retrieval_record)、[OH\_Aip\_ErrCode](dataaugmentation-capi-aip.md#oh_aip_errcode-1)

### OH\_Retrieval\_Retrieve()

PhonePC/2in1Tablet

```
1. int OH_Retrieval_Retrieve (const OH_Retrieval_Retriever * retriever, const OH_Retrieval_Query * query, const OH_Retrieval_Condition * condition, void * context, const OH_Retrieval_Callback * callback )
```

**描述**

执行检索。获得检索器句柄后，输入检索查询词，根据检索条件执行检索，得到检索结果。接口执行时，会在“/data/storage/el2/base/cache”路径下生成临时存储缓存文件。当设备类型为phone、tablet时，该接口仅支持倒排，不支持向量。

**起始版本：** 6.0.0(20)

**参数:**

| 名称 | 描述 |
| --- | --- |
| retriever | 检索器句柄，指向[OH\_Retrieval\_Retriever](dataaugmentation-capi-retrieval.md#oh_retrieval_retriever)实例的指针。 |
| query | 检索的查询词，指向[OH\_Retrieval\_Query](dataaugmentation-capi-retrieval.md#oh_retrieval_query)实例的指针。 |
| condition | 检索条件，指向[OH\_Retrieval\_Condition](dataaugmentation-capi-retrieval.md#oh_retrieval_condition)实例的指针。 |
| context | 表示用户提供的上下文数据，这些数据将在后续调用函数时传递回函数中。 |
| callback | 表示指向[OH\_Retrieval\_Callback](dataaugmentation-capi-retrieval.md#oh_retrieval_callback)实例的指针。 |

**返回：**

返回函数的执行状态。执行成功返回AIP\_OK。

| 错误码ID | 错误信息 |
| --- | --- |
| 0 | 操作成功 |
| 1021200005 | 执行报错 |
| 1021200010 | 无效参数 |
| 1021200012 | 无法生成嵌入向量 |

**参见：**

[OH\_Retrieval\_Retriever](dataaugmentation-capi-retrieval.md#oh_retrieval_retriever)、[OH\_Retrieval\_Query](dataaugmentation-capi-retrieval.md#oh_retrieval_query)、[OH\_Retrieval\_Condition](dataaugmentation-capi-retrieval.md#oh_retrieval_condition)、[OH\_Retrieval\_Callback](dataaugmentation-capi-retrieval.md#oh_retrieval_callback)、[OH\_Aip\_ErrCode](dataaugmentation-capi-aip.md#oh_aip_errcode-1)

### OH\_Retrieval\_SetDbConfig()

PhonePC/2in1Tablet

```
1. int OH_Retrieval_SetDbConfig (OH_Retrieval_DbConfig * dbConfig, OH_Rdb_ConfigV2 * rdbConfig )
```

**描述**

在[OH\_Retrieval\_DbConfig](dataaugmentation-capi-retrieval.md#oh_retrieval_dbconfig)中设置数据库配置。

**起始版本：** 6.0.0(20)

**参数:**

| 名称 | 描述 |
| --- | --- |
| dbConfig | 表示指向[OH\_Retrieval\_DbConfig](dataaugmentation-capi-retrieval.md#oh_retrieval_dbconfig)实例的指针。 |
| rdbConfig | 表示指向数据库配置实例的指针，可能是[OH\_Rdb\_ConfigV2](capi-rdb-oh-rdb-configv2.md)实例。 |

**返回：**

返回函数的执行状态。执行成功返回AIP\_OK。

| 错误码ID | 错误信息 |
| --- | --- |
| 0 | 操作成功 |
| 1021200010 | 无效参数 |

**参见：**

[OH\_Retrieval\_DbConfig](dataaugmentation-capi-retrieval.md#oh_retrieval_dbconfig)、[OH\_Rdb\_ConfigV2](capi-rdb-oh-rdb-configv2.md)、[OH\_Aip\_ErrCode](dataaugmentation-capi-aip.md#oh_aip_errcode-1)

### OH\_Retrieval\_SetOriginalQuestion()

PhonePC/2in1Tablet

```
1. int OH_Retrieval_SetOriginalQuestion (OH_Retrieval_Query * query, const char * question )
```

**描述**

设置[OH\_Retrieval\_Query](dataaugmentation-capi-retrieval.md#oh_retrieval_query)中的检索词。

**起始版本：** 6.0.0(20)

**参数:**

| 名称 | 描述 |
| --- | --- |
| query | 指向检索词[OH\_Retrieval\_Query](dataaugmentation-capi-retrieval.md#oh_retrieval_query)实例的指针。 |
| question | 纯文本的问题。 |

**返回：**

返回函数的执行状态。执行成功返回AIP\_OK。

| 错误码ID | 错误信息 |
| --- | --- |
| 0 | 操作成功 |
| 1021200008 | 数组超过最大长度512字节 |
| 1021200010 | 无效参数 |

**参见：**

[OH\_Retrieval\_Query](dataaugmentation-capi-retrieval.md#oh_retrieval_query)、[OH\_Aip\_ErrCode](dataaugmentation-capi-aip.md#oh_aip_errcode-1)

### OH\_Retrieval\_SetSimilarityThreshold()

PhonePC/2in1Tablet

```
1. int OH_Retrieval_SetSimilarityThreshold (OH_Retrieval_VectorCondition * condition, double threshold )
```

**描述**

在检索条件中，设置向量检索的相似度阈值。

**起始版本：** 6.0.0(20)

**参数:**

| 名称 | 描述 |
| --- | --- |
| condition | 指向检索条件[OH\_Retrieval\_VectorCondition](dataaugmentation-capi-retrieval.md#oh_retrieval_vectorcondition)实例的指针。 |
| threshold | 向量检索的余弦相似度阈值，取值范围[0, 1]。 |

**返回：**

返回函数的执行状态。执行成功返回AIP\_OK。

| 错误码ID | 错误信息 |
| --- | --- |
| 0 | 操作成功 |
| 1021200010 | 无效参数 |

**参见：**

[OH\_Retrieval\_VectorCondition](dataaugmentation-capi-retrieval.md#oh_retrieval_vectorcondition)、[OH\_Aip\_ErrCode](dataaugmentation-capi-aip.md#oh_aip_errcode-1)

### OH\_Retrieval\_SetVectorRecallLimit()

PhonePC/2in1Tablet

```
1. int OH_Retrieval_SetVectorRecallLimit (OH_Retrieval_VectorCondition * condition, uint32_t limit )
```

**描述**

在检索条件中，设置向量检索结果数量上限。

**起始版本：** 6.0.0(20)

**参数:**

| 名称 | 描述 |
| --- | --- |
| condition | 指向检索条件[OH\_Retrieval\_VectorCondition](dataaugmentation-capi-retrieval.md#oh_retrieval_vectorcondition)实例的指针。 |
| limit | 向量检索结果的数量上限，最大值1000。 |

**返回：**

返回函数的执行状态。执行成功返回AIP\_OK。

| 错误码ID | 错误信息 |
| --- | --- |
| 0 | 操作成功 |
| 1021200010 | 无效参数 |

**参见：**

[OH\_Retrieval\_VectorCondition](dataaugmentation-capi-retrieval.md#oh_retrieval_vectorcondition)、[OH\_Aip\_ErrCode](dataaugmentation-capi-aip.md#oh_aip_errcode-1)
