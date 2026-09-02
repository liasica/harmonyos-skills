---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hukstypeapi-oh-huks-pubkeyinfo
title: OH_Huks_PubKeyInfo
breadcrumb: API参考 > 系统 > 安全 > Universal Keystore Kit（密钥管理服务） > C API > 结构体 > OH_Huks_PubKeyInfo
category: harmonyos-references
scraped_at: 2026-09-02T15:01:47+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:ef08f876100bba7dd6c016c24561881bf40f385fccba3a607f67f22526413dd2
---

```c
struct OH_Huks_PubKeyInfo {...}
```

## 概述

定义公钥信息的结构体类型。

**起始版本：** 9

**相关模块：** [HuksTypeApi](capi-hukstypeapi.md)

**所在头文件：** [native\_huks\_type.h](capi-native-huks-type-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| enum [OH\_Huks\_KeyAlg](capi-native-huks-type-h.md#oh_huks_keyalg) keyAlg | 公钥的算法类型。 |
| uint32\_t keySize | 公钥的长度，单位：Bit。 |
| uint32\_t nOrXSize | n或X值的长度，单位：Byte。 |
| uint32\_t eOrYSize | e或Y值的长度，单位：Byte。 |
| uint32\_t placeHolder | 占位符的大小，单位：Byte。 |
