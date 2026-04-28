---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm-jsvm-compileprofile
title: JSVM_CompileProfile
breadcrumb: API参考 > 公共基础能力 > C API > 结构体 > JSVM_CompileProfile
category: harmonyos-references
scraped_at: 2026-04-28T08:19:29+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:77b95572ca12e15b05bfd478d24ebe8580831f64b849dfc4916808c797fc895f
---

```
1. typedef const struct {...} JSVM_CompileProfile
```

## 概述

PhonePC/2in1TabletWearable

与JSVM\_COMPILE\_COMPILE\_PROFILE一起传递的编译采样文件。

**起始版本：** 12

**相关模块：** [JSVM](capi-jsvm.md)

**所在头文件：** [jsvm\_types.h](capi-jsvm-types-h.md)

## 汇总

PhonePC/2in1TabletWearable

### 成员变量

PhonePC/2in1TabletWearable

| 名称 | 描述 |
| --- | --- |
| int \*profile | 编译采样文件的指针。 |
| size\_t length | 编译采样文件的大小。 |
