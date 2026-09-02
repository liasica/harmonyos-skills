---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-camera-device-h
title: camera_device.h
breadcrumb: API参考 > 媒体 > Camera Kit（相机服务） > C API > 头文件 > camera_device.h
category: harmonyos-references
scraped_at: 2026-09-02T15:02:27+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:30b7bde410e618d797fda5d2b21e2d8f5be264d24b7840399816c8f5a1953d3f
---

## 概述

定义相机的基本接口和功能。

**引用文件：** <ohcamera/camera\_device.h>

**库：** libohcamera.so

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 12

**相关模块：** [OH\_Camera](capi-oh-camera.md)

## 汇总

### 函数

| 名称 | 描述 |
| --- | --- |
| [Camera\_ErrorCode OH\_CameraDevice\_GetCameraOrientation(Camera\_Device\* camera, uint32\_t\* orientation)](capi-camera-device-h.md#oh_cameradevice_getcameraorientation) | 获取相机设备的传感器方向属性。 |
| [Camera\_ErrorCode OH\_CameraDevice\_GetHostDeviceName(Camera\_Device\* camera, char\*\* hostDeviceName)](capi-camera-device-h.md#oh_cameradevice_gethostdevicename) | 获取远程设备名称。 |
| [Camera\_ErrorCode OH\_CameraDevice\_GetHostDeviceType(Camera\_Device\* camera, Camera\_HostDeviceType\* hostDeviceType)](capi-camera-device-h.md#oh_cameradevice_gethostdevicetype) | 获取远程设备类型。 |
| [Camera\_ErrorCode OH\_CameraDevice\_GetLensEquivalentFocalLengths(const Camera\_Device\* camera, uint32\_t\*\* equivalentFocalLengths, uint32\_t\* size)](capi-camera-device-h.md#oh_cameradevice_getlensequivalentfocallengths) | 获取相机设备的等效焦距。 |
| [Camera\_ErrorCode OH\_CameraDevice\_IsLogicalCamera(const Camera\_Device\* camera, bool\* isLogicalCamera)](capi-camera-device-h.md#oh_cameradevice_islogicalcamera) | 检查相机设备是否为逻辑摄像头（由一个或多个物理摄像头组成）。 |
| [Camera\_ErrorCode OH\_CameraDevice\_GetLogicalCameraConstituentCameraDevices(const Camera\_Device\* logicalCamera, Camera\_Device\*\* constituentCameras, uint32\_t\* size)](capi-camera-device-h.md#oh_cameradevice_getlogicalcameraconstituentcameradevices) | 获取组成逻辑摄像头的所有物理摄像头。调用[OH\_CameraDevice\_DeleteConstituentCameraDevices](capi-camera-device-h.md#oh_cameradevice_deleteconstituentcameradevices)释放组成逻辑摄像头的所有物理摄像头。 |
| [Camera\_ErrorCode OH\_CameraDevice\_DeleteConstituentCameraDevices(const Camera\_Device\* logicalCamera, Camera\_Device\* constituentCameras, uint32\_t size)](capi-camera-device-h.md#oh_cameradevice_deleteconstituentcameradevices) | 删除组成逻辑摄像头的所有物理摄像头。 |
| [Camera\_ErrorCode OH\_CameraDevice\_GetLensFocalLength(const Camera\_Device\* camera, float\* lensFocalLength)](capi-camera-device-h.md#oh_cameradevice_getlensfocallength) | 获取相机镜头的焦距。 |
| [Camera\_ErrorCode OH\_CameraDevice\_GetMinimumFocusDistance(const Camera\_Device\* camera, float\* minimumFocusDistance)](capi-camera-device-h.md#oh_cameradevice_getminimumfocusdistance) | 获取相机设备的最小对焦距离。 |
| [Camera\_ErrorCode OH\_CameraDevice\_GetLensDistortion(const Camera\_Device\* camera, float\*\* lens, uint32\_t\* size)](capi-camera-device-h.md#oh_cameradevice_getlensdistortion) | 获取相机设备的镜头畸变参数。 |
| [Camera\_ErrorCode OH\_CameraDevice\_GetIntrinsicCalibration(const Camera\_Device\* camera, float\*\* intrinsicCalibration, uint32\_t\* size)](capi-camera-device-h.md#oh_cameradevice_getintrinsiccalibration) | 获取相机设备的内参标定参数。 |
| [Camera\_ErrorCode OH\_CameraDevice\_GetSensorPhysicalSize(const Camera\_Device\* camera, float\* width, float\* height)](capi-camera-device-h.md#oh_cameradevice_getsensorphysicalsize) | 获取相机传感器的物理尺寸。 |
| [Camera\_ErrorCode OH\_CameraDevice\_GetSensorPixelArraySize(const Camera\_Device\* camera, uint32\_t\* width, uint32\_t\* height)](capi-camera-device-h.md#oh_cameradevice_getsensorpixelarraysize) | 获取相机传感器的像素阵列大小。 |
| [Camera\_ErrorCode OH\_CameraDevice\_GetSensorColorFilterArrangement(const Camera\_Device\* camera, OH\_Camera\_SensorColorFilterArrangement\* sensorCFA)](capi-camera-device-h.md#oh_cameradevice_getsensorcolorfilterarrangement) | 获取相机传感器的滤色阵列排列方式。 |
| [Camera\_ErrorCode OH\_CameraDevice\_GetAutomotiveCameraPosition(const Camera\_Device\* camera, OH\_Camera\_AutomotiveCameraPosition\* automotiveCameraPosition)](capi-camera-device-h.md#oh_cameradevice_getautomotivecameraposition) | 获取Car设备相机摄像头的位置。 |

## 函数说明

### OH\_CameraDevice\_GetCameraOrientation()

```c
Camera_ErrorCode OH_CameraDevice_GetCameraOrientation(Camera_Device* camera, uint32_t* orientation)
```

**描述**

获取相机设备的传感器方向属性。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_Device](capi-oh-camera-camera-device.md)\* camera | 用于获取属性的Camera\_Device。 |
| uint32\_t\* orientation | 返回相机sensor角度属性。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功，返回传感器方向属性。  CAMERA\_CAMERA\_INVALID\_ARGUMENT：参数丢失或者参数不正确。  CAMERA\_SERVICE\_FATAL\_ERROR：相机服务异常。 |

### OH\_CameraDevice\_GetHostDeviceName()

```c
Camera_ErrorCode OH_CameraDevice_GetHostDeviceName(Camera_Device* camera, char** hostDeviceName)
```

**描述**

获取远程设备名称。

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_Device](capi-oh-camera-camera-device.md)\* camera | 用于获取属性的Camera\_Device。 |
| char\*\* hostDeviceName | 返回远程设备名称属性。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功，将返回远程设备名称属性。  CAMERA\_CAMERA\_INVALID\_ARGUMENT：参数丢失或者参数不正确。  CAMERA\_SERVICE\_FATAL\_ERROR：相机服务异常。 |

### OH\_CameraDevice\_GetHostDeviceType()

```c
Camera_ErrorCode OH_CameraDevice_GetHostDeviceType(Camera_Device* camera, Camera_HostDeviceType* hostDeviceType)
```

**描述**

获取远程设备类型。

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_Device](capi-oh-camera-camera-device.md)\* camera | 用于获取属性的Camera\_Device。 |
| [Camera\_HostDeviceType](capi-camera-h.md#camera_hostdevicetype)\* hostDeviceType | 远程设备类型属性。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功，将返回远程设备名称属性。  CAMERA\_CAMERA\_INVALID\_ARGUMENT：参数丢失或者参数不正确。  CAMERA\_SERVICE\_FATAL\_ERROR：相机服务异常。 |

### OH\_CameraDevice\_GetLensEquivalentFocalLengths()

```c
Camera_ErrorCode OH_CameraDevice_GetLensEquivalentFocalLengths(const Camera_Device* camera, uint32_t** equivalentFocalLengths, uint32_t* size)
```

**描述**

获取相机设备的等效焦距。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [Camera\_Device](capi-oh-camera-camera-device.md)\* camera | 用于获取属性的Camera\_Device指针。 |
| uint32\_t\*\* equivalentFocalLengths | 输出参数，返回等效焦距数组。 |
| uint32\_t\* size | 输出参数，返回数组大小。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或者参数不正确。  CAMERA\_SERVICE\_FATAL\_ERROR：相机服务异常。 |

### OH\_CameraDevice\_IsLogicalCamera()

```c
Camera_ErrorCode OH_CameraDevice_IsLogicalCamera(const Camera_Device* camera, bool* isLogicalCamera)
```

**描述**

检查相机设备是否为逻辑摄像头（由一个或多个物理摄像头组成）。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [Camera\_Device](capi-oh-camera-camera-device.md)\* camera | 用于获取属性的Camera\_Device指针。 |
| bool\* isLogicalCamera | 输出参数，返回表示是否为逻辑摄像头的布尔值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或者参数不正确。  CAMERA\_SERVICE\_FATAL\_ERROR：相机服务异常。 |

### OH\_CameraDevice\_GetLogicalCameraConstituentCameraDevices()

```c
Camera_ErrorCode OH_CameraDevice_GetLogicalCameraConstituentCameraDevices(const Camera_Device* logicalCamera, Camera_Device** constituentCameras, uint32_t* size)
```

**描述**

获取组成逻辑摄像头的所有物理摄像头。调用[OH\_CameraDevice\_DeleteConstituentCameraDevices](capi-camera-device-h.md#oh_cameradevice_deleteconstituentcameradevices)释放组成逻辑摄像头的所有物理摄像头。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [Camera\_Device](capi-oh-camera-camera-device.md)\* logicalCamera | 逻辑摄像头的Camera\_Device指针。 |
| [Camera\_Device](capi-oh-camera-camera-device.md)\*\* constituentCameras | 输出参数，返回组成逻辑摄像头的物理摄像头集合指针数组。 |
| uint32\_t\* size | 输出物理摄像头数量数组的大小。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或者参数不正确。  CAMERA\_SERVICE\_FATAL\_ERROR：相机服务异常。 |

### OH\_CameraDevice\_DeleteConstituentCameraDevices()

```c
Camera_ErrorCode OH_CameraDevice_DeleteConstituentCameraDevices(const Camera_Device* logicalCamera, Camera_Device* constituentCameras, uint32_t size)
```

**描述**

删除组成逻辑摄像头的所有物理摄像头。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [Camera\_Device](capi-oh-camera-camera-device.md)\* logicalCamera | 逻辑摄像头的Camera\_Device指针。 |
| [Camera\_Device](capi-oh-camera-camera-device.md)\* constituentCameras | 期望被释放的组成逻辑摄像头的物理摄像头集合。 |
| uint32\_t size | 物理摄像头数量数组的大小。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或者参数不正确。 |

### OH\_CameraDevice\_GetLensFocalLength()

```c
Camera_ErrorCode OH_CameraDevice_GetLensFocalLength(const Camera_Device* camera, float* lensFocalLength)
```

**描述**

获取相机镜头的焦距。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [Camera\_Device](capi-oh-camera-camera-device.md)\* camera | 用于获取属性的Camera\_Device指针。 |
| float\* lensFocalLength | 输出参数，返回镜头焦距值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或者参数不正确。  CAMERA\_SERVICE\_FATAL\_ERROR：相机服务异常。 |

### OH\_CameraDevice\_GetMinimumFocusDistance()

```c
Camera_ErrorCode OH_CameraDevice_GetMinimumFocusDistance(const Camera_Device* camera, float* minimumFocusDistance)
```

**描述**

获取相机设备的最小对焦距离。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [Camera\_Device](capi-oh-camera-camera-device.md)\* camera | 用于获取属性的Camera\_Device指针。 |
| float\* minimumFocusDistance | 输出参数，返回最小对焦距离。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或者参数不正确。  CAMERA\_SERVICE\_FATAL\_ERROR：相机服务异常。 |

### OH\_CameraDevice\_GetLensDistortion()

```c
Camera_ErrorCode OH_CameraDevice_GetLensDistortion(const Camera_Device* camera, float** lens, uint32_t* size)
```

**描述**

获取相机设备的镜头畸变参数。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [Camera\_Device](capi-oh-camera-camera-device.md)\* camera | 用于获取属性的Camera\_Device指针。 |
| float\*\* lens | 输出参数，返回镜头畸变参数数组。 |
| uint32\_t\* size | 输出参数，返回数组大小。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或者参数不正确。  CAMERA\_SERVICE\_FATAL\_ERROR：相机服务异常。 |

### OH\_CameraDevice\_GetIntrinsicCalibration()

```c
Camera_ErrorCode OH_CameraDevice_GetIntrinsicCalibration(const Camera_Device* camera, float** intrinsicCalibration, uint32_t* size)
```

**描述**

获取相机设备的内参标定参数。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [Camera\_Device](capi-oh-camera-camera-device.md)\* camera | 用于获取属性的Camera\_Device指针。 |
| float\*\* intrinsicCalibration | 输出参数，返回内参标定参数数组。 |
| uint32\_t\* size | 输出参数，返回数组大小。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或者参数不正确。  CAMERA\_SERVICE\_FATAL\_ERROR：相机服务异常。 |

### OH\_CameraDevice\_GetSensorPhysicalSize()

```c
Camera_ErrorCode OH_CameraDevice_GetSensorPhysicalSize(const Camera_Device* camera, float* width, float* height)
```

**描述**

获取相机传感器的物理尺寸。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [Camera\_Device](capi-oh-camera-camera-device.md)\* camera | 用于获取属性的Camera\_Device指针。 |
| float\* width | 输出参数，返回传感器宽度（单位：毫米）。 |
| float\* height | 输出参数，返回传感器高度（单位：毫米）。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或者参数不正确。  CAMERA\_SERVICE\_FATAL\_ERROR：相机服务异常。 |

### OH\_CameraDevice\_GetSensorPixelArraySize()

```c
Camera_ErrorCode OH_CameraDevice_GetSensorPixelArraySize(const Camera_Device* camera, uint32_t* width, uint32_t* height)
```

**描述**

获取相机传感器的像素阵列大小。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [Camera\_Device](capi-oh-camera-camera-device.md)\* camera | 用于获取属性的Camera\_Device指针。 |
| uint32\_t\* width | 输出参数，返回像素阵列宽度（单位：像素）。 |
| uint32\_t\* height | 输出参数，返回像素阵列高度（单位：像素）。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或者参数不正确。  CAMERA\_SERVICE\_FATAL\_ERROR：相机服务异常。 |

### OH\_CameraDevice\_GetSensorColorFilterArrangement()

```c
Camera_ErrorCode OH_CameraDevice_GetSensorColorFilterArrangement(const Camera_Device* camera, OH_Camera_SensorColorFilterArrangement* sensorCFA)
```

**描述**

获取相机传感器的滤色阵列排列方式。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [Camera\_Device](capi-oh-camera-camera-device.md)\* camera | 用于获取属性的Camera\_Device指针。 |
| [OH\_Camera\_SensorColorFilterArrangement](capi-camera-h.md#oh_camera_sensorcolorfilterarrangement)\* sensorCFA | 输出参数，返回传感器滤色阵列排列枚举值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或者参数不正确。  CAMERA\_SERVICE\_FATAL\_ERROR：相机服务异常。 |

### OH\_CameraDevice\_GetAutomotiveCameraPosition()

```c
Camera_ErrorCode OH_CameraDevice_GetAutomotiveCameraPosition(const Camera_Device* camera, OH_Camera_AutomotiveCameraPosition* automotiveCameraPosition)
```

**描述**

获取Car设备相机摄像头的位置。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [Camera\_Device](capi-oh-camera-camera-device.md)\* camera | 指向用于检索属性的Camera\_Device的指针。 |
| [OH\_Camera\_AutomotiveCameraPosition](capi-camera-h.md#oh_camera_automotivecameraposition)\* automotiveCameraPosition | 输出参数，返回Car设备摄像头位置枚举值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或者参数不正确。  CAMERA\_SERVICE\_FATAL\_ERROR：相机服务异常。 |
