---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-camera-manager-h
title: camera_manager.h
breadcrumb: API参考 > 媒体 > Camera Kit（相机服务） > C API > 头文件 > camera_manager.h
category: harmonyos-references
scraped_at: 2026-04-28T08:12:44+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:9c96a2f6a9adb99ca04466ab3dda5219826591b951eb96f7d62ab06e22278ae4
---

## 概述

PhonePC/2in1TabletTVWearable

声明相机管理器的概念。

**引用文件：** <ohcamera/camera\_manager.h>

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
| [CameraManager\_Callbacks](capi-oh-camera-cameramanager-callbacks.md) | CameraManager\_Callbacks | 相机设备状态的回调。 |

### 函数

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [typedef void (\*OH\_CameraManager\_StatusCallback)(Camera\_Manager\* cameraManager, Camera\_StatusInfo\* status)](capi-camera-manager-h.md#oh_cameramanager_statuscallback) | OH\_CameraManager\_StatusCallback | 在[CameraManager\_Callbacks](capi-oh-camera-cameramanager-callbacks.md)中被调用的相机管理器状态回调。 |
| [typedef void (\*OH\_CameraManager\_TorchStatusCallback)(Camera\_Manager\* cameraManager, Camera\_TorchStatusInfo\* status)](capi-camera-manager-h.md#oh_cameramanager_torchstatuscallback) | OH\_CameraManager\_TorchStatusCallback | 手电筒状态变化回调。 |
| [typedef void (\*OH\_CameraManager\_OnFoldStatusInfoChange)(Camera\_Manager\* cameraManager, Camera\_FoldStatusInfo\* foldStatusInfo)](capi-camera-manager-h.md#oh_cameramanager_onfoldstatusinfochange) | OH\_CameraManager\_OnFoldStatusInfoChange | 相机管理器折叠状态信息回调。 |
| [Camera\_ErrorCode OH\_CameraManager\_RegisterCallback(Camera\_Manager\* cameraManager, CameraManager\_Callbacks\* callback)](capi-camera-manager-h.md#oh_cameramanager_registercallback) | - | 注册相机状态更改事件回调。 |
| [Camera\_ErrorCode OH\_CameraManager\_UnregisterCallback(Camera\_Manager\* cameraManager, CameraManager\_Callbacks\* callback)](capi-camera-manager-h.md#oh_cameramanager_unregistercallback) | - | 注销相机状态更改事件回调。 |
| [Camera\_ErrorCode OH\_CameraManager\_RegisterTorchStatusCallback(Camera\_Manager\* cameraManager, OH\_CameraManager\_TorchStatusCallback torchStatusCallback)](capi-camera-manager-h.md#oh_cameramanager_registertorchstatuscallback) | - | 注册手电筒状态变更事件回调。 |
| [Camera\_ErrorCode OH\_CameraManager\_UnregisterTorchStatusCallback(Camera\_Manager\* cameraManager, OH\_CameraManager\_TorchStatusCallback torchStatusCallback)](capi-camera-manager-h.md#oh_cameramanager_unregistertorchstatuscallback) | - | 注销手电筒状态变更事件回调。 |
| [Camera\_ErrorCode OH\_CameraManager\_RegisterFoldStatusInfoCallback(Camera\_Manager\* cameraManager, OH\_CameraManager\_OnFoldStatusInfoChange foldStatusInfoCallback)](capi-camera-manager-h.md#oh_cameramanager_registerfoldstatusinfocallback) | - | 注册折叠状态信息变更事件回调。 |
| [Camera\_ErrorCode OH\_CameraManager\_UnregisterFoldStatusInfoCallback(Camera\_Manager\* cameraManager, OH\_CameraManager\_OnFoldStatusInfoChange foldStatusInfoCallback)](capi-camera-manager-h.md#oh_cameramanager_unregisterfoldstatusinfocallback) | - | 注销折叠状态信息变更事件回调。 |
| [Camera\_ErrorCode OH\_CameraManager\_GetSupportedCameras(Camera\_Manager\* cameraManager, Camera\_Device\*\* cameras, uint32\_t\* size)](capi-camera-manager-h.md#oh_cameramanager_getsupportedcameras) | - | 获取支持指定的相机设备实例。 |
| [Camera\_ErrorCode OH\_CameraManager\_DeleteSupportedCameras(Camera\_Manager\* cameraManager, Camera\_Device\* cameras, uint32\_t size)](capi-camera-manager-h.md#oh_cameramanager_deletesupportedcameras) | - | 删除支持的相机。 |
| [Camera\_ErrorCode OH\_CameraManager\_GetSupportedCameraOutputCapability(Camera\_Manager\* cameraManager, const Camera\_Device\* camera, Camera\_OutputCapability\*\* cameraOutputCapability)](capi-camera-manager-h.md#oh_cameramanager_getsupportedcameraoutputcapability) | - | 查询指定相机支持的输出能力。 |
| [Camera\_ErrorCode OH\_CameraManager\_GetSupportedCameraOutputCapabilityWithSceneMode(Camera\_Manager\* cameraManager, const Camera\_Device\* camera, Camera\_SceneMode sceneMode, Camera\_OutputCapability\*\* cameraOutputCapability)](capi-camera-manager-h.md#oh_cameramanager_getsupportedcameraoutputcapabilitywithscenemode) | - | 查询指定相机在指定模式下支持的输出能力。 |
| [Camera\_ErrorCode OH\_CameraManager\_GetSupportedFullCameraOutputCapabilityWithSceneMode(Camera\_Manager\* cameraManager, const Camera\_Device\* camera, Camera\_SceneMode sceneMode, Camera\_OutputCapability\*\* cameraOutputCapability)](capi-camera-manager-h.md#oh_cameramanager_getsupportedfullcameraoutputcapabilitywithscenemode) | - | 查询指定相机在指定模式下支持的完整输出能力，包括未压缩图（YUV）、HEIF和HDR等能力。使用YUV，HEIF或HDR等能力前，需要先显式调用此方法确保获取完整输出能力。 |
| [Camera\_ErrorCode OH\_CameraManager\_DeleteSupportedCameraOutputCapability(Camera\_Manager\* cameraManager, Camera\_OutputCapability\* cameraOutputCapability)](capi-camera-manager-h.md#oh_cameramanager_deletesupportedcameraoutputcapability) | - | 删除支持的输出能力。 |
| [Camera\_ErrorCode OH\_CameraManager\_IsCameraMuted(Camera\_Manager\* cameraManager, bool\* isCameraMuted)](capi-camera-manager-h.md#oh_cameramanager_iscameramuted) | - | 确定相机是否静音。 |
| [Camera\_ErrorCode OH\_CameraManager\_CreateCaptureSession(Camera\_Manager\* cameraManager, Camera\_CaptureSession\*\* captureSession)](capi-camera-manager-h.md#oh_cameramanager_createcapturesession) | - | 创建捕获会话实例。 |
| [Camera\_ErrorCode OH\_CameraManager\_CreateCameraInput(Camera\_Manager\* cameraManager, const Camera\_Device\* camera, Camera\_Input\*\* cameraInput)](capi-camera-manager-h.md#oh_cameramanager_createcamerainput) | - | 创建相机输入实例。 |
| [Camera\_ErrorCode OH\_CameraManager\_CreateCameraInput\_WithPositionAndType(Camera\_Manager\* cameraManager, Camera\_Position position, Camera\_Type type, Camera\_Input\*\* cameraInput)](capi-camera-manager-h.md#oh_cameramanager_createcamerainput_withpositionandtype) | - | 创建具有位置和类型的相机输入实例。 |
| [Camera\_ErrorCode OH\_CameraManager\_CreatePreviewOutput(Camera\_Manager\* cameraManager, const Camera\_Profile\* profile, const char\* surfaceId, Camera\_PreviewOutput\*\* previewOutput)](capi-camera-manager-h.md#oh_cameramanager_createpreviewoutput) | - | 创建预览输出实例。 |
| [Camera\_ErrorCode OH\_CameraManager\_CreatePreviewOutputUsedInPreconfig(Camera\_Manager\* cameraManager, const char\* surfaceId, Camera\_PreviewOutput\*\* previewOutput)](capi-camera-manager-h.md#oh_cameramanager_createpreviewoutputusedinpreconfig) | - | 创建在预配置流中使用的预览输出实例。 |
| [Camera\_ErrorCode OH\_CameraManager\_CreatePhotoOutput(Camera\_Manager\* cameraManager, const Camera\_Profile\* profile, const char\* surfaceId, Camera\_PhotoOutput\*\* photoOutput)](capi-camera-manager-h.md#oh_cameramanager_createphotooutput) | - | 创建一个拍照输出实例。该接口只支持创建JPEG格式的拍照输出对象。 |
| [Camera\_ErrorCode OH\_CameraManager\_CreatePhotoOutputUsedInPreconfig(Camera\_Manager\* cameraManager, const char\* surfaceId, Camera\_PhotoOutput\*\* photoOutput)](capi-camera-manager-h.md#oh_cameramanager_createphotooutputusedinpreconfig) | - | 创建在预配置流中使用的照片输出实例。 |
| [Camera\_ErrorCode OH\_CameraManager\_CreatePhotoOutputWithoutSurface(Camera\_Manager \*cameraManager, const Camera\_Profile \*profile, Camera\_PhotoOutput \*\*photoOutput)](capi-camera-manager-h.md#oh_cameramanager_createphotooutputwithoutsurface) | - | 创建照片输出实例，调用此函数不需要surfaceId。 |
| [Camera\_ErrorCode OH\_CameraManager\_CreateVideoOutput(Camera\_Manager\* cameraManager, const Camera\_VideoProfile\* profile, const char\* surfaceId, Camera\_VideoOutput\*\* videoOutput)](capi-camera-manager-h.md#oh_cameramanager_createvideooutput) | - | 创建一个录像输出实例。 |
| [Camera\_ErrorCode OH\_CameraManager\_CreateVideoOutputUsedInPreconfig(Camera\_Manager\* cameraManager, const char\* surfaceId, Camera\_VideoOutput\*\* videoOutput)](capi-camera-manager-h.md#oh_cameramanager_createvideooutputusedinpreconfig) | - | 创建在预配置流中使用的视频输出实例。 |
| [Camera\_ErrorCode OH\_CameraManager\_CreateMetadataOutput(Camera\_Manager\* cameraManager, const Camera\_MetadataObjectType\* profile, Camera\_MetadataOutput\*\* metadataOutput)](capi-camera-manager-h.md#oh_cameramanager_createmetadataoutput) | - | 创建元数据输出实例。 |
| [Camera\_ErrorCode OH\_CameraManager\_CreateMetadataOutputWithObjectTypes(Camera\_Manager\* cameraManager, const Camera\_MetadataObjectType\* metadataObjectTypes, uint32\_t size, Camera\_MetadataOutput\*\* metadataOutput)](capi-camera-manager-h.md#oh_cameramanager_createmetadataoutputwithobjecttypes) | - | 使用元数据对象类型数组创建元数据输出实例。 |
| [Camera\_ErrorCode OH\_CameraManager\_GetSupportedSceneModes(Camera\_Device\* camera, Camera\_SceneMode\*\* sceneModes, uint32\_t\* size)](capi-camera-manager-h.md#oh_cameramanager_getsupportedscenemodes) | - | 获取特定相机支持的场景模式。 |
| [Camera\_ErrorCode OH\_CameraManager\_DeleteSceneModes(Camera\_Manager\* cameraManager, Camera\_SceneMode\* sceneModes)](capi-camera-manager-h.md#oh_cameramanager_deletescenemodes) | - | 删除场景模式。 |
| [Camera\_ErrorCode OH\_CameraManager\_IsTorchSupported(Camera\_Manager\* cameraManager, bool\* isTorchSupported)](capi-camera-manager-h.md#oh_cameramanager_istorchsupported) | - | 检查设备是否支持手电筒。 |
| [Camera\_ErrorCode OH\_CameraManager\_IsTorchSupportedByTorchMode(Camera\_Manager\* cameraManager, Camera\_TorchMode torchMode, bool\* isTorchSupported)](capi-camera-manager-h.md#oh_cameramanager_istorchsupportedbytorchmode) | - | 检查设备是否支持指定的手电筒模式。 |
| [Camera\_ErrorCode OH\_CameraManager\_SetTorchMode(Camera\_Manager\* cameraManager, Camera\_TorchMode torchMode)](capi-camera-manager-h.md#oh_cameramanager_settorchmode) | - | 设置相机手电筒模式。 |
| [Camera\_ErrorCode OH\_CameraManager\_GetCameraDevice(Camera\_Manager\* cameraManager, Camera\_Position position, Camera\_Type type, Camera\_Device\* camera)](capi-camera-manager-h.md#oh_cameramanager_getcameradevice) | - | 根据相机位置和相机类型查询指定的相机。 |
| [Camera\_ErrorCode OH\_CameraManager\_GetCameraDevices(Camera\_Manager\* cameraManager, Camera\_DeviceQueryInfo\* deviceQueryInfo, uint32\_t\* cameraSize, Camera\_Device\*\* cameras)](capi-camera-manager-h.md#oh_cameramanager_getcameradevices) | - | 根据相机位置、相机类型数组和连接类型查询符合条件的相机列表。 |
| [Camera\_ErrorCode OH\_CameraManager\_DeleteCameraDevices(Camera\_Manager\* cameraManager, Camera\_Device\* cameras)](capi-camera-manager-h.md#oh_cameramanager_deletecameradevices) | - | 删除指定相机设备。 |
| [Camera\_ErrorCode OH\_CameraManager\_GetCameraConcurrentInfos(Camera\_Manager\* cameraManager, const Camera\_Device\* camera, uint32\_t deviceSize, Camera\_ConcurrentInfo\*\* cameraConcurrentInfo, uint32\_t\* infoSize)](capi-camera-manager-h.md#oh_cameramanager_getcameraconcurrentinfos) | - | 获取指定相机的并发信息。 |

## 函数说明

PhonePC/2in1TabletTVWearable

### OH\_CameraManager\_StatusCallback()

PhonePC/2in1TabletTVWearable

```
1. typedef void (*OH_CameraManager_StatusCallback)(Camera_Manager* cameraManager, Camera_StatusInfo* status)
```

**描述**

在[CameraManager\_Callbacks](capi-oh-camera-cameramanager-callbacks.md)中被调用的相机管理器状态回调。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_Manager](capi-oh-camera-camera-manager.md)\* cameraManager | 传递回调的Camera\_Manager。 |
| [Camera\_StatusInfo](capi-oh-camera-camera-statusinfo.md)\* status | 每个相机设备的状态信息。 |

### OH\_CameraManager\_TorchStatusCallback()

PhonePC/2in1TabletTVWearable

```
1. typedef void (*OH_CameraManager_TorchStatusCallback)(Camera_Manager* cameraManager, Camera_TorchStatusInfo* status)
```

**描述**

手电筒状态变化回调。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_Manager](capi-oh-camera-camera-manager.md)\* cameraManager | 传递回调的Camera\_Manager。 |
| [Camera\_TorchStatusInfo](capi-oh-camera-camera-torchstatusinfo.md)\* status | 手电筒的状态信息。 |

### OH\_CameraManager\_OnFoldStatusInfoChange()

PhonePC/2in1TabletTVWearable

```
1. typedef void (*OH_CameraManager_OnFoldStatusInfoChange)(Camera_Manager* cameraManager, Camera_FoldStatusInfo* foldStatusInfo)
```

**描述**

相机管理器折叠状态信息回调。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_Manager](capi-oh-camera-camera-manager.md)\* cameraManager | 传递回调的Camera\_Manager。 |
| [Camera\_FoldStatusInfo](capi-oh-camera-camera-foldstatusinfo.md)\* foldStatusInfo | 设备的折叠状态信息。 |

### OH\_CameraManager\_RegisterCallback()

PhonePC/2in1TabletTVWearable

```
1. Camera_ErrorCode OH_CameraManager_RegisterCallback(Camera_Manager* cameraManager, CameraManager_Callbacks* callback)
```

**描述**

注册相机状态更改事件回调。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_Manager](capi-oh-camera-camera-manager.md)\* cameraManager | 相机管理器实例。 |
| [CameraManager\_Callbacks](capi-oh-camera-cameramanager-callbacks.md)\* callback | 要注册的相机设备状态回调。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。 |

### OH\_CameraManager\_UnregisterCallback()

PhonePC/2in1TabletTVWearable

```
1. Camera_ErrorCode OH_CameraManager_UnregisterCallback(Camera_Manager* cameraManager, CameraManager_Callbacks* callback)
```

**描述**

注销相机状态更改事件回调。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_Manager](capi-oh-camera-camera-manager.md)\* cameraManager | 相机管理器实例。 |
| [CameraManager\_Callbacks](capi-oh-camera-cameramanager-callbacks.md)\* callback | 要注销的相机设备状态回调。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。 |

### OH\_CameraManager\_RegisterTorchStatusCallback()

PhonePC/2in1TabletTVWearable

```
1. Camera_ErrorCode OH_CameraManager_RegisterTorchStatusCallback(Camera_Manager* cameraManager, OH_CameraManager_TorchStatusCallback torchStatusCallback)
```

**描述**

注册手电筒状态变更事件回调。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_Manager](capi-oh-camera-camera-manager.md)\* cameraManager | 相机管理器实例。 |
| [OH\_CameraManager\_TorchStatusCallback](capi-camera-manager-h.md#oh_cameramanager_torchstatuscallback) torchStatusCallback | 要注册的手电筒状态变化回调。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。 |

### OH\_CameraManager\_UnregisterTorchStatusCallback()

PhonePC/2in1TabletTVWearable

```
1. Camera_ErrorCode OH_CameraManager_UnregisterTorchStatusCallback(Camera_Manager* cameraManager, OH_CameraManager_TorchStatusCallback torchStatusCallback)
```

**描述**

注销手电筒状态变更事件回调。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_Manager](capi-oh-camera-camera-manager.md)\* cameraManager | 相机管理器实例。 |
| [OH\_CameraManager\_TorchStatusCallback](capi-camera-manager-h.md#oh_cameramanager_torchstatuscallback) torchStatusCallback | 要注销的手电筒状态变化回调。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。 |

### OH\_CameraManager\_RegisterFoldStatusInfoCallback()

PhonePC/2in1TabletTVWearable

```
1. Camera_ErrorCode OH_CameraManager_RegisterFoldStatusInfoCallback(Camera_Manager* cameraManager, OH_CameraManager_OnFoldStatusInfoChange foldStatusInfoCallback)
```

**描述**

注册折叠状态信息变更事件回调。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_Manager](capi-oh-camera-camera-manager.md)\* cameraManager | 相机管理器实例。 |
| [OH\_CameraManager\_OnFoldStatusInfoChange](capi-camera-manager-h.md#oh_cameramanager_onfoldstatusinfochange) foldStatusInfoCallback | 要注册的折叠状态信息变更事件回调。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。 |

### OH\_CameraManager\_UnregisterFoldStatusInfoCallback()

PhonePC/2in1TabletTVWearable

```
1. Camera_ErrorCode OH_CameraManager_UnregisterFoldStatusInfoCallback(Camera_Manager* cameraManager, OH_CameraManager_OnFoldStatusInfoChange foldStatusInfoCallback)
```

**描述**

注销折叠状态信息变更事件回调。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_Manager](capi-oh-camera-camera-manager.md)\* cameraManager | 相机管理器实例。 |
| [OH\_CameraManager\_OnFoldStatusInfoChange](capi-camera-manager-h.md#oh_cameramanager_onfoldstatusinfochange) foldStatusInfoCallback | 要注销的折叠状态信息变更事件回调。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。 |

### OH\_CameraManager\_GetSupportedCameras()

PhonePC/2in1TabletTVWearable

```
1. Camera_ErrorCode OH_CameraManager_GetSupportedCameras(Camera_Manager* cameraManager, Camera_Device** cameras, uint32_t* size)
```

**描述**

获取支持指定的相机设备实例。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_Manager](capi-oh-camera-camera-manager.md)\* cameraManager | 相机管理器实例。 |
| [Camera\_Device](capi-oh-camera-camera-device.md)\*\* cameras | 如果方法调用成功，将记录支持的Camera\_Device列表。 |
| uint32\_t\* size | 如果方法调用成功，将记录支持的Camera\_Device列表的大小。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。 |

### OH\_CameraManager\_DeleteSupportedCameras()

PhonePC/2in1TabletTVWearable

```
1. Camera_ErrorCode OH_CameraManager_DeleteSupportedCameras(Camera_Manager* cameraManager, Camera_Device* cameras, uint32_t size)
```

**描述**

删除支持的相机。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_Manager](capi-oh-camera-camera-manager.md)\* cameraManager | 相机管理器实例。 |
| [Camera\_Device](capi-oh-camera-camera-device.md)\* cameras | 要删除的Camera\_Device列表。 |
| uint32\_t size | 要删除的相机设备数量。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。 |

### OH\_CameraManager\_GetSupportedCameraOutputCapability()

PhonePC/2in1TabletTVWearable

```
1. Camera_ErrorCode OH_CameraManager_GetSupportedCameraOutputCapability(Camera_Manager* cameraManager, const Camera_Device* camera, Camera_OutputCapability** cameraOutputCapability)
```

**描述**

查询指定相机支持的输出能力。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_Manager](capi-oh-camera-camera-manager.md)\* cameraManager | 相机管理器实例。 |
| [const Camera\_Device](capi-oh-camera-camera-device.md)\* camera | 要查询的Camera\_Device。 |
| [Camera\_OutputCapability](capi-oh-camera-camera-outputcapability.md)\*\* cameraOutputCapability | 如果方法调用成功，将记录支持的Camera\_OutputCapability。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。 |

### OH\_CameraManager\_GetSupportedCameraOutputCapabilityWithSceneMode()

PhonePC/2in1TabletTVWearable

```
1. Camera_ErrorCode OH_CameraManager_GetSupportedCameraOutputCapabilityWithSceneMode(Camera_Manager* cameraManager, const Camera_Device* camera, Camera_SceneMode sceneMode, Camera_OutputCapability** cameraOutputCapability)
```

**描述**

查询指定相机在指定模式下支持的输出能力。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_Manager](capi-oh-camera-camera-manager.md)\* cameraManager | 相机管理器实例。 |
| [const Camera\_Device](capi-oh-camera-camera-device.md)\* camera | 要查询的Camera\_Device。 |
| [Camera\_SceneMode](capi-camera-h.md#camera_scenemode) sceneMode | 指定相机模式。 |
| [Camera\_OutputCapability](capi-oh-camera-camera-outputcapability.md)\*\* cameraOutputCapability | 如果方法调用成功，将记录支持的Camera\_OutputCapability列表。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。  CAMERA\_SERVICE\_FATAL\_ERROR：相机服务异常。 |

### OH\_CameraManager\_GetSupportedFullCameraOutputCapabilityWithSceneMode()

PhonePC/2in1TabletTVWearable

```
1. Camera_ErrorCode OH_CameraManager_GetSupportedFullCameraOutputCapabilityWithSceneMode(Camera_Manager* cameraManager, const Camera_Device* camera, Camera_SceneMode sceneMode, Camera_OutputCapability** cameraOutputCapability)
```

**描述**

查询指定相机在指定模式下支持的完整输出能力，包括未压缩图（YUV）、HEIF和HDR等能力。使用YUV，HEIF或HDR等能力前，需要先显式调用此方法确保获取完整输出能力。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_Manager](capi-oh-camera-camera-manager.md)\* cameraManager | 相机管理器实例。 |
| [const Camera\_Device](capi-oh-camera-camera-device.md)\* camera | 要查询的Camera\_Device。 |
| [Camera\_SceneMode](capi-camera-h.md#camera_scenemode) sceneMode | 指定相机模式。 |
| [Camera\_OutputCapability](capi-oh-camera-camera-outputcapability.md)\*\* cameraOutputCapability | 如果方法调用成功，将记录支持的Camera\_OutputCapability列表。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。  CAMERA\_SERVICE\_FATAL\_ERROR：相机服务异常。 |

### OH\_CameraManager\_DeleteSupportedCameraOutputCapability()

PhonePC/2in1TabletTVWearable

```
1. Camera_ErrorCode OH_CameraManager_DeleteSupportedCameraOutputCapability(Camera_Manager* cameraManager, Camera_OutputCapability* cameraOutputCapability)
```

**描述**

删除支持的输出能力。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_Manager](capi-oh-camera-camera-manager.md)\* cameraManager | 相机管理器实例。 |
| [Camera\_OutputCapability](capi-oh-camera-camera-outputcapability.md)\* cameraOutputCapability | 要删除的Camera\_OutputCapability。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。 |

### OH\_CameraManager\_IsCameraMuted()

PhonePC/2in1TabletTVWearable

```
1. Camera_ErrorCode OH_CameraManager_IsCameraMuted(Camera_Manager* cameraManager, bool* isCameraMuted)
```

**描述**

确定相机是否静音。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_Manager](capi-oh-camera-camera-manager.md)\* cameraManager | 相机管理器实例。 |
| bool\* isCameraMuted | 如果方法调用成功，将返回相机是否静音的结果。返回true表示相机已静音，返回false表示未静音。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。 |

### OH\_CameraManager\_CreateCaptureSession()

PhonePC/2in1TabletTVWearable

```
1. Camera_ErrorCode OH_CameraManager_CreateCaptureSession(Camera_Manager* cameraManager, Camera_CaptureSession** captureSession)
```

**描述**

创建捕获会话实例。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_Manager](capi-oh-camera-camera-manager.md)\* cameraManager | 相机管理器实例。 |
| [Camera\_CaptureSession](capi-oh-camera-camera-capturesession.md)\*\* captureSession | 如果方法调用成功，将创建Camera\_CaptureSession。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。  CAMERA\_SERVICE\_FATAL\_ERROR：相机服务异常。 |

### OH\_CameraManager\_CreateCameraInput()

PhonePC/2in1TabletTVWearable

```
1. Camera_ErrorCode OH_CameraManager_CreateCameraInput(Camera_Manager* cameraManager, const Camera_Device* camera, Camera_Input** cameraInput)
```

**描述**

创建相机输入实例。

**需要权限：** ohos.permission.CAMERA

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_Manager](capi-oh-camera-camera-manager.md)\* cameraManager | 相机管理器实例。 |
| [const Camera\_Device](capi-oh-camera-camera-device.md)\* camera | 用于创建Camera\_Input实例的Camera\_Device。 |
| [Camera\_Input](capi-oh-camera-camera-input.md)\*\* cameraInput | 如果方法调用成功，将创建Camera\_Input实例。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。  CAMERA\_SERVICE\_FATAL\_ERROR：相机服务异常。 |

### OH\_CameraManager\_CreateCameraInput\_WithPositionAndType()

PhonePC/2in1TabletTVWearable

```
1. Camera_ErrorCode OH_CameraManager_CreateCameraInput_WithPositionAndType(Camera_Manager* cameraManager, Camera_Position position, Camera_Type type, Camera_Input** cameraInput)
```

**描述**

创建具有位置和类型的相机输入实例。

**需要权限：** ohos.permission.CAMERA

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_Manager](capi-oh-camera-camera-manager.md)\* cameraManager | 相机管理器实例。 |
| [Camera\_Position](capi-camera-h.md#camera_position) position | 用于创建Camera\_Input实例的相机位置。 |
| [Camera\_Type](capi-camera-h.md#camera_type) type | 用于创建Camera\_Input实例的相机类型。 |
| [Camera\_Input](capi-oh-camera-camera-input.md)\*\* cameraInput | 如果方法调用成功，将创建Camera\_Input实例。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。  CAMERA\_SERVICE\_FATAL\_ERROR：相机服务异常。 |

### OH\_CameraManager\_CreatePreviewOutput()

PhonePC/2in1TabletTVWearable

```
1. Camera_ErrorCode OH_CameraManager_CreatePreviewOutput(Camera_Manager* cameraManager, const Camera_Profile* profile, const char* surfaceId, Camera_PreviewOutput** previewOutput)
```

**描述**

创建预览输出实例。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_Manager](capi-oh-camera-camera-manager.md)\* cameraManager | 相机管理器实例。 |
| [const Camera\_Profile](capi-oh-camera-camera-profile.md)\* profile | 用于创建Camera\_PreviewOutput实例的相机流配置文件。 |
| const char\* surfaceId | 用于创建Camera\_PreviewOutput实例的surfaceId。 |
| [Camera\_PreviewOutput](capi-oh-camera-camera-previewoutput.md)\*\* previewOutput | 如果方法调用成功，将创建Camera\_PreviewOutput实例。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。  CAMERA\_SERVICE\_FATAL\_ERROR：相机服务异常。 |

### OH\_CameraManager\_CreatePreviewOutputUsedInPreconfig()

PhonePC/2in1TabletTVWearable

```
1. Camera_ErrorCode OH_CameraManager_CreatePreviewOutputUsedInPreconfig(Camera_Manager* cameraManager, const char* surfaceId, Camera_PreviewOutput** previewOutput)
```

**描述**

创建在预配置流中使用的预览输出实例。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_Manager](capi-oh-camera-camera-manager.md)\* cameraManager | 相机管理器实例。 |
| const char\* surfaceId | 用于创建Camera\_PreviewOutput实例的surfaceId。 |
| [Camera\_PreviewOutput](capi-oh-camera-camera-previewoutput.md)\*\* previewOutput | 如果方法调用成功，将创建Camera\_PreviewOutput实例。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。  CAMERA\_SERVICE\_FATAL\_ERROR：相机服务异常。 |

### OH\_CameraManager\_CreatePhotoOutput()

PhonePC/2in1TabletTVWearable

```
1. Camera_ErrorCode OH_CameraManager_CreatePhotoOutput(Camera_Manager* cameraManager, const Camera_Profile* profile, const char* surfaceId, Camera_PhotoOutput** photoOutput)
```

**描述**

创建一个拍照输出实例。该接口只支持创建JPEG格式的拍照输出对象。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_Manager](capi-oh-camera-camera-manager.md)\* cameraManager | 相机管理器实例。 |
| [const Camera\_Profile](capi-oh-camera-camera-profile.md)\* profile | 用于创建Camera\_PhotoOutput实例的相机流配置文件。 |
| const char\* surfaceId | 用于创建Camera\_PhotoOutput实例的surfaceId。 |
| [Camera\_PhotoOutput](capi-oh-camera-camera-photooutput.md)\*\* photoOutput | 如果方法调用成功，将创建Camera\_PhotoOutput实例。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。  CAMERA\_SERVICE\_FATAL\_ERROR：相机服务异常。 |

### OH\_CameraManager\_CreatePhotoOutputUsedInPreconfig()

PhonePC/2in1TabletTVWearable

```
1. Camera_ErrorCode OH_CameraManager_CreatePhotoOutputUsedInPreconfig(Camera_Manager* cameraManager, const char* surfaceId, Camera_PhotoOutput** photoOutput)
```

**描述**

创建在预配置流中使用的照片输出实例。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_Manager](capi-oh-camera-camera-manager.md)\* cameraManager | 相机管理器实例。 |
| const char\* surfaceId | 用于创建Camera\_PhotoOutput实例的surfaceId。 |
| [Camera\_PhotoOutput](capi-oh-camera-camera-photooutput.md)\*\* photoOutput | 如果方法调用成功，将创建Camera\_PhotoOutput实例。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。  CAMERA\_SERVICE\_FATAL\_ERROR：相机服务异常。 |

### OH\_CameraManager\_CreatePhotoOutputWithoutSurface()

PhonePC/2in1TabletTVWearable

```
1. Camera_ErrorCode OH_CameraManager_CreatePhotoOutputWithoutSurface(Camera_Manager *cameraManager, const Camera_Profile *profile, Camera_PhotoOutput **photoOutput)
```

**描述**

创建照片输出实例，调用此函数不需要surfaceId。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_Manager](capi-oh-camera-camera-manager.md) \*cameraManager | 相机管理器实例。 |
| [const Camera\_Profile](capi-oh-camera-camera-profile.md) \*profile | 用于创建Camera\_PhotoOutput实例的相机流配置文件。 |
| [Camera\_PhotoOutput](capi-oh-camera-camera-photooutput.md) \*\*photoOutput | 如果方法调用成功，将创建Camera\_PhotoOutput实例。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。  CAMERA\_SERVICE\_FATAL\_ERROR：相机服务异常。 |

### OH\_CameraManager\_CreateVideoOutput()

PhonePC/2in1TabletTVWearable

```
1. Camera_ErrorCode OH_CameraManager_CreateVideoOutput(Camera_Manager* cameraManager, const Camera_VideoProfile* profile, const char* surfaceId, Camera_VideoOutput** videoOutput)
```

**描述**

创建一个录像输出实例。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_Manager](capi-oh-camera-camera-manager.md)\* cameraManager | 相机管理器实例。 |
| [const Camera\_VideoProfile](capi-oh-camera-camera-videoprofile.md)\* profile | 用于创建Camera\_VideoOutput实例的录像配置文件。 |
| const char\* surfaceId | 用于创建Camera\_VideoOutput实例的surfaceId。 |
| [Camera\_VideoOutput](capi-oh-camera-camera-videooutput.md)\*\* videoOutput | 如果方法调用成功，将创建Camera\_VideoOutput实例。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。  CAMERA\_SERVICE\_FATAL\_ERROR：相机服务异常。 |

### OH\_CameraManager\_CreateVideoOutputUsedInPreconfig()

PhonePC/2in1TabletTVWearable

```
1. Camera_ErrorCode OH_CameraManager_CreateVideoOutputUsedInPreconfig(Camera_Manager* cameraManager, const char* surfaceId, Camera_VideoOutput** videoOutput)
```

**描述**

创建在预配置流中使用的视频输出实例。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_Manager](capi-oh-camera-camera-manager.md)\* cameraManager | 相机管理器实例。 |
| const char\* surfaceId | 用于创建Camera\_VideoOutput实例的surfaceId。 |
| [Camera\_VideoOutput](capi-oh-camera-camera-videooutput.md)\*\* videoOutput | 如果方法调用成功，将创建Camera\_VideoOutput实例。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。  CAMERA\_SERVICE\_FATAL\_ERROR：相机服务异常。 |

### OH\_CameraManager\_CreateMetadataOutput()

PhonePC/2in1TabletTVWearable

```
1. Camera_ErrorCode OH_CameraManager_CreateMetadataOutput(Camera_Manager* cameraManager, const Camera_MetadataObjectType* profile, Camera_MetadataOutput** metadataOutput)
```

**描述**

创建元数据输出实例。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_Manager](capi-oh-camera-camera-manager.md)\* cameraManager | 相机管理器实例。 |
| [const Camera\_MetadataObjectType](capi-camera-h.md#camera_metadataobjecttype)\* profile | 用于创建Camera\_MetadataOutput实例的元数据对象类型。 |
| [Camera\_MetadataOutput](capi-oh-camera-camera-metadataoutput.md)\*\* metadataOutput | 如果方法调用成功，将创建Camera\_MetadataOutput实例。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。  CAMERA\_SERVICE\_FATAL\_ERROR：相机服务异常。 |

### OH\_CameraManager\_CreateMetadataOutputWithObjectTypes()

PhonePC/2in1TabletTVWearable

```
1. Camera_ErrorCode OH_CameraManager_CreateMetadataOutputWithObjectTypes(Camera_Manager* cameraManager, const Camera_MetadataObjectType* metadataObjectTypes, uint32_t size, Camera_MetadataOutput** metadataOutput)
```

**描述**

使用元数据对象类型数组创建元数据输出实例。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_Manager](capi-oh-camera-camera-manager.md)\* cameraManager | 相机管理器实例。 |
| [const Camera\_MetadataObjectType](capi-camera-h.md#camera_metadataobjecttype)\* metadataObjectTypes | 用于创建Camera\_MetadataOutput实例的元数据对象类型数组。 |
| uint32\_t size | 元数据对象类型数组长度。 |
| [Camera\_MetadataOutput](capi-oh-camera-camera-metadataoutput.md)\*\* metadataOutput | 如果方法调用成功，将创建Camera\_MetadataOutput实例。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。  CAMERA\_SERVICE\_FATAL\_ERROR：相机服务异常。 |

### OH\_CameraManager\_GetSupportedSceneModes()

PhonePC/2in1TabletTVWearable

```
1. Camera_ErrorCode OH_CameraManager_GetSupportedSceneModes(Camera_Device* camera, Camera_SceneMode** sceneModes, uint32_t* size)
```

**描述**

获取特定相机支持的场景模式。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_Device](capi-oh-camera-camera-device.md)\* camera | 要查询的Camera\_Device。 |
| [Camera\_SceneMode](capi-camera-h.md#camera_scenemode)\*\* sceneModes | 如果方法调用成功，将记录支持的场景模式列表。 |
| uint32\_t\* size | 如果方法调用成功，将记录支持的场景模式列表大小。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。  CAMERA\_SERVICE\_FATAL\_ERROR：相机服务异常。 |

### OH\_CameraManager\_DeleteSceneModes()

PhonePC/2in1TabletTVWearable

```
1. Camera_ErrorCode OH_CameraManager_DeleteSceneModes(Camera_Manager* cameraManager, Camera_SceneMode* sceneModes)
```

**描述**

删除场景模式。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_Manager](capi-oh-camera-camera-manager.md)\* cameraManager | 相机管理器实例。 |
| [Camera\_SceneMode](capi-camera-h.md#camera_scenemode)\* sceneModes | 要删除的场景模式列表。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。 |

### OH\_CameraManager\_IsTorchSupported()

PhonePC/2in1TabletTVWearable

```
1. Camera_ErrorCode OH_CameraManager_IsTorchSupported(Camera_Manager* cameraManager, bool* isTorchSupported)
```

**描述**

检查设备是否支持手电筒。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_Manager](capi-oh-camera-camera-manager.md)\* cameraManager | 相机管理器实例。 |
| bool\* isTorchSupported | 设备是否支持手电筒。返回true表示设备支持手电筒，返回false表示不支持。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。 |

### OH\_CameraManager\_IsTorchSupportedByTorchMode()

PhonePC/2in1TabletTVWearable

```
1. Camera_ErrorCode OH_CameraManager_IsTorchSupportedByTorchMode(Camera_Manager* cameraManager, Camera_TorchMode torchMode, bool* isTorchSupported)
```

**描述**

检查设备是否支持指定的手电筒模式。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_Manager](capi-oh-camera-camera-manager.md)\* cameraManager | 相机管理器实例。 |
| [Camera\_TorchMode](capi-camera-h.md#camera_torchmode) torchMode | 要检查的相机手电筒模式。 |
| bool\* isTorchSupported | 设备是否支持指定的手电筒模式。返回true表示设备支持该模式，返回false表示不支持。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。  CAMERA\_SERVICE\_FATAL\_ERROR：相机服务异常。 |

### OH\_CameraManager\_SetTorchMode()

PhonePC/2in1TabletTVWearable

```
1. Camera_ErrorCode OH_CameraManager_SetTorchMode(Camera_Manager* cameraManager, Camera_TorchMode torchMode)
```

**描述**

设置相机手电筒模式。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_Manager](capi-oh-camera-camera-manager.md)\* cameraManager | 相机管理器实例。 |
| [Camera\_TorchMode](capi-camera-h.md#camera_torchmode) torchMode | 要设置的相机手电筒模式。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。  CAMERA\_SERVICE\_FATAL\_ERROR：相机服务异常。 |

### OH\_CameraManager\_GetCameraDevice()

PhonePC/2in1TabletTVWearable

```
1. Camera_ErrorCode OH_CameraManager_GetCameraDevice(Camera_Manager* cameraManager, Camera_Position position, Camera_Type type, Camera_Device* camera)
```

**描述**

根据相机位置和相机类型查询指定的相机。

获取指定[Camera\_Position](capi-camera-h.md#camera_position)和[Camera\_Type](capi-camera-h.md#camera_type)的相机镜头，如果该接口返回值为CAMERA\_SERVICE\_FATAL\_ERROR，表示当前设备未查询到该镜头。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_Manager](capi-oh-camera-camera-manager.md)\* cameraManager | 相机管理器实例。 |
| [Camera\_Position](capi-camera-h.md#camera_position) position | 要查询的相机位置。 |
| [Camera\_Type](capi-camera-h.md#camera_type) type | 要查询的相机类型。 |
| [Camera\_Device](capi-oh-camera-camera-device.md)\* camera | 要查询的Camera\_Device。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。  CAMERA\_SERVICE\_FATAL\_ERROR：相机服务异常。 |

### OH\_CameraManager\_GetCameraDevices()

PhonePC/2in1TabletTVWearable

```
1. Camera_ErrorCode OH_CameraManager_GetCameraDevices(Camera_Manager* cameraManager, Camera_DeviceQueryInfo* deviceQueryInfo, uint32_t* cameraSize, Camera_Device** cameras)
```

**描述**

根据相机位置、相机类型数组和连接类型查询符合条件的相机列表。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_Manager](capi-oh-camera-camera-manager.md)\* cameraManager | 相机管理器实例。 |
| [Camera\_DeviceQueryInfo](capi-oh-camera-camera-devicequeryinfo.md)\* deviceQueryInfo | 相机设备的查询信息实例。 |
| uint32\_t\* cameraSize | 查询的所支持的Camera\_Device列表大小。 |
| [Camera\_Device](capi-oh-camera-camera-device.md)\*\* cameras | 查询的所支持的Camera\_Device列表。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。  CAMERA\_SERVICE\_FATAL\_ERROR：相机服务异常。 |

### OH\_CameraManager\_DeleteCameraDevices()

PhonePC/2in1TabletTVWearable

```
1. Camera_ErrorCode OH_CameraManager_DeleteCameraDevices(Camera_Manager* cameraManager, Camera_Device* cameras)
```

**描述**

删除指定相机设备。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_Manager](capi-oh-camera-camera-manager.md)\* cameraManager | 相机管理器实例。 |
| [Camera\_Device](capi-oh-camera-camera-device.md)\* cameras | 待删除的Camera\_Device列表。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。 |

### OH\_CameraManager\_GetCameraConcurrentInfos()

PhonePC/2in1TabletTVWearable

```
1. Camera_ErrorCode OH_CameraManager_GetCameraConcurrentInfos(Camera_Manager* cameraManager, const Camera_Device* camera, uint32_t deviceSize, Camera_ConcurrentInfo** cameraConcurrentInfo, uint32_t* infoSize)
```

**描述**

获取指定相机的并发信息。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_Manager](capi-oh-camera-camera-manager.md)\* cameraManager | 相机管理器实例。 |
| [const Camera\_Device](capi-oh-camera-camera-device.md)\* camera | 用于查询的Camera\_Device相机设备列表，推荐设置为包含[OH\_CameraManager\_GetCameraDevice](capi-camera-manager-h.md#oh_cameramanager_getcameradevice)获取的前置与后置两个相机设备的相机设备列表。 |
| uint32\_t deviceSize | 用于查询的相机设备列表长度, 必须设置为2（表示前置与后置两个用于并发的相机设备）。 |
| [Camera\_ConcurrentInfo](capi-oh-camera-camera-concurrentinfo.md)\*\* cameraConcurrentInfo | 查询到的相机并发能力数组Camera\_ConcurrentInfo，作为入参应当默认设置为空。  如果相机支持并发，cameraConcurrentInfo会被赋值为查询到的相机并发能力数组Camera\_ConcurrentInfo。  如果相机不支持并发，不会对cameraConcurrentInfo进行更改，并且返回错误码[Camera\_ErrorCode](capi-camera-h.md#camera_errorcode).CAMERA\_SERVICE\_FATAL\_ERROR。 |
| uint32\_t\* infoSize | 查询到的相机并发能力数组长度，作为入参应当默认设置为0。  如果相机支持并发，infoSize会被赋值为查询到的相机并发能力数组长度。  如果相机不支持并发，不会对infoSize进行更改，并且返回错误码[Camera\_ErrorCode](capi-camera-h.md#camera_errorcode).CAMERA\_SERVICE\_FATAL\_ERROR。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。  CAMERA\_SERVICE\_FATAL\_ERROR：相机服务异常，或者相机不支持并发。 |
