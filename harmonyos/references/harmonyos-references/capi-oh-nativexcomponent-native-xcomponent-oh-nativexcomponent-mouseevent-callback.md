---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-nativexcomponent-native-xcomponent-oh-nativexcomponent-mouseevent-callback
title: OH_NativeXComponent_MouseEvent_Callback
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 结构体 > OH_NativeXComponent_MouseEvent_Callback
category: harmonyos-references
scraped_at: 2026-09-02T15:01:23+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:c9f4fda40fc94981c55ed3d155db782c373806f1ade85a9ae7379133ad0656b8
---

```c
typedef struct OH_NativeXComponent_MouseEvent_Callback {...} OH_NativeXComponent_MouseEvent_Callback
```

## 概述

提供了鼠标事件和悬停事件的回调注册能力，开发者可通过该回调结构体监听NativeXComponent上的鼠标和手写笔交互行为，适用于需要在Native侧处理指针输入交互的场景。其中，DispatchMouseEvent侧重鼠标按键按下、释放、移动等组件内的操作行为，DispatchHoverEvent侧重鼠标或手写笔进入/离开组件的悬停状态变化，两者监听维度不同，可按需同时注册。

**起始版本：** 9

**相关模块：** [OH\_NativeXComponent Native XComponent](capi-oh-nativexcomponent-native-xcomponent.md)

**所在头文件：** [native\_interface\_xcomponent.h](capi-native-interface-xcomponent-h.md)

## 汇总

### 成员函数

| 名称 | 描述 |
| --- | --- |
| [void (\*DispatchMouseEvent)(OH\_NativeXComponent\* component, void\* window)](capi-oh-nativexcomponent-native-xcomponent-oh-nativexcomponent-mouseevent-callback.md#dispatchmouseevent) | 当鼠标事件被触发时调用。 |
| [void (\*DispatchHoverEvent)(OH\_NativeXComponent\* component, bool isHover)](capi-oh-nativexcomponent-native-xcomponent-oh-nativexcomponent-mouseevent-callback.md#dispatchhoverevent) | 当悬停事件被触发时调用。 |

## 成员函数说明

### DispatchMouseEvent()

```c
void (*DispatchMouseEvent)(OH_NativeXComponent* component, void* window)
```

**描述：**

当鼠标事件（例如鼠标按键按下、释放、移动等操作）被触发时调用。

**起始版本：** 9

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_NativeXComponent](capi-oh-nativexcomponent-native-xcomponent-oh-nativexcomponent.md)\* component | 表示指向[OH\_NativeXComponent](capi-oh-nativexcomponent-native-xcomponent-oh-nativexcomponent.md)实例的指针。 |
| void\* window | 表示触发鼠标事件时关联的NativeWindow句柄。 |

### DispatchHoverEvent()

```c
void (*DispatchHoverEvent)(OH_NativeXComponent* component, bool isHover)
```

**描述：**

当悬停事件被触发时调用。该函数在鼠标或手写笔进入或离开组件时触发。

**起始版本：** 9

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_NativeXComponent](capi-oh-nativexcomponent-native-xcomponent-oh-nativexcomponent.md)\* component | 表示指向[OH\_NativeXComponent](capi-oh-nativexcomponent-native-xcomponent-oh-nativexcomponent.md)实例的指针。 |
| bool isHover | 表示鼠标或手写笔是否悬停在组件上，进入时为true，离开时为false。 |
