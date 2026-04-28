---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-print-print-range
title: Print_Range
breadcrumb: API参考 > 系统 > 基础功能 > Basic Services Kit（基础服务） > C API > 结构体 > Print_Range
category: harmonyos-references
scraped_at: 2026-04-28T08:09:53+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:878007dc4d21df0461238223eade34f6754b4dca4f9f4dc508dcb3b8e043e9b1
---

```
1. typedef struct {...} Print_Range
```

## 概述

PhonePC/2in1Tablet

表示打印范围结构体。

**起始版本：** 13

**相关模块：** [OH\_Print](capi-oh-print.md)

**所在头文件：** [ohprint.h](capi-ohprint-h.md)

## 汇总

PhonePC/2in1Tablet

### 成员变量

PhonePC/2in1Tablet

| 名称 | 描述 |
| --- | --- |
| uint32\_t startPage | 打印起始页。 |
| uint32\_t endPage | 打印结束页。 |
| uint32\_t pagesArrayLen | 打印页数组长度。 |
| uint32\_t\* pagesArray | 打印页数组。 |
