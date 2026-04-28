---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-photo-output-h
title: photo_output.h
breadcrumb: API参考 > 媒体 > Camera Kit（相机服务） > C API > 头文件 > photo_output.h
category: harmonyos-references
scraped_at: 2026-04-28T08:12:46+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:0c772d1231afa8b223024cf7ef431bac87f9a57661222b2db5ee40e9c2acea60
---

## 概述

PhonePC/2in1TabletTVWearable

声明拍照输出概念。

**引用文件：** <ohcamera/photo\_output.h>

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
| [PhotoOutput\_Callbacks](capi-oh-camera-photooutput-callbacks.md) | PhotoOutput\_Callbacks | 拍照输出的回调。 |
| [Camera\_PhotoOutput](capi-oh-camera-camera-photooutput.md) | Camera\_PhotoOutput | 拍照输出对象。  可以使用[OH\_CameraManager\_CreatePhotoOutput](capi-camera-manager-h.md#oh_cameramanager_createphotooutput)方法创建指针。 |

### 函数

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [typedef void (\*OH\_PhotoOutput\_OnFrameStart)(Camera\_PhotoOutput\* photoOutput)](capi-photo-output-h.md#oh_photooutput_onframestart) | OH\_PhotoOutput\_OnFrameStart | 在[PhotoOutput\_Callbacks](capi-oh-camera-photooutput-callbacks.md)中被调用的拍照输出帧启动回调。 |
| [typedef void (\*OH\_PhotoOutput\_OnFrameShutter)(Camera\_PhotoOutput\* photoOutput, Camera\_FrameShutterInfo\* info)](capi-photo-output-h.md#oh_photooutput_onframeshutter) | OH\_PhotoOutput\_OnFrameShutter | 在[PhotoOutput\_Callbacks](capi-oh-camera-photooutput-callbacks.md)中被调用的拍照输出帧快门回调。 |
| [typedef void (\*OH\_PhotoOutput\_OnFrameEnd)(Camera\_PhotoOutput\* photoOutput, int32\_t frameCount)](capi-photo-output-h.md#oh_photooutput_onframeend) | OH\_PhotoOutput\_OnFrameEnd | 在[PhotoOutput\_Callbacks](capi-oh-camera-photooutput-callbacks.md)中被调用的拍照输出帧结束回调。 |
| [typedef void (\*OH\_PhotoOutput\_OnError)(Camera\_PhotoOutput\* photoOutput, Camera\_ErrorCode errorCode)](capi-photo-output-h.md#oh_photooutput_onerror) | OH\_PhotoOutput\_OnError | 在[PhotoOutput\_Callbacks](capi-oh-camera-photooutput-callbacks.md)中被调用的拍照输出错误回调。 |
| [typedef void (\*OH\_PhotoOutput\_CaptureEnd)(Camera\_PhotoOutput\* photoOutput, int32\_t frameCount)](capi-photo-output-h.md#oh_photooutput_captureend) | OH\_PhotoOutput\_CaptureEnd | 拍照结束回调。 |
| [typedef void (\*OH\_PhotoOutput\_CaptureStartWithInfo)(Camera\_PhotoOutput\* photoOutput, Camera\_CaptureStartInfo\* Info)](capi-photo-output-h.md#oh_photooutput_capturestartwithinfo) | OH\_PhotoOutput\_CaptureStartWithInfo | 拍照开始回调。 |
| [typedef void (\*OH\_PhotoOutput\_OnFrameShutterEnd)(Camera\_PhotoOutput\* photoOutput, Camera\_FrameShutterInfo\* Info)](capi-photo-output-h.md#oh_photooutput_onframeshutterend) | OH\_PhotoOutput\_OnFrameShutterEnd | 拍照曝光结束回调。 |
| [typedef void (\*OH\_PhotoOutput\_CaptureReady)(Camera\_PhotoOutput\* photoOutput)](capi-photo-output-h.md#oh_photooutput_captureready) | OH\_PhotoOutput\_CaptureReady | 拍照准备就绪回调。收到回调后，可以继续进行下一次拍照。 |
| [typedef void (\*OH\_PhotoOutput\_EstimatedCaptureDuration)(Camera\_PhotoOutput\* photoOutput, int64\_t duration)](capi-photo-output-h.md#oh_photooutput_estimatedcaptureduration) | OH\_PhotoOutput\_EstimatedCaptureDuration | 预计拍照时间回调。 |
| [typedef void (\*OH\_PhotoOutput\_PhotoAvailable)(Camera\_PhotoOutput\* photoOutput, OH\_PhotoNative\* photo)](capi-photo-output-h.md#oh_photooutput_photoavailable) | OH\_PhotoOutput\_PhotoAvailable | 照片输出可用高分辨率图像回调。 |
| [typedef void (\*OH\_PhotoOutput\_PhotoAssetAvailable)(Camera\_PhotoOutput\* photoOutput, OH\_MediaAsset\* photoAsset)](capi-photo-output-h.md#oh_photooutput_photoassetavailable) | OH\_PhotoOutput\_PhotoAssetAvailable | 输出照片资源可用回调。 |
| [Camera\_ErrorCode OH\_PhotoOutput\_RegisterCallback(Camera\_PhotoOutput\* photoOutput, PhotoOutput\_Callbacks\* callback)](capi-photo-output-h.md#oh_photooutput_registercallback) | - | 注册拍照输出更改事件回调。 |
| [Camera\_ErrorCode OH\_PhotoOutput\_UnregisterCallback(Camera\_PhotoOutput\* photoOutput, PhotoOutput\_Callbacks\* callback)](capi-photo-output-h.md#oh_photooutput_unregistercallback) | - | 注销拍照输出更改事件回调。 |
| [Camera\_ErrorCode OH\_PhotoOutput\_RegisterCaptureStartWithInfoCallback(Camera\_PhotoOutput\* photoOutput, OH\_PhotoOutput\_CaptureStartWithInfo callback)](capi-photo-output-h.md#oh_photooutput_registercapturestartwithinfocallback) | - | 注册拍照开始事件回调。 |
| [Camera\_ErrorCode OH\_PhotoOutput\_GetPhotoRotation(Camera\_PhotoOutput\* photoOutput, int deviceDegree, Camera\_ImageRotation\* imageRotation)](capi-photo-output-h.md#oh_photooutput_getphotorotation) | - | 获取照片旋转角度。 |
| [Camera\_ErrorCode OH\_PhotoOutput\_GetPhotoRotationWithoutDeviceDegree(Camera\_PhotoOutput\* photoOutput, Camera\_ImageRotation\* imageRotation)](capi-photo-output-h.md#oh_photooutput_getphotorotationwithoutdevicedegree) | - | 获取照片旋转角度。 |
| [Camera\_ErrorCode OH\_PhotoOutput\_UnregisterCaptureStartWithInfoCallback(Camera\_PhotoOutput\* photoOutput, OH\_PhotoOutput\_CaptureStartWithInfo callback)](capi-photo-output-h.md#oh_photooutput_unregistercapturestartwithinfocallback) | - | 注销拍照开始事件回调。 |
| [Camera\_ErrorCode OH\_PhotoOutput\_RegisterCaptureEndCallback(Camera\_PhotoOutput\* photoOutput, OH\_PhotoOutput\_CaptureEnd callback)](capi-photo-output-h.md#oh_photooutput_registercaptureendcallback) | - | 注册拍照结束事件回调。 |
| [Camera\_ErrorCode OH\_PhotoOutput\_UnregisterCaptureEndCallback(Camera\_PhotoOutput\* photoOutput, OH\_PhotoOutput\_CaptureEnd callback)](capi-photo-output-h.md#oh_photooutput_unregistercaptureendcallback) | - | 注销拍照结束事件回调。 |
| [Camera\_ErrorCode OH\_PhotoOutput\_RegisterFrameShutterEndCallback(Camera\_PhotoOutput\* photoOutput, OH\_PhotoOutput\_OnFrameShutterEnd callback)](capi-photo-output-h.md#oh_photooutput_registerframeshutterendcallback) | - | 注册拍照曝光结束事件回调。 |
| [Camera\_ErrorCode OH\_PhotoOutput\_UnregisterFrameShutterEndCallback(Camera\_PhotoOutput\* photoOutput, OH\_PhotoOutput\_OnFrameShutterEnd callback)](capi-photo-output-h.md#oh_photooutput_unregisterframeshutterendcallback) | - | 注销拍照曝光结束事件回调。 |
| [Camera\_ErrorCode OH\_PhotoOutput\_RegisterCaptureReadyCallback(Camera\_PhotoOutput\* photoOutput, OH\_PhotoOutput\_CaptureReady callback)](capi-photo-output-h.md#oh_photooutput_registercapturereadycallback) | - | 注册拍照就绪事件回调。收到回调后，可以继续进行下一次拍照。 |
| [Camera\_ErrorCode OH\_PhotoOutput\_UnregisterCaptureReadyCallback(Camera\_PhotoOutput\* photoOutput, OH\_PhotoOutput\_CaptureReady callback)](capi-photo-output-h.md#oh_photooutput_unregistercapturereadycallback) | - | 注销拍照就绪事件回调。 |
| [Camera\_ErrorCode OH\_PhotoOutput\_RegisterEstimatedCaptureDurationCallback(Camera\_PhotoOutput\* photoOutput, OH\_PhotoOutput\_EstimatedCaptureDuration callback)](capi-photo-output-h.md#oh_photooutput_registerestimatedcapturedurationcallback) | - | 注册预计拍照时间事件回调。 |
| [Camera\_ErrorCode OH\_PhotoOutput\_UnregisterEstimatedCaptureDurationCallback(Camera\_PhotoOutput\* photoOutput, OH\_PhotoOutput\_EstimatedCaptureDuration callback)](capi-photo-output-h.md#oh_photooutput_unregisterestimatedcapturedurationcallback) | - | 注销预计拍照时间事件回调。 |
| [Camera\_ErrorCode OH\_PhotoOutput\_RegisterPhotoAvailableCallback(Camera\_PhotoOutput\* photoOutput, OH\_PhotoOutput\_PhotoAvailable callback)](capi-photo-output-h.md#oh_photooutput_registerphotoavailablecallback) | - | 注册输出照片可用回调。 |
| [Camera\_ErrorCode OH\_PhotoOutput\_UnregisterPhotoAvailableCallback(Camera\_PhotoOutput\* photoOutput, OH\_PhotoOutput\_PhotoAvailable callback)](capi-photo-output-h.md#oh_photooutput_unregisterphotoavailablecallback) | - | 注销输出照片可用回调。 |
| [Camera\_ErrorCode OH\_PhotoOutput\_RegisterPhotoAssetAvailableCallback(Camera\_PhotoOutput\* photoOutput, OH\_PhotoOutput\_PhotoAssetAvailable callback)](capi-photo-output-h.md#oh_photooutput_registerphotoassetavailablecallback) | - | 注册输出照片资源可用回调。 |
| [Camera\_ErrorCode OH\_PhotoOutput\_UnregisterPhotoAssetAvailableCallback(Camera\_PhotoOutput\* photoOutput, OH\_PhotoOutput\_PhotoAssetAvailable callback)](capi-photo-output-h.md#oh_photooutput_unregisterphotoassetavailablecallback) | - | 注销输出照片资源可用回调。 |
| [Camera\_ErrorCode OH\_PhotoOutput\_Capture(Camera\_PhotoOutput\* photoOutput)](capi-photo-output-h.md#oh_photooutput_capture) | - | 拍摄照片。  必须在[OH\_PreviewOutput\_Release](capi-preview-output-h.md#oh_previewoutput_release)之前调用，否则会导致无法拍照。 |
| [Camera\_ErrorCode OH\_PhotoOutput\_Capture\_WithCaptureSetting(Camera\_PhotoOutput\* photoOutput, Camera\_PhotoCaptureSetting setting)](capi-photo-output-h.md#oh_photooutput_capture_withcapturesetting) | - | 使用捕获设置捕获拍照。 |
| [Camera\_ErrorCode OH\_PhotoOutput\_Release(Camera\_PhotoOutput\* photoOutput)](capi-photo-output-h.md#oh_photooutput_release) | - | 释放拍照输出。 |
| [Camera\_ErrorCode OH\_PhotoOutput\_IsMirrorSupported(Camera\_PhotoOutput\* photoOutput, bool\* isSupported)](capi-photo-output-h.md#oh_photooutput_ismirrorsupported) | - | 检查是否支持镜像拍照。 |
| [Camera\_ErrorCode OH\_PhotoOutput\_EnableMirror(Camera\_PhotoOutput\* photoOutput, bool enabled)](capi-photo-output-h.md#oh_photooutput_enablemirror) | - | 是否启用动态照片镜像拍照。 |
| [Camera\_ErrorCode OH\_PhotoOutput\_GetActiveProfile(Camera\_PhotoOutput\* photoOutput, Camera\_Profile\*\* profile)](capi-photo-output-h.md#oh_photooutput_getactiveprofile) | - | 获取当前照片输出配置文件。 |
| [Camera\_ErrorCode OH\_PhotoOutput\_DeleteProfile(Camera\_Profile\* profile)](capi-photo-output-h.md#oh_photooutput_deleteprofile) | - | 删除照片配置文件实例。 |
| [Camera\_ErrorCode OH\_PhotoOutput\_IsMovingPhotoSupported(Camera\_PhotoOutput\* photoOutput, bool\* isSupported)](capi-photo-output-h.md#oh_photooutput_ismovingphotosupported) | - | 检查是否支持动态照片。 |
| [Camera\_ErrorCode OH\_PhotoOutput\_EnableMovingPhoto(Camera\_PhotoOutput\* photoOutput, bool enabled)](capi-photo-output-h.md#oh_photooutput_enablemovingphoto) | - | 是否启用动态照片。 |
| [Camera\_ErrorCode OH\_PhotoOutput\_IsPhotoQualityPrioritizationSupported(Camera\_PhotoOutput\* photoOutput, Camera\_PhotoQualityPrioritization qualityPrioritization, bool\* isSupported)](capi-photo-output-h.md#oh_photooutput_isphotoqualityprioritizationsupported) | - | 检查是否支持指定的拍照画质优先策略。 |
| [Camera\_ErrorCode OH\_PhotoOutput\_SetPhotoQualityPrioritization(Camera\_PhotoOutput\* photoOutput, Camera\_PhotoQualityPrioritization qualityPrioritization)](capi-photo-output-h.md#oh_photooutput_setphotoqualityprioritization) | - | 设置拍照画质优先策略。 |

## 函数说明

PhonePC/2in1TabletTVWearable

### OH\_PhotoOutput\_OnFrameStart()

PhonePC/2in1TabletTVWearable

```
1. typedef void (*OH_PhotoOutput_OnFrameStart)(Camera_PhotoOutput* photoOutput)
```

**描述**

在[PhotoOutput\_Callbacks](capi-oh-camera-photooutput-callbacks.md)中被调用的拍照输出帧启动回调。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_PhotoOutput](capi-oh-camera-camera-photooutput.md)\* photoOutput | 传递回调的拍照输出实例。 |

### OH\_PhotoOutput\_OnFrameShutter()

PhonePC/2in1TabletTVWearable

```
1. typedef void (*OH_PhotoOutput_OnFrameShutter)(Camera_PhotoOutput* photoOutput, Camera_FrameShutterInfo* info)
```

**描述**

在[PhotoOutput\_Callbacks](capi-oh-camera-photooutput-callbacks.md)中被调用的拍照输出帧快门回调。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_PhotoOutput](capi-oh-camera-camera-photooutput.md)\* photoOutput | 传递回调的拍照输出实例。 |
| [Camera\_FrameShutterInfo](capi-oh-camera-camera-frameshutterinfo.md)\* info | 回调传递的帧快门回调信息。 |

### OH\_PhotoOutput\_OnFrameEnd()

PhonePC/2in1TabletTVWearable

```
1. typedef void (*OH_PhotoOutput_OnFrameEnd)(Camera_PhotoOutput* photoOutput, int32_t frameCount)
```

**描述**

在[PhotoOutput\_Callbacks](capi-oh-camera-photooutput-callbacks.md)中被调用的拍照输出帧结束回调。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_PhotoOutput](capi-oh-camera-camera-photooutput.md)\* photoOutput | 传递回调的拍照输出实例。 |
| int32\_t frameCount | 回调传递的帧计数。 |

### OH\_PhotoOutput\_OnError()

PhonePC/2in1TabletTVWearable

```
1. typedef void (*OH_PhotoOutput_OnError)(Camera_PhotoOutput* photoOutput, Camera_ErrorCode errorCode)
```

**描述**

在[PhotoOutput\_Callbacks](capi-oh-camera-photooutput-callbacks.md)中被调用的拍照输出错误回调。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_PhotoOutput](capi-oh-camera-camera-photooutput.md)\* photoOutput | 传递回调的拍照输出实例。 |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) errorCode | 拍照输出的错误码。 |

**参考：**

[CAMERA\_SERVICE\_FATAL\_ERROR](capi-camera-h.md#camera_errorcode)

### OH\_PhotoOutput\_CaptureEnd()

PhonePC/2in1TabletTVWearable

```
1. typedef void (*OH_PhotoOutput_CaptureEnd)(Camera_PhotoOutput* photoOutput, int32_t frameCount)
```

**描述**

拍照结束回调。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_PhotoOutput](capi-oh-camera-camera-photooutput.md)\* photoOutput | 传递回调的拍照输出实例。 |
| int32\_t frameCount | 回调传递的帧数。 |

### OH\_PhotoOutput\_CaptureStartWithInfo()

PhonePC/2in1TabletTVWearable

```
1. typedef void (*OH_PhotoOutput_CaptureStartWithInfo)(Camera_PhotoOutput* photoOutput, Camera_CaptureStartInfo* Info)
```

**描述**

拍照开始回调。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_PhotoOutput](capi-oh-camera-camera-photooutput.md)\* photoOutput | 传递回调的拍照输出实例。 |
| [Camera\_CaptureStartInfo](capi-oh-camera-camera-capturestartinfo.md)\* Info | 回调传递的拍照开始信息。 |

### OH\_PhotoOutput\_OnFrameShutterEnd()

PhonePC/2in1TabletTVWearable

```
1. typedef void (*OH_PhotoOutput_OnFrameShutterEnd)(Camera_PhotoOutput* photoOutput, Camera_FrameShutterInfo* Info)
```

**描述**

拍照曝光结束回调。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_PhotoOutput](capi-oh-camera-camera-photooutput.md)\* photoOutput | 传递回调的拍照输出实例。 |
| [Camera\_FrameShutterInfo](capi-oh-camera-camera-frameshutterinfo.md)\* Info | 回调传递的帧快门回调信息。 |

### OH\_PhotoOutput\_CaptureReady()

PhonePC/2in1TabletTVWearable

```
1. typedef void (*OH_PhotoOutput_CaptureReady)(Camera_PhotoOutput* photoOutput)
```

**描述**

拍照准备就绪回调。收到回调后，可以继续进行下一次拍照。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_PhotoOutput](capi-oh-camera-camera-photooutput.md)\* photoOutput | 传递回调的拍照输出实例。 |

### OH\_PhotoOutput\_EstimatedCaptureDuration()

PhonePC/2in1TabletTVWearable

```
1. typedef void (*OH_PhotoOutput_EstimatedCaptureDuration)(Camera_PhotoOutput* photoOutput, int64_t duration)
```

**描述**

预计拍照时间回调。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_PhotoOutput](capi-oh-camera-camera-photooutput.md)\* photoOutput | 传递回调的拍照输出实例。 |
| int64\_t duration | 回调传递的预计拍照时间，单位毫秒。 |

### OH\_PhotoOutput\_PhotoAvailable()

PhonePC/2in1TabletTVWearable

```
1. typedef void (*OH_PhotoOutput_PhotoAvailable)(Camera_PhotoOutput* photoOutput, OH_PhotoNative* photo)
```

**描述**

照片输出可用高分辨率图像回调。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_PhotoOutput](capi-oh-camera-camera-photooutput.md)\* photoOutput | 传递回调的拍照输出实例。 |
| [OH\_PhotoNative](capi-oh-camera-oh-photonative.md)\* photo | 回调传递的OH\_PhotoNative。 |

### OH\_PhotoOutput\_PhotoAssetAvailable()

PhonePC/2in1TabletTVWearable

```
1. typedef void (*OH_PhotoOutput_PhotoAssetAvailable)(Camera_PhotoOutput* photoOutput, OH_MediaAsset* photoAsset)
```

**描述**

输出照片资源可用回调。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_PhotoOutput](capi-oh-camera-camera-photooutput.md)\* photoOutput | 传递回调的拍照输出实例。 |
| [OH\_MediaAsset](capi-mediaassetmanager-oh-mediaasset.md)\* photoAsset | 回调传递的媒体资源。 |

### OH\_PhotoOutput\_RegisterCallback()

PhonePC/2in1TabletTVWearable

```
1. Camera_ErrorCode OH_PhotoOutput_RegisterCallback(Camera_PhotoOutput* photoOutput, PhotoOutput_Callbacks* callback)
```

**描述**

注册拍照输出更改事件回调。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_PhotoOutput](capi-oh-camera-camera-photooutput.md)\* photoOutput | 拍照输出实例。 |
| [PhotoOutput\_Callbacks](capi-oh-camera-photooutput-callbacks.md)\* callback | 要注册的拍照输出更改事件回调。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。 |

### OH\_PhotoOutput\_UnregisterCallback()

PhonePC/2in1TabletTVWearable

```
1. Camera_ErrorCode OH_PhotoOutput_UnregisterCallback(Camera_PhotoOutput* photoOutput, PhotoOutput_Callbacks* callback)
```

**描述**

注销拍照输出更改事件回调。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_PhotoOutput](capi-oh-camera-camera-photooutput.md)\* photoOutput | 拍照输出实例。 |
| [PhotoOutput\_Callbacks](capi-oh-camera-photooutput-callbacks.md)\* callback | 要注销的拍照输出更改事件回调。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。 |

### OH\_PhotoOutput\_RegisterCaptureStartWithInfoCallback()

PhonePC/2in1TabletTVWearable

```
1. Camera_ErrorCode OH_PhotoOutput_RegisterCaptureStartWithInfoCallback(Camera_PhotoOutput* photoOutput, OH_PhotoOutput_CaptureStartWithInfo callback)
```

**描述**

注册拍照开始事件回调。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_PhotoOutput](capi-oh-camera-camera-photooutput.md)\* photoOutput | 拍照输出实例。 |
| [OH\_PhotoOutput\_CaptureStartWithInfo](capi-photo-output-h.md#oh_photooutput_capturestartwithinfo) callback | 要注册的拍照开始事件回调。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。 |

### OH\_PhotoOutput\_GetPhotoRotation()

PhonePC/2in1TabletTVWearable

```
1. Camera_ErrorCode OH_PhotoOutput_GetPhotoRotation(Camera_PhotoOutput* photoOutput, int deviceDegree, Camera_ImageRotation* imageRotation)
```

**描述**

获取照片旋转角度。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_PhotoOutput](capi-oh-camera-camera-photooutput.md)\* photoOutput | 用于获取照片旋转角度的拍照输出实例。 |
| int deviceDegree | 当前设备旋转角度。 |
| [Camera\_ImageRotation](capi-camera-h.md#camera_imagerotation)\* imageRotation | 照片旋转角度的结果。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。  CAMERA\_SERVICE\_FATAL\_ERROR：相机服务异常。 |

### OH\_PhotoOutput\_GetPhotoRotationWithoutDeviceDegree()

PhonePC/2in1TabletTVWearable

```
1. Camera_ErrorCode OH_PhotoOutput_GetPhotoRotationWithoutDeviceDegree(Camera_PhotoOutput* photoOutput, Camera_ImageRotation* imageRotation)
```

**描述**

获取照片旋转角度。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_PhotoOutput](capi-oh-camera-camera-photooutput.md)\* photoOutput | 用于获取照片旋转角度的拍照输出实例。 |
| [Camera\_ImageRotation](capi-camera-h.md#camera_imagerotation)\* imageRotation | 照片旋转角度的结果。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。  CAMERA\_SERVICE\_FATAL\_ERROR：相机服务异常。 |

### OH\_PhotoOutput\_UnregisterCaptureStartWithInfoCallback()

PhonePC/2in1TabletTVWearable

```
1. Camera_ErrorCode OH_PhotoOutput_UnregisterCaptureStartWithInfoCallback(Camera_PhotoOutput* photoOutput, OH_PhotoOutput_CaptureStartWithInfo callback)
```

**描述**

注销拍照开始事件回调。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_PhotoOutput](capi-oh-camera-camera-photooutput.md)\* photoOutput | 拍照输出实例。 |
| [OH\_PhotoOutput\_CaptureStartWithInfo](capi-photo-output-h.md#oh_photooutput_capturestartwithinfo) callback | 要注销的拍照开始事件回调。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。 |

### OH\_PhotoOutput\_RegisterCaptureEndCallback()

PhonePC/2in1TabletTVWearable

```
1. Camera_ErrorCode OH_PhotoOutput_RegisterCaptureEndCallback(Camera_PhotoOutput* photoOutput, OH_PhotoOutput_CaptureEnd callback)
```

**描述**

注册拍照结束事件回调。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_PhotoOutput](capi-oh-camera-camera-photooutput.md)\* photoOutput | 拍照输出实例。 |
| [OH\_PhotoOutput\_CaptureEnd](capi-photo-output-h.md#oh_photooutput_captureend) callback | 要注册的拍照结束事件回调。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。 |

### OH\_PhotoOutput\_UnregisterCaptureEndCallback()

PhonePC/2in1TabletTVWearable

```
1. Camera_ErrorCode OH_PhotoOutput_UnregisterCaptureEndCallback(Camera_PhotoOutput* photoOutput, OH_PhotoOutput_CaptureEnd callback)
```

**描述**

注销拍照结束事件回调。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_PhotoOutput](capi-oh-camera-camera-photooutput.md)\* photoOutput | 拍照输出实例。 |
| [OH\_PhotoOutput\_CaptureEnd](capi-photo-output-h.md#oh_photooutput_captureend) callback | 要注销的拍照结束事件回调。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。 |

### OH\_PhotoOutput\_RegisterFrameShutterEndCallback()

PhonePC/2in1TabletTVWearable

```
1. Camera_ErrorCode OH_PhotoOutput_RegisterFrameShutterEndCallback(Camera_PhotoOutput* photoOutput, OH_PhotoOutput_OnFrameShutterEnd callback)
```

**描述**

注册拍照曝光结束事件回调。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_PhotoOutput](capi-oh-camera-camera-photooutput.md)\* photoOutput | 拍照输出实例。 |
| [OH\_PhotoOutput\_OnFrameShutterEnd](capi-photo-output-h.md#oh_photooutput_onframeshutterend) callback | 要注册的拍照曝光结束事件回调。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。 |

### OH\_PhotoOutput\_UnregisterFrameShutterEndCallback()

PhonePC/2in1TabletTVWearable

```
1. Camera_ErrorCode OH_PhotoOutput_UnregisterFrameShutterEndCallback(Camera_PhotoOutput* photoOutput, OH_PhotoOutput_OnFrameShutterEnd callback)
```

**描述**

注销拍照曝光结束事件回调。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_PhotoOutput](capi-oh-camera-camera-photooutput.md)\* photoOutput | 拍照输出实例。 |
| [OH\_PhotoOutput\_OnFrameShutterEnd](capi-photo-output-h.md#oh_photooutput_onframeshutterend) callback | 要注销的拍照曝光结束事件回调。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。 |

### OH\_PhotoOutput\_RegisterCaptureReadyCallback()

PhonePC/2in1TabletTVWearable

```
1. Camera_ErrorCode OH_PhotoOutput_RegisterCaptureReadyCallback(Camera_PhotoOutput* photoOutput, OH_PhotoOutput_CaptureReady callback)
```

**描述**

注册拍照就绪事件回调。收到回调后，可以继续进行下一次拍照。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_PhotoOutput](capi-oh-camera-camera-photooutput.md)\* photoOutput | 拍照输出实例。 |
| [OH\_PhotoOutput\_CaptureReady](capi-photo-output-h.md#oh_photooutput_captureready) callback | 要注册的拍照就绪事件回调。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。 |

### OH\_PhotoOutput\_UnregisterCaptureReadyCallback()

PhonePC/2in1TabletTVWearable

```
1. Camera_ErrorCode OH_PhotoOutput_UnregisterCaptureReadyCallback(Camera_PhotoOutput* photoOutput, OH_PhotoOutput_CaptureReady callback)
```

**描述**

注销拍照就绪事件回调。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_PhotoOutput](capi-oh-camera-camera-photooutput.md)\* photoOutput | 拍照输出实例。 |
| [OH\_PhotoOutput\_CaptureReady](capi-photo-output-h.md#oh_photooutput_captureready) callback | 要注销的拍照就绪事件回调。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。 |

### OH\_PhotoOutput\_RegisterEstimatedCaptureDurationCallback()

PhonePC/2in1TabletTVWearable

```
1. Camera_ErrorCode OH_PhotoOutput_RegisterEstimatedCaptureDurationCallback(Camera_PhotoOutput* photoOutput, OH_PhotoOutput_EstimatedCaptureDuration callback)
```

**描述**

注册预计拍照时间事件回调。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_PhotoOutput](capi-oh-camera-camera-photooutput.md)\* photoOutput | 拍照输出实例。 |
| [OH\_PhotoOutput\_EstimatedCaptureDuration](capi-photo-output-h.md#oh_photooutput_estimatedcaptureduration) callback | 要注册的预计拍照时间事件回调。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。 |

### OH\_PhotoOutput\_UnregisterEstimatedCaptureDurationCallback()

PhonePC/2in1TabletTVWearable

```
1. Camera_ErrorCode OH_PhotoOutput_UnregisterEstimatedCaptureDurationCallback(Camera_PhotoOutput* photoOutput, OH_PhotoOutput_EstimatedCaptureDuration callback)
```

**描述**

注销预计拍照时间事件回调。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_PhotoOutput](capi-oh-camera-camera-photooutput.md)\* photoOutput | 拍照输出实例。 |
| [OH\_PhotoOutput\_EstimatedCaptureDuration](capi-photo-output-h.md#oh_photooutput_estimatedcaptureduration) callback | 要注销的预计拍照时间事件回调。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。 |

### OH\_PhotoOutput\_RegisterPhotoAvailableCallback()

PhonePC/2in1TabletTVWearable

```
1. Camera_ErrorCode OH_PhotoOutput_RegisterPhotoAvailableCallback(Camera_PhotoOutput* photoOutput, OH_PhotoOutput_PhotoAvailable callback)
```

**描述**

注册输出照片可用回调。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_PhotoOutput](capi-oh-camera-camera-photooutput.md)\* photoOutput | 拍照输出实例。 |
| [OH\_PhotoOutput\_PhotoAvailable](capi-photo-output-h.md#oh_photooutput_photoavailable) callback | 要注册的输出照片可用回调。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。  CAMERA\_SERVICE\_FATAL\_ERROR：相机服务异常。 |

### OH\_PhotoOutput\_UnregisterPhotoAvailableCallback()

PhonePC/2in1TabletTVWearable

```
1. Camera_ErrorCode OH_PhotoOutput_UnregisterPhotoAvailableCallback(Camera_PhotoOutput* photoOutput, OH_PhotoOutput_PhotoAvailable callback)
```

**描述**

注销输出照片可用回调。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_PhotoOutput](capi-oh-camera-camera-photooutput.md)\* photoOutput | 拍照输出实例。 |
| [OH\_PhotoOutput\_PhotoAvailable](capi-photo-output-h.md#oh_photooutput_photoavailable) callback | 要注销的输出照片可用回调。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。  CAMERA\_SERVICE\_FATAL\_ERROR：相机服务异常。 |

### OH\_PhotoOutput\_RegisterPhotoAssetAvailableCallback()

PhonePC/2in1TabletTVWearable

```
1. Camera_ErrorCode OH_PhotoOutput_RegisterPhotoAssetAvailableCallback(Camera_PhotoOutput* photoOutput, OH_PhotoOutput_PhotoAssetAvailable callback)
```

**描述**

注册输出照片资源可用回调。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_PhotoOutput](capi-oh-camera-camera-photooutput.md)\* photoOutput | 拍照输出实例。 |
| [OH\_PhotoOutput\_PhotoAssetAvailable](capi-photo-output-h.md#oh_photooutput_photoassetavailable) callback | 要注册的输出照片资源可用回调。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。 |

### OH\_PhotoOutput\_UnregisterPhotoAssetAvailableCallback()

PhonePC/2in1TabletTVWearable

```
1. Camera_ErrorCode OH_PhotoOutput_UnregisterPhotoAssetAvailableCallback(Camera_PhotoOutput* photoOutput, OH_PhotoOutput_PhotoAssetAvailable callback)
```

**描述**

注销输出照片资源可用回调。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_PhotoOutput](capi-oh-camera-camera-photooutput.md)\* photoOutput | 拍照输出实例。 |
| [OH\_PhotoOutput\_PhotoAssetAvailable](capi-photo-output-h.md#oh_photooutput_photoassetavailable) callback | 要注销的输出照片资源可用回调。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。 |

### OH\_PhotoOutput\_Capture()

PhonePC/2in1TabletTVWearable

```
1. Camera_ErrorCode OH_PhotoOutput_Capture(Camera_PhotoOutput* photoOutput)
```

**描述**

拍摄照片。

必须在[OH\_PreviewOutput\_Release](capi-preview-output-h.md#oh_previewoutput_release)之前调用，否则会导致无法拍照。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_PhotoOutput](capi-oh-camera-camera-photooutput.md)\* photoOutput | 用于捕获拍照的拍照输出实例。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。  CAMERA\_SESSION\_NOT\_RUNNING：捕获会话未运行。  CAMERA\_SERVICE\_FATAL\_ERROR：相机服务异常。 |

### OH\_PhotoOutput\_Capture\_WithCaptureSetting()

PhonePC/2in1TabletTVWearable

```
1. Camera_ErrorCode OH_PhotoOutput_Capture_WithCaptureSetting(Camera_PhotoOutput* photoOutput, Camera_PhotoCaptureSetting setting)
```

**描述**

使用捕获设置捕获拍照。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_PhotoOutput](capi-oh-camera-camera-photooutput.md)\* photoOutput | 用于捕获拍照的拍照输出实例。 |
| [Camera\_PhotoCaptureSetting](capi-oh-camera-camera-photocapturesetting.md) setting | 用于捕获拍照的[Camera\_PhotoCaptureSetting](capi-oh-camera-camera-photocapturesetting.md)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。  CAMERA\_SESSION\_NOT\_RUNNING：捕获会话未运行。  CAMERA\_SERVICE\_FATAL\_ERROR：相机服务异常。 |

### OH\_PhotoOutput\_Release()

PhonePC/2in1TabletTVWearable

```
1. Camera_ErrorCode OH_PhotoOutput_Release(Camera_PhotoOutput* photoOutput)
```

**描述**

释放拍照输出。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_PhotoOutput](capi-oh-camera-camera-photooutput.md)\* photoOutput | 要释放的拍照输出实例。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。  CAMERA\_SERVICE\_FATAL\_ERROR：相机服务异常。 |

### OH\_PhotoOutput\_IsMirrorSupported()

PhonePC/2in1TabletTVWearable

```
1. Camera_ErrorCode OH_PhotoOutput_IsMirrorSupported(Camera_PhotoOutput* photoOutput, bool* isSupported)
```

**描述**

检查是否支持镜像拍照。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_PhotoOutput](capi-oh-camera-camera-photooutput.md)\* photoOutput | 拍照输出实例，用于检查是否支持镜像。 |
| bool\* isSupported | 是否支持镜像的结果。true表示支持镜像，false表示不支持。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。  CAMERA\_SERVICE\_FATAL\_ERROR：相机服务异常。 |

### OH\_PhotoOutput\_EnableMirror()

PhonePC/2in1TabletTVWearable

```
1. Camera_ErrorCode OH_PhotoOutput_EnableMirror(Camera_PhotoOutput* photoOutput, bool enabled)
```

**描述**

是否启用动态照片镜像拍照。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_PhotoOutput](capi-oh-camera-camera-photooutput.md)\* photoOutput | 拍照输出实例，用于确认是否启用镜像拍照。 |
| bool enabled | 是否启用动态照片镜像拍照的结果，true为开启动态照片镜像拍照，false为关闭动态照片镜像拍照。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。  CAMERA\_SERVICE\_FATAL\_ERROR：相机服务异常。 |

### OH\_PhotoOutput\_GetActiveProfile()

PhonePC/2in1TabletTVWearable

```
1. Camera_ErrorCode OH_PhotoOutput_GetActiveProfile(Camera_PhotoOutput* photoOutput, Camera_Profile** profile)
```

**描述**

获取当前照片输出配置文件。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_PhotoOutput](capi-oh-camera-camera-photooutput.md)\* photoOutput | 传递当前配置文件的拍照输出实例。 |
| [Camera\_Profile](capi-oh-camera-camera-profile.md)\*\* profile | 如果方法调用成功，将记录照片输出配置文件。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。  CAMERA\_SERVICE\_FATAL\_ERROR：相机服务异常。 |

### OH\_PhotoOutput\_DeleteProfile()

PhonePC/2in1TabletTVWearable

```
1. Camera_ErrorCode OH_PhotoOutput_DeleteProfile(Camera_Profile* profile)
```

**描述**

删除照片配置文件实例。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_Profile](capi-oh-camera-camera-profile.md)\* profile | 要被删除的照片配置文件实例。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。 |

### OH\_PhotoOutput\_IsMovingPhotoSupported()

PhonePC/2in1TabletTVWearable

```
1. Camera_ErrorCode OH_PhotoOutput_IsMovingPhotoSupported(Camera_PhotoOutput* photoOutput, bool* isSupported)
```

**描述**

检查是否支持动态照片。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_PhotoOutput](capi-oh-camera-camera-photooutput.md)\* photoOutput | 用于检查是否支持动态照片的拍照输出实例。 |
| bool\* isSupported | 是否支持动态照片的结果。true表示支持动态照片，false表示不支持。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。  CAMERA\_SERVICE\_FATAL\_ERROR：相机服务异常。 |

### OH\_PhotoOutput\_EnableMovingPhoto()

PhonePC/2in1TabletTVWearable

```
1. Camera_ErrorCode OH_PhotoOutput_EnableMovingPhoto(Camera_PhotoOutput* photoOutput, bool enabled)
```

**描述**

是否启用动态照片。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_PhotoOutput](capi-oh-camera-camera-photooutput.md)\* photoOutput | 用于启用或禁用动态照片的拍照输出实例。 |
| bool enabled | 是否启用动态照片。true表示启用动态照片，false表示不启用。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。  CAMERA\_SERVICE\_FATAL\_ERROR：相机服务异常。 |

### OH\_PhotoOutput\_IsPhotoQualityPrioritizationSupported()

PhonePC/2in1TabletTVWearable

```
1. Camera_ErrorCode OH_PhotoOutput_IsPhotoQualityPrioritizationSupported(Camera_PhotoOutput* photoOutput, Camera_PhotoQualityPrioritization qualityPrioritization, bool* isSupported)
```

**描述**

检查是否支持指定的拍照画质优先策略。

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_PhotoOutput](capi-oh-camera-camera-photooutput.md)\* photoOutput | 用于获取是否支持拍照画质优先策略的拍照输出实例。 |
| [Camera\_PhotoQualityPrioritization](capi-camera-h.md#camera_photoqualityprioritization) qualityPrioritization | 要检查的拍照画质优先策略。 |
| bool\* isSupported | 是否支持指定的拍照画质优先策略。true表示支持，false表示不支持。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。  CAMERA\_SERVICE\_FATAL\_ERROR：相机服务异常。 |

### OH\_PhotoOutput\_SetPhotoQualityPrioritization()

PhonePC/2in1TabletTVWearable

```
1. Camera_ErrorCode OH_PhotoOutput_SetPhotoQualityPrioritization(Camera_PhotoOutput* photoOutput, Camera_PhotoQualityPrioritization qualityPrioritization)
```

**描述**

设置拍照画质优先策略。

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_PhotoOutput](capi-oh-camera-camera-photooutput.md)\* photoOutput | 用于设置拍照画质优先策略的拍照输出实例。 |
| [Camera\_PhotoQualityPrioritization](capi-camera-h.md#camera_photoqualityprioritization) qualityPrioritization | 要设置的拍照画质优先策略。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。  CAMERA\_OPERATION\_NOT\_ALLOWED：操作不允许。  CAMERA\_SERVICE\_FATAL\_ERROR：相机服务异常。 |
