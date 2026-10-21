---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-bundle-oh-nativebundle-elementname
title: OH_NativeBundle_ElementName
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > C API > 结构体 > OH_NativeBundle_ElementName
category: harmonyos-references
scraped_at: 2026-10-22T07:07:06+08:00
doc_updated_at: 2026-10-21
content_hash: sha256:248aa9d950876a35b91732cb25c246239d2e357f18a792a9974c9d867d11a637
---

```c
struct OH_NativeBundle_ElementName {...}
typedef struct OH_NativeBundle_ElementName OH_NativeBundle_ElementName
```

## 概述

elementName信息。

**起始版本：** 13

**相关模块：** [Native\_Bundle](capi-native-bundle.md)

**所在头文件：** [native\_interface\_bundle.h](capi-native-interface-bundle-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| char\* bundleName | 应用包名。 |
| char\* moduleName | 模块名称。 |
| char\* abilityName | Ability名称。 |
