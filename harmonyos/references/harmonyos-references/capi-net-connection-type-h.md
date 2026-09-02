---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-net-connection-type-h
title: net_connection_type.h
breadcrumb: API参考 > 系统 > 网络 > Network Kit（网络服务） > C API > 头文件 > net_connection_type.h
category: harmonyos-references
scraped_at: 2026-09-02T15:01:55+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:43812de01466f9b392c2f00a8b48e7b5b68c175d93d5a2ece0226591f1adb341
---

## 概述

为网络管理数据网络连接模块提供C接口。

**引用文件：** <network/netmanager/net\_connection\_type.h>

**库：** libnet\_connection.so

**系统能力：** SystemCapability.Communication.NetManager.Core

**起始版本：** 11

**相关模块：** [NetConnection](capi-netconnection.md)

## 汇总

### 结构体

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [NetConn\_NetHandle](capi-netconnection-netconn-nethandle.md) | NetConn\_NetHandle | 存放网络ID。 |
| [NetConn\_NetCapabilities](capi-netconnection-netconn-netcapabilities.md) | NetConn\_NetCapabilities | 网络能力集。 |
| [NetConn\_NetAddr](capi-netconnection-netconn-netaddr.md) | NetConn\_NetAddr | 网络地址。 |
| [NetConn\_Route](capi-netconnection-netconn-route.md) | NetConn\_Route | 路由配置信息。 |
| [NetConn\_HttpProxy](capi-netconnection-netconn-httpproxy.md) | NetConn\_HttpProxy | 代理配置信息。 |
| [NetConn\_ConnectionProperties](capi-netconnection-netconn-connectionproperties.md) | NetConn\_ConnectionProperties | 网络连接信息。 |
| [NetConn\_NetHandleList](capi-netconnection-netconn-nethandlelist.md) | NetConn\_NetHandleList | 网络列表。 |
| [NetConn\_NetSpecifier](capi-netconnection-netconn-netspecifier.md) | NetConn\_NetSpecifier | 网络的特征集。 |
| [NetConn\_NetConnCallback](capi-netconnection-netconn-netconncallback.md) | NetConn\_NetConnCallback | 网络状态监听回调集合。 |
| [NetConn\_ProbeResultInfo](capi-netconnection-netconn-proberesultinfo.md) | NetConn\_ProbeResultInfo | 定义探测结果信息。 |
| [NetConn\_TraceRouteOption](capi-netconnection-netconn-tracerouteoption.md) | NetConn\_TraceRouteOption | 定义网络跟踪路由选项。 |
| [NetConn\_TraceRouteInfo](capi-netconnection-netconn-tracerouteinfo.md) | NetConn\_TraceRouteInfo | 定义跟踪路由信息。 |

