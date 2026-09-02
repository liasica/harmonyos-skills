---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-nativexcomponent-native-xcomponent-oh-nativexcomponent-callback
title: OH_NativeXComponent_Callback
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 结构体 > OH_NativeXComponent_Callback
category: harmonyos-references
scraped_at: 2026-09-02T15:01:23+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:c69cd543f7af36f972f1a455a765658ac04b47176a18a7f6afb111c961a427f6
---

```c
typedef struct OH_NativeXComponent_Callback {...} OH_NativeXComponent_Callback
```

## 概述

OH\_NativeXComponent\_Callback用于注册XComponent的Surface生命周期（创建、改变、销毁）和触摸事件回调。适用于需要在Native侧感知Surface状态变化并处理用户触摸交互的场景。

**起始版本：** 8

**相关模块：** [OH\_NativeXComponent Native XComponent](capi-oh-nativexcomponent-native-xcomponent.md)

**所在头文件：** [native\_interface\_xcomponent.h](capi-native-interface-xcomponent-h.md)

## 汇总

### 成员函数

| 名称 | 描述 |
| --- | --- |
| [void (\*OnSurfaceCreated)(OH\_NativeXComponent\* component, void\* window)](capi-oh-nativexcomponent-native-xcomponent-oh-nativexcomponent-callback.md#onsurfacecreated) | 当Surface创建时调用。 |
| [void (\*OnSurfaceChanged)(OH\_NativeXComponent\* component, void\* window)](capi-oh-nativexcomponent-native-xcomponent-oh-nativexcomponent-callback.md#onsurfacechanged) | 当Surface尺寸发生改变时调用。 |
| [void (\*OnSurfaceDestroyed)(OH\_NativeXComponent\* component, void\* window)](capi-oh-nativexcomponent-native-xcomponent-oh-nativexcomponent-callback.md#onsurfacedestroyed) | 当Surface被销毁时调用。 |
| [void (\*DispatchTouchEvent)(OH\_NativeXComponent\* component, void\* window)](capi-oh-nativexcomponent-native-xcomponent-oh-nativexcomponent-callback.md#dispatchtouchevent) | 当触摸事件被分发时调用。 |

## 成员函数说明

### OnSurfaceCreated()

```c
void (*OnSurfaceCreated)(OH_NativeXComponent* component, void* window)
```

**描述：**

当Surface创建时调用。

**起始版本：** 8

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_NativeXComponent](capi-oh-nativexcomponent-native-xcomponent-oh-nativexcomponent.md)\* component | 表示指向OH\_NativeXComponent实例的指针。 |
| void\* window | 表示NativeWindow句柄。  通过XComponent生命周期获取的NativeWindow本身由系统侧持有了一次引用计数，并会在OnSurfaceDestroyed回调触发之后将引用计数减一，引用计数归零后NativeWindow将被释放。 |

### OnSurfaceChanged()

```c
void (*OnSurfaceChanged)(OH_NativeXComponent* component, void* window)
```

**描述：**

当Surface尺寸发生改变时调用。

**起始版本：** 8

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_NativeXComponent](capi-oh-nativexcomponent-native-xcomponent-oh-nativexcomponent.md)\* component | 表示指向OH\_NativeXComponent实例的指针。 |
| void\* window | 表示NativeWindow句柄。该句柄在Surface尺寸或格式发生变化时传入，开发者可通过该句柄感知Surface的最新状态并更新渲染配置。 |

### OnSurfaceDestroyed()

```c
void (*OnSurfaceDestroyed)(OH_NativeXComponent* component, void* window)
```

**描述：**

当Surface被销毁时调用。

**起始版本：** 8

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_NativeXComponent](capi-oh-nativexcomponent-native-xcomponent-oh-nativexcomponent.md)\* component | 表示指向OH\_NativeXComponent实例的指针。 |
| void\* window | 表示NativeWindow句柄。此回调触发后，系统侧持有的NativeWindow引用计数将减一，引用计数归零后NativeWindow将被释放，请勿在此回调之后继续使用该window句柄。 |

### DispatchTouchEvent()

```c
void (*DispatchTouchEvent)(OH_NativeXComponent* component, void* window)
```

**描述：**

当触摸事件被分发时调用，开发者可在此回调中获取触摸事件数据以实现自定义交互逻辑（如手势识别、自定义绘制等）。

**起始版本：** 8

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_NativeXComponent](capi-oh-nativexcomponent-native-xcomponent-oh-nativexcomponent.md)\* component | 表示指向OH\_NativeXComponent实例的指针。 |
| void\* window | 表示NativeWindow句柄。  通过XComponent生命周期获取的NativeWindow本身由系统侧持有了一次引用计数，并会在OnSurfaceDestroyed回调触发之后将引用计数减一，引用计数归零后NativeWindow将被释放。 |
