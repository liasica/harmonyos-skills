---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fast-kit--hms-fast-sortdata
title: HMS_FAST_SortData
breadcrumb: API参考 > 系统 > 基础功能 > FAST Kit（算法加速服务） > C API > 头文件和结构体 > 结构体 > HMS_FAST_SortData
category: harmonyos-references
scraped_at: 2026-09-02T15:02:07+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:ab69b68d43ae6659bb0401b5c38d7ae27fbb211862382751d3f1fce66942d86f
---

## 概述

描述待排序的连续内存数据块。

**系统能力：** SystemCapability.FAST.Core

**起始版本：** 26.0.0

**相关模块：** [FAST](fast-kit-fast.md)

**所在头文件：** [fast\_utils\_algorithm.h](fast-kit-fast-utils-algorithm-8h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| size\_t [sizeOf](fast-kit--hms-fast-sortdata.md#sizeof) | 连续内存容器中单个元素的大小。 |
| size\_t [length](fast-kit--hms-fast-sortdata.md#length) | 连续内存容器中的元素个数。 |
| [HMS\_FAST\_SortElementPtr](fast-kit-fast.md#hms_fast_sortelementptr) [data](fast-kit--hms-fast-sortdata.md#data) | 指向待排序的连续内存起始地址的指针。 |

## 结构体成员变量说明

### sizeOf

```c
size_t HMS_FAST_SortData::sizeOf
```

**描述**

data所指向的连续内存容器中单个元素的大小。

### length

```c
size_t HMS_FAST_SortData::length
```

**描述**

data所指向的连续内存容器中的元素个数。

### data

```c
HMS_FAST_SortElementPtr HMS_FAST_SortData::data
```

**描述**

指向待排序的连续内存起始地址的指针。
