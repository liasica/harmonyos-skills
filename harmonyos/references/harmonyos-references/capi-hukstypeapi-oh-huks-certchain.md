---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hukstypeapi-oh-huks-certchain
title: OH_Huks_CertChain
breadcrumb: API参考 > 系统 > 安全 > Universal Keystore Kit（密钥管理服务） > C API > 结构体 > OH_Huks_CertChain
category: harmonyos-references
scraped_at: 2026-04-29T13:58:19+08:00
doc_updated_at: 2026-03-20
content_hash: sha256:8d8409d94284f97e66d737e6fce1bcb1f89c34248cbff7cdce606be5557697b6
---

```
1. struct OH_Huks_CertChain {...}
```

## 概述

PhonePC/2in1TabletTVWearable

定义证书链的结构体类型。

**起始版本：** 9

**相关模块：** [HuksTypeApi](capi-hukstypeapi.md)

**所在头文件：** [native\_huks\_type.h](capi-native-huks-type-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| struct [OH\_Huks\_Blob](capi-hukstypeapi-oh-huks-blob.md) \*certs | 指向证书数据的指针。 |
| uint32\_t certsCount | 证书数量。 |
