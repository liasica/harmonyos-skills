---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-print-print-range
title: Print_Range
breadcrumb: API参考 > 系统 > 基础功能 > Basic Services Kit（基础服务） > C API > 结构体 > Print_Range
category: harmonyos-references
scraped_at: 2026-09-02T15:02:05+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:081e70dda001df466cf0994f2c870503514ceb4a2c6ceb386cdb2cb4729d00af
---

```cpp
typedef struct {...} Print_Range
```

## 概述

表示打印范围结构体，用于指定打印任务中的页码范围。可通过 startPage 和 endPage 指定连续页码范围，或通过 pagesArray 和 pagesArrayLen 指定不连续的打印页码数组。

**起始版本：** 13

**相关模块：** [OH\_Print](capi-oh-print.md)

**所在头文件：** [ohprint.h](capi-ohprint-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| uint32\_t startPage | 打印起始页，页码从 1 开始计数，取值应为文档中的有效页码且需小于等于 endPage。 |
| uint32\_t endPage | 打印结束页，页码从 1 开始计数，取值应为文档中的有效页码且需大于等于 startPage。 |
| uint32\_t pagesArrayLen | 打印页码数组长度，须与 pagesArray 数组实际元素数一致，仅在 pagesArray 不为 NULL 时有效。 |
| uint32\_t\* pagesArray | 打印页码数组，每个元素表示一个需要打印的页码，页码从 1 开始计数，取值应为文档中的有效页码，数组长度由 pagesArrayLen 决定。 |
