---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-print-print-resolution
title: Print_Resolution
breadcrumb: API参考 > 系统 > 基础功能 > Basic Services Kit（基础服务） > C API > 结构体 > Print_Resolution
category: harmonyos-references
scraped_at: 2026-10-22T07:09:24+08:00
doc_updated_at: 2026-10-21
content_hash: sha256:6c5a3c5624719d39e7ee629331ea64715b3d52b943bf97490ddff575c7e1b9e6
---

```cpp
typedef struct {...} Print_Resolution
```

## 概述

Print\_Resolution用于表示以dpi为单位的打印分辨率，可控制打印输出的精细度与质量。

**起始版本：** 12

**相关模块：** [OH\_Print](capi-oh-print.md)

**所在头文件：** [ohprint.h](capi-ohprint-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| uint32\_t horizontalDpi | 水平方向的打印分辨率，单位为dpi。 |
| uint32\_t verticalDpi | 垂直方向的打印分辨率，单位为dpi。 |
