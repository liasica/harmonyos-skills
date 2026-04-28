---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm-jsvm-vminfo
title: JSVM_VMInfo
breadcrumb: API参考 > 公共基础能力 > C API > 结构体 > JSVM_VMInfo
category: harmonyos-references
scraped_at: 2026-04-28T08:19:24+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:8389cc61fbe652e62b63f8f6d44bcf2f18d4745377c26488af2df8e78bd273e7
---

```
1. typedef struct {...} JSVM_VMInfo
```

## 概述

PhonePC/2in1TabletWearable

JavaScript虚拟机信息。

**起始版本：** 11

**相关模块：** [JSVM](capi-jsvm.md)

**所在头文件：** [jsvm\_types.h](capi-jsvm-types-h.md)

## 汇总

PhonePC/2in1TabletWearable

### 成员变量

PhonePC/2in1TabletWearable

| 名称 | 描述 |
| --- | --- |
| uint32\_t apiVersion | 此虚拟机支持的最高API版本。 |
| const char\* engine | 实现虚拟机的引擎名称。 |
| const char\* version | 虚拟机的版本。 |
| uint32\_t cachedDataVersionTag | 缓存数据版本标签。 |
