---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-print-print-range
title: Print_Range
breadcrumb: API参考 > 系统 > 基础功能 > Basic Services Kit（基础服务） > C API > 结构体 > Print_Range
category: harmonyos-references
scraped_at: 2026-10-22T07:09:23+08:00
doc_updated_at: 2026-10-21
content_hash: sha256:193df95aa58f7306f50d3d42b0356b1ac310adebbe2a532cab2217025ee0443c
---

```cpp
typedef struct {...} Print_Range
```

## 概述

表示打印范围结构体，用于指定打印任务中的页码范围。可通过startPage和endPage指定连续页码范围，或通过pagesArray和pagesArrayLen指定不连续的打印页码数组。

**起始版本：** 13

**相关模块：** [OH\_Print](capi-oh-print.md)

**所在头文件：** [ohprint.h](capi-ohprint-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| uint32\_t startPage | 打印起始页，页码从1开始计数，取值应为文档中的有效页码且需小于等于endPage。 |
| uint32\_t endPage | 打印结束页，页码从1开始计数，取值应为文档中的有效页码且需大于等于startPage。 |
| uint32\_t pagesArrayLen | 打印页码数组长度，须与pagesArray数组实际元素数一致，仅在pagesArray不为NULL时有效。 |
| uint32\_t\* pagesArray | 打印页码数组，每个元素表示一个需要打印的页码，页码从1开始计数，取值应为文档中的有效页码，数组长度由pagesArrayLen决定。 |
