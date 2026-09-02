---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-print-print-pagesize
title: Print_PageSize
breadcrumb: API参考 > 系统 > 基础功能 > Basic Services Kit（基础服务） > C API > 结构体 > Print_PageSize
category: harmonyos-references
scraped_at: 2026-09-02T15:02:05+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:c70a9582ecf1418b06c03a01790873c027630e7f3a9b70001b4a556d89bc1730
---

```cpp
typedef struct {...} Print_PageSize
```

## 概述

Print\_PageSize用于表示打印任务中的纸张尺寸信息，包含纸张 ID、名称、宽度与高度等关键属性，适用于需要在打印配置流程中指定或查询纸张规格的场景。

**起始版本：** 12

**相关模块：** [OH\_Print](capi-oh-print.md)

**所在头文件：** [ohprint.h](capi-ohprint-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| char \*id | 纸张尺寸的唯一标识 ID，用于区分不同标准纸张规格。 |
| char \*name | 纸张尺寸的名称，如"A4"、"Letter"等标准纸张规格。 |
| uint32\_t width | 纸张宽度，单位：密尔（千分之一英寸）。取值原则：大于0。 |
| uint32\_t height | 纸张高度，单位：密尔（千分之一英寸）。取值原则：大于0。 |
