---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hukstypeapi-oh-huks-certchain
title: OH_Huks_CertChain
breadcrumb: API参考 > 系统 > 安全 > Universal Keystore Kit（密钥管理服务） > C API > 结构体 > OH_Huks_CertChain
category: harmonyos-references
scraped_at: 2026-09-02T15:01:47+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:63fab03e1c7e8586d16b869e9f8851ee6c83fae4a34903a3d44dfd69af1c06ad
---

```c
struct OH_Huks_CertChain {...}
```

## 概述

定义证书链的结构体类型。

**起始版本：** 9

**相关模块：** [HuksTypeApi](capi-hukstypeapi.md)

**所在头文件：** [native\_huks\_type.h](capi-native-huks-type-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| struct [OH\_Huks\_Blob](capi-hukstypeapi-oh-huks-blob.md) \*certs | 指向证书数据的指针。 |
| uint32\_t certsCount | 证书数量。 |
