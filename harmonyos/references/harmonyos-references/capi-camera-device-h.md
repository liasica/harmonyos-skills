---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-camera-device-h
title: camera_device.h
breadcrumb: API参考 > 媒体 > Camera Kit（相机服务） > C API > 头文件 > camera_device.h
category: harmonyos-references
scraped_at: 2026-04-28T08:12:44+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:df9a47d4b48896ff29c76ec24b6b7b45e6b4927e256fcdb2cf69216df749fc0c
---

## 概述

PhonePC/2in1TabletTVWearable

定义相机的基本接口和功能。

**引用文件：** <ohcamera/camera\_device.h>

**库：** libohcamera.so

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 12

**相关模块：** [OH\_Camera](capi-oh-camera.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 函数

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [Camera\_ErrorCode OH\_CameraDevice\_GetCameraOrientation(Camera\_Device\* camera, uint32\_t\* orientation)](capi-camera-device-h.md#oh_cameradevice_getcameraorientation) | 获取相机设备的传感器方向属性。 |
| [Camera\_ErrorCode OH\_CameraDevice\_GetHostDeviceName(Camera\_Device\* camera, char\*\* hostDeviceName)](capi-camera-device-h.md#oh_cameradevice_gethostdevicename) | 获取远程设备名称。 |
| [Camera\_ErrorCode OH\_CameraDevice\_GetHostDeviceType(Camera\_Device\* camera, Camera\_HostDeviceType\* hostDeviceType)](capi-camera-device-h.md#oh_cameradevice_gethostdevicetype) | 获取远程设备类型。 |

## 函数说明

PhonePC/2in1TabletTVWearable

### OH\_CameraDevice\_GetCameraOrientation()

PhonePC/2in1TabletTVWearable

```
1. Camera_ErrorCode OH_CameraDevice_GetCameraOrientation(Camera_Device* camera, uint32_t* orientation)
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

PhonePC/2in1TabletTVWearable

```
1. Camera_ErrorCode OH_CameraDevice_GetHostDeviceName(Camera_Device* camera, char** hostDeviceName)
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

PhonePC/2in1TabletTVWearable

```
1. Camera_ErrorCode OH_CameraDevice_GetHostDeviceType(Camera_Device* camera, Camera_HostDeviceType* hostDeviceType)
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
