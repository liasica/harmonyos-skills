---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm-jsvm-typetag
title: JSVM_TypeTag
breadcrumb: API参考 > 公共基础能力 > C API > 结构体 > JSVM_TypeTag
category: harmonyos-references
scraped_at: 2026-04-28T08:19:25+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:cb281105a01f07d55ba68b5ee34fbace35aa34bb6d60e4309d2d9c6b63341930
---

```
1. typedef struct {...} JSVM_TypeTag
```

## 概述

PhonePC/2in1TabletWearable

类型标记，存储为两个无符号64位整数的128位值。作为一个UUID，通过它，JavaScript对象可以是"tagged"，以确保它们的类型保持不变。

**起始版本：** 11

**相关模块：** [JSVM](capi-jsvm.md)

**所在头文件：** [jsvm\_types.h](capi-jsvm-types-h.md)

## 汇总

PhonePC/2in1TabletWearable

### 成员变量

PhonePC/2in1TabletWearable

| 名称 | 描述 |
| --- | --- |
| uint64\_t lower | 低64位 |
| uint64\_t upper | 高64位 |
