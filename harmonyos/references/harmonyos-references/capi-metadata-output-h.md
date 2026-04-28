---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-metadata-output-h
title: metadata_output.h
breadcrumb: API参考 > 媒体 > Camera Kit（相机服务） > C API > 头文件 > metadata_output.h
category: harmonyos-references
scraped_at: 2026-04-28T08:12:45+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:2b86308e4e47f037616e5ce990f8982d365bfa80f958dfb2127c7ab382cf99a9
---

## 概述

PhonePC/2in1TabletTVWearable

声明元数据输出概念。

**引用文件：** <ohcamera/metadata\_output.h>

**库：** libohcamera.so

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 11

**相关模块：** [OH\_Camera](capi-oh-camera.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 结构体

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [MetadataOutput\_Callbacks](capi-oh-camera-metadataoutput-callbacks.md) | MetadataOutput\_Callbacks | 元数据输出的回调。 |
| [Camera\_MetadataOutput](capi-oh-camera-camera-metadataoutput.md) | Camera\_MetadataOutput | 元数据输出对象。  可以使用[OH\_CameraManager\_CreateMetadataOutput](capi-camera-manager-h.md#oh_cameramanager_createmetadataoutput)方法创建指针。 |

### 函数

PhonePC/2in1TabletTVWearable

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

## 函数说明

PhonePC/2in1TabletTVWearable

### OH\_MetadataOutput\_OnMetadataObjectAvailable()

PhonePC/2in1TabletTVWearable

```
1. typedef void (*OH_MetadataOutput_OnMetadataObjectAvailable)(Camera_MetadataOutput* metadataOutput, Camera_MetadataObject* metadataObject, uint32_t size)
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

PhonePC/2in1TabletTVWearable

```
1. typedef void (*OH_MetadataOutput_OnError)(Camera_MetadataOutput* metadataOutput, Camera_ErrorCode errorCode)
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

PhonePC/2in1TabletTVWearable

```
1. Camera_ErrorCode OH_MetadataOutput_RegisterCallback(Camera_MetadataOutput* metadataOutput, MetadataOutput_Callbacks* callback)
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

PhonePC/2in1TabletTVWearable

```
1. Camera_ErrorCode OH_MetadataOutput_UnregisterCallback(Camera_MetadataOutput* metadataOutput, MetadataOutput_Callbacks* callback)
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

PhonePC/2in1TabletTVWearable

```
1. Camera_ErrorCode OH_MetadataOutput_Start(Camera_MetadataOutput* metadataOutput)
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

PhonePC/2in1TabletTVWearable

```
1. Camera_ErrorCode OH_MetadataOutput_Stop(Camera_MetadataOutput* metadataOutput)
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

PhonePC/2in1TabletTVWearable

```
1. Camera_ErrorCode OH_MetadataOutput_Release(Camera_MetadataOutput* metadataOutput)
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

PhonePC/2in1TabletTVWearable

```
1. Camera_ErrorCode OH_MetadataOutput_AddMetadataObjectTypes(Camera_MetadataOutput* metadataOutput, Camera_MetadataObjectType* types, uint32_t size)
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

PhonePC/2in1TabletTVWearable

```
1. Camera_ErrorCode OH_MetadataOutput_RemoveMetadataObjectTypes(Camera_MetadataOutput* metadataOutput, Camera_MetadataObjectType* types, uint32_t size)
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
