---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-external-window-h
title: external_window.h
breadcrumb: API参考 > 图形 > ArkGraphics 2D（方舟2D图形服务） > C API > 头文件 > external_window.h
category: harmonyos-references
scraped_at: 2026-04-28T08:15:06+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:301a08939859761c0b256a25327dec7df8f292357aecd52a83c8e778c893f2df
---

## 概述

PhonePC/2in1TabletTVWearable

定义获取和使用NativeWindow的相关函数。

**引用文件：** <native\_window/external\_window.h>

**库：** libnative\_window.so

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeWindow

**起始版本：** 8

**相关模块：** [NativeWindow](capi-nativewindow.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 结构体

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [Region](capi-nativewindow-region.md) | Region | 表示本地窗口OHNativeWindow需要更新内容的矩形区域（脏区）。 |
| [Rect](capi-nativewindow-rect.md) | - | 如果rects是空指针nullptr，默认Buffer大小为脏区。 |
| [OHHDRMetaData](capi-nativewindow-ohhdrmetadata.md) | OHHDRMetaData | HDR元数据结构体定义。 |
| [OHExtDataHandle](capi-nativewindow-ohextdatahandle.md) | OHExtDataHandle | 扩展数据句柄结构体定义。 |
| [OHIPCParcel](capi-nativewindow-ohipcparcel.md) | OHIPCParcel | 提供对IPC序列化对象的访问功能。 |
| [NativeWindow](capi-nativewindow-nativewindow.md) | OHNativeWindow | 提供对OHNativeWindow的访问功能。 |
| [NativeWindowBuffer](capi-nativewindow-nativewindowbuffer.md) | OHNativeWindowBuffer | 提供对OHNativeWindowBuffer的访问功能。 |
| [OH\_NativeBuffer](capi-oh-nativebuffer-oh-nativebuffer.md) | OH\_NativeBuffer | 提供对OH\_NativeBuffer的访问功能。 |

### 枚举

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [NativeWindowOperation](capi-external-window-h.md#nativewindowoperation) | NativeWindowOperation | OH\_NativeWindow\_NativeWindowHandleOpt函数中的操作码。 |
| [OHScalingMode](capi-external-window-h.md#ohscalingmode) | OHScalingMode | 缩放模式Scaling Mode。 |
| [OHScalingModeV2](capi-external-window-h.md#ohscalingmodev2) | OHScalingModeV2 | 渲染缩放模式枚举。 |
| [OHHDRMetadataKey](capi-external-window-h.md#ohhdrmetadatakey) | OHHDRMetadataKey | 枚举HDR元数据关键字。 |
| [OHSurfaceSource](capi-external-window-h.md#ohsurfacesource) | OHSurfaceSource | 本地窗口内容来源类型枚举。 |

### 函数

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [OHNativeWindow\* OH\_NativeWindow\_CreateNativeWindow(void\* pSurface)](capi-external-window-h.md#oh_nativewindow_createnativewindow) | 创建OHNativeWindow实例，每次调用都会产生一个新的OHNativeWindow实例。  说明：此接口不可用，可通过OH\_NativeImage\_AcquireNativeWindow创建，或通过XComponent创建。 |
| [void OH\_NativeWindow\_DestroyNativeWindow(OHNativeWindow\* window)](capi-external-window-h.md#oh_nativewindow_destroynativewindow) | 将OHNativeWindow对象的引用计数减1，当引用计数为0的时候，该OHNativeWindow对象会被析构掉。  本接口为非线程安全类型接口。 |
| [OHNativeWindowBuffer\* OH\_NativeWindow\_CreateNativeWindowBufferFromSurfaceBuffer(void\* pSurfaceBuffer)](capi-external-window-h.md#oh_nativewindow_createnativewindowbufferfromsurfacebuffer) | 创建OHNativeWindowBuffer实例，每次调用都会产生一个新的OHNativeWindowBuffer实例。  说明：此接口不可用，使用OH\_NativeWindow\_CreateNativeWindowBufferFromNativeBuffer替代。 |
| [OHNativeWindowBuffer\* OH\_NativeWindow\_CreateNativeWindowBufferFromNativeBuffer(OH\_NativeBuffer\* nativeBuffer)](capi-external-window-h.md#oh_nativewindow_createnativewindowbufferfromnativebuffer) | 创建OHNativeWindowBuffer实例，每次调用都会产生一个新的OHNativeWindowBuffer实例。  本接口需要与[OH\_NativeWindow\_DestroyNativeWindowBuffer](capi-external-window-h.md#oh_nativewindow_destroynativewindowbuffer)接口配合使用，否则会存在内存泄露。  本接口为非线程安全类型接口。 |
| [void OH\_NativeWindow\_DestroyNativeWindowBuffer(OHNativeWindowBuffer\* buffer)](capi-external-window-h.md#oh_nativewindow_destroynativewindowbuffer) | 将OHNativeWindowBuffer对象的引用计数减1，当引用计数为0的时候，该OHNativeWindowBuffer对象会被析构掉。  本接口为非线程安全类型接口。 |
| [int32\_t OH\_NativeWindow\_NativeWindowRequestBuffer(OHNativeWindow \*window,OHNativeWindowBuffer \*\*buffer, int \*fenceFd)](capi-external-window-h.md#oh_nativewindow_nativewindowrequestbuffer) | 通过OHNativeWindow对象申请一块OHNativeWindowBuffer，用以内容生产。  在调用本接口前，需要通过[SET\_BUFFER\_GEOMETRY](capi-external-window-h.md#nativewindowoperation)对OHNativeWindow设置宽高。  本接口需要与[OH\_NativeWindow\_NativeWindowFlushBuffer](capi-external-window-h.md#oh_nativewindow_nativewindowflushbuffer)接口配合使用，否则内存会耗尽。  当fenceFd使用完，用户需要将其close。  本接口为非线程安全类型接口。 |
| [int32\_t OH\_NativeWindow\_NativeWindowFlushBuffer(OHNativeWindow \*window, OHNativeWindowBuffer \*buffer,int fenceFd, Region region)](capi-external-window-h.md#oh_nativewindow_nativewindowflushbuffer) | 通过OHNativeWindow将生产好内容的OHNativeWindowBuffer放回到Buffer队列中，用以内容消费。  系统会将fenceFd关闭，无需用户close。  本接口为非线程安全类型接口。 |
| [int32\_t OH\_NativeWindow\_GetLastFlushedBuffer(OHNativeWindow \*window, OHNativeWindowBuffer \*\*buffer,int \*fenceFd, float matrix[16])](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-external-window-h#oh_nativewindow_getlastflushedbuffer) | 从OHNativeWindow获取上次送回到buffer队列中的OHNativeWindowBuffer。 |
| [int32\_t OH\_NativeWindow\_NativeWindowAbortBuffer(OHNativeWindow \*window, OHNativeWindowBuffer \*buffer)](capi-external-window-h.md#oh_nativewindow_nativewindowabortbuffer) | 通过OHNativeWindow将之前申请出来的OHNativeWindowBuffer返还到Buffer队列中，供下次再申请。  本接口为非线程安全类型接口。 |
| [int32\_t OH\_NativeWindow\_NativeWindowHandleOpt(OHNativeWindow \*window, int code, ...)](capi-external-window-h.md#oh_nativewindow_nativewindowhandleopt) | 设置/获取OHNativeWindow的属性，包括设置/获取宽高、内容格式等。  本接口为非线程安全类型接口。 |
| [BufferHandle \*OH\_NativeWindow\_GetBufferHandleFromNative(OHNativeWindowBuffer \*buffer)](capi-external-window-h.md#oh_nativewindow_getbufferhandlefromnative) | 通过OHNativeWindowBuffer获取该buffer的BufferHandle指针。  本接口为非线程安全类型接口。 |
| [int32\_t OH\_NativeWindow\_NativeObjectReference(void \*obj)](capi-external-window-h.md#oh_nativewindow_nativeobjectreference) | 增加一个NativeObject的引用计数。  本接口需要与[OH\_NativeWindow\_NativeObjectUnreference](capi-external-window-h.md#oh_nativewindow_nativeobjectunreference)接口配合使用，否则会存在内存泄露。  本接口为非线程安全类型接口。 |
| [int32\_t OH\_NativeWindow\_NativeObjectUnreference(void \*obj)](capi-external-window-h.md#oh_nativewindow_nativeobjectunreference) | 减少一个NativeObject的引用计数，当引用计数减少为0时，该NativeObject将被析构掉。  本接口为非线程安全类型接口。 |
| [int32\_t OH\_NativeWindow\_GetNativeObjectMagic(void \*obj)](capi-external-window-h.md#oh_nativewindow_getnativeobjectmagic) | 获取NativeObject的MagicId。  本接口为非线程安全类型接口。 |
| [int32\_t OH\_NativeWindow\_NativeWindowSetScalingMode(OHNativeWindow \*window, uint32\_t sequence,OHScalingMode scalingMode)](capi-external-window-h.md#oh_nativewindow_nativewindowsetscalingmode) | 设置OHNativeWindow的ScalingMode。 |
| [int32\_t OH\_NativeWindow\_NativeWindowSetMetaData(OHNativeWindow \*window, uint32\_t sequence, int32\_t size,const OHHDRMetaData \*metaData)](capi-external-window-h.md#oh_nativewindow_nativewindowsetmetadata) | 设置OHNativeWindow的元数据。 |
| [int32\_t OH\_NativeWindow\_NativeWindowSetMetaDataSet(OHNativeWindow \*window, uint32\_t sequence, OHHDRMetadataKey key,int32\_t size, const uint8\_t \*metaData)](capi-external-window-h.md#oh_nativewindow_nativewindowsetmetadataset) | 设置OHNativeWindow的元数据集。 |
| [int32\_t OH\_NativeWindow\_NativeWindowSetTunnelHandle(OHNativeWindow \*window, const OHExtDataHandle \*handle)](capi-external-window-h.md#oh_nativewindow_nativewindowsettunnelhandle) | 设置OHNativeWindow的TunnelHandle。 |
| [int32\_t OH\_NativeWindow\_NativeWindowAttachBuffer(OHNativeWindow \*window, OHNativeWindowBuffer \*buffer)](capi-external-window-h.md#oh_nativewindow_nativewindowattachbuffer) | 将OHNativeWindowBuffer添加进OHNativeWindow中。  本接口需要与[OH\_NativeWindow\_NativeWindowDetachBuffer](capi-external-window-h.md#oh_nativewindow_nativewindowdetachbuffer)接口配合使用，否则会存在内存管理混乱问题。  本接口为非线程安全类型接口。 |
| [int32\_t OH\_NativeWindow\_NativeWindowDetachBuffer(OHNativeWindow \*window, OHNativeWindowBuffer \*buffer)](capi-external-window-h.md#oh_nativewindow_nativewindowdetachbuffer) | 将OHNativeWindowBuffer从OHNativeWindow中分离。  本接口为非线程安全类型接口。 |
| [int32\_t OH\_NativeWindow\_GetSurfaceId(OHNativeWindow \*window, uint64\_t \*surfaceId)](capi-external-window-h.md#oh_nativewindow_getsurfaceid) | 通过OHNativeWindow获取对应的surfaceId。  本接口为非线程安全类型接口。 |
| [int32\_t OH\_NativeWindow\_CreateNativeWindowFromSurfaceId(uint64\_t surfaceId, OHNativeWindow \*\*window)](capi-external-window-h.md#oh_nativewindow_createnativewindowfromsurfaceid) | 通过surfaceId创建对应的OHNativeWindow。  本接口需要与[OH\_NativeWindow\_DestroyNativeWindow](capi-external-window-h.md#oh_nativewindow_destroynativewindow)接口配合使用，否则会存在内存泄露。  如果存在并发释放OHNativeWindow的情况，需要通过[OH\_NativeWindow\_NativeObjectReference](capi-external-window-h.md#oh_nativewindow_nativeobjectreference)和[OH\_NativeWindow\_NativeObjectUnreference](capi-external-window-h.md#oh_nativewindow_nativeobjectunreference)对OHNativeWindow进行引用计数加一和减一。  通过surfaceId获取的surface需要是在本进程中创建的，不能跨进程获取surface。  本接口为非线程安全类型接口。 |
| [int32\_t OH\_NativeWindow\_NativeWindowSetScalingModeV2(OHNativeWindow\* window, OHScalingModeV2 scalingMode)](capi-external-window-h.md#oh_nativewindow_nativewindowsetscalingmodev2) | 设置OHNativeWindow的渲染缩放模式。  本接口为非线程安全类型接口。 |
| [int32\_t OH\_NativeWindow\_GetLastFlushedBufferV2(OHNativeWindow \*window, OHNativeWindowBuffer \*\*buffer,int \*fenceFd, float matrix[16])](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-external-window-h#oh_nativewindow_getlastflushedbufferv2) | 从OHNativeWindow获取上次送回到buffer队列中的OHNativeWindowBuffer,与OH\_NativeWindow\_GetLastFlushedBuffer的差异在于matrix不同。  本接口需要与[OH\_NativeWindow\_NativeObjectUnreference](capi-external-window-h.md#oh_nativewindow_nativeobjectunreference)接口配合使用，否则会存在内存泄露。  本接口为非线程安全类型接口。 |
| [void OH\_NativeWindow\_SetBufferHold(OHNativeWindow \*window)](capi-external-window-h.md#oh_nativewindow_setbufferhold) | 启用单帧缓存机制，通过提前缓存一帧buffer并延迟显示，用于平滑帧率波动。 |
| [int32\_t OH\_NativeWindow\_WriteToParcel(OHNativeWindow \*window, OHIPCParcel \*parcel)](capi-external-window-h.md#oh_nativewindow_writetoparcel) | 将窗口对象写入IPC序列化对象中。  本接口为非线程安全类型接口。 |
| [int32\_t OH\_NativeWindow\_ReadFromParcel(OHIPCParcel \*parcel, OHNativeWindow \*\*window)](capi-external-window-h.md#oh_nativewindow_readfromparcel) | 从IPC序列化对象中读取窗口对象。  本接口将会创建一个OHNativeWindow，当窗口对象使用完，开发者需要与[OH\_NativeWindow\_DestroyNativeWindow](capi-external-window-h.md#oh_nativewindow_destroynativewindow)接口配合使用，否则会存在内存泄漏。  本接口为非线程安全类型接口。 |
| [int32\_t OH\_NativeWindow\_SetColorSpace(OHNativeWindow \*window, OH\_NativeBuffer\_ColorSpace colorSpace)](capi-external-window-h.md#oh_nativewindow_setcolorspace) | 为OHNativeWindow设置颜色空间属性。  本接口为非线程安全类型接口。 |
| [int32\_t OH\_NativeWindow\_GetColorSpace(OHNativeWindow \*window, OH\_NativeBuffer\_ColorSpace \*colorSpace)](capi-external-window-h.md#oh_nativewindow_getcolorspace) | 获取OHNativeWindow颜色空间属性。  本接口为非线程安全类型接口。 |
| [int32\_t OH\_NativeWindow\_SetMetadataValue(OHNativeWindow \*window, OH\_NativeBuffer\_MetadataKey metadataKey,int32\_t size, uint8\_t \*metadata)](capi-external-window-h.md#oh_nativewindow_setmetadatavalue) | 为OHNativeWindow设置元数据属性值。  本接口为非线程安全类型接口。 |
| [int32\_t OH\_NativeWindow\_GetMetadataValue(OHNativeWindow \*window, OH\_NativeBuffer\_MetadataKey metadataKey,int32\_t \*size, uint8\_t \*\*metadata)](capi-external-window-h.md#oh_nativewindow_getmetadatavalue) | 获取OHNativeWindow元数据属性值。  本接口为非线程安全类型接口。 |
| [int32\_t OH\_NativeWindow\_CleanCache(OHNativeWindow \*window)](capi-external-window-h.md#oh_nativewindow_cleancache) | 清理OHNativeWindow中的OHNativeWindowBuffer缓存。  使用该接口清理缓存前，需确保已通过[OH\_NativeWindow\_NativeWindowRequestBuffer](capi-external-window-h.md#oh_nativewindow_nativewindowrequestbuffer)接口成功申请OHNativeWindowBuffer。  本接口为非线程安全类型接口。 |
| [int32\_t OH\_NativeWindow\_PreAllocBuffers(OHNativeWindow \*window, uint32\_t allocBufferCnt)](capi-external-window-h.md#oh_nativewindow_preallocbuffers) | 通过OHNativeWindow对象提前申请多块OHNativeWindowBuffer，用以内容生产。  在调用本接口前，需要通过[OH\_NativeWindow\_NativeWindowHandleOpt](capi-external-window-h.md#oh_nativewindow_nativewindowhandleopt)对OHNativeWindow设置宽高。  本接口为非线程安全类型接口。 |
| [int32\_t OH\_NativeWindow\_LockBuffer(OHNativeWindow\* window, Region region, OHNativeWindowBuffer\*\* buffer)](capi-external-window-h.md#oh_nativewindow_lockbuffer) | 通过OHNativeWindow对象申请一块OHNativeWindowBuffer，用以内容生产，并对该OHNativeWindowBuffer加锁。  本接口需要和[OH\_NativeWindow\_UnlockAndFlushBuffer](capi-external-window-h.md#oh_nativewindow_unlockandflushbuffer)接口配合使用。  本接口对OHNativeWindowBuffer加锁后，需要调[OH\_NativeWindow\_UnlockAndFlushBuffer](capi-external-window-h.md#oh_nativewindow_unlockandflushbuffer)接口解锁后才能重新对OHNativeWindowBuffer加锁。  若用本接口重复对OHNativeWindowBuffer加锁，会返回操作非法错误码。  本接口支持通过CPU上的内存读写直接渲染图像。  本接口为非线程安全类型接口。 |
| [int32\_t OH\_NativeWindow\_UnlockAndFlushBuffer(OHNativeWindow\* window)](capi-external-window-h.md#oh_nativewindow_unlockandflushbuffer) | 通过OHNativeWindow将生产好内容的OHNativeWindowBuffer放回到Buffer队列中，用以内容消费，并对OHNativeWindowBuffer解锁。  本接口需要和[OH\_NativeWindow\_LockBuffer](capi-external-window-h.md#oh_nativewindow_lockbuffer)接口配合使用。  若用本接口重复对OHNativeWindowBuffer解锁，会返回操作非法错误码。  本接口为非线程安全类型接口。 |

## 枚举类型说明

PhonePC/2in1TabletTVWearable

### NativeWindowOperation

PhonePC/2in1TabletTVWearable

```
1. enum NativeWindowOperation
```

**描述**

OH\_NativeWindow\_NativeWindowHandleOpt函数中的操作码。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeWindow

**起始版本：** 8

| 枚举项 | 描述 |
| --- | --- |
| SET\_BUFFER\_GEOMETRY | 设置本地窗口缓冲区几何图形，函数中的可变参数是[输入] int32\_t width，[输入] int32\_t height。  **说明：** 设置与获取的宽高顺序不一致，请使用时注意。 |
| GET\_BUFFER\_GEOMETRY | 获取本地窗口缓冲区几何图形，函数中的可变参数是[输出] int32\_t \*height，[输出] int32\_t \*width。  **说明：** 获取与设置的宽高顺序不一致，请使用时注意。 |
| GET\_FORMAT | 获取本地窗口缓冲区格式，函数中的可变参数是[输出] int32\_t \*format，取值具体可见[OH\_NativeBuffer\_Format](capi-buffer-common-h.md#oh_nativebuffer_format)枚举值。 |
| SET\_FORMAT | 设置本地窗口缓冲区格式，函数中的可变参数是[输入] int32\_t format，取值具体可见[OH\_NativeBuffer\_Format](capi-buffer-common-h.md#oh_nativebuffer_format)枚举值。 |
| GET\_USAGE | 获取本地窗口读写方式，函数中的可变参数是[输出] uint64\_t \*usage，取值具体可见[OH\_NativeBuffer\_Usage](capi-native-buffer-h.md#oh_nativebuffer_usage)枚举值。 |
| SET\_USAGE | 设置本地窗口缓冲区读写方式，函数中的可变参数是[输入] uint64\_t usage，取值具体可见[OH\_NativeBuffer\_Usage](capi-native-buffer-h.md#oh_nativebuffer_usage)枚举值。 |
| SET\_STRIDE | 设置本地窗口缓冲区步幅，函数中的可变参数是[输入] int32\_t stride。  **废弃版本：** 16 |
| GET\_STRIDE | 获取本地窗口缓冲区步幅，函数中的可变参数是[输出] int32\_t \*stride。  **废弃版本：** 16  **替代方案：** 使用[OH\_NativeWindow\_GetBufferHandleFromNative](capi-external-window-h.md#oh_nativewindow_getbufferhandlefromnative)接口获取BufferHandle实例，从[BufferHandle](capi-nativewindow-bufferhandle.md)实例中获取stride值。 |
| SET\_SWAP\_INTERVAL | 设置本地窗口缓冲区交换间隔，函数中的可变参数是[输入] int32\_t interval。 |
| GET\_SWAP\_INTERVAL | 获取本地窗口缓冲区交换间隔，函数中的可变参数是[输出] int32\_t \*interval。 |
| SET\_TIMEOUT | 设置请求本地窗口请求缓冲区的超时等待时间，未手动设置时默认值为3000毫秒，函数中的可变参数是[输入] int32\_t timeout, 单位为毫秒。 |
| GET\_TIMEOUT | 获取请求本地窗口请求缓冲区的超时等待时间，未手动设置时默认值为3000毫秒，函数中的可变参数是[输出] int32\_t \*timeout，单位为毫秒。 |
| SET\_COLOR\_GAMUT | 设置本地窗口缓冲区色彩空间，函数中的可变参数是[输入] int32\_t colorGamut，取值具体可见[OH\_NativeBuffer\_ColorGamut](capi-native-buffer-h.md#oh_nativebuffer_colorgamut)枚举值。 |
| GET\_COLOR\_GAMUT | 获取本地窗口缓冲区色彩空间，函数中的可变参数是[输出] int32\_t \*colorGamut，取值具体可见[OH\_NativeBuffer\_ColorGamut](capi-native-buffer-h.md#oh_nativebuffer_colorgamut)枚举值。 |
| SET\_TRANSFORM | 设置本地窗口缓冲区变换，函数中的可变参数是[输入] int32\_t transform，取值具体可见[OH\_NativeBuffer\_TransformType](capi-buffer-common-h.md#oh_nativebuffer_transformtype)枚举值。 |
| GET\_TRANSFORM | 获取本地窗口缓冲区变换，函数中的可变参数是[输出] int32\_t \*transform，取值具体可见[OH\_NativeBuffer\_TransformType](capi-buffer-common-h.md#oh_nativebuffer_transformtype)枚举值。 |
| SET\_UI\_TIMESTAMP | 设置本地窗口缓冲区UI时间戳，函数中的可变参数是[输入] uint64\_t uiTimestamp。 |
| GET\_BUFFERQUEUE\_SIZE | 获取内存队列大小，函数中的可变参数是[输出] int32\_t \*size。  **起始版本：** 12 |
| SET\_SOURCE\_TYPE | 设置本地窗口内容来源，函数中的可变参数是[输入] int32\_t sourceType，取值具体可见[OHSurfaceSource](capi-external-window-h.md#ohsurfacesource)枚举值。  **起始版本：** 12 |
| GET\_SOURCE\_TYPE | 获取本地窗口内容来源，函数中的可变参数是[输出] int32\_t \*sourceType，取值具体可见[OHSurfaceSource](capi-external-window-h.md#ohsurfacesource)枚举值。  **起始版本：** 12 |
| SET\_APP\_FRAMEWORK\_TYPE | 设置本地窗口应用框架名称，函数中的可变参数是[输入] char\* frameworkType，最大支持64字节。  **起始版本：** 12 |
| GET\_APP\_FRAMEWORK\_TYPE | 获取本地窗口应用框架名称，函数中的可变参数是[输出] char\*\* frameworkType。  **起始版本：** 12 |
| SET\_HDR\_WHITE\_POINT\_BRIGHTNESS | 设置HDR白点亮度，函数中的可变参数是[输入] float brightness。取值范围为[0.0f, 1.0f]。  **起始版本：** 12 |
| SET\_SDR\_WHITE\_POINT\_BRIGHTNESS | 设置SDR白点亮度，函数中的可变参数是[输入] float brightness。取值范围为[0.0f, 1.0f]。  **起始版本：** 12 |
| SET\_DESIRED\_PRESENT\_TIMESTAMP = 24 | 设置本地窗口缓冲区期望上屏时间的时间戳。  当且仅当RenderService为本地窗口的消费者时，该时间戳生效  本操作执行后需要配合调用[OH\_NativeWindow\_NativeWindowFlushBuffer](capi-external-window-h.md#oh_nativewindow_nativewindowflushbuffer)生效。  生产者下一次放入队列的buffer，达到该期望上屏时间后，才会被RenderService消费并上屏。  如果buffer队列中存在多个生产者放入的buffer，都设置了desiredPresentTimestamp并已达到期望上屏时间，则较早入队的buffer将被消费者丢弃回队列。  如果期望上屏时间大于消费者提供的时间 1 秒以上，则该期望上屏时间戳将被忽略。  函数中的可变参数是[输入] int64\_t desiredPresentTimestamp，取值范围大于0，应由std::chrono::steady\_clock标准库时钟生成，且单位为纳秒。  **起始版本：** 13 |

### OHScalingMode

PhonePC/2in1TabletTVWearable

```
1. enum OHScalingMode
```

**描述**

缩放模式Scaling Mode。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeWindow

**起始版本：** 9

**废弃版本：** 10

**替代接口：** [OHScalingModeV2](capi-external-window-h.md#ohscalingmodev2)

| 枚举项 | 描述 |
| --- | --- |
| OH\_SCALING\_MODE\_FREEZE = 0 | 在接收到窗口大小的缓冲区之前，不可以更新窗口内容。 |
| OH\_SCALING\_MODE\_SCALE\_TO\_WINDOW | 缓冲区在二维中缩放以匹配窗口大小。 |
| OH\_SCALING\_MODE\_SCALE\_CROP | 缓冲区被统一缩放，使得缓冲区的较小尺寸与窗口大小匹配。 |
| OH\_SCALING\_MODE\_NO\_SCALE\_CROP | 窗口被裁剪为缓冲区裁剪矩形的大小，裁剪矩形之外的像素被视为完全透明。 |

### OHScalingModeV2

PhonePC/2in1TabletTVWearable

```
1. enum OHScalingModeV2
```

**描述**

渲染缩放模式枚举。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeWindow

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| OH\_SCALING\_MODE\_FREEZE\_V2 = 0 | 冻结窗口，在接收到和窗口大小相等的缓冲区之前，窗口内容不进行更新。 |
| OH\_SCALING\_MODE\_SCALE\_TO\_WINDOW\_V2 | 缓冲区进行拉伸缩放以匹配窗口大小。 |
| OH\_SCALING\_MODE\_SCALE\_CROP\_V2 | 缓冲区按原比例缩放，使得缓冲区的较小边与窗口匹配，较长边超出窗口部分被视为透明。 |
| OH\_SCALING\_MODE\_NO\_SCALE\_CROP\_V2 | 按窗口大小将缓冲区裁剪，裁剪矩形之外的像素被视为完全透明。 |
| OH\_SCALING\_MODE\_SCALE\_FIT\_V2 | 缓冲区按原比例缩放。优先显示所有缓冲区内容。如果比例与窗口比例不同，用背景颜色填充窗口的未填充区域。  模拟器不支持该模式。 |

### OHHDRMetadataKey

PhonePC/2in1TabletTVWearable

```
1. enum OHHDRMetadataKey
```

**描述**

枚举HDR元数据关键字。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeWindow

**起始版本：** 9

**废弃版本：** 10

| 枚举项 | 描述 |
| --- | --- |
| OH\_METAKEY\_RED\_PRIMARY\_X = 0 | 红基色X坐标。 |
| OH\_METAKEY\_RED\_PRIMARY\_Y = 1, | 红基色Y坐标。 |
| OH\_METAKEY\_GREEN\_PRIMARY\_X = 2, | 绿基色X坐标。 |
| OH\_METAKEY\_GREEN\_PRIMARY\_Y = 3, | 绿基色Y坐标。 |
| OH\_METAKEY\_BLUE\_PRIMARY\_X = 4, | 蓝基色X坐标。 |
| OH\_METAKEY\_BLUE\_PRIMARY\_Y = 5, | 蓝基色Y坐标。 |
| OH\_METAKEY\_WHITE\_PRIMARY\_X = 6, | 白点X坐标。 |
| OH\_METAKEY\_WHITE\_PRIMARY\_Y = 7, | 白点Y坐标。 |
| OH\_METAKEY\_MAX\_LUMINANCE = 8, | 最大的光亮度。 |
| OH\_METAKEY\_MIN\_LUMINANCE = 9, | 最小的光亮度。 |
| OH\_METAKEY\_MAX\_CONTENT\_LIGHT\_LEVEL = 10, | 最大的内容亮度水平。 |
| OH\_METAKEY\_MAX\_FRAME\_AVERAGE\_LIGHT\_LEVEL = 11, | 最大的帧平均亮度水平。 |
| OH\_METAKEY\_HDR10\_PLUS = 12, | HDR10 Plus。 |
| OH\_METAKEY\_HDR\_VIVID = 13, | Vivid。 |

### OHSurfaceSource

PhonePC/2in1TabletTVWearable

```
1. enum OHSurfaceSource
```

**描述**

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeWindow

本地窗口内容来源类型枚举。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| OH\_SURFACE\_SOURCE\_DEFAULT = 0 | 窗口内容默认来源。 |
| OH\_SURFACE\_SOURCE\_UI | 窗口内容来自于UI。 |
| OH\_SURFACE\_SOURCE\_GAME | 窗口内容来自于游戏。 |
| OH\_SURFACE\_SOURCE\_CAMERA | 窗口内容来自于相机。 |
| OH\_SURFACE\_SOURCE\_VIDEO | 窗口内容来自于视频。 |

## 函数说明

PhonePC/2in1TabletTVWearable

### OH\_NativeWindow\_CreateNativeWindow()

PhonePC/2in1TabletTVWearable

```
1. OHNativeWindow* OH_NativeWindow_CreateNativeWindow(void* pSurface)
```

**描述**

创建OHNativeWindow实例，每次调用都会产生一个新的OHNativeWindow实例。

说明：此接口不可用，可通过[OH\_NativeImage\_AcquireNativeWindow](capi-native-image-h.md#oh_nativeimage_acquirenativewindow)创建，或通过XComponent创建。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeWindow

**起始版本：** 8

**废弃版本：** 从API version 12开始废弃，不再提供替代接口。

**参数：**

| 参数项 | 描述 |
| --- | --- |
| void\* pSurface | 一个指向生产者ProduceSurface的指针，类型为sptr<OHOS::Surface>。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OHNativeWindow](capi-nativewindow-nativewindow.md)\* | 返回一个指针，指向OHNativeWindow的结构体实例。 |

### OH\_NativeWindow\_DestroyNativeWindow()

PhonePC/2in1TabletTVWearable

```
1. void OH_NativeWindow_DestroyNativeWindow(OHNativeWindow* window)
```

**描述**

将OHNativeWindow对象的引用计数减1，当引用计数为0的时候，该OHNativeWindow对象会被析构掉。

本接口为非线程安全类型接口。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeWindow

**起始版本：** 8

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OHNativeWindow](capi-nativewindow-nativewindow.md)\* window | 一个OHNativeWindow的结构体实例的指针。 |

### OH\_NativeWindow\_CreateNativeWindowBufferFromSurfaceBuffer()

PhonePC/2in1TabletTVWearable

```
1. OHNativeWindowBuffer* OH_NativeWindow_CreateNativeWindowBufferFromSurfaceBuffer(void* pSurfaceBuffer)
```

**描述**

创建OHNativeWindowBuffer实例，每次调用都会产生一个新的OHNativeWindowBuffer实例。

说明：此接口不可用，使用[OH\_NativeWindow\_CreateNativeWindowBufferFromNativeBuffer](capi-external-window-h.md#oh_nativewindow_createnativewindowbufferfromnativebuffer)替代。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeWindow

**起始版本：** 8

**废弃版本：** 12

**替代接口：** [OH\_NativeWindow\_CreateNativeWindowBufferFromNativeBuffer](capi-external-window-h.md#oh_nativewindow_createnativewindowbufferfromnativebuffer)

**参数：**

| 参数项 | 描述 |
| --- | --- |
| void\* pSurfaceBuffer | 一个指向生产者buffer的指针，类型为sptrOHOS::SurfaceBuffer。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| OHNativeWindowBuffer\* | 返回一个指针，指向OHNativeWindowBuffer的结构体实例。 |

### OH\_NativeWindow\_CreateNativeWindowBufferFromNativeBuffer()

PhonePC/2in1TabletTVWearable

```
1. OHNativeWindowBuffer* OH_NativeWindow_CreateNativeWindowBufferFromNativeBuffer(OH_NativeBuffer* nativeBuffer)
```

**描述**

创建OHNativeWindowBuffer实例，每次调用都会产生一个新的OHNativeWindowBuffer实例。

本接口需要与[OH\_NativeWindow\_DestroyNativeWindowBuffer](capi-external-window-h.md#oh_nativewindow_destroynativewindowbuffer)接口配合使用，否则会存在内存泄露。

本接口为非线程安全类型接口。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeWindow

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| OH\_NativeBuffer\* nativeBuffer | 一个指向OH\_NativeBuffer的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| OHNativeWindowBuffer\* | 返回一个指针，指向OHNativeWindowBuffer的结构体实例。 |

### OH\_NativeWindow\_DestroyNativeWindowBuffer()

PhonePC/2in1TabletTVWearable

```
1. void OH_NativeWindow_DestroyNativeWindowBuffer(OHNativeWindowBuffer* buffer)
```

**描述**

将OHNativeWindowBuffer对象的引用计数减1，当引用计数为0的时候，该OHNativeWindowBuffer对象会被析构掉。

本接口为非线程安全类型接口。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeWindow

**起始版本：** 8

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OHNativeWindowBuffer](capi-nativewindow-nativewindowbuffer.md)\* buffer | 一个OHNativeWindowBuffer的结构体实例的指针。 |

### OH\_NativeWindow\_NativeWindowRequestBuffer()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_NativeWindow_NativeWindowRequestBuffer(OHNativeWindow *window,OHNativeWindowBuffer **buffer, int *fenceFd)
```

**描述**

通过OHNativeWindow对象申请一块OHNativeWindowBuffer，用以内容生产。

在调用本接口前，需要通过[SET\_BUFFER\_GEOMETRY](capi-external-window-h.md#nativewindowoperation)对OHNativeWindow设置宽高。

未设置宽高将使用消费端设置的默认宽高。

本接口需要与[OH\_NativeWindow\_NativeWindowFlushBuffer](capi-external-window-h.md#oh_nativewindow_nativewindowflushbuffer)接口配合使用，否则内存会耗尽。

当fenceFd使用完，用户需要将其close。

本接口为非线程安全类型接口。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeWindow

**起始版本：** 8

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OHNativeWindow](capi-nativewindow-nativewindow.md) \*window | 一个OHNativeWindow的结构体实例的指针。 |
| [OHNativeWindowBuffer](capi-nativewindow-nativewindowbuffer.md) \*\*buffer | 一个指向OHNativeWindowBuffer指针的指针（二级指针）。  通过OH\_NativeWindow\_GetBufferHandleFromNative可获取BufferHandle结构体，访问缓冲区内存。 |
| int \*fenceFd | 一个文件描述符句柄，用于GPU/CPU同步：不同取值及含义如下：  - 返回≥0：缓冲区正被GPU使用，需要等待文件描述符fenceFd就绪。  - 返回-1：缓冲区可直接使用。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回值为0表示执行成功，其他返回值可参考[OHNativeErrorCode](capi-graphic-error-code-h.md#ohnativeerrorcode)。 |

### OH\_NativeWindow\_NativeWindowFlushBuffer()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_NativeWindow_NativeWindowFlushBuffer(OHNativeWindow *window, OHNativeWindowBuffer *buffer,int fenceFd, Region region)
```

**描述**

通过OHNativeWindow将生产好内容的OHNativeWindowBuffer放回到Buffer队列中，用以内容消费。

系统会将fenceFd关闭，无需用户close。

本接口为非线程安全类型接口。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeWindow

**起始版本：** 8

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OHNativeWindow](capi-nativewindow-nativewindow.md) \*window | 一个OHNativeWindow的结构体实例的指针。 |
| [OHNativeWindowBuffer](capi-nativewindow-nativewindowbuffer.md) \*buffer | 一个OHNativeWindowBuffer的结构体实例的指针。 |
| int fenceFd | 一个文件描述符句柄，用以同步时序。不同取值及含义如下：  - -1：CPU渲染完成，无需同步时序。  - ≥0：从GPU同步对象转换（如EGL的eglDupNativeFenceFDANDROID），对端需要通过此fenceFd同步时序。 |
| [Region](capi-nativewindow-region.md) region | 一个Region结构体，表示一块脏区域，该区域有内容更新。  Region.rectNumber限制最大数量为1000，当rectNumber≤0或者rectNumber>1000时，使用整个buffer作为脏区。  Region.rect以buffer左下角为坐标原点。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回值为0表示执行成功，其他返回值可参考[OHNativeErrorCode](capi-graphic-error-code-h.md#ohnativeerrorcode)。 |

### OH\_NativeWindow\_GetLastFlushedBuffer()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_NativeWindow_GetLastFlushedBuffer(OHNativeWindow *window, OHNativeWindowBuffer **buffer,int *fenceFd, float matrix[16])
```

**描述**

从OHNativeWindow获取上次送回到buffer队列中的OHNativeWindowBuffer。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeWindow

**起始版本：** 11

**废弃版本：** 从API version 12开始废弃。

**替代接口：** [OH\_NativeWindow\_GetLastFlushedBufferV2](capi-external-window-h.md#oh_nativewindow_getlastflushedbufferv2)

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OHNativeWindow](capi-nativewindow-nativewindow.md) \*window | 一个OHNativeWindow的结构体实例的指针。 |
| [OHNativeWindowBuffer](capi-nativewindow-nativewindowbuffer.md) \*\*buffer | 一个OHNativeWindowBuffer结构体指针的指针。 |
| int \*fenceFd | 一个文件描述符的指针。 |
| matrix | 表示检索到的4\*4变换矩阵。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回值为0表示执行成功，其他返回值可参考[OHNativeErrorCode](capi-graphic-error-code-h.md#ohnativeerrorcode)。 |

### OH\_NativeWindow\_NativeWindowAbortBuffer()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_NativeWindow_NativeWindowAbortBuffer(OHNativeWindow *window, OHNativeWindowBuffer *buffer)
```

**描述**

通过OHNativeWindow将之前申请出来的OHNativeWindowBuffer返还到Buffer队列中，供下次再申请。

本接口为非线程安全类型接口。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeWindow

**起始版本：** 8

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OHNativeWindow](capi-nativewindow-nativewindow.md) \*window | 一个OHNativeWindow的结构体实例的指针。 |
| [OHNativeWindowBuffer](capi-nativewindow-nativewindowbuffer.md) \*buffer | 一个OHNativeWindowBuffer的结构体实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回值为0表示执行成功，其他返回值可参考[OHNativeErrorCode](capi-graphic-error-code-h.md#ohnativeerrorcode)。 |

### OH\_NativeWindow\_NativeWindowHandleOpt()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_NativeWindow_NativeWindowHandleOpt(OHNativeWindow *window, int code, ...)
```

**描述**

设置/获取OHNativeWindow的属性，包括设置/获取宽高、内容格式等。

本接口为非线程安全类型接口。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeWindow

**起始版本：** 8

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OHNativeWindow](capi-nativewindow-nativewindow.md) \*window | 一个OHNativeWindow的结构体实例的指针。 |
| int code | 表示操作码，详见[NativeWindowOperation](capi-external-window-h.md#nativewindowoperation)。 |
| ... | 可变参数，必须与操作码对应的数据类型保持一致，且入参数量严格按照操作码提示传入，否则会存在未定义行为。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回值为0表示执行成功，其他返回值可参考[OHNativeErrorCode](capi-graphic-error-code-h.md#ohnativeerrorcode)。 |

### OH\_NativeWindow\_GetBufferHandleFromNative()

PhonePC/2in1TabletTVWearable

```
1. BufferHandle *OH_NativeWindow_GetBufferHandleFromNative(OHNativeWindowBuffer *buffer)
```

**描述**

通过OHNativeWindowBuffer获取该buffer的BufferHandle指针。

本接口为非线程安全类型接口。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeWindow

**起始版本：** 8

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OHNativeWindowBuffer](capi-nativewindow-nativewindowbuffer.md) \*buffer | 一个OHNativeWindowBuffer的结构体实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [BufferHandle](capi-nativewindow-bufferhandle.md) | BufferHandle 返回一个指针，指向[BufferHandle](capi-nativewindow-bufferhandle.md)的结构体实例。 |

### OH\_NativeWindow\_NativeObjectReference()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_NativeWindow_NativeObjectReference(void *obj)
```

**描述**

增加一个NativeObject的引用计数。

本接口需要与[OH\_NativeWindow\_NativeObjectUnreference](capi-external-window-h.md#oh_nativewindow_nativeobjectunreference)接口配合使用，否则会存在内存泄露。

本接口为非线程安全类型接口。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeWindow

**起始版本：** 8

**参数：**

| 参数项 | 描述 |
| --- | --- |
| void \*obj | 一个OHNativeWindow或者OHNativeWindowBuffer的结构体实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回值为0表示执行成功，其他返回值可参考[OHNativeErrorCode](capi-graphic-error-code-h.md#ohnativeerrorcode)。 |

### OH\_NativeWindow\_NativeObjectUnreference()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_NativeWindow_NativeObjectUnreference(void *obj)
```

**描述**

减少一个NativeObject的引用计数，当引用计数减少为0时，该NativeObject将被析构掉。

本接口为非线程安全类型接口。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeWindow

**起始版本：** 8

**参数：**

| 参数项 | 描述 |
| --- | --- |
| void \*obj | 一个OHNativeWindow或者OHNativeWindowBuffer的结构体实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回值为0表示执行成功，其他返回值可参考[OHNativeErrorCode](capi-graphic-error-code-h.md#ohnativeerrorcode)。 |

### OH\_NativeWindow\_GetNativeObjectMagic()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_NativeWindow_GetNativeObjectMagic(void *obj)
```

**描述**

获取NativeObject的MagicId。

本接口为非线程安全类型接口。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeWindow

**起始版本：** 8

**参数：**

| 参数项 | 描述 |
| --- | --- |
| void \*obj | 一个OHNativeWindow或者OHNativeWindowBuffer的结构体实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | MagicId 返回值为魔鬼数字，每个NativeObject唯一。 |

### OH\_NativeWindow\_NativeWindowSetScalingMode()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_NativeWindow_NativeWindowSetScalingMode(OHNativeWindow *window, uint32_t sequence,OHScalingMode scalingMode)
```

**描述**

设置OHNativeWindow的ScalingMode。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeWindow

**起始版本：** 9

**废弃版本：** 从API version 10开始废弃。

**替代接口：** [OH\_NativeWindow\_NativeWindowSetScalingModeV2](capi-external-window-h.md#oh_nativewindow_nativewindowsetscalingmodev2)

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OHNativeWindow](capi-nativewindow-nativewindow.md) \*window | 一个OHNativeWindow的结构体实例的指针。 |
| uint32\_t sequence | 生产缓冲区的序列。 |
| [OHScalingMode](capi-external-window-h.md#ohscalingmode) scalingMode | 枚举值OHScalingMode。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回值为0表示执行成功，其他返回值可参考[OHNativeErrorCode](capi-graphic-error-code-h.md#ohnativeerrorcode)。 |

### OH\_NativeWindow\_NativeWindowSetMetaData()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_NativeWindow_NativeWindowSetMetaData(OHNativeWindow *window, uint32_t sequence, int32_t size,const OHHDRMetaData *metaData)
```

**描述**

设置OHNativeWindow的元数据。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeWindow

**起始版本：** 9

**废弃版本：** 从API version 10开始废弃，不再提供替代接口。

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OHNativeWindow](capi-nativewindow-nativewindow.md) \*window | 一个OHNativeWindow的结构体实例的指针。 |
| uint32\_t sequence | 生产缓冲区的序列。 |
| int32\_t size | OHHDRMetaData数组的大小，最大支持为3000，超出会返回NATIVE\_ERROR\_INVALID\_ARGUMENTS。 |
| metaData | 指向OHHDRMetaData数组的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回值为0表示执行成功，其他返回值可参考[OHNativeErrorCode](capi-graphic-error-code-h.md#ohnativeerrorcode)。 |

### OH\_NativeWindow\_NativeWindowSetMetaDataSet()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_NativeWindow_NativeWindowSetMetaDataSet(OHNativeWindow *window, uint32_t sequence, OHHDRMetadataKey key,int32_t size, const uint8_t *metaData)
```

**描述**

设置OHNativeWindow的元数据集。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeWindow

**起始版本：** 9

**废弃版本：** 从API version 10开始废弃，不再提供替代接口。

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OHNativeWindow](capi-nativewindow-nativewindow.md) \*window | 一个OHNativeWindow的结构体实例的指针。 |
| uint32\_t sequence | 生产缓冲区的序列。 |
| [OHHDRMetadataKey](capi-external-window-h.md#ohhdrmetadatakey) key | 枚举值OHHDRMetadataKey。 |
| int32\_t size | uint8\_t向量的大小，最大支持为3000，超出会返回NATIVE\_ERROR\_INVALID\_ARGUMENTS。 |
| metaData | 指向uint8\_t向量的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回值为0表示执行成功，其他返回值可参考[OHNativeErrorCode](capi-graphic-error-code-h.md#ohnativeerrorcode)。 |

### OH\_NativeWindow\_NativeWindowSetTunnelHandle()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_NativeWindow_NativeWindowSetTunnelHandle(OHNativeWindow *window, const OHExtDataHandle *handle)
```

**描述**

设置OHNativeWindow的TunnelHandle。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeWindow

**起始版本：** 9

**废弃版本：** 从API version 10开始废弃，不再提供替代接口。

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OHNativeWindow](capi-nativewindow-nativewindow.md) \*window | 一个OHNativeWindow的结构体实例的指针。 |
| const [OHExtDataHandle](capi-nativewindow-ohextdatahandle.md) \*handle | 指向OHExtDataHandle的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回值为0表示执行成功，其他返回值可参考[OHNativeErrorCode](capi-graphic-error-code-h.md#ohnativeerrorcode)。 |

### OH\_NativeWindow\_NativeWindowAttachBuffer()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_NativeWindow_NativeWindowAttachBuffer(OHNativeWindow *window, OHNativeWindowBuffer *buffer)
```

**描述**

将OHNativeWindowBuffer添加进OHNativeWindow中。

本接口需要与[OH\_NativeWindow\_NativeWindowDetachBuffer](capi-external-window-h.md#oh_nativewindow_nativewindowdetachbuffer)接口配合使用，否则会存在内存管理混乱问题。

本接口为非线程安全类型接口。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeWindow

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OHNativeWindow](capi-nativewindow-nativewindow.md) \*window | 一个OHNativeWindow的结构体实例的指针。 |
| [OHNativeWindowBuffer](capi-nativewindow-nativewindowbuffer.md) \*buffer | 一个OHNativeWindowBuffer的结构体实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回值为0表示执行成功，其他返回值可参考[OHNativeErrorCode](capi-graphic-error-code-h.md#ohnativeerrorcode)。 |

### OH\_NativeWindow\_NativeWindowDetachBuffer()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_NativeWindow_NativeWindowDetachBuffer(OHNativeWindow *window, OHNativeWindowBuffer *buffer)
```

**描述**

将OHNativeWindowBuffer从OHNativeWindow中分离。

本接口为非线程安全类型接口。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeWindow

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OHNativeWindow](capi-nativewindow-nativewindow.md) \*window | 一个OHNativeWindow的结构体实例的指针。 |
| [OHNativeWindowBuffer](capi-nativewindow-nativewindowbuffer.md) \*buffer | 一个OHNativeWindowBuffer的结构体实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回值为0表示执行成功，其他返回值可参考[OHNativeErrorCode](capi-graphic-error-code-h.md#ohnativeerrorcode)。 |

### OH\_NativeWindow\_GetSurfaceId()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_NativeWindow_GetSurfaceId(OHNativeWindow *window, uint64_t *surfaceId)
```

**描述**

通过OHNativeWindow获取对应的surfaceId。

本接口为非线程安全类型接口。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeWindow

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OHNativeWindow](capi-nativewindow-nativewindow.md) \*window | 一个OHNativeWindow的结构体实例的指针。 |
| uint64\_t \*surfaceId | 一个surface对应ID的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回值为0表示执行成功，其他返回值可参考[OHNativeErrorCode](capi-graphic-error-code-h.md#ohnativeerrorcode)。 |

### OH\_NativeWindow\_CreateNativeWindowFromSurfaceId()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_NativeWindow_CreateNativeWindowFromSurfaceId(uint64_t surfaceId, OHNativeWindow **window)
```

**描述**

通过surfaceId创建对应的OHNativeWindow。

本接口需要与[OH\_NativeWindow\_DestroyNativeWindow](capi-external-window-h.md#oh_nativewindow_destroynativewindow)接口配合使用，否则会存在内存泄露。

如果存在并发释放OHNativeWindow的情况，需要通过[OH\_NativeWindow\_NativeObjectReference](capi-external-window-h.md#oh_nativewindow_nativeobjectreference)和[OH\_NativeWindow\_NativeObjectUnreference](capi-external-window-h.md#oh_nativewindow_nativeobjectunreference)对OHNativeWindow进行引用计数加一和减一。

通过surfaceId获取的surface需要是在本进程中创建的，不能跨进程获取surface。

本接口为非线程安全类型接口。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeWindow

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| uint64\_t surfaceId | 一个surface对应的ID。 |
| [OHNativeWindow](capi-nativewindow-nativewindow.md) \*\*window | 一个OHNativeWindow的结构体实例的二级指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回值为0表示执行成功，其他返回值可参考[OHNativeErrorCode](capi-graphic-error-code-h.md#ohnativeerrorcode)。 |

### OH\_NativeWindow\_NativeWindowSetScalingModeV2()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_NativeWindow_NativeWindowSetScalingModeV2(OHNativeWindow* window, OHScalingModeV2 scalingMode)
```

**描述**

设置OHNativeWindow的渲染缩放模式。

本接口为非线程安全类型接口。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeWindow

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OHNativeWindow](capi-nativewindow-nativewindow.md)\* window | 一个OHNativeWindow的结构体实例的指针。 |
| [OHScalingModeV2](capi-external-window-h.md#ohscalingmodev2) scalingMode | 一个OHScalingModeV2类型的枚举值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回值为0表示执行成功，其他返回值可参考[OHNativeErrorCode](capi-graphic-error-code-h.md#ohnativeerrorcode)。 |

### OH\_NativeWindow\_GetLastFlushedBufferV2()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_NativeWindow_GetLastFlushedBufferV2(OHNativeWindow *window, OHNativeWindowBuffer **buffer,int *fenceFd, float matrix[16])
```

**描述**

从OHNativeWindow获取上次送回到buffer队列中的OHNativeWindowBuffer,与OH\_NativeWindow\_GetLastFlushedBuffer的差异在于matrix不同。

本接口需要与[OH\_NativeWindow\_NativeObjectUnreference](capi-external-window-h.md#oh_nativewindow_nativeobjectunreference)接口配合使用，否则会存在内存泄露。

本接口为非线程安全类型接口。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeWindow

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OHNativeWindow](capi-nativewindow-nativewindow.md) \*window | 一个OHNativeWindow的结构体实例的指针。 |
| [OHNativeWindowBuffer](capi-nativewindow-nativewindowbuffer.md) \*\*buffer | 一个OHNativeWindowBuffer结构体指针的指针。 |
| int \*fenceFd | 一个文件描述符的指针。 |
| matrix | 表示检索到的4\*4变换矩阵。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回值为0表示执行成功，其他返回值可参考[OHNativeErrorCode](capi-graphic-error-code-h.md#ohnativeerrorcode)。 |

### OH\_NativeWindow\_SetBufferHold()

PhonePC/2in1TabletTVWearable

```
1. void OH_NativeWindow_SetBufferHold(OHNativeWindow *window)
```

**描述**

启用单帧缓存机制，通过提前缓存一帧buffer并延迟显示，用于平滑帧率波动。

启用后，系统会预留一帧buffer作为缓冲，该帧会延迟一个显示周期才上屏。当后续渲染出现超长帧或帧间不均匀时，可使用该缓存帧填补空白，减少画面卡顿。

建议在预知即将出现渲染高峰前提前调用，以建立缓冲保护；缓存仅生效一次，被消费后自动失效，如需持续保护需重新调用本接口。

适用于游戏、动画、复杂UI渲染等对帧率稳定性要求较高的场景，但会引入一帧显示延迟（比如，在60hz的刷新率下，会延迟16.6ms上屏显示），不建议在高交互实时场景中使用。

本接口为非线程安全类型接口。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeWindow

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OHNativeWindow](capi-nativewindow-nativewindow.md) \*window | 一个[OHNativeWindow](capi-nativewindow-nativewindow.md)的结构体实例的指针。 |

### OH\_NativeWindow\_WriteToParcel()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_NativeWindow_WriteToParcel(OHNativeWindow *window, OHIPCParcel *parcel)
```

**描述**

将窗口对象写入IPC序列化对象中。

本接口为非线程安全类型接口。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeWindow

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OHNativeWindow](capi-nativewindow-nativewindow.md) \*window | 一个指向[OHNativeWindow](capi-nativewindow-nativewindow.md)的结构体实例的指针。 |
| [OHIPCParcel](capi-nativewindow-ohipcparcel.md) \*parcel | 一个指向[OHIPCParcel](capi-nativewindow-ohipcparcel.md)的结构体实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回值为0表示执行成功，其他返回值可参考[OHNativeErrorCode](capi-graphic-error-code-h.md#ohnativeerrorcode)。 |

### OH\_NativeWindow\_ReadFromParcel()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_NativeWindow_ReadFromParcel(OHIPCParcel *parcel, OHNativeWindow **window)
```

**描述**

从IPC序列化对象中读取窗口对象。

本接口将会创建一个OHNativeWindow，当窗口对象使用完，开发者需要与[OH\_NativeWindow\_DestroyNativeWindow](capi-external-window-h.md#oh_nativewindow_destroynativewindow)接口配合使用，否则会存在内存泄漏。

本接口为非线程安全类型接口。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeWindow

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OHIPCParcel](capi-nativewindow-ohipcparcel.md) \*parcel | 一个指向[OHIPCParcel](capi-nativewindow-ohipcparcel.md)的结构体实例的指针。 |
| [OHNativeWindow](capi-nativewindow-nativewindow.md) \*\*window | 一个指向[OHNativeWindow](capi-nativewindow-nativewindow.md)的结构体实例的二级指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回值为0表示执行成功，其他返回值可参考[OHNativeErrorCode](capi-graphic-error-code-h.md#ohnativeerrorcode)。 |

### OH\_NativeWindow\_SetColorSpace()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_NativeWindow_SetColorSpace(OHNativeWindow *window, OH_NativeBuffer_ColorSpace colorSpace)
```

**描述**

为OHNativeWindow设置颜色空间属性。

本接口为非线程安全类型接口。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeWindow

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OHNativeWindow](capi-nativewindow-nativewindow.md) \*window | 一个指向[OHNativeWindow](capi-nativewindow-nativewindow.md)的结构体实例的指针。 |
| [OH\_NativeBuffer\_ColorSpace](capi-buffer-common-h.md#oh_nativebuffer_colorspace) colorSpace | 为OHNativeWindow设置的颜色空间，其值从[OH\_NativeBuffer\_ColorSpace](capi-buffer-common-h.md#oh_nativebuffer_colorspace)获取。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回值为0表示执行成功，其他返回值可参考[OHNativeErrorCode](capi-graphic-error-code-h.md#ohnativeerrorcode)。 |

### OH\_NativeWindow\_GetColorSpace()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_NativeWindow_GetColorSpace(OHNativeWindow *window, OH_NativeBuffer_ColorSpace *colorSpace)
```

**描述**

获取OHNativeWindow颜色空间属性。

本接口为非线程安全类型接口。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeWindow

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OHNativeWindow](capi-nativewindow-nativewindow.md) \*window | 一个指向[OHNativeWindow](capi-nativewindow-nativewindow.md)的结构体实例的指针。 |
| [OH\_NativeBuffer\_ColorSpace](capi-buffer-common-h.md#oh_nativebuffer_colorspace) \*colorSpace | 为OHNativeWindow设置的颜色空间，其值从[OH\_NativeBuffer\_ColorSpace](capi-buffer-common-h.md#oh_nativebuffer_colorspace)获取。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回值为0表示执行成功，其他返回值可参考[OHNativeErrorCode](capi-graphic-error-code-h.md#ohnativeerrorcode)。 |

### OH\_NativeWindow\_SetMetadataValue()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_NativeWindow_SetMetadataValue(OHNativeWindow *window, OH_NativeBuffer_MetadataKey metadataKey,int32_t size, uint8_t *metadata)
```

**描述**

为OHNativeWindow设置元数据属性值。

本接口为非线程安全类型接口。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeWindow

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OHNativeWindow](capi-nativewindow-nativewindow.md) \*window | 一个指向[OHNativeWindow](capi-nativewindow-nativewindow.md)的结构体实例的指针。 |
| [OH\_NativeBuffer\_MetadataKey](capi-buffer-common-h.md#oh_nativebuffer_metadatakey) metadataKey | Window的元数据类型，其值从[OH\_NativeBuffer\_MetadataKey](capi-buffer-common-h.md#oh_nativebuffer_metadatakey)获取。 |
| int32\_t size | uint8\_t向量的大小，其取值范围见[OH\_NativeBuffer\_MetadataKey](capi-buffer-common-h.md#oh_nativebuffer_metadatakey)。 |
| metadata | 指向uint8\_t向量的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回值为0表示执行成功，其他返回值可参考[OHNativeErrorCode](capi-graphic-error-code-h.md#ohnativeerrorcode)。 |

### OH\_NativeWindow\_GetMetadataValue()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_NativeWindow_GetMetadataValue(OHNativeWindow *window, OH_NativeBuffer_MetadataKey metadataKey,int32_t *size, uint8_t **metadata)
```

**描述**

获取OHNativeWindow元数据属性值。

本接口为非线程安全类型接口。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeWindow

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OHNativeWindow](capi-nativewindow-nativewindow.md) \*window | 一个指向[OHNativeWindow](capi-nativewindow-nativewindow.md)的结构体实例的指针。 |
| [OH\_NativeBuffer\_MetadataKey](capi-buffer-common-h.md#oh_nativebuffer_metadatakey) metadataKey | Window的元数据类型，其值从[OH\_NativeBuffer\_MetadataKey](capi-buffer-common-h.md#oh_nativebuffer_metadatakey)获取。 |
| int32\_t \*size | uint8\_t向量的大小，其取值范围见[OH\_NativeBuffer\_MetadataKey](capi-buffer-common-h.md#oh_nativebuffer_metadatakey)。 |
| metadata | 指向uint8\_t向量的二级指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回值为0表示执行成功，其他返回值可参考[OHNativeErrorCode](capi-graphic-error-code-h.md#ohnativeerrorcode)。 |

### OH\_NativeWindow\_CleanCache()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_NativeWindow_CleanCache(OHNativeWindow *window)
```

**描述**

清理OHNativeWindow中的OHNativeWindowBuffer缓存。

使用该接口清理缓存前，需确保已通过[OH\_NativeWindow\_NativeWindowRequestBuffer](capi-external-window-h.md#oh_nativewindow_nativewindowrequestbuffer)接口成功申请OHNativeWindowBuffer。

本接口为非线程安全类型接口。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeWindow

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OHNativeWindow](capi-nativewindow-nativewindow.md) \*window | 一个指向[OHNativeWindow](capi-nativewindow-nativewindow.md)的结构体实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回值为0表示执行成功，其他返回值可参考[OHNativeErrorCode](capi-graphic-error-code-h.md#ohnativeerrorcode)。 |

### OH\_NativeWindow\_PreAllocBuffers()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_NativeWindow_PreAllocBuffers(OHNativeWindow *window, uint32_t allocBufferCnt)
```

**描述**

通过OHNativeWindow对象提前申请多块OHNativeWindowBuffer，用以内容生产。

在调用本接口前，需要通过[OH\_NativeWindow\_NativeWindowHandleOpt](capi-external-window-h.md#oh_nativewindow_nativewindowhandleopt)对OHNativeWindow设置宽高。

本接口为非线程安全类型接口。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeWindow

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OHNativeWindow](capi-nativewindow-nativewindow.md) \*window | 一个指向OHNativeWindow的结构体实例的指针。 |
| uint32\_t allocBufferCnt | 提前申请buffer的数量。当allocBufferCnt大于bufferQueueSize时，只能提前申请bufferQueueSize数量的buffer。bufferQueueSize可以通过[OH\_NativeWindow\_NativeWindowHandleOpt](capi-external-window-h.md#oh_nativewindow_nativewindowhandleopt)获取。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回值为0表示执行成功，其他返回值可参考[OHNativeErrorCode](capi-graphic-error-code-h.md#ohnativeerrorcode)。 |

### OH\_NativeWindow\_LockBuffer()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_NativeWindow_LockBuffer(OHNativeWindow* window, Region region, OHNativeWindowBuffer** buffer)
```

**描述**

通过OHNativeWindow对象申请一块OHNativeWindowBuffer，用以内容生产，并对该OHNativeWindowBuffer加锁。

本接口需要和[OH\_NativeWindow\_UnlockAndFlushBuffer](capi-external-window-h.md#oh_nativewindow_unlockandflushbuffer)接口配合使用。

本接口对OHNativeWindowBuffer加锁后，需要调[OH\_NativeWindow\_UnlockAndFlushBuffer](capi-external-window-h.md#oh_nativewindow_unlockandflushbuffer)接口解锁后才能重新对OHNativeWindowBuffer加锁。

若用本接口重复对OHNativeWindowBuffer加锁，会返回操作非法错误码。

本接口支持通过CPU上的内存读写直接渲染图像。

本接口为非线程安全类型接口。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeWindow

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OHNativeWindow](capi-nativewindow-nativewindow.md)\* window | 一个指向OHNativeWindow的结构体实例的指针。 |
| [Region](capi-nativewindow-region.md) region | 一个Region结构体，表示一块脏区域，该区域有内容更新。 |
| [OHNativeWindowBuffer](capi-nativewindow-nativewindowbuffer.md)\*\* buffer | 一个指向OHNativeWindowBuffer的二级指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 执行成功时返回NATIVE\_ERROR\_OK。  window或buffer是空指针时返回NATIVE\_ERROR\_INVALID\_ARGUMENTS。  window的surface成员是空指针时返回NATIVE\_ERROR\_UNKNOWN。  其他返回值可参考[OHNativeErrorCode](capi-graphic-error-code-h.md#ohnativeerrorcode)。 |

### OH\_NativeWindow\_UnlockAndFlushBuffer()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_NativeWindow_UnlockAndFlushBuffer(OHNativeWindow* window)
```

**描述**

通过OHNativeWindow将生产好内容的OHNativeWindowBuffer放回到Buffer队列中，用以内容消费，并对OHNativeWindowBuffer解锁。

本接口需要和[OH\_NativeWindow\_LockBuffer](capi-external-window-h.md#oh_nativewindow_lockbuffer)接口配合使用。

若用本接口重复对OHNativeWindowBuffer解锁，会返回操作非法错误码。

本接口为非线程安全类型接口。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeWindow

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OHNativeWindow](capi-nativewindow-nativewindow.md)\* window | 一个指向OHNativeWindow的结构体实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 执行成功时返回NATIVE\_ERROR\_OK。  window是空指针时返回NATIVE\_ERROR\_INVALID\_ARGUMENTS。  window的surface成员是空指针时返回NATIVE\_ERROR\_UNKNOWN。  其他返回值可参考[OHNativeErrorCode](capi-graphic-error-code-h.md#ohnativeerrorcode)。 |
