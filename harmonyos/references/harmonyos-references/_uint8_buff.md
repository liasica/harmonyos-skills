---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_uint8_buff
title: Uint8Buff
breadcrumb: API参考 > 系统 > 安全 > Online Authentication Kit（在线认证服务） > C API > 结构体 > Uint8Buff
category: harmonyos-references
scraped_at: 2026-09-02T15:01:45+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:61abc3b0067c39ad3628a1bc36127d68db36542c115946f48971758b0a0d41d4
---

## 概述

定义uint8\_t字节流。

**起始版本：** 6.0.0(20)

**相关模块：** [FIDO2（通行密钥服务）](passkey.md)

**所在头文件：** [fido2\_api.h](onlineauthentication_capi_header_fido2.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| uint32\_t [length](_uint8_buff.md#length) | 字节流的长度。 |
| uint8\_t\* [val](_uint8_buff.md#val) | 字节流的值。 |

## 结构体成员变量说明

### length

```cpp
uint32_t Uint8Buff::length
```

**描述**

字节流的长度。

### val

```cpp
uint8_t* Uint8Buff::val
```

**描述**

字节流的值。
