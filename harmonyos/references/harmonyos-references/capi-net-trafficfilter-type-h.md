---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-net-trafficfilter-type-h
title: net_trafficfilter_type.h
breadcrumb: API参考 > 系统 > 网络 > Network Kit（网络服务） > C API > 头文件 > net_trafficfilter_type.h
category: harmonyos-references
scraped_at: 2026-09-02T15:01:55+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:8ed65ef7eb2c9885b32d5c6eebae06bb9b7982d34be934a13f226a53f63e3466
---

## 概述

声明网络流量过滤与重定向功能所需的通用类型和错误码。该头文件定义了流量过滤与重定向功能中使用的IP地址、端口、接口等匹配条件结构体，报文过滤规则、重定向规则等配置结构体，以及操作返回的错误码。

适用于调用[OH\_TrafficFilter\_CreateRedirector](capi-net-trafficfilter-h.md#oh_trafficfilter_createredirector)等接口时构造参数和解析返回值。

**引用文件：** <network/netmanager\_ext/net\_trafficfilter\_type.h>

**库：** libnet\_trafficfilter.so

**系统能力：** SystemCapability.Communication.NetManager.NetFirewall

**起始版本：** 26.0.0

**相关模块：** [TrafficFilter](capi-trafficfilter.md)

## 汇总

### 结构体

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [OH\_TrafficFilter\_IPAddress](capi-trafficfilter-oh-trafficfilter-ipaddress.md) | OH\_TrafficFilter\_IPAddress | 二进制形式的IP地址，支持IPv4和IPv6。 |
| [OH\_TrafficFilter\_IPCidr](capi-trafficfilter-oh-trafficfilter-ipcidr.md) | OH\_TrafficFilter\_IPCidr | CIDR（Classless Inter-Domain Routing，无类别域间路由）匹配的IP匹配值。 |
| [OH\_TrafficFilter\_IPRange](capi-trafficfilter-oh-trafficfilter-iprange.md) | OH\_TrafficFilter\_IPRange | 范围匹配的IP匹配值。 |
| [OH\_TrafficFilter\_IPMulti](capi-trafficfilter-oh-trafficfilter-ipmulti.md) | OH\_TrafficFilter\_IPMulti | 多IP匹配的IP匹配值。 |
| [OH\_TrafficFilter\_IPMatch](capi-trafficfilter-oh-trafficfilter-ipmatch.md) | OH\_TrafficFilter\_IPMatch | IP匹配条件。 |
| [OH\_TrafficFilter\_InterfaceMatch](capi-trafficfilter-oh-trafficfilter-interfacematch.md) | OH\_TrafficFilter\_InterfaceMatch | 接口匹配条件。 |
| [OH\_TrafficFilter\_PortRange](capi-trafficfilter-oh-trafficfilter-portrange.md) | OH\_TrafficFilter\_PortRange | 范围匹配的端口匹配值。 |
| [OH\_TrafficFilter\_PortMulti](capi-trafficfilter-oh-trafficfilter-portmulti.md) | OH\_TrafficFilter\_PortMulti | 多端口匹配的端口匹配值。 |
| [OH\_TrafficFilter\_PortMatch](capi-trafficfilter-oh-trafficfilter-portmatch.md) | OH\_TrafficFilter\_PortMatch | 端口匹配条件。 |
| [OH\_TrafficFilter\_ConnectionInfo](capi-trafficfilter-oh-trafficfilter-connectioninfo.md) | OH\_TrafficFilter\_ConnectionInfo | 连接信息结构体。描述一条网络连接的五元组信息（源IP、目的IP、源端口、目的端口、协议类型），用于查询发起该连接的进程信息。初始化规则：调用[OH\_TrafficFilter\_QueryProcess](capi-net-trafficfilter-h.md#oh_trafficfilter_queryprocess)之前，调用者必须将该结构体清零（例如使用memset），然后将[size](capi-trafficfilter-oh-trafficfilter-connectioninfo.md#成员变量)设置为调用者分配的结构体实际大小，通常为sizeof(OH\_TrafficFilter\_ConnectionInfo)。二进制兼容规则（ABI，即应用程序二进制接口，保证新旧版本编译的代码能互相识别结构体布局）：系统通过[size](capi-trafficfilter-oh-trafficfilter-connectioninfo.md#成员变量)来确定哪些字段可以被安全读取。如果[size](capi-trafficfilter-oh-trafficfilter-connectioninfo.md#成员变量)小于当前接口所需的最小大小，接口将返回[OH\_TRAFFICFILTER\_ERROR\_INVALID\_PARAM](capi-net-trafficfilter-type-h.md#oh_trafficfilter_errcode)。如果[size](capi-trafficfilter-oh-trafficfilter-connectioninfo.md#成员变量)大于系统已知的大小，多余的字段将被忽略。 |
| [OH\_TrafficFilter\_ProcessInfo](capi-trafficfilter-oh-trafficfilter-processinfo.md) | OH\_TrafficFilter\_ProcessInfo | 进程信息结构体。存储[OH\_TrafficFilter\_QueryProcess](capi-net-trafficfilter-h.md#oh_trafficfilter_queryprocess)返回的进程信息。初始化规则：调用[OH\_TrafficFilter\_QueryProcess](capi-net-trafficfilter-h.md#oh_trafficfilter_queryprocess)之前，调用者必须将该结构体清零（例如使用memset），然后将[size](capi-trafficfilter-oh-trafficfilter-processinfo.md#成员变量)设置为调用者分配的结构体实际大小，通常为sizeof(OH\_TrafficFilter\_ProcessInfo)。二进制兼容规则（ABI，即应用程序二进制接口，保证新旧版本编译的代码能互相识别结构体布局）：系统通过[size](capi-trafficfilter-oh-trafficfilter-processinfo.md#成员变量)来确定哪些输出字段可以被安全写入。只有被[size](capi-trafficfilter-oh-trafficfilter-processinfo.md#成员变量)完全覆盖的字段才会被系统写入。如果[size](capi-trafficfilter-oh-trafficfilter-processinfo.md#成员变量)小于读取[size](capi-trafficfilter-oh-trafficfilter-processinfo.md#成员变量)字段本身所需的最小大小，接口将返回[OH\_TRAFFICFILTER\_ERROR\_INVALID\_PARAM](capi-net-trafficfilter-type-h.md#oh_trafficfilter_errcode)。如果[size](capi-trafficfilter-oh-trafficfilter-processinfo.md#成员变量)大于系统已知的大小，多余的字段将被忽略。输出有效性规则：当[OH\_TrafficFilter\_QueryProcess](capi-net-trafficfilter-h.md#oh_trafficfilter_queryprocess)返回[OH\_TRAFFICFILTER\_OK](capi-net-trafficfilter-type-h.md#oh_trafficfilter_errcode)时，被[size](capi-trafficfilter-oh-trafficfilter-processinfo.md#成员变量)覆盖的字段包含有效的输出值。当接口返回错误时，调用者不应依赖[size](capi-trafficfilter-oh-trafficfilter-processinfo.md#成员变量)以外的输出字段的值。 |
| [OH\_TrafficFilter\_RedirectRule](capi-trafficfilter-oh-trafficfilter-redirectrule.md) | OH\_TrafficFilter\_RedirectRule | 流量重定向规则。定义TCP流量重定向规则，将匹配的流量重定向到指定的代理服务器。初始化规则：调用[OH\_TrafficFilter\_AddRedirectRule](capi-net-trafficfilter-h.md#oh_trafficfilter_addredirectrule)之前，调用者必须将该结构体清零（例如使用memset），然后将[size](capi-trafficfilter-oh-trafficfilter-redirectrule.md#成员变量)设置为调用者分配的结构体实际大小，通常为sizeof(OH\_TrafficFilter\_RedirectRule)。二进制兼容规则（ABI，即应用程序二进制接口，保证新旧版本编译的代码能互相识别结构体布局）：系统通过[size](capi-trafficfilter-oh-trafficfilter-redirectrule.md#成员变量)来确定哪些字段可以被安全读取。如果[size](capi-trafficfilter-oh-trafficfilter-redirectrule.md#成员变量)小于当前接口所需的最小大小，接口将返回[OH\_TRAFFICFILTER\_ERROR\_INVALID\_PARAM](capi-net-trafficfilter-type-h.md#oh_trafficfilter_errcode)。如果[size](capi-trafficfilter-oh-trafficfilter-redirectrule.md#成员变量)大于系统已知的大小，多余的字段将被忽略。失败规则：如果[OH\_TrafficFilter\_AddRedirectRule](capi-net-trafficfilter-h.md#oh_trafficfilter_addredirectrule)返回错误，不保证规则已被添加或生效。调用者应在假设规则生效之前检查返回值。 |
| [OH\_TrafficFilter\_Redirector](capi-trafficfilter-oh-trafficfilter-redirector.md) | OH\_TrafficFilter\_Redirector | 流量重定向器。 |

### 枚举

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [OH\_TrafficFilter\_ErrCode](capi-net-trafficfilter-type-h.md#oh_trafficfilter_errcode) | OH\_TrafficFilter\_ErrCode | 流量过滤与重定向错误码。 |
| [OH\_TrafficFilter\_IPMatchType](capi-net-trafficfilter-type-h.md#oh_trafficfilter_ipmatchtype) | OH\_TrafficFilter\_IPMatchType | IP匹配类型。 |
| [OH\_TrafficFilter\_IPFamily](capi-net-trafficfilter-type-h.md#oh_trafficfilter_ipfamily) | OH\_TrafficFilter\_IPFamily | IP地址族。 |
| [OH\_TrafficFilter\_PortMatchType](capi-net-trafficfilter-type-h.md#oh_trafficfilter_portmatchtype) | OH\_TrafficFilter\_PortMatchType | 端口匹配类型。 |
| [OH\_TrafficFilter\_HookPoint](capi-net-trafficfilter-type-h.md#oh_trafficfilter_hookpoint) | OH\_TrafficFilter\_HookPoint | 钩子点类型，指定规则在网络协议栈中生效的位置。报文经过内核网络协议栈时会在不同阶段触发钩子点，规则在对应钩子点处对报文进行拦截。例如INPUT链处理进入本机的报文，OUTPUT链处理本机发出的报文。 |

### 宏定义

| 名称 | 描述 |
| --- | --- |
| OH\_TRAFFICFILTER\_IP\_ADDRLEN 16 | IP地址字节数组最大长度（兼容IPv4和IPv6）。  **起始版本：** 26.0.0 |
| OH\_TRAFFICFILTER\_MAX\_MULTI\_IP\_COUNT 16 | 多IP匹配支持的最大IP数量。  **起始版本：** 26.0.0 |
| OH\_TRAFFICFILTER\_MAX\_MULTI\_PORT\_COUNT 64 | 多端口匹配支持的最大端口数量。  **起始版本：** 26.0.0 |
| OH\_TRAFFICFILTER\_NFQUEUE\_COPY\_META 0 | NFQueue报文拷贝模式：仅拷贝元数据。  **起始版本：** 26.0.0 |
| OH\_TRAFFICFILTER\_NFQUEUE\_COPY\_PACKET 0xFFFF | NFQueue报文拷贝模式：拷贝整个报文。  **起始版本：** 26.0.0 |
| OH\_TRAFFICFILTER\_DEFAULT\_COPY\_LEN 0xFFFF | 默认NFQueue报文拷贝长度（字节）。设置为0xFFFF表示拷贝整个报文，较小的值（如128）仅拷贝报文头。  **起始版本：** 26.0.0 |
| OH\_TRAFFICFILTER\_DEFAULT\_QUEUE\_MAXLEN 1024 | 默认NFQueue最大队列长度（报文数量）。  **起始版本：** 26.0.0 |
| OH\_TRAFFICFILTER\_NFQUEUE\_FLAG\_FAIL\_OPEN 0x1 | NFQueue队列标志：FAIL-OPEN模式。当用户态进程崩溃时，内核自动放行报文以避免网络中断。  **起始版本：** 26.0.0 |
| OH\_TRAFFICFILTER\_MIN\_PRIORITY 1 | 最小优先级值。  **起始版本：** 26.0.0 |
| OH\_TRAFFICFILTER\_MAX\_PRIORITY 10000 | 最大优先级值。  **起始版本：** 26.0.0 |
| OH\_TRAFFICFILTER\_MIN\_GROUP\_ID 1 | 最小Group ID值。  **起始版本：** 26.0.0 |
| OH\_TRAFFICFILTER\_MAX\_GROUP\_ID 65535 | 最大Group ID值。  **起始版本：** 26.0.0 |
| OH\_TRAFFICFILTER\_IFNAMSIZ 32 | 网络接口名称最大长度。  **起始版本：** 26.0.0 |
| OH\_TRAFFICFILTER\_PROTO\_ANY 0 | 协议类型常量：任意协议。  **起始版本：** 26.0.0 |
| OH\_TRAFFICFILTER\_PROTO\_TCP 6 | 协议类型常量：TCP协议。  **起始版本：** 26.0.0 |
| OH\_TRAFFICFILTER\_PROTO\_UDP 17 | 协议类型常量：UDP协议。  **起始版本：** 26.0.0 |
| OH\_TRAFFICFILTER\_PROTO\_ICMP 1 | 协议类型常量：ICMP协议。  **起始版本：** 26.0.0 |
| OH\_TRAFFICFILTER\_PROTO\_ICMPV6 58 | 协议类型常量：ICMPV6协议。  **起始版本：** 26.0.0 |

## 枚举类型说明

### OH\_TrafficFilter\_ErrCode

```c
enum OH_TrafficFilter_ErrCode
```

**描述**

流量过滤与重定向错误码。

**起始版本：** 26.0.0

| 枚举项 | 描述 |
| --- | --- |
| OH\_TRAFFICFILTER\_OK = 0 | 操作成功。  **起始版本：** 26.0.0 |
| OH\_TRAFFICFILTER\_E\_BASE = 29410000 | 错误码基值。  **起始版本：** 26.0.0 |
| OH\_TRAFFICFILTER\_ERROR\_PERMISSION\_DENIED = 201 | 缺少权限。  **起始版本：** 26.0.0 |
| OH\_TRAFFICFILTER\_ERROR\_INVALID\_PARAM = (OH\_TRAFFICFILTER\_E\_BASE + 101) | 参数错误（无效的优先级、IP地址、端口或Group ID）。  **起始版本：** 26.0.0 |
| OH\_TRAFFICFILTER\_ERROR\_NOT\_FOUND = (OH\_TRAFFICFILTER\_E\_BASE + 102) | 资源未找到（规则、目标、进程或Group ID未找到）。  **起始版本：** 26.0.0 |
| OH\_TRAFFICFILTER\_ERROR\_TOO\_MANY\_RULES = (OH\_TRAFFICFILTER\_E\_BASE + 103) | 规则数量过多。  **起始版本：** 26.0.0 |
| OH\_TRAFFICFILTER\_ERROR\_GROUP\_ID\_IN\_USE = (OH\_TRAFFICFILTER\_E\_BASE + 104) | Group ID已被占用。  **起始版本：** 26.0.0 |
| OH\_TRAFFICFILTER\_ERROR\_NFQUEUE\_ERROR = (OH\_TRAFFICFILTER\_E\_BASE + 105) | NFQueue错误（初始化失败或无可用队列）。  **起始版本：** 26.0.0 |

### OH\_TrafficFilter\_IPMatchType

```c
enum OH_TrafficFilter_IPMatchType
```

**描述**

IP匹配类型。

**起始版本：** 26.0.0

| 枚举项 | 描述 |
| --- | --- |
| OH\_TRAFFICFILTER\_IP\_MATCH\_ANY = 0 | 任意IP。  **起始版本：** 26.0.0 |
| OH\_TRAFFICFILTER\_IP\_MATCH\_SINGLE = 1 | 单个IP。  **起始版本：** 26.0.0 |
| OH\_TRAFFICFILTER\_IP\_MATCH\_CIDR = 2 | CIDR格式（如192.168.1.0/24，表示匹配该子网内的所有IP）。  **起始版本：** 26.0.0 |
| OH\_TRAFFICFILTER\_IP\_MATCH\_RANGE = 3 | IP范围。  **起始版本：** 26.0.0 |
| OH\_TRAFFICFILTER\_IP\_MATCH\_MULTI = 4 | 多个IP。  **起始版本：** 26.0.0 |

### OH\_TrafficFilter\_IPFamily

```c
enum OH_TrafficFilter_IPFamily
```

**描述**

IP地址族。

**起始版本：** 26.0.0

| 枚举项 | 描述 |
| --- | --- |
| OH\_TRAFFICFILTER\_IP\_FAMILY\_UNSPEC = 0 | 未指定的IP地址族。  **起始版本：** 26.0.0 |
| OH\_TRAFFICFILTER\_IP\_FAMILY\_V4 = 1 | IPv4地址族。  **起始版本：** 26.0.0 |
| OH\_TRAFFICFILTER\_IP\_FAMILY\_V6 = 2 | IPv6地址族。  **起始版本：** 26.0.0 |

### OH\_TrafficFilter\_PortMatchType

```c
enum OH_TrafficFilter_PortMatchType
```

**描述**

端口匹配类型。

**起始版本：** 26.0.0

| 枚举项 | 描述 |
| --- | --- |
| OH\_TRAFFICFILTER\_PORT\_MATCH\_ANY = 0 | 任意端口。  **起始版本：** 26.0.0 |
| OH\_TRAFFICFILTER\_PORT\_MATCH\_SINGLE = 1 | 单个端口。  **起始版本：** 26.0.0 |
| OH\_TRAFFICFILTER\_PORT\_MATCH\_RANGE = 2 | 端口范围。  **起始版本：** 26.0.0 |
| OH\_TRAFFICFILTER\_PORT\_MATCH\_MULTI = 3 | 多个端口。  **起始版本：** 26.0.0 |

### OH\_TrafficFilter\_HookPoint

```c
enum OH_TrafficFilter_HookPoint
```

**描述**

钩子点类型，指定规则在网络协议栈中生效的位置。报文经过内核网络协议栈时会在不同阶段触发钩子点，规则在对应钩子点处对报文进行拦截。例如INPUT链处理进入本机的报文，OUTPUT链处理本机发出的报文。

**起始版本：** 26.0.0

| 枚举项 | 描述 |
| --- | --- |
| OH\_TRAFFICFILTER\_HOOK\_INPUT = 0 | INPUT链，处理进入本机的报文。  **起始版本：** 26.0.0 |
| OH\_TRAFFICFILTER\_HOOK\_OUTPUT = 1 | OUTPUT链，处理本机发出的报文。  **起始版本：** 26.0.0 |
| OH\_TRAFFICFILTER\_HOOK\_FORWARD = 2 | FORWARD链，处理本机转发的报文。  **起始版本：** 26.0.0 |
| OH\_TRAFFICFILTER\_HOOK\_PREROUTING = 3 | PREROUTING链，处理刚到达网卡、尚未路由的报文。  **起始版本：** 26.0.0 |
| OH\_TRAFFICFILTER\_HOOK\_POSTROUTING = 4 | POSTROUTING链，处理即将从网卡发出的报文。  **起始版本：** 26.0.0 |
