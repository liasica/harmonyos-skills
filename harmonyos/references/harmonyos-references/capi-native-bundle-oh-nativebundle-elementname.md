---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-bundle-oh-nativebundle-elementname
title: OH_NativeBundle_ElementName
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > C API > 结构体 > OH_NativeBundle_ElementName
category: harmonyos-references
scraped_at: 2026-10-11T07:23:39+08:00
doc_updated_at: 2026-10-10
content_hash: sha256:c598557cc2f239aa9ba6e2bc11b97ca8a263a4fec42040bdcb0d0bbd45687264
---

```c
typedef struct OH_NativeBundle_ElementName {...} OH_NativeBundle_ElementName
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
