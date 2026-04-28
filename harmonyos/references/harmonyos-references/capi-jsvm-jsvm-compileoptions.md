---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm-jsvm-compileoptions
title: JSVM_CompileOptions
breadcrumb: API参考 > 公共基础能力 > C API > 结构体 > JSVM_CompileOptions
category: harmonyos-references
scraped_at: 2026-04-28T08:19:25+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:84b4f68504a199d5ecd6b1d7bd859341955a64790a61ffb650cf76142d3a554e
---

```
1. typedef struct {...} JSVM_CompileOptions
```

## 概述

PhonePC/2in1TabletWearable

配合[OH\_JSVM\_CompileScriptWithOptions](capi-jsvm-h.md#oh_jsvm_compilescriptwithoptions)接口使用，是其参数中options数组的元素类型。

**起始版本：** 12

**相关模块：** [JSVM](capi-jsvm.md)

**所在头文件：** [jsvm\_types.h](capi-jsvm-types-h.md)

## 汇总

PhonePC/2in1TabletWearable

### 成员变量

PhonePC/2in1TabletWearable

| 名称 | 描述 |
| --- | --- |
| [JSVM\_CompileOptionId](capi-jsvm-types-h.md#jsvm_compileoptionid) id | 编译选项对应的ID。 |
| content | id对应的编译选项值联合体。 |
| content.ptr | 指向编译选项值的指针。 |
| content.num | 存储整数类型的编译选项值。 |
| content.boolean | 存储布尔类型的编译选项值。 |
