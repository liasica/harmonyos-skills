---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-net-http-type-h
title: net_http_type.h
breadcrumb: API参考 > 系统 > 网络 > Network Kit（网络服务） > C API > 头文件 > net_http_type.h
category: harmonyos-references
scraped_at: 2026-04-28T08:08:33+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:e635943bdf89743ef92bdb6e17d79170a62d8043f3036535d0113e29572c7d9d
---

## 概述

PhonePC/2in1TabletTVWearable

定义HTTP请求模块的C接口需要的数据结构。

**引用文件：** <network/netstack/net\_http\_type.h>

**库：** libnet\_http.so

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 20

**相关模块：** [netstack](capi-netstack.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 结构体

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [Http\_Buffer](capi-netstack-http-buffer.md) | Http\_Buffer | HTTP缓存结构体。 |
| [Http\_HeaderValue](capi-netstack-http-headervalue.md) | Http\_HeaderValue | 请求或者响应的标头映射的值类型。 |
| [Http\_HeaderEntry](capi-netstack-http-headerentry.md) | Http\_HeaderEntry | 请求或者响应的标头的所有键值对。 |
| [Http\_ClientCert](capi-netstack-http-clientcert.md) | Http\_ClientCert | 发送到服务端的客户端证书配置，服务端将通过客户端证书校验客户端身份。 |
| [Http\_CustomProxy](capi-netstack-http-customproxy.md) | Http\_CustomProxy | 用户自定义代理配置。 |
| [Http\_Proxy](capi-netstack-http-proxy.md) | Http\_Proxy | 代理配置结构体。 |
| [Http\_PerformanceTiming](capi-netstack-http-performancetiming.md) | Http\_PerformanceTiming | HTTP响应时间信息，会在[Http\_Response.performanceTiming](capi-netstack-http-response.md#成员变量)中收集。 |
| [Http\_RequestOptions](capi-netstack-http-requestoptions.md) | Http\_RequestOptions | 定义HTTP请求配置的结构体。 |
| [Http\_Response](capi-netstack-http-response.md) | Http\_Response | 定义HTTP响应的结构体。 |
| [Http\_Request](capi-netstack-http-request.md) | Http\_Request | HTTP请求结构体。 |
| [Http\_EventsHandler](capi-netstack-http-eventshandler.md) | Http\_EventsHandler | 监听不同HTTP事件的回调函数。 |
| [Http\_Headers](capi-netstack-http-headers.md) | Http\_Headers | HTTP请求或者是响应中的标头。 |

### 枚举

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [Http\_ErrCode](capi-net-http-type-h.md#http_errcode) | Http\_ErrCode | 定义HTTP请求的错误码。 |
| [Http\_ResponseCode](capi-net-http-type-h.md#http_responsecode) | Http\_ResponseCode | 定义HTTP响应码。 |
| [Http\_AddressFamilyType](capi-net-http-type-h.md#http_addressfamilytype) | Http\_AddressFamilyType | 定义解析目标域名时限定的地址类型。 |
| [Http\_HttpProtocol](capi-net-http-type-h.md#http_httpprotocol) | Http\_HttpProtocol | HTTP协议版本号枚举定义。 |
| [Http\_CertType](capi-net-http-type-h.md#http_certtype) | Http\_CertType | 证书类型枚举。 |
| [Http\_ProxyType](capi-net-http-type-h.md#http_proxytype) | Http\_ProxyType | 代理配置类型枚举定义。 |

### 宏定义

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| OHOS\_HTTP\_MAX\_PATH\_LEN 128 | HTTP请求最长目录路径长度。  **起始版本：** 20 |
| OHOS\_HTTP\_MAX\_STR\_LEN 256 | HTTP请求最长字符串长度。  **起始版本：** 20 |
| OHOS\_HTTP\_DNS\_SERVER\_NUM\_MAX 3 | HTTP请求最多DNS服务器数量。  **起始版本：** 20 |
| NET\_HTTP\_METHOD\_GET "GET" | HTTP请求GET方法。  **起始版本：** 20 |
| NET\_HTTPMETHOD\_HEAD "HEAD" | HTTP请求HEAD方法。  **起始版本：** 20 |
| NET\_HTTPMETHOD\_OPTIONS "OPTIONS" | HTTP请求OPTIONS方法。  **起始版本：** 20 |
| NET\_HTTPMETHOD\_TRACE "TRACE" | HTTP请求TRACE方法。  **起始版本：** 20 |
| NET\_HTTPMETHOD\_DELETE "DELETE" | HTTP请求DELETE方法。  **起始版本：** 20 |
| NET\_HTTP\_METHOD\_POST "POST" | HTTP请求POST方法。  **起始版本：** 20 |
| NET\_HTTP\_METHOD\_PUT "PUT" | HTTP请求PUT方法。  **起始版本：** 20 |
| NET\_HTTP\_METHOD\_PATCH "CONNECT" | HTTP请求CONNECT方法。  **起始版本：** 20 |

### 函数

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [typedef void (\*Http\_ResponseCallback)(struct Http\_Response \*response, uint32\_t errCode)](capi-net-http-type-h.md#http_responsecallback) | Http\_ResponseCallback | 接收到HTTP响应的回调函数。 |
| [typedef void (\*Http\_OnDataReceiveCallback)(const char \*data, size\_t length)](capi-net-http-type-h.md#http_ondatareceivecallback) | Http\_OnDataReceiveCallback | 接收到数据的回调。 |
| [typedef void (\*Http\_OnProgressCallback)(uint64\_t totalSize, uint64\_t transferredSize)](capi-net-http-type-h.md#http_onprogresscallback) | Http\_OnProgressCallback | 请求/响应数据传输过程中调用的回调函数。 |
| [typedef void (\*Http\_OnHeaderReceiveCallback)(Http\_Headers \*headers)](capi-net-http-type-h.md#http_onheaderreceivecallback) | Http\_OnHeaderReceiveCallback | 收到HTTP响应头的回调函数。 |
| [typedef void (\*Http\_OnVoidCallback)(void)](capi-net-http-type-h.md#http_onvoidcallback) | Http\_OnVoidCallback | 请求的DataEnd或Cancel事件回调的回调函数。 |

## 枚举类型说明

PhonePC/2in1TabletTVWearable

### Http\_ErrCode

PhonePC/2in1TabletTVWearable

```
1. enum Http_ErrCode
```

**描述**

定义HTTP请求的错误码。

**起始版本：** 20

| 枚举项 | 描述 |
| --- | --- |
| OH\_HTTP\_RESULT\_OK = 0 | 请求成功。 |
| OH\_HTTP\_PARAMETER\_ERROR = 401 | 参数错误。 |
| OH\_HTTP\_PERMISSION\_DENIED = 201 | 权限校验失败。 |
| OH\_HTTP\_NETSTACK\_E\_BASE = 2300000 | 基础错误码偏移。 |
| OH\_HTTP\_UNSUPPORTED\_PROTOCOL = (OH\_HTTP\_NETSTACK\_E\_BASE + 1) | 不支持的协议。 |
| OH\_HTTP\_INVALID\_URL = (OH\_HTTP\_NETSTACK\_E\_BASE + 3) | URL格式错误。 |
| OH\_HTTP\_RESOLVE\_PROXY\_FAILED = (OH\_HTTP\_NETSTACK\_E\_BASE + 5) | 代理服务器域名解析失败。 |
| OH\_HTTP\_RESOLVE\_HOST\_FAILED = (OH\_HTTP\_NETSTACK\_E\_BASE + 6) | 域名解析失败。 |
| OH\_HTTP\_CONNECT\_SERVER\_FAILED = (OH\_HTTP\_NETSTACK\_E\_BASE + 7) | 无法连接到服务器。 |
| OH\_HTTP\_INVALID\_SERVER\_RESPONSE = (OH\_HTTP\_NETSTACK\_E\_BASE + 8) | 服务器返回非法数据。 |
| OH\_HTTP\_ACCESS\_REMOTE\_DENIED = (OH\_HTTP\_NETSTACK\_E\_BASE + 9) | 拒绝访问远程资源。 |
| OH\_HTTP\_HTTP2\_FRAMING\_ERROR = (OH\_HTTP\_NETSTACK\_E\_BASE + 16) | HTTP2框架层出现错误。 |
| OH\_HTTP\_TRANSFER\_PARTIAL\_FILE = (OH\_HTTP\_NETSTACK\_E\_BASE + 18) | 传输了部分文件。 |
| OH\_HTTP\_WRITE\_DATA\_FAILED = (OH\_HTTP\_NETSTACK\_E\_BASE + 23) | 无法将接收到的数据写入磁盘或应用程序。 |
| OH\_HTTP\_UPLOAD\_FAILED = (OH\_HTTP\_NETSTACK\_E\_BASE + 25) | 上传失败。 |
| OH\_HTTP\_OPEN\_LOCAL\_DATA\_FAILED = (OH\_HTTP\_NETSTACK\_E\_BASE + 26) | 无法打开或读取文件或应用程序中的本地数据。 |
| OH\_HTTP\_OUT\_OF\_MEMORY = (OH\_HTTP\_NETSTACK\_E\_BASE + 27) | 内存不足。 |
| OH\_HTTP\_OPERATION\_TIMEOUT = (OH\_HTTP\_NETSTACK\_E\_BASE + 28) | 操作超时。 |
| OH\_HTTP\_TOO\_MANY\_REDIRECTIONS = (OH\_HTTP\_NETSTACK\_E\_BASE + 47) | 重定向次数已达到允许的最大值。 |
| OH\_HTTP\_SERVER\_RETURNED\_NOTHING = (OH\_HTTP\_NETSTACK\_E\_BASE + 52) | 服务器没有返回任何内容（没有标头或数据）。 |
| OH\_HTTP\_SEND\_DATA\_FAILED = (OH\_HTTP\_NETSTACK\_E\_BASE + 55) | 发送数据失败。 |
| OH\_HTTP\_RECEIVE\_DATA\_FAILED = (OH\_HTTP\_NETSTACK\_E\_BASE + 56) | 接收数据失败。 |
| OH\_HTTP\_SSL\_CERTIFICATE\_ERROR = (OH\_HTTP\_NETSTACK\_E\_BASE + 58) | 本地SSL证书错误。 |
| OH\_HTTP\_SSL\_CIPHER\_USED\_ERROR = (OH\_HTTP\_NETSTACK\_E\_BASE + 59) | 指定的加密套件不可用。 |
| OH\_HTTP\_INVALID\_SSL\_PEER\_CERT = (OH\_HTTP\_NETSTACK\_E\_BASE + 60) | SSL对等证书或SSH远程密钥无效。 |
| OH\_HTTP\_INVALID\_ENCODING\_FORMAT = (OH\_HTTP\_NETSTACK\_E\_BASE + 61) | HTTP编码格式无效。 |
| OH\_HTTP\_FILE\_TOO\_LARGE = (OH\_HTTP\_NETSTACK\_E\_BASE + 63) | 超出最大文件大小。 |
| OH\_HTTP\_REMOTE\_DISK\_FULL = (OH\_HTTP\_NETSTACK\_E\_BASE + 70) | 远端磁盘满。 |
| OH\_HTTP\_REMOTE\_FILE\_EXISTS = (OH\_HTTP\_NETSTACK\_E\_BASE + 73) | 远端文件已存在。 |
| OH\_HTTP\_SSL\_CA\_NOT\_EXIST = (OH\_HTTP\_NETSTACK\_E\_BASE + 77) | SSL CA证书不存在或无法访问。 |
| OH\_HTTP\_REMOTE\_FILE\_NOT\_FOUND = (OH\_HTTP\_NETSTACK\_E\_BASE + 78) | 远端文件未找到。 |
| OH\_HTTP\_AUTHENTICATION\_ERROR = (OH\_HTTP\_NETSTACK\_E\_BASE + 94) | 身份验证错误。 |
| OH\_HTTP\_ACCESS\_DOMAIN\_NOT\_ALLOWED = (OH\_HTTP\_NETSTACK\_E\_BASE + 998) | 不允许访问该域。 |
| OH\_HTTP\_UNKNOWN\_ERROR = (OH\_HTTP\_NETSTACK\_E\_BASE + 999) | 未知错误。 |

### Http\_ResponseCode

PhonePC/2in1TabletTVWearable

```
1. enum Http_ResponseCode
```

**描述**

定义HTTP响应码。

**起始版本：** 20

| 枚举项 | 描述 |
| --- | --- |
| OH\_HTTP\_OK = 200 | 请求成功。 |
| OH\_HTTP\_CREATED = 201 | 成功请求并创建新资源。 |
| OH\_HTTP\_ACCEPTED = 202 | 请求已被接受但尚未完全处理。 |
| OH\_HTTP\_NON\_AUTHORITATIVE\_INFO = 203 | 请求成功。但是有未授权信息。 |
| OH\_HTTP\_NO\_CONTENT = 204 | 服务器处理成功，但未返回内容。 |
| OH\_HTTP\_RESET = 205 | 重置内容。 |
| OH\_HTTP\_PARTIAL = 206 | 服务器成功处理了部分GET请求。 |
| OH\_HTTP\_MULTI\_CHOICE = 300 | 多种选择。 |
| OH\_HTTP\_MOVED\_PERM = 301 | 请求的资源已永久移动到新的URI，返回信息将包含新的URI。浏览器将自动重定向到新的URI。 |
| OH\_HTTP\_MOVED\_TEMP = 302 | 临时重定向。 |
| OH\_HTTP\_SEE\_OTHER = 303 | 查看其他地址。请求的资源已移动到新的URL，客户端应使用GET方法访问该URL。 |
| OH\_HTTP\_NOT\_MODIFIED = 304 | 请求的资源没有修改。 |
| OH\_HTTP\_USE\_PROXY = 305 | 请求资源需要使用代理访问。 |
| OH\_HTTP\_BAD\_REQUEST = 400 | 服务器无法理解客户端请求的语法错误。 |
| OH\_HTTP\_UNAUTHORIZED = 401 | 请求用户身份验证。 |
| OH\_HTTP\_PAYMENT\_REQUIRED = 402 | 保留以供将来使用。 |
| OH\_HTTP\_FORBIDDEN = 403 | 服务器理解来自请求客户端的请求，但拒绝执行。 |
| OH\_HTTP\_NOT\_FOUND = 404 | 服务器无法根据客户端的请求找到资源。 |
| OH\_HTTP\_BAD\_METHOD = 405 | 客户端请求中的方法被禁止。 |
| OH\_HTTP\_NOT\_ACCEPTABLE = 406 | 服务器无法根据客户端请求的内容特征完成请求。 |
| OH\_HTTP\_PROXY\_AUTH = 407 | 请求验证代理人的身份。 |
| OH\_HTTP\_CLIENT\_TIMEOUT = 408 | 请求耗时太长，超时。 |
| OH\_HTTP\_CONFLICT = 409 | 服务器在完成客户端的PUT请求时可能返回此代码，因为服务器在处理请求时发生冲突。 |
| OH\_HTTP\_GONE = 410 | 客户端请求的资源不再存在。 |
| OH\_HTTP\_LENGTH\_REQUIRED = 411 | 服务器无法处理客户端发送的不带Content Length的请求信息。 |
| OH\_HTTP\_PRECON\_FAILED = 412 | 向客户端请求信息的前提条件不正确。 |
| OH\_HTTP\_ENTITY\_TOO\_LARGE = 413 | 请求被拒绝，因为请求的实体太大，服务器无法处理。 |
| OH\_HTTP\_REQUEST\_TOO\_LONG = 414 | 请求的URI超过了服务器能够解析的长度，服务器无法处理。 |
| OH\_HTTP\_UNSUPPORTED\_TYPE = 415 | 服务器无法处理请求的格式。 |
| OH\_HTTP\_RANGE\_NOT\_MET = 416 | 请求的范围无法满足。 |
| OH\_HTTP\_INTERNAL\_ERROR = 500 | 内部服务器错误，无法完成请求。 |
| OH\_HTTP\_NOT\_IMPLEMENTED = 501 | 服务器不支持请求的功能，无法完成请求。 |
| OH\_HTTP\_BAD\_GATEWAY = 502 | 充当网关或代理的服务器从远程服务器收到无效请求。 |
| OH\_HTTP\_UNAVAILABLE = 503 | 由于超载或系统维护，服务器暂时无法处理客户端请求。 |
| OH\_HTTP\_GATEWAY\_TIMEOUT = 504 | 作为网关的服务器没有及时从远程服务器获取请求。 |
| OH\_HTTP\_VERSION = 505 | 服务器请求的HTTP协议版本。 |

### Http\_AddressFamilyType

PhonePC/2in1TabletTVWearable

```
1. enum Http_AddressFamilyType
```

**描述**

定义解析目标域名时限定的地址类型。

**起始版本：** 20

| 枚举项 | 描述 |
| --- | --- |
| HTTP\_ADDRESS\_FAMILY\_DEFAULT = 0 | 默认值，系统将自行选择目标域名的IPv4地址或IPv6地址。 |
| HTTP\_ADDRESS\_FAMILY\_ONLY\_V4 = 1 | 系统仅解析目标域名的IPv4地址，忽略IPv6地址。 |
| HTTP\_ADDRESS\_FAMILY\_ONLY\_V6 = 2 | 系统仅解析目标域名的IPv6地址，忽略IPv4地址。 |

### Http\_HttpProtocol

PhonePC/2in1TabletTVWearable

```
1. enum Http_HttpProtocol
```

**描述**

HTTP协议版本号枚举定义。

**起始版本：** 20

| 枚举项 | 描述 |
| --- | --- |
| OH\_HTTP\_NONE = 0 | 遵循curl的协议版本选择。 |
| OH\_HTTP1\_1 | HTTP1.1版本。 |
| OH\_HTTP2 | HTTP2版本。 |
| OH\_HTTP3 | HTTP3版本。 |

### Http\_CertType

PhonePC/2in1TabletTVWearable

```
1. enum Http_CertType
```

**描述**

证书类型枚举。

**起始版本：** 20

| 枚举项 | 描述 |
| --- | --- |
| OH\_HTTP\_PEM = 0 | PEM证书类型。 |
| OH\_HTTP\_DER = 1 | DER证书类型。 |
| OH\_HTTP\_P12 = 2 | P12证书类型。 |

### Http\_ProxyType

PhonePC/2in1TabletTVWearable

```
1. enum Http_ProxyType
```

**描述**

代理配置类型枚举定义。

**起始版本：** 20

| 枚举项 | 描述 |
| --- | --- |
| HTTP\_PROXY\_NOT\_USE | 不使用代理。 |
| HTTP\_PROXY\_SYSTEM | 使用系统代理。 |
| HTTP\_PROXY\_CUSTOM | 使用用户自定义代理。 |

## 函数说明

PhonePC/2in1TabletTVWearable

### Http\_ResponseCallback()

PhonePC/2in1TabletTVWearable

```
1. typedef void (*Http_ResponseCallback)(struct Http_Response *response, uint32_t errCode)
```

**描述**

接收到HTTP响应的回调函数。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [struct Http\_Response](capi-netstack-http-response.md) \*response | HTTP响应结构体，指向Http\_Response的指针，参考[Http\_Response](capi-netstack-http-response.md)。 |
| uint32\_t errCode | 响应码。 |

### Http\_OnDataReceiveCallback()

PhonePC/2in1TabletTVWearable

```
1. typedef void (*Http_OnDataReceiveCallback)(const char *data, size_t length)
```

**描述**

接收到数据的回调。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const char \*data | 响应体。 |
| size\_t length | 响应体的长度。 |

### Http\_OnProgressCallback()

PhonePC/2in1TabletTVWearable

```
1. typedef void (*Http_OnProgressCallback)(uint64_t totalSize, uint64_t transferredSize)
```

**描述**

请求/响应数据传输过程中调用的回调函数。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| uint64\_t totalSize | 数据总大小。 |
| uint64\_t transferredSize | 已传输的数据大小。 |

### Http\_OnHeaderReceiveCallback()

PhonePC/2in1TabletTVWearable

```
1. typedef void (*Http_OnHeaderReceiveCallback)(Http_Headers *headers)
```

**描述**

收到HTTP响应头的回调函数。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Http\_Headers](capi-netstack-http-headers.md) \*headers | 接收到的请求头，指向Http\_Headers的指针，参考[Http\_Headers](capi-netstack-http-headers.md)。 |

### Http\_OnVoidCallback()

PhonePC/2in1TabletTVWearable

```
1. typedef void (*Http_OnVoidCallback)(void)
```

**描述**

请求的DataEnd或Cancel事件回调的回调函数。

**起始版本：** 20
