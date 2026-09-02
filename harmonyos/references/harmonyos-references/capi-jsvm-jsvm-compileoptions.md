---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm-jsvm-compileoptions
title: JSVM_CompileOptions
breadcrumb: API参考 > 公共基础能力 > C API > 结构体 > JSVM_CompileOptions
category: harmonyos-references
scraped_at: 2026-09-02T15:03:14+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:6f78e4ce599ba7a9e9035736ceab30751914476709fb5179c92491ce323b35d1
---

```c
typedef struct {...} JSVM_CompileOptions
```

## 概述

配合[OH\_JSVM\_CompileScriptWithOptions](capi-jsvm-h.md#oh_jsvm_compilescriptwithoptions)接口使用，是其参数中options数组的元素类型。

**使用场景：** 当需要对JS脚本进行自定义编译配置时使用，例如设置编译优化级别、启用调试信息、配置模块解析策略等场景。

**系统能力：** SystemCapability.ArkCompiler.JSVM

**起始版本：** 12

**相关模块：** [JSVM](capi-jsvm.md)

**所在头文件：** [jsvm\_types.h](capi-jsvm-types-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| [JSVM\_CompileOptionId](capi-jsvm-types-h.md#jsvm_compileoptionid) id | 编译选项对应的ID。 |
| content | id对应的编译选项值联合体。 |
| content.ptr | 指向编译选项值的指针。 |
| content.num | 存储整数类型的编译选项值。 |
| content.boolean | 存储布尔类型的编译选项值。 |
