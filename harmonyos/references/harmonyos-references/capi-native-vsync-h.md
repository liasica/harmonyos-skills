---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-vsync-h
title: native_vsync.h
breadcrumb: API参考 > 图形 > ArkGraphics 2D（方舟2D图形服务） > C API > 头文件 > native_vsync.h
category: harmonyos-references
scraped_at: 2026-04-28T08:15:06+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:49e733d71a51ba5acce7d2b5fcfaedba2e7574fb89a62a9457e269504ddc754e
---

## 概述

PhonePC/2in1TabletTVWearable

定义获取和使用NativeVsync的相关函数。

**引用文件：** <native\_vsync/native\_vsync.h>

**库：** libnative\_vsync.so

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeVsync

**起始版本：** 9

**相关模块：** [NativeVsync](capi-nativevsync.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 结构体

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [OH\_NativeVSync\_ExpectedRateRange](capi-nativevsync-oh-nativevsync-expectedraterange.md) | OH\_NativeVSync\_ExpectedRateRange | 期望帧率范围结构体。 |
| [OH\_NativeVSync](capi-nativevsync-oh-nativevsync.md) | OH\_NativeVSync | 提供OH\_NativeVSync结构体声明。 |

### 函数

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [typedef void (\*OH\_NativeVSync\_FrameCallback)(long long timestamp, void \*data)](capi-native-vsync-h.md#oh_nativevsync_framecallback) | OH\_NativeVSync\_FrameCallback | VSync回调函数类型。 |
| [OH\_NativeVSync\* OH\_NativeVSync\_Create(const char\* name, unsigned int length)](capi-native-vsync-h.md#oh_nativevsync_create) | - | 创建一个OH\_NativeVSync实例，每次调用都会产生一个新的实例。  本接口需要与[OH\_NativeVSync\_Destroy](capi-native-vsync-h.md#oh_nativevsync_destroy)接口配合使用，否则会存在内存泄露。 |
| [OH\_NativeVSync\* OH\_NativeVSync\_Create\_ForAssociatedWindow(uint64\_t windowID, const char\* name, unsigned int length)](capi-native-vsync-h.md#oh_nativevsync_create_forassociatedwindow) | - | 创建一个和窗口绑定的OH\_NativeVSync实例，每次调用都会产生一个新的实例。  使用本接口创建出来的OH\_NativeVSync实例的实际vsync周期与系统vsync周期不完全一致，系统会根据窗口的状态对实际vsync周期进行调整。 |
| [void OH\_NativeVSync\_Destroy(OH\_NativeVSync\* nativeVsync)](capi-native-vsync-h.md#oh_nativevsync_destroy) | - | 销毁OH\_NativeVSync实例。  销毁后的OH\_NativeVSync指针不能再继续使用，否则会有野指针问题，尤其需要注意多线程并发时对于OH\_NativeVSync指针的管理。 |
| [int OH\_NativeVSync\_RequestFrame(OH\_NativeVSync\* nativeVsync, OH\_NativeVSync\_FrameCallback callback, void\* data)](capi-native-vsync-h.md#oh_nativevsync_requestframe) | - | 请求下一次vsync信号，当信号到来时，调用回调函数callback。  如果在同一帧内中多次调用此接口，则只会触发最后一个回调。  如果此接口与[OH\_NativeVSync\_RequestFrameWithMultiCallback](capi-native-vsync-h.md#oh_nativevsync_requestframewithmulticallback)接口在同一帧内被调用，则此接口的功能不会生效。 |
| [int OH\_NativeVSync\_RequestFrameWithMultiCallback(OH\_NativeVSync\* nativeVsync, OH\_NativeVSync\_FrameCallback callback, void\* data)](capi-native-vsync-h.md#oh_nativevsync_requestframewithmulticallback) | - | 请求下一次vsync信号，当信号到来时，调用回调函数callback。  如果在同一帧内中多次调用此接口，每一次传入的callback都会被执行。 |
| [int OH\_NativeVSync\_GetPeriod(OH\_NativeVSync\* nativeVsync, long long\* period)](capi-native-vsync-h.md#oh_nativevsync_getperiod) | - | 获取vsync周期。  vsync周期是在每次使用OH\_NativeVSync\_RequestFrame接口请求vsync信号后收到OH\_NativeVSync\_FrameCallback回调的时候才会更新。  首次使用该接口获取vsync周期之前，需要先使用OH\_NativeVSync\_RequestFrame接口请求vsync信号，在收到OH\_NativeVSync\_FrameCallback回调之后，才可以通过该接口获取到vsync周期。 |
| [int OH\_NativeVSync\_DVSyncSwitch(OH\_NativeVSync\* nativeVsync, bool enable)](capi-native-vsync-h.md#oh_nativevsync_dvsyncswitch) | - | 启用DVSync以提高自绘制动画场景的流畅性。  DVSync是Decoupled VSync的缩写，它是一种与硬件VSync解耦的帧时序管理策略。  DVSync通过提前发送带有未来时间戳的VSync信号驱动后续动画帧的提前绘制，这些帧会被帧缓冲队列缓存；DVSync通过缓存的帧减少未来可能发生的丢帧，进而提高动画场景的流畅性。  因为DVSync需要占用空闲的自绘制帧缓冲用于缓存提前绘制的动画帧，用户需要确保至少有一个空闲的帧缓冲区，否则不建议启用此功能。  启用DVSync后，用户需要正确响应提前发送的VSync信号，并在前一个VSync对应的动画帧完成后再请求下一个VSync，且自绘制帧需要携带与VSync一致的时间戳。  在动画结束之后，用户需要关闭DVSync。  在不支持DVSync的平台或者如果有另一个应用程序已经启用了DVSync，则当前的启用操作将不会生效，应用程序仍将收到正常的VSync信号。 |
| [int OH\_NativeVSync\_SetExpectedFrameRateRange(OH\_NativeVSync\* nativeVsync, OH\_NativeVSync\_ExpectedRateRange\* range)](capi-native-vsync-h.md#oh_nativevsync_setexpectedframeraterange) | - | 设置VSync期望帧率以及期望帧率的范围。 |

## 函数说明

PhonePC/2in1TabletTVWearable

### OH\_NativeVSync\_FrameCallback()

PhonePC/2in1TabletTVWearable

```
1. typedef void (*OH_NativeVSync_FrameCallback)(long long timestamp, void *data)
```

**描述**

VSync回调函数类型。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeVsync

**起始版本：** 9

**参数：**

| 参数项 | 描述 |
| --- | --- |
| long long timestamp | VSync使用CLOCK\_MONOTONIC获取的系统时间戳, 单位为纳秒。 |
| void \*data | 用户自定义数据。 |

### OH\_NativeVSync\_Create()

PhonePC/2in1TabletTVWearable

```
1. OH_NativeVSync* OH_NativeVSync_Create(const char* name, unsigned int length)
```

**描述**

创建一个OH\_NativeVSync实例，每次调用都会产生一个新的实例。

本接口需要与[OH\_NativeVSync\_Destroy](capi-native-vsync-h.md#oh_nativevsync_destroy)接口配合使用，否则会存在内存泄露。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeVsync

**起始版本：** 9

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const char\* name | 表示一个名字，与创建的OH\_NativeVSync实例关联。 |
| unsigned int length | name的长度（字符数）。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_NativeVSync](capi-nativevsync-oh-nativevsync.md)\* | 返回一个指向OH\_NativeVSync实例的指针。 |

### OH\_NativeVSync\_Create\_ForAssociatedWindow()

PhonePC/2in1TabletTVWearable

```
1. OH_NativeVSync* OH_NativeVSync_Create_ForAssociatedWindow(uint64_t windowID, const char* name, unsigned int length)
```

**描述**

创建一个和窗口绑定的OH\_NativeVSync实例，每次调用都会产生一个新的实例。

使用本接口创建出来的OH\_NativeVSync实例的实际vsync周期与系统vsync周期不完全一致，系统会根据窗口的状态对实际vsync周期进行调整。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeVsync

**起始版本：** 14

**参数：**

| 参数项 | 描述 |
| --- | --- |
| uint64\_t windowID | 表示窗口ID，窗口子进程索引标识符，可以通过[OH\_NativeWindow\_GetSurfaceId](capi-external-window-h.md#oh_nativewindow_getsurfaceid)接口获取。 |
| const char\* name | 表示一个名称，与创建的OH\_NativeVSync实例关联。 |
| unsigned int length | name的长度（字符数）。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_NativeVSync](capi-nativevsync-oh-nativevsync.md)\* | 返回一个指向OH\_NativeVSync实例的指针。 |

### OH\_NativeVSync\_Destroy()

PhonePC/2in1TabletTVWearable

```
1. void OH_NativeVSync_Destroy(OH_NativeVSync* nativeVsync)
```

**描述**

销毁OH\_NativeVSync实例。

销毁后的OH\_NativeVSync指针不能再继续使用，否则会有野指针问题，尤其需要注意多线程并发时对于OH\_NativeVSync指针的管理。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeVsync

**起始版本：** 9

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_NativeVSync](capi-nativevsync-oh-nativevsync.md)\* nativeVsync | 一个指向OH\_NativeVSync实例的指针。 |

### OH\_NativeVSync\_RequestFrame()

PhonePC/2in1TabletTVWearable

```
1. int OH_NativeVSync_RequestFrame(OH_NativeVSync* nativeVsync, OH_NativeVSync_FrameCallback callback, void* data)
```

**描述**

请求下一次vsync信号，当信号到来时，调用回调函数callback。

如果在同一帧内中多次调用此接口，则只会触发最后一个回调。

如果此接口与[OH\_NativeVSync\_RequestFrameWithMultiCallback](capi-native-vsync-h.md#oh_nativevsync_requestframewithmulticallback)接口在同一帧内被调用，则此接口的功能不会生效。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeVsync

**起始版本：** 9

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_NativeVSync](capi-nativevsync-oh-nativevsync.md)\* nativeVsync | 一个指向OH\_NativeVSync实例的指针。 |
| [OH\_NativeVSync\_FrameCallback](capi-native-vsync-h.md#oh_nativevsync_framecallback) callback | 一个OH\_NativeVSync\_FrameCallback类型的函数指针，当下一次vsync信号到来时会被调用。 |
| void\* data | 一个指向用户自定义数据结构的指针，类型是void。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回值为0表示执行成功，其他返回值可参考[OHNativeErrorCode](capi-graphic-error-code-h.md#ohnativeerrorcode)。 |

### OH\_NativeVSync\_RequestFrameWithMultiCallback()

PhonePC/2in1TabletTVWearable

```
1. int OH_NativeVSync_RequestFrameWithMultiCallback(OH_NativeVSync* nativeVsync, OH_NativeVSync_FrameCallback callback, void* data)
```

**描述**

请求下一次vsync信号，当信号到来时，调用回调函数callback。

如果在同一帧内中多次调用此接口，每一次传入的callback都会被执行。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeVsync

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_NativeVSync](capi-nativevsync-oh-nativevsync.md)\* nativeVsync | 一个指向OH\_NativeVSync实例的指针。 |
| [OH\_NativeVSync\_FrameCallback](capi-native-vsync-h.md#oh_nativevsync_framecallback) callback | 一个OH\_NativeVSync\_FrameCallback类型的函数指针，当下一次vsync信号到来时会被调用。 |
| void\* data | 一个指向用户自定义数据结构的指针，类型是void。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回值为0表示执行成功，其他返回值可参考[OHNativeErrorCode](capi-graphic-error-code-h.md#ohnativeerrorcode)。 |

### OH\_NativeVSync\_GetPeriod()

PhonePC/2in1TabletTVWearable

```
1. int OH_NativeVSync_GetPeriod(OH_NativeVSync* nativeVsync, long long* period)
```

**描述**

获取vsync周期。

vsync周期是在每次使用OH\_NativeVSync\_RequestFrame接口请求vsync信号后收到OH\_NativeVSync\_FrameCallback回调的时候才会更新。

首次使用该接口获取vsync周期之前，需要先使用OH\_NativeVSync\_RequestFrame接口请求vsync信号，在收到OH\_NativeVSync\_FrameCallback回调之后，才可以通过该接口获取到vsync周期。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeVsync

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_NativeVSync](capi-nativevsync-oh-nativevsync.md)\* nativeVsync | 一个指向OH\_NativeVSync实例的指针。 |
| long long\* period | 表示vsync周期，作为出参使用。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回值为0表示执行成功，其他返回值可参考[OHNativeErrorCode](capi-graphic-error-code-h.md#ohnativeerrorcode)。 |

### OH\_NativeVSync\_DVSyncSwitch()

PhonePC/2in1TabletTVWearable

```
1. int OH_NativeVSync_DVSyncSwitch(OH_NativeVSync* nativeVsync, bool enable)
```

**描述**

启用DVSync以提高自绘制动画场景的流畅性。

DVSync是Decoupled VSync的缩写，它是一种与硬件VSync解耦的帧时序管理策略。

DVSync通过提前发送带有未来时间戳的VSync信号驱动后续动画帧的提前绘制，这些帧会被帧缓冲队列缓存；DVSync通过缓存的帧减少未来可能发生的丢帧，进而提高动画场景的流畅性。

因为DVSync需要占用空闲的自绘制帧缓冲用于缓存提前绘制的动画帧，用户需要确保至少有一个空闲的帧缓冲区，否则不建议启用此功能。

启用DVSync后，用户需要正确响应提前发送的VSync信号，并在前一个VSync对应的动画帧完成后再请求下一个VSync，且自绘制帧需要携带与VSync一致的时间戳。

在动画结束之后，用户需要关闭DVSync。

在不支持DVSync的平台或者如果有另一个应用程序已经启用了DVSync，则当前的启用操作将不会生效，应用程序仍将收到正常的VSync信号。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeVsync

**起始版本：** 14

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_NativeVSync](capi-nativevsync-oh-nativevsync.md)\* nativeVsync | 一个指向OH\_NativeVSync实例的指针。 |
| bool enable | 表示打开或者关闭DVSync，true表示打开，false表示关闭。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回值为0表示执行成功，其他返回值可参考[OHNativeErrorCode](capi-graphic-error-code-h.md#ohnativeerrorcode)。 |

### OH\_NativeVSync\_SetExpectedFrameRateRange()

PhonePC/2in1TabletTVWearable

```
1. int OH_NativeVSync_SetExpectedFrameRateRange(OH_NativeVSync* nativeVsync, OH_NativeVSync_ExpectedRateRange* range)
```

**描述**

设置VSync期望帧率及其范围。实际帧率可能因系统功耗、性能和硬件规格等限制而与设置的期望值不一致。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeVsync

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_NativeVSync](capi-nativevsync-oh-nativevsync.md)\* nativeVsync | 指向[OH\_NativeVSync](capi-nativevsync-oh-nativevsync.md)实例的指针。 |
| [OH\_NativeVSync\_ExpectedRateRange](capi-nativevsync-oh-nativevsync-expectedraterange.md)\* range | 指向[OH\_NativeVSync\_ExpectedRateRange](capi-nativevsync-oh-nativevsync-expectedraterange.md)实例的指针。  有效的期望帧率范围为：0 <= 最小值 <= 期望帧率 <= 最大值 <= 144。  期望帧率为0时，表示取消设置期望帧率。  此指针需开发者自行管理生命周期。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回值为0表示成功，其他返回值可参考[OHNativeErrorCode](capi-graphic-error-code-h.md#ohnativeerrorcode)。 |
