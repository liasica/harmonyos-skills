---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-print-print-property
title: Print_Property
breadcrumb: API参考 > 系统 > 基础功能 > Basic Services Kit（基础服务） > C API > 结构体 > Print_Property
category: harmonyos-references
scraped_at: 2026-09-02T15:02:05+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:1d336e0858c641b83df4f761a25e217261755c4b75d1a90942d32e5d8273370c
---

```cpp
typedef struct {...} Print_Property
```

## 概述

Print\_Property表示打印机属性，以键值对形式描述打印机的各类属性信息，开发者可通过该结构体获取或设置打印机的属性参数。

**起始版本：** 12

**相关模块：** [OH\_Print](capi-oh-print.md)

**所在头文件：** [ohprint.h](capi-ohprint-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| char \*key | 属性键，用于标识打印机属性的类型，取值须为[OH\_Print](capi-oh-print.md)模块定义的有效属性名称。 |
| char \*value | 属性值，与属性键key对应的值内容，其格式和有效范围取决于对应的属性键。 |