### 枚举

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [NetConn\_NetCap](capi-net-connection-type-h.md#netconn_netcap) | NetConn\_NetCap | 网络能力集。 |
| [NetConn\_NetBearerType](capi-net-connection-type-h.md#netconn_netbearertype) | NetConn\_NetBearerType | 网络载体类型。 |
| [NetConn\_ErrorCode](capi-net-connection-type-h.md#netconn_errorcode) | NetConn\_ErrorCode | 网络连接返回值错误码。 |
| [NetConn\_PacketsType](capi-net-connection-type-h.md#netconn_packetstype) | NetConn\_PacketsType | 枚举跟踪路由的数据包类型。 |

### 宏定义

| 名称 | 描述 |
| --- | --- |
| NETCONN\_MAX\_NET\_SIZE 32 | [NetConn\_NetHandleList](capi-netconnection-netconn-nethandlelist.md)的成员变量netHandles数组的长度。  **起始版本：** 11 |
| NETCONN\_MAX\_BEARER\_TYPE\_SIZE 32 | [NetConn\_NetCapabilities](capi-netconnection-netconn-netcapabilities.md)的成员变量bearerTypes数组的长度。  **起始版本：** 11 |
| NETCONN\_MAX\_CAP\_SIZE 32 | [NetConn\_NetCapabilities](capi-netconnection-netconn-netcapabilities.md)的成员变量netCaps数组的长度。  **起始版本：** 11 |
| NETCONN\_MAX\_ADDR\_SIZE 32 | [NetConn\_ConnectionProperties](capi-netconnection-netconn-connectionproperties.md)的成员变量netAddrList、dnsList数组的长度。  **起始版本：** 11 |
| NETCONN\_MAX\_ROUTE\_SIZE 64 | [NetConn\_ConnectionProperties](capi-netconnection-netconn-connectionproperties.md)的成员变量routeList数组的长度。  **起始版本：** 11 |
| NETCONN\_MAX\_EXCLUSION\_SIZE 256 | [NetConn\_HttpProxy](capi-netconnection-netconn-httpproxy.md)的成员变量exclusionList数组的长度。  **起始版本：** 11 |
| NETCONN\_MAX\_STR\_LEN 256 | [NetConn\_HttpProxy](capi-netconnection-netconn-httpproxy.md)的成员变量host数组的长度。  **起始版本：** 11 |
| NETCONN\_MAX\_RTT\_NUM 4 | [NetConn\_ProbeResultInfo](capi-netconnection-netconn-proberesultinfo.md)的成员变量rtt数组的长度。  **起始版本：** 20 |

### 函数

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [typedef int (\*OH\_NetConn\_CustomDnsResolver)(const char \*host, const char \*serv,const struct addrinfo \*hint, struct addrinfo \*\*res)](capi-net-connection-type-h.md#oh_netconn_customdnsresolver) | OH\_NetConn\_CustomDnsResolver | 指向自定义DNS解析器的指针。 |
| [typedef void (\*OH\_NetConn\_AppHttpProxyChange)(NetConn\_HttpProxy \*proxy)](capi-net-connection-type-h.md#oh_netconn_apphttpproxychange) | OH\_NetConn\_AppHttpProxyChange | 应用的http代理信息变化回调。 |
| [typedef void (\*OH\_NetConn\_NetworkAvailable)(NetConn\_NetHandle \*netHandle)](capi-net-connection-type-h.md#oh_netconn_networkavailable) | OH\_NetConn\_NetworkAvailable | 网络可用回调。 |
| [typedef void (\*OH\_NetConn\_NetCapabilitiesChange)(NetConn\_NetHandle \*netHandle,NetConn\_NetCapabilities \*netCapabilities)](capi-net-connection-type-h.md#oh_netconn_netcapabilitieschange) | OH\_NetConn\_NetCapabilitiesChange | 网络能力集变更回调。 |
| [typedef void (\*OH\_NetConn\_NetConnectionPropertiesChange)(NetConn\_NetHandle \*netHandle,NetConn\_ConnectionProperties \*connConnetionProperties)](capi-net-connection-type-h.md#oh_netconn_netconnectionpropertieschange) | OH\_NetConn\_NetConnectionPropertiesChange | 网络连接属性变更回调。 |
| [typedef void (\*OH\_NetConn\_GlobalHttpProxyRefreshCallback)(int32\_t result, const NetConn\_HttpProxy \*proxy, void \*userContext)](capi-net-connection-type-h.md#oh_netconn_globalhttpproxyrefreshcallback) | OH\_NetConn\_GlobalHttpProxyRefreshCallback | 全局HTTP代理重新认证结果的回调。 |
| [typedef void (\*OH\_NetConn\_NetLost)(NetConn\_NetHandle \*netHandle)](capi-net-connection-type-h.md#oh_netconn_netlost) | OH\_NetConn\_NetLost | 网络断开回调。 |
| [typedef void (\*OH\_NetConn\_NetUnavailable)(void)](capi-net-connection-type-h.md#oh_netconn_netunavailable) | OH\_NetConn\_NetUnavailable | 网络不可用回调，在指定的超时时间内网络未激活时触发该回调，如果未设置超时时间则不会触发该回调。 |
| [typedef void (\*OH\_NetConn\_NetBlockStatusChange)(NetConn\_NetHandle \*netHandle, bool blocked)](capi-net-connection-type-h.md#oh_netconn_netblockstatuschange) | OH\_NetConn\_NetBlockStatusChange | 网络阻塞状态变更回调。 |

## 枚举类型说明

### NetConn\_NetCap

```c
enum NetConn_NetCap
```

**描述**

网络能力集。

**起始版本：** 11

| 枚举项 | 描述 |
| --- | --- |
| NETCONN\_NET\_CAPABILITY\_MMS = 0 | MMS |
| NETCONN\_NET\_CAPABILITY\_NOT\_METERED = 11 | 非计量网络 |
| NETCONN\_NET\_CAPABILITY\_INTERNET = 12 | Internet |
| NETCONN\_NET\_CAPABILITY\_NOT\_VPN = 15 | 非VPN |
| NETCONN\_NET\_CAPABILITY\_VALIDATED = 16 | 已验证 |
| NETCONN\_NET\_CAPABILITY\_PORTAL = 17 | Portal  **起始版本：** 12 |
| NETCONN\_NET\_CAPABILITY\_CHECKING\_CONNECTIVITY = 31 | 检测连通性中。  **起始版本：** 12 |

### NetConn\_NetBearerType

```c
enum NetConn_NetBearerType
```

**描述**

网络载体类型。

**起始版本：** 11

| 枚举项 | 描述 |
| --- | --- |
| NETCONN\_BEARER\_CELLULAR = 0 | 蜂窝网络 |
| NETCONN\_BEARER\_WIFI = 1 | WIFI |
| NETCONN\_BEARER\_BLUETOOTH = 2 | 蓝牙  **起始版本：** 12 |
| NETCONN\_BEARER\_ETHERNET = 3 | Ethernet |
| NETCONN\_BEARER\_VPN = 4 | VPN  **起始版本：** 12 |

### NetConn\_ErrorCode

```c
enum NetConn_ErrorCode
```

**描述**

网络连接返回值错误码。

**起始版本：** 15

| 枚举项 | 描述 |
| --- | --- |
| NETCONN\_SUCCESS = 0 | 成功 |
| NETCONN\_PERMISSION\_DENIED = 201 | 缺少权限 |
| NETCONN\_PARAMETER\_ERROR = 401 | 参数错误 |
| NETCONN\_OPERATION\_FAILED = 2100002 | 无法连接到服务 |
| NETCONN\_INTERNAL\_ERROR = 2100003 | 内部错误。1. 内存异常，比如内存不足或内存拷贝失败。2. 空指针，比如访问已释放内存的指针。 |

### NetConn\_PacketsType

```c
enum NetConn_PacketsType
```

**描述**

枚举跟踪路由的数据包类型。

**起始版本：** 20

| 枚举项 | 描述 |
| --- | --- |
| NETCONN\_PACKETS\_ICMP = 0 | 互联网控制消息协议。 |
| NETCONN\_PACKETS\_UDP = 1 | 用户数据报协议。 |

## 函数说明

### OH\_NetConn\_CustomDnsResolver()

```c
typedef int (*OH_NetConn_CustomDnsResolver)(const char *host, const char *serv,const struct addrinfo *hint, struct addrinfo **res)
```

**描述**

指向自定义DNS解析器的指针。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const char \*host | 要查询的主机名。 |
| const char \*serv | 服务名称。 |
| const struct addrinfo \*hint | 指向addrinfo结构的指针。 |
| struct addrinfo \*\*res | 存储DNS查询结果并以链表形式返回。 |

### OH\_NetConn\_AppHttpProxyChange()

```c
typedef void (*OH_NetConn_AppHttpProxyChange)(NetConn_HttpProxy *proxy)
```

**描述**

应用的http代理信息变化回调。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [NetConn\_HttpProxy](capi-netconnection-netconn-httpproxy.md) \*proxy | 变化的代理配置信息，可能是空指针。 |

### OH\_NetConn\_GlobalHttpProxyRefreshCallback()

```c
typedef void (*OH_NetConn_GlobalHttpProxyRefreshCallback)(int32_t result, const NetConn_HttpProxy *proxy, void *userContext)
```

**描述**

全局HTTP代理重新认证结果的回调。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| (int32\_t result | 重新认证的结果。0表示成功，其他值表示失败。 |
| [const NetConn\_HttpProxy](capi-netconnection-netconn-httpproxy.md) \*proxy | 当重新认证成功（result为0）时，表示刷新后的全局HTTP代理信息。如果重新认证失败（result非0）时，proxy为NULL。该proxy对象由系统持有，仅在该回调函数内部有效。调用者不得释放或修改它。如果调用者需要在回调返回后继续使用该代理信息，必须进行深拷贝。 |
| void \*userContext | 用户自定义数据。系统不会访问、拷贝或释放该数据。 |

### OH\_NetConn\_NetworkAvailable()

```c
typedef void (*OH_NetConn_NetworkAvailable)(NetConn_NetHandle *netHandle)
```

**描述**

网络可用回调。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [NetConn\_NetHandle](capi-netconnection-netconn-nethandle.md) \*netHandle | 网络句柄。 |

### OH\_NetConn\_NetCapabilitiesChange()

```c
typedef void (*OH_NetConn_NetCapabilitiesChange)(NetConn_NetHandle *netHandle,NetConn_NetCapabilities *netCapabilities)
```

**描述**

网络能力集变更回调。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [NetConn\_NetHandle](capi-netconnection-netconn-nethandle.md) \*netHandle | 网络句柄。 |
| [NetConn\_NetCapabilities](capi-netconnection-netconn-netcapabilities.md) \*netCapabilities | 网络能力集。 |

### OH\_NetConn\_NetConnectionPropertiesChange()

```c
typedef void (*OH_NetConn_NetConnectionPropertiesChange)(NetConn_NetHandle *netHandle,NetConn_ConnectionProperties *connConnetionProperties)
```

**描述**

网络连接属性变更回调。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [NetConn\_NetHandle](capi-netconnection-netconn-nethandle.md) \*netHandle | 网络句柄。 |
| [NetConn\_ConnectionProperties](capi-netconnection-netconn-connectionproperties.md) \*connConnetionProperties | 网络连接属性。 |

### OH\_NetConn\_NetLost()

```c
typedef void (*OH_NetConn_NetLost)(NetConn_NetHandle *netHandle)
```

**描述**

网络断开回调。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [NetConn\_NetHandle](capi-netconnection-netconn-nethandle.md) \*netHandle | 网络句柄。 |

### OH\_NetConn\_NetUnavailable()

```c
typedef void (*OH_NetConn_NetUnavailable)(void)
```

**描述**

网络不可用回调，在指定的超时时间内网络未激活时触发该回调，如果未设置超时时间则不会触发该回调。

**起始版本：** 12

### OH\_NetConn\_NetBlockStatusChange()

```c
typedef void (*OH_NetConn_NetBlockStatusChange)(NetConn_NetHandle *netHandle, bool blocked)
```

**描述**

网络阻塞状态变更回调。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [NetConn\_NetHandle](capi-netconnection-netconn-nethandle.md) \*netHandle | 网络句柄。 |
| bool blocked | 指示网络是否将被阻塞的标志。true表示网络被阻塞，false表示网络未被阻塞。 |
