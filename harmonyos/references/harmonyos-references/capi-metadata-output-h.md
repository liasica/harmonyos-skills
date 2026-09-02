---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-metadata-output-h
title: metadata_output.h
breadcrumb: API参考 > 媒体 > Camera Kit（相机服务） > C API > 头文件 > metadata_output.h
category: harmonyos-references
scraped_at: 2026-09-02T15:02:28+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:3a742eca2947c58dbafca56c1decbd0035f11b93d96b9c5cc9ae9f94f45c7e0e
---

## 概述

声明元数据输出概念。

**引用文件：** <ohcamera/metadata\_output.h>

**库：** libohcamera.so

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 11

**相关模块：** [OH\_Camera](capi-oh-camera.md)

## 汇总

### 结构体

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [MetadataOutput\_Callbacks](capi-oh-camera-metadataoutput-callbacks.md) | MetadataOutput\_Callbacks | 元数据输出的回调。 |
| [Camera\_MetadataOutput](capi-oh-camera-camera-metadataoutput.md) | Camera\_MetadataOutput | 元数据输出对象。  可以使用[OH\_CameraManager\_CreateMetadataOutput](capi-camera-manager-h.md#oh_cameramanager_createmetadataoutput)方法创建指针。 |

### 函数

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [typedef void (\*OH\_MetadataOutput\_OnMetadataObjectAvailable)(Camera\_MetadataOutput\* metadataOutput, Camera\_MetadataObject\* metadataObject, uint32\_t size)](capi-metadata-output-h.md#oh_metadataoutput_onmetadataobjectavailable) | OH\_MetadataOutput\_OnMetadataObjectAvailable | 在[MetadataOutput\_Callbacks](capi-oh-camera-metadataoutput-callbacks.md)中被调用的元数据输出元数据对象可用回调。 |
| [typedef void (\*OH\_MetadataOutput\_OnError)(Camera\_MetadataOutput\* metadataOutput, Camera\_ErrorCode errorCode)](capi-metadata-output-h.md#oh_metadataoutput_onerror) | OH\_MetadataOutput\_OnError | 在[MetadataOutput\_Callbacks](capi-oh-camera-metadataoutput-callbacks.md)中被调用的元数据输出错误回调。 |
| [Camera\_ErrorCode OH\_MetadataOutput\_RegisterCallback(Camera\_MetadataOutput\* metadataOutput, MetadataOutput\_Callbacks\* callback)](capi-metadata-output-h.md#oh_metadataoutput_registercallback) | - | 注册元数据输出更改事件回调。 |
| [Camera\_ErrorCode OH\_MetadataOutput\_UnregisterCallback(Camera\_MetadataOutput\* metadataOutput, MetadataOutput\_Callbacks\* callback)](capi-metadata-output-h.md#oh_metadataoutput_unregistercallback) | - | 注销元数据输出更改事件回调。 |
| [Camera\_ErrorCode OH\_MetadataOutput\_Start(Camera\_MetadataOutput\* metadataOutput)](capi-metadata-output-h.md#oh_metadataoutput_start) | - | 启动元数据输出。 |
| [Camera\_ErrorCode OH\_MetadataOutput\_Stop(Camera\_MetadataOutput\* metadataOutput)](capi-metadata-output-h.md#oh_metadataoutput_stop) | - | 停止元数据输出。 |
| [Camera\_ErrorCode OH\_MetadataOutput\_Release(Camera\_MetadataOutput\* metadataOutput)](capi-metadata-output-h.md#oh_metadataoutput_release) | - | 释放元数据输出实例。 |
| [Camera\_ErrorCode OH\_MetadataOutput\_AddMetadataObjectTypes(Camera\_MetadataOutput\* metadataOutput, Camera\_MetadataObjectType\* types, uint32\_t size)](capi-metadata-output-h.md#oh_metadataoutput_addmetadataobjecttypes) | - | 添加元数据对象类型。 |
| [Camera\_ErrorCode OH\_MetadataOutput\_RemoveMetadataObjectTypes(Camera\_MetadataOutput\* metadataOutput, Camera\_MetadataObjectType\* types, uint32\_t size)](capi-metadata-output-h.md#oh_metadataoutput_removemetadataobjecttypes) | - | 移除元数据对象类型。 |
| [typedef void (\*OH\_MetadataOutput\_OnMetadataObjectExtAvailable)(void\* context, OH\_Camera\_MetadataObjectExt\*\* metadataObjectExt, uint32\_t size)](capi-metadata-output-h.md#oh_metadataoutput_onmetadataobjectextavailable) | OH\_MetadataOutput\_OnMetadataObjectExtAvailable | 用于监听元数据对象上报事件的回调。使用[OH\_MetadataOutput\_RegisterMetadataObjectExtAvailableCallback](capi-metadata-output-h.md#oh_metadataoutput_registermetadataobjectextavailablecallback)进行注册。 |
| [typedef void (\*OH\_MetadataOutput\_OnErrorExt)(void\* context, Camera\_ErrorCode errorCode)](capi-metadata-output-h.md#oh_metadataoutput_onerrorext) | OH\_MetadataOutput\_OnErrorExt | 在元数据输出期间，用于监听错误事件的回调。 |
| [Camera\_ErrorCode OH\_MetadataOutput\_RegisterMetadataObjectExtAvailableCallback(Camera\_MetadataOutput\* metadataOutput, void\* context, OH\_MetadataOutput\_OnMetadataObjectExtAvailable callback)](capi-metadata-output-h.md#oh_metadataoutput_registermetadataobjectextavailablecallback) | - | 注册监听元数据对象上报事件的回调。该回调可通过[OH\_MetadataOutput\_UnregisterMetadataObjectExtAvailableCallback](capi-metadata-output-h.md#oh_metadataoutput_unregistermetadataobjectextavailablecallback)注销。 |
| [Camera\_ErrorCode OH\_MetadataOutput\_UnregisterMetadataObjectExtAvailableCallback(Camera\_MetadataOutput\* metadataOutput, void\* context, OH\_MetadataOutput\_OnMetadataObjectExtAvailable callback)](capi-metadata-output-h.md#oh_metadataoutput_unregistermetadataobjectextavailablecallback) | - | 注销监听元数据对象上报事件的回调。 |
| [Camera\_ErrorCode OH\_MetadataOutput\_RegisterErrorExtCallback(Camera\_MetadataOutput\* metadataOutput, void\* context, OH\_MetadataOutput\_OnErrorExt callback)](capi-metadata-output-h.md#oh_metadataoutput_registererrorextcallback) | - | 注册监听错误事件的回调。该回调可通过[OH\_MetadataOutput\_UnregisterErrorExtCallback](capi-metadata-output-h.md#oh_metadataoutput_unregistererrorextcallback)注销。 |
| [Camera\_ErrorCode OH\_MetadataOutput\_UnregisterErrorExtCallback(Camera\_MetadataOutput\* metadataOutput, void\* context, OH\_MetadataOutput\_OnErrorExt callback)](capi-metadata-output-h.md#oh_metadataoutput_unregistererrorextcallback) | - | 注销监听错误事件的回调。 |
| [bool OH\_MetadataOutput\_IsLockMetadataObjectTrackingSupported(const Camera\_MetadataOutput\* metadataOutput)](capi-metadata-output-h.md#oh_metadataoutput_islockmetadataobjecttrackingsupported) | - | 检查设备是否支持锁定元数据对象（如猫脸、狗脸）追踪功能。 |
| [Camera\_ErrorCode OH\_MetadataOutput\_LockMetadataObjectTracking(Camera\_MetadataOutput\* metadataOutput, Camera\_Point\* pointOfInterest)](capi-metadata-output-h.md#oh_metadataoutput_lockmetadataobjecttracking) | - | 锁定对特定元数据对象（如猫脸、狗脸）的追踪。  该功能以pointOfInterest所指向的点所在的对象为追踪对象，如果该点不存在追踪对象，则功能不生效。  被锁定追踪的对象离开取景范围超过三秒或调用解锁追踪后，锁定追踪自动取消。 |
| [Camera\_ErrorCode OH\_MetadataOutput\_UnlockMetadataObjectTracking(Camera\_MetadataOutput\* metadataOutput)](capi-metadata-output-h.md#oh_metadataoutput_unlockmetadataobjecttracking) | - | 解锁元数据对象（如猫脸、狗脸）的追踪。 |

## 函数说明

### OH\_MetadataOutput\_OnMetadataObjectAvailable()

```c
typedef void (*OH_MetadataOutput_OnMetadataObjectAvailable)(Camera_MetadataOutput* metadataOutput, Camera_MetadataObject* metadataObject, uint32_t size)
```

**描述**

在[MetadataOutput\_Callbacks](capi-oh-camera-metadataoutput-callbacks.md)中被调用的元数据输出元数据对象可用回调。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_MetadataOutput](capi-oh-camera-camera-metadataoutput.md)\* metadataOutput | 传递回调的元数据输出实例。 |
| [Camera\_MetadataObject](capi-oh-camera-camera-metadataobject.md)\* metadataObject | 回调传递的元数据实例信息。 |
| uint32\_t size | 元数据对象的大小。 |

### OH\_MetadataOutput\_OnError()

```c
typedef void (*OH_MetadataOutput_OnError)(Camera_MetadataOutput* metadataOutput, Camera_ErrorCode errorCode)
```

**描述**

在[MetadataOutput\_Callbacks](capi-oh-camera-metadataoutput-callbacks.md)中被调用的元数据输出错误回调。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_MetadataOutput](capi-oh-camera-camera-metadataoutput.md)\* metadataOutput | 传递回调的元数据输出实例。 |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) errorCode | 元数据输出的错误码。 |

**参考：**

[CAMERA\_SERVICE\_FATAL\_ERROR](capi-camera-h.md#camera_errorcode)

### OH\_MetadataOutput\_RegisterCallback()

```c
Camera_ErrorCode OH_MetadataOutput_RegisterCallback(Camera_MetadataOutput* metadataOutput, MetadataOutput_Callbacks* callback)
```

**描述**

注册元数据输出更改事件回调。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_MetadataOutput](capi-oh-camera-camera-metadataoutput.md)\* metadataOutput | 元数据输出实例。 |
| [MetadataOutput\_Callbacks](capi-oh-camera-metadataoutput-callbacks.md)\* callback | 要注册的元数据输出回调。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。 |

### OH\_MetadataOutput\_UnregisterCallback()

```c
Camera_ErrorCode OH_MetadataOutput_UnregisterCallback(Camera_MetadataOutput* metadataOutput, MetadataOutput_Callbacks* callback)
```

**描述**

注销元数据输出更改事件回调。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_MetadataOutput](capi-oh-camera-camera-metadataoutput.md)\* metadataOutput | 元数据输出实例。 |
| [MetadataOutput\_Callbacks](capi-oh-camera-metadataoutput-callbacks.md)\* callback | 要注销的元数据输出回调。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。 |

### OH\_MetadataOutput\_Start()

```c
Camera_ErrorCode OH_MetadataOutput_Start(Camera_MetadataOutput* metadataOutput)
```

**描述**

启动元数据输出。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_MetadataOutput](capi-oh-camera-camera-metadataoutput.md)\* metadataOutput | 要启动的元数据输出实例。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。  CAMERA\_SESSION\_NOT\_CONFIG：捕获会话未配置。  CAMERA\_SERVICE\_FATAL\_ERROR：相机服务异常。 |

### OH\_MetadataOutput\_Stop()

```c
Camera_ErrorCode OH_MetadataOutput_Stop(Camera_MetadataOutput* metadataOutput)
```

**描述**

停止元数据输出。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_MetadataOutput](capi-oh-camera-camera-metadataoutput.md)\* metadataOutput | 要停止的元数据输出实例。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。  CAMERA\_SERVICE\_FATAL\_ERROR：相机服务异常。 |

### OH\_MetadataOutput\_Release()

```c
Camera_ErrorCode OH_MetadataOutput_Release(Camera_MetadataOutput* metadataOutput)
```

**描述**

释放元数据输出实例。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_MetadataOutput](capi-oh-camera-camera-metadataoutput.md)\* metadataOutput | 要释放的元数据输出实例。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。  CAMERA\_SERVICE\_FATAL\_ERROR：相机服务异常。 |

### OH\_MetadataOutput\_AddMetadataObjectTypes()

```c
Camera_ErrorCode OH_MetadataOutput_AddMetadataObjectTypes(Camera_MetadataOutput* metadataOutput, Camera_MetadataObjectType* types, uint32_t size)
```

**描述**

添加元数据对象类型。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_MetadataOutput](capi-oh-camera-camera-metadataoutput.md)\* metadataOutput | 元数据输出实例。 |
| [Camera\_MetadataObjectType](capi-camera-h.md#camera_metadataobjecttype)\* types | 用于添加到Camera\_MetadataOutput实例的元数据对象类型数组。 |
| uint32\_t size | 元数据对象类型数组长度。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。  CAMERA\_SERVICE\_FATAL\_ERROR：相机服务异常。 |

### OH\_MetadataOutput\_RemoveMetadataObjectTypes()

```c
Camera_ErrorCode OH_MetadataOutput_RemoveMetadataObjectTypes(Camera_MetadataOutput* metadataOutput, Camera_MetadataObjectType* types, uint32_t size)
```

**描述**

移除元数据对象类型。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_MetadataOutput](capi-oh-camera-camera-metadataoutput.md)\* metadataOutput | 元数据输出实例。 |
| [Camera\_MetadataObjectType](capi-camera-h.md#camera_metadataobjecttype)\* types | 从Camera\_MetadataOutput实例移除的元数据对象类型数组。 |
| uint32\_t size | 元数据对象类型数组长度。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。  CAMERA\_SERVICE\_FATAL\_ERROR：相机服务异常。 |

### OH\_MetadataOutput\_OnMetadataObjectExtAvailable()

```c
typedef void (*OH_MetadataOutput_OnMetadataObjectExtAvailable)(void* context, OH_Camera_MetadataObjectExt** metadataObjectExt, uint32_t size)
```

**描述**

用于监听元数据对象上报事件的回调。使用[OH\_MetadataOutput\_RegisterMetadataObjectExtAvailableCallback](capi-metadata-output-h.md#oh_metadataoutput_registermetadataobjectextavailablecallback)进行注册。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| void\* context | 用户提供的上下文指针。 |
| [OH\_Camera\_MetadataObjectExt](capi-oh-camera-oh-camera-metadataobjectext.md)\*\* metadataObjectExt | 指向元数据对象的二级指针。 |
| uint32\_t size | 元数据对象的数量。 |

### OH\_MetadataOutput\_OnErrorExt()

```c
typedef void (*OH_MetadataOutput_OnErrorExt)(void* context, Camera_ErrorCode errorCode)
```

**描述**

在元数据输出期间，用于监听错误事件的回调。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| void\* context | 用户提供的上下文指针。 |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) errorCode | 元数据输出期间报告的错误码。 |

### OH\_MetadataOutput\_RegisterMetadataObjectExtAvailableCallback()

```c
Camera_ErrorCode OH_MetadataOutput_RegisterMetadataObjectExtAvailableCallback(Camera_MetadataOutput* metadataOutput, void* context, OH_MetadataOutput_OnMetadataObjectExtAvailable callback)
```

**描述**

注册监听元数据对象上报事件的回调。该回调可通过[OH\_MetadataOutput\_UnregisterMetadataObjectExtAvailableCallback](capi-metadata-output-h.md#oh_metadataoutput_unregistermetadataobjectextavailablecallback)注销。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_MetadataOutput](capi-oh-camera-camera-metadataoutput.md)\* metadataOutput | 元数据输出实例的指针。 |
| void\* context | 用户提供的上下文指针。 |
| [OH\_MetadataOutput\_OnMetadataObjectExtAvailable](capi-metadata-output-h.md#oh_metadataoutput_onmetadataobjectextavailable) callback | 监听元数据对象上报事件的回调的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：操作成功。  CAMERA\_INVALID\_ARGUMENT：参数缺失或参数类型错误。 |

### OH\_MetadataOutput\_UnregisterMetadataObjectExtAvailableCallback()

```c
Camera_ErrorCode OH_MetadataOutput_UnregisterMetadataObjectExtAvailableCallback(Camera_MetadataOutput* metadataOutput, void* context, OH_MetadataOutput_OnMetadataObjectExtAvailable callback)
```

**描述**

注销监听元数据对象上报事件的回调。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_MetadataOutput](capi-oh-camera-camera-metadataoutput.md)\* metadataOutput | 元数据输出实例的指针。 |
| void\* context | 用户提供的上下文指针。 |
| [OH\_MetadataOutput\_OnMetadataObjectExtAvailable](capi-metadata-output-h.md#oh_metadataoutput_onmetadataobjectextavailable) callback | 监听元数据对象上报事件的回调的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：操作成功。  CAMERA\_INVALID\_ARGUMENT：参数缺失或参数类型错误。 |

### OH\_MetadataOutput\_RegisterErrorExtCallback()

```c
Camera_ErrorCode OH_MetadataOutput_RegisterErrorExtCallback(Camera_MetadataOutput* metadataOutput, void* context, OH_MetadataOutput_OnErrorExt callback)
```

**描述**

注册监听错误事件的回调。该回调可通过[OH\_MetadataOutput\_UnregisterErrorExtCallback](capi-metadata-output-h.md#oh_metadataoutput_unregistererrorextcallback)注销。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_MetadataOutput](capi-oh-camera-camera-metadataoutput.md)\* metadataOutput | 元数据输出实例的指针。 |
| void\* context | 用户提供的上下文指针。 |
| [OH\_MetadataOutput\_OnErrorExt](capi-metadata-output-h.md#oh_metadataoutput_onerrorext) callback | 监听错误事件的回调的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：操作成功。  CAMERA\_INVALID\_ARGUMENT：参数缺失或参数类型错误。 |

### OH\_MetadataOutput\_UnregisterErrorExtCallback()

```c
Camera_ErrorCode OH_MetadataOutput_UnregisterErrorExtCallback(Camera_MetadataOutput* metadataOutput, void* context, OH_MetadataOutput_OnErrorExt callback)
```

**描述**

注销监听错误事件的回调。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_MetadataOutput](capi-oh-camera-camera-metadataoutput.md)\* metadataOutput | 元数据输出实例的指针。 |
| void\* context | 用户提供的上下文指针。 |
| [OH\_MetadataOutput\_OnErrorExt](capi-metadata-output-h.md#oh_metadataoutput_onerrorext) callback | 监听错误事件的回调的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：操作成功。  CAMERA\_INVALID\_ARGUMENT：参数缺失或参数类型错误。 |

### OH\_MetadataOutput\_IsLockMetadataObjectTrackingSupported()

```c
bool OH_MetadataOutput_IsLockMetadataObjectTrackingSupported(const Camera_MetadataOutput* metadataOutput)
```

**描述**

检查设备是否支持锁定元数据对象（如猫脸、狗脸）追踪功能。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [Camera\_MetadataOutput](capi-oh-camera-camera-metadataoutput.md)\* metadataOutput | MetadataOutput实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| bool | true表示支持该功能。  false表示不支持该功能。 |

### OH\_MetadataOutput\_LockMetadataObjectTracking()

```c
Camera_ErrorCode OH_MetadataOutput_LockMetadataObjectTracking(Camera_MetadataOutput* metadataOutput, Camera_Point* pointOfInterest)
```

**描述**

锁定对特定元数据对象（如猫脸、狗脸）的追踪。

该功能以pointOfInterest所指向的点所在的对象为追踪对象，如果该点不存在追踪对象，则功能不生效。

被锁定追踪的对象离开取景范围超过三秒或调用解锁追踪后，锁定追踪自动取消。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_MetadataOutput](capi-oh-camera-camera-metadataoutput.md)\* metadataOutput | 元数据输出实例的指针。 |
| [Camera\_Point](capi-oh-camera-camera-point.md)\* pointOfInterest | 期望追踪对应位置对象的点的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：操作成功。  CAMERA\_INVALID\_ARGUMENT：参数缺失或参数类型错误。  CAMERA\_SESSION\_NOT\_CONFIG：捕获会话未配置。  CAMERA\_SERVICE\_FATAL\_ERROR：相机服务异常。 |

### OH\_MetadataOutput\_UnlockMetadataObjectTracking()

```c
Camera_ErrorCode OH_MetadataOutput_UnlockMetadataObjectTracking(Camera_MetadataOutput* metadataOutput)
```

**描述**

解锁元数据对象（如猫脸、狗脸）的追踪。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_MetadataOutput](capi-oh-camera-camera-metadataoutput.md)\* metadataOutput | 元数据输出实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：操作成功。  CAMERA\_INVALID\_ARGUMENT：参数缺失或参数类型错误。  CAMERA\_SESSION\_NOT\_CONFIG：捕获会话未配置。  CAMERA\_SERVICE\_FATAL\_ERROR：相机服务异常。 |
