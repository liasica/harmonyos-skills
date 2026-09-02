---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___response_cookies
title: Rcp_ResponseCookies
breadcrumb: API参考 > 系统 > 网络 > Remote Communication Kit（远场通信服务） > C API > 结构体 > Rcp_ResponseCookies
category: harmonyos-references
scraped_at: 2026-09-02T15:01:59+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:156459804f6fafa185f011b11763160db90d470bd9657c47c1232c1577095692
---

## 概述

响应Cookie。

**起始版本：** 5.0.0(12)

**相关模块：** [RemoteCommunication](remote-communication-overview.md)

**所在头文件：** [rcp.h](rcp_8h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| char \* [name](_rcp___response_cookies.md#name) | 响应Cookie名称。 |
| char \* [value](_rcp___response_cookies.md#value) | 响应Cookie值。 |
| char \* [domain](_rcp___response_cookies.md#domain) | 响应Cookie域属性。 |
| char \* [path](_rcp___response_cookies.md#path) | 响应Cookie路径属性。 |
| char \* [expires](_rcp___response_cookies.md#expires) | 响应Cookie过期属性。 |
| uint64\_t [maxAge](_rcp___response_cookies.md#maxage) | 响应Cookie maxAge属性。 |
| bool [secure](_rcp___response_cookies.md#secure) | 响应Cookie安全属性。true表示此cookie是通过安全连接返回的，false表示此cookie不是通过安全连接返回的。 |
| bool [httpOnly](_rcp___response_cookies.md#httponly) | 响应Cookie httpOnly属性。true表示不可通过页面脚本等活动内容访问cookie，false表示表示可以通过页面脚本等活动内容访问cookie。 |
| char \* [sameSite](_rcp___response_cookies.md#samesite) | 响应Cookie sameSite属性。 |
| uint64\_t [rawSize](_rcp___response_cookies.md#rawsize) | 此响应Cookie的原始大小。 |
| char \* [originString](_rcp___response_cookies.md#originstring) | 原始字符串。 |
| [Rcp\_CookieAttributes](remote-communication-overview.md#rcp_cookieattributes) \* [cookieAttributes](_rcp___response_cookies.md#cookieattributes) | 响应Cookie中的所有属性。 |
| struct [Rcp\_ResponseCookies](_rcp___response_cookies.md) \* [next](_rcp___response_cookies.md#next) | 链式存储。指向下一个[Rcp\_ResponseCookies](_rcp___response_cookies.md)的指针。 |

## 结构体成员变量说明

### cookieAttributes

```cpp
Rcp_CookieAttributes* Rcp_ResponseCookies::cookieAttributes
```

**描述**

响应Cookie中的所有属性。

### domain

```cpp
char* Rcp_ResponseCookies::domain
```

**描述**

响应Cookie域属性。

### expires

```cpp
char* Rcp_ResponseCookies::expires
```

**描述**

响应Cookie过期属性。

### httpOnly

```cpp
bool Rcp_ResponseCookies::httpOnly
```

**描述**

响应Cookie httpOnly属性。true表示不可通过页面脚本等活动内容访问cookie，false表示表示可以通过页面脚本等活动内容访问cookie。

### maxAge

```cpp
uint64_t Rcp_ResponseCookies::maxAge
```

**描述**

响应Cookie maxAge属性。

### name

```cpp
char* Rcp_ResponseCookies::name
```

**描述**

响应Cookie名称。

### next

```cpp
struct Rcp_ResponseCookies* Rcp_ResponseCookies::next
```

**描述**

链式存储。指向下一个[Rcp\_ResponseCookies](_rcp___response_cookies.md)的指针。

### originString

```cpp
char* Rcp_ResponseCookies::originString
```

**描述**

原始字符串。

### path

```cpp
char* Rcp_ResponseCookies::path
```

**描述**

响应Cookie路径属性。

### rawSize

```cpp
uint64_t Rcp_ResponseCookies::rawSize
```

**描述**

此响应Cookie的原始大小。

### sameSite

```cpp
char* Rcp_ResponseCookies::sameSite
```

**描述**

响应Cookie sameSite属性。

### secure

```cpp
bool Rcp_ResponseCookies::secure
```

**描述**

响应Cookie安全属性。true表示此cookie是通过安全连接返回的，false表示此cookie不是通过安全连接返回的。

### value

```cpp
char* Rcp_ResponseCookies::value
```

**描述**

响应Cookie值。
