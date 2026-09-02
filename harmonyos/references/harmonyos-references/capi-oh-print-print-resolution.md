---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-print-print-resolution
title: Print_Resolution
breadcrumb: API参考 > 系统 > 基础功能 > Basic Services Kit（基础服务） > C API > 结构体 > Print_Resolution
category: harmonyos-references
scraped_at: 2026-09-02T15:02:05+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:bf3a75de5db7baf62abd48aff1968dba690dcc99f328fee298d34bd4fb9f11bc
---

```cpp
typedef struct {...} Print_Resolution
```

## 概述

Print\_Resolution用于表示以 dpi 为单位的打印分辨率，可控制打印输出的精细度与质量。

**起始版本：** 12

**相关模块：** [OH\_Print](capi-oh-print.md)

**所在头文件：** [ohprint.h](capi-ohprint-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| uint32\_t horizontalDpi | 水平方向的打印分辨率，单位为 dpi。 |
| uint32\_t verticalDpi | 垂直方向的打印分辨率，单位为 dpi。 |
