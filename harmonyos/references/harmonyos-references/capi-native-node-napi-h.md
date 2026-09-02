---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-node-napi-h
title: native_node_napi.h
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 头文件 > native_node_napi.h
category: harmonyos-references
scraped_at: 2026-09-02T15:01:18+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:89e9b4dd2c8d5ef1c816b25797c436d10691c36b7ce61ff60bf29fba51c845fe
---

## 概述

提供ArkTS侧[FrameNode](js-apis-arkui-framenode.md)、[UIContext](arkts-apis-uicontext-uicontext.md)、NodeContent、DrawableDescriptor等对象与Native侧对象的转换，以及Navigation、Router页面信息查询、帧回调/空闲回调注册和事件直通启用或禁用等能力，适用于ArkTS与Native侧进行ArkUI节点、上下文、资源和页面状态联动的场景。

**引用文件：** <arkui/native\_node\_napi.h>

**库：** libace\_ndk.z.so

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**相关模块：** [ArkUI\_NativeModule](capi-arkui-nativemodule.md)

**相关示例：** [NativeNodeNapiSample](https://gitcode.com/HarmonyOS_Samples/guide-snippets/tree/master/ArkUISample/NativeNodeNapiSample)

## 汇总

### 函数

| 名称 | 描述 |
| --- | --- |
| [int32\_t OH\_ArkUI\_GetNodeHandleFromNapiValue(napi\_env env, napi\_value frameNode, ArkUI\_NodeHandle\* handle)](capi-native-node-napi-h.md#oh_arkui_getnodehandlefromnapivalue) | 将ArkTS侧创建的FrameNode节点对象映射为Native侧的ArkUI\_NodeHandle，适用于Native侧需要操作或管理ArkTS侧FrameNode节点的场景。 |
| [int32\_t OH\_ArkUI\_GetContextFromNapiValue(napi\_env env, napi\_value value, ArkUI\_ContextHandle\* context)](capi-native-node-napi-h.md#oh_arkui_getcontextfromnapivalue) | 将ArkTS侧创建的[UIContext](arkts-apis-uicontext-uicontext.md)对象映射为Native侧的ArkUI\_ContextHandle，适用于Native侧需要基于UIContext调用ArkUI能力的场景。 |
| [int32\_t OH\_ArkUI\_GetNodeContentFromNapiValue(napi\_env env, napi\_value value, ArkUI\_NodeContentHandle\* content)](capi-native-node-napi-h.md#oh_arkui_getnodecontentfromnapivalue) | 将ArkTS侧创建的NodeContent对象映射为Native侧的ArkUI\_NodeContentHandle，适用于Native侧需要操作或挂载ArkTS侧NodeContent内容的场景。 |
| [int32\_t OH\_ArkUI\_GetDrawableDescriptorFromNapiValue(napi\_env env, napi\_value value, ArkUI\_DrawableDescriptor\*\* drawableDescriptor)](capi-native-node-napi-h.md#oh_arkui_getdrawabledescriptorfromnapivalue) | 将ArkTS侧创建的[DrawableDescriptor](ts-basic-components-image.md#drawabledescriptor10)对象映射到Native侧的[ArkUI\_DrawableDescriptor](capi-arkui-nativemodule-arkui-drawabledescriptor.md)，适用于Native侧需要使用ArkTS侧图片资源描述对象的场景。 |
| [int32\_t OH\_ArkUI\_GetDrawableDescriptorFromResourceNapiValue(napi\_env env, napi\_value value, ArkUI\_DrawableDescriptor\*\* drawableDescriptor)](capi-native-node-napi-h.md#oh_arkui_getdrawabledescriptorfromresourcenapivalue) | 将ArkTS侧通过$r()获取的资源对象转换为Native侧可使用的[ArkUI\_DrawableDescriptor](capi-arkui-nativemodule-arkui-drawabledescriptor.md)对象，适用于Native侧需要使用ArkTS资源对象作为图片资源描述的场景。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_GetNavigationId(ArkUI\_NodeHandle node, char\* buffer, int32\_t bufferSize, int32\_t\* writeLength)](capi-native-node-napi-h.md#oh_arkui_getnavigationid) | 获取当前节点所在的Navigation组件的ID。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_GetNavDestinationName(ArkUI\_NodeHandle node, char\* buffer, int32\_t bufferSize, int32\_t\* writeLength)](capi-native-node-napi-h.md#oh_arkui_getnavdestinationname) | 获取当前节点所在的[NavDestination](ts-basic-components-navdestination.md)组件的名称。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_GetNavStackLength(ArkUI\_NodeHandle node, int32\_t\* length)](capi-native-node-napi-h.md#oh_arkui_getnavstacklength) | 获取当前节点所在的Navigation栈的长度。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_GetNavDestinationNameByIndex(ArkUI\_NodeHandle node, int32\_t index, char\* buffer, int32\_t bufferSize, int32\_t\* writeLength)](capi-native-node-napi-h.md#oh_arkui_getnavdestinationnamebyindex) | 根据给定索引值，获取当前节点所在的Navigation栈中对应位置的页面名称。索引值从0开始计数，0为栈底。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_GetNavDestinationId(ArkUI\_NodeHandle node, char\* buffer, int32\_t bufferSize, int32\_t\* writeLength)](capi-native-node-napi-h.md#oh_arkui_getnavdestinationid) | 获取当前节点所在的NavDestination组件的ID。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_GetNavDestinationState(ArkUI\_NodeHandle node, ArkUI\_NavDestinationState\* state)](capi-native-node-napi-h.md#oh_arkui_getnavdestinationstate) | 获取当前节点所在的NavDestination组件的状态。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_GetNavDestinationIndex(ArkUI\_NodeHandle node, int32\_t\* index)](capi-native-node-napi-h.md#oh_arkui_getnavdestinationindex) | 获取当前节点所在的NavDestination组件在页面栈中的索引。 |
| [napi\_value OH\_ArkUI\_GetNavDestinationParam(ArkUI\_NodeHandle node)](capi-native-node-napi-h.md#oh_arkui_getnavdestinationparam) | 获取当前节点所在的NavDestination组件的参数。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_GetRouterPageIndex(ArkUI\_NodeHandle node, int32\_t\* index)](capi-native-node-napi-h.md#oh_arkui_getrouterpageindex) | 获取当前节点所在页面在Router页面栈中的索引。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_GetRouterPageName(ArkUI\_NodeHandle node, char\* buffer, int32\_t bufferSize, int32\_t\* writeLength)](capi-native-node-napi-h.md#oh_arkui_getrouterpagename) | 获取当前节点所在页面的名称。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_GetRouterPagePath(ArkUI\_NodeHandle node, char\* buffer, int32\_t bufferSize, int32\_t\* writeLength)](capi-native-node-napi-h.md#oh_arkui_getrouterpagepath) | 获取当前节点所在页面的Page组件的路径。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_GetRouterPageState(ArkUI\_NodeHandle node, ArkUI\_RouterPageState\* state)](capi-native-node-napi-h.md#oh_arkui_getrouterpagestate) | 获取当前节点所在页面的Page组件的状态。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_GetRouterPageId(ArkUI\_NodeHandle node, char\* buffer, int32\_t bufferSize, int32\_t\* writeLength)](capi-native-node-napi-h.md#oh_arkui_getrouterpageid) | 获取当前节点所在页面的Page组件的ID。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_InitModuleForArkTSEnv(napi\_env env)](capi-native-node-napi-h.md#oh_arkui_initmoduleforarktsenv) | 初始化指定上下文环境的ArkUI相关接口，适用于在Native侧使用ArkUI相关接口前进行上下文环境初始化的场景。该函数禁止在非UI线程中调用，否则程序将主动中止。使用该函数初始化指定上下文环境后，在对应环境销毁时调用[OH\_ArkUI\_NotifyArkTSEnvDestroy()](capi-native-node-napi-h.md#oh_arkui_notifyarktsenvdestroy)通知环境已销毁。 |
| [void OH\_ArkUI\_NotifyArkTSEnvDestroy(napi\_env env)](capi-native-node-napi-h.md#oh_arkui_notifyarktsenvdestroy) | 通知指定的上下文环境已销毁，适用于ArkTS上下文环境销毁时在Native侧同步清理相关状态的场景。使用[OH\_ArkUI\_InitModuleForArkTSEnv()](capi-native-node-napi-h.md#oh_arkui_initmoduleforarktsenv)初始化上下文环境后，应在该环境销毁时调用此函数。该函数禁止在非UI线程中调用，否则程序将主动中止。 |
| [int32\_t OH\_ArkUI\_PostFrameCallback(ArkUI\_ContextHandle uiContext, void\* userData, void (\*callback)(uint64\_t nanoTimestamp, uint32\_t frameCount, void\* userData))](capi-native-node-napi-h.md#oh_arkui_postframecallback) | 注册一个回调函数，以便在下一帧渲染时执行，适用于Native侧在下一帧执行界面刷新或渲染相关任务的场景。不允许在非UI线程调用；如果检查到在非UI线程调用，程序会主动中止。 |
| [int32\_t OH\_ArkUI\_PostIdleCallback(ArkUI\_ContextHandle uiContext, void\* userData, void (\*callback)(uint64\_t nanoTimeLeft, uint32\_t frameCount, void\* userData))](capi-native-node-napi-h.md#oh_arkui_postidlecallback) | 注册一个回调函数，适用于需要在Native侧利用帧间空闲时间处理非紧急任务的场景。下一帧渲染结束后，如果距离该帧之后的下一个VSync信号到来的剩余时间大于1ms，该回调函数将被执行；如果剩余时间小于1ms，回调函数将顺延至后续某一帧渲染结束后剩余时间大于1ms时执行。如果当前没有下一帧，将自动请求下一帧。不允许在非UI线程调用；如果检查到在非UI线程调用，程序会主动中止。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_EnableEventPassthrough(ArkUI\_ContextHandle uiContext, bool enabled, ArkUI\_RawInputEventType type)](capi-native-node-napi-h.md#oh_arkui_enableeventpassthrough) | 启用或禁用事件直通。事件直通表示在事件分发过程中，不经过[重采样](../harmonyos-guides/arkts-interaction-development-guide-touch-screen.md#重采样与历史点)直接下发给组件。 |

## 函数说明

### OH\_ArkUI\_GetNodeHandleFromNapiValue()

```c
int32_t OH_ArkUI_GetNodeHandleFromNapiValue(napi_env env, napi_value frameNode, ArkUI_NodeHandle* handle)
```

**描述：**

将ArkTS侧创建的FrameNode节点对象映射为Native侧的ArkUI\_NodeHandle，适用于Native侧需要操作或管理ArkTS侧FrameNode节点的场景。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| napi\_env env | Node-API的环境指针。 |
| napi\_value frameNode | ArkTS侧创建的FrameNode对象。 |
| [ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md)\* handle | ArkUI\_NodeHandle指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常，请检查传入的env、frameNode和handle是否有效。 |

### OH\_ArkUI\_GetContextFromNapiValue()

```c
int32_t OH_ArkUI_GetContextFromNapiValue(napi_env env, napi_value value, ArkUI_ContextHandle* context)
```

**描述：**

将ArkTS侧创建的[UIContext](arkts-apis-uicontext-uicontext.md)对象映射为Native侧的ArkUI\_ContextHandle，适用于Native侧需要基于UIContext调用ArkUI能力的场景。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| napi\_env env | Node-API的环境指针。 |
| napi\_value value | ArkTS侧创建的UIContext对象。 |
| [ArkUI\_ContextHandle](capi-arkui-nativemodule-arkui-context8h.md)\* context | ArkUI\_ContextHandle指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常，请检查传入的env、value和context是否有效。 |

### OH\_ArkUI\_GetNodeContentFromNapiValue()

```c
int32_t OH_ArkUI_GetNodeContentFromNapiValue(napi_env env, napi_value value, ArkUI_NodeContentHandle* content)
```

**描述：**

将ArkTS侧创建的NodeContent对象映射为Native侧的ArkUI\_NodeContentHandle，适用于Native侧需要操作或挂载ArkTS侧NodeContent内容的场景。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| napi\_env env | Node-API的环境指针。 |
| napi\_value value | ArkTS侧创建的NodeContent对象。 |
| [ArkUI\_NodeContentHandle](capi-arkui-nativemodule-arkui-nodecontent8h.md)\* content | ArkUI\_NodeContentHandle指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常，请检查传入的env、value和content是否有效。 |

### OH\_ArkUI\_GetDrawableDescriptorFromNapiValue()

```c
int32_t OH_ArkUI_GetDrawableDescriptorFromNapiValue(napi_env env, napi_value value, ArkUI_DrawableDescriptor** drawableDescriptor)
```

**描述：**

将ArkTS侧创建的[DrawableDescriptor](ts-basic-components-image.md#drawabledescriptor10)对象映射到Native侧的[ArkUI\_DrawableDescriptor](capi-arkui-nativemodule-arkui-drawabledescriptor.md)，适用于Native侧需要使用ArkTS侧图片资源描述对象的场景。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| napi\_env env | Node-API的环境指针。 |
| napi\_value value | ArkTS侧创建的[DrawableDescriptor](ts-basic-components-image.md#drawabledescriptor10)对象。 |
| [ArkUI\_DrawableDescriptor](capi-arkui-nativemodule-arkui-drawabledescriptor.md)\*\* drawableDescriptor | 接受ArkUI\_DrawableDescriptor指针的对象。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常，请检查传入的env、value和drawableDescriptor是否有效。 |

### OH\_ArkUI\_GetDrawableDescriptorFromResourceNapiValue()

```c
int32_t OH_ArkUI_GetDrawableDescriptorFromResourceNapiValue(napi_env env, napi_value value, ArkUI_DrawableDescriptor** drawableDescriptor)
```

**描述：**

将ArkTS侧通过$r()获取的资源对象转换为Native侧可使用的[ArkUI\_DrawableDescriptor](capi-arkui-nativemodule-arkui-drawabledescriptor.md)对象，适用于Native侧需要使用ArkTS资源对象作为图片资源描述的场景。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| napi\_env env | Node-API的环境指针。 |
| napi\_value value | ArkTS侧通过$r()获取的资源对象。 |
| [ArkUI\_DrawableDescriptor](capi-arkui-nativemodule-arkui-drawabledescriptor.md)\*\* drawableDescriptor | 接受ArkUI\_DrawableDescriptor指针的对象。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常，请检查传入的env、value和drawableDescriptor是否有效。 |

### OH\_ArkUI\_GetNavigationId()

```c
ArkUI_ErrorCode OH_ArkUI_GetNavigationId(ArkUI_NodeHandle node, char* buffer, int32_t bufferSize, int32_t* writeLength)
```

**描述：**

获取当前节点所在的[Navigation](ts-basic-components-navigation.md)组件的ID。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md) node | 指定的节点。 |
| char\* buffer | 缓冲区，NavigationID写入该内存区域。 |
| int32\_t bufferSize | 缓冲区大小。 |
| int32\_t\* writeLength | 在返回[ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)时表示实际写入到缓冲区的字符串长度。 在返回[ARKUI\_ERROR\_CODE\_BUFFER\_SIZE\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)时表示可以容纳目标的最小缓冲区大小。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。  [ARKUI\_ERROR\_CODE\_GET\_INFO\_FAILED](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 查询信息失败，可能因为当前节点未挂载在页面下。  [ARKUI\_ERROR\_CODE\_BUFFER\_SIZE\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 数据大小超过指定的缓冲区大小。 |

### OH\_ArkUI\_GetNavDestinationName()

```c
ArkUI_ErrorCode OH_ArkUI_GetNavDestinationName(ArkUI_NodeHandle node, char* buffer, int32_t bufferSize, int32_t* writeLength)
```

**描述：**

获取当前节点所在的[NavDestination](ts-basic-components-navdestination.md)组件的名称。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md) node | 指定的节点。 |
| char\* buffer | 缓冲区，被查询的NavDestination名称写入该内存区域。 |
| int32\_t bufferSize | 缓冲区大小。 |
| int32\_t\* writeLength | 在返回[ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)时表示实际写入到缓冲区的字符串长度。 在返回[ARKUI\_ERROR\_CODE\_BUFFER\_SIZE\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)时表示可以容纳目标的最小缓冲区大小。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。  [ARKUI\_ERROR\_CODE\_GET\_INFO\_FAILED](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 查询信息失败，可能因为当前节点未挂载在页面下。  [ARKUI\_ERROR\_CODE\_BUFFER\_SIZE\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 给定的buffer size小于可以容纳目标的最小缓冲区大小。 |

### OH\_ArkUI\_GetNavStackLength()

```c
ArkUI_ErrorCode OH_ArkUI_GetNavStackLength(ArkUI_NodeHandle node, int32_t* length)
```

**描述：**

获取当前节点所在的Navigation栈的长度。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md) node | 指定的节点。 |
| int32\_t\* length | 栈的长度。查询成功后将结果写回该参数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。  [ARKUI\_ERROR\_CODE\_GET\_INFO\_FAILED](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 查询信息失败，可能因为当前节点未挂载在页面下。 |

### OH\_ArkUI\_GetNavDestinationNameByIndex()

```c
ArkUI_ErrorCode OH_ArkUI_GetNavDestinationNameByIndex(ArkUI_NodeHandle node, int32_t index, char* buffer, int32_t bufferSize, int32_t* writeLength)
```

**描述：**

根据给定索引值，获取当前节点所在的Navigation栈中的页面名称。索引值从0开始计数，0为栈底。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md) node | 指定的节点。 |
| int32\_t index | 被查询NavDestination在栈中的索引。 |
| char\* buffer | 缓冲区，被查询页面的名称写入该内存区域。 |
| int32\_t bufferSize | 缓冲区大小。 |
| int32\_t\* writeLength | 在返回[ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)时表示实际写入到缓冲区的字符串长度。 在返回[ARKUI\_ERROR\_CODE\_BUFFER\_SIZE\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)时表示可以容纳目标的最小缓冲区大小。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_NODE\_INDEX\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) index为非法值。  [ARKUI\_ERROR\_CODE\_GET\_INFO\_FAILED](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 查询信息失败，可能因为当前节点未挂载在页面下。  [ARKUI\_ERROR\_CODE\_BUFFER\_SIZE\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 给定的buffer size小于可以容纳目标的最小缓冲区大小。 |

### OH\_ArkUI\_GetNavDestinationId()

```c
ArkUI_ErrorCode OH_ArkUI_GetNavDestinationId(ArkUI_NodeHandle node, char* buffer, int32_t bufferSize, int32_t* writeLength)
```

**描述：**

获取当前节点所在的NavDestination组件的ID。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md) node | 指定的节点。 |
| char\* buffer | 缓冲区，NavDestinationID写入该内存区域。 |
| int32\_t bufferSize | 缓冲区大小。 |
| int32\_t\* writeLength | 在返回[ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)时表示实际写入到缓冲区的字符串长度。 在返回[ARKUI\_ERROR\_CODE\_BUFFER\_SIZE\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)时表示可以容纳目标的最小缓冲区大小。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。  [ARKUI\_ERROR\_CODE\_GET\_INFO\_FAILED](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 查询信息失败，可能因为当前节点未挂载在页面下。  [ARKUI\_ERROR\_CODE\_BUFFER\_SIZE\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 数据大小超过指定的缓冲区大小。 |

### OH\_ArkUI\_GetNavDestinationState()

```c
ArkUI_ErrorCode OH_ArkUI_GetNavDestinationState(ArkUI_NodeHandle node, ArkUI_NavDestinationState* state)
```

**描述：**

获取当前节点所在的NavDestination组件的状态。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md) node | 指定的节点。 |
| [ArkUI\_NavDestinationState](capi-navigation-router-h.md#arkui_navdestinationstate)\* state | NavDestination的状态值写回该参数中。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。  [ARKUI\_ERROR\_CODE\_GET\_INFO\_FAILED](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 查询信息失败，可能因为当前节点未挂载在页面下。 |

### OH\_ArkUI\_GetNavDestinationIndex()

```c
ArkUI_ErrorCode OH_ArkUI_GetNavDestinationIndex(ArkUI_NodeHandle node, int32_t* index)
```

**描述：**

获取当前节点所在的NavDestination组件在页面栈中的索引。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md) node | 指定的节点。 |
| int32\_t\* index | 索引值，从0开始计数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。  [ARKUI\_ERROR\_CODE\_GET\_INFO\_FAILED](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 查询信息失败，可能因为当前节点未挂载在页面下。 |

### OH\_ArkUI\_GetNavDestinationParam()

```c
napi_value OH_ArkUI_GetNavDestinationParam(ArkUI_NodeHandle node)
```

**描述：**

获取当前节点所在的NavDestination组件的参数。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md) node | 指定的节点。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| napi\_value | 参数对象。如返回为空，则说明参数不存在或指定的节点为空。 |

### OH\_ArkUI\_GetRouterPageIndex()

```c
ArkUI_ErrorCode OH_ArkUI_GetRouterPageIndex(ArkUI_NodeHandle node, int32_t* index)
```

**描述：**

获取当前节点所在[Router](arkts-apis-uicontext-router.md)页面栈中的索引。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md) node | 指定的节点。 |
| int32\_t\* index | 索引值，从1开始计数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 指定的节点或传递的索引异常。  [ARKUI\_ERROR\_CODE\_GET\_INFO\_FAILED](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 查询信息失败，可能因为当前节点未挂载在页面下。 |

### OH\_ArkUI\_GetRouterPageName()

```c
ArkUI_ErrorCode OH_ArkUI_GetRouterPageName(ArkUI_NodeHandle node, char* buffer, int32_t bufferSize, int32_t* writeLength)
```

**描述：**

获取当前节点所在Router页面的名称。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md) node | 指定的节点。 |
| char\* buffer | 缓冲区，页面名称写入该内存区域。 |
| int32\_t bufferSize | 缓冲区大小。 |
| int32\_t\* writeLength | 在返回[ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)时表示实际写入到缓冲区的字符串长度。 在返回[ARKUI\_ERROR\_CODE\_BUFFER\_SIZE\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)时表示可以容纳目标的最小缓冲区大小。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。  [ARKUI\_ERROR\_CODE\_GET\_INFO\_FAILED](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 查询信息失败。  [ARKUI\_ERROR\_CODE\_BUFFER\_SIZE\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 给定的buffer size小于可以容纳目标的最小缓冲区大小。 |

### OH\_ArkUI\_GetRouterPagePath()

```c
ArkUI_ErrorCode OH_ArkUI_GetRouterPagePath(ArkUI_NodeHandle node, char* buffer, int32_t bufferSize, int32_t* writeLength)
```

**描述：**

获取当前节点所在Router页面的路径。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md) node | 指定的节点。 |
| char\* buffer | 缓冲区，页面路径写入该内存区域。 |
| int32\_t bufferSize | 缓冲区大小。 |
| int32\_t\* writeLength | 在返回[ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)时表示实际写入到缓冲区的字符串长度。 在返回[ARKUI\_ERROR\_CODE\_BUFFER\_SIZE\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)时表示可以容纳目标的最小缓冲区大小。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。  [ARKUI\_ERROR\_CODE\_GET\_INFO\_FAILED](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 查询信息失败。  [ARKUI\_ERROR\_CODE\_BUFFER\_SIZE\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 给定的buffer size小于可以容纳目标的最小缓冲区大小。 |

### OH\_ArkUI\_GetRouterPageState()

```c
ArkUI_ErrorCode OH_ArkUI_GetRouterPageState(ArkUI_NodeHandle node, ArkUI_RouterPageState* state)
```

**描述：**

获取当前节点所在Router页面的状态。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md) node | 指定的节点。 |
| [ArkUI\_RouterPageState](capi-navigation-router-h.md#arkui_routerpagestate)\* state | Router页面的状态值写回该参数中。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。  [ARKUI\_ERROR\_CODE\_GET\_INFO\_FAILED](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 查询信息失败。 |

### OH\_ArkUI\_GetRouterPageId()

```c
ArkUI_ErrorCode OH_ArkUI_GetRouterPageId(ArkUI_NodeHandle node, char* buffer, int32_t bufferSize, int32_t* writeLength)
```

**描述：**

获取当前节点所在Router页面的ID。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md) node | 指定的节点。 |
| char\* buffer | 缓冲区，页面ID写入该内存区域。 |
| int32\_t bufferSize | 缓冲区大小。 |
| int32\_t\* writeLength | 在返回[ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)时表示实际写入到缓冲区的字符串长度。 在返回[ARKUI\_ERROR\_CODE\_BUFFER\_SIZE\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)时表示可以容纳目标的最小缓冲区大小。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。  [ARKUI\_ERROR\_CODE\_GET\_INFO\_FAILED](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 查询信息失败。  [ARKUI\_ERROR\_CODE\_BUFFER\_SIZE\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 数据大小超过指定的缓冲区大小。 |

### OH\_ArkUI\_InitModuleForArkTSEnv()

```c
ArkUI_ErrorCode OH_ArkUI_InitModuleForArkTSEnv(napi_env env)
```

**描述：**

初始化指定上下文环境的ArkUI相关接口，适用于在Native侧使用ArkUI相关接口前进行上下文环境初始化的场景。该函数禁止在非UI线程中调用，否则程序将主动中止。使用该函数初始化指定上下文环境后，在对应环境销毁时调用[OH\_ArkUI\_NotifyArkTSEnvDestroy()](capi-native-node-napi-h.md#oh_arkui_notifyarktsenvdestroy)通知环境已销毁。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| napi\_env env | Node-API的环境指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 参数无效，可能原因是env为空或设置白名单失败；请检查env是否有效后重试。  [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) CAPI初始化错误，请确认当前运行环境支持ArkUI Native接口并重试。 |

### OH\_ArkUI\_NotifyArkTSEnvDestroy()

```c
void OH_ArkUI_NotifyArkTSEnvDestroy(napi_env env)
```

**描述：**

通知指定的上下文环境已销毁，适用于ArkTS上下文环境销毁时在Native侧同步清理相关状态的场景。使用[OH\_ArkUI\_InitModuleForArkTSEnv()](capi-native-node-napi-h.md#oh_arkui_initmoduleforarktsenv)初始化上下文环境后，应在该环境销毁时调用此函数。该函数禁止在非UI线程中调用，否则程序将主动中止。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| napi\_env env | Node-API的环境指针。 |

### OH\_ArkUI\_PostFrameCallback()

```c
int32_t OH_ArkUI_PostFrameCallback(ArkUI_ContextHandle uiContext, void* userData, void (*callback)(uint64_t nanoTimestamp, uint32_t frameCount, void* userData))
```

**描述：**

注册一个回调函数，以便在下一帧渲染时执行，适用于Native侧在下一帧执行界面刷新或渲染相关任务的场景。不允许在非UI线程调用；如果检查到在非UI线程调用，程序会主动中止。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_ContextHandle](capi-arkui-nativemodule-arkui-context8h.md) uiContext | [UIContext](ts-custom-component-api.md#uicontext)对象指针，用以绑定实例。 |
| void\* userData | 自定义事件参数，当事件触发时在回调参数中携带回来。 |
| void (\*callback)(uint64\_t nanoTimestamp, uint32\_t frameCount, void\* userData) | 自定义回调函数，签名为void (\*callback)(uint64\_t nanoTimestamp, uint32\_t frameCount, void\* userData)，用于在下一帧渲染时执行。其中nanoTimestamp表示帧信号的时间戳，frameCount表示帧号，userData表示注册时传入并在回调触发时携带回来的自定义数据。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) CAPI初始化错误，请确认ArkUI Native接口运行环境已完成初始化后重试。  [ARKUI\_ERROR\_CODE\_UI\_CONTEXT\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) uiContext对象无效，请检查uiContext是否为空或是否来自有效的UIContext对象。  [ARKUI\_ERROR\_CODE\_CALLBACK\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 回调函数无效，请检查callback是否为空。 |

### OH\_ArkUI\_PostIdleCallback()

```c
int32_t OH_ArkUI_PostIdleCallback(ArkUI_ContextHandle uiContext, void* userData, void (*callback)(uint64_t nanoTimeLeft, uint32_t frameCount, void* userData))
```

**描述：**

注册一个回调函数，适用于需要在Native侧利用帧间空闲时间处理非紧急任务的场景。下一帧渲染结束后，如果距离该帧之后的下一个VSync信号到来的剩余时间大于1ms，该回调函数将被执行；如果剩余时间小于1ms，回调函数将顺延至后续某一帧渲染结束后剩余时间大于1ms时执行。如果当前没有下一帧，将自动请求下一帧。不允许在非UI线程调用；如果检查到在非UI线程调用，程序会主动中止。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_ContextHandle](capi-arkui-nativemodule-arkui-context8h.md) uiContext | UIContext对象指针，用以绑定实例。 |
| void\* userData | 自定义事件参数，当自定义回调函数触发时在回调参数中携带回来。 |
| void (\*callback)(uint64\_t nanoTimeLeft, uint32\_t frameCount, void\* userData) | 自定义回调函数，签名为void (\*callback)(uint64\_t nanoTimeLeft, uint32\_t frameCount, void\* userData)，用于在下一帧渲染结束后，剩余时间大于1ms时执行。其中nanoTimeLeft表示距离当前帧截止时间的剩余时间，frameCount表示帧号，userData表示注册时传入并在回调触发时携带回来的自定义数据。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) CAPI初始化错误，请确认ArkUI Native接口运行环境已完成初始化后重试。  [ARKUI\_ERROR\_CODE\_UI\_CONTEXT\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) uiContext对象无效，请检查uiContext是否为空或是否来自有效的UIContext对象。  [ARKUI\_ERROR\_CODE\_CALLBACK\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 回调函数无效，请检查callback是否为空。 |

### OH\_ArkUI\_EnableEventPassthrough()

```c
ArkUI_ErrorCode OH_ArkUI_EnableEventPassthrough(ArkUI_ContextHandle uiContext, bool enabled, ArkUI_RawInputEventType type)
```

**描述：**

启用或禁用事件直通。事件直通表示在事件分发过程中，不经过[重采样](../harmonyos-guides/arkts-interaction-development-guide-touch-screen.md#重采样与历史点)直接下发给组件。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_ContextHandle](capi-arkui-nativemodule-arkui-context8h.md) uiContext | [UIContext](arkts-apis-uicontext-uicontext.md)对象，用以绑定实例。 |
| bool enabled | 启用或禁用事件直通。true表示启用事件直通，false表示禁用事件直通。 |
| [ArkUI\_RawInputEventType](capi-common-attributes-h.md#arkui_rawinputeventtype) type | 指定启用或禁用事件直通的原始输入事件类型[ArkUI\_RawInputEventType](capi-common-attributes-h.md#arkui_rawinputeventtype)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) UIContext对象无效。 |
