---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fast-kit-fast-utils-algorithm-8h
title: fast_utils_algorithm.h
breadcrumb: API参考 > 系统 > 基础功能 > FAST Kit（算法加速服务） > C API > 头文件和结构体 > 头文件 > fast_utils_algorithm.h
category: harmonyos-references
scraped_at: 2026-09-02T15:02:07+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:ac4081ebe16bc30d934d50fc757ee6ab4cf080d188178545aa4c630b54e99dde
---

## 概述

通用算法工具头文件，目前提供排序相关的数据结构和函数定义。

**引用文件：** <FASTKit/fast\_utils\_algorithm.h>

**库：** libfast\_utils.so

**系统能力：** SystemCapability.FAST.Core

**起始版本：** 26.0.0

**相关模块：** [FAST](fast-kit-fast.md)

## 汇总

### 结构体

| 名称 | 描述 |
| --- | --- |
| struct [HMS\_FAST\_SortData](fast-kit--hms-fast-sortdata.md) | 描述待排序的连续内存数据块。 |

### 类型定义

| 名称 | 描述 |
| --- | --- |
| typedef struct [HMS\_FAST\_SortData](fast-kit--hms-fast-sortdata.md) [HMS\_FAST\_SortData](fast-kit-fast.md#hms_fast_sortdata) | 描述待排序的连续内存数据块。 |
| typedef void\* [HMS\_FAST\_SortElementPtr](fast-kit-fast.md#hms_fast_sortelementptr) | 表示通用容器中单个元素的opaque pointer类型。 |
| typedef const void\* [HMS\_FAST\_SortElementConstPtr](fast-kit-fast.md#hms_fast_sortelementconstptr) | 表示通用容器中单个元素的const opaque pointer类型。 |
| typedef int32\_t(\*[HMS\_FAST\_Sort\_CompFunc](fast-kit-fast.md#hms_fast_sort_compfunc)) ([HMS\_FAST\_SortElementConstPtr](fast-kit-fast.md#hms_fast_sortelementconstptr) first, [HMS\_FAST\_SortElementConstPtr](fast-kit-fast.md#hms_fast_sortelementconstptr) second) | 开发者自定义比较函数的回调函数指针类型。 |

### 函数

| 名称 | 描述 |
| --- | --- |
| [FAST\_ErrorCode](fast-kit-fast.md#fast_errorcode-1) [HMS\_FAST\_Algo\_Sort](fast-kit-fast.md#hms_fast_algo_sort) ([HMS\_FAST\_SortData](fast-kit--hms-fast-sortdata.md) \*data, [HMS\_FAST\_Sort\_CompFunc](fast-kit-fast.md#hms_fast_sort_compfunc) comp) | 使用开发者提供的比较函数对任意类型数组进行完整排序。 |
| [FAST\_ErrorCode](fast-kit-fast.md#fast_errorcode-1) [HMS\_FAST\_Algo\_PartialSortAt](fast-kit-fast.md#hms_fast_algo_partialsortat) ([HMS\_FAST\_SortData](fast-kit--hms-fast-sortdata.md) \*data, size\_t offset, size\_t count, [HMS\_FAST\_Sort\_CompFunc](fast-kit-fast.md#hms_fast_sort_compfunc) comp) | 对数组进行原地部分排序，使指定区间对应排序后的相应段。 |
| [FAST\_ErrorCode](fast-kit-fast.md#fast_errorcode-1) [HMS\_FAST\_Algo\_NaturalSort](fast-kit-fast.md#hms_fast_algo_naturalsort) ([HMS\_FAST\_SortData](fast-kit--hms-fast-sortdata.md) \*data, int32\_t ascend) | 使用自然语言规则对UTF-8字符串数组进行排序。 |
| [FAST\_ErrorCode](fast-kit-fast.md#fast_errorcode-1) [HMS\_FAST\_Algo\_NaturalPartialSortAt](fast-kit-fast.md#hms_fast_algo_naturalpartialsortat) ([HMS\_FAST\_SortData](fast-kit--hms-fast-sortdata.md) \*data, size\_t offset, size\_t count, int32\_t ascend) | 使用自然语言规则对UTF-8字符串数组进行部分排序，使指定区间对应排序后的相应段。 |
