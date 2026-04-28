---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-cryptocommonapi-crypto-datablob
title: Crypto_DataBlob
breadcrumb: API参考 > 系统 > 安全 > Crypto Architecture Kit（加解密算法框架服务） > C API > 结构体 > Crypto_DataBlob
category: harmonyos-references
scraped_at: 2026-04-28T08:07:00+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:e1e22782cc1d7c3e7aa8832294c7df6a21b506bf00caccc04fb78efd9c7780ee
---

```
1. typedef struct Crypto_DataBlob {...} Crypto_DataBlob
```

## 概述

PhonePC/2in1TabletTVWearable

加解密数据结构体。

**起始版本：** 12

**相关模块：** [CryptoCommonApi](capi-cryptocommonapi.md)

**所在头文件：** [crypto\_common.h](capi-crypto-common-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| uint8\_t\* data | 数据Blob的内容。 |
| size\_t len | 数据Blob的长度。 |
