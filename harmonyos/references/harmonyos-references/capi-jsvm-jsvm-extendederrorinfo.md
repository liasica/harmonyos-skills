---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm-jsvm-extendederrorinfo
title: JSVM_ExtendedErrorInfo
breadcrumb: API参考 > 公共基础能力 > C API > 结构体 > JSVM_ExtendedErrorInfo
category: harmonyos-references
scraped_at: 2026-09-02T15:03:14+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:c119fbed0740a2978b5ef0211dfc17e0505db2ed5a9899d677ce652efba5224d
---

```c
typedef struct {...} JSVM_ExtendedErrorInfo
```

## 概述

扩展的异常信息。

**使用场景：** 在JSVM API调用失败时获取详细的异常信息，调试和排查JavaScript运行时错误，日志记录和错误上报。

**系统能力：** SystemCapability.ArkCompiler.JSVM

**起始版本：** 11

**相关模块：** [JSVM](capi-jsvm.md)

**所在头文件：** [jsvm\_types.h](capi-jsvm-types-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| const char\* errorMessage | UTF-8编码的字符串，包含异常信息。 |
| void\* engineReserved | 特定于VM的详细异常信息。目前尚未为任何VM实现此功能。 |
| uint32\_t engineErrorCode | 特定于VM的异常代码。目前尚未为任何VM实现此功能。 |
| [JSVM\_Status](capi-jsvm-types-h.md#jsvm_status) errorCode | 源自最后一个异常的JSVM-API状态码。 |
