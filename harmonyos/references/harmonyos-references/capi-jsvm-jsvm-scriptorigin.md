---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm-jsvm-scriptorigin
title: JSVM_ScriptOrigin
breadcrumb: API参考 > 公共基础能力 > C API > 结构体 > JSVM_ScriptOrigin
category: harmonyos-references
scraped_at: 2026-04-28T08:19:24+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:a3b7e4a98ba7348d789a2a3dc4c64010ce588cdf2b18c90fde1c2d9f95795de4
---

```
1. typedef struct {...} JSVM_ScriptOrigin
```

## 概述

PhonePC/2in1TabletWearable

某段JavaScript代码的原始信息，如sourceMap路径、源文件名、源文件中的起始行/列号等。

**起始版本：** 12

**相关模块：** [JSVM](capi-jsvm.md)

**所在头文件：** [jsvm\_types.h](capi-jsvm-types-h.md)

## 汇总

PhonePC/2in1TabletWearable

### 成员变量

PhonePC/2in1TabletWearable

| 名称 | 描述 |
| --- | --- |
| const char\* sourceMapUrl | Sourcemap 路径。 |
| const char\* resourceName | 源文件名。 |
| size\_t resourceLineOffset | 这段代码在源文件中的起始行号。 |
| size\_t resourceColumnOffset | 这段代码在源文件中的起始列号。 |
