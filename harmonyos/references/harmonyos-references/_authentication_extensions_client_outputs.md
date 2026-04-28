---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_authentication_extensions_client_outputs
title: AuthenticationExtensionsClientOutputs
breadcrumb: API参考 > 系统 > 安全 > Online Authentication Kit（在线认证服务） > C API > 结构体 > AuthenticationExtensionsClientOutputs
category: harmonyos-references
scraped_at: 2026-04-28T08:07:28+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:a0158fddf7a900e641dc707610952e667f143cce4854bbf974a2204a2da44f3f
---

## 概述

身份认证扩展输出。

**起始版本：** 6.0.0(20)

**相关模块：** [FIDO2](passkey.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| char \* [placeholder](_authentication_extensions_client_outputs.md#placeholder) | 占位符，表示返回的JSON消息中包含key clientExtensionResults。默认返回NULL。 |

## 结构体成员变量说明

### placeholder

```
1. char* AuthenticationExtensionsClientOutputs::placeholder
```

**描述**

占位符，表示返回的JSON消息中包含"clientExtensionResults"这个key值。该值始终返回NULL。
