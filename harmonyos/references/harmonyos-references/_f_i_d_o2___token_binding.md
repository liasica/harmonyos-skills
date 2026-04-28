---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_f_i_d_o2___token_binding
title: FIDO2_TokenBinding
breadcrumb: API参考 > 系统 > 安全 > Online Authentication Kit（在线认证服务） > C API > 结构体 > FIDO2_TokenBinding
category: harmonyos-references
scraped_at: 2026-04-28T08:07:33+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:487cdd9121f4fbb436d185485c99f0132a05330c0b1e6c4e47371c0dbe71f5ef
---

## 概述

Token binding协议，用于客户端与依赖方通信。

**起始版本：** 6.0.0(20)

**相关模块：** [FIDO2](passkey.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| [FIDO2\_TokenBindingStatus](passkey.md#fido2_tokenbindingstatus-1) [status](_f_i_d_o2___token_binding.md#status) | 客户端的绑定状态。 |
| char \* [id](_f_i_d_o2___token_binding.md#id) | 令牌绑定标识符。 |

## 结构体成员变量说明

### id

```
1. char* FIDO2_TokenBinding::id
```

**描述**

令牌绑定标识符。

### status

```
1. FIDO2_TokenBindingStatus FIDO2_TokenBinding::status
```

**描述**

客户端的绑定状态。
