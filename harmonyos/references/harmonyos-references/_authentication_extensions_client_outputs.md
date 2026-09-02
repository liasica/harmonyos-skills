---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_authentication_extensions_client_outputs
title: AuthenticationExtensionsClientOutputs
breadcrumb: API参考 > 系统 > 安全 > Online Authentication Kit（在线认证服务） > C API > 结构体 > AuthenticationExtensionsClientOutputs
category: harmonyos-references
scraped_at: 2026-09-02T15:01:45+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:18709b705b9cbcd173a904239d5d0bf6026a797b91cf6b43ff270158d60b89fc
---

## 概述

身份认证扩展输出。

**起始版本：** 6.0.0(20)

**相关模块：** [FIDO2（通行密钥服务）](passkey.md)

**所在头文件：** [fido2\_api.h](onlineauthentication_capi_header_fido2.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| char \* [placeholder](_authentication_extensions_client_outputs.md#placeholder) | 占位符，表示返回的JSON消息中包含key值"clientExtensionResults"。始终返回NULL。 |

## 结构体成员变量说明

### placeholder

```cpp
char* AuthenticationExtensionsClientOutputs::placeholder
```

**描述**

占位符，表示返回的JSON消息中包含"clientExtensionResults"这个key值。该值始终返回NULL。
