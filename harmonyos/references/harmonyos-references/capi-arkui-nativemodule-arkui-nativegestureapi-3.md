---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativegestureapi-3
title: ArkUI_NativeGestureAPI_3
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 结构体 > ArkUI_NativeGestureAPI_3
category: harmonyos-references
scraped_at: 2026-09-02T15:01:25+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:57203734e1ff1b52efae0f1902e4590c677da8e4663f5fc2f0ab1b5f4c140bf3
---

```c
typedef struct {...} ArkUI_NativeGestureAPI_3
```

## 概述

定义手势模块接口集合。包含[ArkUI\_NativeGestureAPI\_1](capi-arkui-nativemodule-arkui-nativegestureapi-1.md)、[ArkUI\_NativeGestureAPI\_2](capi-arkui-nativemodule-arkui-nativegestureapi-2.md)结构体中的手势接口及新增手势接口，支持为ArkUI节点设置并行手势事件回调，适用于需要进行并行手势识别处理的交互场景。

**起始版本：** 26.0.0

**相关模块：** [ArkUI\_NativeModule](capi-arkui-nativemodule.md)

**所在头文件：** [native\_gesture.h](capi-native-gesture-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| [ArkUI\_NativeGestureAPI\_2](capi-arkui-nativemodule-arkui-nativegestureapi-2.md)\* gestureApi2 | 指向ArkUI\_NativeGestureAPI\_2结构体的指针。 |

### 成员函数

| 名称 | 描述 |
| --- | --- |
| [ArkUI\_ErrorCode (\*setGestureParallelTo)(ArkUI\_NodeHandle node, void\* userData, ArkUI\_GestureRecognizer\* (\*parallelGesture)(ArkUI\_ParallelGestureEvent\* event))](capi-arkui-nativemodule-arkui-nativegestureapi-3.md#setgestureparallelto) | 设置并行手势事件的回调函数。 |

## 成员函数说明

### setGestureParallelTo()

```c
ArkUI_ErrorCode (*setGestureParallelTo)(ArkUI_NodeHandle node, void* userData, ArkUI_GestureRecognizer* (*parallelGesture)(ArkUI_ParallelGestureEvent* event))
```

**描述：**

设置并行手势事件的回调函数。此接口适用于开发者自定义手势与响应链上其他组件手势需要并行处理的场景。

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md) node | 需要设置并行手势事件回调的ArkUI节点指针。 |
| void\* userData | 用户自定义数据，在并行手势事件回调中传递调用方自定义上下文信息。不需要关联自定义上下文时可传入nullptr。传入非空指针时，调用者需要确保数据的生命周期安全，若数据在回调过程中被释放可能导致回调执行异常。 |
| ArkUI\_GestureRecognizer\* (\*parallelGesture)(ArkUI\_ParallelGestureEvent\* event) | 并行手势事件的回调函数。event为并行手势事件对象，包含触发该回调时的手势事件信息；parallelGesture返回需要并行识别的手势识别器指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回[ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)表示成功。  返回[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)表示参数错误。 |
