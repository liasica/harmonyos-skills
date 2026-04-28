---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-camera-input-h
title: camera_input.h
breadcrumb: API参考 > 媒体 > Camera Kit（相机服务） > C API > 头文件 > camera_input.h
category: harmonyos-references
scraped_at: 2026-04-28T08:12:44+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:5795a11bbb2cede252c4b337655f2798bdb78236d18a7f19731c57f4b71201da
---

## 概述

PhonePC/2in1TabletTVWearable

声明相机输入概念。

**引用文件：** <ohcamera/camera\_input.h>

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
| [CameraInput\_Callbacks](capi-oh-camera-camerainput-callbacks.md) | CameraInput\_Callbacks | 相机输入错误事件的回调。 |
| [Camera\_Input](capi-oh-camera-camera-input.md) | Camera\_Input | 相机输入对象。可以使用[OH\_CameraManager\_CreateCameraInput](capi-camera-manager-h.md#oh_cameramanager_createcamerainput)方法创建指针。 |

### 函数

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [typedef void (\*OH\_CameraInput\_OnError)(const Camera\_Input\* cameraInput, Camera\_ErrorCode errorCode)](capi-camera-input-h.md#oh_camerainput_onerror) | OH\_CameraInput\_OnError | 在[CameraInput\_Callbacks](capi-oh-camera-camerainput-callbacks.md)中被调用的相机输入错误回调。 |
| [Camera\_ErrorCode OH\_CameraInput\_RegisterCallback(Camera\_Input\* cameraInput, CameraInput\_Callbacks\* callback)](capi-camera-input-h.md#oh_camerainput_registercallback) | - | 注册相机输入更改事件回调。 |
| [Camera\_ErrorCode OH\_CameraInput\_UnregisterCallback(Camera\_Input\* cameraInput, CameraInput\_Callbacks\* callback)](capi-camera-input-h.md#oh_camerainput_unregistercallback) | - | 注销相机输入更改事件回调。 |
| [Camera\_ErrorCode OH\_CameraInput\_Open(Camera\_Input\* cameraInput)](capi-camera-input-h.md#oh_camerainput_open) | - | 打开相机。 |
| [Camera\_ErrorCode OH\_CameraInput\_OpenSecureCamera(Camera\_Input\* cameraInput, uint64\_t\* secureSeqId)](capi-camera-input-h.md#oh_camerainput_opensecurecamera) | - | 打开安全相机。 |
| [Camera\_ErrorCode OH\_CameraInput\_OpenConcurrentCameras(Camera\_Input\* cameraInput, Camera\_ConcurrentType type)](capi-camera-input-h.md#oh_camerainput_openconcurrentcameras) | - | 根据指定并发类型打开相机。 |
| [Camera\_ErrorCode OH\_CameraInput\_Close(Camera\_Input\* cameraInput)](capi-camera-input-h.md#oh_camerainput_close) | - | 关闭相机。 |
| [Camera\_ErrorCode OH\_CameraInput\_Release(Camera\_Input\* cameraInput)](capi-camera-input-h.md#oh_camerainput_release) | - | 释放相机输入实例。  和[OH\_CameraInput\_Close](capi-camera-input-h.md#oh_camerainput_close)只需要调用其中一个，调用之后无须再调用[OH\_CameraInput\_Close](capi-camera-input-h.md#oh_camerainput_close)。 |
| [Camera\_ErrorCode OH\_CameraInput\_IsPhysicalCameraOrientationVariable(Camera\_Input\* cameraInput, bool\* isVariable)](capi-camera-input-h.md#oh_camerainput_isphysicalcameraorientationvariable) | - | 查询设备不同折叠状态下，相机物理镜头角度是否可变。 |
| [Camera\_ErrorCode OH\_CameraInput\_GetPhysicalCameraOrientation(Camera\_Input\* cameraInput, uint32\_t\* orientation)](capi-camera-input-h.md#oh_camerainput_getphysicalcameraorientation) | - | 获取设备当前折叠状态下的物理镜头角度。 |
| [Camera\_ErrorCode OH\_CameraInput\_UsePhysicalCameraOrientation(Camera\_Input\* cameraInput, bool isUsed)](capi-camera-input-h.md#oh_camerainput_usephysicalcameraorientation) | - | 选择是否使用物理镜头角度。 |
| [typedef void (\*OH\_CameraInput\_OnOcclusionDetectionCallback)(const Camera\_Input\* cameraInput, Camera\_OcclusionDetectionResult occlusionDetectionResult)](capi-camera-input-h.md#oh_camerainput_onocclusiondetectioncallback) | OH\_CameraInput\_OnOcclusionDetectionCallback | 相机镜头遮挡、脏污检测结果回调。 |
| [Camera\_ErrorCode OH\_CameraInput\_RegisterOcclusionDetectionCallback(Camera\_Input\* cameraInput, OH\_CameraInput\_OnOcclusionDetectionCallback occlusionDetectionCallback)](capi-camera-input-h.md#oh_camerainput_registerocclusiondetectioncallback) | - | 注册相机镜头遮挡、脏污检测事件回调。 |
| [Camera\_ErrorCode OH\_CameraInput\_UnregisterOcclusionDetectionCallback(Camera\_Input\* cameraInput, OH\_CameraInput\_OnOcclusionDetectionCallback occlusionDetectionCallback)](capi-camera-input-h.md#oh_camerainput_unregisterocclusiondetectioncallback) | - | 注销相机镜头遮挡、脏污检测事件回调。 |

## 函数说明

PhonePC/2in1TabletTVWearable

### OH\_CameraInput\_OnError()

PhonePC/2in1TabletTVWearable

```
1. typedef void (*OH_CameraInput_OnError)(const Camera_Input* cameraInput, Camera_ErrorCode errorCode)
```

**描述**

在[CameraInput\_Callbacks](capi-oh-camera-camerainput-callbacks.md)中被调用的相机输入错误回调。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [Camera\_Input](capi-oh-camera-camera-input.md)\* cameraInput | 传递回调的Camera\_Input。 |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) errorCode | 相机输入的Camera\_ErrorCode。 |

**参考：**

[CAMERA\_CONFLICT\_CAMERA](capi-camera-h.md#camera_errorcode)

[CAMERA\_DEVICE\_DISABLED](capi-camera-h.md#camera_errorcode)

[CAMERA\_DEVICE\_PREEMPTED](capi-camera-h.md#camera_errorcode)

[CAMERA\_SERVICE\_FATAL\_ERROR](capi-camera-h.md#camera_errorcode)

### OH\_CameraInput\_RegisterCallback()

PhonePC/2in1TabletTVWearable

```
1. Camera_ErrorCode OH_CameraInput_RegisterCallback(Camera_Input* cameraInput, CameraInput_Callbacks* callback)
```

**描述**

注册相机输入更改事件回调。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_Input](capi-oh-camera-camera-input.md)\* cameraInput | Camera\_Input实例。 |
| [CameraInput\_Callbacks](capi-oh-camera-camerainput-callbacks.md)\* callback | 要注册的相机输入更改事件回调。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。 |

### OH\_CameraInput\_UnregisterCallback()

PhonePC/2in1TabletTVWearable

```
1. Camera_ErrorCode OH_CameraInput_UnregisterCallback(Camera_Input* cameraInput, CameraInput_Callbacks* callback)
```

**描述**

注销相机输入更改事件回调。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_Input](capi-oh-camera-camera-input.md)\* cameraInput | Camera\_Input实例。 |
| [CameraInput\_Callbacks](capi-oh-camera-camerainput-callbacks.md)\* callback | 要注销的相机输入更改事件回调。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。 |

### OH\_CameraInput\_Open()

PhonePC/2in1TabletTVWearable

```
1. Camera_ErrorCode OH_CameraInput_Open(Camera_Input* cameraInput)
```

**描述**

打开相机。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_Input](capi-oh-camera-camera-input.md)\* cameraInput | 要打开的Camera\_Input实例。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。  CAMERA\_CONFLICT\_CAMERA：因冲突而无法使用相机。  CAMERA\_DEVICE\_DISABLED：由于安全原因禁用了相机。  CAMERA\_SERVICE\_FATAL\_ERROR：相机服务异常。 |

### OH\_CameraInput\_OpenSecureCamera()

PhonePC/2in1TabletTVWearable

```
1. Camera_ErrorCode OH_CameraInput_OpenSecureCamera(Camera_Input* cameraInput, uint64_t* secureSeqId)
```

**描述**

打开安全相机。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_Input](capi-oh-camera-camera-input.md)\* cameraInput | 要打开的Camera\_Input实例。 |
| uint64\_t\* secureSeqId | 表示安全摄像头的序列值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。  CAMERA\_CONFLICT\_CAMERA：因冲突而无法使用相机。  CAMERA\_DEVICE\_DISABLED：由于安全原因禁用了相机。  CAMERA\_SERVICE\_FATAL\_ERROR：相机服务异常。 |

### OH\_CameraInput\_OpenConcurrentCameras()

PhonePC/2in1TabletTVWearable

```
1. Camera_ErrorCode OH_CameraInput_OpenConcurrentCameras(Camera_Input* cameraInput, Camera_ConcurrentType type)
```

**描述**

根据指定并发类型打开相机。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_Input](capi-oh-camera-camera-input.md)\* cameraInput | 要打开的Camera\_Input实例。 |
| [Camera\_ConcurrentType](capi-camera-h.md#camera_concurrenttype) type | 指定并发类型。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK: 方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。  CAMERA\_CONFLICT\_CAMERA：因冲突而无法使用相机。  CAMERA\_DEVICE\_DISABLED：由于安全原因禁用了相机。  CAMERA\_SERVICE\_FATAL\_ERROR：相机服务异常。 |

### OH\_CameraInput\_Close()

PhonePC/2in1TabletTVWearable

```
1. Camera_ErrorCode OH_CameraInput_Close(Camera_Input* cameraInput)
```

**描述**

关闭相机。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_Input](capi-oh-camera-camera-input.md)\* cameraInput | 要关闭的Camera\_Input实例。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。  CAMERA\_SERVICE\_FATAL\_ERROR：相机服务异常。 |

### OH\_CameraInput\_Release()

PhonePC/2in1TabletTVWearable

```
1. Camera_ErrorCode OH_CameraInput_Release(Camera_Input* cameraInput)
```

**描述**

释放相机输入实例。

和[OH\_CameraInput\_Close](capi-camera-input-h.md#oh_camerainput_close)只需要调用其中一个，调用之后无须再调用[OH\_CameraInput\_Close](capi-camera-input-h.md#oh_camerainput_close)。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_Input](capi-oh-camera-camera-input.md)\* cameraInput | 要释放的Camera\_Input实例。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。  CAMERA\_SERVICE\_FATAL\_ERROR：相机服务异常。 |

### OH\_CameraInput\_IsPhysicalCameraOrientationVariable()

PhonePC/2in1TabletTVWearable

```
1. Camera_ErrorCode OH_CameraInput_IsPhysicalCameraOrientationVariable(Camera_Input* cameraInput, bool* isVariable)
```

**描述**

查询设备不同折叠状态下，相机物理镜头角度是否可变。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_Input](capi-oh-camera-camera-input.md)\* cameraInput | Camera\_Input实例。 |
| bool\* isVariable | 查询设备不同折叠状态下，相机物理镜头角度是否可变。true表示可变，false表示不可变。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。 |

### OH\_CameraInput\_GetPhysicalCameraOrientation()

PhonePC/2in1TabletTVWearable

```
1. Camera_ErrorCode OH_CameraInput_GetPhysicalCameraOrientation(Camera_Input* cameraInput, uint32_t* orientation)
```

**描述**

获取设备当前折叠状态下的物理镜头角度。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_Input](capi-oh-camera-camera-input.md)\* cameraInput | Camera\_Input实例。 |
| uint32\_t\* orientation | 如果方法调用成功，将返回设备当前折叠状态下的物理镜头角度。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。 |

### OH\_CameraInput\_UsePhysicalCameraOrientation()

PhonePC/2in1TabletTVWearable

```
1. Camera_ErrorCode OH_CameraInput_UsePhysicalCameraOrientation(Camera_Input* cameraInput, bool isUsed)
```

**描述**

选择是否使用物理镜头角度。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_Input](capi-oh-camera-camera-input.md)\* cameraInput | Camera\_Input实例。 |
| bool isUsed | 选择是否使用物理镜头角度。true表示使用，false表示不使用。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。  CAMERA\_OPERATION\_NOT\_ALLOWED：操作不允许。  CAMERA\_SERVICE\_FATAL\_ERROR：相机服务异常。 |

### OH\_CameraInput\_OnOcclusionDetectionCallback()

PhonePC/2in1TabletTVWearable

```
1. typedef void (*OH_CameraInput_OnOcclusionDetectionCallback)(const Camera_Input* cameraInput, Camera_OcclusionDetectionResult occlusionDetectionResult)
```

**描述**

相机镜头遮挡、脏污检测结果回调。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const Camera\_Input\* cameraInput | 传递回调的Camera\_Input。 |
| [Camera\_OcclusionDetectionResult](capi-oh-camera-camera-occlusiondetectionresult.md) occlusionDetectionResult | 相机镜头遮挡、脏污检测结果。 |

### OH\_CameraInput\_RegisterOcclusionDetectionCallback()

PhonePC/2in1TabletTVWearable

```
1. Camera_ErrorCode OH_CameraInput_RegisterOcclusionDetectionCallback(Camera_Input* cameraInput, OH_CameraInput_OnOcclusionDetectionCallback occlusionDetectionCallback)
```

**描述**

注册相机镜头遮挡、脏污检测事件回调。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_Input](capi-oh-camera-camera-input.md)\* cameraInput | Camera\_Input实例。 |
| [OH\_CameraInput\_OnOcclusionDetectionCallback](capi-camera-input-h.md#oh_camerainput_onocclusiondetectioncallback) occlusionDetectionCallback | 要注册的相机镜头遮挡、脏污检测事件回调。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。 |

### OH\_CameraInput\_UnregisterOcclusionDetectionCallback()

PhonePC/2in1TabletTVWearable

```
1. Camera_ErrorCode OH_CameraInput_UnregisterOcclusionDetectionCallback(Camera_Input* cameraInput, OH_CameraInput_OnOcclusionDetectionCallback occlusionDetectionCallback)
```

**描述**

注销相机镜头遮挡、脏污检测事件回调。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_Input](capi-oh-camera-camera-input.md)\* cameraInput | Camera\_Input实例。 |
| [OH\_CameraInput\_OnOcclusionDetectionCallback](capi-camera-input-h.md#oh_camerainput_onocclusiondetectioncallback) occlusionDetectionCallback | 要注销的相机镜头遮挡、脏污检测事件回调。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。 |
