---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm-jsvm-codecache
title: JSVM_CodeCache
breadcrumb: API参考 > 公共基础能力 > C API > 结构体 > JSVM_CodeCache
category: harmonyos-references
scraped_at: 2026-09-02T15:03:14+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:ec4b355697dae9fa907389f162256091e5abb781daba0f2e23f60508e1a5b768
---

```c
typedef struct {...} JSVM_CodeCache
```

## 概述

表示当id为JSVM\_COMPILE\_CODE\_CACHE时，content的类型。

**系统能力：** SystemCapability.ArkCompiler.JSVM

**起始版本：** 12

**相关模块：** [JSVM](capi-jsvm.md)

**所在头文件：** [jsvm\_types.h](capi-jsvm-types-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| uint8\_t\* cache | 缓存地址。 |
| size\_t length | 缓存大小。 |
