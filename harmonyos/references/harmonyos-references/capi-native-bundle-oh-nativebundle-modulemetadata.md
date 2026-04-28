---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-bundle-oh-nativebundle-modulemetadata
title: OH_NativeBundle_ModuleMetadata
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > C API > 结构体 > OH_NativeBundle_ModuleMetadata
category: harmonyos-references
scraped_at: 2026-04-28T07:59:03+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:efa153127dc4b2e2e929145dcd5c312e261c18a14ac60b57a1fc47d8bb25c1ed
---

```
1. typedef struct OH_NativeBundle_ModuleMetadata {...} OH_NativeBundle_ModuleMetadata
```

## 概述

PhonePC/2in1TabletTVWearable

模块元数据的信息。

**起始版本：** 20

**相关模块：** [Native\_Bundle](capi-native-bundle.md)

**所在头文件：** [native\_interface\_bundle.h](capi-native-interface-bundle-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| char\* moduleName | 模块名称。 |
| [OH\_NativeBundle\_Metadata\*](capi-native-bundle-oh-nativebundle-metadata.md) metadataArray | 模块的元数据数组。 |
| size\_t metadataArraySize | 模块的元数据数组大小。 |
