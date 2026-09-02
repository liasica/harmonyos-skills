---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-bundle-oh-nativebundle-metadata
title: OH_NativeBundle_Metadata
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > C API > 结构体 > OH_NativeBundle_Metadata
category: harmonyos-references
scraped_at: 2026-09-02T15:00:37+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:85a02cea8a24b883599350ac4303f7d6738ea05cdbe58082829d358cd612f909
---

```c
typedef struct OH_NativeBundle_Metadata {...} OH_NativeBundle_Metadata
```

## 概述

元数据信息。

**起始版本：** 20

**相关模块：** [Native\_Bundle](capi-native-bundle.md)

**所在头文件：** [native\_interface\_bundle.h](capi-native-interface-bundle-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| char\* name | 元数据名称。 |
| char\* value | 元数据值。 |
| char\* resource | 元数据资源。 |
