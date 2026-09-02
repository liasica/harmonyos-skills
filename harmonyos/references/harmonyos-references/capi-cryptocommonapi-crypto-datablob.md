---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-cryptocommonapi-crypto-datablob
title: Crypto_DataBlob
breadcrumb: API参考 > 系统 > 安全 > Crypto Architecture Kit（加解密算法框架服务） > C API > 结构体 > Crypto_DataBlob
category: harmonyos-references
scraped_at: 2026-09-02T15:01:42+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:b008f0ca057d4d3d59d5d0807f18abd5c150626cc37a45a00c06d7bad9684b6f
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
| uint8\_t\* data | 数据Blob的内容。 |
| size\_t len | 数据Blob的长度。 |
