---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm-jsvm-extendederrorinfo
title: JSVM_ExtendedErrorInfo
breadcrumb: API参考 > 公共基础能力 > C API > 结构体 > JSVM_ExtendedErrorInfo
category: harmonyos-references
scraped_at: 2026-04-28T08:19:25+08:00
doc_updated_at: 2026-03-17
content_hash: sha256:d6ab3956d44c66780bb01ce917d0ddaf3a8bedf1d3f118e37ceda5b5057d8185
---

```
1. typedef struct {...} JSVM_ExtendedErrorInfo
```

## 概述

PhonePC/2in1TabletWearable

扩展的异常信息。

**起始版本：** 11

**相关模块：** [JSVM](capi-jsvm.md)

**所在头文件：** [jsvm\_types.h](capi-jsvm-types-h.md)

## 汇总

PhonePC/2in1TabletWearable

### 成员变量

PhonePC/2in1TabletWearable

| 名称 | 描述 |
| --- | --- |
| const char\* errorMessage | UTF-8编码的字符串，包含异常信息。 |
| void\* engineReserved | 特定于VM的详细异常信息。目前尚未为任何VM实现此功能。 |
| uint32\_t engineErrorCode | 特定于VM的异常代码。目前尚未为任何VM实现此功能。 |
| JSVM\_Status errorCode | 源自最后一个异常的JSVM-API状态码。 |
