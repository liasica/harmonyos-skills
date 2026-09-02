---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm-jsvm-initoptions
title: JSVM_InitOptions
breadcrumb: API参考 > 公共基础能力 > C API > 结构体 > JSVM_InitOptions
category: harmonyos-references
scraped_at: 2026-09-02T15:03:14+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:782ea76b84b907edfe0880b5e43e75745f12f312e2f3a017f0269a48e34b45ca
---

```c
typedef struct {...} JSVM_InitOptions
```

## 概述

初始化选项，用于初始化JavaScript虚拟机。

**使用场景：** 嵌入JavaScript引擎的应用程序初始化，需要在应用中执行JavaScript代码的场景，需要自定义虚拟机配置的开发调试场景。

**系统能力：** SystemCapability.ArkCompiler.JSVM

**起始版本：** 11

**相关模块：** [JSVM](capi-jsvm.md)

**所在头文件：** [jsvm\_types.h](capi-jsvm-types-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| const intptr\_t\* externalReferences | 可选。嵌入器中可选的、以nullptr结尾的原始地址数组，虚拟机可以在序列化期间与之匹配，并可用于反序列化。此数组及其内容必须在虚拟机实例的整个生命周期内保持有效。 |
| int\* argc | 虚拟机的标志。如果removeFlags为true，则已识别的标志将从（argc, argv）中移除。请注意，这些标志当前仅限于V8虚拟机。它们主要用于开发。不要将它们用于生产环境，因为如果虚拟机与开发环境不同，它们可能不会生效。 |
| char\*\* argv | 指向命令行参数字符串数组的指针，与argc配合传递虚拟机相关配置。 |
| bool removeFlags | 是否删除，为true，则已识别的标志将从（argc, argv）中移除，为false，则已识别的标志不会从（argc, argv）中移除。 |
