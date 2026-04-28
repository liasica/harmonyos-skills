---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-print-print-printattributes
title: Print_PrintAttributes
breadcrumb: API参考 > 系统 > 基础功能 > Basic Services Kit（基础服务） > C API > 结构体 > Print_PrintAttributes
category: harmonyos-references
scraped_at: 2026-04-28T08:09:55+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:591514c11365dd98799cb8df603ca4c45605bf19ad5baa5fd027948c1818c703
---

```
1. typedef struct {...} Print_PrintAttributes
```

## 概述

PhonePC/2in1Tablet

表示打印属性结构体。

**起始版本：** 13

**相关模块：** [OH\_Print](capi-oh-print.md)

**所在头文件：** [ohprint.h](capi-ohprint-h.md)

## 汇总

PhonePC/2in1Tablet

### 成员变量

PhonePC/2in1Tablet

| 名称 | 描述 |
| --- | --- |
| [Print\_Range](capi-oh-print-print-range.md) pageRange | 打印范围。 |
| [Print\_PageSize](capi-oh-print-print-pagesize.md) pageSize | 打印纸张尺寸。 |
| [Print\_Margin](capi-oh-print-print-margin.md) pageMargin | 打印边距。 |
| uint32\_t copyNumber | 份数。 |
| uint32\_t duplexMode | 双面模式。 |
| uint32\_t colorMode | 色彩模式。 |
| bool isSequential | 顺序打印。  true表示顺序打印，false表示逆序打印。 |
| bool isLandscape | 打印方向（是否横向）。  true表示打印方式为横向，false表示打印方向为竖向。 |
| bool hasOption | 打印选项标志。  true表示有打印选项，false表示没有打印选项。 |
| char options[256] | 打印选项。 |
