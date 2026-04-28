---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___response_cookies
title: Rcp_ResponseCookies
breadcrumb: API参考 > 系统 > 网络 > Remote Communication Kit（远场通信服务） > C API > 结构体 > Rcp_ResponseCookies
category: harmonyos-references
scraped_at: 2026-04-28T08:09:07+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:62c049fbb47c90a9a71c5b4bde3c391ffc1e8370b0d1011bd3aed485d3676597
---

## 概述

PhonePC/2in1TabletTVWearable

响应Cookie。

**起始版本：** 5.0.0(12)

**相关模块：** [RemoteCommunication](remote-communication-overview.md)

**所在头文件：** [rcp.h](rcp_8h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| char \* [name](_rcp___response_cookies.md#name) | 响应Cookie名称。 |
| char \* [value](_rcp___response_cookies.md#value) | 响应Cookie值。 |
| char \* [domain](_rcp___response_cookies.md#domain) | 响应Cookie域属性。 |
| char \* [path](_rcp___response_cookies.md#path) | 响应Cookie路径属性。 |
| char \* [expires](_rcp___response_cookies.md#expires) | 响应Cookie过期属性。 |
| uint64\_t [maxAge](_rcp___response_cookies.md#maxage) | 响应Cookie maxAge属性。 |
| bool [secure](_rcp___response_cookies.md#secure) | 响应Cookie安全属性。 |
| bool [httpOnly](_rcp___response_cookies.md#httponly) | 响应Cookie httpOnly属性。 |
| char \* [sameSite](_rcp___response_cookies.md#samesite) | 响应Cookie sameSite属性。 |
| uint64\_t [rawSize](_rcp___response_cookies.md#rawsize) | 此响应Cookie的原始大小。 |
| char \* [originString](_rcp___response_cookies.md#originstring) | 原始字符串。 |
| [Rcp\_CookieAttributes](remote-communication-overview.md#rcp_cookieattributes) \* [cookieAttributes](_rcp___response_cookies.md#cookieattributes) | 响应Cookie中的所有属性。 |
| struct [Rcp\_ResponseCookies](_rcp___response_cookies.md) \* [next](_rcp___response_cookies.md#next) | 链式存储。指向下一个[Rcp\_ResponseCookies](_rcp___response_cookies.md)的指针。 |

## 结构体成员变量说明

PhonePC/2in1TabletTVWearable

### cookieAttributes

PhonePC/2in1TabletTVWearable

```
1. Rcp_CookieAttributes* Rcp_ResponseCookies::cookieAttributes
```

**描述**

响应Cookie中的所有属性。

### domain

PhonePC/2in1TabletTVWearable

```
1. char* Rcp_ResponseCookies::domain
```

**描述**

响应Cookie域属性。

### expires

PhonePC/2in1TabletTVWearable

```
1. char* Rcp_ResponseCookies::expires
```

**描述**

响应Cookie过期属性。

### httpOnly

PhonePC/2in1TabletTVWearable

```
1. bool Rcp_ResponseCookies::httpOnly
```

**描述**

响应Cookie httpOnly属性。

### maxAge

PhonePC/2in1TabletTVWearable

```
1. uint64_t Rcp_ResponseCookies::maxAge
```

**描述**

响应Cookie maxAge属性。

### name

PhonePC/2in1TabletTVWearable

```
1. char* Rcp_ResponseCookies::name
```

**描述**

响应Cookie名称。

### next

PhonePC/2in1TabletTVWearable

```
1. struct Rcp_ResponseCookies* Rcp_ResponseCookies::next
```

**描述**

链式存储。指向下一个[Rcp\_ResponseCookies](_rcp___response_cookies.md)的指针。

### originString

PhonePC/2in1TabletTVWearable

```
1. char* Rcp_ResponseCookies::originString
```

**描述**

原始字符串。

### path

PhonePC/2in1TabletTVWearable

```
1. char* Rcp_ResponseCookies::path
```

**描述**

响应Cookie路径属性。

### rawSize

PhonePC/2in1TabletTVWearable

```
1. uint64_t Rcp_ResponseCookies::rawSize
```

**描述**

此响应Cookie的原始大小。

### sameSite

PhonePC/2in1TabletTVWearable

```
1. char* Rcp_ResponseCookies::sameSite
```

**描述**

响应Cookie sameSite属性。

### secure

PhonePC/2in1TabletTVWearable

```
1. bool Rcp_ResponseCookies::secure
```

**描述**

响应Cookie安全属性。

### value

PhonePC/2in1TabletTVWearable

```
1. char* Rcp_ResponseCookies::value
```

**描述**

响应Cookie值。
