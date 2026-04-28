---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-print-print-propertylist
title: Print_PropertyList
breadcrumb: API参考 > 系统 > 基础功能 > Basic Services Kit（基础服务） > C API > 结构体 > Print_PropertyList
category: harmonyos-references
scraped_at: 2026-04-28T08:09:54+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:55b9a089008ec7f40cd2eabcfe9f8cfaffe8ec635fe1475ac58b24ceea3604c9
---

```
1. typedef struct {...} Print_PropertyList
```

## 概述

PhonePC/2in1Tablet

打印机属性列表。

**起始版本：** 12

**相关模块：** [OH\_Print](capi-oh-print.md)

**所在头文件：** [ohprint.h](capi-ohprint-h.md)

## 汇总

PhonePC/2in1Tablet

### 成员变量

PhonePC/2in1Tablet

| 名称 | 描述 |
| --- | --- |
| uint32\_t count | 属性数量。 |
| [Print\_Property](capi-oh-print-print-property.md) \*list | 属性指针数组。 |
