---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-bundle-oh-nativebundle-applicationinfo
title: OH_NativeBundle_ApplicationInfo
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > C API > 结构体 > OH_NativeBundle_ApplicationInfo
category: harmonyos-references
scraped_at: 2026-04-28T07:59:02+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:2a5ebf15d87de46f5a880f52d625e738693dc27fb9ebc532948b0fb6d3f7c612
---

```
1. typedef struct {...} OH_NativeBundle_ApplicationInfo
```

## 概述

PhonePC/2in1TabletTVWearable

应用包信息数据结构，包含应用包名和应用指纹信息。

**起始版本：** 9

**相关模块：** [Native\_Bundle](capi-native-bundle.md)

**所在头文件：** [native\_interface\_bundle.h](capi-native-interface-bundle-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| char\* bundleName | 应用包名。 |
| char\* fingerprint | 应用的指纹信息，由签名证书通过SHA-256算法计算哈希值生成。使用的签名证书发生变化时，该字段也会发生变化。 |
