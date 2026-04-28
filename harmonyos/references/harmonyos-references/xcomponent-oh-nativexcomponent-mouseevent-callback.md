---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xcomponent-oh-nativexcomponent-mouseevent-callback
title: OH_NativeXComponent_MouseEvent_Callback
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 结构体 > OH_NativeXComponent_MouseEvent_Callback
category: harmonyos-references
scraped_at: 2026-04-28T08:04:15+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:b1730cfba616b2aff7b88f79bed6f333398e69599526ef3021b78622ebefb252
---

```
1. typedef struct OH_NativeXComponent_MouseEvent_Callback {...} OH_NativeXComponent_MouseEvent_Callback
```

## 概述

PhonePC/2in1TabletTVWearable

注册鼠标事件的回调。

**起始版本：** 9

**相关模块：** [OH\_NativeXComponent Native XComponent](capi-oh-nativexcomponent-native-xcomponent.md)

**所在头文件：** [native\_interface\_xcomponent.h](capi-native-interface-xcomponent-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员函数

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [void (\*DispatchMouseEvent)(OH\_NativeXComponent\* component, void\* window)](xcomponent-oh-nativexcomponent-mouseevent-callback.md#dispatchmouseevent) | 当鼠标事件被触发时调用。 |
| [void (\*DispatchHoverEvent)(OH\_NativeXComponent\* component, bool isHover)](xcomponent-oh-nativexcomponent-mouseevent-callback.md#dispatchhoverevent) | 当悬停事件被触发时调用。 |

## 成员函数说明

PhonePC/2in1TabletTVWearable

### DispatchMouseEvent()

PhonePC/2in1TabletTVWearable

```
1. void (*DispatchMouseEvent)(OH_NativeXComponent* component, void* window)
```

**描述：**

当鼠标事件被触发时调用。

**起始版本：** 9

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_NativeXComponent](vexcomponent-native-xcomponent-oh-nativexcomponent.md)\* component | 表示指向[OH\_NativeXComponent](vexcomponent-native-xcomponent-oh-nativexcomponent.md)实例的指针。 |
| void\* window | 表示NativeWindow句柄。 |

### DispatchHoverEvent()

PhonePC/2in1TabletTVWearable

```
1. void (*DispatchHoverEvent)(OH_NativeXComponent* component, bool isHover)
```

**描述：**

当悬停事件被触发时调用。

**起始版本：** 9

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_NativeXComponent](vexcomponent-native-xcomponent-oh-nativexcomponent.md)\* component | 表示指向[OH\_NativeXComponent](vexcomponent-native-xcomponent-oh-nativexcomponent.md)实例的指针。 |
| bool isHover | 表示鼠标或手写笔是否悬浮在组件上，进入时为true，离开时为false。 |
