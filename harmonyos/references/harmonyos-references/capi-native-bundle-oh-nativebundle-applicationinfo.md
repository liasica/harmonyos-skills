---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-bundle-oh-nativebundle-applicationinfo
title: OH_NativeBundle_ApplicationInfo
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > C API > 结构体 > OH_NativeBundle_ApplicationInfo
category: harmonyos-references
scraped_at: 2026-09-02T15:00:37+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:52af4d75ee2a1e916aca0ae15518d329f645baaa6df1083d031c08365901b133
---

```c
typedef struct {...} OH_NativeBundle_ApplicationInfo
```

## 概述

应用包信息数据结构，包含应用包名和应用指纹信息。

**起始版本：** 9

**相关模块：** [Native\_Bundle](capi-native-bundle.md)

**所在头文件：** [native\_interface\_bundle.h](capi-native-interface-bundle-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| char\* bundleName | 应用包名。 |
| char\* fingerprint | 应用的指纹信息，由签名证书通过SHA-256算法计算哈希值生成。使用的签名证书发生变化时，该字段也会发生变化。 |
