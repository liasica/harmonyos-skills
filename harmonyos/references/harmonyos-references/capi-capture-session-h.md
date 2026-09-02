---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-capture-session-h
title: capture_session.h
breadcrumb: API参考 > 媒体 > Camera Kit（相机服务） > C API > 头文件 > capture_session.h
category: harmonyos-references
scraped_at: 2026-09-02T15:02:28+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:823af8ef0aae9ef3a53d365cbec5d91a161cb0efca764b6238741521146ac4de
---

## 概述

声明捕获会话概念。

**引用文件：** <ohcamera/capture\_session.h>

**库：** libohcamera.so

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 11

**相关模块：** [OH\_Camera](capi-oh-camera.md)

## 汇总

### 结构体

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [CaptureSession\_Callbacks](capi-oh-camera-capturesession-callbacks.md) | CaptureSession\_Callbacks | 捕获会话的回调。 |
| [Camera\_CaptureSession](capi-oh-camera-camera-capturesession.md) | Camera\_CaptureSession | 捕获会话对象。  可以使用[OH\_CameraManager\_CreateCaptureSession](capi-camera-manager-h.md#oh_cameramanager_createcapturesession)方法创建指针。 |

### 函数

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [typedef void (\*OH\_CaptureSession\_OnFocusStateChange)(Camera\_CaptureSession\* session, Camera\_FocusState focusState)](capi-capture-session-h.md#oh_capturesession_onfocusstatechange) | OH\_CaptureSession\_OnFocusStateChange | 在[CaptureSession\_Callbacks](capi-oh-camera-capturesession-callbacks.md)中被调用的捕获会话焦点状态回调。 |
| [typedef void (\*OH\_CaptureSession\_OnError)(Camera\_CaptureSession\* session, Camera\_ErrorCode errorCode)](capi-capture-session-h.md#oh_capturesession_onerror) | OH\_CaptureSession\_OnError | 在[CaptureSession\_Callbacks](capi-oh-camera-capturesession-callbacks.md)中被调用的捕获会话错误回调。 |
| [typedef void (\*OH\_CaptureSession\_OnSmoothZoomInfo)(Camera\_CaptureSession\* session, Camera\_SmoothZoomInfo\* smoothZoomInfo)](capi-capture-session-h.md#oh_capturesession_onsmoothzoominfo) | OH\_CaptureSession\_OnSmoothZoomInfo | 拍照会话平滑变焦信息回调，触发平滑变焦后该回调会返回。 |
| [typedef void (\*OH\_CaptureSession\_OnAutoDeviceSwitchStatusChange)(Camera\_CaptureSession\* session, Camera\_AutoDeviceSwitchStatusInfo\* autoDeviceSwitchStatusInfo)](capi-capture-session-h.md#oh_capturesession_onautodeviceswitchstatuschange) | OH\_CaptureSession\_OnAutoDeviceSwitchStatusChange | 捕获会话设备切换状态回调。 |
| [typedef void (\*OH\_CaptureSession\_OnSystemPressureLevelChange)(Camera\_CaptureSession\* session, Camera\_SystemPressureLevel systemPressureLevel)](capi-capture-session-h.md#oh_capturesession_onsystempressurelevelchange) | OH\_CaptureSession\_OnSystemPressureLevelChange | 捕获系统压力状态变化回调。 |
| [typedef void (\*OH\_CaptureSession\_OnControlCenterEffectStatusChange)(Camera\_CaptureSession\* session, Camera\_ControlCenterStatusInfo\* controlCenterStatusInfo)](capi-capture-session-h.md#oh_capturesession_oncontrolcentereffectstatuschange) | OH\_CaptureSession\_OnControlCenterEffectStatusChange | 相机控制器效果激活状态变化回调。 |
| [Camera\_ErrorCode OH\_CaptureSession\_RegisterCallback(Camera\_CaptureSession\* session, CaptureSession\_Callbacks\* callback)](capi-capture-session-h.md#oh_capturesession_registercallback) | - | 注册捕获会话事件回调。 |
| [Camera\_ErrorCode OH\_CaptureSession\_UnregisterCallback(Camera\_CaptureSession\* session, CaptureSession\_Callbacks\* callback)](capi-capture-session-h.md#oh_capturesession_unregistercallback) | - | 注销捕获会话事件回调。 |
| [Camera\_ErrorCode OH\_CaptureSession\_RegisterSmoothZoomInfoCallback(Camera\_CaptureSession\* session, OH\_CaptureSession\_OnSmoothZoomInfo smoothZoomInfoCallback)](capi-capture-session-h.md#oh_capturesession_registersmoothzoominfocallback) | - | 注册平滑变焦信息事件回调。 |
| [Camera\_ErrorCode OH\_CaptureSession\_UnregisterSmoothZoomInfoCallback(Camera\_CaptureSession\* session, OH\_CaptureSession\_OnSmoothZoomInfo smoothZoomInfoCallback)](capi-capture-session-h.md#oh_capturesession_unregistersmoothzoominfocallback) | - | 注销平滑变焦信息事件回调。 |
| [Camera\_ErrorCode OH\_CaptureSession\_SetSessionMode(Camera\_CaptureSession\* session, Camera\_SceneMode sceneMode)](capi-capture-session-h.md#oh_capturesession_setsessionmode) | - | 设置会话模式。  此接口不能在[OH\_CaptureSession\_BeginConfig](capi-capture-session-h.md#oh_capturesession_beginconfig)之后使用。  建议在使用[OH\_CameraManager\_CreateCaptureSession](capi-camera-manager-h.md#oh_cameramanager_createcapturesession)后立即使用此接口。 |
| [Camera\_ErrorCode OH\_CaptureSession\_AddSecureOutput(Camera\_CaptureSession\* session, Camera\_PreviewOutput\* previewOutput)](capi-capture-session-h.md#oh_capturesession_addsecureoutput) | - | 把其中一条PreviewOutput标记成安全输出。 |
| [Camera\_ErrorCode OH\_CaptureSession\_BeginConfig(Camera\_CaptureSession\* session)](capi-capture-session-h.md#oh_capturesession_beginconfig) | - | 开始捕获会话配置。 |
| [Camera\_ErrorCode OH\_CaptureSession\_CommitConfig(Camera\_CaptureSession\* session)](capi-capture-session-h.md#oh_capturesession_commitconfig) | - | 提交捕获会话配置。 |
| [Camera\_ErrorCode OH\_CaptureSession\_AddInput(Camera\_CaptureSession\* session, Camera\_Input\* cameraInput)](capi-capture-session-h.md#oh_capturesession_addinput) | - | 添加相机输入。 |
| [Camera\_ErrorCode OH\_CaptureSession\_RemoveInput(Camera\_CaptureSession\* session, Camera\_Input\* cameraInput)](capi-capture-session-h.md#oh_capturesession_removeinput) | - | 删除相机输入。 |
| [Camera\_ErrorCode OH\_CaptureSession\_AddPreviewOutput(Camera\_CaptureSession\* session, Camera\_PreviewOutput\* previewOutput)](capi-capture-session-h.md#oh_capturesession_addpreviewoutput) | - | 添加预览输出。 |
| [Camera\_ErrorCode OH\_CaptureSession\_RemovePreviewOutput(Camera\_CaptureSession\* session, Camera\_PreviewOutput\* previewOutput)](capi-capture-session-h.md#oh_capturesession_removepreviewoutput) | - | 删除预览输出。 |
| [Camera\_ErrorCode OH\_CaptureSession\_AddPhotoOutput(Camera\_CaptureSession\* session, Camera\_PhotoOutput\* photoOutput)](capi-capture-session-h.md#oh_capturesession_addphotooutput) | - | 添加拍照输出。 |
| [Camera\_ErrorCode OH\_CaptureSession\_RemovePhotoOutput(Camera\_CaptureSession\* session, Camera\_PhotoOutput\* photoOutput)](capi-capture-session-h.md#oh_capturesession_removephotooutput) | - | 删除拍照输出。 |
| [Camera\_ErrorCode OH\_CaptureSession\_AddVideoOutput(Camera\_CaptureSession\* session, Camera\_VideoOutput\* videoOutput)](capi-capture-session-h.md#oh_capturesession_addvideooutput) | - | 添加录像输出。 |
| [Camera\_ErrorCode OH\_CaptureSession\_RemoveVideoOutput(Camera\_CaptureSession\* session, Camera\_VideoOutput\* videoOutput)](capi-capture-session-h.md#oh_capturesession_removevideooutput) | - | 删除录像输出。 |
| [Camera\_ErrorCode OH\_CaptureSession\_AddMetadataOutput(Camera\_CaptureSession\* session, Camera\_MetadataOutput\* metadataOutput)](capi-capture-session-h.md#oh_capturesession_addmetadataoutput) | - | 添加元数据输出。 |
| [Camera\_ErrorCode OH\_CaptureSession\_RemoveMetadataOutput(Camera\_CaptureSession\* session, Camera\_MetadataOutput\* metadataOutput)](capi-capture-session-h.md#oh_capturesession_removemetadataoutput) | - | 删除元数据输出。 |
| [Camera\_ErrorCode OH\_CaptureSession\_Start(Camera\_CaptureSession\* session)](capi-capture-session-h.md#oh_capturesession_start) | - | 启动捕获会话。 |
| [Camera\_ErrorCode OH\_CaptureSession\_Stop(Camera\_CaptureSession\* session)](capi-capture-session-h.md#oh_capturesession_stop) | - | 停止捕获会话。 |
| [Camera\_ErrorCode OH\_CaptureSession\_Release(Camera\_CaptureSession\* session)](capi-capture-session-h.md#oh_capturesession_release) | - | 释放捕获会话。 |
| [Camera\_ErrorCode OH\_CaptureSession\_HasFlash(Camera\_CaptureSession\* session, bool\* hasFlash)](capi-capture-session-h.md#oh_capturesession_hasflash) | - | 检查设备是否有闪光灯。 |
| [Camera\_ErrorCode OH\_CaptureSession\_IsFlashModeSupported(Camera\_CaptureSession\* session, Camera\_FlashMode flashMode, bool\* isSupported)](capi-capture-session-h.md#oh_capturesession_isflashmodesupported) | - | 检查是否支持指定的闪光灯模式。 |
| [Camera\_ErrorCode OH\_CaptureSession\_GetFlashMode(Camera\_CaptureSession\* session, Camera\_FlashMode\* flashMode)](capi-capture-session-h.md#oh_capturesession_getflashmode) | - | 获取当前闪光灯模式。 |
| [Camera\_ErrorCode OH\_CaptureSession\_SetFlashMode(Camera\_CaptureSession\* session, Camera\_FlashMode flashMode)](capi-capture-session-h.md#oh_capturesession_setflashmode) | - | 设置闪光灯模式。 |
| [typedef void (\*OH\_CaptureSession\_OnFlashStateChange)(const Camera\_CaptureSession\* session, OH\_Camera\_FlashState flashState)](capi-capture-session-h.md#oh_capturesession_onflashstatechange) | OH\_CaptureSession\_OnFlashStateChange | 捕获会话闪光灯状态变更回调。 |
| [Camera\_ErrorCode OH\_CaptureSession\_RegisterFlashStateChangeCallback(const Camera\_CaptureSession\* session, OH\_CaptureSession\_OnFlashStateChange flashStateChange)](capi-capture-session-h.md#oh_capturesession_registerflashstatechangecallback) | - | 注册闪光灯状态变更事件回调。 |
| [Camera\_ErrorCode OH\_CaptureSession\_UnregisterFlashStateChangeCallback(const Camera\_CaptureSession\* session, OH\_CaptureSession\_OnFlashStateChange flashStateChange)](capi-capture-session-h.md#oh_capturesession_unregisterflashstatechangecallback) | - | 注销闪光灯状态变更回调。 |
| [Camera\_ErrorCode OH\_CaptureSession\_IsExposureModeSupported(Camera\_CaptureSession\* session, Camera\_ExposureMode exposureMode, bool\* isSupported)](capi-capture-session-h.md#oh_capturesession_isexposuremodesupported) | - | 检查是否支持指定的曝光模式。 |
| [Camera\_ErrorCode OH\_CaptureSession\_GetExposureMode(Camera\_CaptureSession\* session, Camera\_ExposureMode\* exposureMode)](capi-capture-session-h.md#oh_capturesession_getexposuremode) | - | 获取当前曝光模式。 |
| [Camera\_ErrorCode OH\_CaptureSession\_SetExposureMode(Camera\_CaptureSession\* session, Camera\_ExposureMode exposureMode)](capi-capture-session-h.md#oh_capturesession_setexposuremode) | - | 设置曝光模式。 |
| [Camera\_ErrorCode OH\_CaptureSession\_GetMeteringPoint(Camera\_CaptureSession\* session, Camera\_Point\* point)](capi-capture-session-h.md#oh_capturesession_getmeteringpoint) | - | 获取当前测量点。 |
| [Camera\_ErrorCode OH\_CaptureSession\_SetMeteringPoint(Camera\_CaptureSession\* session, Camera\_Point point)](capi-capture-session-h.md#oh_capturesession_setmeteringpoint) | - | 设置计量区域的中心点。 |
| [Camera\_ErrorCode OH\_CaptureSession\_IsExposureMeteringModeSupported(const Camera\_CaptureSession\* session, OH\_Camera\_ExposureMeteringMode exposureMeteringMode, bool\* isSupported)](capi-capture-session-h.md#oh_capturesession_isexposuremeteringmodesupported) | - | 查询指定曝光测光模式是否支持。 |
| [Camera\_ErrorCode OH\_CaptureSession\_GetExposureMeteringMode(const Camera\_CaptureSession\* session, OH\_Camera\_ExposureMeteringMode\* exposureMeteringMode)](capi-capture-session-h.md#oh_capturesession_getexposuremeteringmode) | - | 获取当前曝光测光模式。 |
| [Camera\_ErrorCode OH\_CaptureSession\_SetExposureMeteringMode(const Camera\_CaptureSession\* session, OH\_Camera\_ExposureMeteringMode exposureMeteringMode)](capi-capture-session-h.md#oh_capturesession_setexposuremeteringmode) | - | 设置曝光测光模式。 |
| [Camera\_ErrorCode OH\_CaptureSession\_GetSupportedISORange(const Camera\_CaptureSession\* session, int32\_t \*minIsoValue, int32\_t \*maxIsoValue)](capi-capture-session-h.md#oh_capturesession_getsupportedisorange) | - | 查询ISO感光度范围。 |
| [Camera\_ErrorCode OH\_CaptureSession\_GetIso(const Camera\_CaptureSession\* session, int32\_t\* isoValue)](capi-capture-session-h.md#oh_capturesession_getiso) | - | 获取当前ISO感光度值（遵循ISO 12232:2006标准）。 |
| [Camera\_ErrorCode OH\_CaptureSession\_SetIso(const Camera\_CaptureSession\* session, int32\_t isoValue)](capi-capture-session-h.md#oh_capturesession_setiso) | - | 设置ISO感光度值。设置的值需在[OH\_CaptureSession\_GetSupportedISORange](capi-capture-session-h.md#oh_capturesession_getsupportedisorange)范围内。当曝光锁定模式[ExposureMode](capi-camera-h.md#camera_exposuremode)为EXPOSURE\_MODE\_LOCKED时，不支持设置ISO感光度值。 |
| [Camera\_ErrorCode OH\_CaptureSession\_GetSupportedPhysicalApertures(const Camera\_CaptureSession\* session, OH\_Camera\_PhysicalAperture\*\* apertures, uint32\_t\* size)](capi-capture-session-h.md#oh_capturesession_getsupportedphysicalapertures) | - | 获取支持的物理光圈列表。调用[OH\_CaptureSession\_DeletePhysicalApertures](capi-capture-session-h.md#oh_capturesession_deletephysicalapertures)删除支持的物理光圈列表。 |
| [Camera\_ErrorCode OH\_CaptureSession\_DeletePhysicalApertures(const Camera\_CaptureSession\* session, OH\_Camera\_PhysicalAperture\* apertures, uint32\_t size)](capi-capture-session-h.md#oh_capturesession_deletephysicalapertures) | - | 删除支持的物理光圈列表。 |
| [Camera\_ErrorCode OH\_CaptureSession\_GetPhysicalAperture(const Camera\_CaptureSession\* session, double\* aperture)](capi-capture-session-h.md#oh_capturesession_getphysicalaperture) | - | 获取当前物理光圈值。 |
| [Camera\_ErrorCode OH\_CaptureSession\_SetPhysicalAperture(const Camera\_CaptureSession\* session, double aperture)](capi-capture-session-h.md#oh_capturesession_setphysicalaperture) | - | 设置物理光圈值。设置前，建议通过[OH\_CaptureSession\_GetSupportedPhysicalApertures](capi-capture-session-h.md#oh_capturesession_getsupportedphysicalapertures)获取支持的物理光圈列表。 |
| [Camera\_ErrorCode OH\_CaptureSession\_GetExposureBiasRange(Camera\_CaptureSession\* session, float\* minExposureBias, float\* maxExposureBias, float\* step)](capi-capture-session-h.md#oh_capturesession_getexposurebiasrange) | - | 查询曝光补偿范围。 |
| [Camera\_ErrorCode OH\_CaptureSession\_SetExposureBias(Camera\_CaptureSession\* session, float exposureBias)](capi-capture-session-h.md#oh_capturesession_setexposurebias) | - | 设置曝光补偿。设置前，建议通过[OH\_CaptureSession\_GetExposureBiasRange](capi-capture-session-h.md#oh_capturesession_getexposurebiasrange)获取支持配置的曝光补偿范围。 |
| [Camera\_ErrorCode OH\_CaptureSession\_GetExposureBias(Camera\_CaptureSession\* session, float\* exposureBias)](capi-capture-session-h.md#oh_capturesession_getexposurebias) | - | 获取当前曝光补偿。 |
| [Camera\_ErrorCode OH\_CaptureSession\_GetSupportedExposureDurationRange(const Camera\_CaptureSession\* session, int32\_t\* minExposureDuration, int32\_t\* maxExposureDuration)](capi-capture-session-h.md#oh_capturesession_getsupportedexposuredurationrange) | - | 获取支持的曝光时间范围。单位：微秒。 |
| [Camera\_ErrorCode OH\_CaptureSession\_SetExposureDuration(const Camera\_CaptureSession\* session, int32\_t exposureDuration)](capi-capture-session-h.md#oh_capturesession_setexposureduration) | - | 设置曝光时间。单位：微秒。若传感器无法精确使用该曝光时间，系统会自动调整为最近的支持值，并通过[OH\_CaptureSession\_OnExposureDurationChange](capi-capture-session-h.md#oh_capturesession_onexposuredurationchange)回调通知。仅在[ExposureMode](capi-camera-h.md#camera_exposuremode).EXPOSURE\_MODE\_MANUAL手动曝光模式下设置生效。 |
| [Camera\_ErrorCode OH\_CaptureSession\_GetExposureDuration(const Camera\_CaptureSession\* session, int32\_t\* exposureDuration)](capi-capture-session-h.md#oh_capturesession_getexposureduration) | - | 获取当前曝光时间。单位：微秒。 |
| [typedef void (\*OH\_CaptureSession\_OnExposureDurationChange)(const Camera\_CaptureSession\* session, int32\_t exposureDuration)](capi-capture-session-h.md#oh_capturesession_onexposuredurationchange) | OH\_CaptureSession\_OnExposureDurationChange | 捕获会话曝光时间变更回调。 |
| [Camera\_ErrorCode OH\_CaptureSession\_RegisterExposureInfoChangeCallback(const Camera\_CaptureSession\* session, OH\_CaptureSession\_OnExposureDurationChange exposureDurationChange)](capi-capture-session-h.md#oh_capturesession_registerexposureinfochangecallback) | - | 注册曝光信息变更事件回调，曝光参数变更后系统会返回更新后的曝光信息。 |
| [Camera\_ErrorCode OH\_CaptureSession\_UnregisterExposureInfoChangeCallback(const Camera\_CaptureSession\* session, OH\_CaptureSession\_OnExposureDurationChange exposureDurationChange)](capi-capture-session-h.md#oh_capturesession_unregisterexposureinfochangecallback) | - | 注销曝光信息变更回调，相机操作完成后调用该方法。 |
| [Camera\_ErrorCode OH\_CaptureSession\_IsFocusModeSupported(Camera\_CaptureSession\* session, Camera\_FocusMode focusMode, bool\* isSupported)](capi-capture-session-h.md#oh_capturesession_isfocusmodesupported) | - | 检查是否支持指定的聚焦模式。 |
| [Camera\_ErrorCode OH\_CaptureSession\_GetFocusMode(Camera\_CaptureSession\* session, Camera\_FocusMode\* focusMode)](capi-capture-session-h.md#oh_capturesession_getfocusmode) | - | 获取当前聚焦模式。 |
| [Camera\_ErrorCode OH\_CaptureSession\_SetFocusMode(Camera\_CaptureSession\* session, Camera\_FocusMode focusMode)](capi-capture-session-h.md#oh_capturesession_setfocusmode) | - | 设置聚焦模式。 |
| [Camera\_ErrorCode OH\_CaptureSession\_GetFocusPoint(Camera\_CaptureSession\* session, Camera\_Point\* focusPoint)](capi-capture-session-h.md#oh_capturesession_getfocuspoint) | - | 获取当前焦点。 |
| [Camera\_ErrorCode OH\_CaptureSession\_SetFocusPoint(Camera\_CaptureSession\* session, Camera\_Point focusPoint)](capi-capture-session-h.md#oh_capturesession_setfocuspoint) | - | 设置焦点。 |
| [Camera\_ErrorCode OH\_CaptureSession\_GetZoomRatioRange(Camera\_CaptureSession\* session, float\* minZoom, float\* maxZoom)](capi-capture-session-h.md#oh_capturesession_getzoomratiorange) | - | 获取所有支持的缩放比例范围。 |
| [Camera\_ErrorCode OH\_CaptureSession\_GetZoomRatio(Camera\_CaptureSession\* session, float\* zoom)](capi-capture-session-h.md#oh_capturesession_getzoomratio) | - | 获取当前缩放比例。 |
| [Camera\_ErrorCode OH\_CaptureSession\_SetZoomRatio(Camera\_CaptureSession\* session, float zoom)](capi-capture-session-h.md#oh_capturesession_setzoomratio) | - | 设置缩放比例。设置前，建议通过[OH\_CaptureSession\_GetZoomRatioRange](capi-capture-session-h.md#oh_capturesession_getzoomratiorange)获取支持的缩放比例范围。 |
| [Camera\_ErrorCode OH\_CaptureSession\_IsVideoStabilizationModeSupported(Camera\_CaptureSession\* session, Camera\_VideoStabilizationMode mode, bool\* isSupported)](capi-capture-session-h.md#oh_capturesession_isvideostabilizationmodesupported) | - | 检查是否支持指定的录像防抖模式。 |
| [Camera\_ErrorCode OH\_CaptureSession\_GetVideoStabilizationMode(Camera\_CaptureSession\* session, Camera\_VideoStabilizationMode\* mode)](capi-capture-session-h.md#oh_capturesession_getvideostabilizationmode) | - | 获取当前录像防抖模式。 |
| [Camera\_ErrorCode OH\_CaptureSession\_SetVideoStabilizationMode(Camera\_CaptureSession\* session, Camera\_VideoStabilizationMode mode)](capi-capture-session-h.md#oh_capturesession_setvideostabilizationmode) | - | 设置录像防抖模式。 |
| [Camera\_ErrorCode OH\_CaptureSession\_CanAddInput(Camera\_CaptureSession\* session, Camera\_Input\* cameraInput, bool\* isSuccessful)](capi-capture-session-h.md#oh_capturesession_canaddinput) | - | 确定是否可以将相机输入添加到会话中。 |
| [Camera\_ErrorCode OH\_CaptureSession\_CanAddPreviewOutput(Camera\_CaptureSession\* session, Camera\_PreviewOutput\* cameraOutput, bool\* isSuccessful)](capi-capture-session-h.md#oh_capturesession_canaddpreviewoutput) | - | 确定是否可以将相机预览输出添加到会话中。 |
| [Camera\_ErrorCode OH\_CaptureSession\_CanAddPhotoOutput(Camera\_CaptureSession\* session, Camera\_PhotoOutput\* cameraOutput, bool\* isSuccessful)](capi-capture-session-h.md#oh_capturesession_canaddphotooutput) | - | 确定是否可以将拍照输出添加到会话中。 |
| [Camera\_ErrorCode OH\_CaptureSession\_CanAddVideoOutput(Camera\_CaptureSession\* session, Camera\_VideoOutput\* cameraOutput, bool\* isSuccessful)](capi-capture-session-h.md#oh_capturesession_canaddvideooutput) | - | 确定是否可以将录像输出添加到会话中。 |
| [Camera\_ErrorCode OH\_CaptureSession\_CanPreconfig(Camera\_CaptureSession\* session, Camera\_PreconfigType preconfigType, bool\* canPreconfig)](capi-capture-session-h.md#oh_capturesession_canpreconfig) | - | 检查是否支持指定的预配置类型。 |
| [Camera\_ErrorCode OH\_CaptureSession\_CanPreconfigWithRatio(Camera\_CaptureSession\* session, Camera\_PreconfigType preconfigType, Camera\_PreconfigRatio preconfigRatio, bool\* canPreconfig)](capi-capture-session-h.md#oh_capturesession_canpreconfigwithratio) | - | 检查是否支持带比例的预配置类型。 |
| [Camera\_ErrorCode OH\_CaptureSession\_Preconfig(Camera\_CaptureSession\* session, Camera\_PreconfigType preconfigType)](capi-capture-session-h.md#oh_capturesession_preconfig) | - | 设置预配置类型。 |
| [Camera\_ErrorCode OH\_CaptureSession\_PreconfigWithRatio(Camera\_CaptureSession\* session, Camera\_PreconfigType preconfigType, Camera\_PreconfigRatio preconfigRatio)](capi-capture-session-h.md#oh_capturesession_preconfigwithratio) | - | 设置带有比例的预配置类型。 |
| [Camera\_ErrorCode OH\_CaptureSession\_GetExposureValue(Camera\_CaptureSession\* session, float\* exposureValue)](capi-capture-session-h.md#oh_capturesession_getexposurevalue) | - | 查询曝光值。 |
| [Camera\_ErrorCode OH\_CaptureSession\_GetFocalLength(Camera\_CaptureSession\* session, float\* focalLength)](capi-capture-session-h.md#oh_capturesession_getfocallength) | - | 获取当前焦距值。 |
| [Camera\_ErrorCode OH\_CaptureSession\_GetFocusDistance(const Camera\_CaptureSession\* session, float\* focusDistance)](capi-capture-session-h.md#oh_capturesession_getfocusdistance) | - | 获取当前对焦距离。取值范围为[0.0, 1.0]。0.0表示镜头可对焦的最近距离；1.0表示最远距离。默认值为1.0。 |
| [Camera\_ErrorCode OH\_CaptureSession\_SetFocusDistance(const Camera\_CaptureSession\* session, float focusDistance)](capi-capture-session-h.md#oh_capturesession_setfocusdistance) | - | 设置对焦距离。取值范围为[0.0, 1.0]。0.0表示镜头可对焦的最近距离；1.0表示最远距离。默认值为1.0。 |
| [Camera\_ErrorCode OH\_CaptureSession\_IsFocusDistanceSupported(const Camera\_CaptureSession\* session, bool\* isSupported)](capi-capture-session-h.md#oh_capturesession_isfocusdistancesupported) | - | 查询是否支持对焦距离设置。 |
| [Camera\_ErrorCode OH\_CaptureSession\_SetSmoothZoom(Camera\_CaptureSession\* session, float targetZoom, Camera\_SmoothZoomMode smoothZoomMode)](capi-capture-session-h.md#oh_capturesession_setsmoothzoom) | - | 触发平滑变焦。 |
| [Camera\_ErrorCode OH\_CaptureSession\_GetSupportedColorSpaces(Camera\_CaptureSession\* session, OH\_NativeBuffer\_ColorSpace\*\* colorSpace, uint32\_t\* size)](capi-capture-session-h.md#oh_capturesession_getsupportedcolorspaces) | - | 获取支持的色彩空间列表。 |
| [Camera\_ErrorCode OH\_CaptureSession\_DeleteColorSpaces(Camera\_CaptureSession\* session, OH\_NativeBuffer\_ColorSpace\* colorSpace)](capi-capture-session-h.md#oh_capturesession_deletecolorspaces) | - | 删除色彩空间列表。 |
| [Camera\_ErrorCode OH\_CaptureSession\_GetActiveColorSpace(Camera\_CaptureSession\* session, OH\_NativeBuffer\_ColorSpace\* colorSpace)](capi-capture-session-h.md#oh_capturesession_getactivecolorspace) | - | 获取当前色彩空间。 |
| [Camera\_ErrorCode OH\_CaptureSession\_SetActiveColorSpace(Camera\_CaptureSession\* session, OH\_NativeBuffer\_ColorSpace colorSpace)](capi-capture-session-h.md#oh_capturesession_setactivecolorspace) | - | 设置当前色彩空间。设置的值需在[OH\_CaptureSession\_GetSupportedColorSpaces](capi-capture-session-h.md#oh_capturesession_getsupportedcolorspaces)获取的支持列表中。 |
| [Camera\_ErrorCode OH\_CaptureSession\_RegisterAutoDeviceSwitchStatusCallback(Camera\_CaptureSession\* session, OH\_CaptureSession\_OnAutoDeviceSwitchStatusChange autoDeviceSwitchStatusChange)](capi-capture-session-h.md#oh_capturesession_registerautodeviceswitchstatuscallback) | - | 注册设备切换事件回调。 |
| [Camera\_ErrorCode OH\_CaptureSession\_UnregisterAutoDeviceSwitchStatusCallback(Camera\_CaptureSession\* session, OH\_CaptureSession\_OnAutoDeviceSwitchStatusChange autoDeviceSwitchStatusChange)](capi-capture-session-h.md#oh_capturesession_unregisterautodeviceswitchstatuscallback) | - | 注销设备切换事件回调。 |
| [Camera\_ErrorCode OH\_CaptureSession\_IsAutoDeviceSwitchSupported(Camera\_CaptureSession\* session, bool\* isSupported)](capi-capture-session-h.md#oh_capturesession_isautodeviceswitchsupported) | - | 检查是否支持自动设备切换。 |
| [Camera\_ErrorCode OH\_CaptureSession\_EnableAutoDeviceSwitch(Camera\_CaptureSession\* session, bool enabled)](capi-capture-session-h.md#oh_capturesession_enableautodeviceswitch) | - | 是否启用相机设备的自动切换。 |
| [Camera\_ErrorCode OH\_CaptureSession\_RegisterSystemPressureLevelChangeCallback(Camera\_CaptureSession\* session, OH\_CaptureSession\_OnSystemPressureLevelChange systemPressureLevelChange)](capi-capture-session-h.md#oh_capturesession_registersystempressurelevelchangecallback) | - | 注册系统压力状态变化回调。 |
| [Camera\_ErrorCode OH\_CaptureSession\_UnregisterSystemPressureLevelChangeCallback(Camera\_CaptureSession\* session, OH\_CaptureSession\_OnSystemPressureLevelChange systemPressureLevelChange)](capi-capture-session-h.md#oh_capturesession_unregistersystempressurelevelchangecallback) | - | 注销系统压力状态变化回调。 |
| [Camera\_ErrorCode OH\_CaptureSession\_SetQualityPrioritization(Camera\_CaptureSession\* session, Camera\_QualityPrioritization qualityPrioritization)](capi-capture-session-h.md#oh_capturesession_setqualityprioritization) | - | 设置录像质量优先级。  默认为高录像质量，设置为功耗平衡将降低录像质量以减少功耗。实际功耗收益因平台而异。建议该接口在[OH\_CaptureSession\_CommitConfig](capi-capture-session-h.md#oh_capturesession_commitconfig)和[OH\_CaptureSession\_Start](capi-capture-session-h.md#oh_capturesession_start)之间调用。 |
| [Camera\_ErrorCode OH\_CaptureSession\_IsMacroSupported(Camera\_CaptureSession\* session, bool\* isSupported)](capi-capture-session-h.md#oh_capturesession_ismacrosupported) | - | 检查是否支持微距能力。 |
| [Camera\_ErrorCode OH\_CaptureSession\_EnableMacro(Camera\_CaptureSession\* session, bool enabled)](capi-capture-session-h.md#oh_capturesession_enablemacro) | - | 是否启用相机设备的微距能力。 |
| [Camera\_ErrorCode OH\_CaptureSession\_SetWhiteBalance(Camera\_CaptureSession\* session, int32\_t colorTemperature)](capi-capture-session-h.md#oh_capturesession_setwhitebalance) | - | 设置白平衡的色温。  设置前，建议通过[OH\_CaptureSession\_GetWhiteBalanceRange](capi-capture-session-h.md#oh_capturesession_getwhitebalancerange)获取支持配置的白平衡色温范围。 |
| [Camera\_ErrorCode OH\_CaptureSession\_GetColorTintRange(const Camera\_CaptureSession\* session, int32\_t \*minColorTint, int32\_t \*maxColorTint)](capi-capture-session-h.md#oh_capturesession_getcolortintrange) | - | 获取支持配置的白平衡色调调节范围。 |
| [Camera\_ErrorCode OH\_CaptureSession\_GetColorTint(const Camera\_CaptureSession\* session, int32\_t \*colorTint)](capi-capture-session-h.md#oh_capturesession_getcolortint) | - | 获取当前白平衡的色调调节值。 |
| [Camera\_ErrorCode OH\_CaptureSession\_SetColorTint(Camera\_CaptureSession\* session, int32\_t colorTint)](capi-capture-session-h.md#oh_capturesession_setcolortint) | - | 设置白平衡的色调调节值。设置前，建议通过[OH\_CaptureSession\_GetColorTintRange](capi-capture-session-h.md#oh_capturesession_getcolortintrange)获取支持配置的白平衡色调调节范围。 |
| [Camera\_ErrorCode OH\_CaptureSession\_GetWhiteBalance(Camera\_CaptureSession\* session, int32\_t \*colorTemperature)](capi-capture-session-h.md#oh_capturesession_getwhitebalance) | - | 获取当前白平衡色温值。 |
| [Camera\_ErrorCode OH\_CaptureSession\_GetWhiteBalanceMode(Camera\_CaptureSession\* session, Camera\_WhiteBalanceMode\* whiteBalanceMode)](capi-capture-session-h.md#oh_capturesession_getwhitebalancemode) | - | 获取当前的白平衡模式。 |
| [Camera\_ErrorCode OH\_CaptureSession\_IsWhiteBalanceModeSupported(Camera\_CaptureSession\* session, Camera\_WhiteBalanceMode whiteBalanceMode, bool\* isSupported)](capi-capture-session-h.md#oh_capturesession_iswhitebalancemodesupported) | - | 检查是否支持指定的白平衡模式。 |
| [Camera\_ErrorCode OH\_CaptureSession\_SetWhiteBalanceMode(Camera\_CaptureSession\* session, Camera\_WhiteBalanceMode whiteBalanceMode)](capi-capture-session-h.md#oh_capturesession_setwhitebalancemode) | - | 设置白平衡模式。 |
| [Camera\_ErrorCode OH\_CaptureSession\_GetWhiteBalanceRange(Camera\_CaptureSession\* session, int32\_t \*minColorTemperature, int32\_t \*maxColorTemperature)](capi-capture-session-h.md#oh_capturesession_getwhitebalancerange) | - | 获取支持配置的白平衡色温范围。 |
| [Camera\_ErrorCode OH\_CaptureSession\_IsControlCenterSupported(Camera\_CaptureSession\* session, bool\* isSupported)](capi-capture-session-h.md#oh_capturesession_iscontrolcentersupported) | - | 检查是否支持相机控制器。 |
| [Camera\_ErrorCode OH\_CaptureSession\_GetSupportedEffectTypes(Camera\_CaptureSession\* session, Camera\_ControlCenterEffectType\*\* types, uint32\_t\* size)](capi-capture-session-h.md#oh_capturesession_getsupportedeffecttypes) | - | 获取相机控制器支持的效果类型。 |
| [Camera\_ErrorCode OH\_CaptureSession\_DeleteSupportedEffectTypes(Camera\_CaptureSession\* session, Camera\_ControlCenterEffectType\* types, uint32\_t size)](capi-capture-session-h.md#oh_capturesession_deletesupportedeffecttypes) | - | 删除相机控制器效果类型列表。 |
| [Camera\_ErrorCode OH\_CaptureSession\_EnableControlCenter(Camera\_CaptureSession\* session, bool enabled)](capi-capture-session-h.md#oh_capturesession_enablecontrolcenter) | - | 是否启用相机控制器。 |
| [Camera\_ErrorCode OH\_CaptureSession\_RegisterControlCenterEffectStatusChangeCallback(Camera\_CaptureSession\* session, OH\_CaptureSession\_OnControlCenterEffectStatusChange controlCenterEffectStatusChange)](capi-capture-session-h.md#oh_capturesession_registercontrolcentereffectstatuschangecallback) | - | 注册相机控制器效果激活状态变化回调。 |
| [Camera\_ErrorCode OH\_CaptureSession\_UnregisterControlCenterEffectStatusChangeCallback(Camera\_CaptureSession\* session, OH\_CaptureSession\_OnControlCenterEffectStatusChange controlCenterEffectStatusChange)](capi-capture-session-h.md#oh_capturesession_unregistercontrolcentereffectstatuschangecallback) | - | 注销相机控制器效果激活状态变化回调。 |
| [typedef void (\*OH\_CaptureSession\_OnMacroStatusChange)(Camera\_CaptureSession\* session, bool isMacroDetected)](capi-capture-session-h.md#oh_capturesession_onmacrostatuschange) | OH\_CaptureSession\_OnMacroStatusChange | 相机会话微距状态改变回调。 |
| [Camera\_ErrorCode OH\_CaptureSession\_RegisterMacroStatusChangeCallback(Camera\_CaptureSession\* session, OH\_CaptureSession\_OnMacroStatusChange macroStatusChange)](capi-capture-session-h.md#oh_capturesession_registermacrostatuschangecallback) | - | 注册相机会话微距状态改变回调函数。 |
| [Camera\_ErrorCode OH\_CaptureSession\_UnregisterMacroStatusChangeCallback(Camera\_CaptureSession\* session, OH\_CaptureSession\_OnMacroStatusChange macroStatusChange)](capi-capture-session-h.md#oh_capturesession_unregistermacrostatuschangecallback) | - | 取消注册相机会话微距状态改变回调函数。 |
| [typedef void (\*OH\_CaptureSession\_OnIsoChange)(Camera\_CaptureSession\* session, int32\_t isoValue)](capi-capture-session-h.md#oh_capturesession_onisochange) | OH\_CaptureSession\_OnIsoChange | 用于在相机会话中监听感光度（ISO）变化的回调函数。 |
| [Camera\_ErrorCode OH\_CaptureSession\_RegisterIsoChangeCallback(Camera\_CaptureSession\* session, OH\_CaptureSession\_OnIsoChange isoChange)](capi-capture-session-h.md#oh_capturesession_registerisochangecallback) | - | 注册监听感光度（ISO）改变的事件回调。 |
| [Camera\_ErrorCode OH\_CaptureSession\_UnregisterIsoChangeCallback(Camera\_CaptureSession\* session, OH\_CaptureSession\_OnIsoChange isoChange)](capi-capture-session-h.md#oh_capturesession_unregisterisochangecallback) | - | 取消注册监听感光度（ISO）改变的事件回调。 |
| [Camera\_ErrorCode OH\_CaptureSession\_GetRAWCaptureZoomRatioRange(const Camera\_CaptureSession\* session, float\* minZoom, float\* maxZoom)](capi-capture-session-h.md#oh_capturesession_getrawcapturezoomratiorange) | - | 查询物理镜头RAW图拍照支持的变焦范围。 |
| [Camera\_ErrorCode OH\_CaptureSession\_IsOISModeSupported(const Camera\_CaptureSession\* session, OH\_Camera\_OISMode oisMode, bool\* isSupported)](capi-capture-session-h.md#oh_capturesession_isoismodesupported) | - | 检查指定的光学防抖（OIS）模式是否支持。 |
| [Camera\_ErrorCode OH\_CaptureSession\_GetSupportedOISBiasRange(const Camera\_CaptureSession\* session, OH\_Camera\_OISAxes oisAxis, float\* minBias, float\* maxBias, float\* step)](capi-capture-session-h.md#oh_capturesession_getsupportedoisbiasrange) | - | 获取指定光学防抖轴支持的偏移范围。 |
| [Camera\_ErrorCode OH\_CaptureSession\_GetCurrentOISMode(const Camera\_CaptureSession\* session, OH\_Camera\_OISMode\* oisMode)](capi-capture-session-h.md#oh_capturesession_getcurrentoismode) | - | 获取当前光学防抖（OIS）模式。 |
| [Camera\_ErrorCode OH\_CaptureSession\_GetCurrentCustomOISBias(const Camera\_CaptureSession\* session, float\* pitchBias, float\* yawBias)](capi-capture-session-h.md#oh_capturesession_getcurrentcustomoisbias) | - | 获取所有光学防抖轴当前的自定义偏移值。 |
| [Camera\_ErrorCode OH\_CaptureSession\_SetOISMode(const Camera\_CaptureSession\* session, OH\_Camera\_OISMode oisMode)](capi-capture-session-h.md#oh_capturesession_setoismode) | - | 设置光学防抖（OIS）模式。 |
| [Camera\_ErrorCode OH\_CaptureSession\_SetOISModeCustom(const Camera\_CaptureSession\* session, float pitchBias, float yawBias)](capi-capture-session-h.md#oh_capturesession_setoismodecustom) | - | 为对应轴设置自定义光学防抖偏移值。设置前，建议通过[OH\_CaptureSession\_GetSupportedOISBiasRange](capi-capture-session-h.md#oh_capturesession_getsupportedoisbiasrange)获取对应轴支持的偏移范围。 |
| [typedef void (\*OH\_CaptureSession\_OnExposureStateChange)(void\* context, OH\_Camera\_ExposureState exposureState)](capi-capture-session-h.md#oh_capturesession_onexposurestatechange) | OH\_CaptureSession\_OnExposureStateChange | 定义曝光状态变更时的回调函数。 |
| [Camera\_ErrorCode OH\_CaptureSession\_RegisterExposureStateChangeCallback(const Camera\_CaptureSession\* session, void\* context, OH\_CaptureSession\_OnExposureStateChange callback)](capi-capture-session-h.md#oh_capturesession_registerexposurestatechangecallback) | - | 注册曝光状态变化的回调。注册此回调后，当捕获会话中的曝光状态发生变化时，将调用该回调。 |
| [Camera\_ErrorCode OH\_CaptureSession\_UnregisterExposureStateChangeCallback(const Camera\_CaptureSession\* session, void\* context, OH\_CaptureSession\_OnExposureStateChange callback)](capi-capture-session-h.md#oh_capturesession_unregisterexposurestatechangecallback) | - | 注销曝光状态变更时的回调函数。 |
| [Camera\_ErrorCode OH\_CaptureSession\_GetZoomPointInfos(const Camera\_CaptureSession\* session, uint32\_t\* size, OH\_Camera\_ZoomPointInfo\*\* zoomPointInfo)](capi-capture-session-h.md#oh_capturesession_getzoompointinfos) | - | 获取变焦点信息。  需要通过调用[OH\_CaptureSession\_DeleteZoomPointInfos](capi-capture-session-h.md#oh_capturesession_deletezoompointinfos)来释放变焦点信息的内存。 |
| [Camera\_ErrorCode OH\_CaptureSession\_DeleteZoomPointInfos(const Camera\_CaptureSession\* session, OH\_Camera\_ZoomPointInfo\* zoomPointInfo)](capi-capture-session-h.md#oh_capturesession_deletezoompointinfos) | - | 删除变焦点信息。 |
| [bool OH\_CaptureSession\_IsLockFocusTrackingSupported(const Camera\_CaptureSession\* session)](capi-capture-session-h.md#oh_capturesession_islockfocustrackingsupported) | - | 查询是否支持锁定焦点跟踪。 |
| [Camera\_ErrorCode OH\_CaptureSession\_LockFocusTracking(Camera\_CaptureSession\* session, Camera\_Point focusPoint)](capi-capture-session-h.md#oh_capturesession_lockfocustracking) | - | 锁定焦点跟踪，可通过[OH\_CaptureSession\_UnlockFocusTracking](capi-capture-session-h.md#oh_capturesession_unlockfocustracking)解锁。 |
| [Camera\_ErrorCode OH\_CaptureSession\_UnlockFocusTracking(Camera\_CaptureSession\* session)](capi-capture-session-h.md#oh_capturesession_unlockfocustracking) | - | 解锁焦点跟踪。 |

## 函数说明

### OH\_CaptureSession\_OnFocusStateChange()

```c
typedef void (*OH_CaptureSession_OnFocusStateChange)(Camera_CaptureSession* session, Camera_FocusState focusState)
```

**描述**

在[CaptureSession\_Callbacks](capi-oh-camera-capturesession-callbacks.md)中被调用的捕获会话焦点状态回调。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_CaptureSession](capi-oh-camera-camera-capturesession.md)\* session | 传递回调的Camera\_CaptureSession实例。 |
| [Camera\_FocusState](capi-camera-h.md#camera_focusstate) focusState | 回调传递的会话焦点状态。 |

### OH\_CaptureSession\_OnError()

```c
typedef void (*OH_CaptureSession_OnError)(Camera_CaptureSession* session, Camera_ErrorCode errorCode)
```

**描述**

在[CaptureSession\_Callbacks](capi-oh-camera-capturesession-callbacks.md)中被调用的捕获会话错误回调。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_CaptureSession](capi-oh-camera-camera-capturesession.md)\* session | 传递回调的Camera\_CaptureSession实例。 |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) errorCode | 捕获会话的错误码。 |

**参考：**

[CAMERA\_SERVICE\_FATAL\_ERROR](capi-camera-h.md#camera_errorcode)

### OH\_CaptureSession\_OnSmoothZoomInfo()

```c
typedef void (*OH_CaptureSession_OnSmoothZoomInfo)(Camera_CaptureSession* session, Camera_SmoothZoomInfo* smoothZoomInfo)
```

**描述**

拍照会话平滑变焦信息回调，触发平滑变焦后该回调会返回。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_CaptureSession](capi-oh-camera-camera-capturesession.md)\* session | 传递回调的Camera\_CaptureSession实例。 |
| [Camera\_SmoothZoomInfo](capi-oh-camera-camera-smoothzoominfo.md)\* smoothZoomInfo | 回调传递的平滑变焦参数信息。 |

### OH\_CaptureSession\_OnAutoDeviceSwitchStatusChange()

```c
typedef void (*OH_CaptureSession_OnAutoDeviceSwitchStatusChange)(Camera_CaptureSession* session, Camera_AutoDeviceSwitchStatusInfo* autoDeviceSwitchStatusInfo)
```

**描述**

捕获会话设备切换状态回调。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_CaptureSession](capi-oh-camera-camera-capturesession.md)\* session | 传递回调的Camera\_CaptureSession实例。 |
| [Camera\_AutoDeviceSwitchStatusInfo](capi-oh-camera-camera-autodeviceswitchstatusinfo.md)\* autoDeviceSwitchStatusInfo | 回调传递的设备切换状态信息。 |

### OH\_CaptureSession\_OnSystemPressureLevelChange()

```c
typedef void (*OH_CaptureSession_OnSystemPressureLevelChange)(Camera_CaptureSession* session, Camera_SystemPressureLevel systemPressureLevel)
```

**描述**

捕获系统压力状态变化回调。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_CaptureSession](capi-oh-camera-camera-capturesession.md)\* session | 传递回调的Camera\_CaptureSession实例。 |
| [Camera\_SystemPressureLevel](capi-camera-h.md#camera_systempressurelevel) systemPressureLevel | 回调传递的系统压力等级。 |

### OH\_CaptureSession\_OnControlCenterEffectStatusChange()

```c
typedef void (*OH_CaptureSession_OnControlCenterEffectStatusChange)(Camera_CaptureSession* session, Camera_ControlCenterStatusInfo* controlCenterStatusInfo)
```

**描述**

相机控制器效果激活状态变化回调。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_CaptureSession](capi-oh-camera-camera-capturesession.md)\* session | 传递回调的Camera\_CaptureSession实例。 |
| [Camera\_ControlCenterStatusInfo](capi-oh-camera-camera-controlcenterstatusinfo.md)\* controlCenterStatusInfo | 回调传递的相机控制器效果激活状态。 |

### OH\_CaptureSession\_RegisterCallback()

```c
Camera_ErrorCode OH_CaptureSession_RegisterCallback(Camera_CaptureSession* session, CaptureSession_Callbacks* callback)
```

**描述**

注册捕获会话事件回调。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_CaptureSession](capi-oh-camera-camera-capturesession.md)\* session | 传递回调的Camera\_CaptureSession实例。 |
| [CaptureSession\_Callbacks](capi-oh-camera-capturesession-callbacks.md)\* callback | 要注册的捕获会话事件回调。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。 |

### OH\_CaptureSession\_UnregisterCallback()

```c
Camera_ErrorCode OH_CaptureSession_UnregisterCallback(Camera_CaptureSession* session, CaptureSession_Callbacks* callback)
```

**描述**

注销捕获会话事件回调。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_CaptureSession](capi-oh-camera-camera-capturesession.md)\* session | 传递回调的Camera\_CaptureSession实例。 |
| [CaptureSession\_Callbacks](capi-oh-camera-capturesession-callbacks.md)\* callback | 要注销的捕获会话事件回调。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。 |

### OH\_CaptureSession\_RegisterSmoothZoomInfoCallback()

```c
Camera_ErrorCode OH_CaptureSession_RegisterSmoothZoomInfoCallback(Camera_CaptureSession* session, OH_CaptureSession_OnSmoothZoomInfo smoothZoomInfoCallback)
```

**描述**

注册平滑变焦信息事件回调。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_CaptureSession](capi-oh-camera-camera-capturesession.md)\* session | 传递回调的Camera\_CaptureSession实例。 |
| [OH\_CaptureSession\_OnSmoothZoomInfo](capi-capture-session-h.md#oh_capturesession_onsmoothzoominfo) smoothZoomInfoCallback | 要注册的平滑变焦信息事件回调。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。 |

### OH\_CaptureSession\_UnregisterSmoothZoomInfoCallback()

```c
Camera_ErrorCode OH_CaptureSession_UnregisterSmoothZoomInfoCallback(Camera_CaptureSession* session, OH_CaptureSession_OnSmoothZoomInfo smoothZoomInfoCallback)
```

**描述**

注销平滑变焦信息事件回调。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_CaptureSession](capi-oh-camera-camera-capturesession.md)\* session | 传递回调的Camera\_CaptureSession实例。 |
| [OH\_CaptureSession\_OnSmoothZoomInfo](capi-capture-session-h.md#oh_capturesession_onsmoothzoominfo) smoothZoomInfoCallback | 要注销的平滑变焦信息事件回调。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。 |

### OH\_CaptureSession\_SetSessionMode()

```c
Camera_ErrorCode OH_CaptureSession_SetSessionMode(Camera_CaptureSession* session, Camera_SceneMode sceneMode)
```

**描述**

设置会话模式。

此接口不能在[OH\_CaptureSession\_BeginConfig](capi-capture-session-h.md#oh_capturesession_beginconfig)之后使用。

建议在使用[OH\_CameraManager\_CreateCaptureSession](capi-camera-manager-h.md#oh_cameramanager_createcapturesession)后立即使用此接口。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_CaptureSession](capi-oh-camera-camera-capturesession.md)\* session | Camera\_CaptureSession实例。 |
| [Camera\_SceneMode](capi-camera-h.md#camera_scenemode) sceneMode | 相机模式。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。  CAMERA\_OPERATION\_NOT\_ALLOWED：操作不允许。  CAMERA\_SESSION\_CONFIG\_LOCKED：会话配置已锁定。 |

### OH\_CaptureSession\_AddSecureOutput()

```c
Camera_ErrorCode OH_CaptureSession_AddSecureOutput(Camera_CaptureSession* session, Camera_PreviewOutput* previewOutput)
```

**描述**

把其中一条PreviewOutput标记成安全输出。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_CaptureSession](capi-oh-camera-camera-capturesession.md)\* session | Camera\_CaptureSession实例。 |
| [Camera\_PreviewOutput](capi-oh-camera-camera-previewoutput.md)\* previewOutput | 要标记为安全输出的Camera\_PreviewOutput。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。  CAMERA\_OPERATION\_NOT\_ALLOWED：操作不允许。  CAMERA\_SESSION\_CONFIG\_LOCKED：会话配置已锁定。 |

### OH\_CaptureSession\_BeginConfig()

```c
Camera_ErrorCode OH_CaptureSession_BeginConfig(Camera_CaptureSession* session)
```

**描述**

开始捕获会话配置。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_CaptureSession](capi-oh-camera-camera-capturesession.md)\* session | Camera\_CaptureSession实例。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。  CAMERA\_SESSION\_CONFIG\_LOCKED：会话配置已锁定。 |

### OH\_CaptureSession\_CommitConfig()

```c
Camera_ErrorCode OH_CaptureSession_CommitConfig(Camera_CaptureSession* session)
```

**描述**

提交捕获会话配置。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_CaptureSession](capi-oh-camera-camera-capturesession.md)\* session | Camera\_CaptureSession实例。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。  CAMERA\_OPERATION\_NOT\_ALLOWED：操作不允许。  CAMERA\_SERVICE\_FATAL\_ERROR：相机服务异常。 |

### OH\_CaptureSession\_AddInput()

```c
Camera_ErrorCode OH_CaptureSession_AddInput(Camera_CaptureSession* session, Camera_Input* cameraInput)
```

**描述**

添加相机输入。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_CaptureSession](capi-oh-camera-camera-capturesession.md)\* session | Camera\_CaptureSession实例。 |
| [Camera\_Input](capi-oh-camera-camera-input.md)\* cameraInput | 要添加的相机输入实例。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。  CAMERA\_OPERATION\_NOT\_ALLOWED：操作不允许。 |

### OH\_CaptureSession\_RemoveInput()

```c
Camera_ErrorCode OH_CaptureSession_RemoveInput(Camera_CaptureSession* session, Camera_Input* cameraInput)
```

**描述**

删除相机输入。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_CaptureSession](capi-oh-camera-camera-capturesession.md)\* session | Camera\_CaptureSession实例。 |
| [Camera\_Input](capi-oh-camera-camera-input.md)\* cameraInput | 要删除的相机输入实例。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。  CAMERA\_OPERATION\_NOT\_ALLOWED：操作不允许。 |

### OH\_CaptureSession\_AddPreviewOutput()

```c
Camera_ErrorCode OH_CaptureSession_AddPreviewOutput(Camera_CaptureSession* session, Camera_PreviewOutput* previewOutput)
```

**描述**

添加预览输出。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_CaptureSession](capi-oh-camera-camera-capturesession.md)\* session | Camera\_CaptureSession实例。 |
| [Camera\_PreviewOutput](capi-oh-camera-camera-previewoutput.md)\* previewOutput | 要添加的预览输出实例。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。  CAMERA\_OPERATION\_NOT\_ALLOWED：操作不允许。 |

### OH\_CaptureSession\_RemovePreviewOutput()

```c
Camera_ErrorCode OH_CaptureSession_RemovePreviewOutput(Camera_CaptureSession* session, Camera_PreviewOutput* previewOutput)
```

**描述**

删除预览输出。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_CaptureSession](capi-oh-camera-camera-capturesession.md)\* session | Camera\_CaptureSession实例。 |
| [Camera\_PreviewOutput](capi-oh-camera-camera-previewoutput.md)\* previewOutput | 要删除的预览输出实例。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。  CAMERA\_OPERATION\_NOT\_ALLOWED：操作不允许。 |

### OH\_CaptureSession\_AddPhotoOutput()

```c
Camera_ErrorCode OH_CaptureSession_AddPhotoOutput(Camera_CaptureSession* session, Camera_PhotoOutput* photoOutput)
```

**描述**

添加拍照输出。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_CaptureSession](capi-oh-camera-camera-capturesession.md)\* session | Camera\_CaptureSession实例。 |
| [Camera\_PhotoOutput](capi-oh-camera-camera-photooutput.md)\* photoOutput | 要添加的拍照输出实例。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。  CAMERA\_OPERATION\_NOT\_ALLOWED：操作不允许。 |

### OH\_CaptureSession\_RemovePhotoOutput()

```c
Camera_ErrorCode OH_CaptureSession_RemovePhotoOutput(Camera_CaptureSession* session, Camera_PhotoOutput* photoOutput)
```

**描述**

删除拍照输出。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_CaptureSession](capi-oh-camera-camera-capturesession.md)\* session | Camera\_CaptureSession实例。 |
| [Camera\_PhotoOutput](capi-oh-camera-camera-photooutput.md)\* photoOutput | 要删除的拍照输出实例。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。  CAMERA\_OPERATION\_NOT\_ALLOWED：操作不允许。 |

### OH\_CaptureSession\_AddVideoOutput()

```c
Camera_ErrorCode OH_CaptureSession_AddVideoOutput(Camera_CaptureSession* session, Camera_VideoOutput* videoOutput)
```

**描述**

添加录像输出。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_CaptureSession](capi-oh-camera-camera-capturesession.md)\* session | Camera\_CaptureSession实例。 |
| [Camera\_VideoOutput](capi-oh-camera-camera-videooutput.md)\* videoOutput | 要添加的录像输出实例。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。  CAMERA\_OPERATION\_NOT\_ALLOWED：操作不允许。 |

### OH\_CaptureSession\_RemoveVideoOutput()

```c
Camera_ErrorCode OH_CaptureSession_RemoveVideoOutput(Camera_CaptureSession* session, Camera_VideoOutput* videoOutput)
```

**描述**

删除录像输出。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_CaptureSession](capi-oh-camera-camera-capturesession.md)\* session | Camera\_CaptureSession实例。 |
| [Camera\_VideoOutput](capi-oh-camera-camera-videooutput.md)\* videoOutput | 要删除的录像输出实例。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。  CAMERA\_OPERATION\_NOT\_ALLOWED：操作不允许。 |

### OH\_CaptureSession\_AddMetadataOutput()

```c
Camera_ErrorCode OH_CaptureSession_AddMetadataOutput(Camera_CaptureSession* session, Camera_MetadataOutput* metadataOutput)
```

**描述**

添加元数据输出。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_CaptureSession](capi-oh-camera-camera-capturesession.md)\* session | Camera\_CaptureSession实例。 |
| [Camera\_MetadataOutput](capi-oh-camera-camera-metadataoutput.md)\* metadataOutput | 要添加的元数据输出实例。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。  CAMERA\_OPERATION\_NOT\_ALLOWED：操作不允许。 |

### OH\_CaptureSession\_RemoveMetadataOutput()

```c
Camera_ErrorCode OH_CaptureSession_RemoveMetadataOutput(Camera_CaptureSession* session, Camera_MetadataOutput* metadataOutput)
```

**描述**

删除元数据输出。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_CaptureSession](capi-oh-camera-camera-capturesession.md)\* session | Camera\_CaptureSession实例。 |
| [Camera\_MetadataOutput](capi-oh-camera-camera-metadataoutput.md)\* metadataOutput | 要删除的元数据输出实例。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。  CAMERA\_OPERATION\_NOT\_ALLOWED：操作不允许。 |

### OH\_CaptureSession\_Start()

```c
Camera_ErrorCode OH_CaptureSession_Start(Camera_CaptureSession* session)
```

**描述**

启动捕获会话。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_CaptureSession](capi-oh-camera-camera-capturesession.md)\* session | 要启动的Camera\_CaptureSession实例。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。  CAMERA\_SESSION\_NOT\_CONFIG：捕获会话未配置。  CAMERA\_SERVICE\_FATAL\_ERROR：相机服务异常。 |

### OH\_CaptureSession\_Stop()

```c
Camera_ErrorCode OH_CaptureSession_Stop(Camera_CaptureSession* session)
```

**描述**

停止捕获会话。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_CaptureSession](capi-oh-camera-camera-capturesession.md)\* session | 要停止的Camera\_CaptureSession实例。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。  CAMERA\_SERVICE\_FATAL\_ERROR：相机服务异常。 |

### OH\_CaptureSession\_Release()

```c
Camera_ErrorCode OH_CaptureSession_Release(Camera_CaptureSession* session)
```

**描述**

释放捕获会话。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_CaptureSession](capi-oh-camera-camera-capturesession.md)\* session | 要释放的Camera\_CaptureSession实例。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。  CAMERA\_SERVICE\_FATAL\_ERROR：相机服务异常。 |

### OH\_CaptureSession\_HasFlash()

```c
Camera_ErrorCode OH_CaptureSession_HasFlash(Camera_CaptureSession* session, bool* hasFlash)
```

**描述**

检查设备是否有闪光灯。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_CaptureSession](capi-oh-camera-camera-capturesession.md)\* session | Camera\_CaptureSession实例。 |
| bool\* hasFlash | 是否支持闪光灯的结果。返回true表示支持闪光灯，返回false表示不支持。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。  CAMERA\_SESSION\_NOT\_CONFIG：捕获会话未配置。 |

### OH\_CaptureSession\_IsFlashModeSupported()

```c
Camera_ErrorCode OH_CaptureSession_IsFlashModeSupported(Camera_CaptureSession* session, Camera_FlashMode flashMode, bool* isSupported)
```

**描述**

检查是否支持指定的闪光灯模式。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_CaptureSession](capi-oh-camera-camera-capturesession.md)\* session | Camera\_CaptureSession实例。 |
| [Camera\_FlashMode](capi-camera-h.md#camera_flashmode) flashMode | 要检查的闪光灯模式。 |
| bool\* isSupported | 是否支持闪光灯模式的结果。返回true表示支持闪光灯模式，返回false表示不支持。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。  CAMERA\_SESSION\_NOT\_CONFIG：捕获会话未配置。 |

### OH\_CaptureSession\_GetFlashMode()

```c
Camera_ErrorCode OH_CaptureSession_GetFlashMode(Camera_CaptureSession* session, Camera_FlashMode* flashMode)
```

**描述**

获取当前闪光灯模式。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_CaptureSession](capi-oh-camera-camera-capturesession.md)\* session | Camera\_CaptureSession实例。 |
| [Camera\_FlashMode](capi-camera-h.md#camera_flashmode)\* flashMode | 当前闪光灯模式。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。  CAMERA\_SESSION\_NOT\_CONFIG：捕获会话未配置。 |

### OH\_CaptureSession\_SetFlashMode()

```c
Camera_ErrorCode OH_CaptureSession_SetFlashMode(Camera_CaptureSession* session, Camera_FlashMode flashMode)
```

**描述**

设置闪光灯模式。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_CaptureSession](capi-oh-camera-camera-capturesession.md)\* session | Camera\_CaptureSession实例。 |
| [Camera\_FlashMode](capi-camera-h.md#camera_flashmode) flashMode | 要设置的闪光灯模式。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。  CAMERA\_SESSION\_NOT\_CONFIG：捕获会话未配置。 |

### OH\_CaptureSession\_OnFlashStateChange()

```c
typedef void (*OH_CaptureSession_OnFlashStateChange)(const Camera_CaptureSession* session, OH_Camera_FlashState flashState)
```

**描述**

捕获会话闪光灯状态变更回调。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [Camera\_CaptureSession](capi-oh-camera-camera-capturesession.md)\* session | 传递回调的Camera\_CaptureSession指针。 |
| [OH\_Camera\_FlashState](capi-camera-h.md#oh_camera_flashstate) flashState | 回调传递的闪光灯状态。 |

### OH\_CaptureSession\_RegisterFlashStateChangeCallback()

```c
Camera_ErrorCode OH_CaptureSession_RegisterFlashStateChangeCallback(const Camera_CaptureSession* session, OH_CaptureSession_OnFlashStateChange flashStateChange)
```

**描述**

注册闪光灯状态变更事件回调。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [Camera\_CaptureSession](capi-oh-camera-camera-capturesession.md)\* session | Camera\_CaptureSession实例指针。 |
| [OH\_CaptureSession\_OnFlashStateChange](capi-capture-session-h.md#oh_capturesession_onflashstatechange) flashStateChange | 待注册的闪光灯状态变更回调。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或者参数不正确。 |

### OH\_CaptureSession\_UnregisterFlashStateChangeCallback()

```c
Camera_ErrorCode OH_CaptureSession_UnregisterFlashStateChangeCallback(const Camera_CaptureSession* session, OH_CaptureSession_OnFlashStateChange flashStateChange)
```

**描述**

注销闪光灯状态变更回调。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [Camera\_CaptureSession](capi-oh-camera-camera-capturesession.md)\* session | Camera\_CaptureSession实例指针。 |
| [OH\_CaptureSession\_OnFlashStateChange](capi-capture-session-h.md#oh_capturesession_onflashstatechange) flashStateChange | 待注销的闪光灯状态变更回调。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或者参数不正确。 |

### OH\_CaptureSession\_IsExposureModeSupported()

```c
Camera_ErrorCode OH_CaptureSession_IsExposureModeSupported(Camera_CaptureSession* session, Camera_ExposureMode exposureMode, bool* isSupported)
```

**描述**

检查是否支持指定的曝光模式。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_CaptureSession](capi-oh-camera-camera-capturesession.md)\* session | Camera\_CaptureSession实例。 |
| [Camera\_ExposureMode](capi-camera-h.md#camera_exposuremode) exposureMode | 要检查的曝光模式。 |
| bool\* isSupported | 是否支持曝光模式的结果。返回true表示支持曝光模式，返回false表示不支持。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。  CAMERA\_SESSION\_NOT\_CONFIG：捕获会话未配置。 |

### OH\_CaptureSession\_GetExposureMode()

```c
Camera_ErrorCode OH_CaptureSession_GetExposureMode(Camera_CaptureSession* session, Camera_ExposureMode* exposureMode)
```

**描述**

获取当前曝光模式。如果未通过[OH\_CaptureSession\_SetExposureMode](capi-capture-session-h.md#oh_capturesession_setexposuremode)接口进行设置，则直接调用该接口查询当前曝光模式，会返回无效值。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_CaptureSession](capi-oh-camera-camera-capturesession.md)\* session | Camera\_CaptureSession实例。 |
| [Camera\_ExposureMode](capi-camera-h.md#camera_exposuremode)\* exposureMode | 当前的曝光模式。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。  CAMERA\_SESSION\_NOT\_CONFIG：捕获会话未配置。 |

### OH\_CaptureSession\_SetExposureMode()

```c
Camera_ErrorCode OH_CaptureSession_SetExposureMode(Camera_CaptureSession* session, Camera_ExposureMode exposureMode)
```

**描述**

设置曝光模式。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_CaptureSession](capi-oh-camera-camera-capturesession.md)\* session | Camera\_CaptureSession实例。 |
| [Camera\_ExposureMode](capi-camera-h.md#camera_exposuremode) exposureMode | 要设置的曝光模式。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。  CAMERA\_SESSION\_NOT\_CONFIG：捕获会话未配置。 |

### OH\_CaptureSession\_GetMeteringPoint()

```c
Camera_ErrorCode OH_CaptureSession_GetMeteringPoint(Camera_CaptureSession* session, Camera_Point* point)
```

**描述**

获取当前测量点。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_CaptureSession](capi-oh-camera-camera-capturesession.md)\* session | Camera\_CaptureSession实例。 |
| [Camera\_Point](capi-oh-camera-camera-point.md)\* point | 当前测量点。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。  CAMERA\_SESSION\_NOT\_CONFIG：捕获会话未配置。 |

### OH\_CaptureSession\_SetMeteringPoint()

```c
Camera_ErrorCode OH_CaptureSession_SetMeteringPoint(Camera_CaptureSession* session, Camera_Point point)
```

**描述**

设置计量区域的中心点。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_CaptureSession](capi-oh-camera-camera-capturesession.md)\* session | Camera\_CaptureSession实例。 |
| [Camera\_Point](capi-oh-camera-camera-point.md) point | 要设置的测量点。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。  CAMERA\_SESSION\_NOT\_CONFIG：捕获会话未配置。 |

### OH\_CaptureSession\_IsExposureMeteringModeSupported()

```c
Camera_ErrorCode OH_CaptureSession_IsExposureMeteringModeSupported(const Camera_CaptureSession* session, OH_Camera_ExposureMeteringMode exposureMeteringMode, bool* isSupported)
```

**描述**

查询指定曝光测光模式是否支持。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [Camera\_CaptureSession](capi-oh-camera-camera-capturesession.md)\* session | Camera\_CaptureSession实例指针。 |
| [OH\_Camera\_ExposureMeteringMode](capi-camera-h.md#oh_camera_exposuremeteringmode) exposureMeteringMode | 待检查的曝光测光模式。 |
| bool\* isSupported | 输出参数，返回曝光模式是否支持的结果。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。  CAMERA\_SESSION\_NOT\_CONFIG：捕获会话未配置。 |

### OH\_CaptureSession\_GetExposureMeteringMode()

```c
Camera_ErrorCode OH_CaptureSession_GetExposureMeteringMode(const Camera_CaptureSession* session, OH_Camera_ExposureMeteringMode* exposureMeteringMode)
```

**描述**

获取当前曝光测光模式。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [Camera\_CaptureSession](capi-oh-camera-camera-capturesession.md)\* session | Camera\_CaptureSession实例指针。 |
| [OH\_Camera\_ExposureMeteringMode](capi-camera-h.md#oh_camera_exposuremeteringmode)\* exposureMeteringMode | 输出参数，返回当前曝光测光模式。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。  CAMERA\_OPERATION\_NOT\_ALLOWED：操作不允许，会话或相机状态异常。  CAMERA\_SESSION\_NOT\_CONFIG：捕获会话未配置。 |

### OH\_CaptureSession\_SetExposureMeteringMode()

```c
Camera_ErrorCode OH_CaptureSession_SetExposureMeteringMode(const Camera_CaptureSession* session, OH_Camera_ExposureMeteringMode exposureMeteringMode)
```

**描述**

设置曝光测光模式。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [Camera\_CaptureSession](capi-oh-camera-camera-capturesession.md)\* session | Camera\_CaptureSession实例指针。 |
| [OH\_Camera\_ExposureMeteringMode](capi-camera-h.md#oh_camera_exposuremeteringmode) exposureMeteringMode | 待设置的目标曝光测光模式。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。  CAMERA\_OPERATION\_NOT\_ALLOWED：操作不允许，会话或相机状态异常。  CAMERA\_SESSION\_NOT\_CONFIG：捕获会话未配置。 |

### OH\_CaptureSession\_GetSupportedISORange()

```c
Camera_ErrorCode OH_CaptureSession_GetSupportedISORange(const Camera_CaptureSession* session, int32_t *minIsoValue, int32_t *maxIsoValue)
```

**描述**

查询ISO感光度范围。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [Camera\_CaptureSession](capi-oh-camera-camera-capturesession.md)\* session | Camera\_CaptureSession实例。 |
| int32\_t \*minIsoValue | 输出参数，返回ISO最小值。 |
| int32\_t \*maxIsoValue | 输出参数，返回ISO最大值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。  CAMERA\_OPERATION\_NOT\_ALLOWED：操作不允许，会话或相机状态异常。  CAMERA\_SESSION\_NOT\_CONFIG：捕获会话未配置。 |

### OH\_CaptureSession\_GetIso()

```c
Camera_ErrorCode OH_CaptureSession_GetIso(const Camera_CaptureSession* session, int32_t* isoValue)
```

**描述**

获取当前ISO感光度值（遵循ISO 12232:2006标准）。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [Camera\_CaptureSession](capi-oh-camera-camera-capturesession.md)\* session | Camera\_CaptureSession实例指针。 |
| int32\_t\* isoValue | 输出参数，返回当前ISO感光度值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。  CAMERA\_OPERATION\_NOT\_ALLOWED：操作不允许，会话或相机状态异常。  CAMERA\_SESSION\_NOT\_CONFIG：捕获会话未配置。 |

### OH\_CaptureSession\_SetIso()

```c
Camera_ErrorCode OH_CaptureSession_SetIso(const Camera_CaptureSession* session, int32_t isoValue)
```

**描述**

设置ISO感光度值。设置的值需在[OH\_CaptureSession\_GetSupportedISORange](capi-capture-session-h.md#oh_capturesession_getsupportedisorange)范围内。当曝光锁定模式[ExposureMode](capi-camera-h.md#camera_exposuremode)为EXPOSURE\_MODE\_LOCKED时，不支持设置ISO感光度值。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [Camera\_CaptureSession](capi-oh-camera-camera-capturesession.md)\* session | Camera\_CaptureSession实例指针。 |
| int32\_t isoValue | 待设置的目标ISO值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。  CAMERA\_OPERATION\_NOT\_ALLOWED：操作不允许，会话或相机状态异常。  CAMERA\_SESSION\_NOT\_CONFIG：捕获会话未配置。 |

### OH\_CaptureSession\_GetSupportedPhysicalApertures()

```c
Camera_ErrorCode OH_CaptureSession_GetSupportedPhysicalApertures(const Camera_CaptureSession* session, OH_Camera_PhysicalAperture** apertures, uint32_t* size)
```

**描述**

获取支持的物理光圈列表。调用[OH\_CaptureSession\_DeletePhysicalApertures](capi-capture-session-h.md#oh_capturesession_deletephysicalapertures)删除支持的物理光圈列表。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [Camera\_CaptureSession](capi-oh-camera-camera-capturesession.md)\* session | Camera\_CaptureSession实例。 |
| [OH\_Camera\_PhysicalAperture](capi-oh-camera-oh-camera-physicalaperture.md)\*\* apertures | 用于存储物理光圈值的数组指针。 |
| uint32\_t\* size | 输出物理光圈数组大小。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。  CAMERA\_OPERATION\_NOT\_ALLOWED：操作不允许，会话或相机状态异常。  CAMERA\_SESSION\_NOT\_CONFIG：捕获会话未配置。 |

### OH\_CaptureSession\_DeletePhysicalApertures()

```c
Camera_ErrorCode OH_CaptureSession_DeletePhysicalApertures(const Camera_CaptureSession* session, OH_Camera_PhysicalAperture* apertures, uint32_t size)
```

**描述**

删除支持的物理光圈列表。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [Camera\_CaptureSession](capi-oh-camera-camera-capturesession.md)\* session | Camera\_CaptureSession实例指针。 |
| [OH\_Camera\_PhysicalAperture](capi-oh-camera-oh-camera-physicalaperture.md)\* apertures | 待删除的物理光圈数组指针。 |
| uint32\_t size | 物理光圈数组大小。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。 |

### OH\_CaptureSession\_GetPhysicalAperture()

```c
Camera_ErrorCode OH_CaptureSession_GetPhysicalAperture(const Camera_CaptureSession* session, double* aperture)
```

**描述**

获取当前物理光圈值。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [Camera\_CaptureSession](capi-oh-camera-camera-capturesession.md)\* session | Camera\_CaptureSession实例。 |
| double\* aperture | 输出参数，返回当前光圈值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。  CAMERA\_OPERATION\_NOT\_ALLOWED：操作不允许，会话或相机状态异常。  CAMERA\_SESSION\_NOT\_CONFIG：捕获会话未配置。 |

### OH\_CaptureSession\_SetPhysicalAperture()

```c
Camera_ErrorCode OH_CaptureSession_SetPhysicalAperture(const Camera_CaptureSession* session, double aperture)
```

**描述**

设置物理光圈值。

设置前，建议通过[OH\_CaptureSession\_GetSupportedPhysicalApertures](capi-capture-session-h.md#oh_capturesession_getsupportedphysicalapertures)获取支持的物理光圈列表。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [Camera\_CaptureSession](capi-oh-camera-camera-capturesession.md)\* session | Camera\_CaptureSession实例。 |
| double aperture | 待设置的光圈值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。  CAMERA\_OPERATION\_NOT\_ALLOWED：操作不允许，会话或相机状态异常。  CAMERA\_SESSION\_NOT\_CONFIG：捕获会话未配置。 |

### OH\_CaptureSession\_GetExposureBiasRange()

```c
Camera_ErrorCode OH_CaptureSession_GetExposureBiasRange(Camera_CaptureSession* session, float* minExposureBias, float* maxExposureBias, float* step)
```

**描述**

查询曝光补偿范围。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_CaptureSession](capi-oh-camera-camera-capturesession.md)\* session | Camera\_CaptureSession实例。 |
| float\* minExposureBias | 曝光补偿的最小值。 |
| float\* maxExposureBias | 曝光补偿的最大值。 |
| float\* step | 每个级别之间的曝光补偿阶梯。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。  CAMERA\_SESSION\_NOT\_CONFIG：捕获会话未配置。 |

### OH\_CaptureSession\_SetExposureBias()

```c
Camera_ErrorCode OH_CaptureSession_SetExposureBias(Camera_CaptureSession* session, float exposureBias)
```

**描述**

设置曝光补偿。

设置前，建议通过[OH\_CaptureSession\_GetExposureBiasRange](capi-capture-session-h.md#oh_capturesession_getexposurebiasrange)获取支持配置的曝光补偿范围。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_CaptureSession](capi-oh-camera-camera-capturesession.md)\* session | Camera\_CaptureSession实例。 |
| float exposureBias | 要设置的曝光补偿。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。  CAMERA\_SESSION\_NOT\_CONFIG：捕获会话未配置。 |

### OH\_CaptureSession\_GetExposureBias()

```c
Camera_ErrorCode OH_CaptureSession_GetExposureBias(Camera_CaptureSession* session, float* exposureBias)
```

**描述**

获取当前曝光补偿。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_CaptureSession](capi-oh-camera-camera-capturesession.md)\* session | Camera\_CaptureSession实例。 |
| float\* exposureBias | 当前的曝光补偿。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。  CAMERA\_SESSION\_NOT\_CONFIG：捕获会话未配置。 |

### OH\_CaptureSession\_GetSupportedExposureDurationRange()

```c
Camera_ErrorCode OH_CaptureSession_GetSupportedExposureDurationRange(const Camera_CaptureSession* session, int32_t* minExposureDuration, int32_t* maxExposureDuration)
```

**描述**

获取支持的曝光时间范围。单位：微秒。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [Camera\_CaptureSession](capi-oh-camera-camera-capturesession.md)\* session | Camera\_CaptureSession实例指针。 |
| int32\_t\* minExposureDuration | 输出参数，返回曝光时间最小值。 |
| int32\_t\* maxExposureDuration | 输出参数，返回曝光时间最大值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或者参数不正确。  CAMERA\_OPERATION\_NOT\_ALLOWED：操作不允许。  CAMERA\_SESSION\_NOT\_CONFIG：捕获会话未配置。 |

### OH\_CaptureSession\_SetExposureDuration()

```c
Camera_ErrorCode OH_CaptureSession_SetExposureDuration(const Camera_CaptureSession* session, int32_t exposureDuration)
```

**描述**

设置曝光时间。单位：微秒。若传感器无法精确使用该曝光时间，系统会自动调整为最近的支持值，并通过[OH\_CaptureSession\_OnExposureDurationChange](capi-capture-session-h.md#oh_capturesession_onexposuredurationchange)回调通知。仅在[ExposureMode](capi-camera-h.md#camera_exposuremode).EXPOSURE\_MODE\_MANUAL手动曝光模式下设置生效。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [Camera\_CaptureSession](capi-oh-camera-camera-capturesession.md)\* session | Camera\_CaptureSession实例指针。 |
| int32\_t exposureDuration | 待设置的目标曝光时间。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或者参数不正确。  CAMERA\_OPERATION\_NOT\_ALLOWED：操作不允许，会话或相机状态异常。  CAMERA\_SESSION\_NOT\_CONFIG：捕获会话未配置。 |

### OH\_CaptureSession\_GetExposureDuration()

```c
Camera_ErrorCode OH_CaptureSession_GetExposureDuration(const Camera_CaptureSession* session, int32_t* exposureDuration)
```

**描述**

获取当前曝光时间。单位：微秒。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [Camera\_CaptureSession](capi-oh-camera-camera-capturesession.md)\* session | Camera\_CaptureSession实例指针。 |
| int32\_t\* exposureDuration | 输出参数，返回当前曝光时间。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或者参数不正确。  CAMERA\_OPERATION\_NOT\_ALLOWED：操作不允许，会话或相机状态异常。  CAMERA\_SESSION\_NOT\_CONFIG：捕获会话未配置。 |

### OH\_CaptureSession\_OnExposureDurationChange()

```c
typedef void (*OH_CaptureSession_OnExposureDurationChange)(const Camera_CaptureSession* session, int32_t exposureDuration)
```

**描述**

捕获会话曝光时间变更回调。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [Camera\_CaptureSession](capi-oh-camera-camera-capturesession.md)\* session | 传递回调的Camera\_CaptureSession指针。 |
| int32\_t exposureDuration | 回调传递的曝光时间。 |

### OH\_CaptureSession\_RegisterExposureInfoChangeCallback()

```c
Camera_ErrorCode OH_CaptureSession_RegisterExposureInfoChangeCallback(const Camera_CaptureSession* session, OH_CaptureSession_OnExposureDurationChange exposureDurationChange)
```

**描述**

注册曝光信息变更事件回调，曝光参数变更后系统会返回更新后的曝光信息。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [Camera\_CaptureSession](capi-oh-camera-camera-capturesession.md)\* session | Camera\_CaptureSession实例指针。 |
| [OH\_CaptureSession\_OnExposureDurationChange](capi-capture-session-h.md#oh_capturesession_onexposuredurationchange) exposureDurationChange | 待注册的曝光时间变更回调。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或者参数不正确。 |

### OH\_CaptureSession\_UnregisterExposureInfoChangeCallback()

```c
Camera_ErrorCode OH_CaptureSession_UnregisterExposureInfoChangeCallback(const Camera_CaptureSession* session, OH_CaptureSession_OnExposureDurationChange exposureDurationChange)
```

**描述**

注销曝光信息变更回调，相机操作完成后调用该方法。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [Camera\_CaptureSession](capi-oh-camera-camera-capturesession.md)\* session | Camera\_CaptureSession实例指针。 |
| [OH\_CaptureSession\_OnExposureDurationChange](capi-capture-session-h.md#oh_capturesession_onexposuredurationchange) exposureDurationChange | 待注销的曝光时间变更回调。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或者参数不正确。 |

### OH\_CaptureSession\_IsFocusModeSupported()

```c
Camera_ErrorCode OH_CaptureSession_IsFocusModeSupported(Camera_CaptureSession* session, Camera_FocusMode focusMode, bool* isSupported)
```

**描述**

检查是否支持指定的聚焦模式。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_CaptureSession](capi-oh-camera-camera-capturesession.md)\* session | Camera\_CaptureSession实例。 |
| [Camera\_FocusMode](capi-camera-h.md#camera_focusmode) focusMode | 要检查的聚焦模式。 |
| bool\* isSupported | 是否支持聚焦模式的结果。返回true表示支持聚焦模式，返回false表示不支持。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。  CAMERA\_SESSION\_NOT\_CONFIG：捕获会话未配置。 |

### OH\_CaptureSession\_GetFocusMode()

```c
Camera_ErrorCode OH_CaptureSession_GetFocusMode(Camera_CaptureSession* session, Camera_FocusMode* focusMode)
```

**描述**

获取当前聚焦模式。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_CaptureSession](capi-oh-camera-camera-capturesession.md)\* session | Camera\_CaptureSession实例。 |
| [Camera\_FocusMode](capi-camera-h.md#camera_focusmode)\* focusMode | 当前聚焦模式。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。  CAMERA\_SESSION\_NOT\_CONFIG：捕获会话未配置。 |

### OH\_CaptureSession\_SetFocusMode()

```c
Camera_ErrorCode OH_CaptureSession_SetFocusMode(Camera_CaptureSession* session, Camera_FocusMode focusMode)
```

**描述**

设置聚焦模式。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_CaptureSession](capi-oh-camera-camera-capturesession.md)\* session | Camera\_CaptureSession实例。 |
| [Camera\_FocusMode](capi-camera-h.md#camera_focusmode) focusMode | 要设置的聚焦模式。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。  CAMERA\_SESSION\_NOT\_CONFIG：捕获会话未配置。 |

### OH\_CaptureSession\_GetFocusPoint()

```c
Camera_ErrorCode OH_CaptureSession_GetFocusPoint(Camera_CaptureSession* session, Camera_Point* focusPoint)
```

**描述**

获取当前焦点。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_CaptureSession](capi-oh-camera-camera-capturesession.md)\* session | Camera\_CaptureSession实例。 |
| [Camera\_Point](capi-oh-camera-camera-point.md)\* focusPoint | 当前焦点。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。  CAMERA\_SESSION\_NOT\_CONFIG：捕获会话未配置。 |

### OH\_CaptureSession\_SetFocusPoint()

```c
Camera_ErrorCode OH_CaptureSession_SetFocusPoint(Camera_CaptureSession* session, Camera_Point focusPoint)
```

**描述**

设置焦点。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_CaptureSession](capi-oh-camera-camera-capturesession.md)\* session | Camera\_CaptureSession实例。 |
| [Camera\_Point](capi-oh-camera-camera-point.md) focusPoint | 要设置的目标点。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。  CAMERA\_SESSION\_NOT\_CONFIG：捕获会话未配置。 |

### OH\_CaptureSession\_GetZoomRatioRange()

```c
Camera_ErrorCode OH_CaptureSession_GetZoomRatioRange(Camera_CaptureSession* session, float* minZoom, float* maxZoom)
```

**描述**

获取所有支持的缩放比例范围。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_CaptureSession](capi-oh-camera-camera-capturesession.md)\* session | Camera\_CaptureSession实例。 |
| float\* minZoom | 缩放比范围的最小值。 |
| float\* maxZoom | 缩放比例范围的最大值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。  CAMERA\_SESSION\_NOT\_CONFIG：捕获会话未配置。 |

### OH\_CaptureSession\_GetZoomRatio()

```c
Camera_ErrorCode OH_CaptureSession_GetZoomRatio(Camera_CaptureSession* session, float* zoom)
```

**描述**

获取当前缩放比例。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_CaptureSession](capi-oh-camera-camera-capturesession.md)\* session | Camera\_CaptureSession实例。 |
| float\* zoom | 当前缩放比例。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。  CAMERA\_SESSION\_NOT\_CONFIG：捕获会话未配置。 |

### OH\_CaptureSession\_SetZoomRatio()

```c
Camera_ErrorCode OH_CaptureSession_SetZoomRatio(Camera_CaptureSession* session, float zoom)
```

**描述**

设置缩放比例。

设置前，建议通过[OH\_CaptureSession\_GetZoomRatioRange](capi-capture-session-h.md#oh_capturesession_getzoomratiorange)获取支持的缩放比例范围。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_CaptureSession](capi-oh-camera-camera-capturesession.md)\* session | Camera\_CaptureSession实例。 |
| float zoom | 要设置的目标缩放比。  设置可变焦距比到底层生效需要一定时间，获取正确设置的可变焦距比需要等待1~2帧的时间。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。  CAMERA\_SESSION\_NOT\_CONFIG：捕获会话未配置。 |

### OH\_CaptureSession\_IsVideoStabilizationModeSupported()

```c
Camera_ErrorCode OH_CaptureSession_IsVideoStabilizationModeSupported(Camera_CaptureSession* session, Camera_VideoStabilizationMode mode, bool* isSupported)
```

**描述**

检查是否支持指定的录像防抖模式。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_CaptureSession](capi-oh-camera-camera-capturesession.md)\* session | Camera\_CaptureSession实例。 |
| [Camera\_VideoStabilizationMode](capi-camera-h.md#camera_videostabilizationmode) mode | 要检查的录像防抖模式。 |
| bool\* isSupported | 是否支持录像防抖模式的结果。返回true表示支持录像防抖模式，返回false表示不支持。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。  CAMERA\_SESSION\_NOT\_CONFIG：捕获会话未配置。 |

### OH\_CaptureSession\_GetVideoStabilizationMode()

```c
Camera_ErrorCode OH_CaptureSession_GetVideoStabilizationMode(Camera_CaptureSession* session, Camera_VideoStabilizationMode* mode)
```

**描述**

获取当前录像防抖模式。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_CaptureSession](capi-oh-camera-camera-capturesession.md)\* session | Camera\_CaptureSession实例。 |
| [Camera\_VideoStabilizationMode](capi-camera-h.md#camera_videostabilizationmode)\* mode | 当前录像防抖模式。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。  CAMERA\_SESSION\_NOT\_CONFIG：捕获会话未配置。 |

### OH\_CaptureSession\_SetVideoStabilizationMode()

```c
Camera_ErrorCode OH_CaptureSession_SetVideoStabilizationMode(Camera_CaptureSession* session, Camera_VideoStabilizationMode mode)
```

**描述**

设置录像防抖模式。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_CaptureSession](capi-oh-camera-camera-capturesession.md)\* session | Camera\_CaptureSession实例。 |
| [Camera\_VideoStabilizationMode](capi-camera-h.md#camera_videostabilizationmode) mode | 要设置的录像防抖模式。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。  CAMERA\_SESSION\_NOT\_CONFIG：捕获会话未配置。 |

### OH\_CaptureSession\_CanAddInput()

```c
Camera_ErrorCode OH_CaptureSession_CanAddInput(Camera_CaptureSession* session, Camera_Input* cameraInput, bool* isSuccessful)
```

**描述**

确定是否可以将相机输入添加到会话中。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_CaptureSession](capi-oh-camera-camera-capturesession.md)\* session | Camera\_CaptureSession实例。 |
| [Camera\_Input](capi-oh-camera-camera-input.md)\* cameraInput | 要设置的相机输入实例。 |
| bool\* isSuccessful | 是否可以将相机输入添加到会话中的结果。返回true表示可以将相机输入添加到会话中，返回false表示不可以。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。 |

### OH\_CaptureSession\_CanAddPreviewOutput()

```c
Camera_ErrorCode OH_CaptureSession_CanAddPreviewOutput(Camera_CaptureSession* session, Camera_PreviewOutput* cameraOutput, bool* isSuccessful)
```

**描述**

确定是否可以将相机预览输出添加到会话中。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_CaptureSession](capi-oh-camera-camera-capturesession.md)\* session | Camera\_CaptureSession实例。 |
| [Camera\_PreviewOutput](capi-oh-camera-camera-previewoutput.md)\* cameraOutput | 要设置的预览输出实例。 |
| bool\* isSuccessful | 是否可以将相机预览输出添加到会话中的结果。返回true表示可以将相机预览输出添加到会话中，返回false表示不可以。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。 |

### OH\_CaptureSession\_CanAddPhotoOutput()

```c
Camera_ErrorCode OH_CaptureSession_CanAddPhotoOutput(Camera_CaptureSession* session, Camera_PhotoOutput* cameraOutput, bool* isSuccessful)
```

**描述**

确定是否可以将拍照输出添加到会话中。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_CaptureSession](capi-oh-camera-camera-capturesession.md)\* session | Camera\_CaptureSession实例。 |
| [Camera\_PhotoOutput](capi-oh-camera-camera-photooutput.md)\* cameraOutput | 要设置的拍照输出实例。 |
| bool\* isSuccessful | 拍照输出是否可以添加到会话中的结果。返回true表示拍照输出可以添加到会话中，返回false表示不可以。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。 |

### OH\_CaptureSession\_CanAddVideoOutput()

```c
Camera_ErrorCode OH_CaptureSession_CanAddVideoOutput(Camera_CaptureSession* session, Camera_VideoOutput* cameraOutput, bool* isSuccessful)
```

**描述**

确定是否可以将录像输出添加到会话中。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_CaptureSession](capi-oh-camera-camera-capturesession.md)\* session | Camera\_CaptureSession实例。 |
| [Camera\_VideoOutput](capi-oh-camera-camera-videooutput.md)\* cameraOutput | 要添加的录像输出实例。 |
| bool\* isSuccessful | 录像输出是否可以添加到会话中的结果。返回true表示录像输出可以添加到会话中，返回false表示不可以。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。 |

### OH\_CaptureSession\_CanPreconfig()

```c
Camera_ErrorCode OH_CaptureSession_CanPreconfig(Camera_CaptureSession* session, Camera_PreconfigType preconfigType, bool* canPreconfig)
```

**描述**

检查是否支持指定的预配置类型。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_CaptureSession](capi-oh-camera-camera-capturesession.md)\* session | Camera\_CaptureSession实例。 |
| [Camera\_PreconfigType](capi-camera-h.md#camera_preconfigtype) preconfigType | 要检查的预配置类型。 |
| bool\* canPreconfig | 是否支持预配置的结果。返回true表示支持预配置，返回false表示不支持。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。 |

### OH\_CaptureSession\_CanPreconfigWithRatio()

```c
Camera_ErrorCode OH_CaptureSession_CanPreconfigWithRatio(Camera_CaptureSession* session, Camera_PreconfigType preconfigType, Camera_PreconfigRatio preconfigRatio, bool* canPreconfig)
```

**描述**

检查是否支持带比例的预配置类型。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_CaptureSession](capi-oh-camera-camera-capturesession.md)\* session | Camera\_CaptureSession实例。 |
| [Camera\_PreconfigType](capi-camera-h.md#camera_preconfigtype) preconfigType | 要检查的预配置类型。 |
| [Camera\_PreconfigRatio](capi-camera-h.md#camera_preconfigratio) preconfigRatio | 要检查的预配置比例。 |
| bool\* canPreconfig | 是否支持预配置的结果。返回true表示支持预配置，返回false表示不支持。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。 |

### OH\_CaptureSession\_Preconfig()

```c
Camera_ErrorCode OH_CaptureSession_Preconfig(Camera_CaptureSession* session, Camera_PreconfigType preconfigType)
```

**描述**

设置预配置类型。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_CaptureSession](capi-oh-camera-camera-capturesession.md)\* session | Camera\_CaptureSession实例。 |
| [Camera\_PreconfigType](capi-camera-h.md#camera_preconfigtype) preconfigType | 指定的预配置类型。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。  CAMERA\_SERVICE\_FATAL\_ERROR：相机服务异常。 |

### OH\_CaptureSession\_PreconfigWithRatio()

```c
Camera_ErrorCode OH_CaptureSession_PreconfigWithRatio(Camera_CaptureSession* session, Camera_PreconfigType preconfigType, Camera_PreconfigRatio preconfigRatio)
```

**描述**

设置带有比例的预配置类型。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_CaptureSession](capi-oh-camera-camera-capturesession.md)\* session | Camera\_CaptureSession实例。 |
| [Camera\_PreconfigType](capi-camera-h.md#camera_preconfigtype) preconfigType | 指定的预配置类型。 |
| [Camera\_PreconfigRatio](capi-camera-h.md#camera_preconfigratio) preconfigRatio | 指定的预配置比例。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。  CAMERA\_SERVICE\_FATAL\_ERROR：相机服务异常。 |

### OH\_CaptureSession\_GetExposureValue()

```c
Camera_ErrorCode OH_CaptureSession_GetExposureValue(Camera_CaptureSession* session, float* exposureValue)
```

**描述**

查询曝光值。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_CaptureSession](capi-oh-camera-camera-capturesession.md)\* session | Camera\_CaptureSession实例。 |
| float\* exposureValue | 当前的曝光值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。  CAMERA\_SERVICE\_FATAL\_ERROR：相机服务异常。 |

### OH\_CaptureSession\_GetFocalLength()

```c
Camera_ErrorCode OH_CaptureSession_GetFocalLength(Camera_CaptureSession* session, float* focalLength)
```

**描述**

获取当前焦距值。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_CaptureSession](capi-oh-camera-camera-capturesession.md)\* session | Camera\_CaptureSession实例。 |
| float\* focalLength | 当前焦距值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。  CAMERA\_SESSION\_NOT\_CONFIG：捕获会话未配置。 |

### OH\_CaptureSession\_GetFocusDistance()

```c
Camera_ErrorCode OH_CaptureSession_GetFocusDistance(const Camera_CaptureSession* session, float* focusDistance)
```

**描述**

获取当前对焦距离。取值范围为[0.0, 1.0]。0.0表示镜头可对焦的最近距离；1.0表示最远距离。默认值为1.0。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [Camera\_CaptureSession](capi-oh-camera-camera-capturesession.md)\* session | Camera\_CaptureSession实例指针。 |
| float\* focusDistance | 输出参数，返回当前对焦距离。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或者参数不正确。  CAMERA\_OPERATION\_NOT\_ALLOWED：操作不允许，会话或输入设备可能异常。  CAMERA\_SESSION\_NOT\_CONFIG：捕获会话未配置。 |

### OH\_CaptureSession\_SetFocusDistance()

```c
Camera_ErrorCode OH_CaptureSession_SetFocusDistance(const Camera_CaptureSession* session, float focusDistance)
```

**描述**

设置对焦距离。取值范围为[0.0, 1.0]。0.0表示镜头可对焦的最近距离；1.0表示最远距离。默认值为1.0。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [Camera\_CaptureSession](capi-oh-camera-camera-capturesession.md)\* session | Camera\_CaptureSession实例指针。 |
| float focusDistance | 待设置的对焦距离。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或者参数不正确。  CAMERA\_OPERATION\_NOT\_ALLOWED：操作不允许，会话或输入设备可能异常。  CAMERA\_SESSION\_NOT\_CONFIG：捕获会话未配置。 |

### OH\_CaptureSession\_IsFocusDistanceSupported()

```c
Camera_ErrorCode OH_CaptureSession_IsFocusDistanceSupported(const Camera_CaptureSession* session, bool* isSupported)
```

**描述**

查询是否支持对焦距离设置。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [Camera\_CaptureSession](capi-oh-camera-camera-capturesession.md)\* session | Camera\_CaptureSession实例指针。 |
| bool\* isSupported | 输出参数，返回是否支持对焦距离的结果。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或者参数不正确。  CAMERA\_SESSION\_NOT\_CONFIG：捕获会话未配置。 |

### OH\_CaptureSession\_SetSmoothZoom()

```c
Camera_ErrorCode OH_CaptureSession_SetSmoothZoom(Camera_CaptureSession* session, float targetZoom, Camera_SmoothZoomMode smoothZoomMode)
```

**描述**

触发平滑变焦。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_CaptureSession](capi-oh-camera-camera-capturesession.md)\* session | Camera\_CaptureSession实例。 |
| float targetZoom | 要设置的目标变焦比。取值范围需通过[OH\_CaptureSession\_GetZoomRatioRange](capi-capture-session-h.md#oh_capturesession_getzoomratiorange)获取。 |
| [Camera\_SmoothZoomMode](capi-camera-h.md#camera_smoothzoommode) smoothZoomMode | 平滑变焦模式。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。  CAMERA\_SESSION\_NOT\_CONFIG：捕获会话未配置。 |

### OH\_CaptureSession\_GetSupportedColorSpaces()

```c
Camera_ErrorCode OH_CaptureSession_GetSupportedColorSpaces(Camera_CaptureSession* session, OH_NativeBuffer_ColorSpace** colorSpace, uint32_t* size)
```

**描述**

获取支持的色彩空间列表。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_CaptureSession](capi-oh-camera-camera-capturesession.md)\* session | Camera\_CaptureSession实例。 |
| OH\_NativeBuffer\_ColorSpace\*\* colorSpace | 如果方法调用成功，将记录支持的OH\_NativeBuffer\_ColorSpace列表。 |
| uint32\_t\* size | 如果方法调用成功，将记录支持的OH\_NativeBuffer\_ColorSpace列表的大小。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。  CAMERA\_SESSION\_NOT\_CONFIG：捕获会话未配置。 |

### OH\_CaptureSession\_DeleteColorSpaces()

```c
Camera_ErrorCode OH_CaptureSession_DeleteColorSpaces(Camera_CaptureSession* session, OH_NativeBuffer_ColorSpace* colorSpace)
```

**描述**

删除色彩空间列表。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_CaptureSession](capi-oh-camera-camera-capturesession.md)\* session | Camera\_CaptureSession实例。 |
| [OH\_NativeBuffer\_ColorSpace](capi-buffer-common-h.md#oh_nativebuffer_colorspace)\* colorSpace | 如果方法调用成功，将删除的OH\_NativeBuffer\_ColorSpace列表。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。 |

### OH\_CaptureSession\_GetActiveColorSpace()

```c
Camera_ErrorCode OH_CaptureSession_GetActiveColorSpace(Camera_CaptureSession* session, OH_NativeBuffer_ColorSpace* colorSpace)
```

**描述**

获取当前色彩空间。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_CaptureSession](capi-oh-camera-camera-capturesession.md)\* session | Camera\_CaptureSession实例。 |
| [OH\_NativeBuffer\_ColorSpace](capi-buffer-common-h.md#oh_nativebuffer_colorspace)\* colorSpace | 当前的OH\_NativeBuffer\_ColorSpace。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。  CAMERA\_SESSION\_NOT\_CONFIG：捕获会话未配置。 |

### OH\_CaptureSession\_SetActiveColorSpace()

```c
Camera_ErrorCode OH_CaptureSession_SetActiveColorSpace(Camera_CaptureSession* session, OH_NativeBuffer_ColorSpace colorSpace)
```

**描述**

设置当前色彩空间。

设置的值需在[OH\_CaptureSession\_GetSupportedColorSpaces](capi-capture-session-h.md#oh_capturesession_getsupportedcolorspaces)获取的支持列表中。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_CaptureSession](capi-oh-camera-camera-capturesession.md)\* session | Camera\_CaptureSession实例。 |
| [OH\_NativeBuffer\_ColorSpace](capi-buffer-common-h.md#oh_nativebuffer_colorspace) colorSpace | 要设置的目标OH\_NativeBuffer\_ColorSpace。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。  CAMERA\_SESSION\_NOT\_CONFIG：捕获会话未配置。 |

### OH\_CaptureSession\_RegisterAutoDeviceSwitchStatusCallback()

```c
Camera_ErrorCode OH_CaptureSession_RegisterAutoDeviceSwitchStatusCallback(Camera_CaptureSession* session, OH_CaptureSession_OnAutoDeviceSwitchStatusChange autoDeviceSwitchStatusChange)
```

**描述**

注册设备切换事件回调。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_CaptureSession](capi-oh-camera-camera-capturesession.md)\* session | Camera\_CaptureSession实例。 |
| [OH\_CaptureSession\_OnAutoDeviceSwitchStatusChange](capi-capture-session-h.md#oh_capturesession_onautodeviceswitchstatuschange) autoDeviceSwitchStatusChange | 要注册的设备切换事件回调。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。 |

### OH\_CaptureSession\_UnregisterAutoDeviceSwitchStatusCallback()

```c
Camera_ErrorCode OH_CaptureSession_UnregisterAutoDeviceSwitchStatusCallback(Camera_CaptureSession* session, OH_CaptureSession_OnAutoDeviceSwitchStatusChange autoDeviceSwitchStatusChange)
```

**描述**

注销设备切换事件回调。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_CaptureSession](capi-oh-camera-camera-capturesession.md)\* session | Camera\_CaptureSession实例。 |
| [OH\_CaptureSession\_OnAutoDeviceSwitchStatusChange](capi-capture-session-h.md#oh_capturesession_onautodeviceswitchstatuschange) autoDeviceSwitchStatusChange | 要注销的设备切换事件回调。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。 |

### OH\_CaptureSession\_IsAutoDeviceSwitchSupported()

```c
Camera_ErrorCode OH_CaptureSession_IsAutoDeviceSwitchSupported(Camera_CaptureSession* session, bool* isSupported)
```

**描述**

检查是否支持自动设备切换。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_CaptureSession](capi-oh-camera-camera-capturesession.md)\* session | Camera\_CaptureSession实例。 |
| bool\* isSupported | 是否支持自动设备切换的结果。返回true表示支持自动设备切换，返回false表示不支持。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。  CAMERA\_SESSION\_NOT\_CONFIG：捕获会话未配置。 |

### OH\_CaptureSession\_EnableAutoDeviceSwitch()

```c
Camera_ErrorCode OH_CaptureSession_EnableAutoDeviceSwitch(Camera_CaptureSession* session, bool enabled)
```

**描述**

是否启用相机设备的自动切换。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_CaptureSession](capi-oh-camera-camera-capturesession.md)\* session | Camera\_CaptureSession实例。 |
| bool enabled | 是否启用自动切换的标志。返回true表示启用自动切换，返回false表示不启用。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。  CAMERA\_SESSION\_NOT\_CONFIG：捕获会话未配置。  CAMERA\_SERVICE\_FATAL\_ERROR：相机服务异常。 |

### OH\_CaptureSession\_RegisterSystemPressureLevelChangeCallback()

```c
Camera_ErrorCode OH_CaptureSession_RegisterSystemPressureLevelChangeCallback(Camera_CaptureSession* session, OH_CaptureSession_OnSystemPressureLevelChange systemPressureLevelChange)
```

**描述**

注册系统压力状态变化回调。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_CaptureSession](capi-oh-camera-camera-capturesession.md)\* session | 传递回调的Camera\_CaptureSession实例。 |
| [OH\_CaptureSession\_OnSystemPressureLevelChange](capi-capture-session-h.md#oh_capturesession_onsystempressurelevelchange) systemPressureLevelChange | 要注册的系统压力状态变化OH\_CaptureSession\_OnSystemPressureLevelChange回调。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。 |

### OH\_CaptureSession\_UnregisterSystemPressureLevelChangeCallback()

```c
Camera_ErrorCode OH_CaptureSession_UnregisterSystemPressureLevelChangeCallback(Camera_CaptureSession* session, OH_CaptureSession_OnSystemPressureLevelChange systemPressureLevelChange)
```

**描述**

注销系统压力状态变化回调。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_CaptureSession](capi-oh-camera-camera-capturesession.md)\* session | 传递回调的Camera\_CaptureSession实例。 |
| [OH\_CaptureSession\_OnSystemPressureLevelChange](capi-capture-session-h.md#oh_capturesession_onsystempressurelevelchange) systemPressureLevelChange | 要注销的系统压力状态变化OH\_CaptureSession\_OnSystemPressureLevelChange回调。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。 |

### OH\_CaptureSession\_SetQualityPrioritization()

```c
Camera_ErrorCode OH_CaptureSession_SetQualityPrioritization(Camera_CaptureSession* session, Camera_QualityPrioritization qualityPrioritization)
```

**描述**

设置录像质量优先级。

默认为高录像质量，设置为功耗平衡将降低录像质量以减少功耗。实际功耗收益因平台而异。建议该接口在[OH\_CaptureSession\_CommitConfig](capi-capture-session-h.md#oh_capturesession_commitconfig)和[OH\_CaptureSession\_Start](capi-capture-session-h.md#oh_capturesession_start)之间调用。

**起始版本：** 14

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_CaptureSession](capi-oh-camera-camera-capturesession.md)\* session | Camera\_CaptureSession实例。 |
| [Camera\_QualityPrioritization](capi-camera-h.md#camera_qualityprioritization) qualityPrioritization | 要设置的录像质量优先级，默认为高录像质量。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。  CAMERA\_SESSION\_NOT\_CONFIG：捕获会话未配置。 |

### OH\_CaptureSession\_IsMacroSupported()

```c
Camera_ErrorCode OH_CaptureSession_IsMacroSupported(Camera_CaptureSession* session, bool* isSupported)
```

**描述**

检查是否支持微距能力。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_CaptureSession](capi-oh-camera-camera-capturesession.md)\* session | Camera\_CaptureSession实例。 |
| bool\* isSupported | 是否支持微距能力的结果。返回true表示支持微距能力，返回false表示不支持。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK = 0：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。  CAMERA\_SESSION\_NOT\_CONFIG：捕获会话未配置。 |

### OH\_CaptureSession\_EnableMacro()

```c
Camera_ErrorCode OH_CaptureSession_EnableMacro(Camera_CaptureSession* session, bool enabled)
```

**描述**

是否启用相机设备的微距能力。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_CaptureSession](capi-oh-camera-camera-capturesession.md)\* session | Camera\_CaptureSession实例。 |
| bool enabled | 是否启用微距能力的标志。返回true表示启用微距能力，返回false表示不启用。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK = 0：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。  CAMERA\_SESSION\_NOT\_CONFIG：捕获会话未配置。  CAMERA\_OPERATION\_NOT\_ALLOWED：不允许操作。 |

### OH\_CaptureSession\_SetWhiteBalance()

```c
Camera_ErrorCode OH_CaptureSession_SetWhiteBalance(Camera_CaptureSession* session, int32_t colorTemperature)
```

**描述**

设置白平衡的色温。

设置前，建议通过[OH\_CaptureSession\_GetWhiteBalanceRange](capi-capture-session-h.md#oh_capturesession_getwhitebalancerange)获取支持配置的白平衡色温范围。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_CaptureSession](capi-oh-camera-camera-capturesession.md)\* session | Camera\_CaptureSession实例。 |
| int32\_t colorTemperature | 色温值，单位为K。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：设置成功。  CAMERA\_INVALID\_ARGUMENT：参数缺失或者参数类型不正确。  CAMERA\_SESSION\_NOT\_CONFIG：相机会话未配置。 |

### OH\_CaptureSession\_GetColorTintRange()

```c
Camera_ErrorCode OH_CaptureSession_GetColorTintRange(const Camera_CaptureSession* session, int32_t *minColorTint, int32_t *maxColorTint)
```

**描述**

获取支持配置的白平衡色调调节范围。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const Camera\_CaptureSession](capi-oh-camera-camera-capturesession.md)\* session | Camera\_CaptureSession实例。 |
| int32\_t \*minColorTint | 指向最小色调值的指针。 |
| int32\_t \*maxColorTint | 指向最大色调值的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。  CAMERA\_SESSION\_NOT\_CONFIG：当调用该方法时，捕获会话未配置。 |

### OH\_CaptureSession\_GetColorTint()

```c
Camera_ErrorCode OH_CaptureSession_GetColorTint(const Camera_CaptureSession* session, int32_t *colorTint)
```

**描述**

获取当前白平衡的色调调节值。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const Camera\_CaptureSession](capi-oh-camera-camera-capturesession.md)\* session | Camera\_CaptureSession实例。 |
| int32\_t \*colorTint | 指向色调值的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。  CAMERA\_SESSION\_NOT\_CONFIG：当调用该方法时，捕获会话未配置。 |

### OH\_CaptureSession\_SetColorTint()

```c
Camera_ErrorCode OH_CaptureSession_SetColorTint(Camera_CaptureSession* session, int32_t colorTint)
```

**描述**

设置白平衡的色调调节值。设置前，建议通过[OH\_CaptureSession\_GetColorTintRange](capi-capture-session-h.md#oh_capturesession_getcolortintrange)获取支持配置的白平衡色调调节范围。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_CaptureSession](capi-oh-camera-camera-capturesession.md)\* session | Camera\_CaptureSession实例。 |
| int32\_t colorTint | 色调调节值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。  CAMERA\_SESSION\_NOT\_CONFIG：当调用该方法时，捕获会话未配置。 |

### OH\_CaptureSession\_GetWhiteBalance()

```c
Camera_ErrorCode OH_CaptureSession_GetWhiteBalance(Camera_CaptureSession* session, int32_t *colorTemperature)
```

**描述**

获取当前白平衡色温值。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_CaptureSession](capi-oh-camera-camera-capturesession.md)\* session | Camera\_CaptureSession实例。 |
| int32\_t \*colorTemperature | 色温值，单位为K。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：函数调用成功。  CAMERA\_INVALID\_ARGUMENT：参数缺失或者参数类型不正确。  CAMERA\_SESSION\_NOT\_CONFIG：相机会话未配置。 |

### OH\_CaptureSession\_GetWhiteBalanceMode()

```c
Camera_ErrorCode OH_CaptureSession_GetWhiteBalanceMode(Camera_CaptureSession* session, Camera_WhiteBalanceMode* whiteBalanceMode)
```

**描述**

获取当前的白平衡模式。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_CaptureSession](capi-oh-camera-camera-capturesession.md)\* session | Camera\_CaptureSession实例。 |
| [Camera\_WhiteBalanceMode](capi-camera-h.md#camera_whitebalancemode)\* whiteBalanceMode | 白平衡模式。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：函数调用成功。  CAMERA\_INVALID\_ARGUMENT：参数缺失或者参数类型不正确。  CAMERA\_SESSION\_NOT\_CONFIG：相机会话未配置。 |

### OH\_CaptureSession\_IsWhiteBalanceModeSupported()

```c
Camera_ErrorCode OH_CaptureSession_IsWhiteBalanceModeSupported(Camera_CaptureSession* session, Camera_WhiteBalanceMode whiteBalanceMode, bool* isSupported)
```

**描述**

检查是否支持指定的白平衡模式。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_CaptureSession](capi-oh-camera-camera-capturesession.md)\* session | Camera\_CaptureSession实例。 |
| [Camera\_WhiteBalanceMode](capi-camera-h.md#camera_whitebalancemode) whiteBalanceMode | 指定的白平衡模式。 |
| bool\* isSupported | 用于返回是否支持指定的白平衡模式，支持返回true，否则返回false。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：函数调用成功。  CAMERA\_INVALID\_ARGUMENT：参数缺失或者参数类型不正确。  CAMERA\_SESSION\_NOT\_CONFIG：相机会话未配置。 |

### OH\_CaptureSession\_SetWhiteBalanceMode()

```c
Camera_ErrorCode OH_CaptureSession_SetWhiteBalanceMode(Camera_CaptureSession* session, Camera_WhiteBalanceMode whiteBalanceMode)
```

**描述**

设置白平衡模式。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_CaptureSession](capi-oh-camera-camera-capturesession.md)\* session | Camera\_CaptureSession实例。 |
| [Camera\_WhiteBalanceMode](capi-camera-h.md#camera_whitebalancemode) whiteBalanceMode | 白平衡模式。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：设置成功。  CAMERA\_INVALID\_ARGUMENT：参数缺失或者参数类型不正确。  CAMERA\_SESSION\_NOT\_CONFIG：相机会话未配置。 |

### OH\_CaptureSession\_GetWhiteBalanceRange()

```c
Camera_ErrorCode OH_CaptureSession_GetWhiteBalanceRange(Camera_CaptureSession* session, int32_t *minColorTemperature, int32_t *maxColorTemperature)
```

**描述**

获取支持配置的白平衡色温范围。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_CaptureSession](capi-oh-camera-camera-capturesession.md)\* session | Camera\_CaptureSession实例。 |
| int32\_t \*minColorTemperature | 支持的最小色温值，单位为K。 |
| int32\_t \*maxColorTemperature | 支持的最大色温值，单位为K。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：函数调用成功。  CAMERA\_INVALID\_ARGUMENT：参数缺失或者参数类型不正确。  CAMERA\_SESSION\_NOT\_CONFIG：相机会话未配置。 |

### OH\_CaptureSession\_IsControlCenterSupported()

```c
Camera_ErrorCode OH_CaptureSession_IsControlCenterSupported(Camera_CaptureSession* session, bool* isSupported)
```

**描述**

检查是否支持相机控制器。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_CaptureSession](capi-oh-camera-camera-capturesession.md)\* session | Camera\_CaptureSession实例。 |
| bool\* isSupported | 是否支持相机控制器的结果。true表示支持，false表示不支持。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK = 0：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。  CAMERA\_SESSION\_NOT\_CONFIG：捕获会话未配置。 |

### OH\_CaptureSession\_GetSupportedEffectTypes()

```c
Camera_ErrorCode OH_CaptureSession_GetSupportedEffectTypes(Camera_CaptureSession* session, Camera_ControlCenterEffectType** types, uint32_t* size)
```

**描述**

获取相机控制器支持的效果类型。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_CaptureSession](capi-oh-camera-camera-capturesession.md)\* session | Camera\_CaptureSession实例。 |
| [Camera\_ControlCenterEffectType](capi-camera-h.md#camera_controlcentereffecttype)\*\* types | 如果方法调用成功，将记录支持的Camera\_ControlCenterEffectType列表。 |
| uint32\_t\* size | 如果方法调用成功，将记录支持的Camera\_ControlCenterEffectType列表的大小。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。  CAMERA\_SESSION\_NOT\_CONFIG：捕获会话未配置。 |

### OH\_CaptureSession\_DeleteSupportedEffectTypes()

```c
Camera_ErrorCode OH_CaptureSession_DeleteSupportedEffectTypes(Camera_CaptureSession* session, Camera_ControlCenterEffectType* types, uint32_t size)
```

**描述**

删除相机控制器效果类型列表。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_CaptureSession](capi-oh-camera-camera-capturesession.md)\* session | Camera\_CaptureSession实例。 |
| [Camera\_ControlCenterEffectType](capi-camera-h.md#camera_controlcentereffecttype)\* types | 如果方法调用成功，要删除的Camera\_ControlCenterEffectType列表。 |
| uint32\_t size | 要删除的Camera\_ControlCenterEffectType列表的大小。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。 |

### OH\_CaptureSession\_EnableControlCenter()

```c
Camera_ErrorCode OH_CaptureSession_EnableControlCenter(Camera_CaptureSession* session, bool enabled)
```

**描述**

是否启用相机控制器。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_CaptureSession](capi-oh-camera-camera-capturesession.md)\* session | Camera\_CaptureSession实例。 |
| bool enabled | 是否启用相机控制器的标志。true表示启用，false表示禁用。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK = 0：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。  CAMERA\_SESSION\_NOT\_CONFIG：捕获会话未配置。  CAMERA\_SERVICE\_FATAL\_ERROR：相机服务异常。 |

### OH\_CaptureSession\_RegisterControlCenterEffectStatusChangeCallback()

```c
Camera_ErrorCode OH_CaptureSession_RegisterControlCenterEffectStatusChangeCallback(Camera_CaptureSession* session, OH_CaptureSession_OnControlCenterEffectStatusChange controlCenterEffectStatusChange)
```

**描述**

注册相机控制器效果激活状态变化回调。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_CaptureSession](capi-oh-camera-camera-capturesession.md)\* session | 传递回调的Camera\_CaptureSession实例。 |
| [OH\_CaptureSession\_OnControlCenterEffectStatusChange](capi-capture-session-h.md#oh_capturesession_oncontrolcentereffectstatuschange) controlCenterEffectStatusChange | 要注册的相机控制器效果激活状态变化OH\_CaptureSession\_OnControlCenterEffectStatusChange回调。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。 |

### OH\_CaptureSession\_UnregisterControlCenterEffectStatusChangeCallback()

```c
Camera_ErrorCode OH_CaptureSession_UnregisterControlCenterEffectStatusChangeCallback(Camera_CaptureSession* session, OH_CaptureSession_OnControlCenterEffectStatusChange controlCenterEffectStatusChange)
```

**描述**

注销相机控制器效果激活状态变化回调。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_CaptureSession](capi-oh-camera-camera-capturesession.md)\* session | 传递回调的Camera\_CaptureSession实例。 |
| [OH\_CaptureSession\_OnControlCenterEffectStatusChange](capi-capture-session-h.md#oh_capturesession_oncontrolcentereffectstatuschange) controlCenterEffectStatusChange | 要注销的相机控制器效果激活状态变化OH\_CaptureSession\_OnControlCenterEffectStatusChange回调。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。 |

### OH\_CaptureSession\_OnMacroStatusChange()

```c
 typedef void (*OH_CaptureSession_OnMacroStatusChange)(Camera_CaptureSession* session, bool isMacroDetected)
```

**描述**

相机会话微距状态改变回调。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_CaptureSession](capi-oh-camera-camera-capturesession.md)\* session | 指向Camera\_CaptureSession实例的指针。 |
| bool isMacroDetected | 是否进入超级微距，true表示进入超级微距，false表示未进入超级微距。 |

### OH\_CaptureSession\_RegisterMacroStatusChangeCallback()

```c
 Camera_ErrorCode OH_CaptureSession_RegisterMacroStatusChangeCallback(Camera_CaptureSession* session, OH_CaptureSession_OnMacroStatusChange macroStatusChange)
```

**描述**

注册相机会话微距状态改变回调函数。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_CaptureSession](capi-oh-camera-camera-capturesession.md)\* session | 指向Camera\_CaptureSession实例的指针。 |
| [OH\_CaptureSession\_OnMacroStatusChange](capi-capture-session-h.md#oh_capturesession_onmacrostatuschange) macroStatusChange | 微距状态改变回调函数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。 |

### OH\_CaptureSession\_UnregisterMacroStatusChangeCallback()

```c
 Camera_ErrorCode OH_CaptureSession_UnregisterMacroStatusChangeCallback(Camera_CaptureSession* session, OH_CaptureSession_OnMacroStatusChange macroStatusChange)
```

**描述**

取消注册相机会话微距状态改变回调函数。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_CaptureSession](capi-oh-camera-camera-capturesession.md)\* session | 指向Camera\_CaptureSession实例的指针。 |
| [OH\_CaptureSession\_OnMacroStatusChange](capi-capture-session-h.md#oh_capturesession_onmacrostatuschange) macroStatusChange | 微距状态改变回调函数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。 |

### OH\_CaptureSession\_OnIsoChange()

```c
typedef void (*OH_CaptureSession_OnIsoChange)(Camera_CaptureSession* session, int32_t isoValue)
```

**描述**

用于在相机会话中监听感光度（ISO）变化的回调函数。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_CaptureSession](capi-oh-camera-camera-capturesession.md)\* session | 指向Camera\_CaptureSession的指针。 |
| int32\_t isoValue | 回调中获取的感光度（ISO）的值。 |

### OH\_CaptureSession\_RegisterIsoChangeCallback()

```c
Camera_ErrorCode OH_CaptureSession_RegisterIsoChangeCallback(Camera_CaptureSession* session, OH_CaptureSession_OnIsoChange isoChange)
```

**描述**

注册监听感光度（ISO）改变的事件回调。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_CaptureSession](capi-oh-camera-camera-capturesession.md)\* session | 指向Camera\_CaptureSession实例的指针。 |
| [OH\_CaptureSession\_OnIsoChange](capi-capture-session-h.md#oh_capturesession_onisochange) isoChange | OH\_CaptureSession\_OnIsoChange类型的回调函数，用于监听ISO改变。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数缺失或者参数类型不正确。 |

### OH\_CaptureSession\_UnregisterIsoChangeCallback()

```c
Camera_ErrorCode OH_CaptureSession_UnregisterIsoChangeCallback(Camera_CaptureSession* session, OH_CaptureSession_OnIsoChange isoChange)
```

**描述**

取消注册监听感光度（ISO）改变的事件回调。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_CaptureSession](capi-oh-camera-camera-capturesession.md)\* session | 指向Camera\_CaptureSession实例的指针。 |
| [OH\_CaptureSession\_OnIsoChange](capi-capture-session-h.md#oh_capturesession_onisochange) isoChange | OH\_CaptureSession\_OnIsoChange类型的回调函数，用于监听ISO改变。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数缺失或者参数类型不正确。 |

### OH\_CaptureSession\_GetRAWCaptureZoomRatioRange()

```c
Camera_ErrorCode OH_CaptureSession_GetRAWCaptureZoomRatioRange(const Camera_CaptureSession* session, float* minZoom, float* maxZoom)
```

**描述**

查询物理镜头RAW图拍照支持的变焦范围。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [Camera\_CaptureSession](capi-oh-camera-camera-capturesession.md)\* session | Camera\_CaptureSession实例。 |
| float\* minZoom | 输出参数，返回变焦最小值。 |
| float\* maxZoom | 输出参数，返回变焦最大值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或者参数不正确。  CAMERA\_OPERATION\_NOT\_ALLOWED：操作不允许,会话或相机状态异常。  CAMERA\_SESSION\_NOT\_CONFIG：捕获会话未配置。 |

### OH\_CaptureSession\_IsOISModeSupported()

```c
Camera_ErrorCode OH_CaptureSession_IsOISModeSupported(const Camera_CaptureSession* session, OH_Camera_OISMode oisMode, bool* isSupported)
```

**描述**

检查指定的光学防抖（OIS）模式是否支持。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [Camera\_CaptureSession](capi-oh-camera-camera-capturesession.md)\* session | Camera\_CaptureSession实例指针。 |
| [OH\_Camera\_OISMode](capi-camera-h.md#oh_camera_oismode) oisMode | 待检查的光学防抖模式。 |
| bool\* isSupported | 输出参数，返回当前设备是否支持该模式。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或者参数不正确。  CAMERA\_OPERATION\_NOT\_ALLOWED：操作不允许。  CAMERA\_SESSION\_NOT\_CONFIG：捕获会话未配置。 |

### OH\_CaptureSession\_GetSupportedOISBiasRange()

```c
Camera_ErrorCode OH_CaptureSession_GetSupportedOISBiasRange(const Camera_CaptureSession* session, OH_Camera_OISAxes oisAxis, float* minBias, float* maxBias, float* step)
```

**描述**

获取指定光学防抖轴支持的偏移范围。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [Camera\_CaptureSession](capi-oh-camera-camera-capturesession.md)\* session | Camera\_CaptureSession实例指针。 |
| [OH\_Camera\_OISAxes](capi-camera-h.md#oh_camera_oisaxes) oisAxis | 光学防抖轴。 |
| float\* minBias | 输出参数，返回最小偏移值。 |
| float\* maxBias | 输出参数，返回最大偏移值。 |
| float\* step | 输出参数，返回偏移步长值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或者参数不正确。  CAMERA\_OPERATION\_NOT\_ALLOWED：操作不允许。  CAMERA\_SESSION\_NOT\_CONFIG：捕获会话未配置。 |

### OH\_CaptureSession\_GetCurrentOISMode()

```c
Camera_ErrorCode OH_CaptureSession_GetCurrentOISMode(const Camera_CaptureSession* session, OH_Camera_OISMode* oisMode)
```

**描述**

获取当前光学防抖（OIS）模式。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [Camera\_CaptureSession](capi-oh-camera-camera-capturesession.md)\* session | Camera\_CaptureSession实例指针。 |
| [OH\_Camera\_OISMode](capi-camera-h.md#oh_camera_oismode)\* oisMode | 输出参数，返回当前光学防抖模式。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或者参数不正确。  CAMERA\_OPERATION\_NOT\_ALLOWED：操作不允许。  CAMERA\_SESSION\_NOT\_CONFIG：捕获会话未配置。 |

### OH\_CaptureSession\_GetCurrentCustomOISBias()

```c
Camera_ErrorCode OH_CaptureSession_GetCurrentCustomOISBias(const Camera_CaptureSession* session, float* pitchBias, float* yawBias)
```

**描述**

获取所有光学防抖轴当前的自定义偏移值。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [Camera\_CaptureSession](capi-oh-camera-camera-capturesession.md)\* session | Camera\_CaptureSession实例指针。 |
| float\* pitchBias | 输出参数，返回俯仰轴偏移值。 |
| float\* yawBias | 输出参数，返回偏航轴偏移值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或者参数不正确。  CAMERA\_OPERATION\_NOT\_ALLOWED：操作不允许。  CAMERA\_SESSION\_NOT\_CONFIG：捕获会话未配置。 |

### OH\_CaptureSession\_SetOISMode()

```c
Camera_ErrorCode OH_CaptureSession_SetOISMode(const Camera_CaptureSession* session, OH_Camera_OISMode oisMode)
```

**描述**

设置光学防抖（OIS）模式。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [Camera\_CaptureSession](capi-oh-camera-camera-capturesession.md)\* session | Camera\_CaptureSession实例指针。 |
| [OH\_Camera\_OISMode](capi-camera-h.md#oh_camera_oismode) oisMode | 待设置的光学防抖模式。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或者参数不正确。  CAMERA\_OPERATION\_NOT\_ALLOWED：操作不允许。  CAMERA\_SESSION\_NOT\_CONFIG：捕获会话未配置。 |

### OH\_CaptureSession\_SetOISModeCustom()

```c
Camera_ErrorCode OH_CaptureSession_SetOISModeCustom(const Camera_CaptureSession* session, float pitchBias, float yawBias)
```

**描述**

为对应轴设置自定义光学防抖偏移值。

设置前，建议通过[OH\_CaptureSession\_GetSupportedOISBiasRange](capi-capture-session-h.md#oh_capturesession_getsupportedoisbiasrange)获取对应轴支持的偏移范围。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [Camera\_CaptureSession](capi-oh-camera-camera-capturesession.md)\* session | Camera\_CaptureSession实例指针。 |
| float pitchBias | 俯仰轴偏移值。 |
| float yawBias | 偏航轴偏移值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或者参数不正确。  CAMERA\_OPERATION\_NOT\_ALLOWED：操作不允许。  CAMERA\_SESSION\_NOT\_CONFIG：捕获会话未配置。 |

### OH\_CaptureSession\_OnExposureStateChange()

```c
typedef void (*OH_CaptureSession_OnExposureStateChange)(void* context, OH_Camera_ExposureState exposureState)
```

**描述**

定义曝光状态变更时的回调函数。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| void\* context | 指向自定义上下文的指针。 |
| [OH\_Camera\_ExposureState](capi-camera-h.md#oh_camera_exposurestate) exposureState | 当前曝光状态。 |

### OH\_CaptureSession\_RegisterExposureStateChangeCallback()

```c
Camera_ErrorCode OH_CaptureSession_RegisterExposureStateChangeCallback(const Camera_CaptureSession* session, void* context, OH_CaptureSession_OnExposureStateChange callback)
```

**描述**

注册曝光状态变化的回调。注册此回调后，当捕获会话中的曝光状态发生变化时，将调用该回调。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const Camera\_CaptureSession](capi-oh-camera-camera-capturesession.md)\* session | Camera\_CaptureSession实例。 |
| void\* context | 指向自定义上下文的指针。 |
| [OH\_CaptureSession\_OnExposureStateChange](capi-capture-session-h.md#oh_capturesession_onexposurestatechange) callback | 表示曝光状态改变的回调函数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数缺失或参数类型不正确。 |

### OH\_CaptureSession\_UnregisterExposureStateChangeCallback()

```c
Camera_ErrorCode OH_CaptureSession_UnregisterExposureStateChangeCallback(const Camera_CaptureSession* session, void* context, OH_CaptureSession_OnExposureStateChange callback)
```

**描述**

注销曝光状态变更时的回调函数。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const Camera\_CaptureSession](capi-oh-camera-camera-capturesession.md)\* session | Camera\_CaptureSession实例。 |
| void\* context | 指向注册回调时指定的自定义上下文的指针。 |
| [OH\_CaptureSession\_OnExposureStateChange](capi-capture-session-h.md#oh_capturesession_onexposurestatechange) callback | 表示曝光状态改变的回调函数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数缺失或参数类型不正确。 |

### OH\_CaptureSession\_GetZoomPointInfos()

```c
Camera_ErrorCode OH_CaptureSession_GetZoomPointInfos(const Camera_CaptureSession* session, uint32_t* size, OH_Camera_ZoomPointInfo** zoomPointInfo)
```

**描述**

获取变焦点信息。

需要通过调用[OH\_CaptureSession\_DeleteZoomPointInfos](capi-capture-session-h.md#oh_capturesession_deletezoompointinfos)来释放变焦点信息的内存。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const Camera\_CaptureSession](capi-oh-camera-camera-capturesession.md)\* session | 捕获会话对象的实例指针。 |
| uint32\_t\* size | 输出参数，返回查询到的变焦点信息数量。 |
| [OH\_Camera\_ZoomPointInfo](capi-oh-camera-oh-camera-zoompointinfo.md)\*\* zoomPointInfo | 输出参数，返回查询到的变焦点信息数组。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或者参数不正确。  CAMERA\_OPERATION\_NOT\_ALLOWED：操作不允许。  CAMERA\_SESSION\_NOT\_CONFIG：捕获会话未配置。 |

### OH\_CaptureSession\_DeleteZoomPointInfos()

```c
Camera_ErrorCode OH_CaptureSession_DeleteZoomPointInfos(const Camera_CaptureSession* session, OH_Camera_ZoomPointInfo* zoomPointInfo)
```

**描述**

删除变焦点信息。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const Camera\_CaptureSession](capi-oh-camera-camera-capturesession.md)\* session | 捕获会话对象的实例指针。 |
| [OH\_Camera\_ZoomPointInfo](capi-oh-camera-oh-camera-zoompointinfo.md)\* zoomPointInfo | 待删除的变焦点信息数组，方法调用成功后该内存将被释放。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或者参数不正确。 |

### OH\_CaptureSession\_IsLockFocusTrackingSupported()

```c
bool OH_CaptureSession_IsLockFocusTrackingSupported(const Camera_CaptureSession* session)
```

**描述**

查询是否支持锁定焦点跟踪。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const Camera\_CaptureSession](capi-oh-camera-camera-capturesession.md)\* session | 指向Camera\_CaptureSession实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| bool | 是否支持追焦跟踪功能，返回true表示支持，返回false表示不支持。 |

### OH\_CaptureSession\_LockFocusTracking()

```c
Camera_ErrorCode OH_CaptureSession_LockFocusTracking(Camera_CaptureSession* session, Camera_Point focusPoint)
```

**描述**

锁定焦点跟踪，可通过[OH\_CaptureSession\_UnlockFocusTracking](capi-capture-session-h.md#oh_capturesession_unlockfocustracking)解锁。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_CaptureSession](capi-oh-camera-camera-capturesession.md)\* session | 指向Camera\_CaptureSession实例的指针。 |
| [Camera\_Point](capi-oh-camera-camera-point.md) focusPoint | 锁定焦点跟踪的追踪点。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或者参数不正确。  CAMERA\_SERVICE\_FATAL\_ERROR：相机服务异常。 |

### OH\_CaptureSession\_UnlockFocusTracking()

```c
Camera_ErrorCode OH_CaptureSession_UnlockFocusTracking(Camera_CaptureSession* session)
```

**描述**

解锁焦点跟踪。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Camera\_CaptureSession](capi-oh-camera-camera-capturesession.md)\* session | 指向Camera\_CaptureSession实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或者参数不正确。  CAMERA\_SERVICE\_FATAL\_ERROR：相机服务异常。 |
