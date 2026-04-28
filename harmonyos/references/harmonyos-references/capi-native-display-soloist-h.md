---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-display-soloist-h
title: native_display_soloist.h
breadcrumb: API参考 > 图形 > ArkGraphics 2D（方舟2D图形服务） > C API > 头文件 > native_display_soloist.h
category: harmonyos-references
scraped_at: 2026-04-28T08:14:51+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:cc70e0a17184049679572a9ce6ab6de607e9958ac4004d3f7aee206b3080f200
---

## 概述

PhonePC/2in1TabletTVWearable

定义获取和使用NativeDisplaySoloist的相关函数。

**引用文件：** <native\_display\_soloist/native\_display\_soloist.h>

**库：** libnative\_display\_soloist.so

**系统能力：** SystemCapability.Graphic.Graphic2D.HyperGraphicManager

**起始版本：** 12

**相关模块：** [NativeDisplaySoloist](capi-nativedisplaysoloist.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 结构体

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [DisplaySoloist\_ExpectedRateRange](ivedisplaysoloist-displaysoloist-expectedraterange.md) | DisplaySoloist\_ExpectedRateRange | 提供期望帧率范围结构体。 |
| [OH\_DisplaySoloist](capi-nativedisplaysoloist-oh-displaysoloist.md) | OH\_DisplaySoloist | 提供OH\_DisplaySoloist结构体声明。 |

### 函数

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [typedef void (\*OH\_DisplaySoloist\_FrameCallback)(long long timestamp, long long targetTimestamp, void\* data)](capi-native-display-soloist-h.md#oh_displaysoloist_framecallback) | OH\_DisplaySoloist\_FrameCallback | OH\_DisplaySoloist回调函数类型。 |
| [OH\_DisplaySoloist\* OH\_DisplaySoloist\_Create(bool useExclusiveThread)](capi-native-display-soloist-h.md#oh_displaysoloist_create) | - | 创建一个OH\_DisplaySoloist实例，每次调用都会产生一个新的实例。 |
| [int32\_t OH\_DisplaySoloist\_Destroy(OH\_DisplaySoloist\* displaySoloist)](capi-native-display-soloist-h.md#oh_displaysoloist_destroy) | - | 销毁OH\_DisplaySoloist实例并回收对象占用的内存。 |
| [int32\_t OH\_DisplaySoloist\_Start(OH\_DisplaySoloist\* displaySoloist, OH\_DisplaySoloist\_FrameCallback callback, void\* data)](capi-native-display-soloist-h.md#oh_displaysoloist_start) | - | 设置每帧回调函数，每次VSync信号到来时启动每帧回调。 |
| [int32\_t OH\_DisplaySoloist\_Stop(OH\_DisplaySoloist\* displaySoloist)](capi-native-display-soloist-h.md#oh_displaysoloist_stop) | - | 停止请求下一次VSync信号，并停止调用回调函数callback。 |
| [int32\_t OH\_DisplaySoloist\_SetExpectedFrameRateRange(OH\_DisplaySoloist\* displaySoloist, DisplaySoloist\_ExpectedRateRange\* range)](capi-native-display-soloist-h.md#oh_displaysoloist_setexpectedframeraterange) | - | 设置VSync期望帧率范围。 |

## 函数说明

PhonePC/2in1TabletTVWearable

### OH\_DisplaySoloist\_FrameCallback()

PhonePC/2in1TabletTVWearable

```
1. typedef void (*OH_DisplaySoloist_FrameCallback)(long long timestamp, long long targetTimestamp, void* data)
```

**描述**

OH\_DisplaySoloist回调函数类型。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| long long timestamp | 当前帧VSync时间戳。 |
| long long targetTimestamp | 预期的下一帧VSync时间戳。 |
| void\* data | 用户自定义数据。 |

### OH\_DisplaySoloist\_Create()

PhonePC/2in1TabletTVWearable

```
1. OH_DisplaySoloist* OH_DisplaySoloist_Create(bool useExclusiveThread)
```

**描述**

创建一个OH\_DisplaySoloist实例，每次调用都会产生一个新的实例。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| bool useExclusiveThread | 表示此OH\_DisplaySoloist实例是否是独占线程。true表示独占一个线程，false表示共享线程。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| OH\_DisplaySoloist\* | 返回一个指向[OH\_DisplaySoloist](capi-nativedisplaysoloist-oh-displaysoloist.md)实例的指针，如果返回空表示执行失败，可能的原因是内存不足。 |

### OH\_DisplaySoloist\_Destroy()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_DisplaySoloist_Destroy(OH_DisplaySoloist* displaySoloist)
```

**描述**

销毁OH\_DisplaySoloist实例并回收对象占用的内存。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_DisplaySoloist](capi-nativedisplaysoloist-oh-displaysoloist.md)\* displaySoloist | 一个指向[OH\_DisplaySoloist](capi-nativedisplaysoloist-oh-displaysoloist.md)实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回值为0表示执行成功，-1表示执行失败。 |

### OH\_DisplaySoloist\_Start()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_DisplaySoloist_Start(OH_DisplaySoloist* displaySoloist, OH_DisplaySoloist_FrameCallback callback, void* data)
```

**描述**

设置每帧回调函数，每次VSync信号到来时启动每帧回调。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_DisplaySoloist](capi-nativedisplaysoloist-oh-displaysoloist.md)\* displaySoloist | 一个指向[OH\_DisplaySoloist](capi-nativedisplaysoloist-oh-displaysoloist.md)实例的指针。 |
| [OH\_DisplaySoloist\_FrameCallback](capi-native-display-soloist-h.md#oh_displaysoloist_framecallback) callback | 表示下一次VSync信号到来时执行的回调函数类型。 |
| void\* data | 一个指向用户自定义数据结构的指针，类型是void。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回值为0表示执行成功，-1表示执行失败。 |

### OH\_DisplaySoloist\_Stop()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_DisplaySoloist_Stop(OH_DisplaySoloist* displaySoloist)
```

**描述**

停止请求下一次VSync信号，并停止调用回调函数callback。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_DisplaySoloist](capi-nativedisplaysoloist-oh-displaysoloist.md)\* displaySoloist | 一个指向[OH\_DisplaySoloist](capi-nativedisplaysoloist-oh-displaysoloist.md)实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回值为0表示执行成功，-1表示执行失败。 |

### OH\_DisplaySoloist\_SetExpectedFrameRateRange()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_DisplaySoloist_SetExpectedFrameRateRange(OH_DisplaySoloist* displaySoloist, DisplaySoloist_ExpectedRateRange* range)
```

**描述**

设置VSync期望帧率范围。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_DisplaySoloist](capi-nativedisplaysoloist-oh-displaysoloist.md)\* displaySoloist | 一个指向[OH\_DisplaySoloist](capi-nativedisplaysoloist-oh-displaysoloist.md)实例的指针。 |
| [DisplaySoloist\_ExpectedRateRange](ivedisplaysoloist-displaysoloist-expectedraterange.md)\* range | 一个指向期望帧率范围[DisplaySoloist\_ExpectedRateRange](ivedisplaysoloist-displaysoloist-expectedraterange.md)实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回值为0表示执行成功，-1表示执行失败。 |
