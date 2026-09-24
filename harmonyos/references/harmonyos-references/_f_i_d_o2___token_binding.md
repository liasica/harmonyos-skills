---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_f_i_d_o2___token_binding
title: FIDO2_TokenBinding
breadcrumb: API参考 > 系统 > 安全 > Online Authentication Kit（在线认证服务） > C API > 结构体 > FIDO2_TokenBinding
category: harmonyos-references
scraped_at: 2026-09-25T07:11:32+08:00
doc_updated_at: 2026-09-24
content_hash: sha256:aa9de707d4ccea70c7fd1c107faff880b91109f1b40176a32c2d9b92aeae9e1d
---

## 概述

Token binding协议，用于客户端与依赖方通信。

**起始版本：** 6.0.0(20)

**相关模块：** [FIDO2（通行密钥服务）](passkey.md)

**所在头文件：** [fido2\_api.h](onlineauthentication_capi_header_fido2.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| [FIDO2\_TokenBindingStatus](passkey.md#fido2_tokenbindingstatus-1) [status](_f_i_d_o2___token_binding.md#status) | 客户端的绑定状态。 |
| char \* [id](_f_i_d_o2___token_binding.md#id) | 令牌绑定标识符。 长度限制0到512。 |

## 结构体成员变量说明

### id

```cpp
char* FIDO2_TokenBinding::id
```

**描述**

令牌绑定标识符。

### status

```cpp
FIDO2_TokenBindingStatus FIDO2_TokenBinding::status
```

**描述**

客户端的绑定状态。
