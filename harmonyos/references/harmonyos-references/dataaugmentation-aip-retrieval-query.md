---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/dataaugmentation-aip-retrieval-query
title: aip_retrieval_query.h
breadcrumb: API参考 > 应用框架 > Data Augmentation Kit（数据增强服务） > C API > 头文件和结构体 > aip_retrieval_query.h
category: harmonyos-references
scraped_at: 2026-04-28T08:05:59+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:151f89d67aa1d75ef5071740f6fe23e1db72652cd86deb080a46f823ee07a336
---

## 概述

PhonePC/2in1Tablet

提供与检索查询相关的接口。

**引用文件：** #include "dataaugmentation/retrieval/aip\_retrieval\_query.h"

**库：** libretrieval\_ndk.so

**系统能力：** SystemCapability.DataAugmentation.Retrieval

**起始版本：** 6.0.0(20)

**相关模块：** [Retrieval](dataaugmentation-capi-retrieval.md)

## 汇总

PhonePC/2in1Tablet

### 类型定义

| 名称 | 描述 |
| --- | --- |
| typedef struct [OH\_Retrieval\_Query](dataaugmentation-capi-retrieval.md#oh_retrieval_query) [OH\_Retrieval\_Query](dataaugmentation-capi-retrieval.md#oh_retrieval_query) | 定义检索词，当前只支持纯文本检索。 |

### 函数

| 名称 | 描述 |
| --- | --- |
| [OH\_Retrieval\_Query](dataaugmentation-capi-retrieval.md#oh_retrieval_query) \* [OH\_Retrieval\_CreateQuery](dataaugmentation-capi-retrieval.md#oh_retrieval_createquery) () | 创建检索词，作为检索接口的入参。 |
| int [OH\_Retrieval\_DestroyQuery](dataaugmentation-capi-retrieval.md#oh_retrieval_destroyquery) ([OH\_Retrieval\_Query](dataaugmentation-capi-retrieval.md#oh_retrieval_query) \*query) | 销毁通过[OH\_Retrieval\_CreateQuery](dataaugmentation-capi-retrieval.md#oh_retrieval_createquery)获得的检索词。 |
| int [OH\_Retrieval\_SetOriginalQuestion](dataaugmentation-capi-retrieval.md#oh_retrieval_setoriginalquestion) ([OH\_Retrieval\_Query](dataaugmentation-capi-retrieval.md#oh_retrieval_query) \*query, const char \*question) | 设置[OH\_Retrieval\_Query](dataaugmentation-capi-retrieval.md#oh_retrieval_query)中的检索词。 |
