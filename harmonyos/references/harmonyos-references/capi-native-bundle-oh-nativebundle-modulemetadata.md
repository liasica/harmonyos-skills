---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-bundle-oh-nativebundle-modulemetadata
title: OH_NativeBundle_ModuleMetadata
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > C API > 结构体 > OH_NativeBundle_ModuleMetadata
category: harmonyos-references
scraped_at: 2026-09-02T15:00:37+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:dc223055cf7c4fb88a6f1de2189346127bc1b3a3f50418eaebc0171d334b3476
---

```c
typedef struct OH_NativeBundle_ModuleMetadata {...} OH_NativeBundle_ModuleMetadata
```

## 概述

模块元数据的信息。

**起始版本：** 20

**相关模块：** [Native\_Bundle](capi-native-bundle.md)

**所在头文件：** [native\_interface\_bundle.h](capi-native-interface-bundle-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| char\* moduleName | 模块名称。 |
| [OH\_NativeBundle\_Metadata\*](capi-native-bundle-oh-nativebundle-metadata.md) metadataArray | 模块的元数据数组。 |
| size\_t metadataArraySize | 模块的元数据数组大小。需与metadataArray配合使用，应等于metadataArray数组的实际元素数量，设置错误可能导致数组越界或数据访问异常。 |
