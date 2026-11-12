---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-net-trafficfilter-h
title: net_trafficfilter.h
breadcrumb: API参考 > 系统 > 网络 > Network Kit（网络服务） > C API > 头文件 > net_trafficfilter.h
category: harmonyos-references
scraped_at: 2026-11-12T09:55:42+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:182592c8664ed81f821b93d12ead46a05a4f65f43f2438e969cb8a48e5973060
---

## 概述

声明网络流量过滤与重定向功能的C接口。该头文件提供创建和销毁报文控制器、注册报文回调、添加和清除过滤规则，以及创建和销毁流量重定向器、添加和清除重定向规则的接口。

适用于需要在系统层面对网络数据包进行拦截、过滤和重定向的应用场景。

**引用文件：** <network/netmanager\_ext/net\_trafficfilter.h>

**库：** libnet\_trafficfilter.so

**系统能力：** SystemCapability.Communication.NetManager.NetFirewall

**起始版本：** 26.0.0

**相关模块：** [TrafficFilter](capi-trafficfilter.md)

## 汇总

### 函数

| 名称 | 描述 |
| --- | --- |
| [int32\_t OH\_TrafficFilter\_CreateRedirector(uint32\_t group\_id, uint32\_t priority, OH\_TrafficFilter\_Redirector\*\* redirector)](capi-net-trafficfilter-h.md#oh_trafficfilter_createredirector) | 创建流量重定向实例，用于将TCP流量重定向到代理服务器。资源管理：必须调用[OH\_TrafficFilter\_DestroyRedirector](capi-net-trafficfilter-h.md#oh_trafficfilter_destroyredirector)释放资源。如果该函数失败，不会返回有效的重定向器。 |
| [int32\_t OH\_TrafficFilter\_DestroyRedirector(OH\_TrafficFilter\_Redirector\* redirector)](capi-net-trafficfilter-h.md#oh_trafficfilter_destroyredirector) | 销毁重定向实例并释放相关资源（包括规则），调用后句柄将失效。 |
| [int32\_t OH\_TrafficFilter\_AddRedirectRule(OH\_TrafficFilter\_Redirector\* redirector, const OH\_TrafficFilter\_RedirectRule\* rule)](capi-net-trafficfilter-h.md#oh_trafficfilter_addredirectrule) | 添加TCP流量重定向规则，将匹配的流量重定向到指定的代理服务器。如需清除重定向规则，需要调用[OH\_TrafficFilter\_ClearRedirectRule](capi-net-trafficfilter-h.md#oh_trafficfilter_clearredirectrule)。 |
| [int32\_t OH\_TrafficFilter\_ClearRedirectRule(OH\_TrafficFilter\_Redirector\* redirector)](capi-net-trafficfilter-h.md#oh_trafficfilter_clearredirectrule) | 清除所有重定向规则。 |
| [int32\_t OH\_TrafficFilter\_QueryProcess(const OH\_TrafficFilter\_ConnectionInfo\* connection\_info, OH\_TrafficFilter\_ProcessInfo\* process\_info)](capi-net-trafficfilter-h.md#oh_trafficfilter_queryprocess) | 根据网络连接信息查询对应的进程信息。通过源IP、目的IP、源端口、目的端口和协议类型组成的五元组连接信息，查询发起该连接的进程信息。 |
| [int32\_t OH\_TrafficFilter\_CreatePacketController(uint32\_t groupId, uint32\_t priority, const OH\_TrafficFilter\_Config\* config, OH\_TrafficFilter\_PacketController\*\* controller)](capi-net-trafficfilter-h.md#oh_trafficfilter_createpacketcontroller) | 创建报文控制器实例，用于拦截和过滤网络报文。资源管理：必须调用[OH\_TrafficFilter\_DestroyPacketController](capi-net-trafficfilter-h.md#oh_trafficfilter_destroypacketcontroller)释放资源。如果该函数失败，不会返回有效的控制器。 |
| [int32\_t OH\_TrafficFilter\_DestroyPacketController(OH\_TrafficFilter\_PacketController\* controller)](capi-net-trafficfilter-h.md#oh_trafficfilter_destroypacketcontroller) | 销毁报文控制器实例并释放相关资源（包括规则），调用后句柄将失效。 |
| [int32\_t OH\_TrafficFilter\_RegisterPacketCallback(OH\_TrafficFilter\_PacketController\* controller, OH\_TrafficFilter\_PacketCallback callback, void\* userData)](capi-net-trafficfilter-h.md#oh_trafficfilter_registerpacketcallback) | 注册一个回调函数用于处理拦截到的报文，当报文匹配到过滤规则时，将触发该回调。 |
| [int32\_t OH\_TrafficFilter\_UnregisterPacketCallback(OH\_TrafficFilter\_PacketController\* controller)](capi-net-trafficfilter-h.md#oh_trafficfilter_unregisterpacketcallback) | 注销报文回调函数。 |
| [int32\_t OH\_TrafficFilter\_AddPacketRule(OH\_TrafficFilter\_PacketController\* controller, const OH\_TrafficFilter\_FilterRule\* rule)](capi-net-trafficfilter-h.md#oh_trafficfilter_addpacketrule) | 添加报文过滤规则，当报文匹配到该规则时，将触发报文回调。如需清除过滤规则，需要调用[OH\_TrafficFilter\_ClearPacketRule](capi-net-trafficfilter-h.md#oh_trafficfilter_clearpacketrule)。 |
| [int32\_t OH\_TrafficFilter\_ClearPacketRule(OH\_TrafficFilter\_PacketController\* controller)](capi-net-trafficfilter-h.md#oh_trafficfilter_clearpacketrule) | 清除报文过滤规则。 |

## 函数说明

### OH\_TrafficFilter\_CreateRedirector()

```c
int32_t OH_TrafficFilter_CreateRedirector(uint32_t group_id, uint32_t priority, OH_TrafficFilter_Redirector** redirector)
```

**描述**

创建流量重定向实例，用于将TCP流量重定向到代理服务器。资源管理：必须调用[OH\_TrafficFilter\_DestroyRedirector](capi-net-trafficfilter-h.md#oh_trafficfilter_destroyredirector)释放资源。如果该函数失败，不会返回有效的重定向器。

**需要权限：** ohos.permission.kernel.TRAFFIC\_FILTER

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| uint32\_t group\_id | 重定向链标识符。这是应用内的逻辑分组ID。同一应用内的多个重定向器可以使用不同的group\_id。不同应用的相同group\_id会自动隔离。有效范围为[[OH\_TRAFFICFILTER\_MIN\_GROUP\_ID](capi-net-trafficfilter-type-h.md#宏定义), [OH\_TRAFFICFILTER\_MAX\_GROUP\_ID](capi-net-trafficfilter-type-h.md#宏定义)]，包含两个边界。如果group\_id超出此范围，该函数返回[OH\_TRAFFICFILTER\_ERROR\_INVALID\_PARAM](capi-net-trafficfilter-type-h.md#oh_trafficfilter_errcode)。 |
| uint32\_t priority | 优先级。决定不同group\_id链之间的执行顺序，数值越小越先执行。注意：重定向器优先级高于报文过滤器优先级。有效范围为[[OH\_TRAFFICFILTER\_MIN\_PRIORITY](capi-net-trafficfilter-type-h.md#宏定义), [OH\_TRAFFICFILTER\_MAX\_PRIORITY](capi-net-trafficfilter-type-h.md#宏定义)]，包含两个边界。如果priority超出此范围，该函数返回[OH\_TRAFFICFILTER\_ERROR\_INVALID\_PARAM](capi-net-trafficfilter-type-h.md#oh_trafficfilter_errcode)。 |
| [OH\_TrafficFilter\_Redirector\*\*](capi-trafficfilter-oh-trafficfilter-redirector.md) redirector | 出参，成功时为重定向句柄。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | [OH\_TRAFFICFILTER\_OK](capi-net-trafficfilter-type-h.md#oh_trafficfilter_errcode) - 成功。  [OH\_TRAFFICFILTER\_ERROR\_PERMISSION\_DENIED](capi-net-trafficfilter-type-h.md#oh_trafficfilter_errcode) - 缺少权限。  [OH\_TRAFFICFILTER\_ERROR\_GROUP\_ID\_IN\_USE](capi-net-trafficfilter-type-h.md#oh_trafficfilter_errcode) - group\_id已存在。  [OH\_TRAFFICFILTER\_ERROR\_INVALID\_PARAM](capi-net-trafficfilter-type-h.md#oh_trafficfilter_errcode) - 参数错误。 |

### OH\_TrafficFilter\_DestroyRedirector()

```c
int32_t OH_TrafficFilter_DestroyRedirector(OH_TrafficFilter_Redirector* redirector)
```

**描述**

销毁重定向实例并释放相关资源（包括规则），调用后句柄将失效。

**需要权限：** ohos.permission.kernel.TRAFFIC\_FILTER

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_TrafficFilter\_Redirector](capi-trafficfilter-oh-trafficfilter-redirector.md)\* redirector | OH\_TrafficFilter\_Redirector句柄。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | [OH\_TRAFFICFILTER\_OK](capi-net-trafficfilter-type-h.md#oh_trafficfilter_errcode) - 成功。  [OH\_TRAFFICFILTER\_ERROR\_PERMISSION\_DENIED](capi-net-trafficfilter-type-h.md#oh_trafficfilter_errcode) - 缺少权限。  [OH\_TRAFFICFILTER\_ERROR\_INVALID\_PARAM](capi-net-trafficfilter-type-h.md#oh_trafficfilter_errcode) - redirector为NULL。  [OH\_TRAFFICFILTER\_ERROR\_NOT\_FOUND](capi-net-trafficfilter-type-h.md#oh_trafficfilter_errcode) - 未找到指定的重定向器句柄。 |

### OH\_TrafficFilter\_AddRedirectRule()

```c
int32_t OH_TrafficFilter_AddRedirectRule(OH_TrafficFilter_Redirector* redirector, const OH_TrafficFilter_RedirectRule* rule)
```

**描述**

添加TCP流量重定向规则，将匹配的流量重定向到指定的代理服务器。如需清除重定向规则，需要调用[OH\_TrafficFilter\_ClearRedirectRule](capi-net-trafficfilter-h.md#oh_trafficfilter_clearredirectrule)。

**需要权限：** ohos.permission.kernel.TRAFFIC\_FILTER

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_TrafficFilter\_Redirector](capi-trafficfilter-oh-trafficfilter-redirector.md)\* redirector | OH\_TrafficFilter\_Redirector句柄。 |
| [const OH\_TrafficFilter\_RedirectRule](capi-trafficfilter-oh-trafficfilter-redirectrule.md)\* rule | 重定向规则。不能为NULL。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | [OH\_TRAFFICFILTER\_OK](capi-net-trafficfilter-type-h.md#oh_trafficfilter_errcode) - 成功。  [OH\_TRAFFICFILTER\_ERROR\_PERMISSION\_DENIED](capi-net-trafficfilter-type-h.md#oh_trafficfilter_errcode) - 缺少权限。  [OH\_TRAFFICFILTER\_ERROR\_INVALID\_PARAM](capi-net-trafficfilter-type-h.md#oh_trafficfilter_errcode) - redirector或rule为NULL。  [OH\_TRAFFICFILTER\_ERROR\_TOO\_MANY\_RULES](capi-net-trafficfilter-type-h.md#oh_trafficfilter_errcode) - 添加的规则过多。 |

### OH\_TrafficFilter\_ClearRedirectRule()

```c
int32_t OH_TrafficFilter_ClearRedirectRule(OH_TrafficFilter_Redirector* redirector)
```

**描述**

清除所有重定向规则。

**需要权限：** ohos.permission.kernel.TRAFFIC\_FILTER

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_TrafficFilter\_Redirector](capi-trafficfilter-oh-trafficfilter-redirector.md)\* redirector | OH\_TrafficFilter\_Redirector句柄。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | [OH\_TRAFFICFILTER\_OK](capi-net-trafficfilter-type-h.md#oh_trafficfilter_errcode) - 成功。  [OH\_TRAFFICFILTER\_ERROR\_PERMISSION\_DENIED](capi-net-trafficfilter-type-h.md#oh_trafficfilter_errcode) - 缺少权限。  [OH\_TRAFFICFILTER\_ERROR\_INVALID\_PARAM](capi-net-trafficfilter-type-h.md#oh_trafficfilter_errcode) - redirector为NULL。 |

### OH\_TrafficFilter\_QueryProcess()

```c
int32_t OH_TrafficFilter_QueryProcess(const OH_TrafficFilter_ConnectionInfo* connection_info, OH_TrafficFilter_ProcessInfo* process_info)
```

**描述**

根据网络连接信息查询对应的进程信息。通过源IP、目的IP、源端口、目的端口和协议类型组成的五元组连接信息，查询发起该连接的进程信息。

**需要权限：** ohos.permission.kernel.TRAFFIC\_FILTER

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const OH\_TrafficFilter\_ConnectionInfo](capi-trafficfilter-oh-trafficfilter-connectioninfo.md)\* connection\_info | 输入的连接信息。 |
| [OH\_TrafficFilter\_ProcessInfo](capi-trafficfilter-oh-trafficfilter-processinfo.md)\* process\_info | 输出的进程信息。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | [OH\_TRAFFICFILTER\_OK](capi-net-trafficfilter-type-h.md#oh_trafficfilter_errcode) - 成功。  [OH\_TRAFFICFILTER\_ERROR\_PERMISSION\_DENIED](capi-net-trafficfilter-type-h.md#oh_trafficfilter_errcode) - 缺少权限。  [OH\_TRAFFICFILTER\_ERROR\_INVALID\_PARAM](capi-net-trafficfilter-type-h.md#oh_trafficfilter_errcode) - 输入参数无效。  [OH\_TRAFFICFILTER\_ERROR\_NOT\_FOUND](capi-net-trafficfilter-type-h.md#oh_trafficfilter_errcode) - 未找到进程。 |

### OH\_TrafficFilter\_CreatePacketController()

```c
int32_t OH_TrafficFilter_CreatePacketController(
    uint32_t groupId,
    uint32_t priority,
    const OH_TrafficFilter_Config* config,
    OH_TrafficFilter_PacketController** controller
)
```

**描述**

创建报文控制器实例。用于拦截和过滤网络报文。资源管理：该实例占用系统资源，必须调用[OH\_TrafficFilter\_DestroyPacketController](capi-net-trafficfilter-h.md#oh_trafficfilter_destroypacketcontroller)释放资源。如果该函数失败，不会返回有效的控制器。

**需要权限：** ohos.permission.kernel.TRAFFIC\_FILTER

**起始版本：** 26.0.1

**参数：**

| 参数项 | 描述 |
| --- | --- |
| uint32\_t groupId | 过滤链标识符。同一应用内的多个控制器可以使用不同的groupId。不同应用的相同groupId会自动隔离。取值范围为[OH\_TRAFFICFILTER\_MIN\_GROUP\_ID, OH\_TRAFFICFILTER\_MAX\_GROUP\_ID]。 |
| uint32\_t priority | 优先级（决定不同groupId链之间的执行顺序，数值越小执行优先级越高）。取值范围为[OH\_TRAFFICFILTER\_MIN\_PRIORITY, OH\_TRAFFICFILTER\_MAX\_PRIORITY]。 |
| [const OH\_TrafficFilter\_Config](capi-trafficfilter-oh-trafficfilter-config.md)\* config | 配置参数（配置为NULL时表示使用默认配置）。 |
| [OH\_TrafficFilter\_PacketController\*\*](capi-trafficfilter-oh-trafficfilter-packetcontroller.md) controller | 出参，成功时为报文控制器句柄。失败时为NULL，句柄不可用。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | [OH\_TRAFFICFILTER\_OK](capi-net-trafficfilter-type-h.md#oh_trafficfilter_errcode) - 成功。  [OH\_TRAFFICFILTER\_ERROR\_PERMISSION\_DENIED](capi-net-trafficfilter-type-h.md#oh_trafficfilter_errcode) - 缺少权限。  [OH\_TRAFFICFILTER\_ERROR\_GROUP\_ID\_IN\_USE](capi-net-trafficfilter-type-h.md#oh_trafficfilter_errcode) - group\_id已存在。  [OH\_TRAFFICFILTER\_ERROR\_INVALID\_PARAM](capi-net-trafficfilter-type-h.md#oh_trafficfilter_errcode) - group\_id或priority无效。  [OH\_TRAFFICFILTER\_ERROR\_NFQUEUE\_ERROR](capi-net-trafficfilter-type-h.md#oh_trafficfilter_errcode) - NFQueue初始化失败。 |

### OH\_TrafficFilter\_DestroyPacketController()

```c
int32_t OH_TrafficFilter_DestroyPacketController(OH_TrafficFilter_PacketController* controller)
```

**描述**

销毁报文控制器实例。销毁控制器实例并释放相关资源（包括规则），调用后句柄将失效。

**需要权限：** ohos.permission.kernel.TRAFFIC\_FILTER

**起始版本：** 26.0.1

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_TrafficFilter\_PacketController](capi-trafficfilter-oh-trafficfilter-packetcontroller.md)\* controller | OH\_TrafficFilter\_PacketController句柄。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | [OH\_TRAFFICFILTER\_OK](capi-net-trafficfilter-type-h.md#oh_trafficfilter_errcode) - 成功。  [OH\_TRAFFICFILTER\_ERROR\_PERMISSION\_DENIED](capi-net-trafficfilter-type-h.md#oh_trafficfilter_errcode) - 缺少权限。  [OH\_TRAFFICFILTER\_ERROR\_INVALID\_PARAM](capi-net-trafficfilter-type-h.md#oh_trafficfilter_errcode) - controller为NULL。  [OH\_TRAFFICFILTER\_ERROR\_NOT\_FOUND](capi-net-trafficfilter-type-h.md#oh_trafficfilter_errcode) - 未找到指定的控制器句柄。 |

### OH\_TrafficFilter\_RegisterPacketCallback()

```c
int32_t OH_TrafficFilter_RegisterPacketCallback(
    OH_TrafficFilter_PacketController* controller,
    OH_TrafficFilter_PacketCallback callback,
    void* userData
)
```

**描述**

注册报文回调函数。注册一个回调函数用于处理拦截到的报文，当报文匹配到过滤规则时，将触发该回调。如需释放回调，需调用OH\_TrafficFilter\_UnregisterPacketCallback。

**需要权限：** ohos.permission.kernel.TRAFFIC\_FILTER

**起始版本：** 26.0.1

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_TrafficFilter\_PacketController](capi-trafficfilter-oh-trafficfilter-packetcontroller.md)\* controller | OH\_TrafficFilter\_PacketController句柄。 |
| [OH\_TrafficFilter\_PacketCallback](capi-trafficfilter-oh-trafficfilter-packetcallback.md) callback | 回调函数指针。不能为NULL。 |
| void\* userData | 用户数据（将在回调中回传）。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | [OH\_TRAFFICFILTER\_OK](capi-net-trafficfilter-type-h.md#oh_trafficfilter_errcode) - 成功。  [OH\_TRAFFICFILTER\_ERROR\_PERMISSION\_DENIED](capi-net-trafficfilter-type-h.md#oh_trafficfilter_errcode) - 缺少权限。  [OH\_TRAFFICFILTER\_ERROR\_INVALID\_PARAM](capi-net-trafficfilter-type-h.md#oh_trafficfilter_errcode) - controller或callback为NULL。 |

### OH\_TrafficFilter\_UnregisterPacketCallback()

```c
int32_t OH_TrafficFilter_UnregisterPacketCallback(OH_TrafficFilter_PacketController* controller)
```

**描述**

注销报文回调函数。

**需要权限：** ohos.permission.kernel.TRAFFIC\_FILTER

**起始版本：** 26.0.1

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_TrafficFilter\_PacketController](capi-trafficfilter-oh-trafficfilter-packetcontroller.md)\* controller | OH\_TrafficFilter\_PacketController句柄。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | [OH\_TRAFFICFILTER\_OK](capi-net-trafficfilter-type-h.md#oh_trafficfilter_errcode) - 成功。  [OH\_TRAFFICFILTER\_ERROR\_PERMISSION\_DENIED](capi-net-trafficfilter-type-h.md#oh_trafficfilter_errcode) - 缺少权限。  [OH\_TRAFFICFILTER\_ERROR\_INVALID\_PARAM](capi-net-trafficfilter-type-h.md#oh_trafficfilter_errcode) - controller为NULL。 |

### OH\_TrafficFilter\_AddPacketRule()

```c
int32_t OH_TrafficFilter_AddPacketRule(
    OH_TrafficFilter_PacketController* controller,
    const OH_TrafficFilter_FilterRule* rule
)
```

**描述**

添加报文过滤规则。单个[OH\_TrafficFilter\_FilterRule](capi-trafficfilter-oh-trafficfilter-filterrule.md)结构内的条件为逻辑与关系。添加到同一[OH\_TrafficFilter\_PacketController](capi-trafficfilter-oh-trafficfilter-packetcontroller.md)的多个规则为逻辑或关系。如需清除过滤规则，需调用[OH\_TrafficFilter\_ClearPacketRule](capi-net-trafficfilter-h.md#oh_trafficfilter_clearpacketrule)。

**需要权限：** ohos.permission.kernel.TRAFFIC\_FILTER

**起始版本：** 26.0.1

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_TrafficFilter\_PacketController](capi-trafficfilter-oh-trafficfilter-packetcontroller.md)\* controller | OH\_TrafficFilter\_PacketController句柄。 |
| [const OH\_TrafficFilter\_FilterRule](capi-trafficfilter-oh-trafficfilter-filterrule.md)\* rule | 过滤规则。不能为NULL。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | [OH\_TRAFFICFILTER\_OK](capi-net-trafficfilter-type-h.md#oh_trafficfilter_errcode) - 成功。  [OH\_TRAFFICFILTER\_ERROR\_PERMISSION\_DENIED](capi-net-trafficfilter-type-h.md#oh_trafficfilter_errcode) - 缺少权限。  [OH\_TRAFFICFILTER\_ERROR\_INVALID\_PARAM](capi-net-trafficfilter-type-h.md#oh_trafficfilter_errcode) - controller或rule为NULL。  [OH\_TRAFFICFILTER\_ERROR\_TOO\_MANY\_RULES](capi-net-trafficfilter-type-h.md#oh_trafficfilter_errcode) - 添加的规则超过2000条。 |

### OH\_TrafficFilter\_ClearPacketRule()

```c
int32_t OH_TrafficFilter_ClearPacketRule(OH_TrafficFilter_PacketController* controller)
```

**描述**

清除报文过滤规则（清除controller句柄上添加的所有报文过滤规则）。

**需要权限：** ohos.permission.kernel.TRAFFIC\_FILTER

**起始版本：** 26.0.1

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_TrafficFilter\_PacketController](capi-trafficfilter-oh-trafficfilter-packetcontroller.md)\* controller | OH\_TrafficFilter\_PacketController句柄。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | [OH\_TRAFFICFILTER\_OK](capi-net-trafficfilter-type-h.md#oh_trafficfilter_errcode) - 成功。  [OH\_TRAFFICFILTER\_ERROR\_PERMISSION\_DENIED](capi-net-trafficfilter-type-h.md#oh_trafficfilter_errcode) - 缺少权限。  [OH\_TRAFFICFILTER\_ERROR\_INVALID\_PARAM](capi-net-trafficfilter-type-h.md#oh_trafficfilter_errcode) - controller为NULL。 |
