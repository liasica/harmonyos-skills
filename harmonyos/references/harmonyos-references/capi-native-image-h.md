---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-image-h
title: native_image.h
breadcrumb: API参考 > 图形 > ArkGraphics 2D（方舟2D图形服务） > C API > 头文件 > native_image.h
category: harmonyos-references
scraped_at: 2026-04-28T08:15:06+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:2cb99b57502c2ad000e43d1bd7febaf84452a8c5842c4ac722f96426c0a403ce
---

## 概述

PhonePC/2in1TabletTVWearable

定义获取和使用NativeImage的相关函数。

**引用文件：** <native\_image/native\_image.h>

**库：** libnative\_image.so

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeImage

**起始版本：** 9

**相关模块：** [OH\_NativeImage](capi-oh-nativeimage.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 结构体

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [OH\_OnFrameAvailableListener](capi-oh-nativeimage-oh-onframeavailablelistener.md) | OH\_OnFrameAvailableListener | 一个OH\_NativeImage的监听者，通过[OH\_NativeImage\_SetOnFrameAvailableListener](capi-native-image-h.md#oh_nativeimage_setonframeavailablelistener)接口注册该监听结构体，当有buffer可获取时，将触发回调给用户。 |
| [OH\_NativeImage](capi-oh-nativeimage-oh-nativeimage.md) | OH\_NativeImage | 提供OH\_NativeImage结构体声明。 |
| [NativeWindow](capi-nativewindow-nativewindow.md) | OHNativeWindow | 提供对NativeWindow的访问功能。 |
| [NativeWindowBuffer](capi-nativewindow-nativewindowbuffer.md) | OHNativeWindowBuffer | 提供NativeWindowBuffer结构体声明。 |

### 函数

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [typedef void (\*OH\_OnFrameAvailable)(void \*context)](capi-native-image-h.md#oh_onframeavailable) | OH\_OnFrameAvailable | 有buffer可获取时触发的回调函数。 |
| [OH\_NativeImage\* OH\_NativeImage\_Create(uint32\_t textureId, uint32\_t textureTarget)](capi-native-image-h.md#oh_nativeimage_create) | - | 创建一个OH\_NativeImage实例，该实例与OpenGL ES的纹理ID和纹理目标相关联。  本接口需要与[OH\_NativeImage\_Destroy](capi-native-image-h.md#oh_nativeimage_destroy)接口配合使用，否则会存在内存泄露。  本接口为非线程安全类型接口。 |
| [OHNativeWindow\* OH\_NativeImage\_AcquireNativeWindow(OH\_NativeImage\* image)](capi-native-image-h.md#oh_nativeimage_acquirenativewindow) | - | 获取与OH\_NativeImage相关联的OHNativeWindow指针。  本接口为非线程安全类型接口。  本接口获取到的OHNativeWindow无需额外释放，执行[OH\_NativeImage\_Destroy](capi-native-image-h.md#oh_nativeimage_destroy)会将对应的OHNativeWindow引用计数减一。当执行[OH\_NativeImage\_Destroy](capi-native-image-h.md#oh_nativeimage_destroy)时，请将本接口获取到的OHNativeWindow指针置空，防止后续产生野指针。 |
| [int32\_t OH\_NativeImage\_AttachContext(OH\_NativeImage\* image, uint32\_t textureId)](capi-native-image-h.md#oh_nativeimage_attachcontext) | - | 将OH\_NativeImage实例附加到当前OpenGL ES上下文，且该OpenGL ES纹理会绑定到GL\_TEXTURE\_EXTERNAL\_OES, 并通过OH\_NativeImage进行更新。  本接口为非线程安全类型接口。 |
| [int32\_t OH\_NativeImage\_DetachContext(OH\_NativeImage\* image)](capi-native-image-h.md#oh_nativeimage_detachcontext) | - | 将OH\_NativeImage实例从当前OpenGL ES上下文分离。  本接口为非线程安全类型接口。 |
| [int32\_t OH\_NativeImage\_UpdateSurfaceImage(OH\_NativeImage\* image)](capi-native-image-h.md#oh_nativeimage_updatesurfaceimage) | - | 通过OH\_NativeImage获取最新帧更新相关联的OpenGL ES纹理。  本接口需要在OpenGL ES环境上下文的线程中调用。  本接口需要在接收到[OH\_OnFrameAvailableListener](capi-oh-nativeimage-oh-onframeavailablelistener.md)回调后调用。  本接口为非线程安全类型接口。 |
| [int64\_t OH\_NativeImage\_GetTimestamp(OH\_NativeImage\* image)](capi-native-image-h.md#oh_nativeimage_gettimestamp) | - | 获取最近调用OH\_NativeImage\_UpdateSurfaceImage的纹理图像的相关时间戳。  本接口为非线程安全类型接口。 |
| [int32\_t OH\_NativeImage\_GetTransformMatrix(OH\_NativeImage\* image, float matrix[16])](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-image-h#oh_nativeimage_gettransformmatrix) | - | 获取最近调用OH\_NativeImage\_UpdateSurfaceImage的纹理图像的变化矩阵。 |
| [int32\_t OH\_NativeImage\_GetSurfaceId(OH\_NativeImage\* image, uint64\_t\* surfaceId)](capi-native-image-h.md#oh_nativeimage_getsurfaceid) | - | 获取OH\_NativeImage的surface编号。  本接口为非线程安全类型接口。 |
| [int32\_t OH\_NativeImage\_SetOnFrameAvailableListener(OH\_NativeImage\* image, OH\_OnFrameAvailableListener listener)](capi-native-image-h.md#oh_nativeimage_setonframeavailablelistener) | - | 设置帧可用回调。  不允许在回调函数中调用本模块的其他接口。  本接口为非线程安全类型接口。 |
| [int32\_t OH\_NativeImage\_UnsetOnFrameAvailableListener(OH\_NativeImage\* image)](capi-native-image-h.md#oh_nativeimage_unsetonframeavailablelistener) | - | 取消设置帧可用回调。  本接口为非线程安全类型接口。 |
| [void OH\_NativeImage\_Destroy(OH\_NativeImage\*\* image)](capi-native-image-h.md#oh_nativeimage_destroy) | - | 销毁通过OH\_NativeImage\_Create创建的OH\_NativeImage实例，销毁后该OH\_NativeImage指针会被赋值为空。  并将对应OHNativeWindow引用计数减一。  本接口为非线程安全类型接口。 |
| [int32\_t OH\_NativeImage\_GetTransformMatrixV2(OH\_NativeImage\* image, float matrix[16])](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-image-h#oh_nativeimage_gettransformmatrixv2) | - | 根据生产端设置的旋转角度，获取最近调用OH\_NativeImage\_UpdateSurfaceImage的纹理图像的变化矩阵。  matrix在[OH\_NativeImage\_UpdateSurfaceImage](capi-native-image-h.md#oh_nativeimage_updatesurfaceimage)接口调用后，才会更新。  本接口为非线程安全类型接口。 |
| [int32\_t OH\_NativeImage\_GetBufferMatrix(OH\_NativeImage\* image, float matrix[16])](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-image-h#oh_nativeimage_getbuffermatrix) | - | 获取根据生产端设置的旋转角度和buffer实际有效内容区域计算出的变换矩阵。  本接口返回一个变换矩阵，该矩阵是[OH\_NativeImage](capi-oh-nativeimage-oh-nativeimage.md)在消费buffer，即调用[OH\_NativeImage\_UpdateSurfaceImage](capi-native-image-h.md#oh_nativeimage_updatesurfaceimage)或者[OH\_NativeImage\_AcquireNativeWindowBuffer](capi-native-image-h.md#oh_nativeimage_acquirenativewindowbuffer)时，根据buffer的旋转角度和实际有效内容区域计算所得。  本接口为非线程安全类型接口。 |
| [int32\_t OH\_NativeImage\_AcquireNativeWindowBuffer(OH\_NativeImage\* image,OHNativeWindowBuffer\*\* nativeWindowBuffer, int\* fenceFd)](capi-native-image-h.md#oh_nativeimage_acquirenativewindowbuffer) | - | 通过消费端的OH\_NativeImage获取一个OHNativeWindowBuffer。  本接口不能与[OH\_NativeImage\_UpdateSurfaceImage](capi-native-image-h.md#oh_nativeimage_updatesurfaceimage)接口同时使用。  本接口将会创建一个OHNativeWindowBuffer。  当使用OHNativeWindowBuffer时，用户需要通过[OH\_NativeWindow\_NativeObjectReference](capi-external-window-h.md#oh_nativewindow_nativeobjectreference)接口将其引用计数加一。  当OHNativeWindowBuffer使用完，用户需要通过[OH\_NativeWindow\_NativeObjectUnreference](capi-external-window-h.md#oh_nativewindow_nativeobjectunreference)接口将其引用计数减一。  本接口需要和[OH\_NativeImage\_ReleaseNativeWindowBuffer](capi-native-image-h.md#oh_nativeimage_releasenativewindowbuffer)接口配合使用，否则会存在内存泄露。  当fenceFd使用完，用户需要将其close。  本接口为非线程安全类型接口。 |
| [int32\_t OH\_NativeImage\_ReleaseNativeWindowBuffer(OH\_NativeImage\* image,OHNativeWindowBuffer\* nativeWindowBuffer, int fenceFd)](capi-native-image-h.md#oh_nativeimage_releasenativewindowbuffer) | - | 通过OH\_NativeImage实例将OHNativeWindowBuffer归还到buffer队列中。  系统会将fenceFd关闭，无需用户close。  当接口返回失败时，需要额外执行一次[OH\_NativeWindow\_NativeObjectUnreference](capi-external-window-h.md#oh_nativewindow_nativeobjectunreference)对buffer引用计数减一，否则会存在内存泄露。  本接口为非线程安全类型接口。 |
| [OH\_NativeImage\* OH\_ConsumerSurface\_Create(void)](capi-native-image-h.md#oh_consumersurface_create) | - | 创建一个OH\_NativeImage实例，作为surface的消费端。  本接口仅用于surface消费端的内存轮转，创建的OH\_NativeImage内部不会主动进行内存渲染处理。  本接口不能与[OH\_NativeImage\_UpdateSurfaceImage](capi-native-image-h.md#oh_nativeimage_updatesurfaceimage)接口同时使用。  本接口与[OH\_NativeImage\_AcquireNativeWindowBuffer](capi-native-image-h.md#oh_nativeimage_acquirenativewindowbuffer)和[OH\_NativeImage\_ReleaseNativeWindowBuffer](capi-native-image-h.md#oh_nativeimage_releasenativewindowbuffer)配合使用。  本接口需要和[OH\_NativeImage\_Destroy](capi-native-image-h.md#oh_nativeimage_destroy)接口配合使用，否则会存在内存泄露。  本接口为非线程安全类型接口。 |
| [int32\_t OH\_ConsumerSurface\_SetDefaultUsage(OH\_NativeImage\* image, uint64\_t usage)](capi-native-image-h.md#oh_consumersurface_setdefaultusage) | - | 设置默认读写方式。  本接口为非线程安全类型接口。 |
| [int32\_t OH\_ConsumerSurface\_SetDefaultSize(OH\_NativeImage\* image, int32\_t width, int32\_t height)](capi-native-image-h.md#oh_consumersurface_setdefaultsize) | - | 设置几何图形默认尺寸。  本接口为非线程安全类型接口。 |
| [int32\_t OH\_NativeImage\_SetDropBufferMode(OH\_NativeImage\* image, bool isOpen)](capi-native-image-h.md#oh_nativeimage_setdropbuffermode) | - | 设置OH\_NativeImage是否为渲染丢帧模式。  处于此模式时，大部分生产端生产的buffer将会被丢弃，最新的buffer会及时上屏渲染。  此模式不能同时保证帧率高的要求。  此接口建议在[OH\_NativeImage\_Create](capi-native-image-h.md#oh_nativeimage_create)接口调用后立即调用。  此接口在与[OH\_NativeImage\_UpdateSurfaceImage](capi-native-image-h.md#oh_nativeimage_updatesurfaceimage)接口一起使用的场景下才会生效。  本接口为非线程安全类型接口。 |
| [OH\_NativeImage\* OH\_NativeImage\_CreateWithSingleBufferMode(uint32\_t textureId, uint32\_t textureTarget, bool singleBufferMode)](capi-native-image-h.md#oh_nativeimage_createwithsinglebuffermode) | - | 使用纹理ID创建一个OH\_NativeImage实例，该实例与OpenGL ES的纹理ID和纹理目标相关联，并选择是否设置单buffer模式。  本接口需要与[OH\_NativeImage\_Destroy](capi-native-image-h.md#oh_nativeimage_destroy)接口配合使用，否则会存在内存泄露。  本接口为非线程安全类型接口。 |
| [OH\_NativeImage\* OH\_ConsumerSurface\_CreateWithSingleBufferMode(bool singleBufferMode)](capi-native-image-h.md#oh_consumersurface_createwithsinglebuffermode) | - | 不使用纹理ID创建一个[OH\_NativeImage](capi-oh-nativeimage-oh-nativeimage.md)实例，作为surface的消费端，并选择是否设置单buffer模式。  本接口仅用于surface消费端的内存轮转，创建的[OH\_NativeImage](capi-oh-nativeimage-oh-nativeimage.md)内部不会主动进行内存渲染处理。  本接口不能与[OH\_NativeImage\_UpdateSurfaceImage](capi-native-image-h.md#oh_nativeimage_updatesurfaceimage)接口同时使用。  本接口需要和[OH\_NativeImage\_Destroy](capi-native-image-h.md#oh_nativeimage_destroy)接口配合使用，否则会存在内存泄露。  本接口为非线程安全类型接口。 |
| [int32\_t OH\_NativeImage\_ReleaseTextImage(OH\_NativeImage\* image)](capi-native-image-h.md#oh_nativeimage_releasetextimage) | - | 解除SurfaceBuffer与纹理的绑定，将纹理恢复到未使用状态。  单buffer模式下，需要调用该接口释放纹理，否则生产者下次无法申请buffer。  本接口为非线程安全类型接口。 |
| [int32\_t OH\_NativeImage\_GetColorSpace(OH\_NativeImage\* image, OH\_NativeBuffer\_ColorSpace\* colorSpace)](capi-native-image-h.md#oh_nativeimage_getcolorspace) | - | 获取最近调用[OH\_NativeImage\_UpdateSurfaceImage](capi-native-image-h.md#oh_nativeimage_updatesurfaceimage)的纹理图像的相关色彩空间。  本接口为非线程安全类型接口。 |
| [int32\_t OH\_NativeImage\_AcquireLatestNativeWindowBuffer(OH\_NativeImage\* image, OHNativeWindowBuffer\*\* nativeWindowBuffer, int\* fenceFd)](capi-native-image-h.md#oh_nativeimage_acquirelatestnativewindowbuffer) | - | 通过消费端的OH\_NativeImage获取一个生产者最近生产的OHNativeWindowBuffer，并将其余buffer丢弃。  消费端可以通过[OH\_OnFrameAvailableListener](capi-oh-nativeimage-oh-onframeavailablelistener.md)注册的回调，收到所有可用buffer（包括被丢弃的buffer)的回调。  本接口不能与[OH\_NativeImage\_UpdateSurfaceImage](capi-native-image-h.md#oh_nativeimage_updatesurfaceimage)接口同时使用。  本接口为非线程安全类型接口。 |
| [int32\_t OH\_NativeImage\_IsReleased(OH\_NativeImage\* image, bool\* isReleased)](capi-native-image-h.md#oh_nativeimage_isreleased) | - | 查询与[OH\_NativeImage](capi-oh-nativeimage-oh-nativeimage.md)关联的纹理是否已释放。  本接口为非线程安全类型接口。 |
| [int32\_t OH\_NativeImage\_Release(OH\_NativeImage\* image)](capi-native-image-h.md#oh_nativeimage_release) | - | 清除所有[OHNativeWindow](capi-nativewindow-nativewindow.md)的OHNativeWindowBuffer缓存，并将[OH\_NativeImage](capi-oh-nativeimage-oh-nativeimage.md)从OpenGL ES上下文中分离。  本接口为非线程安全类型接口。 |

## 函数说明

PhonePC/2in1TabletTVWearable

### OH\_OnFrameAvailable()

PhonePC/2in1TabletTVWearable

```
1. typedef void (*OH_OnFrameAvailable)(void *context)
```

**描述**

有buffer可获取时触发的回调函数。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeImage

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| void \*context | 用户自定义的上下文信息，会在回调触发时返回给用户。 |

### OH\_NativeImage\_Create()

PhonePC/2in1TabletTVWearable

```
1. OH_NativeImage* OH_NativeImage_Create(uint32_t textureId, uint32_t textureTarget)
```

**描述**

创建一个OH\_NativeImage实例，该实例与OpenGL ES的纹理ID和纹理目标相关联。

本接口需要与[OH\_NativeImage\_Destroy](capi-native-image-h.md#oh_nativeimage_destroy)接口配合使用，否则会存在内存泄露。

本接口为非线程安全类型接口。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeImage

**起始版本：** 9

**参数：**

| 参数项 | 描述 |
| --- | --- |
| uint32\_t textureId | OpenGL ES的纹理ID，OH\_NativeImage实例会与之相关联。 |
| uint32\_t textureTarget | OpenGL ES的纹理目标，取值范围为GL\_TEXTURE\_2D和GL\_TEXTURE\_EXTERNAL\_OES，具体可见[选择纹理类型](../harmonyos-faqs/faqs-arkgraphics-2d-12.md)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| OH\_NativeImage\* | 创建成功则返回一个指向OH\_NativeImage实例的指针，否则返回NULL。 |

### OH\_NativeImage\_AcquireNativeWindow()

PhonePC/2in1TabletTVWearable

```
1. OHNativeWindow* OH_NativeImage_AcquireNativeWindow(OH_NativeImage* image)
```

**描述**

获取与OH\_NativeImage相关联的OHNativeWindow指针。

本接口为非线程安全类型接口。

本接口获取到的OHNativeWindow无需额外释放，执行[OH\_NativeImage\_Destroy](capi-native-image-h.md#oh_nativeimage_destroy)会将对应的OHNativeWindow引用计数减一。当执行[OH\_NativeImage\_Destroy](capi-native-image-h.md#oh_nativeimage_destroy)时，请将本接口获取到的OHNativeWindow指针置空，防止后续产生野指针。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeImage

**起始版本：** 9

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_NativeImage](capi-oh-nativeimage-oh-nativeimage.md)\* image | 指向OH\_NativeImage实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OHNativeWindow](capi-nativewindow-nativewindow.md)\* | 成功则返回一个指向OHNativeWindow实例的指针，否则返回NULL。 |

### OH\_NativeImage\_AttachContext()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_NativeImage_AttachContext(OH_NativeImage* image, uint32_t textureId)
```

**描述**

将OH\_NativeImage实例附加到当前OpenGL ES上下文，且该OpenGL ES纹理会绑定到GL\_TEXTURE\_EXTERNAL\_OES, 并通过OH\_NativeImage进行更新。

本接口为非线程安全类型接口。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeImage

**起始版本：** 9

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_NativeImage](capi-oh-nativeimage-oh-nativeimage.md)\* image | 指向OH\_NativeImage实例的指针。 |
| uint32\_t textureId | 是OH\_NativeImage要附加到的OpenGL ES纹理的id。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回值为0表示执行成功，其他返回值可参考[OHNativeErrorCode](capi-graphic-error-code-h.md#ohnativeerrorcode)。 |

### OH\_NativeImage\_DetachContext()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_NativeImage_DetachContext(OH_NativeImage* image)
```

**描述**

将OH\_NativeImage实例从当前OpenGL ES上下文分离。

本接口为非线程安全类型接口。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeImage

**起始版本：** 9

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_NativeImage](capi-oh-nativeimage-oh-nativeimage.md)\* image | 指向OH\_NativeImage实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回值为0表示执行成功，其他返回值可参考[OHNativeErrorCode](capi-graphic-error-code-h.md#ohnativeerrorcode)。 |

### OH\_NativeImage\_UpdateSurfaceImage()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_NativeImage_UpdateSurfaceImage(OH_NativeImage* image)
```

**描述**

通过OH\_NativeImage获取最新帧更新相关联的OpenGL ES纹理。

本接口需要在OpenGL ES环境上下文的线程中调用。

本接口需要在接收到[OH\_OnFrameAvailableListener](capi-oh-nativeimage-oh-onframeavailablelistener.md)回调后调用。

本接口为非线程安全类型接口。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeImage

**起始版本：** 9

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_NativeImage](capi-oh-nativeimage-oh-nativeimage.md)\* image | 指向OH\_NativeImage实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回值为0表示执行成功，其他返回值可参考[OHNativeErrorCode](capi-graphic-error-code-h.md#ohnativeerrorcode)。 |

### OH\_NativeImage\_GetTimestamp()

PhonePC/2in1TabletTVWearable

```
1. int64_t OH_NativeImage_GetTimestamp(OH_NativeImage* image)
```

**描述**

获取最近调用OH\_NativeImage\_UpdateSurfaceImage的纹理图像的相关时间戳。

本接口为非线程安全类型接口。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeImage

**起始版本：** 9

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_NativeImage](capi-oh-nativeimage-oh-nativeimage.md)\* image | 指向OH\_NativeImage实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int64\_t | 返回纹理图像的相关时间戳。 |

### OH\_NativeImage\_GetTransformMatrix()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_NativeImage_GetTransformMatrix(OH_NativeImage* image, float matrix[16])
```

**描述**

获取最近调用OH\_NativeImage\_UpdateSurfaceImage的纹理图像的变化矩阵。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeImage

**起始版本：** 9

**废弃版本：** 从API version 12开始废弃。

**替代接口：** [OH\_NativeImage\_GetTransformMatrixV2](capi-native-image-h.md#oh_nativeimage_gettransformmatrixv2)

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_NativeImage](capi-oh-nativeimage-oh-nativeimage.md)\* image | 指向OH\_NativeImage实例的指针。 |
| matrix | 用来存储要获取的4\*4的变化矩阵。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回值为0表示执行成功，其他返回值可参考[OHNativeErrorCode](capi-graphic-error-code-h.md#ohnativeerrorcode)。 |

### OH\_NativeImage\_GetSurfaceId()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_NativeImage_GetSurfaceId(OH_NativeImage* image, uint64_t* surfaceId)
```

**描述**

获取OH\_NativeImage的surface编号。

本接口为非线程安全类型接口。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeImage

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_NativeImage](capi-oh-nativeimage-oh-nativeimage.md)\* image | 指向OH\_NativeImage实例的指针。 |
| uint64\_t\* surfaceId | 是指向surface编号的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回值为0表示执行成功，其他返回值可参考[OHNativeErrorCode](capi-graphic-error-code-h.md#ohnativeerrorcode)。 |

### OH\_NativeImage\_SetOnFrameAvailableListener()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_NativeImage_SetOnFrameAvailableListener(OH_NativeImage* image, OH_OnFrameAvailableListener listener)
```

**描述**

设置帧可用回调。

不允许在回调函数中调用本模块的其他接口。

本接口为非线程安全类型接口。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeImage

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_NativeImage](capi-oh-nativeimage-oh-nativeimage.md)\* image | 指向OH\_NativeImage实例的指针。 |
| [OH\_OnFrameAvailableListener](capi-oh-nativeimage-oh-onframeavailablelistener.md) listener | 表示回调监听者。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回值为0表示执行成功，其他返回值可参考[OHNativeErrorCode](capi-graphic-error-code-h.md#ohnativeerrorcode)。 |

### OH\_NativeImage\_UnsetOnFrameAvailableListener()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_NativeImage_UnsetOnFrameAvailableListener(OH_NativeImage* image)
```

**描述**

取消设置帧可用回调。

本接口为非线程安全类型接口。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeImage

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_NativeImage](capi-oh-nativeimage-oh-nativeimage.md)\* image | 指向OH\_NativeImage实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回值为0表示执行成功，其他返回值可参考[OHNativeErrorCode](capi-graphic-error-code-h.md#ohnativeerrorcode)。 |

### OH\_NativeImage\_Destroy()

PhonePC/2in1TabletTVWearable

```
1. void OH_NativeImage_Destroy(OH_NativeImage** image)
```

**描述**

销毁通过OH\_NativeImage\_Create创建的OH\_NativeImage实例, 销毁后该OH\_NativeImage指针会被赋值为空。

并将对应OHNativeWindow引用计数减一。

本接口为非线程安全类型接口。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeImage

**起始版本：** 9

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_NativeImage](capi-oh-nativeimage-oh-nativeimage.md)\*\* image | 指向OH\_NativeImage实例的指针。 |

### OH\_NativeImage\_GetTransformMatrixV2()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_NativeImage_GetTransformMatrixV2(OH_NativeImage* image, float matrix[16])
```

**描述**

根据生产端设置的旋转角度，获取最近调用OH\_NativeImage\_UpdateSurfaceImage的纹理图像的变化矩阵。

matrix在[OH\_NativeImage\_UpdateSurfaceImage](capi-native-image-h.md#oh_nativeimage_updatesurfaceimage)接口调用后，才会更新。

本接口为非线程安全类型接口。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeImage

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_NativeImage](capi-oh-nativeimage-oh-nativeimage.md)\* image | 指向OH\_NativeImage实例的指针。 |
| matrix | 用来存储要获取的4\*4的变化矩阵。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回接口执行结果。NATIVE\_ERROR\_OK，表示接口执行成功。  返回NATIVE\_ERROR\_INVALID\_ARGUMENTS，对应错误码为40001000，表示image参数为空。  返回NATIVE\_ERROR\_UNKNOWN，对应错误码为50002000，表示未知错误，请查看日志。 |

### OH\_NativeImage\_GetBufferMatrix()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_NativeImage_GetBufferMatrix(OH_NativeImage* image, float matrix[16])
```

**描述**

获取根据生产端设置的旋转角度和buffer实际有效内容区域计算出的变换矩阵。

本接口返回一个变换矩阵，该矩阵是[OH\_NativeImage](capi-oh-nativeimage-oh-nativeimage.md)在消费buffer，即调用[OH\_NativeImage\_UpdateSurfaceImage](capi-native-image-h.md#oh_nativeimage_updatesurfaceimage)或者[OH\_NativeImage\_AcquireNativeWindowBuffer](capi-native-image-h.md#oh_nativeimage_acquirenativewindowbuffer)时，根据buffer的旋转角度和实际有效内容区域计算所得。

本接口为非线程安全类型接口。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeImage

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_NativeImage](capi-oh-nativeimage-oh-nativeimage.md)\* image | 指向[OH\_NativeImage](capi-oh-nativeimage-oh-nativeimage.md)实例的指针。 |
| matrix | 用于存储获取的4\*4变换矩阵。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回接口执行结果。NATIVE\_ERROR\_OK，表示接口执行成功。  返回NATIVE\_ERROR\_INVALID\_ARGUMENTS，对应错误码为40001000，表示image参数为空。  返回NATIVE\_ERROR\_MEM\_OPERATION\_ERROR，对应错误码为30001000，表示内存操作错误，获取变换矩阵失败。 |

### OH\_NativeImage\_AcquireNativeWindowBuffer()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_NativeImage_AcquireNativeWindowBuffer(OH_NativeImage* image,OHNativeWindowBuffer** nativeWindowBuffer, int* fenceFd)
```

**描述**

通过消费端的OH\_NativeImage获取一个OHNativeWindowBuffer。本接口不能与[OH\_NativeImage\_UpdateSurfaceImage](capi-native-image-h.md#oh_nativeimage_updatesurfaceimage)接口同时使用。

本接口将会创建一个OHNativeWindowBuffer。当使用OHNativeWindowBuffer时，用户需要通过[OH\_NativeWindow\_NativeObjectReference](capi-external-window-h.md#oh_nativewindow_nativeobjectreference)接口将其引用计数加一。当OHNativeWindowBuffer使用完，用户需要通过[OH\_NativeWindow\_NativeObjectUnreference](capi-external-window-h.md#oh_nativewindow_nativeobjectunreference)接口将其引用计数减一。

本接口需要和[OH\_NativeImage\_ReleaseNativeWindowBuffer](capi-native-image-h.md#oh_nativeimage_releasenativewindowbuffer)接口配合使用，否则会存在内存泄露。

当fenceFd使用完，用户需要将其close。

本接口为非线程安全类型接口。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeImage

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_NativeImage](capi-oh-nativeimage-oh-nativeimage.md)\* image | 指向OH\_NativeImage实例的指针。 |
| [OHNativeWindowBuffer](capi-nativewindow-nativewindowbuffer.md)\*\* nativeWindowBuffer | 指向OHNativeWindowBuffer指针的指针。 |
| int\* fenceFd | 指向文件描述符句柄的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 执行成功时返回NATIVE\_ERROR\_OK。  image, nativeWindowBuffer, fenceFd是空指针时返回NATIVE\_ERROR\_INVALID\_ARGUMENTS。  没有buffer可以消费时返回NATIVE\_ERROR\_NO\_BUFFER。 |

### OH\_NativeImage\_ReleaseNativeWindowBuffer()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_NativeImage_ReleaseNativeWindowBuffer(OH_NativeImage* image,OHNativeWindowBuffer* nativeWindowBuffer, int fenceFd)
```

**描述**

通过OH\_NativeImage实例将OHNativeWindowBuffer归还到buffer队列中。

系统会将fenceFd关闭，无需用户close。

当接口返回失败时，需要额外执行一次[OH\_NativeWindow\_NativeObjectUnreference](capi-external-window-h.md#oh_nativewindow_nativeobjectunreference)对buffer引用计数减一，否则会存在内存泄露。

本接口为非线程安全类型接口。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeImage

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_NativeImage](capi-oh-nativeimage-oh-nativeimage.md)\* image | 指向OH\_NativeImage实例的指针。 |
| [OHNativeWindowBuffer](capi-nativewindow-nativewindowbuffer.md)\* nativeWindowBuffer | 指向OHNativeWindowBuffer实例的指针。 |
| int fenceFd | 指向文件描述符句柄, 用于并发同步控制。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 执行成功时返回NATIVE\_ERROR\_OK。  image, nativeWindowBuffer是空指针时返回NATIVE\_ERROR\_INVALID\_ARGUMENTS。  nativeWindowBuffer为状态非法时返回NATIVE\_ERROR\_BUFFER\_STATE\_INVALID。  nativeWindowBuffer不在缓存中返回NATIVE\_ERROR\_BUFFER\_NOT\_IN\_CACHE。 |

### OH\_ConsumerSurface\_Create()

PhonePC/2in1TabletTVWearable

```
1. OH_NativeImage* OH_ConsumerSurface_Create(void)
```

**描述**

创建一个OH\_NativeImage实例，作为surface的消费端。

本接口仅用于surface消费端的内存轮转，创建的OH\_NativeImage内部不会主动进行内存渲染处理。

本接口不能与[OH\_NativeImage\_UpdateSurfaceImage](capi-native-image-h.md#oh_nativeimage_updatesurfaceimage)接口同时使用。

本接口与[OH\_NativeImage\_AcquireNativeWindowBuffer](capi-native-image-h.md#oh_nativeimage_acquirenativewindowbuffer)和[OH\_NativeImage\_ReleaseNativeWindowBuffer](capi-native-image-h.md#oh_nativeimage_releasenativewindowbuffer)配合使用。

本接口需要和[OH\_NativeImage\_Destroy](capi-native-image-h.md#oh_nativeimage_destroy)接口配合使用，否则会存在内存泄露。

本接口为非线程安全类型接口。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeImage

**起始版本：** 12

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_NativeImage](capi-oh-nativeimage-oh-nativeimage.md)\* | 成功则返回一个指向OH\_NativeImage实例的指针，否则返回NULL。 |

### OH\_ConsumerSurface\_SetDefaultUsage()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ConsumerSurface_SetDefaultUsage(OH_NativeImage* image, uint64_t usage)
```

**描述**

设置默认读写方式。

本接口为非线程安全类型接口。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeImage

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_NativeImage](capi-oh-nativeimage-oh-nativeimage.md)\* image | 指向OH\_NativeImage实例的指针。 |
| uint64\_t usage | 表示读写方式。枚举值参考[OH\_NativeBuffer\_Usage](capi-native-buffer-h.md#oh_nativebuffer_usage)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 执行成功时返回NATIVE\_ERROR\_OK。  image是空指针时返回NATIVE\_ERROR\_INVALID\_ARGUMENTS。 |

### OH\_ConsumerSurface\_SetDefaultSize()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ConsumerSurface_SetDefaultSize(OH_NativeImage* image, int32_t width, int32_t height)
```

**描述**

设置几何图形默认尺寸。

本接口为非线程安全类型接口。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeImage

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_NativeImage](capi-oh-nativeimage-oh-nativeimage.md)\* image | 指向OH\_NativeImage实例的指针。 |
| int32\_t width | 表示几何图形宽度，取值范围大于0，单位为像素。 |
| int32\_t height | 表示几何图形高度，取值范围大于0，单位为像素。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 执行成功时返回NATIVE\_ERROR\_OK。  image是空指针时，或width、height小于等于0时返回NATIVE\_ERROR\_INVALID\_ARGUMENTS。 |

### OH\_NativeImage\_SetDropBufferMode()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_NativeImage_SetDropBufferMode(OH_NativeImage* image, bool isOpen)
```

**描述**

设置OH\_NativeImage是否为渲染丢帧模式。

处于此模式时，大部分生产端生产的buffer将会被丢弃，最新的buffer会及时上屏渲染。

此模式不能同时保证帧率高的要求。

此接口建议在[OH\_NativeImage\_Create](capi-native-image-h.md#oh_nativeimage_create)接口调用后立即调用。

此接口在与[OH\_NativeImage\_UpdateSurfaceImage](capi-native-image-h.md#oh_nativeimage_updatesurfaceimage)接口一起使用的场景下才会生效。

本接口为非线程安全类型接口。

通过[OH\_NativeImage\_SetOnFrameAvailableListener](capi-native-image-h.md#oh_nativeimage_setonframeavailablelistener)设置的listener回调不会因为设置了丢帧模式而减少。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeImage

**起始版本：** 17

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_NativeImage](capi-oh-nativeimage-oh-nativeimage.md)\* image | 指向OH\_NativeImage实例的指针。 |
| bool isOpen | 是否设置渲染丢帧。true表示设置为渲染丢帧模式，false表示不设置。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 执行成功时返回NATIVE\_ERROR\_OK。  image是空指针时返回NATIVE\_ERROR\_INVALID\_ARGUMENTS。 |

### OH\_NativeImage\_CreateWithSingleBufferMode()

PhonePC/2in1TabletTVWearable

```
1. OH_NativeImage* OH_NativeImage_CreateWithSingleBufferMode(uint32_t textureId, uint32_t textureTarget, bool singleBufferMode)
```

**描述**

使用纹理ID创建一个OH\_NativeImage实例，该实例与OpenGL ES的纹理ID和纹理目标相关联，并选择是否设置单buffer模式。

本接口需要与[OH\_NativeImage\_Destroy](capi-native-image-h.md#oh_nativeimage_destroy)接口配合使用，否则会存在内存泄露。

本接口为非线程安全类型接口。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeImage

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| uint32\_t textureId | OpenGL ES的纹理ID，OH\_NativeImage实例会与之相关联。 |
| uint32\_t textureTarget | OpenGL ES的纹理目标，具体可见[选择纹理类型](../harmonyos-faqs/faqs-arkgraphics-2d-12.md)。 |
| bool singleBufferMode | 是否设置单buffer模式。true表示设置为单buffer模式，false表示不设置。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_NativeImage\*](capi-oh-nativeimage-oh-nativeimage.md) | 创建成功则返回一个指向OH\_NativeImage实例的指针，否则返回NULL。 |

### OH\_ConsumerSurface\_CreateWithSingleBufferMode()

PhonePC/2in1TabletTVWearable

```
1. OH_NativeImage* OH_ConsumerSurface_CreateWithSingleBufferMode(bool singleBufferMode)
```

**描述**

不使用纹理ID创建一个[OH\_NativeImage](capi-oh-nativeimage-oh-nativeimage.md)实例，作为surface的消费端，并选择是否设置单buffer模式。

本接口仅用于surface消费端的内存轮转，创建的[OH\_NativeImage](capi-oh-nativeimage-oh-nativeimage.md)内部不会主动进行内存渲染处理。

本接口不能与[OH\_NativeImage\_UpdateSurfaceImage](capi-native-image-h.md#oh_nativeimage_updatesurfaceimage)接口同时使用。

本接口需要和[OH\_NativeImage\_Destroy](capi-native-image-h.md#oh_nativeimage_destroy)接口配合使用，否则会存在内存泄露。

本接口为非线程安全类型接口。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeImage

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| bool singleBufferMode | 是否设置单buffer模式。true表示设置为单buffer模式，false表示不设置。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_NativeImage\*](capi-oh-nativeimage-oh-nativeimage.md) | 成功则返回一个指向[OH\_NativeImage](capi-oh-nativeimage-oh-nativeimage.md)实例的指针，否则返回NULL。 |

### OH\_NativeImage\_ReleaseTextImage()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_NativeImage_ReleaseTextImage(OH_NativeImage* image)
```

**描述**

解除SurfaceBuffer与纹理的绑定，将纹理恢复到未使用状态。

单buffer模式下，需要调用该接口释放纹理，否则生产者下次无法申请buffer。

本接口为非线程安全类型接口。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeImage

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_NativeImage](capi-oh-nativeimage-oh-nativeimage.md)\* image | 指向[OH\_NativeImage](capi-oh-nativeimage-oh-nativeimage.md)实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 执行成功时返回NATIVE\_ERROR\_OK。  image是空指针时返回NATIVE\_ERROR\_INVALID\_ARGUMENTS。  其他返回值可参考[OHNativeErrorCode](capi-graphic-error-code-h.md#ohnativeerrorcode)。 |

### OH\_NativeImage\_GetColorSpace()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_NativeImage_GetColorSpace(OH_NativeImage* image, OH_NativeBuffer_ColorSpace* colorSpace)
```

**描述**

获取最近调用[OH\_NativeImage\_UpdateSurfaceImage](capi-native-image-h.md#oh_nativeimage_updatesurfaceimage)的纹理图像的相关色彩空间。

本接口为非线程安全类型接口。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeImage

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_NativeImage](capi-oh-nativeimage-oh-nativeimage.md)\* image | 指向[OH\_NativeImage](capi-oh-nativeimage-oh-nativeimage.md)实例的指针。 |
| OH\_NativeBuffer\_ColorSpace\* colorSpace | 为[OH\_NativeImage](capi-oh-nativeimage-oh-nativeimage.md)设置的颜色空间，其值从[OH\_NativeBuffer\_ColorSpace](capi-buffer-common-h.md#oh_nativebuffer_colorspace)获取。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 执行成功时返回NATIVE\_ERROR\_OK。  image，colorSpace是空指针时返回NATIVE\_ERROR\_INVALID\_ARGUMENTS。  其他返回值可参考[OHNativeErrorCode](capi-graphic-error-code-h.md#ohnativeerrorcode)。 |

### OH\_NativeImage\_AcquireLatestNativeWindowBuffer()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_NativeImage_AcquireLatestNativeWindowBuffer(OH_NativeImage* image, OHNativeWindowBuffer** nativeWindowBuffer, int* fenceFd)
```

**描述**

通过消费端的OH\_NativeImage获取一个生产者最近生产的OHNativeWindowBuffer，并将其余buffer丢弃。

消费端可以通过[OH\_OnFrameAvailableListener](capi-oh-nativeimage-oh-onframeavailablelistener.md)注册的回调，收到所有可用buffer（包括被丢弃的buffer)的回调。

本接口不能与[OH\_NativeImage\_UpdateSurfaceImage](capi-native-image-h.md#oh_nativeimage_updatesurfaceimage)接口同时使用。

本接口将会创建一个OHNativeWindowBuffer。当使用OHNativeWindowBuffer时，用户需要通过[OH\_NativeWindow\_NativeObjectReference](capi-external-window-h.md#oh_nativewindow_nativeobjectreference)接口将其引用计数加一。

当OHNativeWindowBuffer使用完，用户需要通过[OH\_NativeWindow\_NativeObjectUnreference](capi-external-window-h.md#oh_nativewindow_nativeobjectunreference)接口将其引用计数减一。

本接口需要和[OH\_NativeImage\_ReleaseNativeWindowBuffer](capi-native-image-h.md#oh_nativeimage_releasenativewindowbuffer)接口配合使用，否则会存在内存泄露。

当fenceFd使用完，用户需要将其close。

本接口为非线程安全类型接口。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeImage

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_NativeImage](capi-oh-nativeimage-oh-nativeimage.md)\* image | 指向OH\_NativeImage实例的指针。 |
| [OHNativeWindowBuffer](capi-nativewindow-nativewindowbuffer.md)\*\* nativeWindowBuffer | 指向OHNativeWindowBuffer的二级指针。 |
| int\* fenceFd | 指向文件描述符句柄的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 执行成功时返回NATIVE\_ERROR\_OK。  image，nativeWindowBuffer或fenceFd是空指针时返回NATIVE\_ERROR\_INVALID\_ARGUMENTS。  没有buffer可以消费时返回NATIVE\_ERROR\_NO\_BUFFER。  其他返回值可参考[OHNativeErrorCode](capi-graphic-error-code-h.md#ohnativeerrorcode)。 |

### OH\_NativeImage\_IsReleased()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_NativeImage_IsReleased(OH_NativeImage* image, bool* isReleased)
```

**描述**

查询与[OH\_NativeImage](capi-oh-nativeimage-oh-nativeimage.md)关联的纹理是否已释放。

本接口为非线程安全类型接口。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeImage

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_NativeImage](capi-oh-nativeimage-oh-nativeimage.md)\* image | 指向OH\_NativeImage实例的指针。 |
| bool\* isReleased | 纹理是否已释放。true表示纹理已释放，false表示纹理未释放，作为出参使用。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 执行成功时返回NATIVE\_ERROR\_OK。  image或isReleased为空指针时返回NATIVE\_ERROR\_INVALID\_ARGUMENTS。  其他返回值可参考[OHNativeErrorCode](capi-graphic-error-code-h.md#ohnativeerrorcode)。 |

### OH\_NativeImage\_Release()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_NativeImage_Release(OH_NativeImage* image)
```

**描述**

清除所有[OHNativeWindow](capi-nativewindow-nativewindow.md)的OHNativeWindowBuffer缓存，并将[OH\_NativeImage](capi-oh-nativeimage-oh-nativeimage.md)从OpenGL ES上下文中分离。

本接口为非线程安全类型接口。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeImage

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_NativeImage](capi-oh-nativeimage-oh-nativeimage.md)\* image | 指向OH\_NativeImage实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 执行成功时返回NATIVE\_ERROR\_OK。  image为空指针时返回NATIVE\_ERROR\_INVALID\_ARGUMENTS。  其他返回值可参考[OHNativeErrorCode](capi-graphic-error-code-h.md#ohnativeerrorcode)。 |
