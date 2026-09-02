---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-print-print-printattributes
title: Print_PrintAttributes
breadcrumb: API参考 > 系统 > 基础功能 > Basic Services Kit（基础服务） > C API > 结构体 > Print_PrintAttributes
category: harmonyos-references
scraped_at: 2026-09-02T15:02:05+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:2859b97370c43559560705c1d6b56d8057cd2cc36c0a6cd42f4e3413942282b3
---

```cpp
typedef struct {...} Print_PrintAttributes
```

## 概述

表示打印属性结构体，用于配置打印任务的各项属性（如打印范围、纸张尺寸、边距、份数、双面模式、色彩模式、打印方向及打印选项等），适用于需要对打印输出进行精细化控制的场景。

**起始版本：** 13

**相关模块：** [OH\_Print](capi-oh-print.md)

**所在头文件：** [ohprint.h](capi-ohprint-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| [Print\_Range](capi-oh-print-print-range.md) pageRange | 打印范围。 |
| [Print\_PageSize](capi-oh-print-print-pagesize.md) pageSize | 打印纸张尺寸。 |
| [Print\_Margin](capi-oh-print-print-margin.md) pageMargin | 打印边距。 |
| uint32\_t copyNumber | 份数。取值范围：大于等于1。 |
| uint32\_t duplexMode | 双面模式。有效取值参见[Print\_DuplexMode](capi-ohprint-h.md#print_duplexmode)枚举定义。 |
| uint32\_t colorMode | 色彩模式。有效取值参见[Print\_ColorMode](capi-ohprint-h.md#print_colormode)枚举定义。 |
| bool isSequential | 顺序打印。  true 表示顺序打印，false 表示逆序打印。 |
| bool isLandscape | 打印方向（是否横向）。  true 表示打印方向为横向，false 表示打印方向为纵向。 |
| bool hasOption | 打印选项标志。  true 表示有打印选项（options 字段有效），false 表示没有打印选项（options 字段无效）。 |
| char options[256] | 打印选项，用于传递额外的打印配置参数。仅在 hasOption 为 true 时生效，最大长度255个字符。 |
