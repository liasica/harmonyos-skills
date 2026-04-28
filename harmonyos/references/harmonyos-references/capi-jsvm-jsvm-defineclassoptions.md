---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm-jsvm-defineclassoptions
title: JSVM_DefineClassOptions
breadcrumb: API参考 > 公共基础能力 > C API > 结构体 > JSVM_DefineClassOptions
category: harmonyos-references
scraped_at: 2026-04-28T08:19:26+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:40420f0bc30fefa1bc668c97864536c43c2e46638d9be459642766351895843e
---

```
1. typedef struct {...} JSVM_DefineClassOptions
```

## 概述

PhonePC/2in1TabletWearable

定义Class的选项。

**起始版本：** 18

**相关模块：** [JSVM](capi-jsvm.md)

**所在头文件：** [jsvm\_types.h](capi-jsvm-types-h.md)

## 汇总

PhonePC/2in1TabletWearable

### 成员变量

PhonePC/2in1TabletWearable

| 名称 | 描述 |
| --- | --- |
| [JSVM\_DefineClassOptionsId](capi-jsvm-types-h.md#jsvm_defineclassoptionsid) id | 定义Class的选项ID。 |
| content | id对应的定义Class选项值联合体。 |
| content.ptr | 指向定义Class选项值的指针。 |
| content.num | 存储整数类型的定义Class选项值。 |
| content.boolean | 存储布尔类型的定义Class选项值。 |
