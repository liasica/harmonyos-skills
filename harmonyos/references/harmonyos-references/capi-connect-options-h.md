---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-connect-options-h
title: connect_options.h
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > C API > 头文件 > connect_options.h
category: harmonyos-references
scraped_at: 2026-09-02T15:00:36+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:806bc78c67b91580ad4116b043b0e040675a14d34369e279cef9aba634af7194
---

## 概述

声明ExtensionAbility的连接选项，包括连接成功、断开连接和连接失败的回调接口。

**引用文件：** <AbilityKit/ability\_runtime/connect\_options.h>

**库：** libability\_runtime.so

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 26.0.0

**相关模块：** [AbilityRuntime](capi-abilityruntime.md)

## 汇总

### 结构体

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [OH\_AbilityRuntime\_ConnectOptions](capi-abilityruntime-oh-abilityruntime-connectoptions.md) | OH\_AbilityRuntime\_ConnectOptions | 定义OH\_AbilityRuntime\_ConnectOptions结构体类型。 |

### 函数

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [typedef void (\*OH\_AbilityRuntime\_ConnectOptions\_OnConnectCallback)(OH\_AbilityRuntime\_ConnectOptions \*connectOptions, AbilityBase\_Element \*element, OHIPCRemoteProxy \*proxy)](capi-connect-options-h.md#oh_abilityruntime_connectoptions_onconnectcallback) | OH\_AbilityRuntime\_ConnectOptions\_OnConnectCallback | 连接成功时触发的回调函数。 |
| [typedef void (\*OH\_AbilityRuntime\_ConnectOptions\_OnDisconnectCallback)(OH\_AbilityRuntime\_ConnectOptions \*connectOptions, AbilityBase\_Element \*element)](capi-connect-options-h.md#oh_abilityruntime_connectoptions_ondisconnectcallback) | OH\_AbilityRuntime\_ConnectOptions\_OnDisconnectCallback | 断开连接时触发的回调函数。 |
| [typedef void (\*OH\_AbilityRuntime\_ConnectOptions\_OnFailedCallback)(OH\_AbilityRuntime\_ConnectOptions \*connectOptions, AbilityRuntime\_ErrorCode code)](capi-connect-options-h.md#oh_abilityruntime_connectoptions_onfailedcallback) | OH\_AbilityRuntime\_ConnectOptions\_OnFailedCallback | 连接失败时触发的回调函数。 |
| [OH\_AbilityRuntime\_ConnectOptions\* OH\_AbilityRuntime\_CreateConnectOptions()](capi-connect-options-h.md#oh_abilityruntime_createconnectoptions) | - | 创建一个ConnectOptions对象。 |
| [AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_DestroyConnectOptions(OH\_AbilityRuntime\_ConnectOptions \*connectOptions)](capi-connect-options-h.md#oh_abilityruntime_destroyconnectoptions) | - | 销毁指定的ConnectOptions对象。 |
| [AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_ConnectOptions\_SetOnConnectCallback(OH\_AbilityRuntime\_ConnectOptions \*connectOptions, OH\_AbilityRuntime\_ConnectOptions\_OnConnectCallback onConnectCallback)](capi-connect-options-h.md#oh_abilityruntime_connectoptions_setonconnectcallback) | - | 在[OH\_AbilityRuntime\_ConnectOptions](capi-abilityruntime-oh-abilityruntime-connectoptions.md)中设置连接成功回调[OH\_AbilityRuntime\_ConnectOptions\_OnConnectCallback](capi-connect-options-h.md#oh_abilityruntime_connectoptions_onconnectcallback)。 |
| [AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_ConnectOptions\_SetOnDisconnectCallback(OH\_AbilityRuntime\_ConnectOptions \*connectOptions, OH\_AbilityRuntime\_ConnectOptions\_OnDisconnectCallback onDisconnectCallback)](capi-connect-options-h.md#oh_abilityruntime_connectoptions_setondisconnectcallback) | - | 在[OH\_AbilityRuntime\_ConnectOptions](capi-abilityruntime-oh-abilityruntime-connectoptions.md)中设置断开连接回调[OH\_AbilityRuntime\_ConnectOptions\_OnDisconnectCallback](capi-connect-options-h.md#oh_abilityruntime_connectoptions_ondisconnectcallback)。 |
| [AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_ConnectOptions\_SetOnFailedCallback(OH\_AbilityRuntime\_ConnectOptions \*connectOptions, OH\_AbilityRuntime\_ConnectOptions\_OnFailedCallback onFailedCallback)](capi-connect-options-h.md#oh_abilityruntime_connectoptions_setonfailedcallback) | - | 在[OH\_AbilityRuntime\_ConnectOptions](capi-abilityruntime-oh-abilityruntime-connectoptions.md)中设置连接失败回调[OH\_AbilityRuntime\_ConnectOptions\_OnFailedCallback](capi-connect-options-h.md#oh_abilityruntime_connectoptions_onfailedcallback)。 |

## 函数说明

### OH\_AbilityRuntime\_ConnectOptions\_OnConnectCallback()

```c
typedef void (*OH_AbilityRuntime_ConnectOptions_OnConnectCallback)(OH_AbilityRuntime_ConnectOptions *connectOptions, AbilityBase_Element *element, OHIPCRemoteProxy *proxy)
```

**描述**

连接成功时触发的回调函数。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| OH\_AbilityRuntime\_ConnectOptions \*connectOptions | 指向[OH\_AbilityRuntime\_ConnectOptions](capi-abilityruntime-oh-abilityruntime-connectoptions.md)实例的指针。 |
| [AbilityBase\_Element](capi-abilitybase-element.md) \*element | 表示ExtensionAbility的组件名称。 |
| [OHIPCRemoteProxy](capi-ohipcparcel-ohipcremoteproxy.md) \*proxy | 表示远端对象实例。 |

### OH\_AbilityRuntime\_ConnectOptions\_OnDisconnectCallback()

```c
typedef void (*OH_AbilityRuntime_ConnectOptions_OnDisconnectCallback)(OH_AbilityRuntime_ConnectOptions *connectOptions, AbilityBase_Element *element)
```

**描述**

断开连接时触发的回调函数。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| OH\_AbilityRuntime\_ConnectOptions \*connectOptions | 指向[OH\_AbilityRuntime\_ConnectOptions](capi-abilityruntime-oh-abilityruntime-connectoptions.md)实例的指针。 |
| [AbilityBase\_Element](capi-abilitybase-element.md) \*element | 表示ExtensionAbility的组件名称。 |

### OH\_AbilityRuntime\_ConnectOptions\_OnFailedCallback()

```c
typedef void (*OH_AbilityRuntime_ConnectOptions_OnFailedCallback)(OH_AbilityRuntime_ConnectOptions *connectOptions, AbilityRuntime_ErrorCode code)
```

**描述**

连接失败时触发的回调函数。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| OH\_AbilityRuntime\_ConnectOptions \*connectOptions | 指向[OH\_AbilityRuntime\_ConnectOptions](capi-abilityruntime-oh-abilityruntime-connectoptions.md)实例的指针。 |
| [AbilityRuntime\_ErrorCode](capi-ability-runtime-common-h.md#abilityruntime_errorcode) code | 表示失败的错误码。 |

### OH\_AbilityRuntime\_CreateConnectOptions()

```c
OH_AbilityRuntime_ConnectOptions* OH_AbilityRuntime_CreateConnectOptions()
```

**描述**

创建一个ConnectOptions对象。

**起始版本：** 26.0.0

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AbilityRuntime\_ConnectOptions\*](capi-abilityruntime-oh-abilityruntime-connectoptions.md) | 返回新创建的OH\_AbilityRuntime\_ConnectOptions对象。  调用方需调用[OH\_AbilityRuntime\_DestroyConnectOptions](capi-connect-options-h.md#oh_abilityruntime_destroyconnectoptions)销毁返回的对象，避免内存泄漏。 |

### OH\_AbilityRuntime\_DestroyConnectOptions()

```c
AbilityRuntime_ErrorCode OH_AbilityRuntime_DestroyConnectOptions(OH_AbilityRuntime_ConnectOptions *connectOptions)
```

**描述**

销毁指定的ConnectOptions对象。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AbilityRuntime\_ConnectOptions](capi-abilityruntime-oh-abilityruntime-connectoptions.md) \*connectOptions | 指向待销毁的[OH\_AbilityRuntime\_ConnectOptions](capi-abilityruntime-oh-abilityruntime-connectoptions.md)实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [AbilityRuntime\_ErrorCode](capi-ability-runtime-common-h.md#abilityruntime_errorcode) | 返回特定的错误码。  [ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR](capi-ability-runtime-common-h.md#abilityruntime_errorcode) 操作成功。  [ABILITY\_RUNTIME\_ERROR\_CODE\_PARAM\_INVALID](capi-ability-runtime-common-h.md#abilityruntime_errorcode) connectOptions无效。 |

### OH\_AbilityRuntime\_ConnectOptions\_SetOnConnectCallback()

```c
AbilityRuntime_ErrorCode OH_AbilityRuntime_ConnectOptions_SetOnConnectCallback(OH_AbilityRuntime_ConnectOptions *connectOptions, OH_AbilityRuntime_ConnectOptions_OnConnectCallback onConnectCallback)
```

**描述**

在[OH\_AbilityRuntime\_ConnectOptions](capi-abilityruntime-oh-abilityruntime-connectoptions.md)中设置连接成功回调[OH\_AbilityRuntime\_ConnectOptions\_OnConnectCallback](capi-connect-options-h.md#oh_abilityruntime_connectoptions_onconnectcallback)。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AbilityRuntime\_ConnectOptions](capi-abilityruntime-oh-abilityruntime-connectoptions.md) \*connectOptions | 指向待设置的[OH\_AbilityRuntime\_ConnectOptions](capi-abilityruntime-oh-abilityruntime-connectoptions.md)实例的指针。 |
| [OH\_AbilityRuntime\_ConnectOptions\_OnConnectCallback](capi-connect-options-h.md#oh_abilityruntime_connectoptions_onconnectcallback) onConnectCallback | 表示待设置的[OH\_AbilityRuntime\_ConnectOptions\_OnConnectCallback](capi-connect-options-h.md#oh_abilityruntime_connectoptions_onconnectcallback)回调函数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [AbilityRuntime\_ErrorCode](capi-ability-runtime-common-h.md#abilityruntime_errorcode) | 返回特定的错误码。  [ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR](capi-ability-runtime-common-h.md#abilityruntime_errorcode) 接口调用成功。  [ABILITY\_RUNTIME\_ERROR\_CODE\_PARAM\_INVALID](capi-ability-runtime-common-h.md#abilityruntime_errorcode) 参数校验失败。 |

### OH\_AbilityRuntime\_ConnectOptions\_SetOnDisconnectCallback()

```c
AbilityRuntime_ErrorCode OH_AbilityRuntime_ConnectOptions_SetOnDisconnectCallback(OH_AbilityRuntime_ConnectOptions *connectOptions, OH_AbilityRuntime_ConnectOptions_OnDisconnectCallback onDisconnectCallback)
```

**描述**

在[OH\_AbilityRuntime\_ConnectOptions](capi-abilityruntime-oh-abilityruntime-connectoptions.md)中设置断开连接回调[OH\_AbilityRuntime\_ConnectOptions\_OnDisconnectCallback](capi-connect-options-h.md#oh_abilityruntime_connectoptions_ondisconnectcallback)。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AbilityRuntime\_ConnectOptions](capi-abilityruntime-oh-abilityruntime-connectoptions.md) \*connectOptions | 指向待设置的[OH\_AbilityRuntime\_ConnectOptions](capi-abilityruntime-oh-abilityruntime-connectoptions.md)实例的指针。 |
| [OH\_AbilityRuntime\_ConnectOptions\_OnDisconnectCallback](capi-connect-options-h.md#oh_abilityruntime_connectoptions_ondisconnectcallback) onDisconnectCallback | 表示待设置的[OH\_AbilityRuntime\_ConnectOptions\_OnDisconnectCallback](capi-connect-options-h.md#oh_abilityruntime_connectoptions_ondisconnectcallback)回调函数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [AbilityRuntime\_ErrorCode](capi-ability-runtime-common-h.md#abilityruntime_errorcode) | 返回特定的错误码。  [ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR](capi-ability-runtime-common-h.md#abilityruntime_errorcode) 接口调用成功。  [ABILITY\_RUNTIME\_ERROR\_CODE\_PARAM\_INVALID](capi-ability-runtime-common-h.md#abilityruntime_errorcode) 参数校验失败。 |

### OH\_AbilityRuntime\_ConnectOptions\_SetOnFailedCallback()

```c
AbilityRuntime_ErrorCode OH_AbilityRuntime_ConnectOptions_SetOnFailedCallback(OH_AbilityRuntime_ConnectOptions *connectOptions, OH_AbilityRuntime_ConnectOptions_OnFailedCallback onFailedCallback)
```

**描述**

在[OH\_AbilityRuntime\_ConnectOptions](capi-abilityruntime-oh-abilityruntime-connectoptions.md)中设置连接失败回调[OH\_AbilityRuntime\_ConnectOptions\_OnFailedCallback](capi-connect-options-h.md#oh_abilityruntime_connectoptions_onfailedcallback)。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AbilityRuntime\_ConnectOptions](capi-abilityruntime-oh-abilityruntime-connectoptions.md) \*connectOptions | 指向待设置的[OH\_AbilityRuntime\_ConnectOptions](capi-abilityruntime-oh-abilityruntime-connectoptions.md)实例的指针。 |
| [OH\_AbilityRuntime\_ConnectOptions\_OnFailedCallback](capi-connect-options-h.md#oh_abilityruntime_connectoptions_onfailedcallback) onFailedCallback | 表示待设置的[OH\_AbilityRuntime\_ConnectOptions\_OnFailedCallback](capi-connect-options-h.md#oh_abilityruntime_connectoptions_onfailedcallback)回调函数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [AbilityRuntime\_ErrorCode](capi-ability-runtime-common-h.md#abilityruntime_errorcode) | 返回特定的错误码。  [ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR](capi-ability-runtime-common-h.md#abilityruntime_errorcode) 接口调用成功。  [ABILITY\_RUNTIME\_ERROR\_CODE\_PARAM\_INVALID](capi-ability-runtime-common-h.md#abilityruntime_errorcode) 参数校验失败。 |
