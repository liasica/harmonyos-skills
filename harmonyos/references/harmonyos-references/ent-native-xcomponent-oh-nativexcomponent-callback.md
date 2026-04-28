---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ent-native-xcomponent-oh-nativexcomponent-callback
title: OH_NativeXComponent_Callback
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 结构体 > OH_NativeXComponent_Callback
category: harmonyos-references
scraped_at: 2026-04-28T08:04:15+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:8ed059ce298966a447c9c97a8c30f0c2eed7055306752b34b6b1384ed071b5e4
---

```
1. typedef struct OH_NativeXComponent_Callback {...} OH_NativeXComponent_Callback
```

## 概述

PhonePC/2in1TabletTVWearable

注册Surface生命周期和触摸事件回调。

**起始版本：** 8

**相关模块：** [OH\_NativeXComponent Native XComponent](capi-oh-nativexcomponent-native-xcomponent.md)

**所在头文件：** [native\_interface\_xcomponent.h](capi-native-interface-xcomponent-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员函数

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [void (\*OnSurfaceCreated)(OH\_NativeXComponent\* component, void\* window)](ent-native-xcomponent-oh-nativexcomponent-callback.md#onsurfacecreated) | 创建Surface时调用。 |
| [void (\*OnSurfaceChanged)(OH\_NativeXComponent\* component, void\* window)](ent-native-xcomponent-oh-nativexcomponent-callback.md#onsurfacechanged) | 当Surface改变时调用。 |
| [void (\*OnSurfaceDestroyed)(OH\_NativeXComponent\* component, void\* window)](ent-native-xcomponent-oh-nativexcomponent-callback.md#onsurfacedestroyed) | 当Surface被销毁时调用。 |
| [void (\*DispatchTouchEvent)(OH\_NativeXComponent\* component, void\* window)](ent-native-xcomponent-oh-nativexcomponent-callback.md#dispatchtouchevent) | 当触摸事件被触发时调用。 |

## 成员函数说明

PhonePC/2in1TabletTVWearable

### OnSurfaceCreated()

PhonePC/2in1TabletTVWearable

```
1. void (*OnSurfaceCreated)(OH_NativeXComponent* component, void* window)
```

**描述：**

创建Surface时调用。

**起始版本：** 8

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_NativeXComponent](vexcomponent-native-xcomponent-oh-nativexcomponent.md)\* component | 表示指向[OH\_NativeXComponent](vexcomponent-native-xcomponent-oh-nativexcomponent.md)实例的指针。 |
| void\* window | 表示NativeWindow句柄。  通过XComponent生命周期获取的NativeWindow本身由系统侧持有了一次引用计数，并会在OnSurfaceDestroyed回调触发之后将引用计数减一，引用计数归零后NativeWindow将被释放。 |

### OnSurfaceChanged()

PhonePC/2in1TabletTVWearable

```
1. void (*OnSurfaceChanged)(OH_NativeXComponent* component, void* window)
```

**描述：**

当Surface改变时调用。

**起始版本：** 8

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_NativeXComponent](vexcomponent-native-xcomponent-oh-nativexcomponent.md)\* component | 表示指向[OH\_NativeXComponent](vexcomponent-native-xcomponent-oh-nativexcomponent.md)实例的指针。 |
| void\* window | 表示NativeWindow句柄。 |

### OnSurfaceDestroyed()

PhonePC/2in1TabletTVWearable

```
1. void (*OnSurfaceDestroyed)(OH_NativeXComponent* component, void* window)
```

**描述：**

当Surface被销毁时调用。

**起始版本：** 8

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_NativeXComponent](vexcomponent-native-xcomponent-oh-nativexcomponent.md)\* component | 表示指向[OH\_NativeXComponent](vexcomponent-native-xcomponent-oh-nativexcomponent.md)实例的指针。 |
| void\* window | 表示NativeWindow句柄。 |

### DispatchTouchEvent()

PhonePC/2in1TabletTVWearable

```
1. void (*DispatchTouchEvent)(OH_NativeXComponent* component, void* window)
```

**描述：**

当触摸事件被触发时调用。

**起始版本：** 8

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_NativeXComponent](vexcomponent-native-xcomponent-oh-nativexcomponent.md)\* component | 表示指向[OH\_NativeXComponent](vexcomponent-native-xcomponent-oh-nativexcomponent.md)实例的指针。 |
| void\* window | 表示NativeWindow句柄。 |
