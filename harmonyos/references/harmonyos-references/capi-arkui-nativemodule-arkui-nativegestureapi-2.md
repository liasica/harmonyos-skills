---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativegestureapi-2
title: ArkUI_NativeGestureAPI_2
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 结构体 > ArkUI_NativeGestureAPI_2
category: harmonyos-references
scraped_at: 2026-09-02T15:01:23+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:cf046e957fefdfc34dfadb2fcd4547f1aa8bab22553278c9652309a8c63f87a7
---

```c
typedef struct {...} ArkUI_NativeGestureAPI_2
```

## 概述

定义手势模块接口集合，在[ArkUI\_NativeGestureAPI\_1](capi-arkui-nativemodule-arkui-nativegestureapi-1.md)的基础上扩展提供设置手势打断事件回调的能力，用于在手势处理过程中根据回调结果继续或打断手势。开发者可以通过[gestureApi1](capi-arkui-nativemodule-arkui-nativegestureapi-2.md#成员变量)访问基础手势接口，配合[setGestureInterrupterToNode](capi-arkui-nativemodule-arkui-nativegestureapi-2.md#setgestureinterruptertonode)实现完整的手势打断处理功能。

**起始版本：** 18

**相关模块：** [ArkUI\_NativeModule](capi-arkui-nativemodule.md)

**所在头文件：** [native\_gesture.h](capi-native-gesture-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| [ArkUI\_NativeGestureAPI\_1](capi-arkui-nativemodule-arkui-nativegestureapi-1.md)\* gestureApi1 | 指向ArkUI\_NativeGestureAPI\_1结构体的指针。 |

### 成员函数

| 名称 | 描述 |
| --- | --- |
| [int32\_t (\*setGestureInterrupterToNode)(ArkUI\_NodeHandle node, void\* userData, ArkUI\_GestureInterruptResult (\*interrupter)(ArkUI\_GestureInterruptInfo\* info))](capi-arkui-nativemodule-arkui-nativegestureapi-2.md#setgestureinterruptertonode) | 设置手势打断事件的回调函数。 |

## 成员函数说明

### setGestureInterrupterToNode()

```c
int32_t (*setGestureInterrupterToNode)(ArkUI_NodeHandle node, void* userData, ArkUI_GestureInterruptResult (*interrupter)(ArkUI_GestureInterruptInfo* info))
```

**描述：**

设置手势打断事件的回调函数，适用于需要在手势识别过程中根据当前交互状态决定手势继续响应或中断的场景，例如处理手势响应冲突。

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md) node | 需要被设置手势打断回调的ArkUI节点指针。 |
| void\* userData | 用户自定义数据，用于在设置手势打断回调时关联调用方自定义的上下文数据，供回调执行处理逻辑时使用；不需要关联自定义上下文时可传入nullptr。 |
| [ArkUI\_GestureInterruptResult](capi-native-gesture-h.md#arkui_gestureinterruptresult) (\*interrupter)([ArkUI\_GestureInterruptInfo](capi-arkui-nativemodule-arkui-gestureinterruptinfo.md)\* info) | 手势打断回调，info提供手势打断数据。interrupter返回GESTURE\_INTERRUPT\_RESULT\_CONTINUE时手势正常进行，适用于允许手势继续响应的场景；返回GESTURE\_INTERRUPT\_RESULT\_REJECT时手势打断，适用于需要优先处理其他手势或交互的场景。设置此参数为nullptr时将取消注册回调函数。  **说明：** 该手势打断回调注册后，后续在单次手势处理流程中都会存在。即使在同一次手势处理流程中使用setGestureInterrupterToNode接口将手势打断回调重置为nullptr，或者使用[dispose](capi-arkui-nativemodule-arkui-nativegestureapi-1.md#dispose)接口使即将被触发的手势销毁，该回调在满足触发条件后仍会响应。如果在该回调中使用到的对象，在回调触发前可能已被释放，需要确保该对象在回调触发期间仍可安全访问。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 参数错误。 |
