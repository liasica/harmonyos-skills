---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-print-print-printerinfo
title: Print_PrinterInfo
breadcrumb: API参考 > 系统 > 基础功能 > Basic Services Kit（基础服务） > C API > 结构体 > Print_PrinterInfo
category: harmonyos-references
scraped_at: 2026-04-28T08:09:53+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:dbe168ed3feb959ff304dc971b9aad0da80272c0d9ad83287a309eb3cdfcdf2c
---

```
1. typedef struct {...} Print_PrinterInfo
```

## 概述

PhonePC/2in1Tablet

表示打印机信息。

**起始版本：** 12

**相关模块：** [OH\_Print](capi-oh-print.md)

**所在头文件：** [ohprint.h](capi-ohprint-h.md)

## 汇总

PhonePC/2in1Tablet

### 成员变量

PhonePC/2in1Tablet

| 名称 | 描述 |
| --- | --- |
| [Print\_PrinterState](capi-ohprint-h.md#print_printerstate) printerState | 打印机状态。 |
| [Print\_PrinterCapability](capi-oh-print-print-printercapability.md) capability | 打印机能力。 |
| [Print\_DefaultValue](capi-oh-print-print-defaultvalue.md) defaultValue | 打印机当前属性。 |
| bool isDefaultPrinter | 默认打印机。 |
| char \*printerId | 打印机 ID。 |
| char \*printerName | 打印机名称。 |
| char \*description | 打印机描述。 |
| char \*location | 打印机位置。 |
| char \*makeAndModel | 打印机品牌和型号信息。 |
| char \*printerUri | 打印机 URI。 |
| char \*detailInfo | JSON 格式的详细信息。 |
