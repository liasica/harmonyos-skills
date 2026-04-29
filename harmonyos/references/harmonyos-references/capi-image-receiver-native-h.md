---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-receiver-native-h
title: image_receiver_native.h
breadcrumb: API参考 > 媒体 > Image Kit（图片处理服务） > C API > 头文件 > image_receiver_native.h
category: harmonyos-references
scraped_at: 2026-04-29T14:03:54+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:52f5fbe1f474e820c763bbc0fd2e6d77aeefb1345d253de9fff6a7052e91f69f
---

## 概述

PhonePC/2in1TabletTVWearable

声明从native层获取图片数据的方法。

**引用文件：** <multimedia/image\_framework/image/image\_receiver\_native.h>

**库：** libimage\_receiver.so

**系统能力：** SystemCapability.Multimedia.Image.ImageReceiver

**起始版本：** 12

**相关模块：** [Image\_NativeModule](capi-image-nativemodule.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 结构体

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [OH\_ImageReceiverNative](capi-image-nativemodule-oh-imagereceivernative.md) | OH\_ImageReceiverNative | OH\_ImageReceiverNative是native层封装的图片接收器结构体，OH\_ImageReceiverNative结构体不可直接操作，而是采用函数调用方式创建、释放结构体以及操作具体字段。 |
| [OH\_ImageReceiverOptions](capi-image-nativemodule-oh-imagereceiveroptions.md) | OH\_ImageReceiverOptions | 用于定义OH\_ImageReceiverOptions数据类型名称。 |

### 函数

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [typedef void (\*OH\_ImageReceiver\_OnCallback)(OH\_ImageReceiverNative \*receiver)](capi-image-receiver-native-h.md#oh_imagereceiver_oncallback) | OH\_ImageReceiver\_OnCallback | 定义native层图片的回调方法。 |
| [typedef void (\*OH\_ImageReceiver\_ImageArriveCallback)(OH\_ImageReceiverNative \*receiver, void \*userData)](capi-image-receiver-native-h.md#oh_imagereceiver_imagearrivecallback) | OH\_ImageReceiver\_ImageArriveCallback | ImageArrive事件的回调方法。 |
| [Image\_ErrorCode OH\_ImageReceiverOptions\_Create(OH\_ImageReceiverOptions \*\*options)](capi-image-receiver-native-h.md#oh_imagereceiveroptions_create) | - | 创建应用层OH\_ImageReceiverOptions对象。 |
| [Image\_ErrorCode OH\_ImageReceiverOptions\_GetSize(OH\_ImageReceiverOptions\* options, Image\_Size\* size)](capi-image-receiver-native-h.md#oh_imagereceiveroptions_getsize) | - | 获取OH\_ImageReceiverOptions对象的Image\_Size。 |
| [Image\_ErrorCode OH\_ImageReceiverOptions\_SetSize(OH\_ImageReceiverOptions\* options, Image\_Size size)](capi-image-receiver-native-h.md#oh_imagereceiveroptions_setsize) | - | 设置OH\_ImageReceiverOptions对象的Image\_Size。 |
| [Image\_ErrorCode OH\_ImageReceiverOptions\_GetCapacity(OH\_ImageReceiverOptions\* options, int32\_t\* capacity)](capi-image-receiver-native-h.md#oh_imagereceiveroptions_getcapacity) | - | 获取OH\_ImageReceiverOptions对象的图片缓存容量。 |
| [Image\_ErrorCode OH\_ImageReceiverOptions\_SetCapacity(OH\_ImageReceiverOptions\* options, int32\_t capacity)](capi-image-receiver-native-h.md#oh_imagereceiveroptions_setcapacity) | - | 设置OH\_ImageReceiverOptions对象的图片缓存容量。 |
| [Image\_ErrorCode OH\_ImageReceiverOptions\_Release(OH\_ImageReceiverOptions\* options)](capi-image-receiver-native-h.md#oh_imagereceiveroptions_release) | - | 释放OH\_ImageReceiverOptions对象。 |
| [Image\_ErrorCode OH\_ImageReceiverNative\_Create(OH\_ImageReceiverOptions\* options, OH\_ImageReceiverNative\*\* receiver)](capi-image-receiver-native-h.md#oh_imagereceivernative_create) | - | 创建应用层OH\_ImageReceiverNative对象。 |
| [Image\_ErrorCode OH\_ImageReceiverNative\_GetReceivingSurfaceId(OH\_ImageReceiverNative\* receiver, uint64\_t\* surfaceId)](capi-image-receiver-native-h.md#oh_imagereceivernative_getreceivingsurfaceid) | - | 通过OH\_ImageReceiverNative获取SurfaceId。 |
| [Image\_ErrorCode OH\_ImageReceiverNative\_ReadLatestImage(OH\_ImageReceiverNative\* receiver, OH\_ImageNative\*\* image)](capi-image-receiver-native-h.md#oh_imagereceivernative_readlatestimage) | - | 通过OH\_ImageReceiverNative获取最新的一张图片。 |
| [Image\_ErrorCode OH\_ImageReceiverNative\_ReadNextImage(OH\_ImageReceiverNative\* receiver, OH\_ImageNative\*\* image)](capi-image-receiver-native-h.md#oh_imagereceivernative_readnextimage) | - | 通过OH\_ImageReceiverNative获取下一张图片。 |
| [Image\_ErrorCode OH\_ImageReceiverNative\_On(OH\_ImageReceiverNative\* receiver, OH\_ImageReceiver\_OnCallback callback)](capi-image-receiver-native-h.md#oh_imagereceivernative_on) | - | 注册一个[OH\_ImageReceiver\_OnCallback](capi-image-receiver-native-h.md#oh_imagereceiver_oncallback)回调事件。  每当接收到新的图片，该回调事件就会响应。 |
| [Image\_ErrorCode OH\_ImageReceiverNative\_Off(OH\_ImageReceiverNative\* receiver)](capi-image-receiver-native-h.md#oh_imagereceivernative_off) | - | 关闭[OH\_ImageReceiver\_OnCallback](capi-image-receiver-native-h.md#oh_imagereceiver_oncallback)回调事件。  关闭被[OH\_ImageReceiverNative\_On](capi-image-receiver-native-h.md#oh_imagereceivernative_on)开启的回调事件。 |
| [Image\_ErrorCode OH\_ImageReceiverNative\_GetSize(OH\_ImageReceiverNative\* receiver, Image\_Size\* size)](capi-image-receiver-native-h.md#oh_imagereceivernative_getsize) | - | 通过OH\_ImageReceiverNative获取ImageReceiver的大小。 |
| [Image\_ErrorCode OH\_ImageReceiverNative\_GetCapacity(OH\_ImageReceiverNative\* receiver, int32\_t\* capacity)](capi-image-receiver-native-h.md#oh_imagereceivernative_getcapacity) | - | 通过OH\_ImageReceiverNative获取ImageReceiver的容量。 |
| [Image\_ErrorCode OH\_ImageReceiverNative\_Release(OH\_ImageReceiverNative\* receiver)](capi-image-receiver-native-h.md#oh_imagereceivernative_release) | - | 释放Native OH\_ImageReceiverNative对象。 |
| [Image\_ErrorCode OH\_ImageReceiverNative\_OnImageArrive(OH\_ImageReceiverNative \*receiver, OH\_ImageReceiver\_ImageArriveCallback callback, void \*userData)](capi-image-receiver-native-h.md#oh_imagereceivernative_onimagearrive) | - | 注册[OH\_ImageReceiver\_ImageArriveCallback](capi-image-receiver-native-h.md#oh_imagereceiver_imagearrivecallback)回调。 |
| [Image\_ErrorCode OH\_ImageReceiverNative\_OffImageArrive(OH\_ImageReceiverNative \*receiver, OH\_ImageReceiver\_ImageArriveCallback callback)](capi-image-receiver-native-h.md#oh_imagereceivernative_offimagearrive) | - | 注销[OH\_ImageReceiver\_ImageArriveCallback](capi-image-receiver-native-h.md#oh_imagereceiver_imagearrivecallback)回调。 |

## 函数说明

PhonePC/2in1TabletTVWearable

### OH\_ImageReceiver\_OnCallback()

PhonePC/2in1TabletTVWearable

```
1. typedef void (*OH_ImageReceiver_OnCallback)(OH_ImageReceiverNative *receiver)
```

**描述**

定义native层图片的回调方法。

**起始版本：** 12

### OH\_ImageReceiver\_ImageArriveCallback()

PhonePC/2in1TabletTVWearable

```
1. typedef void (*OH_ImageReceiver_ImageArriveCallback)(OH_ImageReceiverNative *receiver, void *userData)
```

**描述**

ImageArrive事件的回调方法。

**起始版本：** 20

### OH\_ImageReceiverOptions\_Create()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_ImageReceiverOptions_Create(OH_ImageReceiverOptions **options)
```

**描述**

创建应用层OH\_ImageReceiverOptions对象。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ImageReceiverOptions](capi-image-nativemodule-oh-imagereceiveroptions.md) \*\*options | 表示作为获取结果的 OH\_ImageReceiverOptions对象的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。  IMAGE\_ALLOC\_FAILED：申请内存失败。 |

### OH\_ImageReceiverOptions\_GetSize()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_ImageReceiverOptions_GetSize(OH_ImageReceiverOptions* options, Image_Size* size)
```

**描述**

获取OH\_ImageReceiverOptions对象的Image\_Size。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ImageReceiverOptions](capi-image-nativemodule-oh-imagereceiveroptions.md)\* options | 表示OH\_ImageReceiverOptions对象的指针。 |
| [Image\_Size](capi-image-nativemodule-image-size.md)\* size | 表示作为获取结果的Image\_Size对象的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。 |

### OH\_ImageReceiverOptions\_SetSize()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_ImageReceiverOptions_SetSize(OH_ImageReceiverOptions* options, Image_Size size)
```

**描述**

设置OH\_ImageReceiverOptions对象的Image\_Size。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ImageReceiverOptions](capi-image-nativemodule-oh-imagereceiveroptions.md)\* options | 表示OH\_ImageReceiverOptions对象的指针。 |
| [Image\_Size](capi-image-nativemodule-image-size.md) size | 表示Image\_Size对象的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。 |

### OH\_ImageReceiverOptions\_GetCapacity()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_ImageReceiverOptions_GetCapacity(OH_ImageReceiverOptions* options, int32_t* capacity)
```

**描述**

获取OH\_ImageReceiverOptions对象的图片缓存容量。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ImageReceiverOptions](capi-image-nativemodule-oh-imagereceiveroptions.md)\* options | 表示OH\_ImageReceiverOptions对象的指针。 |
| int32\_t\* capacity | 表示作为获取结果的图片缓存容量对象的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。 |

### OH\_ImageReceiverOptions\_SetCapacity()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_ImageReceiverOptions_SetCapacity(OH_ImageReceiverOptions* options, int32_t capacity)
```

**描述**

设置OH\_ImageReceiverOptions对象的图片缓存容量。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ImageReceiverOptions](capi-image-nativemodule-oh-imagereceiveroptions.md)\* options | 表示OH\_ImageReceiverOptions对象的指针。 |
| int32\_t capacity | 表示图片缓存容量值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。 |

### OH\_ImageReceiverOptions\_Release()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_ImageReceiverOptions_Release(OH_ImageReceiverOptions* options)
```

**描述**

释放OH\_ImageReceiverOptions对象。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ImageReceiverOptions](capi-image-nativemodule-oh-imagereceiveroptions.md)\* options | 表示OH\_ImageReceiverOptions对象的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。 |

### OH\_ImageReceiverNative\_Create()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_ImageReceiverNative_Create(OH_ImageReceiverOptions* options, OH_ImageReceiverNative** receiver)
```

**描述**

创建应用层OH\_ImageReceiverNative对象。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ImageReceiverOptions](capi-image-nativemodule-oh-imagereceiveroptions.md)\* options | 表示OH\_ImageReceiverOptions对象的指针。 |
| [OH\_ImageReceiverNative](capi-image-nativemodule-oh-imagereceivernative.md)\*\* receiver | 表示作为获取结果的OH\_ImageReceiverNative对象的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。  IMAGE\_ALLOC\_FAILED：申请内存失败。 |

### OH\_ImageReceiverNative\_GetReceivingSurfaceId()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_ImageReceiverNative_GetReceivingSurfaceId(OH_ImageReceiverNative* receiver, uint64_t* surfaceId)
```

**描述**

通过OH\_ImageReceiverNative获取SurfaceId。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ImageReceiverNative](capi-image-nativemodule-oh-imagereceivernative.md)\* receiver | 表示OH\_ImageReceiverNative对象的指针。 |
| uint64\_t\* surfaceId | 表示作为获取结果的id对象的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。  IMAGE\_UNKNOWN\_ERROR：未知原因错误。 |

### OH\_ImageReceiverNative\_ReadLatestImage()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_ImageReceiverNative_ReadLatestImage(OH_ImageReceiverNative* receiver, OH_ImageNative** image)
```

**描述**

通过OH\_ImageReceiverNative获取最新的一张图片。

说明

* 此接口需要在[OH\_ImageReceiver\_OnCallback](capi-image-receiver-native-h.md#oh_imagereceiver_oncallback)回调后调用，才能正常的接收到数据。
* 此接口返回的OH\_ImageNative使用完毕后需要调用[OH\_ImageNative\_Release](capi-image-native-h.md#oh_imagenative_release)方法释放，释放后才可以继续接收新的数据。
* 此接口需加锁保证使用过程中OH\_ImageReceiverNative对象未被释放，具体使用方法可参考开发指南[使用imagereceiver完成图片接收](../harmonyos-guides/image-receiver-c.md)。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ImageReceiverNative](capi-image-nativemodule-oh-imagereceivernative.md)\* receiver | 表示OH\_ImageReceiverNative对象的指针。 |
| [OH\_ImageNative](capi-image-nativemodule-oh-imagenative.md)\*\* image | 获取到的应用层的OH\_ImageNative指针对象。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。  IMAGE\_UNKNOWN\_ERROR：未知原因错误。  IMAGE\_ALLOC\_FAILED：申请内存失败。 |

### OH\_ImageReceiverNative\_ReadNextImage()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_ImageReceiverNative_ReadNextImage(OH_ImageReceiverNative* receiver, OH_ImageNative** image)
```

**描述**

通过OH\_ImageReceiverNative获取下一张图片。

说明

* 此接口需要在[OH\_ImageReceiver\_OnCallback](capi-image-receiver-native-h.md#oh_imagereceiver_oncallback)回调后调用，才能正常的接收到数据。
* 此接口返回的OH\_ImageNative使用完毕后需要调用[OH\_ImageNative\_Release](capi-image-native-h.md#oh_imagenative_release)方法释放，释放后才可以继续接收新的数据。
* 此接口需加锁保证使用过程中OH\_ImageReceiverNative对象未被释放，具体使用方法可参考开发指南[使用imagereceiver完成图片接收](../harmonyos-guides/image-receiver-c.md)。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ImageReceiverNative](capi-image-nativemodule-oh-imagereceivernative.md)\* receiver | 表示OH\_ImageReceiverNative对象的指针。 |
| [OH\_ImageNative](capi-image-nativemodule-oh-imagenative.md)\*\* image | 获取到的应用层的OH\_ImageNative指针对象。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。  IMAGE\_UNKNOWN\_ERROR：未知原因错误。  IMAGE\_ALLOC\_FAILED：申请内存失败。 |

### OH\_ImageReceiverNative\_On()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_ImageReceiverNative_On(OH_ImageReceiverNative* receiver, OH_ImageReceiver_OnCallback callback)
```

**描述**

注册一个[OH\_ImageReceiver\_OnCallback](capi-image-receiver-native-h.md#oh_imagereceiver_oncallback)回调事件。

每当接收到新的图片，该回调事件就会响应。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ImageReceiverNative](capi-image-nativemodule-oh-imagereceivernative.md)\* receiver | 表示OH\_ImageReceiverNative对象的指针。 |
| [OH\_ImageReceiver\_OnCallback](capi-image-receiver-native-h.md#oh_imagereceiver_oncallback) callback | 表示OH\_ImageReceiver\_OnCallback事件的回调函数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。 |

### OH\_ImageReceiverNative\_Off()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_ImageReceiverNative_Off(OH_ImageReceiverNative* receiver)
```

**描述**

关闭[OH\_ImageReceiver\_OnCallback](capi-image-receiver-native-h.md#oh_imagereceiver_oncallback)回调事件。

关闭被[OH\_ImageReceiverNative\_On](capi-image-receiver-native-h.md#oh_imagereceivernative_on)开启的回调事件。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ImageReceiverNative](capi-image-nativemodule-oh-imagereceivernative.md)\* receiver | 表示OH\_ImageReceiverNative对象的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。 |

### OH\_ImageReceiverNative\_GetSize()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_ImageReceiverNative_GetSize(OH_ImageReceiverNative* receiver, Image_Size* size)
```

**描述**

通过OH\_ImageReceiverNative获取ImageReceiver的大小。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ImageReceiverNative](capi-image-nativemodule-oh-imagereceivernative.md)\* receiver | 表示OH\_ImageReceiverNative对象的指针。 |
| [Image\_Size](capi-image-nativemodule-image-size.md)\* size | 表示作为获取结果的Image\_Size对象的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。 |

### OH\_ImageReceiverNative\_GetCapacity()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_ImageReceiverNative_GetCapacity(OH_ImageReceiverNative* receiver, int32_t* capacity)
```

**描述**

通过OH\_ImageReceiverNative获取ImageReceiver的容量。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ImageReceiverNative](capi-image-nativemodule-oh-imagereceivernative.md)\* receiver | 表示OH\_ImageReceiverNative对象的指针。 |
| int32\_t\* capacity | 表示作为获取结果的图片缓存容量对象的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。 |

### OH\_ImageReceiverNative\_Release()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_ImageReceiverNative_Release(OH_ImageReceiverNative* receiver)
```

**描述**

释放Native OH\_ImageReceiverNative对象。

说明

此接口需加锁保证释放后OH\_ImageReceiverNative对象不被其他接口使用，具体使用方法可参考开发指南[使用imagereceiver完成图片接收](../harmonyos-guides/image-receiver-c.md)。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ImageReceiverNative](capi-image-nativemodule-oh-imagereceivernative.md)\* receiver | 表示OH\_ImageReceiverNative对象的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。 |

### OH\_ImageReceiverNative\_OnImageArrive()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_ImageReceiverNative_OnImageArrive(OH_ImageReceiverNative *receiver,OH_ImageReceiver_ImageArriveCallback callback, void *userData)
```

**描述**

注册[OH\_ImageReceiver\_ImageArriveCallback](capi-image-receiver-native-h.md#oh_imagereceiver_imagearrivecallback)回调。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ImageReceiverNative](capi-image-nativemodule-oh-imagereceivernative.md) \*receiver | 处理回调的OH\_ImageReceiverNative对象。 |
| [OH\_ImageReceiver\_ImageArriveCallback](capi-image-receiver-native-h.md#oh_imagereceiver_imagearrivecallback) callback | 要注册的OH\_ImageReceiver\_ImageArriveCallback回调方法。 |
| void \*userData | 用户自定义数据指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：操作成功。  IMAGE\_RECEIVER\_INVALID\_PARAMETER：参数错误。 |

### OH\_ImageReceiverNative\_OffImageArrive()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_ImageReceiverNative_OffImageArrive(OH_ImageReceiverNative *receiver,OH_ImageReceiver_ImageArriveCallback callback)
```

**描述**

注销[OH\_ImageReceiver\_ImageArriveCallback](capi-image-receiver-native-h.md#oh_imagereceiver_imagearrivecallback)回调。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ImageReceiverNative](capi-image-nativemodule-oh-imagereceivernative.md) \*receiver | 处理回调的OH\_ImageReceiverNative对象。 |
| [OH\_ImageReceiver\_ImageArriveCallback](capi-image-receiver-native-h.md#oh_imagereceiver_imagearrivecallback) callback | 要注册的OH\_ImageReceiver\_ImageArriveCallback回调。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：操作成功。  IMAGE\_RECEIVER\_INVALID\_PARAMETER：参数错误，receiver或callback未注册。 |
