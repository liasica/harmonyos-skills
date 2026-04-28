---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_f_i_d_o2___public_key_credential_rp_entity
title: FIDO2_PublicKeyCredentialRpEntity
breadcrumb: API参考 > 系统 > 安全 > Online Authentication Kit（在线认证服务） > C API > 结构体 > FIDO2_PublicKeyCredentialRpEntity
category: harmonyos-references
scraped_at: 2026-04-28T08:07:32+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:31c608fa55427f38c52763bc2f6e1e7037d0c15e0f2ae059ab3e2ddf85e95e76
---

## 概述

创建新凭据时依赖方的属性。

**起始版本：** 6.0.0(20)

**相关模块：** [FIDO2](passkey.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| char \* [id](_f_i_d_o2___public_key_credential_rp_entity.md#id) | 依赖方标识符。 |
| char \* [name](_f_i_d_o2___public_key_credential_rp_entity.md#name) | 依赖方名称。 |

## 结构体成员变量说明

### id

```
1. char* FIDO2_PublicKeyCredentialRpEntity::id
```

**描述**

依赖方标识符。

### name

```
1. char* FIDO2_PublicKeyCredentialRpEntity::name
```

**描述**

依赖方名称。
