---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hukstypeapi-oh-huks-keyinfo
title: OH_Huks_KeyInfo
breadcrumb: API参考 > 系统 > 安全 > Universal Keystore Kit（密钥管理服务） > C API > 结构体 > OH_Huks_KeyInfo
category: harmonyos-references
scraped_at: 2026-04-29T13:58:19+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:b28a727004d7da7dcea34e1a103618e705b9ea87aaff34abd2112112642a67ff
---

```
1. struct OH_Huks_KeyInfo {...}
```

## 概述

PhonePC/2in1TabletTVWearable

定义密钥信息的结构体类型。

**起始版本：** 9

**相关模块：** [HuksTypeApi](capi-hukstypeapi.md)

**所在头文件：** [native\_huks\_type.h](capi-native-huks-type-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| struct [OH\_Huks\_Blob](capi-hukstypeapi-oh-huks-blob.md) alias | 密钥的别名。 |
| struct [OH\_Huks\_ParamSet](capi-hukstypeapi-oh-huks-paramset.md) \*paramSet | 指向密钥参数集的指针。 |
