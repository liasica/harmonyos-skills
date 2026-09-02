---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativeanimateapi-1
title: ArkUI_NativeAnimateAPI_1
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 结构体 > ArkUI_NativeAnimateAPI_1
category: harmonyos-references
scraped_at: 2026-09-02T15:01:22+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:5fd633b5f6ee246bf5269306ea7aee1710908926c40e162fc3f14e0b0e3b5431
---

```c
typedef struct {...} ArkUI_NativeAnimateAPI_1
```

## 概述

ArkUI（方舟UI框架）提供的Native侧动画接口集合。

**起始版本：** 12

**相关模块：** [ArkUI\_NativeModule](capi-arkui-nativemodule.md)

**所在头文件：** [native\_animate.h](capi-native-animate-h.md)

## 汇总

### 成员函数

| 名称 | 描述 |
| --- | --- |
| [int32\_t (\*animateTo)(ArkUI\_ContextHandle context, ArkUI\_AnimateOption\* option, ArkUI\_ContextCallback\* update, ArkUI\_AnimateCompleteCallback\* complete)](capi-arkui-nativemodule-arkui-nativeanimateapi-1.md#animateto) | 触发显式动画。 |
| [int32\_t (\*keyframeAnimateTo)(ArkUI\_ContextHandle context, ArkUI\_KeyframeAnimateOption\* option)](capi-arkui-nativemodule-arkui-nativeanimateapi-1.md#keyframeanimateto) | 触发关键帧动画。 |
| [ArkUI\_AnimatorHandle (\*createAnimator)(ArkUI\_ContextHandle context, ArkUI\_AnimatorOption\* option)](capi-arkui-nativemodule-arkui-nativeanimateapi-1.md#createanimator) | 创建animator动画对象并返回其指针（调用者获取对象所有权）。 |
| [void (\*disposeAnimator)(ArkUI\_AnimatorHandle animatorHandle)](capi-arkui-nativemodule-arkui-nativeanimateapi-1.md#disposeanimator) | 销毁传入指针所指向的animator动画对象，并释放其内存，销毁后不可再使用该指针。 |

## 成员函数说明

### animateTo()

```c
int32_t (*animateTo)(ArkUI_ContextHandle context, ArkUI_AnimateOption* option, ArkUI_ContextCallback* update, ArkUI_AnimateCompleteCallback* complete)
```

**描述：**

执行显式动画过渡效果。

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_ContextHandle](capi-arkui-nativemodule-arkui-context8h.md) context | UI上下文实例，用于指定动画所在的UI上下文环境，不可为NULL。 |
| [ArkUI\_AnimateOption](capi-arkui-nativemodule-arkui-animateoption.md)\* option | 动画效果配置参数，不可为NULL。 |
| [ArkUI\_ContextCallback](capi-arkui-nativemodule-arkui-contextcallback.md)\* update | 指定动效的闭包函数。在闭包函数中产生的状态变化，系统会自动插入过渡动画。传参不可为NULL。  **说明**：在闭包函数中要设置的组件属性，必须在调用animateTo之前已在组件上设置过。 |
| [ArkUI\_AnimateCompleteCallback](capi-arkui-nativemodule-arkui-animatecompletecallback.md)\* complete | 动画播放完成回调函数。传参为NULL时不设置完成回调通知。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常，请检查传入参数的类型和有效性。可能原因：context无效、option为NULL或配置不合理。解决措施：确保context有效、option配置正确且非NULL。 |

### keyframeAnimateTo()

```c
int32_t (*keyframeAnimateTo)(ArkUI_ContextHandle context, ArkUI_KeyframeAnimateOption* option)
```

**描述：**

关键帧动画接口，通过指定关键帧定义属性在不同时间节点的值，系统根据插值算法自动计算中间帧的属性值实现平滑过渡。关键帧参数配置详见[ArkUI\_KeyframeAnimateOption](capi-arkui-nativemodule-arkui-keyframeanimateoption.md)。与animateTo的显式过渡动画不同，keyframeAnimateTo适用于需要在多个时间节点定义不同动画状态的场景。选取原则：仅需起始到结束状态的过渡动画时使用animateTo，需多关键帧精细控制动画过程时使用keyframeAnimateTo。

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_ContextHandle](capi-arkui-nativemodule-arkui-context8h.md) context | UI上下文实例，用于指定关键帧动画所在的UI上下文环境，不可为NULL。 |
| [ArkUI\_KeyframeAnimateOption](capi-arkui-nativemodule-arkui-keyframeanimateoption.md)\* option | 关键帧动画参数，设置关键帧动画的配置参数，包括关键帧的时间节点、动画属性值及过渡效果等，不可为NULL。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常，请检查传入参数的类型和有效性。可能原因：context无效、option为NULL或配置不合理。解决措施：确保context有效、option配置正确且非NULL。 |

### createAnimator()

```c
ArkUI_AnimatorHandle (*createAnimator)(ArkUI_ContextHandle context, ArkUI_AnimatorOption* option)
```

**描述：**

创建animator动画对象并返回其指针。与animateTo/keyframeAnimateTo的触发式动画不同，createAnimator创建可持久控制的动画对象，适用于需要反复启动、停止、监听状态等精细控制的动画场景。选取原则：一次性过渡动画使用animateTo或keyframeAnimateTo，需持久控制动画生命周期时使用createAnimator。

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_ContextHandle](capi-arkui-nativemodule-arkui-context8h.md) context | UI上下文实例，用于指定动画所在的UI上下文环境，不可为NULL。 |
| [ArkUI\_AnimatorOption](capi-arkui-nativemodule-arkui-animatoroption.md)\* option | animator动画参数，不可为NULL。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_AnimatorHandle](capi-arkui-nativemodule-arkui-animator8h.md) | animator动画对象指针，用于后续对动画对象进行控制。函数参数异常时返回NULL。 |

### disposeAnimator()

```c
void (*disposeAnimator)(ArkUI_AnimatorHandle animatorHandle)
```

**描述：**

销毁animator动画对象并释放其内存，销毁后不可再使用该handle。传入NULL或已销毁的句柄时，函数不执行销毁操作。

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_AnimatorHandle](capi-arkui-nativemodule-arkui-animator8h.md) animatorHandle | animator动画对象，必须为由createAnimator创建的有效handle，不可传入已销毁的对象。 |
