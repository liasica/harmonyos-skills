---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-net-connection-h
title: net_connection.h
category: harmonyos-references
scraped_at: 2026-04-28T08:08:30+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:809ef9bb4f6d5afefa382714044cb123af047f5f1b371c3c3dc7462fdf6d8096
---

## 概述

PhonePC/2in1TabletTVWearable

为网络管理数据网络连接模块提供C接口。

**引用文件：** <network/netmanager/net\_connection.h>

**库：** libnet\_connection.so

**系统能力：** SystemCapability.Communication.NetManager.Core

**起始版本：** 11

**相关模块：** [NetConnection](capi-netconnection.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 函数

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [int32\_t OH\_NetConn\_HasDefaultNet(int32\_t \*hasDefaultNet)](capi-net-connection-h.md#oh_netconn_hasdefaultnet) | 查询是否有默认激活的数据网络。 |
| [int32\_t OH\_NetConn\_GetDefaultNet(NetConn\_NetHandle \*netHandle)](capi-net-connection-h.md#oh_netconn_getdefaultnet) | 获取激活的默认的数据网络。 |
| [int32\_t OH\_NetConn\_IsDefaultNetMetered(int32\_t \*isMetered)](capi-net-connection-h.md#oh_netconn_isdefaultnetmetered) | 查询默认网络是否按流量计费。 |
| [int32\_t OH\_NetConn\_GetConnectionProperties(NetConn\_NetHandle \*netHandle, NetConn\_ConnectionProperties \*prop)](capi-net-connection-h.md#oh_netconn_getconnectionproperties) | 查询某个数据网络的链路信息。 |
| [int32\_t OH\_NetConn\_GetNetCapabilities(NetConn\_NetHandle \*netHandle, NetConn\_NetCapabilities \*netCapabilities)](capi-net-connection-h.md#oh_netconn_getnetcapabilities) | 查询某个网络的能力集。 |
| [int32\_t OH\_NetConn\_GetDefaultHttpProxy(NetConn\_HttpProxy \*httpProxy)](capi-net-connection-h.md#oh_netconn_getdefaulthttpproxy) | 查询默认的网络代理。 |
| [int32\_t OH\_NetConn\_GetAddrInfo(char \*host, char \*serv, struct addrinfo \*hint, struct addrinfo \*\*res, int32\_t netId)](capi-net-connection-h.md#oh_netconn_getaddrinfo) | 通过netId获取DNS结果。 |
| [int32\_t OH\_NetConn\_FreeDnsResult(struct addrinfo \*res)](capi-net-connection-h.md#oh_netconn_freednsresult) | 释放DNS结果。 |
| [int32\_t OH\_NetConn\_GetAllNets(NetConn\_NetHandleList \*netHandleList)](capi-net-connection-h.md#oh_netconn_getallnets) | 查询所有激活的数据网络。 |
| [int32\_t OHOS\_NetConn\_RegisterDnsResolver(OH\_NetConn\_CustomDnsResolver resolver)](capi-net-connection-h.md#ohos_netconn_registerdnsresolver) | 注册自定义DNS解析器。 |
| [int32\_t OHOS\_NetConn\_UnregisterDnsResolver(void)](capi-net-connection-h.md#ohos_netconn_unregisterdnsresolver) | 取消注册自定义DNS解析器。 |
| [int32\_t OH\_NetConn\_RegisterDnsResolver(OH\_NetConn\_CustomDnsResolver resolver)](capi-net-connection-h.md#oh_netconn_registerdnsresolver) | 注册自定义DNS解析器。 |
| [int32\_t OH\_NetConn\_UnregisterDnsResolver(void)](capi-net-connection-h.md#oh_netconn_unregisterdnsresolver) | 取消注册自定义DNS解析器。 |
| [int32\_t OH\_NetConn\_BindSocket(int32\_t socketFd, NetConn\_NetHandle \*netHandle)](capi-net-connection-h.md#oh_netconn_bindsocket) | 将套接字绑定到特定的网络。 |
| [int32\_t OH\_NetConn\_SetAppHttpProxy(NetConn\_HttpProxy \*httpProxy)](capi-net-connection-h.md#oh_netconn_setapphttpproxy) | 为当前应用设置http代理配置信息。 |
| [int32\_t OH\_NetConn\_RegisterAppHttpProxyCallback(OH\_NetConn\_AppHttpProxyChange appHttpProxyChange, uint32\_t \*callbackId)](capi-net-connection-h.md#oh_netconn_registerapphttpproxycallback) | 注册监听应用http代理变化的回调。 |
| [void OH\_NetConn\_UnregisterAppHttpProxyCallback(uint32\_t callbackId)](capi-net-connection-h.md#oh_netconn_unregisterapphttpproxycallback) | 注销监听应用http代理变化的回调。 |
| [int32\_t OH\_NetConn\_RegisterNetConnCallback(NetConn\_NetSpecifier \*specifier, NetConn\_NetConnCallback \*netConnCallback,uint32\_t timeout, uint32\_t \*callbackId)](capi-net-connection-h.md#oh_netconn_registernetconncallback) | 注册监听网络状态变化的回调。 |
| [int32\_t OH\_NetConn\_RegisterDefaultNetConnCallback(NetConn\_NetConnCallback \*netConnCallback, uint32\_t \*callbackId)](capi-net-connection-h.md#oh_netconn_registerdefaultnetconncallback) | 注册监听默认网络状态变化的回调。 |
| [int32\_t OH\_NetConn\_UnregisterNetConnCallback(uint32\_t callBackId)](capi-net-connection-h.md#oh_netconn_unregisternetconncallback) | 注销监听网络状态变化的回调。 |
| [NetConn\_ErrorCode OH\_NetConn\_SetPacUrl(const char \*pacUrl)](capi-net-connection-h.md#oh_netconn_setpacurl) | 设置系统级代理自动配置（PAC）脚本地址。 |
| [NetConn\_ErrorCode OH\_NetConn\_GetPacUrl(char \*pacUrl)](capi-net-connection-h.md#oh_netconn_getpacurl) | 获取系统级代理自动配置（PAC）脚本地址。 |
| [int32\_t OH\_NetConn\_QueryProbeResult(char \*destination, int32\_t duration, NetConn\_ProbeResultInfo \*probeResultInfo)](capi-net-connection-h.md#oh_netconn_queryproberesult) | 查询网络探测结果。 |
| [int32\_t OH\_NetConn\_QueryTraceRoute(char \*destination, NetConn\_TraceRouteOption \*option,NetConn\_TraceRouteInfo \*traceRouteInfo)](capi-net-connection-h.md#oh_netconn_querytraceroute) | 查询网络跟踪路由。 |

## 函数说明

PhonePC/2in1TabletTVWearable

### OH\_NetConn\_HasDefaultNet()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_NetConn_HasDefaultNet(int32_t *hasDefaultNet)
```

**描述**

查询是否有默认激活的数据网络。

**系统能力：** SystemCapability.Communication.NetManager.Core

**需要权限：** ohos.permission.GET\_NETWORK\_INFO

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| int32\_t \*hasDefaultNet | 是否有默认网络。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 0 - 成功。 201 - 缺少权限。  401 - 参数错误。 2100002 - 无法连接到服务。  2100003 - 内部错误。 |

### OH\_NetConn\_GetDefaultNet()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_NetConn_GetDefaultNet(NetConn_NetHandle *netHandle)
```

**描述**

获取激活的默认的数据网络。

**系统能力：** SystemCapability.Communication.NetManager.Core

**需要权限：** ohos.permission.GET\_NETWORK\_INFO

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [NetConn\_NetHandle](capi-netconnection-netconn-nethandle.md) \*netHandle | 存放网络ID。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 0 - 成功。 201 - 缺少权限。  401 - 参数错误。 2100002 - 无法连接到服务。  2100003 - 内部错误。 |

### OH\_NetConn\_IsDefaultNetMetered()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_NetConn_IsDefaultNetMetered(int32_t *isMetered)
```

**描述**

查询默认数据网络是否计流量。

**系统能力：** SystemCapability.Communication.NetManager.Core

**需要权限：** ohos.permission.GET\_NETWORK\_INFO

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| int32\_t \*isMetered | 是否激活。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 0 - 成功。 201 - 缺少权限。  401 - 参数错误。 2100002 - 无法连接到服务。  2100003 - 内部错误。 |

### OH\_NetConn\_GetConnectionProperties()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_NetConn_GetConnectionProperties(NetConn_NetHandle *netHandle, NetConn_ConnectionProperties *prop)
```

**描述**

查询某个数据网络的链路信息。

**系统能力：** SystemCapability.Communication.NetManager.Core

**需要权限：** ohos.permission.GET\_NETWORK\_INFO

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [NetConn\_NetHandle](capi-netconnection-netconn-nethandle.md) \*netHandle | 存放网络ID。 |
| [NetConn\_ConnectionProperties](capi-netconnection-netconn-connectionproperties.md) \*prop | 存放链路信息。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 0 - 成功。 201 - 缺少权限。  401 - 参数错误。 2100002 - 无法连接到服务。  2100003 - 内部错误。 |

### OH\_NetConn\_GetNetCapabilities()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_NetConn_GetNetCapabilities(NetConn_NetHandle *netHandle, NetConn_NetCapabilities *netCapabilities)
```

**描述**

查询某个网络的能力集。

**系统能力：** SystemCapability.Communication.NetManager.Core

**需要权限：** ohos.permission.GET\_NETWORK\_INFO

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [NetConn\_NetHandle](capi-netconnection-netconn-nethandle.md) \*netHandle | 存放网络ID。 |
| [NetConn\_NetCapabilities](capi-netconnection-netconn-netcapabilities.md) \*netCapabilities | 存放能力集。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 0 - 成功。 201 - 缺少权限。  401 - 参数错误. 2100002 - 无法连接到服务。  2100003 - 内部错误。 |

### OH\_NetConn\_GetDefaultHttpProxy()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_NetConn_GetDefaultHttpProxy(NetConn_HttpProxy *httpProxy)
```

**描述**

查询默认的网络代理。

**系统能力：** SystemCapability.Communication.NetManager.Core

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [NetConn\_HttpProxy](capi-netconnection-netconn-httpproxy.md) \*httpProxy | 存放代理配置信息。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 0 - 成功。 201 - 缺少权限。  401 - 参数错误. 2100002 - 无法连接到服务。  2100003 - 内部错误。 |

### OH\_NetConn\_GetAddrInfo()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_NetConn_GetAddrInfo(char *host, char *serv, struct addrinfo *hint, struct addrinfo **res, int32_t netId)
```

**描述**

通过netId获取DNS结果。

**系统能力：** SystemCapability.Communication.NetManager.Core

**需要权限：** ohos.permission.INTERNET

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| char \*host | 所需查询的host名。 |
| char \*serv | 服务名。 |
| struct addrinfo \*hint | 指向addrinfo结构体的指针。 |
| struct addrinfo \*\*res | 存放DNS查询结果，以链表形式返回。 |
| int32\_t netId | DNS查询netId为0时，使用默认netId查询。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 0 - 成功。 201 - 缺少权限。  401 - 参数错误。 2100002 - 无法连接到服务。  2100003 - 内部错误。 |

### OH\_NetConn\_FreeDnsResult()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_NetConn_FreeDnsResult(struct addrinfo *res)
```

**描述**

释放DNS结果。

**系统能力：** SystemCapability.Communication.NetManager.Core

**需要权限：** ohos.permission.INTERNET

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| struct addrinfo \*res | DNS查询结果链表头。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 0 - 成功。 201 - 缺少权限。  401 - 参数错误。 2100002 - 无法连接到服务。  2100003 - 内部错误。 |

### OH\_NetConn\_GetAllNets()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_NetConn_GetAllNets(NetConn_NetHandleList *netHandleList)
```

**描述**

查询所有激活的数据网络。

**系统能力：** SystemCapability.Communication.NetManager.Core

**需要权限：** ohos.permission.GET\_NETWORK\_INFO

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [NetConn\_NetHandleList](capi-netconnection-netconn-nethandlelist.md) \*netHandleList | 网络信息列表。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 0 - 成功。 201 - 缺少权限。  401 - 参数错误。 2100002 - 无法连接到服务。  2100003 - 内部错误。 |

### OHOS\_NetConn\_RegisterDnsResolver()

PhonePC/2in1TabletTVWearable

```
1. int32_t OHOS_NetConn_RegisterDnsResolver(OH_NetConn_CustomDnsResolver resolver)
```

**描述**

注册自定义DNS解析器。

**系统能力：** SystemCapability.Communication.NetManager.Core

**起始版本：** 11

**废弃版本：** 13

**替代接口：** OH\_NetConn\_RegisterDnsResolver

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_NetConn\_CustomDnsResolver](capi-net-connection-type-h.md#oh_netconn_customdnsresolver) resolver | 指向自定义DNS解析器的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 0 - 成功。 401 - 参数错误。  2100002 - 无法连接到服务。 2100003 - 内部错误。 |

### OHOS\_NetConn\_UnregisterDnsResolver()

PhonePC/2in1TabletTVWearable

```
1. int32_t OHOS_NetConn_UnregisterDnsResolver(void)
```

**描述**

取消注册自定义DNS解析器。

**系统能力：** SystemCapability.Communication.NetManager.Core

**起始版本：** 11

**废弃版本：** 13

**替代接口：** OH\_NetConn\_UnregisterDnsResolver

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 0 - 成功。  2100002 - 无法连接到服务。  2100003 - 内部错误。 |

### OH\_NetConn\_RegisterDnsResolver()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_NetConn_RegisterDnsResolver(OH_NetConn_CustomDnsResolver resolver)
```

**描述**

注册自定义DNS解析器。

**系统能力：** SystemCapability.Communication.NetManager.Core

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_NetConn\_CustomDnsResolver](capi-net-connection-type-h.md#oh_netconn_customdnsresolver) resolver | 指向自定义DNS解析器的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回结果码。  NETMANAGER\_EXT\_SUCCESS 如果操作成功。  NETMANAGER\_ERR\_PARAMETER\_ERROR 参数错误。请输入正确的参数。 |

### OH\_NetConn\_UnregisterDnsResolver()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_NetConn_UnregisterDnsResolver(void)
```

**描述**

取消注册自定义DNS解析器。

**系统能力：** SystemCapability.Communication.NetManager.Core

**起始版本：** 13

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 0 - 成功。  2100002 - 无法连接到服务。  2100003 - 内部错误。 |

### OH\_NetConn\_BindSocket()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_NetConn_BindSocket(int32_t socketFd, NetConn_NetHandle *netHandle)
```

**描述**

将套接字绑定到特定的网络。

**系统能力：** SystemCapability.Communication.NetManager.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| int32\_t socketFd | 由用户构造的套接字。 |
| [NetConn\_NetHandle](capi-netconnection-netconn-nethandle.md) \*netHandle | 指针类型，指向包含网络ID的网络句柄。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 0 - 成功。  401 - 参数错误。  2100002 - 无法连接到服务。  2100003 - 内部错误。 |

### OH\_NetConn\_SetAppHttpProxy()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_NetConn_SetAppHttpProxy(NetConn_HttpProxy *httpProxy)
```

**描述**

为当前应用设置http代理配置信息。

**系统能力：** SystemCapability.Communication.NetManager.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [NetConn\_HttpProxy](capi-netconnection-netconn-httpproxy.md) \*httpProxy | 需要设置的http代理配置信息。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 0 - 成功。  401 - 参数错误。 |

### OH\_NetConn\_RegisterAppHttpProxyCallback()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_NetConn_RegisterAppHttpProxyCallback(OH_NetConn_AppHttpProxyChange appHttpProxyChange, uint32_t *callbackId)
```

**描述**

注册监听应用http代理变化的回调。

**系统能力：** SystemCapability.Communication.NetManager.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_NetConn\_AppHttpProxyChange](capi-net-connection-type-h.md#oh_netconn_apphttpproxychange) appHttpProxyChange | 需要注册的监听回调。 |
| uint32\_t \*callbackId | 回调注册后生成的id, 关联已注册的回调。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 0 - 成功。  401 - 参数错误。 |

### OH\_NetConn\_UnregisterAppHttpProxyCallback()

PhonePC/2in1TabletTVWearable

```
1. void OH_NetConn_UnregisterAppHttpProxyCallback(uint32_t callbackId)
```

**描述**

注销监听应用http代理变化的回调。

**系统能力：** SystemCapability.Communication.NetManager.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| uint32\_t callbackId | 需要被注销的回调所对应的id。 |

### OH\_NetConn\_RegisterNetConnCallback()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_NetConn_RegisterNetConnCallback(NetConn_NetSpecifier *specifier, NetConn_NetConnCallback *netConnCallback,uint32_t timeout, uint32_t *callbackId)
```

**描述**

注册监听网络状态变化的回调。

**系统能力：** SystemCapability.Communication.NetManager.Core

**需要权限：** ohos.permission.GET\_NETWORK\_INFO

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| netSpecifier | 网络特征集。 |
| callback | 注册的回调函数集合。 |
| uint32\_t timeout | 超时时间，单位为毫秒，为0时表示无限等待。 |
| uint32\_t \*callbackId | 出参，对应本次注册成功的回调。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 0 - 成功。  201 - 缺少权限。  401 - 参数错误。  2100002 - 无法连接到服务。  2100003 - 内部错误。  2101008 - 回调已注册。  2101022 - 请求数超出了允许的最大值。 |

### OH\_NetConn\_RegisterDefaultNetConnCallback()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_NetConn_RegisterDefaultNetConnCallback(NetConn_NetConnCallback *netConnCallback, uint32_t *callbackId)
```

**描述**

注册监听默认网络状态变化的回调。

**系统能力：** SystemCapability.Communication.NetManager.Core

**需要权限：** ohos.permission.GET\_NETWORK\_INFO

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| callback | 注册的回调函数集合。 |
| uint32\_t \*callbackId | 出参，对应本次注册成功的回调。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 0 - 成功。  201 - 缺少权限。  401 - 参数错误。  2100002 - 无法连接到服务。  2100003 - 内部错误。  2101008 - 回调已注册。  2101022 - 请求数超出了允许的最大值。 |

### OH\_NetConn\_UnregisterNetConnCallback()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_NetConn_UnregisterNetConnCallback(uint32_t callBackId)
```

**描述**

注销监听网络状态变化的回调。

**系统能力：** SystemCapability.Communication.NetManager.Core

**需要权限：** ohos.permission.GET\_NETWORK\_INFO

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| uint32\_t callBackId | 需要被注销的回调对应ID。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 0 - 成功。  201 - 缺少权限。  401 - 参数错误。  2100002 - 无法连接到服务。  2100003 - 内部错误。  2101007 - 回调不存在。 |

### OH\_NetConn\_SetPacUrl()

PhonePC/2in1TabletTVWearable

```
1. NetConn_ErrorCode OH_NetConn_SetPacUrl(const char *pacUrl)
```

**描述**

设置当前PAC脚本（Proxy Auto-Configuration Script，代理自动配置脚本）的URL地址，比如：http://127.0.0.1:21998/PacProxyScript.pac。通过解析脚本地址可以获取代理信息。

**需要权限：** ohos.permission.SET\_PAC\_URL

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const char \*pacUrl | 需要设置的PAC脚本地址。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [NetConn\_ErrorCode](capi-net-connection-type-h.md#netconn_errorcode) | 结果定义在 [NetConn\_ErrorCode](capi-net-connection-type-h.md#netconn_errorcode)。  [NETCONN\_SUCCESS](capi-net-connection-type-h.md#netconn_errorcode) 成功。  [NETCONN\_PERMISSION\_DENIED](capi-net-connection-type-h.md#netconn_errorcode) 缺少权限。  [NETCONN\_PARAMETER\_ERROR](capi-net-connection-type-h.md#netconn_errorcode) 参数错误。  [NETCONN\_OPERATION\_FAILED](capi-net-connection-type-h.md#netconn_errorcode) 无法连接到服务。  [NETCONN\_INTERNAL\_ERROR](capi-net-connection-type-h.md#netconn_errorcode) 内部错误。 |

### OH\_NetConn\_GetPacUrl()

PhonePC/2in1TabletTVWearable

```
1. NetConn_ErrorCode OH_NetConn_GetPacUrl(char *pacUrl)
```

**描述**

获取系统级代理自动配置（PAC）脚本地址。

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| char \*pacUrl | 获取的PAC脚本地址。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [NetConn\_ErrorCode](capi-net-connection-type-h.md#netconn_errorcode) | 结果定义在 [NetConn\_ErrorCode](capi-net-connection-type-h.md#netconn_errorcode)。  [NETCONN\_SUCCESS](capi-net-connection-type-h.md#netconn_errorcode) 成功。  [NETCONN\_PARAMETER\_ERROR](capi-net-connection-type-h.md#netconn_errorcode) 参数错误。  [NETCONN\_OPERATION\_FAILED](capi-net-connection-type-h.md#netconn_errorcode) 无法连接到服务。  [NETCONN\_INTERNAL\_ERROR](capi-net-connection-type-h.md#netconn_errorcode) 内部错误。 |

### OH\_NetConn\_QueryProbeResult()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_NetConn_QueryProbeResult(char *destination, int32_t duration, NetConn_ProbeResultInfo *probeResultInfo)
```

**描述**

查询网络探测结果。若出现异常（例如断网），导致发送请求失败，则接口会立即返回，不再进行后续探测。本接口涉及网络操作，避免在主流程调用，否则可能导致UI卡顿。

**系统能力：** SystemCapability.Communication.NetManager.Core

**需要权限：** ohos.permission.INTERNET

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| char \*destination | 需要探测的目标域名或者IP地址。对于域名，探测前会进行域名解析，将域名解析为目标IP，之后发起探测。域名解析时间不包含在duration指示的探测持续时间内。 |
| int32\_t duration | 探测持续时间。单位：秒。探测间隔为1秒，因此可通过本字段控制探测次数。 |
| [NetConn\_ProbeResultInfo](capi-netconnection-netconn-proberesultinfo.md) \*probeResultInfo | 丢包率和往返时间（RTT）。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 0 - 成功。  201 - 缺少权限。  401 - 参数错误。  2100003 - 内部错误。 |

### OH\_NetConn\_QueryTraceRoute()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_NetConn_QueryTraceRoute(char *destination, NetConn_TraceRouteOption *option,NetConn_TraceRouteInfo *traceRouteInfo)
```

**描述**

查询网络跟踪路由。

说明

应用调用该接口需申请精确位置权限。根据[申请位置权限开发指导](../harmonyos-guides/location-permission-guidelines.md)，调用方需同时申请ohos.permission.APPROXIMATELY\_LOCATION和ohos.permission.LOCATION。

**需要权限：** ohos.permission.INTERNET、ohos.permission.LOCATION 和 ohos.permission.ACCESS\_NET\_TRACE\_INFO

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| char \*destination | 目的地址。 |
| [NetConn\_TraceRouteOption](capi-netconnection-netconn-tracerouteoption.md) \*option | 路由参数选项。 |
| [NetConn\_TraceRouteInfo](capi-netconnection-netconn-tracerouteinfo.md) \*traceRouteInfo | 路由结果。需传入数组指针，数组大小代表路由跳数，默认30跳。若自定义跳数，则需保证数组大小与option字段中的maxJumpNumber数值保持一致。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 0 - 成功。  201 - 缺少权限。 |
