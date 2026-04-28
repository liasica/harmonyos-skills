---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-video-output-h
title: video_output.h
breadcrumb: API参考 > 媒体 > Camera Kit（相机服务） > C API > 头文件 > video_output.h
category: harmonyos-references
scraped_at: 2026-04-28T08:12:46+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:1ee1fa8235c8aaded61ec313a638d903ab9ea68aa801101310783cbe690378c7
---

## 概述

PhonePC/2in1TabletTVWearable

声明录像输出概念。

**引用文件：** <ohcamera/video\_output.h>

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
| [VideoOutput\_Callbacks](capi-oh-camera-videooutput-callbacks.md) | VideoOutput\_Callbacks | 用于录像输出的回调。 |
| [Camera\_VideoOutput](capi-oh-camera-camera-videooutput.md) | Camera\_VideoOutput | 录像输出对象。  可以使用[OH\_CameraManager\_CreateVideoOutput](capi-camera-manager-h.md#oh_cameramanager_createvideooutput)方法创建指针。 |

### 函数

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [typedef void (\*OH\_VideoOutput\_OnFrameStart)(Camera\_VideoOutput\* videoOutput)](capi-video-output-h.md#oh_videooutput_onframestart) | OH\_VideoOutput\_OnFrameStart | 在[VideoOutput\_Callbacks](capi-oh-camera-videooutput-callbacks.md)中被调用的录像输出帧开始回调。 |
| [typedef void (\*OH\_VideoOutput\_OnFrameEnd)(Camera\_VideoOutput\* videoOutput, int32\_t frameCount)](capi-video-output-h.md#oh_videooutput_onframeend) | OH\_VideoOutput\_OnFrameEnd | 在[VideoOutput\_Callbacks](capi-oh-camera-videooutput-callbacks.md)中被调用的录像输出帧结束回调。 |
| [typedef void (\*OH\_VideoOutput\_OnError)(Camera\_VideoOutput\* videoOutput, Camera\_ErrorCode errorCode)](capi-video-output-h.md#oh_videooutput_onerror) | OH\_VideoOutput\_OnError | 在[VideoOutput\_Callbacks](capi-oh-camera-videooutput-callbacks.md)中被调用的录像输出错误回调。 |
| [Camera\_ErrorCode OH\_VideoOutput\_RegisterCallback(Camera\_VideoOutput\* videoOutput, VideoOutput\_Callbacks\* callback)](capi-video-output-h.md#oh_videooutput_registercallback) | - | 注册录像输出更改事件回调。 |
| [Camera\_ErrorCode OH\_VideoOutput\_UnregisterCallback(Camera\_VideoOutput\* videoOutput, VideoOutput\_Callbacks\* callback)](capi-video-output-h.md#oh_videooutput_unregistercallback) | - | 注销录像输出更改事件回调。 |
| [Camera\_ErrorCode OH\_VideoOutput\_Start(Camera\_VideoOutput\* videoOutput)](capi-video-output-h.md#oh_videooutput_start) | - | 开始录像输出。 |
| [Camera\_ErrorCode OH\_VideoOutput\_Stop(Camera\_VideoOutput\* videoOutput)](capi-video-output-h.md#oh_videooutput_stop) | - | 停止录像输出。 |
| [Camera\_ErrorCode OH\_VideoOutput\_Release(Camera\_VideoOutput\* videoOutput)](capi-video-output-h.md#oh_videooutput_release) | - | 释放录像输出实例。 |
| [Camera\_ErrorCode OH\_VideoOutput\_GetActiveProfile(Camera\_VideoOutput\* videoOutput, Camera\_VideoProfile\*\* profile)](capi-video-output-h.md#oh_videooutput_getactiveprofile) | - | 获取当前视频输出配置文件。 |
| [Camera\_ErrorCode OH\_VideoOutput\_DeleteProfile(Camera\_VideoProfile\* profile)](capi-video-output-h.md#oh_videooutput_deleteprofile) | - | 删除视频配置文件实例。 |
| [Camera\_ErrorCode OH\_VideoOutput\_IsMirrorSupported(Camera\_VideoOutput\* videoOutput, bool\* isSupported)](capi-video-output-h.md#oh_videooutput_ismirrorsupported) | - | 判断当前视频输出是否支持镜像。 |
| [Camera\_ErrorCode OH\_VideoOutput\_EnableMirror(Camera\_VideoOutput\* videoOutput, bool mirrorMode)](capi-video-output-h.md#oh_videooutput_enablemirror) | - | 打开/关闭当前视频输出镜像功能。 |
| [Camera\_ErrorCode OH\_VideoOutput\_GetVideoRotation(Camera\_VideoOutput\* videoOutput, int deviceDegree, Camera\_ImageRotation\* imageRotation)](capi-video-output-h.md#oh_videooutput_getvideorotation) | - | 获取录像旋转角度。 |
| [Camera\_ErrorCode OH\_VideoOutput\_GetVideoRotationWithoutDeviceDegree(Camera\_VideoOutput\* videoOutput, Camera\_ImageRotation\* imageRotation)](capi-video-output-h.md#oh_videooutput_getvideorotationwithoutdevicedegree) | - | 获取录像旋转角度。 |
| [Camera\_ErrorCode OH\_VideoOutput\_GetSupportedFrameRates(Camera\_VideoOutput\* videoOutput, Camera\_FrameRateRange\*\* frameRateRange, uint32\_t\* size)](capi-video-output-h.md#oh_videooutput_getsupportedframerates) | - | 获取支持的视频输出帧率列表。 |
| [Camera\_ErrorCode OH\_VideoOutput\_DeleteFrameRates(Camera\_VideoOutput\* videoOutput, Camera\_FrameRateRange\* frameRateRange)](capi-video-output-h.md#oh_videooutput_deleteframerates) | - | 删除帧率列表。 |
| [Camera\_ErrorCode OH\_VideoOutput\_SetFrameRate(Camera\_VideoOutput\* videoOutput, int32\_t minFps, int32\_t maxFps)](capi-video-output-h.md#oh_videooutput_setframerate) | - | 设置视频输出帧率。 |
| [Camera\_ErrorCode OH\_VideoOutput\_GetActiveFrameRate(Camera\_VideoOutput\* videoOutput, Camera\_FrameRateRange\* frameRateRange)](capi-video-output-h.md#oh_videooutput_getactiveframerate) | - | 获取当前视频输出帧率。 |

## 函数说明

PhonePC/2in1TabletTVWearable

### OH\_VideoOutput\_OnFrameStart()

PhonePC/2in1TabletTVWearable

```
1. typedef void (*OH_VideoOutput_OnFrameStart)(Camera_VideoOutput* videoOutput)
```

**描述**

在[VideoOutput\_Callbacks](capi-oh-camera-videooutput-callbacks.md)中被调用的录像输出帧开始回调。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_VideoOutput](capi-oh-camera-camera-videooutput.md)\* videoOutput | 传递回调的录像输出实例。 |

### OH\_VideoOutput\_OnFrameEnd()

PhonePC/2in1TabletTVWearable

```
1. typedef void (*OH_VideoOutput_OnFrameEnd)(Camera_VideoOutput* videoOutput, int32_t frameCount)
```

**描述**

在[VideoOutput\_Callbacks](capi-oh-camera-videooutput-callbacks.md)中被调用的录像输出帧结束回调。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_VideoOutput](capi-oh-camera-camera-videooutput.md)\* videoOutput | 传递回调的录像输出实例。 |
| int32\_t frameCount | 回调传递的帧计数。 |

### OH\_VideoOutput\_OnError()

PhonePC/2in1TabletTVWearable

```
1. typedef void (*OH_VideoOutput_OnError)(Camera_VideoOutput* videoOutput, Camera_ErrorCode errorCode)
```

**描述**

在[VideoOutput\_Callbacks](capi-oh-camera-videooutput-callbacks.md)中被调用的录像输出错误回调。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_VideoOutput](capi-oh-camera-camera-videooutput.md)\* videoOutput | 传递回调的录像输出实例。 |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) errorCode | 录像输出的错误码。 |

**参考：**

[CAMERA\_SERVICE\_FATAL\_ERROR](capi-camera-h.md#camera_errorcode)

### OH\_VideoOutput\_RegisterCallback()

PhonePC/2in1TabletTVWearable

```
1. Camera_ErrorCode OH_VideoOutput_RegisterCallback(Camera_VideoOutput* videoOutput, VideoOutput_Callbacks* callback)
```

**描述**

注册录像输出更改事件回调。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_VideoOutput](capi-oh-camera-camera-videooutput.md)\* videoOutput | 录像输出实例。 |
| [VideoOutput\_Callbacks](capi-oh-camera-videooutput-callbacks.md)\* callback | 要注册的录像输出更改事件回调。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。 |

### OH\_VideoOutput\_UnregisterCallback()

PhonePC/2in1TabletTVWearable

```
1. Camera_ErrorCode OH_VideoOutput_UnregisterCallback(Camera_VideoOutput* videoOutput, VideoOutput_Callbacks* callback)
```

**描述**

注销录像输出更改事件回调。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_VideoOutput](capi-oh-camera-camera-videooutput.md)\* videoOutput | 录像输出实例。 |
| [VideoOutput\_Callbacks](capi-oh-camera-videooutput-callbacks.md)\* callback | 要注销的录像输出更改事件回调。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。 |

### OH\_VideoOutput\_Start()

PhonePC/2in1TabletTVWearable

```
1. Camera_ErrorCode OH_VideoOutput_Start(Camera_VideoOutput* videoOutput)
```

**描述**

开始录像输出。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_VideoOutput](capi-oh-camera-camera-videooutput.md)\* videoOutput | 要启动的录像输出实例。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。  CAMERA\_SESSION\_NOT\_CONFIG：捕获会话未配置。  CAMERA\_SERVICE\_FATAL\_ERROR：相机服务异常。 |

### OH\_VideoOutput\_Stop()

PhonePC/2in1TabletTVWearable

```
1. Camera_ErrorCode OH_VideoOutput_Stop(Camera_VideoOutput* videoOutput)
```

**描述**

停止录像输出。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_VideoOutput](capi-oh-camera-camera-videooutput.md)\* videoOutput | 要停止的录像输出实例。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。  CAMERA\_SERVICE\_FATAL\_ERROR：相机服务异常。 |

### OH\_VideoOutput\_Release()

PhonePC/2in1TabletTVWearable

```
1. Camera_ErrorCode OH_VideoOutput_Release(Camera_VideoOutput* videoOutput)
```

**描述**

释放录像输出实例。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_VideoOutput](capi-oh-camera-camera-videooutput.md)\* videoOutput | 要释放的录像输出实例。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。  CAMERA\_SERVICE\_FATAL\_ERROR：相机服务异常。 |

### OH\_VideoOutput\_GetActiveProfile()

PhonePC/2in1TabletTVWearable

```
1. Camera_ErrorCode OH_VideoOutput_GetActiveProfile(Camera_VideoOutput* videoOutput, Camera_VideoProfile** profile)
```

**描述**

获取当前视频输出配置文件。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_VideoOutput](capi-oh-camera-camera-videooutput.md)\* videoOutput | 传递当前视频输出配置文件的录像输出实例。 |
| [Camera\_VideoProfile](capi-oh-camera-camera-videoprofile.md)\*\* profile | 如果方法调用成功，将记录当前的视频输出配置文件。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。  CAMERA\_SERVICE\_FATAL\_ERROR：相机服务异常。 |

### OH\_VideoOutput\_DeleteProfile()

PhonePC/2in1TabletTVWearable

```
1. Camera_ErrorCode OH_VideoOutput_DeleteProfile(Camera_VideoProfile* profile)
```

**描述**

删除视频配置文件实例。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_VideoProfile](capi-oh-camera-camera-videoprofile.md)\* profile | 要删除的视频配置文件实例。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。 |

### OH\_VideoOutput\_IsMirrorSupported()

PhonePC/2in1TabletTVWearable

```
1. Camera_ErrorCode OH_VideoOutput_IsMirrorSupported(Camera_VideoOutput* videoOutput, bool* isSupported)
```

**描述**

判断当前视频输出是否支持镜像。

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_VideoOutput](capi-oh-camera-camera-videooutput.md)\* videoOutput | 传递当前视频输出的录像输出实例。 |
| bool\* isSupported | 当前视频输出是否支持镜像。true表示当前视频输出支持镜像，false表示不支持。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。  CAMERA\_SERVICE\_FATAL\_ERROR：相机服务异常。 |

### OH\_VideoOutput\_EnableMirror()

PhonePC/2in1TabletTVWearable

```
1. Camera_ErrorCode OH_VideoOutput_EnableMirror(Camera_VideoOutput* videoOutput, bool mirrorMode)
```

**描述**

打开/关闭当前视频输出镜像功能。

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_VideoOutput](capi-oh-camera-camera-videooutput.md)\* videoOutput | 传递当前视频输出的录像输出实例。 |
| bool mirrorMode | 设备是否开启镜像功能。true表示打开镜像功能，false表示关闭镜像功能。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。  CAMERA\_SERVICE\_FATAL\_ERROR：相机服务异常。 |

### OH\_VideoOutput\_GetVideoRotation()

PhonePC/2in1TabletTVWearable

```
1. Camera_ErrorCode OH_VideoOutput_GetVideoRotation(Camera_VideoOutput* videoOutput, int deviceDegree, Camera_ImageRotation* imageRotation)
```

**描述**

获取录像旋转角度。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_VideoOutput](capi-oh-camera-camera-videooutput.md)\* videoOutput | 传递当前视频输出的录像输出实例。 |
| int deviceDegree | 设备目前相对于自然方向（充电口朝下）顺时针的旋转角度。 |
| [Camera\_ImageRotation](capi-camera-h.md#camera_imagerotation)\* imageRotation | 录像旋转角度的结果。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。  CAMERA\_SERVICE\_FATAL\_ERROR：相机服务异常。 |

### OH\_VideoOutput\_GetVideoRotationWithoutDeviceDegree()

PhonePC/2in1TabletTVWearable

```
1. Camera_ErrorCode OH_VideoOutput_GetVideoRotationWithoutDeviceDegree(Camera_VideoOutput* videoOutput, Camera_ImageRotation* imageRotation)
```

**描述**

获取录像旋转角度。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_VideoOutput](capi-oh-camera-camera-videooutput.md)\* videoOutput | 传递当前视频输出的录像输出实例。 |
| [Camera\_ImageRotation](capi-camera-h.md#camera_imagerotation)\* imageRotation | 录像旋转角度的结果。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。  CAMERA\_SERVICE\_FATAL\_ERROR：相机服务异常。 |

### OH\_VideoOutput\_GetSupportedFrameRates()

PhonePC/2in1TabletTVWearable

```
1. Camera_ErrorCode OH_VideoOutput_GetSupportedFrameRates(Camera_VideoOutput* videoOutput, Camera_FrameRateRange** frameRateRange, uint32_t* size)
```

**描述**

获取支持的视频输出帧率列表。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_VideoOutput](capi-oh-camera-camera-videooutput.md)\* videoOutput | 传递支持的视频输出帧率列表的录像输出实例。 |
| [Camera\_FrameRateRange](capi-oh-camera-camera-frameraterange.md)\*\* frameRateRange | 如果方法调用成功，将记录支持的视频输出帧率列表。 |
| uint32\_t\* size | 如果方法调用成功，将记录支持的视频输出帧率列表大小。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。  CAMERA\_SERVICE\_FATAL\_ERROR：相机服务异常。 |

### OH\_VideoOutput\_DeleteFrameRates()

PhonePC/2in1TabletTVWearable

```
1. Camera_ErrorCode OH_VideoOutput_DeleteFrameRates(Camera_VideoOutput* videoOutput, Camera_FrameRateRange* frameRateRange)
```

**描述**

删除帧率列表。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_VideoOutput](capi-oh-camera-camera-videooutput.md)\* videoOutput | 录像输出实例。 |
| [Camera\_FrameRateRange](capi-oh-camera-camera-frameraterange.md)\* frameRateRange | 要删除的帧率列表。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。 |

### OH\_VideoOutput\_SetFrameRate()

PhonePC/2in1TabletTVWearable

```
1. Camera_ErrorCode OH_VideoOutput_SetFrameRate(Camera_VideoOutput* videoOutput, int32_t minFps, int32_t maxFps)
```

**描述**

设置视频输出帧率。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_VideoOutput](capi-oh-camera-camera-videooutput.md)\* videoOutput | 要设置帧率的录像输出实例。 |
| int32\_t minFps | 设置的最小帧率。 |
| int32\_t maxFps | 设置的最大帧率。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。 |

### OH\_VideoOutput\_GetActiveFrameRate()

PhonePC/2in1TabletTVWearable

```
1. Camera_ErrorCode OH_VideoOutput_GetActiveFrameRate(Camera_VideoOutput* videoOutput, Camera_FrameRateRange* frameRateRange)
```

**描述**

获取当前视频输出帧率。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_VideoOutput](capi-oh-camera-camera-videooutput.md)\* videoOutput | 传递当前视频输出帧率的录像输出实例。 |
| [Camera\_FrameRateRange](capi-oh-camera-camera-frameraterange.md)\* frameRateRange | 如果方法调用成功，将记录当前的视频输出帧率。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。  CAMERA\_SERVICE\_FATAL\_ERROR：相机服务异常。 |
