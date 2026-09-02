---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm-jsvm-defineclassoptions
title: JSVM_DefineClassOptions
breadcrumb: API参考 > 公共基础能力 > C API > 结构体 > JSVM_DefineClassOptions
category: harmonyos-references
scraped_at: 2026-09-02T15:03:14+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:590de8b67ae13d413939474963cd0b1f8b75263aada0a66b221a226654fbf940
---

```c
typedef struct {...} JSVM_DefineClassOptions
```

## 概述

定义Class的选项。

**系统能力：** SystemCapability.ArkCompiler.JSVM

**起始版本：** 18

**相关模块：** [JSVM](capi-jsvm.md)

**所在头文件：** [jsvm\_types.h](capi-jsvm-types-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| [JSVM\_DefineClassOptionsId](capi-jsvm-types-h.md#jsvm_defineclassoptionsid) id | 定义Class的选项ID。 |
| content | id对应的定义Class选项值联合体。 |
| content.ptr | 指向定义Class选项值的指针。 |
| content.num | 存储整数类型的定义Class选项值。 |
| content.boolean | 存储布尔类型的定义Class选项值。 |
