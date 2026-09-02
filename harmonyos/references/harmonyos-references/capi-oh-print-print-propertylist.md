---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-print-print-propertylist
title: Print_PropertyList
breadcrumb: API参考 > 系统 > 基础功能 > Basic Services Kit（基础服务） > C API > 结构体 > Print_PropertyList
category: harmonyos-references
scraped_at: 2026-09-02T15:02:05+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:1bb2937c0bce927d3de09ac05f2b5609b47267c7fe586a247dd1095ca27247ce
---

```cpp
typedef struct {...} Print_PropertyList
```

## 概述

打印机属性列表，用于存储和管理打印机属性，支持通过属性数量和属性数组的指针对打印机属性进行批量访问和操作。其中count表示属性数量，list为指向属性数组的指针，两者配合表示一组完整的打印机属性，适用于需要查询或设置打印机多项属性信息的场景。

**起始版本：** 12

**相关模块：** [OH\_Print](capi-oh-print.md)

**所在头文件：** [ohprint.h](capi-ohprint-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| uint32\_t count | 属性数量。与list指向的属性数组实际元素数一致。 |
| [Print\_Property](capi-oh-print-print-property.md) \*list | 指向属性数组的指针，用于存储打印机属性信息。须与count配合使用，数组长度由count指定。 |
