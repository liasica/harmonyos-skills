---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-print-print-stringlist
title: Print_StringList
breadcrumb: API参考 > 系统 > 基础功能 > Basic Services Kit（基础服务） > C API > 结构体 > Print_StringList
category: harmonyos-references
scraped_at: 2026-09-02T15:02:05+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:0a118227539c13e651c5707c71666afbf5b83da2a0299b4abaadfb5c332ea422
---

```cpp
typedef struct {...} Print_StringList
```

## 概述

表示字符串列表，用于在打印模块中传递多个字符串数据。该结构体通过count字段记录字符串数量、list字段指向字符串数组，适用于需要批量传递多个字符串数据的场景。相关接口请参见[OH\_Print](capi-oh-print.md)。

**起始版本：** 12

**相关模块：** [OH\_Print](capi-oh-print.md)

**所在头文件：** [ohprint.h](capi-ohprint-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| uint32\_t count | 字符串数量，表示list数组中的元素数量。 |
| char \*\*list | 指向字符串数组的指针，数组元素数量须与count值一致。 |
