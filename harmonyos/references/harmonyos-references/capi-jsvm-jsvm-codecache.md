---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm-jsvm-codecache
title: JSVM_CodeCache
breadcrumb: API参考 > 公共基础能力 > C API > 结构体 > JSVM_CodeCache
category: harmonyos-references
scraped_at: 2026-04-28T08:19:25+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:597a12ff73364a4c3a72a6518e005f215bd075bdc853b61ada5304a2a8379b34
---

```
1. typedef struct {...} JSVM_CodeCache
```

## 概述

PhonePC/2in1TabletWearable

表示当id为JSVM\_COMPILE\_CODE\_CACHE时，content的类型。

**起始版本：** 12

**相关模块：** [JSVM](capi-jsvm.md)

**所在头文件：** [jsvm\_types.h](capi-jsvm-types-h.md)

## 汇总

PhonePC/2in1TabletWearable

### 成员变量

PhonePC/2in1TabletWearable

| 名称 | 描述 |
| --- | --- |
| uint8\_t\* cache | 缓存地址。 |
| size\_t length | 缓存大小。 |
