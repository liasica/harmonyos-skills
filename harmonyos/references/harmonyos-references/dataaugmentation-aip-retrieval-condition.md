---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/dataaugmentation-aip-retrieval-condition
title: aip_retrieval_condition.h
breadcrumb: API参考 > 应用框架 > Data Augmentation Kit（数据增强服务） > C API > 头文件 > aip_retrieval_condition.h
category: harmonyos-references
scraped_at: 2026-09-02T15:01:33+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:0ce24f11978f6300ac0d8780258ec9daf7bbd1694e6502327acfb3ccb09d4155
---

## 概述

提供与检索条件相关的接口。

**引用文件：** #include "dataaugmentation/retrieval/aip\_retrieval\_condition.h"

**库：** libretrieval\_ndk.so

**系统能力：** SystemCapability.DataAugmentation.Retrieval

**起始版本：** 6.0.0(20)

**相关模块：** [Retrieval](dataaugmentation-capi-retrieval.md)

## 汇总

### 类型定义

| 名称 | 描述 |
| --- | --- |
| typedef struct [OH\_Retrieval\_Condition](dataaugmentation-capi-retrieval.md#oh_retrieval_condition) [OH\_Retrieval\_Condition](dataaugmentation-capi-retrieval.md#oh_retrieval_condition) | 定义检索条件，可包含多个子检索条件等。 |
| typedef struct [OH\_Retrieval\_SubCondition](dataaugmentation-capi-retrieval.md#oh_retrieval_subcondition) [OH\_Retrieval\_SubCondition](dataaugmentation-capi-retrieval.md#oh_retrieval_subcondition) | 定义子检索条件，可以是向量检索。 |

### 函数

| 名称 | 描述 |
| --- | --- |
| [OH\_Retrieval\_Condition](dataaugmentation-capi-retrieval.md#oh_retrieval_condition) \* [OH\_Retrieval\_CreateCondition](dataaugmentation-capi-retrieval.md#oh_retrieval_createcondition) () | 创建检索条件，作为检索接口的入参。 |
| int [OH\_Retrieval\_DestroyCondition](dataaugmentation-capi-retrieval.md#oh_retrieval_destroycondition) ([OH\_Retrieval\_Condition](dataaugmentation-capi-retrieval.md#oh_retrieval_condition) \*condition) | 销毁通过[OH\_Retrieval\_CreateCondition](dataaugmentation-capi-retrieval.md#oh_retrieval_createcondition)获得的检索条件。 |
| int [OH\_Retrieval\_DestroySubCondition](dataaugmentation-capi-retrieval.md#oh_retrieval_destroysubcondition) ([OH\_Retrieval\_SubCondition](dataaugmentation-capi-retrieval.md#oh_retrieval_subcondition) \*condition) | 销毁通过[OH\_Retrieval\_SubCondition](dataaugmentation-capi-retrieval.md#oh_retrieval_subcondition)创建的条件。 |
| int [OH\_Retrieval\_AddSubCondition](dataaugmentation-capi-retrieval.md#oh_retrieval_addsubcondition) ([OH\_Retrieval\_Condition](dataaugmentation-capi-retrieval.md#oh_retrieval_condition) \*condition, [OH\_Retrieval\_SubCondition](dataaugmentation-capi-retrieval.md#oh_retrieval_subcondition) \*subCondition) | 在检索条件中，增加子检索条件。 |
