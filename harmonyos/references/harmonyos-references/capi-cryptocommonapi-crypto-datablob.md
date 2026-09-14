---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-cryptocommonapi-crypto-datablob
title: Crypto_DataBlob
breadcrumb: API参考 > 系统 > 安全 > Crypto Architecture Kit（加解密算法框架服务） > C API > 结构体 > Crypto_DataBlob
category: harmonyos-references
scraped_at: 2026-09-15T07:06:21+08:00
doc_updated_at: 2026-09-14
content_hash: sha256:19b66cd0dc19c95da55efbc7148ee80445434154a15b75e27fb2173905ee90b1
---

```c
typedef struct Crypto_DataBlob {...} Crypto_DataBlob
```

## 概述

加解密数据结构体。

**起始版本：** 12

**相关模块：** [CryptoCommonApi](capi-cryptocommonapi.md)

**所在头文件：** [crypto\_common.h](capi-crypto-common-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| uint8\_t \*data | 数据缓冲区。 |
| size\_t len | 数据长度。 |
