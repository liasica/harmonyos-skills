---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-buffer-h
title: native_buffer.h
breadcrumb: API参考 > 图形 > ArkGraphics 2D（方舟2D图形服务） > C API > 头文件 > native_buffer.h
category: harmonyos-references
scraped_at: 2026-04-28T08:14:51+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:b5f4069fa0cd274d8f16de05638bbb2baf1409485a6a427a7a1ea1e58ea4e605
---

## 概述

PhonePC/2in1TabletTVWearable

定义获取和使用NativeBuffer的相关函数。

**引用文件：** <native\_buffer/native\_buffer.h>

**库：** libnative\_buffer.so

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeBuffer

**起始版本：** 9

**相关模块：** [OH\_NativeBuffer](capi-oh-nativebuffer.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 结构体

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [OH\_NativeBuffer\_Config](capi-oh-nativebuffer-oh-nativebuffer-config.md) | OH\_NativeBuffer\_Config | OH\_NativeBuffer的属性配置，用于申请新的OH\_NativeBuffer实例或查询现有实例的相关属性。 |
| [OH\_NativeBuffer\_Plane](capi-oh-nativebuffer-oh-nativebuffer-plane.md) | OH\_NativeBuffer\_Plane | 单个图像平面格式信息。 |
| [OH\_NativeBuffer\_Planes](capi-oh-nativebuffer-oh-nativebuffer-planes.md) | OH\_NativeBuffer\_Planes | OH\_NativeBuffer的图像平面格式信息。 |
| [OH\_NativeBuffer](capi-oh-nativebuffer-oh-nativebuffer.md) | OH\_NativeBuffer | 提供OH\_NativeBuffer结构体声明。 |
| [OHIPCParcel](capi-ohipcparcel-ohipcparcel.md) | OHIPCParcel | 提供OHIPCParcel结构体声明，用于进程间通信。 |

### 枚举

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [OH\_NativeBuffer\_Usage](capi-native-buffer-h.md#oh_nativebuffer_usage) | OH\_NativeBuffer\_Usage | OH\_NativeBuffer的用途。 |
| [OH\_NativeBuffer\_ColorGamut](capi-native-buffer-h.md#oh_nativebuffer_colorgamut) | OH\_NativeBuffer\_ColorGamut | OH\_NativeBuffer的色域。 |

### 函数

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [OH\_NativeBuffer\* OH\_NativeBuffer\_Alloc(const OH\_NativeBuffer\_Config\* config)](capi-native-buffer-h.md#oh_nativebuffer_alloc) | 通过OH\_NativeBuffer\_Config创建OH\_NativeBuffer实例，每次调用都会产生一个新的OH\_NativeBuffer实例。  本接口需要与[OH\_NativeBuffer\_Unreference](capi-native-buffer-h.md#oh_nativebuffer_unreference)接口配合使用，否则会存在内存泄露。  本接口为非线程安全类型接口。 |
| [int32\_t OH\_NativeBuffer\_Reference(OH\_NativeBuffer \*buffer)](capi-native-buffer-h.md#oh_nativebuffer_reference) | 将OH\_NativeBuffer对象的引用计数加1。  本接口需要与[OH\_NativeBuffer\_Unreference](capi-native-buffer-h.md#oh_nativebuffer_unreference)接口配合使用，否则会存在内存泄露。  本接口为非线程安全类型接口。 |
| [int32\_t OH\_NativeBuffer\_Unreference(OH\_NativeBuffer \*buffer)](capi-native-buffer-h.md#oh_nativebuffer_unreference) | 将OH\_NativeBuffer对象的引用计数减1，当引用计数为0的时候，该NativeBuffer对象会被析构掉。  本接口为非线程安全类型接口。 |
| [void OH\_NativeBuffer\_GetConfig(OH\_NativeBuffer buffer, OH\_NativeBuffer\_Config config)](capi-native-buffer-h.md#oh_nativebuffer_getconfig) | 用于获取OH\_NativeBuffer的属性。  本接口为非线程安全类型接口。 |
| [int32\_t OH\_NativeBuffer\_Map(OH\_NativeBuffer \*buffer, void \*\*virAddr)](capi-native-buffer-h.md#oh_nativebuffer_map) | 将OH\_NativeBuffer对应的ION内存映射到进程空间。  需注意调用该接口的OH\_NativeBuffer的usage必须带有CPU\_READ属性，否则可能导致稳定性问题。  通过[OH\_NativeBuffer\_Alloc](capi-native-buffer-h.md#oh_nativebuffer_alloc)申请的OH\_NativeBuffer，需保证参数config.usage带有NATIVEBUFFER\_USAGE\_CPU\_READ。  通过[OH\_NativeBuffer\_FromNativeWindowBuffer](capi-native-buffer-h.md#oh_nativebuffer_fromnativewindowbuffer)转换来的OH\_NativeBuffer，需保证原OH\_NativeWindowBuffer申请前，通过[OH\_NativeWindow\_NativeWindowHandleOpt](capi-external-window-h.md#oh_nativewindow_nativewindowhandleopt)接口设置的USAGE带有NATIVEBUFFER\_USAGE\_CPU\_READ。  本接口需要与[OH\_NativeBuffer\_Unmap](capi-native-buffer-h.md#oh_nativebuffer_unmap)接口配合使用。  本接口为非线程安全类型接口。 |
| [int32\_t OH\_NativeBuffer\_Unmap(OH\_NativeBuffer \*buffer)](capi-native-buffer-h.md#oh_nativebuffer_unmap) | 将OH\_NativeBuffer对应的ION内存从进程空间移除。  本接口为非线程安全类型接口。 |
| [uint32\_t OH\_NativeBuffer\_GetSeqNum(OH\_NativeBuffer \*buffer)](capi-native-buffer-h.md#oh_nativebuffer_getseqnum) | 获取OH\_NativeBuffer的序列号。  本接口为非线程安全类型接口。 |
| [int32\_t OH\_NativeBuffer\_SetColorSpace(OH\_NativeBuffer \*buffer, OH\_NativeBuffer\_ColorSpace colorSpace)](capi-native-buffer-h.md#oh_nativebuffer_setcolorspace) | 为OH\_NativeBuffer设置颜色空间属性。  本接口为非线程安全类型接口。 |
| [int32\_t OH\_NativeBuffer\_MapPlanes(OH\_NativeBuffer \*buffer, void \*\*virAddr, OH\_NativeBuffer\_Planes \*outPlanes)](capi-native-buffer-h.md#oh_nativebuffer_mapplanes) | 将OH\_NativeBuffer对应的多通道ION内存映射到进程空间。  本接口为非线程安全类型接口。 |
| [int32\_t OH\_NativeBuffer\_FromNativeWindowBuffer(OHNativeWindowBuffer \*nativeWindowBuffer, OH\_NativeBuffer \*\*buffer)](capi-native-buffer-h.md#oh_nativebuffer_fromnativewindowbuffer) | 将OHNativeWindowBuffer实例转换为OH\_NativeBuffer实例。  本接口为非线程安全类型接口。 |
| [int32\_t OH\_NativeBuffer\_GetColorSpace(OH\_NativeBuffer \*buffer, OH\_NativeBuffer\_ColorSpace \*colorSpace)](capi-native-buffer-h.md#oh_nativebuffer_getcolorspace) | 获取OH\_NativeBuffer颜色空间属性。  本接口为非线程安全类型接口。 |
| [int32\_t OH\_NativeBuffer\_SetMetadataValue(OH\_NativeBuffer \*buffer, OH\_NativeBuffer\_MetadataKey metadataKey,int32\_t size, uint8\_t \*metadata)](capi-native-buffer-h.md#oh_nativebuffer_setmetadatavalue) | 为OH\_NativeBuffer设置元数据属性值。  本接口为非线程安全类型接口。 |
| [int32\_t OH\_NativeBuffer\_GetMetadataValue(OH\_NativeBuffer \*buffer, OH\_NativeBuffer\_MetadataKey metadataKey,int32\_t \*size, uint8\_t \*\*metadata)](capi-native-buffer-h.md#oh_nativebuffer_getmetadatavalue) | 获取OH\_NativeBuffer元数据属性值。  本接口为非线程安全类型接口。 |
| [int32\_t OH\_NativeBuffer\_MapWaitFence(OH\_NativeBuffer \*buffer, int32\_t fenceFd, void \*\*virAddr)](capi-native-buffer-h.md#oh_nativebuffer_mapwaitfence) | 将[OH\_NativeBuffer](capi-oh-nativebuffer-oh-nativebuffer.md)对应的ION内存映射到进程空间，永久阻塞传入的fenceFd。  如果接口返回OK，系统会将fenceFd关闭，无需用户close，否则，用户需要自行关闭fenceFd。  本接口需要与[OH\_NativeBuffer\_Unmap](capi-native-buffer-h.md#oh_nativebuffer_unmap)接口配合使用。  本接口为非线程安全类型接口。 |
| [int32\_t OH\_NativeBuffer\_WriteToParcel(OH\_NativeBuffer\* buffer, OHIPCParcel\* parcel)](capi-native-buffer-h.md#oh_nativebuffer_writetoparcel) | 将[OH\_NativeBuffer](capi-oh-nativebuffer-oh-nativebuffer.md)对象写入IPC序列化对象中。  本接口为非线程安全类型接口。 |
| [int32\_t OH\_NativeBuffer\_ReadFromParcel(OHIPCParcel\* parcel, OH\_NativeBuffer\*\* buffer)](capi-native-buffer-h.md#oh_nativebuffer_readfromparcel) | 从IPC序列化对象中读取[OH\_NativeBuffer](capi-oh-nativebuffer-oh-nativebuffer.md)对象。  本接口将会创建一个[OH\_NativeBuffer](capi-oh-nativebuffer-oh-nativebuffer.md)，当OH\_NativeBuffer对象使用完，开发者需要与[OH\_NativeBuffer\_Unreference](capi-native-buffer-h.md#oh_nativebuffer_unreference)接口配合使用，否则会存在内存泄漏。  本接口为非线程安全类型接口。 |
| [int32\_t OH\_NativeBuffer\_IsSupported(OH\_NativeBuffer\_Config config, bool\* isSupported)](capi-native-buffer-h.md#oh_nativebuffer_issupported) | 检查系统是否支持传入的[OH\_NativeBuffer\_Config](capi-oh-nativebuffer-oh-nativebuffer-config.md)配置信息。  本接口为非线程安全类型接口。 |
| [int32\_t OH\_NativeBuffer\_MapAndGetConfig(OH\_NativeBuffer\* buffer, void\*\* virAddr, OH\_NativeBuffer\_Config\* config)](capi-native-buffer-h.md#oh_nativebuffer_mapandgetconfig) | 将[OH\_NativeBuffer](capi-oh-nativebuffer-oh-nativebuffer.md)对应的多通道ION内存映射到进程空间，并获取[OH\_NativeBuffer](capi-oh-nativebuffer-oh-nativebuffer.md)对应的[OH\_NativeBuffer\_Config](capi-oh-nativebuffer-oh-nativebuffer-config.md)。  本接口为非线程安全类型接口。 |

## 枚举类型说明

PhonePC/2in1TabletTVWearable

### OH\_NativeBuffer\_Usage

PhonePC/2in1TabletTVWearable

```
1. enum OH_NativeBuffer_Usage
```

**描述**

OH\_NativeBuffer的用途。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeBuffer

**起始版本：** 10

| 枚举项 | 描述 |
| --- | --- |
| NATIVEBUFFER\_USAGE\_CPU\_READ = (1ULL << 0) | CPU可读。 |
| NATIVEBUFFER\_USAGE\_CPU\_WRITE = (1ULL << 1) | CPU可写。 |
| NATIVEBUFFER\_USAGE\_MEM\_DMA = (1ULL << 3) | 直接内存访问缓冲区。 |
| NATIVEBUFFER\_USAGE\_MEM\_MMZ\_CACHE = (1ULL << 5) | 媒体内存区域缓存。  **起始版本：** 20 |
| NATIVEBUFFER\_USAGE\_HW\_RENDER = (1ULL << 8) | GPU可写。  **起始版本：** 12 |
| NATIVEBUFFER\_USAGE\_HW\_TEXTURE = (1ULL << 9) | GPU可读。  **起始版本：** 12 |
| NATIVEBUFFER\_USAGE\_CPU\_READ\_OFTEN = (1ULL << 16) | CPU可直接映射。  **起始版本：** 12 |
| NATIVEBUFFER\_USAGE\_ALIGNMENT\_512 = (1ULL << 18) | 512字节对齐。  **起始版本：** 12 |

### OH\_NativeBuffer\_ColorGamut

PhonePC/2in1TabletTVWearable

```
1. enum OH_NativeBuffer_ColorGamut
```

**描述**

OH\_NativeBuffer的色域。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeBuffer

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| NATIVEBUFFER\_COLOR\_GAMUT\_NATIVE = 0 | 默认色域格式。 |
| NATIVEBUFFER\_COLOR\_GAMUT\_STANDARD\_BT601 = 1 | Standard BT601色域格式。 |
| NATIVEBUFFER\_COLOR\_GAMUT\_STANDARD\_BT709 = 2 | Standard BT709色域格式。 |
| NATIVEBUFFER\_COLOR\_GAMUT\_DCI\_P3 = 3 | DCI P3色域格式。 |
| NATIVEBUFFER\_COLOR\_GAMUT\_SRGB = 4 | SRGB色域格式。 |
| NATIVEBUFFER\_COLOR\_GAMUT\_ADOBE\_RGB = 5 | Adobe RGB色域格式。 |
| NATIVEBUFFER\_COLOR\_GAMUT\_DISPLAY\_P3 = 6 | Display P3色域格式。 |
| NATIVEBUFFER\_COLOR\_GAMUT\_BT2020 = 7 | BT2020色域格式。 |
| NATIVEBUFFER\_COLOR\_GAMUT\_BT2100\_PQ = 8 | BT2100 PQ色域格式。 |
| NATIVEBUFFER\_COLOR\_GAMUT\_BT2100\_HLG = 9 | BT2100 HLG色域格式。 |
| NATIVEBUFFER\_COLOR\_GAMUT\_DISPLAY\_BT2020 = 10 | Display BT2020色域格式。 |

## 函数说明

PhonePC/2in1TabletTVWearable

### OH\_NativeBuffer\_Alloc()

PhonePC/2in1TabletTVWearable

```
1. OH_NativeBuffer* OH_NativeBuffer_Alloc(const OH_NativeBuffer_Config* config)
```

**描述**

通过OH\_NativeBuffer\_Config创建OH\_NativeBuffer实例，每次调用都会产生一个新的OH\_NativeBuffer实例。

本接口需要与[OH\_NativeBuffer\_Unreference](capi-native-buffer-h.md#oh_nativebuffer_unreference)接口配合使用，否则会存在内存泄露。

本接口为非线程安全类型接口。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeBuffer

**起始版本：** 9

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_NativeBuffer\_Config](capi-oh-nativebuffer-oh-nativebuffer-config.md)\* config | 一个指向OH\_NativeBuffer\_Config类型的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| OH\_NativeBuffer\* | 创建成功则返回一个指向OH\_NativeBuffer结构体实例的指针，否则返回NULL。 |

### OH\_NativeBuffer\_Reference()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_NativeBuffer_Reference(OH_NativeBuffer *buffer)
```

**描述**

将OH\_NativeBuffer对象的引用计数加1。

本接口需要与[OH\_NativeBuffer\_Unreference](capi-native-buffer-h.md#oh_nativebuffer_unreference)接口配合使用，否则会存在内存泄露。

本接口为非线程安全类型接口。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeBuffer

**起始版本：** 9

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_NativeBuffer](capi-oh-nativebuffer-oh-nativebuffer.md) \*buffer | 一个指向OH\_NativeBuffer实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回值为0表示执行成功，其他返回值可参考[OHNativeErrorCode](capi-graphic-error-code-h.md#ohnativeerrorcode)。 |

### OH\_NativeBuffer\_Unreference()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_NativeBuffer_Unreference(OH_NativeBuffer *buffer)
```

**描述**

将OH\_NativeBuffer对象的引用计数减1，当引用计数为0的时候，该NativeBuffer对象会被析构掉。

本接口为非线程安全类型接口。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeBuffer

**起始版本：** 9

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_NativeBuffer](capi-oh-nativebuffer-oh-nativebuffer.md) \*buffer | 一个指向OH\_NativeBuffer实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回值为0表示执行成功，其他返回值可参考[OHNativeErrorCode](capi-graphic-error-code-h.md#ohnativeerrorcode)。 |

### OH\_NativeBuffer\_GetConfig()

PhonePC/2in1TabletTVWearable

```
1. void OH_NativeBuffer_GetConfig(OH_NativeBuffer *buffer, OH_NativeBuffer_Config* config)
```

**描述**

用于获取OH\_NativeBuffer的属性。

本接口为非线程安全类型接口。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeBuffer

**起始版本：** 9

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_NativeBuffer](capi-oh-nativebuffer-oh-nativebuffer.md) \*buffer | 一个指向OH\_NativeBuffer实例的指针。 |
| [OH\_NativeBuffer\_Config](capi-oh-nativebuffer-oh-nativebuffer-config.md)\* config | 一个指向OH\_NativeBuffer\_Config的指针，用于接收OH\_NativeBuffer的属性。 |

### OH\_NativeBuffer\_Map()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_NativeBuffer_Map(OH_NativeBuffer *buffer, void **virAddr)
```

**描述**

将OH\_NativeBuffer对应的ION内存映射到进程空间。

需注意调用该接口的OH\_NativeBuffer的usage必须带有CPU\_READ属性，否则可能导致稳定性问题。

通过[OH\_NativeBuffer\_Alloc](capi-native-buffer-h.md#oh_nativebuffer_alloc)申请的OH\_NativeBuffer，需保证参数config.usage带有NATIVEBUFFER\_USAGE\_CPU\_READ。

通过[OH\_NativeBuffer\_FromNativeWindowBuffer](capi-native-buffer-h.md#oh_nativebuffer_fromnativewindowbuffer)转换来的OH\_NativeBuffer，需保证原OH\_NativeWindowBuffer申请前，通过[OH\_NativeWindow\_NativeWindowHandleOpt](capi-external-window-h.md#oh_nativewindow_nativewindowhandleopt)接口设置的USAGE带有NATIVEBUFFER\_USAGE\_CPU\_READ。

本接口需要与[OH\_NativeBuffer\_Unmap](capi-native-buffer-h.md#oh_nativebuffer_unmap)接口配合使用。

本接口为非线程安全类型接口。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeBuffer

**起始版本：** 9

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_NativeBuffer](capi-oh-nativebuffer-oh-nativebuffer.md) \*buffer | 一个指向OH\_NativeBuffer实例的指针。 |
| void \*\*virAddr | 一个二级指针，二级指针指向映射到当前进程的虚拟内存的地址。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回值为0表示执行成功，其他返回值可参考[OHNativeErrorCode](capi-graphic-error-code-h.md#ohnativeerrorcode)。 |

### OH\_NativeBuffer\_Unmap()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_NativeBuffer_Unmap(OH_NativeBuffer *buffer)
```

**描述**

将OH\_NativeBuffer对应的ION内存从进程空间移除。

本接口为非线程安全类型接口。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeBuffer

**起始版本：** 9

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_NativeBuffer](capi-oh-nativebuffer-oh-nativebuffer.md) \*buffer | 一个指向OH\_NativeBuffer实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回值为0表示执行成功，其他返回值可参考[OHNativeErrorCode](capi-graphic-error-code-h.md#ohnativeerrorcode)。 |

### OH\_NativeBuffer\_GetSeqNum()

PhonePC/2in1TabletTVWearable

```
1. uint32_t OH_NativeBuffer_GetSeqNum(OH_NativeBuffer *buffer)
```

**描述**

获取OH\_NativeBuffer的序列号。

本接口为非线程安全类型接口。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeBuffer

**起始版本：** 9

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_NativeBuffer](capi-oh-nativebuffer-oh-nativebuffer.md) \*buffer | 一个指向OH\_NativeBuffer实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| uint32\_t | 返回对应OH\_NativeBuffer的唯一序列号。 |

### OH\_NativeBuffer\_SetColorSpace()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_NativeBuffer_SetColorSpace(OH_NativeBuffer *buffer, OH_NativeBuffer_ColorSpace colorSpace)
```

**描述**

为OH\_NativeBuffer设置颜色空间属性。

本接口为非线程安全类型接口。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeBuffer

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_NativeBuffer](capi-oh-nativebuffer-oh-nativebuffer.md) \*buffer | 一个指向OH\_NativeBuffer实例的指针。 |
| [OH\_NativeBuffer\_ColorSpace](capi-buffer-common-h.md#oh_nativebuffer_colorspace) colorSpace | 为OH\_NativeBuffer设置的颜色空间，其值从[OH\_NativeBuffer\_ColorSpace](capi-buffer-common-h.md#oh_nativebuffer_colorspace)获取。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回值为0表示执行成功，其他返回值可参考[OHNativeErrorCode](capi-graphic-error-code-h.md#ohnativeerrorcode)。 |

### OH\_NativeBuffer\_MapPlanes()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_NativeBuffer_MapPlanes(OH_NativeBuffer *buffer, void **virAddr, OH_NativeBuffer_Planes *outPlanes)
```

**描述**

将OH\_NativeBuffer对应的多通道ION内存映射到进程空间。

本接口为非线程安全类型接口。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeBuffer

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_NativeBuffer](capi-oh-nativebuffer-oh-nativebuffer.md) \*buffer | 一个指向OH\_NativeBuffer实例的指针。 |
| void \*\*virAddr | 一个二级指针，二级指针指向映射到当前进程的虚拟内存的地址。 |
| [OH\_NativeBuffer\_Planes](capi-oh-nativebuffer-oh-nativebuffer-planes.md) \*outPlanes | 一个指向所有图像平面格式信息的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回值为0表示执行成功，其他返回值可参考[OHNativeErrorCode](capi-graphic-error-code-h.md#ohnativeerrorcode)。 |

### OH\_NativeBuffer\_FromNativeWindowBuffer()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_NativeBuffer_FromNativeWindowBuffer(OHNativeWindowBuffer *nativeWindowBuffer, OH_NativeBuffer **buffer)
```

**描述**

将OHNativeWindowBuffer实例转换为OH\_NativeBuffer实例。

本接口为非线程安全类型接口。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeBuffer

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OHNativeWindowBuffer](capi-nativewindow-nativewindowbuffer.md) \*nativeWindowBuffer | 一个指向[OHNativeWindowBuffer](capi-nativewindow-nativewindowbuffer.md)实例的指针。 |
| [OH\_NativeBuffer](capi-oh-nativebuffer-oh-nativebuffer.md) \*\*buffer | 一个指向OH\_NativeBuffer实例的二级指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回值为0表示执行成功，其他返回值可参考[OHNativeErrorCode](capi-graphic-error-code-h.md#ohnativeerrorcode)。 |

### OH\_NativeBuffer\_GetColorSpace()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_NativeBuffer_GetColorSpace(OH_NativeBuffer *buffer, OH_NativeBuffer_ColorSpace *colorSpace)
```

**描述**

获取OH\_NativeBuffer颜色空间属性。

本接口为非线程安全类型接口。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeBuffer

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_NativeBuffer](capi-oh-nativebuffer-oh-nativebuffer.md) \*buffer | 一个指向OH\_NativeBuffer实例的指针。 |
| [OH\_NativeBuffer\_ColorSpace](capi-buffer-common-h.md#oh_nativebuffer_colorspace) \*colorSpace | 为[OH\_NativeBuffer](capi-oh-nativebuffer-oh-nativebuffer.md)设置的颜色空间，其值从[OH\_NativeBuffer\_ColorSpace](capi-buffer-common-h.md#oh_nativebuffer_colorspace)获取。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回值为0表示执行成功，其他返回值可参考[OHNativeErrorCode](capi-graphic-error-code-h.md#ohnativeerrorcode)。 |

### OH\_NativeBuffer\_SetMetadataValue()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_NativeBuffer_SetMetadataValue(OH_NativeBuffer *buffer, OH_NativeBuffer_MetadataKey metadataKey,int32_t size, uint8_t *metadata)
```

**描述**

为OH\_NativeBuffer设置元数据属性值。

本接口为非线程安全类型接口。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeBuffer

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_NativeBuffer](capi-oh-nativebuffer-oh-nativebuffer.md) \*buffer | 一个指向OH\_NativeBuffer实例的指针。 |
| [OH\_NativeBuffer\_MetadataKey](capi-buffer-common-h.md#oh_nativebuffer_metadatakey) metadataKey | [OH\_NativeBuffer](capi-oh-nativebuffer-oh-nativebuffer.md)的元数据类型，其值从[OH\_NativeBuffer\_MetadataKey](capi-buffer-common-h.md#oh_nativebuffer_metadatakey)获取。 |
| int32\_t size | uint8\_t向量的大小，其取值范围参考[OH\_NativeBuffer\_MetadataKey](capi-buffer-common-h.md#oh_nativebuffer_metadatakey)。 |
| uint8\_t \*metadata | 指向uint8\_t向量的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回值为0表示执行成功，其他返回值可参考[OHNativeErrorCode](capi-graphic-error-code-h.md#ohnativeerrorcode)。 |

### OH\_NativeBuffer\_GetMetadataValue()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_NativeBuffer_GetMetadataValue(OH_NativeBuffer *buffer, OH_NativeBuffer_MetadataKey metadataKey,int32_t *size, uint8_t **metadata)
```

**描述**

获取OH\_NativeBuffer元数据属性值。

本接口为非线程安全类型接口。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeBuffer

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_NativeBuffer](capi-oh-nativebuffer-oh-nativebuffer.md) \*buffer | 一个指向OH\_NativeBuffer实例的指针。 |
| [OH\_NativeBuffer\_MetadataKey](capi-buffer-common-h.md#oh_nativebuffer_metadatakey) metadataKey | [OH\_NativeBuffer](capi-oh-nativebuffer-oh-nativebuffer.md)的元数据类型，其值从[OH\_NativeBuffer\_MetadataKey](capi-buffer-common-h.md#oh_nativebuffer_metadatakey)获取。 |
| int32\_t \*size | uint8\_t向量的大小，其取值范围参考[OH\_NativeBuffer\_MetadataKey](capi-buffer-common-h.md#oh_nativebuffer_metadatakey)。 |
| uint8\_t \*\*metadata | 指向uint8\_t向量的二级指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回值为0表示执行成功，其他返回值可参考[OHNativeErrorCode](capi-graphic-error-code-h.md#ohnativeerrorcode)。 |

### OH\_NativeBuffer\_MapWaitFence()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_NativeBuffer_MapWaitFence(OH_NativeBuffer *buffer, int32_t fenceFd, void **virAddr)
```

**描述**

将[OH\_NativeBuffer](capi-oh-nativebuffer-oh-nativebuffer.md)对应的ION内存映射到进程空间，永久阻塞传入的fenceFd。

如果接口返回OK，系统会将fenceFd关闭，无需用户close，否则，用户需要自行关闭fenceFd。

本接口需要与[OH\_NativeBuffer\_Unmap](capi-native-buffer-h.md#oh_nativebuffer_unmap)接口配合使用。

本接口为非线程安全类型接口。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeBuffer

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_NativeBuffer](capi-oh-nativebuffer-oh-nativebuffer.md) \*buffer | 一个指向[OH\_NativeBuffer](capi-oh-nativebuffer-oh-nativebuffer.md)实例的指针。 |
| int32\_t fenceFd | 指向文件描述符句柄，用于并发同步控制。 |
| void \*\*virAddr | 一个二级指针，二级指针指向映射到当前进程的虚拟内存的地址。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 执行成功时返回NATIVE\_ERROR\_OK。  buffer、virAddr是空指针或fenceFd小于0时返回NATIVE\_ERROR\_INVALID\_ARGUMENTS。  映射失败时返回NATIVE\_ERROR\_UNKNOWN。  其他返回值可参考[OHNativeErrorCode](capi-graphic-error-code-h.md#ohnativeerrorcode)。 |

### OH\_NativeBuffer\_WriteToParcel()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_NativeBuffer_WriteToParcel(OH_NativeBuffer* buffer, OHIPCParcel* parcel)
```

**描述**

将[OH\_NativeBuffer](capi-oh-nativebuffer-oh-nativebuffer.md)对象写入IPC序列化对象中。

本接口为非线程安全类型接口。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeBuffer

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_NativeBuffer](capi-oh-nativebuffer-oh-nativebuffer.md)\* buffer | 一个指向[OH\_NativeBuffer](capi-oh-nativebuffer-oh-nativebuffer.md)实例的指针。 |
| [OHIPCParcel](capi-ohipcparcel-ohipcparcel.md)\* parcel | 一个指向[OHIPCParcel](capi-ohipcparcel-ohipcparcel.md)结构体实例的指针，作为出参使用。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 执行成功时返回NATIVE\_ERROR\_OK。  buffer或parcel为空指针时返回NATIVE\_ERROR\_INVALID\_ARGUMENTS。  IPC发送失败返回NATIVE\_ERROR\_BINDER\_ERROR。  其他返回值可参考[OHNativeErrorCode](capi-graphic-error-code-h.md#ohnativeerrorcode)。 |

### OH\_NativeBuffer\_ReadFromParcel()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_NativeBuffer_ReadFromParcel(OHIPCParcel* parcel, OH_NativeBuffer** buffer)
```

**描述**

从IPC序列化对象中读取[OH\_NativeBuffer](capi-oh-nativebuffer-oh-nativebuffer.md)对象。

本接口将会创建一个[OH\_NativeBuffer](capi-oh-nativebuffer-oh-nativebuffer.md)，当OH\_NativeBuffer对象使用完，开发者需要与[OH\_NativeBuffer\_Unreference](capi-native-buffer-h.md#oh_nativebuffer_unreference)接口配合使用，否则会存在内存泄漏。

本接口为非线程安全类型接口。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeBuffer

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OHIPCParcel](capi-ohipcparcel-ohipcparcel.md)\* parcel | 一个指向[OHIPCParcel](capi-ohipcparcel-ohipcparcel.md)的结构体实例的指针。 |
| [OH\_NativeBuffer](capi-oh-nativebuffer-oh-nativebuffer.md)\*\* buffer | 一个指向[OH\_NativeBuffer](capi-oh-nativebuffer-oh-nativebuffer.md)结构体实例的二级指针，作为出参使用。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 执行成功时返回NATIVE\_ERROR\_OK。  parcel或buffer为空指针时返回NATIVE\_ERROR\_INVALID\_ARGUMENTS。  parcel反序列化失败返回NATIVE\_ERROR\_UNKNOWN。  其他返回值可参考[OHNativeErrorCode](capi-graphic-error-code-h.md#ohnativeerrorcode)。 |

### OH\_NativeBuffer\_IsSupported()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_NativeBuffer_IsSupported(OH_NativeBuffer_Config config, bool* isSupported)
```

**描述**

检查系统是否支持传入的[OH\_NativeBuffer\_Config](capi-oh-nativebuffer-oh-nativebuffer-config.md)配置信息。

本接口为非线程安全类型接口。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeBuffer

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_NativeBuffer\_Config](capi-oh-nativebuffer-oh-nativebuffer-config.md) config | [OH\_NativeBuffer\_Config](capi-oh-nativebuffer-oh-nativebuffer-config.md)结构体实例。 |
| bool\* isSupported | 为true代表系统支持传入的[OH\_NativeBuffer\_Config](capi-oh-nativebuffer-oh-nativebuffer-config.md)配置信息，为false表示系统不支持传入的OH\_NativeBuffer\_Config配置信息，作为出参使用。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 执行成功时返回NATIVE\_ERROR\_OK。  isSupported为空指针时返回NATIVE\_ERROR\_INVALID\_ARGUMENTS。  其他返回值可参考[OHNativeErrorCode](capi-graphic-error-code-h.md#ohnativeerrorcode)。 |

### OH\_NativeBuffer\_MapAndGetConfig()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_NativeBuffer_MapAndGetConfig(OH_NativeBuffer* buffer, void** virAddr, OH_NativeBuffer_Config* config)
```

**描述**

将[OH\_NativeBuffer](capi-oh-nativebuffer-oh-nativebuffer.md)对应的多通道ION内存映射到进程空间，并获取[OH\_NativeBuffer](capi-oh-nativebuffer-oh-nativebuffer.md)对应的[OH\_NativeBuffer\_Config](capi-oh-nativebuffer-oh-nativebuffer-config.md)。

本接口为非线程安全类型接口。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeBuffer

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_NativeBuffer](capi-oh-nativebuffer-oh-nativebuffer.md)\* buffer | 一个指向[OH\_NativeBuffer](capi-oh-nativebuffer-oh-nativebuffer.md)的结构体实例的指针。 |
| void\*\* virAddr | 一个指向映射到当前进程的虚拟内存的地址的二级指针，作为出参使用。 |
| [OH\_NativeBuffer\_Config](capi-oh-nativebuffer-oh-nativebuffer-config.md)\* config | 一个指向[OH\_NativeBuffer\_Config](capi-oh-nativebuffer-oh-nativebuffer-config.md)的结构体实例的指针，作为出参使用。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 执行成功时返回NATIVE\_ERROR\_OK。  buffer、virAddr或config为空指针时返回NATIVE\_ERROR\_INVALID\_ARGUMENTS。  映射时返回NATIVE\_ERROR\_UNKNOWN。  其他返回值可参考[OHNativeErrorCode](capi-graphic-error-code-h.md#ohnativeerrorcode)。 |
