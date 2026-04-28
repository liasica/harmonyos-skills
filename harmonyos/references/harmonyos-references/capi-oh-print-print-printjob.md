---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-print-print-printjob
title: Print_PrintJob
breadcrumb: API参考 > 系统 > 基础功能 > Basic Services Kit（基础服务） > C API > 结构体 > Print_PrintJob
category: harmonyos-references
scraped_at: 2026-04-28T08:09:54+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:5b40ae114062d92108d42f29bcfa768b50323a89cedde1fdc0d2f4f7eabece30
---

```
1. typedef struct {...} Print_PrintJob
```

## 概述

PhonePC/2in1Tablet

表示打印任务结构体。

**起始版本：** 12

**相关模块：** [OH\_Print](capi-oh-print.md)

**所在头文件：** [ohprint.h](capi-ohprint-h.md)

## 汇总

PhonePC/2in1Tablet

### 成员变量

PhonePC/2in1Tablet

| 名称 | 描述 |
| --- | --- |
| char \*jobName | 任务名称。 |
| uint32\_t \*fdList | 待打印的文件描述符数组。 |
| uint32\_t fdListCount | 待打印的文件描述符数量。 |
| char \*printerId | 打印机 ID。 |
| uint32\_t copyNumber | 打印份数。 |
| char \*paperSource | 纸张来源。 |
| char \*mediaType | 介质类型。 |
| char \*pageSizeId | 纸张尺寸 ID。 |
| [Print\_ColorMode](capi-ohprint-h.md#print_colormode) colorMode | 色彩模式。 |
| [Print\_DuplexMode](capi-ohprint-h.md#print_duplexmode) duplexMode | 双面模式。 |
| [Print\_Resolution](capi-oh-print-print-resolution.md) resolution | 以 dpi 为单位的打印分辨率。 |
| [Print\_Margin](capi-oh-print-print-margin.md) printMargin | 打印边距。 |
| bool borderless | 无边距。 |
| [Print\_OrientationMode](capi-ohprint-h.md#print_orientationmode) orientationMode | 方向模式。 |
| [Print\_Quality](capi-ohprint-h.md#print_quality) printQuality | 打印质量。 |
| [Print\_DocumentFormat](capi-ohprint-h.md#print_documentformat) documentFormat | 文档格式。 |
| char \*advancedOptions | JSON 格式的高级选项。  支持的键包括：  - **isReverse**：布尔类型，表示是否逆序打印。  - **isCollate**：布尔类型，表示是否逐份打印。 |
