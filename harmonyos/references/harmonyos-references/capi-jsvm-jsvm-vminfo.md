---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm-jsvm-vminfo
title: JSVM_VMInfo
breadcrumb: API参考 > 公共基础能力 > C API > 结构体 > JSVM_VMInfo
category: harmonyos-references
scraped_at: 2026-09-02T15:03:14+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:77da812ee247d2e42e02374eafcaba903d498e9d3627b6a0a13a6a0c246d9d19
---

```c
typedef struct {...} JSVM_VMInfo
```

## 概述

JavaScript虚拟机信息。

**系统能力：** SystemCapability.ArkCompiler.JSVM

**起始版本：** 11

**相关模块：** [JSVM](capi-jsvm.md)

**所在头文件：** [jsvm\_types.h](capi-jsvm-types-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| uint32\_t apiVersion | 此虚拟机支持的最高API版本。 |
| const char\* engine | 实现虚拟机的引擎名称。 |
| const char\* version | 虚拟机的版本。 |
| uint32\_t cachedDataVersionTag | 缓存数据版本标签。 |
