---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/dataaugmentation-aip-retrieval
title: aip_retrieval.h
breadcrumb: API参考 > 应用框架 > Data Augmentation Kit（数据增强服务） > C API > 头文件和结构体 > aip_retrieval.h
category: harmonyos-references
scraped_at: 2026-04-28T08:05:58+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:fc4236883fb7f7d8120e9187c0474f9cb2376f7edb15909dab7ebdedbc84695a
---

## 概述

PhonePC/2in1Tablet

提供知识检索相关的接口。

**引用文件：** #include "dataaugmentation/retrieval/aip\_retrieval.h"

**库：** libretrieval\_ndk.so

**系统能力：** SystemCapability.DataAugmentation.Retrieval

**起始版本：** 6.0.0(20)

**相关模块：** [Retrieval](dataaugmentation-capi-retrieval.md)

## 汇总

PhonePC/2in1Tablet

### 类型定义

| 名称 | 描述 |
| --- | --- |
| typedef struct [OH\_Retrieval\_Retriever](dataaugmentation-capi-retrieval.md#oh_retrieval_retriever) [OH\_Retrieval\_Retriever](dataaugmentation-capi-retrieval.md#oh_retrieval_retriever) | 定义检索器类型，检索器是进行检索的句柄。 |
| typedef struct [OH\_Retrieval\_Config](dataaugmentation-capi-retrieval.md#oh_retrieval_config) [OH\_Retrieval\_Config](dataaugmentation-capi-retrieval.md#oh_retrieval_config) | 定义检索器配置。 |
| typedef struct [OH\_Retrieval\_DbConfig](dataaugmentation-capi-retrieval.md#oh_retrieval_dbconfig) [OH\_Retrieval\_DbConfig](dataaugmentation-capi-retrieval.md#oh_retrieval_dbconfig) | 定义一个用于打开数据库存储的数据库配置。 |
| typedef enum [Retrieval\_Channel\_Type](dataaugmentation-capi-retrieval.md#retrieval_channel_type) [Retrieval\_Channel\_Type](dataaugmentation-capi-retrieval.md#retrieval_channel_type) | 定义数据索引类型，目前仅包含向量索引数据。 |
| typedef void(\* [OH\_Retrieval\_Callback](dataaugmentation-capi-retrieval.md#oh_retrieval_callback)) (void \*context, [OH\_Retrieval\_Record](dataaugmentation-capi-retrieval.md#oh_retrieval_record) \*record, int errCode) | 检索结果记录的回调函数。 |

### 枚举

| 名称 | 描述 |
| --- | --- |
| [Retrieval\_Channel\_Type](dataaugmentation-capi-retrieval.md#retrieval_channel_type) { RETRIEVAL\_TYPE\_VECTOR = 1 } | 定义数据索引类型，目前仅包含向量索引数据。 |

### 函数

| 名称 | 描述 |
| --- | --- |
| int [OH\_Retrieval\_CreateRetriever](dataaugmentation-capi-retrieval.md#oh_retrieval_createretriever) (const [OH\_Retrieval\_Config](dataaugmentation-capi-retrieval.md#oh_retrieval_config) \*config, [OH\_Retrieval\_Retriever](dataaugmentation-capi-retrieval.md#oh_retrieval_retriever) \*\*retriever) | 读取检索配置，初始化检索器。 |
| int [OH\_Retrieval\_DestroyRetriever](dataaugmentation-capi-retrieval.md#oh_retrieval_destroyretriever) ([OH\_Retrieval\_Retriever](dataaugmentation-capi-retrieval.md#oh_retrieval_retriever) \*retriever) | 销毁通过[OH\_Retrieval\_CreateRetriever](dataaugmentation-capi-retrieval.md#oh_retrieval_createretriever)获得的检索器。 |
| [OH\_Retrieval\_Config](dataaugmentation-capi-retrieval.md#oh_retrieval_config) \* [OH\_Retrieval\_CreateConfig](dataaugmentation-capi-retrieval.md#oh_retrieval_createconfig) () | 获取检索器配置。用于初始化检索器。 |
| int [OH\_Retrieval\_DestroyConfig](dataaugmentation-capi-retrieval.md#oh_retrieval_destroyconfig) ([OH\_Retrieval\_Config](dataaugmentation-capi-retrieval.md#oh_retrieval_config) \*config) | 销毁通过[OH\_Retrieval\_CreateConfig](dataaugmentation-capi-retrieval.md#oh_retrieval_createconfig)获得的检索配置。 |
| [OH\_Retrieval\_DbConfig](dataaugmentation-capi-retrieval.md#oh_retrieval_dbconfig) \* [OH\_Retrieval\_CreateDbConfig](dataaugmentation-capi-retrieval.md#oh_retrieval_createdbconfig) () | 创建一个配置项以打开数据库。 |
| int [OH\_Retrieval\_DestroyDbConfig](dataaugmentation-capi-retrieval.md#oh_retrieval_destroydbconfig) ([OH\_Retrieval\_DbConfig](dataaugmentation-capi-retrieval.md#oh_retrieval_dbconfig) \*dbConfig) | 销毁[OH\_Retrieval\_CreateDbConfig](dataaugmentation-capi-retrieval.md#oh_retrieval_createdbconfig)创建的[OH\_Retrieval\_DbConfig](dataaugmentation-capi-retrieval.md#oh_retrieval_dbconfig)。 |
| int [OH\_Retrieval\_SetDbConfig](dataaugmentation-capi-retrieval.md#oh_retrieval_setdbconfig) ([OH\_Retrieval\_DbConfig](dataaugmentation-capi-retrieval.md#oh_retrieval_dbconfig) \*dbConfig, [OH\_Rdb\_ConfigV2](capi-rdb-oh-rdb-configv2.md) \*rdbConfig) | 在[OH\_Retrieval\_DbConfig](dataaugmentation-capi-retrieval.md#oh_retrieval_dbconfig)中设置数据库配置。 |
| int [OH\_Retrieval\_AddConfig](dataaugmentation-capi-retrieval.md#oh_retrieval_addconfig) ([OH\_Retrieval\_Config](dataaugmentation-capi-retrieval.md#oh_retrieval_config) \*config, [Retrieval\_Channel\_Type](dataaugmentation-capi-retrieval.md#retrieval_channel_type) channelType, [OH\_Retrieval\_DbConfig](dataaugmentation-capi-retrieval.md#oh_retrieval_dbconfig) \*dbConfig) | 设置[OH\_Retrieval\_Config](dataaugmentation-capi-retrieval.md#oh_retrieval_config)中的数据库配置。 |
| int [OH\_Retrieval\_Retrieve](dataaugmentation-capi-retrieval.md#oh_retrieval_retrieve) (const [OH\_Retrieval\_Retriever](dataaugmentation-capi-retrieval.md#oh_retrieval_retriever) \*retriever, const [OH\_Retrieval\_Query](dataaugmentation-capi-retrieval.md#oh_retrieval_query) \*query, const [OH\_Retrieval\_Condition](dataaugmentation-capi-retrieval.md#oh_retrieval_condition) \*condition, void \*context, const [OH\_Retrieval\_Callback](dataaugmentation-capi-retrieval.md#oh_retrieval_callback) \*callback) | 执行检索。获得检索器句柄后，输入检索查询词，根据检索条件执行检索，得到检索结果。 |
