---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-avscreen-capture-h
title: native_avscreen_capture.h
breadcrumb: API参考 > 媒体 > Media Kit（媒体服务） > C API > 头文件 > native_avscreen_capture.h
category: harmonyos-references
scraped_at: 2026-04-28T08:13:54+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:eb18610bac53a55ffb11c4c1341a6662d4f1ab2bef8b5ea9389180aa6c50450c
---

## 概述

PhonePC/2in1TabletTV

声明用于构造屏幕录制对象的API。

**引用文件：** <multimedia/player\_framework/native\_avscreen\_capture.h>

**库：** libnative\_avscreen\_capture.so

**系统能力：** SystemCapability.Multimedia.Media.AVScreenCapture

**起始版本：** 10

**相关模块：** [AVScreenCapture](capi-avscreencapture.md)

**相关示例：** [NativeAvScreenCapture](https://gitcode.com/openharmony/applications_app_samples/tree/master/code/DocsSample/Media/ScreenCapture/ScreenCaptureSample)

## 汇总

PhonePC/2in1TabletTV

### 函数

PhonePC/2in1TabletTV

| 名称 | 描述 |
| --- | --- |
| [struct OH\_AVScreenCapture \*OH\_AVScreenCapture\_Create(void)](capi-native-avscreen-capture-h.md#oh_avscreencapture_create) | 实例化对象，创建OH\_AVScreenCapture。  可以通过调用[OH\_AVScreenCapture\_Release](capi-native-avscreen-capture-h.md#oh_avscreencapture_release)释放实例。 |
| [OH\_AVSCREEN\_CAPTURE\_ErrCode OH\_AVScreenCapture\_Init(struct OH\_AVScreenCapture \*capture, OH\_AVScreenCaptureConfig config)](capi-native-avscreen-capture-h.md#oh_avscreencapture_init) | 初始化[OH\_AVScreenCapture](capi-avscreencapture-oh-avscreencapture.md)相关参数，包括下发的音频麦克风采样相关参数（可选）、音频内录采样相关参数、视频分辨率相关参数。 |
| [OH\_AVSCREEN\_CAPTURE\_ErrCode OH\_AVScreenCapture\_StartScreenCapture(struct OH\_AVScreenCapture \*capture)](capi-native-avscreen-capture-h.md#oh_avscreencapture_startscreencapture) | 开始录屏，采集原始码流。 |
| [OH\_AVSCREEN\_CAPTURE\_ErrCode OH\_AVScreenCapture\_StopScreenCapture(struct OH\_AVScreenCapture \*capture)](capi-native-avscreen-capture-h.md#oh_avscreencapture_stopscreencapture) | 结束录屏，与[OH\_AVScreenCapture\_StartScreenCapture](capi-native-avscreen-capture-h.md#oh_avscreencapture_startscreencapture)配合使用。调用后针对调用该接口的应用会停止录屏或屏幕共享，释放麦克风。 |
| [OH\_AVSCREEN\_CAPTURE\_ErrCode OH\_AVScreenCapture\_StartScreenRecording(struct OH\_AVScreenCapture \*capture)](capi-native-avscreen-capture-h.md#oh_avscreencapture_startscreenrecording) | 启动录屏，调用此接口，可保存录屏文件。 |
| [OH\_AVSCREEN\_CAPTURE\_ErrCode OH\_AVScreenCapture\_StopScreenRecording(struct OH\_AVScreenCapture \*capture)](capi-native-avscreen-capture-h.md#oh_avscreencapture_stopscreenrecording) | 停止录屏，与[OH\_AVScreenCapture\_StartScreenRecording](capi-native-avscreen-capture-h.md#oh_avscreencapture_startscreenrecording)配合使用。 |
| [OH\_AVSCREEN\_CAPTURE\_ErrCode OH\_AVScreenCapture\_AcquireAudioBuffer(struct OH\_AVScreenCapture \*capture, OH\_AudioBuffer \*\*audiobuffer, OH\_AudioCaptureSourceType type)](capi-native-avscreen-capture-h.md#oh_avscreencapture_acquireaudiobuffer) | 获取音频buffer。应用调用时需分配audiobuffer对应结构体大小的内存，否则影响音频buffer的获取。  从API version 12开始，推荐使用接口[OH\_AVScreenCapture\_OnBufferAvailable](capi-native-avscreen-capture-base-h.md#oh_avscreencapture_onbufferavailable)替代。 |
| [OH\_NativeBuffer\* OH\_AVScreenCapture\_AcquireVideoBuffer(struct OH\_AVScreenCapture \*capture, int32\_t \*fence, int64\_t \*timestamp, struct OH\_Rect \*region)](capi-native-avscreen-capture-h.md#oh_avscreencapture_acquirevideobuffer) | 获取视频buffer。应用通过此接口获取视频缓存区及时间戳等信息。  buffer使用完成后，调用OH\_AVScreenCapture\_ReleaseVideoBuffer接口进行视频buffer的释放。  从API version 12开始，推荐使用接口[OH\_AVScreenCapture\_OnBufferAvailable](capi-native-avscreen-capture-base-h.md#oh_avscreencapture_onbufferavailable)替代。 |
| [OH\_AVSCREEN\_CAPTURE\_ErrCode OH\_AVScreenCapture\_ReleaseAudioBuffer(struct OH\_AVScreenCapture \*capture, OH\_AudioCaptureSourceType type)](capi-native-avscreen-capture-h.md#oh_avscreencapture_releaseaudiobuffer) | 根据音频类型释放buffer。当某一帧音频buffer使用完成后，调用此接口进行释放对应的音频buffer。  从API version 12开始，推荐使用接口[OH\_AVScreenCapture\_OnBufferAvailable](capi-native-avscreen-capture-base-h.md#oh_avscreencapture_onbufferavailable)替代。 |
| [OH\_AVSCREEN\_CAPTURE\_ErrCode OH\_AVScreenCapture\_ReleaseVideoBuffer(struct OH\_AVScreenCapture \*capture)](capi-native-avscreen-capture-h.md#oh_avscreencapture_releasevideobuffer) | 根据视频类型释放buffer。当某一帧视频buffer使用完成后，调用此接口释放对应的视频buffer。  从API version 12开始，推荐使用接口[OH\_AVScreenCapture\_OnBufferAvailable](capi-native-avscreen-capture-base-h.md#oh_avscreencapture_onbufferavailable)替代。 |
| [OH\_AVSCREEN\_CAPTURE\_ErrCode OH\_AVScreenCapture\_SetCallback(struct OH\_AVScreenCapture \*capture, struct OH\_AVScreenCaptureCallback callback)](capi-native-avscreen-capture-h.md#oh_avscreencapture_setcallback) | 设置监听接口，通过设置监听，可以监听到调用过程中的错误信息，以及是否有可用的视频buffer和音频buffer。  从API version 12开始，推荐使用接口[OH\_AVScreenCapture\_SetErrorCallback](capi-native-avscreen-capture-h.md#oh_avscreencapture_seterrorcallback)、[OH\_AVScreenCapture\_SetDataCallback](capi-native-avscreen-capture-h.md#oh_avscreencapture_setdatacallback)替代。 |
| [OH\_AVSCREEN\_CAPTURE\_ErrCode OH\_AVScreenCapture\_Release(struct OH\_AVScreenCapture \*capture)](capi-native-avscreen-capture-h.md#oh_avscreencapture_release) | 释放创建的OH\_AVScreenCapture实例，对应[OH\_AVScreenCapture\_Create](capi-native-avscreen-capture-h.md#oh_avscreencapture_create)。 |
| [OH\_AVSCREEN\_CAPTURE\_ErrCode OH\_AVScreenCapture\_SetMicrophoneEnabled(struct OH\_AVScreenCapture \*capture, bool isMicrophone)](capi-native-avscreen-capture-h.md#oh_avscreencapture_setmicrophoneenabled) | 设置麦克风开关。  当isMicrophone为true时，则打开麦克风，通过调用[OH\_AVScreenCapture\_StartScreenCapture](capi-native-avscreen-capture-h.md#oh_avscreencapture_startscreencapture)和[OH\_AVScreenCapture\_AcquireAudioBuffer](capi-native-avscreen-capture-h.md#oh_avscreencapture_acquireaudiobuffer)可以正常获取到音频的麦克风原始PCM数据；isMicrophone为false时，获取到的音频数据为无声数据。  默认麦克风开关为开启。 |
| [OH\_AVSCREEN\_CAPTURE\_ErrCode OH\_AVScreenCapture\_SetStateCallback(struct OH\_AVScreenCapture \*capture, OH\_AVScreenCapture\_OnStateChange callback, void \*userData)](capi-native-avscreen-capture-h.md#oh_avscreencapture_setstatecallback) | 设置状态变更处理回调方法，在开始录制前调用。 |
| [OH\_AVSCREEN\_CAPTURE\_ErrCode OH\_AVScreenCapture\_SetDataCallback(struct OH\_AVScreenCapture \*capture, OH\_AVScreenCapture\_OnBufferAvailable callback, void \*userData)](capi-native-avscreen-capture-h.md#oh_avscreencapture_setdatacallback) | 设置数据处理回调方法，在开始录制前调用。 |
| [OH\_AVSCREEN\_CAPTURE\_ErrCode OH\_AVScreenCapture\_SetErrorCallback(struct OH\_AVScreenCapture \*capture, OH\_AVScreenCapture\_OnError callback, void \*userData)](capi-native-avscreen-capture-h.md#oh_avscreencapture_seterrorcallback) | 设置错误处理回调方法，在开始录制前调用。 |
| [OH\_AVSCREEN\_CAPTURE\_ErrCode OH\_AVScreenCapture\_StartScreenCaptureWithSurface(struct OH\_AVScreenCapture \*capture, OHNativeWindow \*window)](capi-native-avscreen-capture-h.md#oh_avscreencapture_startscreencapturewithsurface) | 使用Surface模式录屏。 |
| [OH\_AVSCREEN\_CAPTURE\_ErrCode OH\_AVScreenCapture\_SetCanvasRotation(struct OH\_AVScreenCapture \*capture, bool canvasRotation)](capi-native-avscreen-capture-h.md#oh_avscreencapture_setcanvasrotation) | 设置录屏屏幕数据旋转。  调用该方法可以设置录屏屏幕数据是否旋转，当canvasRotation为true时，打开录屏屏幕数据旋转功能，录制的屏幕数据保持正向。  默认为false。 |
| [struct OH\_AVScreenCapture\_ContentFilter \*OH\_AVScreenCapture\_CreateContentFilter(void)](capi-native-avscreen-capture-h.md#oh_avscreencapture_createcontentfilter) | 创建ContentFilter。 |
| [OH\_AVSCREEN\_CAPTURE\_ErrCode OH\_AVScreenCapture\_ReleaseContentFilter(struct OH\_AVScreenCapture\_ContentFilter \*filter)](capi-native-avscreen-capture-h.md#oh_avscreencapture_releasecontentfilter) | 释放ContentFilter。 |
| [OH\_AVSCREEN\_CAPTURE\_ErrCode OH\_AVScreenCapture\_ContentFilter\_AddAudioContent(struct OH\_AVScreenCapture\_ContentFilter \*filter, OH\_AVScreenCaptureFilterableAudioContent content)](capi-native-avscreen-capture-h.md#oh_avscreencapture_contentfilter_addaudiocontent) | 向ContentFilter实例添加可过滤的声音类型。 |
| [OH\_AVSCREEN\_CAPTURE\_ErrCode OH\_AVScreenCapture\_ExcludeContent(struct OH\_AVScreenCapture \*capture, struct OH\_AVScreenCapture\_ContentFilter \*filter)](capi-native-avscreen-capture-h.md#oh_avscreencapture_excludecontent) | 设置OH\_AVScreenCapture实例的内容过滤器ContentFilter。 |
| [OH\_AVSCREEN\_CAPTURE\_ErrCode OH\_AVScreenCapture\_ContentFilter\_AddWindowContent(struct OH\_AVScreenCapture\_ContentFilter \*filter, int32\_t \*windowIDs, int32\_t windowCount)](capi-native-avscreen-capture-h.md#oh_avscreencapture_contentfilter_addwindowcontent) | 向ContentFilter实例添加可被过滤的窗口ID列表。 |
| [OH\_AVSCREEN\_CAPTURE\_ErrCode OH\_AVScreenCapture\_ResizeCanvas(struct OH\_AVScreenCapture \*capture, int32\_t width, int32\_t height)](capi-native-avscreen-capture-h.md#oh_avscreencapture_resizecanvas) | 调整屏幕的分辨率。  调用该方法可以设置录屏屏幕数据的分辨率，width为屏幕的宽度，height为屏幕的高度。  该接口目前仅支持录屏取码流的场景，不支持录屏存文件的场景。并且调用该接口的调用者以及视频数据的消费者需要确保自身能够支持收到的视频数据分辨率发生变化。 |
| [OH\_AVSCREEN\_CAPTURE\_ErrCode OH\_AVScreenCapture\_SkipPrivacyMode(struct OH\_AVScreenCapture \*capture, int32\_t \*windowIDs, int32\_t windowCount)](capi-native-avscreen-capture-h.md#oh_avscreencapture_skipprivacymode) | 录屏时豁免隐私窗口。  调用该方法可以豁免隐私窗口，windowIDs为需要豁免的隐私窗口ID指针，windowCount 为隐私窗口ID列表的长度，目前豁免需要传入所有隐私子窗口和主窗口ID。 |
| [OH\_AVSCREEN\_CAPTURE\_ErrCode OH\_AVScreenCapture\_SetMaxVideoFrameRate(struct OH\_AVScreenCapture \*capture, int32\_t frameRate)](capi-native-avscreen-capture-h.md#oh_avscreencapture_setmaxvideoframerate) | 设置录屏时的最大帧率。  该接口应在录屏启动之后被调用。  调用该方法可以设置录屏时的最大帧率，frameRate为想要设置的最大帧率。  该接口设置最大帧率时，实际设置的帧率受限设备的能力，由底层的系统能力决定。  调用该接口设置录屏最大帧率时，实际帧率将受限于设备能力。目前接口入参的最大值不设限制，但当前支持的最高帧率为60FPS，当入参设置超过60FPS，将以60FPS处理。不超过上限时，则按照实际入参值处理。 |
| [OH\_AVSCREEN\_CAPTURE\_ErrCode OH\_AVScreenCapture\_ShowCursor(struct OH\_AVScreenCapture \*capture, bool showCursor)](capi-native-avscreen-capture-h.md#oh_avscreencapture_showcursor) | 设置光标显示开关。 |
| [OH\_AVSCREEN\_CAPTURE\_ErrCode OH\_AVScreenCapture\_SetDisplayCallback(struct OH\_AVScreenCapture \*capture, OH\_AVScreenCapture\_OnDisplaySelected callback, void \*userData)](capi-native-avscreen-capture-h.md#oh_avscreencapture_setdisplaycallback) | 设置获取录屏屏幕Id的回调。 |
| [OH\_AVScreenCapture\_CaptureStrategy\* OH\_AVScreenCapture\_CreateCaptureStrategy(void)](capi-native-avscreen-capture-h.md#oh_avscreencapture_createcapturestrategy) | 创建录屏策略对象。 |
| [OH\_AVSCREEN\_CAPTURE\_ErrCode OH\_AVScreenCapture\_ReleaseCaptureStrategy(OH\_AVScreenCapture\_CaptureStrategy\* strategy)](capi-native-avscreen-capture-h.md#oh_avscreencapture_releasecapturestrategy) | 释放录屏策略对象。 |
| [OH\_AVSCREEN\_CAPTURE\_ErrCode OH\_AVScreenCapture\_SetCaptureStrategy(struct OH\_AVScreenCapture \*capture, OH\_AVScreenCapture\_CaptureStrategy \*strategy)](capi-native-avscreen-capture-h.md#oh_avscreencapture_setcapturestrategy) | 给指定的OH\_AVScreenCapture实例设置捕获策略。  该接口应在录屏启动之前被调用。 |
| [OH\_AVSCREEN\_CAPTURE\_ErrCode OH\_AVScreenCapture\_StrategyForCanvasFollowRotation(OH\_AVScreenCapture\_CaptureStrategy \*strategy, bool value)](capi-native-avscreen-capture-h.md#oh_avscreencapture_strategyforcanvasfollowrotation) | 设置屏幕录屏自动跟随旋转配置。设为true，表示跟随屏幕旋转，并在横竖屏旋转后，自动调换虚拟屏尺寸，确保输出画面及时跟随旋转。  设置是否自动跟随旋转配置后，在旋转通知后，无需再手动调用[OH\_AVScreenCapture\_ResizeCanvas](capi-native-avscreen-capture-h.md#oh_avscreencapture_resizecanvas)接口。 |
| [OH\_AVSCREEN\_CAPTURE\_ErrCode OH\_AVScreenCapture\_StrategyForKeepCaptureDuringCall(OH\_AVScreenCapture\_CaptureStrategy \*strategy, bool value)](capi-native-avscreen-capture-h.md#oh_avscreencapture_strategyforkeepcaptureduringcall) | 向CaptureStrategy实例设置蜂窝通话时是否保持录屏。  value设置为true时并且录屏时接听蜂窝通话的过程中，出于隐私要求，双方通话的声音（本地麦克风和对方说话声音）不会被录制，其他系统音录制正常。电话挂断之后，录屏框架恢复麦克风录制。注意，如果挂断电话时录屏应用在后台运行，麦克风录制会启动失败，原因是音频模块不允许后台应用启动麦克风录制。 |
| [OH\_AVSCREEN\_CAPTURE\_ErrCode OH\_AVScreenCapture\_SetCaptureContentChangedCallback(struct OH\_AVScreenCapture \*capture, OH\_AVScreenCapture\_OnCaptureContentChanged callback, void \*userData)](capi-native-avscreen-capture-h.md#oh_avscreencapture_setcapturecontentchangedcallback) | 设置录屏内容变更回调事件，需在录屏启动前被调用。 |
| [OH\_AVSCREEN\_CAPTURE\_ErrCode OH\_AVScreenCapture\_SetCaptureArea(struct OH\_AVScreenCapture \*capture, uint64\_t displayId, OH\_Rect\* area)](capi-native-avscreen-capture-h.md#oh_avscreencapture_setcapturearea) | 设置或更新捕获区域。  接口在开始录屏前后都可以设置，设置的坐标和宽高不能为负数，捕获区域不能跨屏幕，区域位置设置失败后仍按照上一次的区域进行捕获。 |
| [OH\_AVSCREEN\_CAPTURE\_ErrCode OH\_AVScreenCapture\_StrategyForPrivacyMaskMode(OH\_AVScreenCapture\_CaptureStrategy \*strategy, int32\_t value)](capi-native-avscreen-capture-h.md#oh_avscreencapture_strategyforprivacymaskmode) | 设置隐私窗口屏蔽模式。 |
| [OH\_AVSCREEN\_CAPTURE\_ErrCode OH\_AVScreenCapture\_SetSelectionCallback(struct OH\_AVScreenCapture \*capture, OH\_AVScreenCapture\_OnUserSelected callback, void \*userData)](capi-native-avscreen-capture-h.md#oh_avscreencapture_setselectioncallback) | 注册手工确认界面用户选择结果的回调，需在录屏启动前被调用。 |
| [OH\_AVSCREEN\_CAPTURE\_ErrCode OH\_AVScreenCapture\_GetCaptureTypeSelected(OH\_AVScreenCapture\_UserSelectionInfo \*selection, int32\_t\* type)](capi-native-avscreen-capture-h.md#oh_avscreencapture_getcapturetypeselected) | 获取用户在确认界面选择的屏幕捕获对象类型。在[OH\_AVScreenCapture\_OnUserSelected](capi-native-avscreen-capture-base-h.md#oh_avscreencapture_onuserselected)回调中使用，selection指针在回调结束后销毁。 |
| [OH\_AVSCREEN\_CAPTURE\_ErrCode OH\_AVScreenCapture\_GetDisplayIdSelected(OH\_AVScreenCapture\_UserSelectionInfo \*selection, uint64\_t\* displayId)](capi-native-avscreen-capture-h.md#oh_avscreencapture_getdisplayidselected) | 获取确认页面，用户选择录制的屏幕ID。在[OH\_AVScreenCapture\_OnUserSelected](capi-native-avscreen-capture-base-h.md#oh_avscreencapture_onuserselected)回调中使用，selection指针在回调结束后销毁。 |
| [OH\_AVSCREEN\_CAPTURE\_ErrCode OH\_AVScreenCapture\_StrategyForBFramesEncoding(OH\_AVScreenCapture\_CaptureStrategy \*strategy, bool value)](capi-native-avscreen-capture-h.md#oh_avscreencapture_strategyforbframesencoding) | 向CaptureStrategy实例设置是否使能B帧编码，用于减小录制文件的大小。  B帧视频编码相关的约束和限制可以参考文档[B帧视频编码约束和限制](../harmonyos-guides/video-encoding-b-frame.md#约束和限制)。如果当前不符合B帧视频编码的约束和限制，则正常录制不含B帧的视频，不会返回错误。 |
| [OH\_AVSCREEN\_CAPTURE\_ErrCode OH\_AVScreenCapture\_StrategyForPickerPopUp(OH\_AVScreenCapture\_CaptureStrategy \*strategy, bool value)](capi-native-avscreen-capture-h.md#oh_avscreencapture_strategyforpickerpopup) | 设置是否弹出屏幕捕获Picker。 |
| [OH\_AVSCREEN\_CAPTURE\_ErrCode OH\_AVScreenCapture\_StrategyForFillMode(OH\_AVScreenCapture\_CaptureStrategy \*strategy, OH\_AVScreenCapture\_FillMode mode)](capi-native-avscreen-capture-h.md#oh_avscreencapture_strategyforfillmode) | 设置捕获图像在目标区域的填充模式。 |
| [OH\_AVSCREEN\_CAPTURE\_ErrCode OH\_AVScreenCapture\_PresentPicker(struct OH\_AVScreenCapture \*capture)](capi-native-avscreen-capture-h.md#oh_avscreencapture_presentpicker) | 录屏开始后，调用该接口再次弹出picker，可动态更新录制源（窗口、屏幕）。更新录制源过程中，原录制流程不中断。  通过picker动态更新录制源后，可以按照新的录制源进行录制。 |
| [OH\_AVSCREEN\_CAPTURE\_ErrCode OH\_AVScreenCapture\_SetCaptureAreaHighlight(struct OH\_AVScreenCapture \*capture, OH\_AVScreenCaptureHighlightConfig config)](capi-native-avscreen-capture-h.md#oh_avscreencapture_setcaptureareahighlight) | 设置屏幕捕获区域高亮模式。 |
| [OH\_AVSCREEN\_CAPTURE\_ErrCode OH\_AVScreenCapture\_SetPickerMode(struct OH\_AVScreenCapture \*capture, OH\_CapturePickerMode pickerMode)](capi-native-avscreen-capture-h.md#oh_avscreencapture_setpickermode) | 设置Picker显示模式。定义picker中显示的内容类型，模式更改会在下一次调用[OH\_AVScreenCapture\_PresentPicker](capi-native-avscreen-capture-h.md#oh_avscreencapture_presentpicker) 函数时生效。 |
| [OH\_AVSCREEN\_CAPTURE\_ErrCode OH\_AVScreenCapture\_ExcludePickerWindows(struct OH\_AVScreenCapture \*capture, const int32\_t \*excludedWindowIDs, uint32\_t windowCount)](capi-native-avscreen-capture-h.md#oh_avscreencapture_excludepickerwindows) | 在Picker界面中隐藏指定的窗口。在picker界面显示前调用本接口，可对指定窗口进行过滤和隐藏。 |

## 函数说明

PhonePC/2in1TabletTV

### OH\_AVScreenCapture\_Create()

PhonePC/2in1TabletTV

```
1. struct OH_AVScreenCapture *OH_AVScreenCapture_Create(void)
```

**描述**

实例化对象，创建OH\_AVScreenCapture。

可以通过调用[OH\_AVScreenCapture\_Release](capi-native-avscreen-capture-h.md#oh_avscreencapture_release)释放实例。

**系统能力：** SystemCapability.Multimedia.Media.AVScreenCapture

**起始版本：** 10

**返回：**

| 类型 | 说明 |
| --- | --- |
| [struct OH\_AVScreenCapture](capi-avscreencapture-oh-avscreencapture.md) \* | 返回一个指向OH\_AVScreenCapture实例的指针。 |

### OH\_AVScreenCapture\_Init()

PhonePC/2in1TabletTV

```
1. OH_AVSCREEN_CAPTURE_ErrCode OH_AVScreenCapture_Init(struct OH_AVScreenCapture *capture, OH_AVScreenCaptureConfig config)
```

**描述**

初始化[OH\_AVScreenCapture](capi-avscreencapture-oh-avscreencapture.md)相关参数，包括下发的音频麦克风采样相关参数（可选）、音频内录采样相关参数、视频分辨率相关参数。

录屏存文件场景，应用需要保证视频编码参数、视频采样参数、音频编码参数、音频内录采样参数均合法，音频麦克风采样参数合法（可选）。

录屏出码流场景，应用需要保证音频内录采样参数、视频采样参数至少一个合法，音频麦克风采样参数合法（可选）。

由于结构体变量在初始化时不会对成员进行初始化，应用必须根据使用场景正确设置各项参数。建议应用先将OH\_AVScreenCaptureConfig结构体变量的所有内存字节均设置为0，然后再根据录屏场景设置合法参数。

音频采样参数结构体[OH\_AudioCaptureInfo](capi-avscreencapture-oh-audiocaptureinfo.md)，若audioSampleRate和audioChannels同时为0，则录屏实例OH\_AVScreenCapture将忽略该类型的音频参数，且不采集该类型的音频数据。

视频采样参数结构体[OH\_VideoCaptureInfo](capi-avscreencapture-oh-videocaptureinfo.md)，若videoFrameWidth和videoFrameHeight同时为0，则录屏实例OH\_AVScreenCapture将忽略对应视频参数，且不采集屏幕数据。

**系统能力：** SystemCapability.Multimedia.Media.AVScreenCapture

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [struct OH\_AVScreenCapture](capi-avscreencapture-oh-avscreencapture.md) \*capture | 指向OH\_AVScreenCapture实例的指针。 |
| [OH\_AVScreenCaptureConfig](capi-avscreencapture-oh-avscreencaptureconfig.md) config | 录屏初始化相关参数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVSCREEN\_CAPTURE\_ErrCode](capi-native-avscreen-capture-errors-h.md#oh_avscreen_capture_errcode) | AV\_SCREEN\_CAPTURE\_ERR\_OK：执行成功。  AV\_SCREEN\_CAPTURE\_ERR\_INVALID\_VAL：输入参数capture为空指针。  AV\_SCREEN\_CAPTURE\_ERR\_OPERATE\_NOT\_PERMIT：不允许操作，初始化配置失败。 |

### OH\_AVScreenCapture\_StartScreenCapture()

PhonePC/2in1TabletTV

```
1. OH_AVSCREEN_CAPTURE_ErrCode OH_AVScreenCapture_StartScreenCapture(struct OH_AVScreenCapture *capture)
```

**描述**

开始录屏，采集原始码流。

调用后可以通过回调的监听（[OH\_AVScreenCapture\_OnBufferAvailable](capi-native-avscreen-capture-base-h.md#oh_avscreencapture_onbufferavailable)）来监听当前是否有码流的产生,通过回调的监听（[OH\_AVScreenCapture\_OnStateChange](capi-native-avscreen-capture-base-h.md#oh_avscreencapture_onstatechange)）来监听启动状态。

通过调用获取音频buffer（[OH\_AVScreenCapture\_AcquireAudioBuffer](capi-native-avscreen-capture-h.md#oh_avscreencapture_acquireaudiobuffer)）和视频buffer（[OH\_AVScreenCapture\_AcquireVideoBuffer](capi-native-avscreen-capture-h.md#oh_avscreencapture_acquirevideobuffer)）的接口来获取录屏的原始码流。

**系统能力：** SystemCapability.Multimedia.Media.AVScreenCapture

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [struct OH\_AVScreenCapture](capi-avscreencapture-oh-avscreencapture.md) \*capture | 指向OH\_AVScreenCapture实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVSCREEN\_CAPTURE\_ErrCode](capi-native-avscreen-capture-errors-h.md#oh_avscreen_capture_errcode) | AV\_SCREEN\_CAPTURE\_ERR\_OK：执行成功。  AV\_SCREEN\_CAPTURE\_ERR\_INVALID\_VAL：输入参数capture为空指针。  AV\_SCREEN\_CAPTURE\_ERR\_UNSUPPORT（API version 20新增）：设备不支持该操作。  AV\_SCREEN\_CAPTURE\_ERR\_OPERATE\_NOT\_PERMIT：不允许操作，设置隐私权限启用失败或启动录屏失败。 |

### OH\_AVScreenCapture\_StopScreenCapture()

PhonePC/2in1TabletTV

```
1. OH_AVSCREEN_CAPTURE_ErrCode OH_AVScreenCapture_StopScreenCapture(struct OH_AVScreenCapture *capture)
```

**描述**

结束录屏，与[OH\_AVScreenCapture\_StartScreenCapture](capi-native-avscreen-capture-h.md#oh_avscreencapture_startscreencapture)配合使用。调用后针对调用该接口的应用会停止录屏或屏幕共享，释放麦克风。

**系统能力：** SystemCapability.Multimedia.Media.AVScreenCapture

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [struct OH\_AVScreenCapture](capi-avscreencapture-oh-avscreencapture.md) \*capture | 指向OH\_AVScreenCapture实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVSCREEN\_CAPTURE\_ErrCode](capi-native-avscreen-capture-errors-h.md#oh_avscreen_capture_errcode) | AV\_SCREEN\_CAPTURE\_ERR\_OK：执行成功。  AV\_SCREEN\_CAPTURE\_ERR\_INVALID\_VAL：输入参数capture为空指针。  AV\_SCREEN\_CAPTURE\_ERR\_OPERATE\_NOT\_PERMIT：不允许操作，结束录屏失败。 |

### OH\_AVScreenCapture\_StartScreenRecording()

PhonePC/2in1TabletTV

```
1. OH_AVSCREEN_CAPTURE_ErrCode OH_AVScreenCapture_StartScreenRecording(struct OH_AVScreenCapture *capture)
```

**描述**

启动录屏，调用此接口，可保存录屏文件。

**系统能力：** SystemCapability.Multimedia.Media.AVScreenCapture

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [struct OH\_AVScreenCapture](capi-avscreencapture-oh-avscreencapture.md) \*capture | 指向OH\_AVScreenCapture实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVSCREEN\_CAPTURE\_ErrCode](capi-native-avscreen-capture-errors-h.md#oh_avscreen_capture_errcode) | AV\_SCREEN\_CAPTURE\_ERR\_OK：执行成功。  AV\_SCREEN\_CAPTURE\_ERR\_INVALID\_VAL：输入参数capture为空指针。  AV\_SCREEN\_CAPTURE\_ERR\_UNSUPPORT（API version 20新增）：设备不支持该操作。  AV\_SCREEN\_CAPTURE\_ERR\_OPERATE\_NOT\_PERMIT：不允许操作，设置隐私权限启用失败或启用屏幕录制失败。 |

### OH\_AVScreenCapture\_StopScreenRecording()

PhonePC/2in1TabletTV

```
1. OH_AVSCREEN_CAPTURE_ErrCode OH_AVScreenCapture_StopScreenRecording(struct OH_AVScreenCapture *capture)
```

**描述**

停止录屏，与[OH\_AVScreenCapture\_StartScreenRecording](capi-native-avscreen-capture-h.md#oh_avscreencapture_startscreenrecording)配合使用。

**系统能力：** SystemCapability.Multimedia.Media.AVScreenCapture

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [struct OH\_AVScreenCapture](capi-avscreencapture-oh-avscreencapture.md) \*capture | 指向OH\_AVScreenCapture实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVSCREEN\_CAPTURE\_ErrCode](capi-native-avscreen-capture-errors-h.md#oh_avscreen_capture_errcode) | AV\_SCREEN\_CAPTURE\_ERR\_OK：执行成功。  AV\_SCREEN\_CAPTURE\_ERR\_INVALID\_VAL：输入参数capture为空指针。  AV\_SCREEN\_CAPTURE\_ERR\_OPERATE\_NOT\_PERMIT：不允许操作，停止屏幕录制失败。 |

### OH\_AVScreenCapture\_AcquireAudioBuffer()

PhonePC/2in1TabletTV

```
1. OH_AVSCREEN_CAPTURE_ErrCode OH_AVScreenCapture_AcquireAudioBuffer(struct OH_AVScreenCapture *capture, OH_AudioBuffer **audiobuffer, OH_AudioCaptureSourceType type)
```

**描述**

获取音频buffer。应用调用时需分配audiobuffer对应结构体大小的内存，否则影响音频buffer的获取。

从API version 12开始，推荐使用接口[OH\_AVScreenCapture\_OnBufferAvailable](capi-native-avscreen-capture-base-h.md#oh_avscreencapture_onbufferavailable)替代。

**系统能力：** SystemCapability.Multimedia.Media.AVScreenCapture

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [struct OH\_AVScreenCapture](capi-avscreencapture-oh-avscreencapture.md) \*capture | 指向OH\_AVScreenCapture实例的指针。 |
| [OH\_AudioBuffer](capi-avscreencapture-oh-audiobuffer.md) \*\*audiobuffer | 保存音频buffer的结构体，通过该结构体获取到音频buffer以及buffer的时间戳等信息。 |
| [OH\_AudioCaptureSourceType](capi-native-avscreen-capture-base-h.md#oh_audiocapturesourcetype) type | 音频buffer的类型，区分是麦克风录制的外部流还是系统内部播放音频的内录流。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVSCREEN\_CAPTURE\_ErrCode](capi-native-avscreen-capture-errors-h.md#oh_avscreen_capture_errcode) | AV\_SCREEN\_CAPTURE\_ERR\_OK：执行成功。  AV\_SCREEN\_CAPTURE\_ERR\_INVALID\_VAL：输入参数capture为空指针或输入参数audiobuffer为空指针。  AV\_SCREEN\_CAPTURE\_ERR\_NO\_MEMORY：内存不足，audiobuffer分配失败。  AV\_SCREEN\_CAPTURE\_ERR\_OPERATE\_NOT\_PERMIT：不允许操作，设置隐私权限启用失败或获取音频buffer失败。 |

### OH\_AVScreenCapture\_AcquireVideoBuffer()

PhonePC/2in1TabletTV

```
1. OH_NativeBuffer* OH_AVScreenCapture_AcquireVideoBuffer(struct OH_AVScreenCapture *capture, int32_t *fence, int64_t *timestamp, struct OH_Rect *region)
```

**描述**

获取视频buffer。应用通过此接口获取视频缓存区及时间戳等信息。

buffer使用完成后，调用OH\_AVScreenCapture\_ReleaseVideoBuffer接口进行视频buffer的释放。

从API version 12开始，推荐使用接口[OH\_AVScreenCapture\_OnBufferAvailable](capi-native-avscreen-capture-base-h.md#oh_avscreencapture_onbufferavailable)替代。

**系统能力：** SystemCapability.Multimedia.Media.AVScreenCapture

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [struct OH\_AVScreenCapture](capi-avscreencapture-oh-avscreencapture.md) \*capture | 指向OH\_AVScreenCapture实例的指针。 |
| int32\_t \*fence | 用于同步的显示相关参数信息。 |
| int64\_t \*timestamp | 视频帧的时间戳。 |
| [struct OH\_Rect](capi-avscreencapture-oh-rect.md) \*region | 视频显示相关的坐标信息。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_NativeBuffer](pi-avscreencapture-avscreencapture-oh-nativebuffer.md)\* | 执行成功返回OH\_NativeBuffer对象，通过OH\_NativeBuffer对象相关接口可以获取到视频buffer和分辨率等信息参数。 |

### OH\_AVScreenCapture\_ReleaseAudioBuffer()

PhonePC/2in1TabletTV

```
1. OH_AVSCREEN_CAPTURE_ErrCode OH_AVScreenCapture_ReleaseAudioBuffer(struct OH_AVScreenCapture *capture, OH_AudioCaptureSourceType type)
```

**描述**

根据音频类型释放buffer。当某一帧音频buffer使用完成后，调用此接口进行释放对应的音频buffer。

从API version 12开始，推荐使用接口[OH\_AVScreenCapture\_OnBufferAvailable](capi-native-avscreen-capture-base-h.md#oh_avscreencapture_onbufferavailable)替代。

**系统能力：** SystemCapability.Multimedia.Media.AVScreenCapture

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [struct OH\_AVScreenCapture](capi-avscreencapture-oh-avscreencapture.md) \*capture | 指向OH\_AVScreenCapture实例的指针。 |
| [OH\_AudioCaptureSourceType](capi-native-avscreen-capture-base-h.md#oh_audiocapturesourcetype) type | 音频buffer的类型，区分麦克风录制的外部流还是系统内部播放音频的内录流。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVSCREEN\_CAPTURE\_ErrCode](capi-native-avscreen-capture-errors-h.md#oh_avscreen_capture_errcode) | AV\_SCREEN\_CAPTURE\_ERR\_OK：执行成功。  AV\_SCREEN\_CAPTURE\_ERR\_INVALID\_VAL：输入参数capture为空指针。  AV\_SCREEN\_CAPTURE\_ERR\_OPERATE\_NOT\_PERMIT：不允许操作，不允许用于已设置过DataCallback或释放音频buffer失败。 |

### OH\_AVScreenCapture\_ReleaseVideoBuffer()

PhonePC/2in1TabletTV

```
1. OH_AVSCREEN_CAPTURE_ErrCode OH_AVScreenCapture_ReleaseVideoBuffer(struct OH_AVScreenCapture *capture)
```

**描述**

根据视频类型释放buffer。当某一帧视频buffer使用完成后，调用此接口释放对应的视频buffer。

从API version 12开始，推荐使用接口[OH\_AVScreenCapture\_OnBufferAvailable](capi-native-avscreen-capture-base-h.md#oh_avscreencapture_onbufferavailable)替代。

**系统能力：** SystemCapability.Multimedia.Media.AVScreenCapture

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [struct OH\_AVScreenCapture](capi-avscreencapture-oh-avscreencapture.md) \*capture | 指向OH\_AVScreenCapture实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVSCREEN\_CAPTURE\_ErrCode](capi-native-avscreen-capture-errors-h.md#oh_avscreen_capture_errcode) | AV\_SCREEN\_CAPTURE\_ERR\_OK：执行成功。  AV\_SCREEN\_CAPTURE\_ERR\_INVALID\_VAL：输入参数capture为空指针。  AV\_SCREEN\_CAPTURE\_ERR\_OPERATE\_NOT\_PERMIT：不允许操作，不允许用于已设置过DataCallback或释放视频buffer失败。 |

### OH\_AVScreenCapture\_SetCallback()

PhonePC/2in1TabletTV

```
1. OH_AVSCREEN_CAPTURE_ErrCode OH_AVScreenCapture_SetCallback(struct OH_AVScreenCapture *capture, struct OH_AVScreenCaptureCallback callback)
```

**描述**

设置监听接口，通过设置监听，可以监听到调用过程中的错误信息，以及是否有可用的视频buffer和音频buffer。

从API version 12开始，推荐使用接口[OH\_AVScreenCapture\_SetErrorCallback](capi-native-avscreen-capture-h.md#oh_avscreencapture_seterrorcallback)、[OH\_AVScreenCapture\_SetDataCallback](capi-native-avscreen-capture-h.md#oh_avscreencapture_setdatacallback)替代。

**系统能力：** SystemCapability.Multimedia.Media.AVScreenCapture

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [struct OH\_AVScreenCapture](capi-avscreencapture-oh-avscreencapture.md) \*capture | 指向OH\_AVScreenCapture实例的指针。 |
| [struct OH\_AVScreenCaptureCallback](capi-avscreencapture-oh-avscreencapturecallback.md) callback | OH\_AVScreenCaptureCallback的结构体，保存相关回调函数指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVSCREEN\_CAPTURE\_ErrCode](capi-native-avscreen-capture-errors-h.md#oh_avscreen_capture_errcode) | AV\_SCREEN\_CAPTURE\_ERR\_OK：执行成功。  AV\_SCREEN\_CAPTURE\_ERR\_INVALID\_VAL：输入参数capture为空指针或输入参数callback为空指针。  AV\_SCREEN\_CAPTURE\_ERR\_OPERATE\_NOT\_PERMIT：不允许操作，设置监听接口失败。 |

### OH\_AVScreenCapture\_Release()

PhonePC/2in1TabletTV

```
1. OH_AVSCREEN_CAPTURE_ErrCode OH_AVScreenCapture_Release(struct OH_AVScreenCapture *capture)
```

**描述**

释放创建的OH\_AVScreenCapture实例，对应[OH\_AVScreenCapture\_Create](capi-native-avscreen-capture-h.md#oh_avscreencapture_create)。

**系统能力：** SystemCapability.Multimedia.Media.AVScreenCapture

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [struct OH\_AVScreenCapture](capi-avscreencapture-oh-avscreencapture.md) \*capture | 指向OH\_AVScreenCapture实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVSCREEN\_CAPTURE\_ErrCode](capi-native-avscreen-capture-errors-h.md#oh_avscreen_capture_errcode) | AV\_SCREEN\_CAPTURE\_ERR\_OK：执行成功。  AV\_SCREEN\_CAPTURE\_ERR\_INVALID\_VAL：输入参数capture为空指针。  AV\_SCREEN\_CAPTURE\_ERR\_OPERATE\_NOT\_PERMIT：不允许操作，OH\_AVScreenCapture实例释放失败。 |

### OH\_AVScreenCapture\_SetMicrophoneEnabled()

PhonePC/2in1TabletTV

```
1. OH_AVSCREEN_CAPTURE_ErrCode OH_AVScreenCapture_SetMicrophoneEnabled(struct OH_AVScreenCapture *capture, bool isMicrophone)
```

**描述**

设置麦克风开关。

当isMicrophone为true时，则打开麦克风，通过调用[OH\_AVScreenCapture\_StartScreenCapture](capi-native-avscreen-capture-h.md#oh_avscreencapture_startscreencapture)和[OH\_AVScreenCapture\_AcquireAudioBuffer](capi-native-avscreen-capture-h.md#oh_avscreencapture_acquireaudiobuffer)可以正常获取到音频的麦克风原始PCM数据；isMicrophone为false时，获取到的音频数据为无声数据。

默认麦克风开关为开启。

**系统能力：** SystemCapability.Multimedia.Media.AVScreenCapture

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [struct OH\_AVScreenCapture](capi-avscreencapture-oh-avscreencapture.md) \*capture | 指向OH\_AVScreenCapture实例的指针。 |
| bool isMicrophone | 麦克风开关参数。  true表示打开麦克风，false表示关闭麦克风。  默认是true。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVSCREEN\_CAPTURE\_ErrCode](capi-native-avscreen-capture-errors-h.md#oh_avscreen_capture_errcode) | AV\_SCREEN\_CAPTURE\_ERR\_OK：执行成功。  AV\_SCREEN\_CAPTURE\_ERR\_INVALID\_VAL：输入参数capture为空指针。  AV\_SCREEN\_CAPTURE\_ERR\_OPERATE\_NOT\_PERMIT：不允许操作，设置麦克风开关失败。 |

### OH\_AVScreenCapture\_SetStateCallback()

PhonePC/2in1TabletTV

```
1. OH_AVSCREEN_CAPTURE_ErrCode OH_AVScreenCapture_SetStateCallback(struct OH_AVScreenCapture *capture, OH_AVScreenCapture_OnStateChange callback, void *userData)
```

**描述**

设置状态变更处理回调方法，在开始录制前调用。

调用该方法设置状态变更处理回调方法，当OH\_AVScreenCapture实例发生状态变更时，该状态变更处理回调方法将会被调用。

调用该设置方法成功后，在启动录屏时将通过隐私弹窗方式征求用户同意：

1. 如果用户同意则开始启动录屏流程，在启动录屏成功后，通过该状态处理回调方法上报[OH\_AVScreenCaptureStateCode](capi-native-avscreen-capture-base-h.md#oh_avscreencapturestatecode).OH\_SCREEN\_CAPTURE\_STATE\_STARTED状态，告知应用启动录屏成功，并在屏幕显示录屏通知。如果启动录屏失败，则通过该状态处理回调方法上报失败状态信息（如，若麦克风不可用则上报[OH\_AVScreenCaptureStateCode](capi-native-avscreen-capture-base-h.md#oh_avscreencapturestatecode).OH\_SCREEN\_CAPTURE\_STATE\_MIC\_UNAVAILABLE状态），或通过错误处理回调方法[OH\_AVScreenCapture\_OnError](capi-native-avscreen-capture-base-h.md#oh_avscreencapture_onerror)上报错误信息。

2. 如果用户拒绝，则终止启动录屏，通过该状态处理回调方法上报[OH\_AVScreenCaptureStateCode](capi-native-avscreen-capture-base-h.md#oh_avscreencapturestatecode).OH\_SCREEN\_CAPTURE\_STATE\_CANCELED状态，告知应用用户拒绝启动录屏，启动录屏失败。

**系统能力：** SystemCapability.Multimedia.Media.AVScreenCapture

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [struct OH\_AVScreenCapture](capi-avscreencapture-oh-avscreencapture.md) \*capture | 指向OH\_AVScreenCapture实例的指针。 |
| [OH\_AVScreenCapture\_OnStateChange](capi-native-avscreen-capture-base-h.md#oh_avscreencapture_onstatechange) callback | 指向状态处理回调方法实例的指针。 |
| void \*userData | 指向应用提供的自定义数据的指针，在状态处理回调方法被调用时作为入参回传。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVSCREEN\_CAPTURE\_ErrCode](capi-native-avscreen-capture-errors-h.md#oh_avscreen_capture_errcode) | AV\_SCREEN\_CAPTURE\_ERR\_OK：执行成功。  AV\_SCREEN\_CAPTURE\_ERR\_INVALID\_VAL：输入参数capture为空指针或输入参数callback为空指针。  AV\_SCREEN\_CAPTURE\_ERR\_NO\_MEMORY：内存不足，内存分配失败。  AV\_SCREEN\_CAPTURE\_ERR\_OPERATE\_NOT\_PERMIT：不允许操作，设置StateCallback失败。 |

### OH\_AVScreenCapture\_SetDataCallback()

PhonePC/2in1TabletTV

```
1. OH_AVSCREEN_CAPTURE_ErrCode OH_AVScreenCapture_SetDataCallback(struct OH_AVScreenCapture *capture, OH_AVScreenCapture_OnBufferAvailable callback, void *userData)
```

**描述**

设置数据处理回调方法，在开始录制前调用。

调用该方法设置数据处理回调方法，当OH\_AVScreenCapture操作期间有音频或视频数据缓存区可用时，将调用该数据处理回调方法。

应用需要在该数据处理回调方法中根据数据类型完成处理麦克风音频、内录音频、视频数据，当该数据处理回调方法返回后数据缓存区将不再有效。

调用该方法成功后：

1. 当OH\_AVScreenCapture操作期间有音视频缓存区可用时，将不再调用通过[OH\_AVScreenCapture\_SetCallback](capi-native-avscreen-capture-h.md#oh_avscreencapture_setcallback)设置的数据回调方法[OH\_AVScreenCaptureOnAudioBufferAvailable](capi-native-avscreen-capture-base-h.md#oh_avscreencaptureonaudiobufferavailable)和[OH\_AVScreenCaptureOnVideoBufferAvailable](capi-native-avscreen-capture-base-h.md#oh_avscreencaptureonvideobufferavailable)。

2. 不允许应用调用如下4个方法[OH\_AVScreenCapture\_AcquireAudioBuffer](capi-native-avscreen-capture-h.md#oh_avscreencapture_acquireaudiobuffer)、[OH\_AVScreenCapture\_ReleaseAudioBuffer](capi-native-avscreen-capture-h.md#oh_avscreencapture_releaseaudiobuffer)、[OH\_AVScreenCapture\_AcquireVideoBuffer](capi-native-avscreen-capture-h.md#oh_avscreencapture_acquirevideobuffer)和[OH\_AVScreenCapture\_ReleaseVideoBuffer](capi-native-avscreen-capture-h.md#oh_avscreencapture_releasevideobuffer)，直接返回失败。

**系统能力：** SystemCapability.Multimedia.Media.AVScreenCapture

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [struct OH\_AVScreenCapture](capi-avscreencapture-oh-avscreencapture.md) \*capture | 指向OH\_AVScreenCapture实例的指针。 |
| [OH\_AVScreenCapture\_OnBufferAvailable](capi-native-avscreen-capture-base-h.md#oh_avscreencapture_onbufferavailable) callback | 指向数据处理回调方法实例的指针。 |
| void \*userData | 指向应用提供的自定义数据的指针，在数据处理回调方法被调用时作为入参回传。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVSCREEN\_CAPTURE\_ErrCode](capi-native-avscreen-capture-errors-h.md#oh_avscreen_capture_errcode) | AV\_SCREEN\_CAPTURE\_ERR\_OK：执行成功。  AV\_SCREEN\_CAPTURE\_ERR\_INVALID\_VAL：输入参数capture为空指针或输入参数callback为空指针。  AV\_SCREEN\_CAPTURE\_ERR\_NO\_MEMORY：内存不足，内存分配失败。  AV\_SCREEN\_CAPTURE\_ERR\_OPERATE\_NOT\_PERMIT：不允许操作，设置DataCallback失败。 |

### OH\_AVScreenCapture\_SetErrorCallback()

PhonePC/2in1TabletTV

```
1. OH_AVSCREEN_CAPTURE_ErrCode OH_AVScreenCapture_SetErrorCallback(struct OH_AVScreenCapture *capture, OH_AVScreenCapture_OnError callback, void *userData)
```

**描述**

设置错误处理回调方法，在开始录制前调用。

调用该方法设置错误处理回调方法，当OH\_AVScreenCapture实例发生错误时，该错误处理回调方法将会被调用。

调用该设置方法成功后，当OH\_AVScreenCapture实例发生错误时，将不再调用通过[OH\_AVScreenCapture\_SetCallback](capi-native-avscreen-capture-h.md#oh_avscreencapture_setcallback)设置的错误处理回调方法[OH\_AVScreenCaptureOnError](capi-native-avscreen-capture-base-h.md#oh_avscreencaptureonerror)。

**系统能力：** SystemCapability.Multimedia.Media.AVScreenCapture

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [struct OH\_AVScreenCapture](capi-avscreencapture-oh-avscreencapture.md) \*capture | 指向OH\_AVScreenCapture实例的指针。 |
| [OH\_AVScreenCapture\_OnError](capi-native-avscreen-capture-base-h.md#oh_avscreencapture_onerror) callback | 指向错误处理回调方法实例的指针。 |
| void \*userData | 指向应用提供的自定义数据的指针，在错误处理回调方法被调用时作为入参回传。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVSCREEN\_CAPTURE\_ErrCode](capi-native-avscreen-capture-errors-h.md#oh_avscreen_capture_errcode) | AV\_SCREEN\_CAPTURE\_ERR\_OK：执行成功。  AV\_SCREEN\_CAPTURE\_ERR\_INVALID\_VAL：输入参数capture为空指针或输入参数callback为空指针。  AV\_SCREEN\_CAPTURE\_ERR\_NO\_MEMORY：内存不足，内存分配失败。  AV\_SCREEN\_CAPTURE\_ERR\_OPERATE\_NOT\_PERMIT：不允许操作，设置ErrorCallback失败。 |

### OH\_AVScreenCapture\_StartScreenCaptureWithSurface()

PhonePC/2in1TabletTV

```
1. OH_AVSCREEN_CAPTURE_ErrCode OH_AVScreenCapture_StartScreenCaptureWithSurface(struct OH_AVScreenCapture *capture, OHNativeWindow *window)
```

**描述**

使用Surface模式录屏。

**系统能力：** SystemCapability.Multimedia.Media.AVScreenCapture

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [struct OH\_AVScreenCapture](capi-avscreencapture-oh-avscreencapture.md) \*capture | 指向OH\_AVScreenCapture实例的指针。 |
| [OHNativeWindow](capi-nativewindow-nativewindow.md) \*window | 指向OHNativeWindow实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVSCREEN\_CAPTURE\_ErrCode](capi-native-avscreen-capture-errors-h.md#oh_avscreen_capture_errcode) | AV\_SCREEN\_CAPTURE\_ERR\_OK：执行成功。  AV\_SCREEN\_CAPTURE\_ERR\_INVALID\_VAL：输入参数capture为空指针或输入参数window为空指针或window指向的windowSurface为空指针。  AV\_SCREEN\_CAPTURE\_ERR\_UNSUPPORT（API version 20新增）：设备不支持该操作。  AV\_SCREEN\_CAPTURE\_ERR\_OPERATE\_NOT\_PERMIT：不允许操作，设置隐私权限启用失败或启动ScreenCaptureWithSurface失败。 |

### OH\_AVScreenCapture\_SetCanvasRotation()

PhonePC/2in1TabletTV

```
1. OH_AVSCREEN_CAPTURE_ErrCode OH_AVScreenCapture_SetCanvasRotation(struct OH_AVScreenCapture *capture, bool canvasRotation)
```

**描述**

设置录屏屏幕数据旋转。

调用该方法可以设置录屏屏幕数据是否旋转，当canvasRotation为true时，打开录屏屏幕数据旋转功能，录制的屏幕数据保持正向。

默认为false。

说明

从API version 20开始，支持折叠PC/2in1设备。

**系统能力：** SystemCapability.Multimedia.Media.AVScreenCapture

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [struct OH\_AVScreenCapture](capi-avscreencapture-oh-avscreencapture.md) \*capture | 指向OH\_AVScreenCapture实例的指针。 |
| bool canvasRotation | 指示屏幕数据旋转参数。  true表示打开录屏屏幕数据旋转功能，录制的屏幕数据保持正向，false表示关闭录屏屏幕数据旋转功能，录制的屏幕数据跟随屏幕旋转。  默认是false。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVSCREEN\_CAPTURE\_ErrCode](capi-native-avscreen-capture-errors-h.md#oh_avscreen_capture_errcode) | AV\_SCREEN\_CAPTURE\_ERR\_OK：执行成功。  AV\_SCREEN\_CAPTURE\_ERR\_INVALID\_VAL：输入参数capture为空指针。  AV\_SCREEN\_CAPTURE\_ERR\_UNSUPPORT（API version 20新增）：设备不支持该操作。  AV\_SCREEN\_CAPTURE\_ERR\_OPERATE\_NOT\_PERMIT：不允许操作，设置录屏屏幕数据旋转失败。 |

### OH\_AVScreenCapture\_CreateContentFilter()

PhonePC/2in1TabletTV

```
1. struct OH_AVScreenCapture_ContentFilter *OH_AVScreenCapture_CreateContentFilter(void)
```

**描述**

创建ContentFilter。

**系统能力：** SystemCapability.Multimedia.Media.AVScreenCapture

**起始版本：** 12

**返回：**

| 类型 | 说明 |
| --- | --- |
| struct [OH\_AVScreenCapture\_ContentFilter](i-avscreencapture-oh-avscreencapture-contentfilter.md) \* | 执行成功返回OH\_AVScreenCapture\_ContentFilter实例，否则返回空指针。 |

### OH\_AVScreenCapture\_ReleaseContentFilter()

PhonePC/2in1TabletTV

```
1. OH_AVSCREEN_CAPTURE_ErrCode OH_AVScreenCapture_ReleaseContentFilter(struct OH_AVScreenCapture_ContentFilter *filter)
```

**描述**

释放ContentFilter。

**系统能力：** SystemCapability.Multimedia.Media.AVScreenCapture

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [struct OH\_AVScreenCapture\_ContentFilter](i-avscreencapture-oh-avscreencapture-contentfilter.md) \*filter | 指向OH\_AVScreenCapture\_ContentFilter实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVSCREEN\_CAPTURE\_ErrCode](capi-native-avscreen-capture-errors-h.md#oh_avscreen_capture_errcode) | AV\_SCREEN\_CAPTURE\_ERR\_OK：执行成功。  AV\_SCREEN\_CAPTURE\_ERR\_INVALID\_VAL：输入参数filter为空指针。 |

### OH\_AVScreenCapture\_ContentFilter\_AddAudioContent()

PhonePC/2in1TabletTV

```
1. OH_AVSCREEN_CAPTURE_ErrCode OH_AVScreenCapture_ContentFilter_AddAudioContent(struct OH_AVScreenCapture_ContentFilter *filter, OH_AVScreenCaptureFilterableAudioContent content)
```

**描述**

向ContentFilter实例添加可过滤的声音类型。

**系统能力：** SystemCapability.Multimedia.Media.AVScreenCapture

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [struct OH\_AVScreenCapture\_ContentFilter](i-avscreencapture-oh-avscreencapture-contentfilter.md) \*filter | 指向OH\_AVScreenCapture\_ContentFilter实例的指针。 |
| [OH\_AVScreenCaptureFilterableAudioContent](capi-native-avscreen-capture-base-h.md#oh_avscreencapturefilterableaudiocontent) content | OH\_AVScreenCaptureFilterableAudioContent实例。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVSCREEN\_CAPTURE\_ErrCode](capi-native-avscreen-capture-errors-h.md#oh_avscreen_capture_errcode) | AV\_SCREEN\_CAPTURE\_ERR\_OK：执行成功。  AV\_SCREEN\_CAPTURE\_ERR\_INVALID\_VAL：输入参数filter为空指针或输入参数content无效。 |

### OH\_AVScreenCapture\_ExcludeContent()

PhonePC/2in1TabletTV

```
1. OH_AVSCREEN_CAPTURE_ErrCode OH_AVScreenCapture_ExcludeContent(struct OH_AVScreenCapture *capture, struct OH_AVScreenCapture_ContentFilter *filter)
```

**描述**

设置OH\_AVScreenCapture实例的内容过滤器ContentFilter。

**系统能力：** SystemCapability.Multimedia.Media.AVScreenCapture

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [struct OH\_AVScreenCapture](capi-avscreencapture-oh-avscreencapture.md) \*capture | 指向OH\_AVScreenCapture实例的指针。 |
| [struct OH\_AVScreenCapture\_ContentFilter](i-avscreencapture-oh-avscreencapture-contentfilter.md) \*filter | 指向OH\_AVScreenCapture\_ContentFilter实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVSCREEN\_CAPTURE\_ErrCode](capi-native-avscreen-capture-errors-h.md#oh_avscreen_capture_errcode) | AV\_SCREEN\_CAPTURE\_ERR\_OK：执行成功。  AV\_SCREEN\_CAPTURE\_ERR\_INVALID\_VAL：输入参数capture为空指针或输入参数filter为空指针。  AV\_SCREEN\_CAPTURE\_ERR\_UNSUPPORT：操作不支持。对于流，启动时应该调用AudioCapturer接口。  对于capture文件，启动时调用Recorder接口。 |

### OH\_AVScreenCapture\_ContentFilter\_AddWindowContent()

PhonePC/2in1TabletTV

```
1. OH_AVSCREEN_CAPTURE_ErrCode OH_AVScreenCapture_ContentFilter_AddWindowContent(struct OH_AVScreenCapture_ContentFilter *filter, int32_t *windowIDs, int32_t windowCount)
```

**描述**

向ContentFilter实例添加可被过滤的窗口ID列表。

**系统能力：** SystemCapability.Multimedia.Media.AVScreenCapture

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [struct OH\_AVScreenCapture\_ContentFilter](i-avscreencapture-oh-avscreencapture-contentfilter.md) \*filter | 指向OH\_AVScreenCapture\_ContentFilter实例的指针。 |
| int32\_t \*windowIDs | 指向窗口ID的指针。 |
| int32\_t windowCount | 窗口ID列表的长度。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVSCREEN\_CAPTURE\_ErrCode](capi-native-avscreen-capture-errors-h.md#oh_avscreen_capture_errcode) | 执行成功返回AV\_SCREEN\_CAPTURE\_ERR\_OK，否则返回具体错误码。 |

### OH\_AVScreenCapture\_ResizeCanvas()

PhonePC/2in1TabletTV

```
1. OH_AVSCREEN_CAPTURE_ErrCode OH_AVScreenCapture_ResizeCanvas(struct OH_AVScreenCapture *capture, int32_t width, int32_t height)
```

**描述**

调整屏幕的分辨率。

调用该方法可以设置录屏屏幕数据的分辨率，width为屏幕的宽度，height为屏幕的高度。

该接口目前仅支持录屏取码流的场景，不支持录屏存文件的场景。并且调用该接口的调用者以及视频数据的消费者需要确保自身能够支持收到的视频数据分辨率发生变化。

**系统能力：** SystemCapability.Multimedia.Media.AVScreenCapture

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [struct OH\_AVScreenCapture](capi-avscreencapture-oh-avscreencapture.md) \*capture | 指向OH\_AVScreenCapture实例的指针。 |
| int32\_t width | 录屏屏幕的宽度。 |
| int32\_t height | 录屏屏幕的高度。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVSCREEN\_CAPTURE\_ErrCode](capi-native-avscreen-capture-errors-h.md#oh_avscreen_capture_errcode) | AV\_SCREEN\_CAPTURE\_ERR\_OK：执行成功。  AV\_SCREEN\_CAPTURE\_ERR\_INVALID\_VAL：输入参数capture为空指针。  AV\_SCREEN\_CAPTURE\_ERR\_UNSUPPORT（API version 20新增）：设备不支持该操作。  AV\_SCREEN\_CAPTURE\_ERR\_OPERATE\_NOT\_PERMIT：不允许操作。 |

### OH\_AVScreenCapture\_SkipPrivacyMode()

PhonePC/2in1TabletTV

```
1. OH_AVSCREEN_CAPTURE_ErrCode OH_AVScreenCapture_SkipPrivacyMode(struct OH_AVScreenCapture *capture, int32_t *windowIDs, int32_t windowCount)
```

**描述**

录屏时豁免隐私窗口。

调用该方法可以豁免隐私窗口，windowIDs为需要豁免的隐私窗口ID指针，windowCount 为隐私窗口ID列表的长度，目前豁免需要传入所有隐私子窗口和主窗口ID。

**系统能力：** SystemCapability.Multimedia.Media.AVScreenCapture

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [struct OH\_AVScreenCapture](capi-avscreencapture-oh-avscreencapture.md) \*capture | 指向OH\_AVScreenCapture实例的指针。 |
| int32\_t \*windowIDs | 向隐私窗口ID的指针。 |
| int32\_t windowCount | 隐私窗口ID列表的长度。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVSCREEN\_CAPTURE\_ErrCode](capi-native-avscreen-capture-errors-h.md#oh_avscreen_capture_errcode) | AV\_SCREEN\_CAPTURE\_ERR\_OK：执行成功。  AV\_SCREEN\_CAPTURE\_ERR\_INVALID\_VAL：输入参数capture为空指针。  AV\_SCREEN\_CAPTURE\_ERR\_UNSUPPORT（API version 20新增）：设备不支持该操作。  AV\_SCREEN\_CAPTURE\_ERR\_OPERATE\_NOT\_PERMIT：不允许操作。 |

### OH\_AVScreenCapture\_SetMaxVideoFrameRate()

PhonePC/2in1TabletTV

```
1. OH_AVSCREEN_CAPTURE_ErrCode OH_AVScreenCapture_SetMaxVideoFrameRate(struct OH_AVScreenCapture *capture, int32_t frameRate)
```

**描述**

设置录屏时的最大帧率。

该接口应在录屏启动之后被调用。

调用该方法可以设置录屏时的最大帧率，frameRate为想要设置的最大帧率。

该接口设置最大帧率时，实际设置的帧率受限设备的能力，由底层的系统能力决定。

调用该接口设置录屏最大帧率时，实际帧率将受限于设备能力。目前接口入参的最大值不设限制，但当前支持的最高帧率为60FPS，当入参设置超过60FPS，将以60FPS处理。不超过上限时，则按照实际入参值处理。

**系统能力：** SystemCapability.Multimedia.Media.AVScreenCapture

**起始版本：** 14

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [struct OH\_AVScreenCapture](capi-avscreencapture-oh-avscreencapture.md) \*capture | 指向OH\_AVScreenCapture实例的指针。 |
| int32\_t frameRate | 录屏的最大帧率。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVSCREEN\_CAPTURE\_ErrCode](capi-native-avscreen-capture-errors-h.md#oh_avscreen_capture_errcode) | AV\_SCREEN\_CAPTURE\_ERR\_OK：执行成功。  AV\_SCREEN\_CAPTURE\_ERR\_INVALID\_VAL：输入参数capture为空指针或者输入参数frameRate不支持。  AV\_SCREEN\_CAPTURE\_ERR\_UNSUPPORT（API version 20新增）：设备不支持该操作。  AV\_SCREEN\_CAPTURE\_ERR\_OPERATE\_NOT\_PERMIT：不允许操作。 |

### OH\_AVScreenCapture\_ShowCursor()

PhonePC/2in1TabletTV

```
1. OH_AVSCREEN_CAPTURE_ErrCode OH_AVScreenCapture_ShowCursor(struct OH_AVScreenCapture *capture, bool showCursor)
```

**描述**

设置光标显示开关。

**系统能力：** SystemCapability.Multimedia.Media.AVScreenCapture

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [struct OH\_AVScreenCapture](capi-avscreencapture-oh-avscreencapture.md) \*capture | 指向OH\_AVScreenCapture实例的指针。 |
| bool showCursor | 光标显示参数。  true表示显示光标，false表示隐藏光标。  默认是true。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVSCREEN\_CAPTURE\_ErrCode](capi-native-avscreen-capture-errors-h.md#oh_avscreen_capture_errcode) | AV\_SCREEN\_CAPTURE\_ERR\_OK：执行成功。  AV\_SCREEN\_CAPTURE\_ERR\_INVALID\_VAL：输入参数capture为空指针。  AV\_SCREEN\_CAPTURE\_ERR\_UNSUPPORT（API version 20新增）：设备不支持该操作。  AV\_SCREEN\_CAPTURE\_ERR\_OPERATE\_NOT\_PERMIT：不允许操作，设置光标失败。 |

### OH\_AVScreenCapture\_SetDisplayCallback()

PhonePC/2in1TabletTV

```
1. OH_AVSCREEN_CAPTURE_ErrCode OH_AVScreenCapture_SetDisplayCallback(struct OH_AVScreenCapture *capture, OH_AVScreenCapture_OnDisplaySelected callback, void *userData)
```

**描述**

设置获取录屏屏幕Id的回调。

**系统能力：** SystemCapability.Multimedia.Media.AVScreenCapture

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [struct OH\_AVScreenCapture](capi-avscreencapture-oh-avscreencapture.md) \*capture | 指向OH\_AVScreenCapture实例的指针。 |
| [OH\_AVScreenCapture\_OnDisplaySelected](capi-native-avscreen-capture-base-h.md#oh_avscreencapture_ondisplayselected) callback | 指向录屏屏幕Id回调方法实例的指针。 |
| void \*userData | 指向应用提供的自定义数据的指针，在状态处理回调方法被调用时作为入参回传。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVSCREEN\_CAPTURE\_ErrCode](capi-native-avscreen-capture-errors-h.md#oh_avscreen_capture_errcode) | AV\_SCREEN\_CAPTURE\_ERR\_OK：执行成功。  AV\_SCREEN\_CAPTURE\_ERR\_INVALID\_VAL：输入参数capture为空指针或输入参数callback为空指针。  AV\_SCREEN\_CAPTURE\_ERR\_NO\_MEMORY：内存不足，内存分配失败。  AV\_SCREEN\_CAPTURE\_ERR\_INVALID\_STATE：回调必须在start方法前调用。 |

### OH\_AVScreenCapture\_CreateCaptureStrategy()

PhonePC/2in1TabletTV

```
1. OH_AVScreenCapture_CaptureStrategy* OH_AVScreenCapture_CreateCaptureStrategy(void)
```

**描述**

创建录屏策略对象。

**系统能力：** SystemCapability.Multimedia.Media.AVScreenCapture

**起始版本：** 20

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVScreenCapture\_CaptureStrategy](avscreencapture-oh-avscreencapture-capturestrategy.md)\* | 执行成功返回OH\_AVScreenCapture\_CaptureStrategy实例，否则返回空指针。 |

### OH\_AVScreenCapture\_ReleaseCaptureStrategy()

PhonePC/2in1TabletTV

```
1. OH_AVSCREEN_CAPTURE_ErrCode OH_AVScreenCapture_ReleaseCaptureStrategy(OH_AVScreenCapture_CaptureStrategy* strategy)
```

**描述**

释放录屏策略对象。

**系统能力：** SystemCapability.Multimedia.Media.AVScreenCapture

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVScreenCapture\_CaptureStrategy](avscreencapture-oh-avscreencapture-capturestrategy.md)\* strategy | 指向录屏策略对象的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVSCREEN\_CAPTURE\_ErrCode](capi-native-avscreen-capture-errors-h.md#oh_avscreen_capture_errcode) | AV\_SCREEN\_CAPTURE\_ERR\_OK：执行成功。  AV\_SCREEN\_CAPTURE\_ERR\_INVALID\_VAL：输入参数strategy为空指针。 |

### OH\_AVScreenCapture\_SetCaptureStrategy()

PhonePC/2in1TabletTV

```
1. OH_AVSCREEN_CAPTURE_ErrCode OH_AVScreenCapture_SetCaptureStrategy(struct OH_AVScreenCapture *capture, OH_AVScreenCapture_CaptureStrategy *strategy)
```

**描述**

给指定的OH\_AVScreenCapture实例设置捕获策略。

该接口应在录屏启动之前被调用。

**系统能力：** SystemCapability.Multimedia.Media.AVScreenCapture

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [struct OH\_AVScreenCapture](capi-avscreencapture-oh-avscreencapture.md) \*capture | 指向OH\_AVScreenCapture实例的指针。 |
| [OH\_AVScreenCapture\_CaptureStrategy](avscreencapture-oh-avscreencapture-capturestrategy.md) \*strategy | 指向捕获策略对象的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVSCREEN\_CAPTURE\_ErrCode](capi-native-avscreen-capture-errors-h.md#oh_avscreen_capture_errcode) | AV\_SCREEN\_CAPTURE\_ERR\_OK：执行成功。  AV\_SCREEN\_CAPTURE\_ERR\_INVALID\_VAL：输入参数capture或strategy为空指针。  AV\_SCREEN\_CAPTURE\_ERR\_INVALID\_STATE：在录屏启动之后调用该接口。 |

### OH\_AVScreenCapture\_StrategyForCanvasFollowRotation()

PhonePC/2in1TabletTV

```
1. OH_AVSCREEN_CAPTURE_ErrCode OH_AVScreenCapture_StrategyForCanvasFollowRotation(OH_AVScreenCapture_CaptureStrategy *strategy, bool value)
```

**描述**

设置屏幕录屏自动跟随旋转配置。设为true，表示跟随屏幕旋转，并在横竖屏旋转后，自动调换虚拟屏尺寸，确保输出画面及时跟随旋转。

设置是否自动跟随旋转配置后，在旋转通知后，无需再手动调用[OH\_AVScreenCapture\_ResizeCanvas](capi-native-avscreen-capture-h.md#oh_avscreencapture_resizecanvas)接口。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVScreenCapture\_CaptureStrategy](avscreencapture-oh-avscreencapture-capturestrategy.md) \*strategy | 指向OH\_AVScreenCapture\_CaptureStrategy实例的指针。 |
| bool value | 虚拟屏的宽和高是否跟随屏幕旋转而旋转。  true表示虚拟屏的宽和高随着屏幕的旋转而旋转，false表示虚拟屏的宽和高保持初始设定。  默认是false。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVSCREEN\_CAPTURE\_ErrCode](capi-native-avscreen-capture-errors-h.md#oh_avscreen_capture_errcode) | AV\_SCREEN\_CAPTURE\_ERR\_OK：执行成功。  AV\_SCREEN\_CAPTURE\_ERR\_INVALID\_VAL：输入参数strategy为空指针。 |

### OH\_AVScreenCapture\_StrategyForKeepCaptureDuringCall()

PhonePC/2in1TabletTV

```
1. OH_AVSCREEN_CAPTURE_ErrCode OH_AVScreenCapture_StrategyForKeepCaptureDuringCall(OH_AVScreenCapture_CaptureStrategy *strategy, bool value)
```

**描述**

向CaptureStrategy实例设置蜂窝通话时是否保持录屏。

value设置为true时并且录屏时接听蜂窝通话的过程中，出于隐私要求，双方通话的声音（本地麦克风和对方说话声音）不会被录制，其他系统音录制正常。电话挂断之后，录屏框架恢复麦克风录制。注意，如果挂断电话时录屏应用在后台运行，麦克风录制会启动失败，原因是音频模块不允许后台应用启动麦克风录制。

**系统能力：** SystemCapability.Multimedia.Media.AVScreenCapture

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVScreenCapture\_CaptureStrategy](avscreencapture-oh-avscreencapture-capturestrategy.md) \*strategy | 指向OH\_AVScreenCapture\_CaptureStrategy对象的指针。 |
| bool value | 蜂窝通话时是否可以进行屏幕录制。  true表示蜂窝通话时可以录屏，false表示蜂窝通话时不允许录屏。  默认是false。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVSCREEN\_CAPTURE\_ErrCode](capi-native-avscreen-capture-errors-h.md#oh_avscreen_capture_errcode) | AV\_SCREEN\_CAPTURE\_ERR\_OK：执行成功。  AV\_SCREEN\_CAPTURE\_ERR\_INVALID\_VAL：输入参数strategy为空指针。 |

### OH\_AVScreenCapture\_SetCaptureContentChangedCallback()

PhonePC/2in1TabletTV

```
1. OH_AVSCREEN_CAPTURE_ErrCode OH_AVScreenCapture_SetCaptureContentChangedCallback(struct OH_AVScreenCapture *capture, OH_AVScreenCapture_OnCaptureContentChanged callback, void *userData)
```

**描述**

设置录屏内容变更回调事件，需在录屏启动前被调用。

**系统能力：** SystemCapability.Multimedia.Media.AVScreenCapture

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [struct OH\_AVScreenCapture](capi-avscreencapture-oh-avscreencapture.md) \*capture | 指向OH\_AVScreenCapture实例的指针。 |
| [OH\_AVScreenCapture\_OnCaptureContentChanged](capi-native-avscreen-capture-base-h.md#oh_avscreencapture_oncapturecontentchanged) callback | 指向录屏内容变更回调方法实例的指针。 |
| void \*userData | 指向应用提供的自定义数据的指针，在错误处理回调方法被调用时作为入参回传。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVSCREEN\_CAPTURE\_ErrCode](capi-native-avscreen-capture-errors-h.md#oh_avscreen_capture_errcode) | AV\_SCREEN\_CAPTURE\_ERR\_OK：操作成功。  AV\_SCREEN\_CAPTURE\_ERR\_INVALID\_VAL：参数无效，输入参数capture或callback为空指针。  AV\_SCREEN\_CAPTURE\_ERR\_OPERATE\_NOT\_PERMIT：不允许操作，设置录屏内容回调失败。 |

### OH\_AVScreenCapture\_SetCaptureArea()

PhonePC/2in1TabletTV

```
1. OH_AVSCREEN_CAPTURE_ErrCode OH_AVScreenCapture_SetCaptureArea(struct OH_AVScreenCapture *capture, uint64_t displayId, OH_Rect* area)
```

**描述**

设置或更新捕获区域。

接口在开始录屏前后都可以设置，设置的坐标和宽高不能为负数，捕获区域不能跨屏幕，区域位置设置失败后仍按照上一次的区域进行捕获。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [struct OH\_AVScreenCapture](capi-avscreencapture-oh-avscreencapture.md) \*capture | 指向OH\_AVScreenCapture的指针。 |
| uint64\_t displayId | 需要执行屏幕捕获的屏幕ID。 |
| [OH\_Rect](capi-avscreencapture-oh-rect.md)\* area | 指定捕获的区域。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVSCREEN\_CAPTURE\_ErrCode](capi-native-avscreen-capture-errors-h.md#oh_avscreen_capture_errcode) | AV\_SCREEN\_CAPTURE\_ERR\_OK：执行成功。  AV\_SCREEN\_CAPTURE\_ERR\_INVALID\_VAL：输入参数capture为空指针、输入displayId不存在或输入的捕获区域异常。 |

### OH\_AVScreenCapture\_StrategyForPrivacyMaskMode()

PhonePC/2in1TabletTV

```
1. OH_AVSCREEN_CAPTURE_ErrCode OH_AVScreenCapture_StrategyForPrivacyMaskMode(OH_AVScreenCapture_CaptureStrategy *strategy, int32_t value)
```

**描述**

设置隐私窗口屏蔽模式。

**系统能力：** SystemCapability.Multimedia.Media.AVScreenCapture

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVScreenCapture\_CaptureStrategy](avscreencapture-oh-avscreencapture-capturestrategy.md) \*strategy | 指向OH\_AVScreenCapture\_CaptureStrategy实例的指针。 |
| int32\_t value | 设置为0，表示存在隐私窗口时，采用全屏屏蔽模式。  设置为1，表示存在隐私窗口时，采用隐私窗口屏蔽模式，设置为其他值时返回错误。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVSCREEN\_CAPTURE\_ErrCode](capi-native-avscreen-capture-errors-h.md#oh_avscreen_capture_errcode) | AV\_SCREEN\_CAPTURE\_ERR\_OK：执行成功。  AV\_SCREEN\_CAPTURE\_ERR\_INVALID\_VAL：输入参数strategy为空指针或输入value为无效值。 |

### OH\_AVScreenCapture\_SetSelectionCallback()

PhonePC/2in1TabletTV

```
1. OH_AVSCREEN_CAPTURE_ErrCode OH_AVScreenCapture_SetSelectionCallback(struct OH_AVScreenCapture *capture, OH_AVScreenCapture_OnUserSelected callback, void *userData)
```

**描述**

注册手工确认界面用户选择结果的回调，需在录屏启动前被调用。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [struct OH\_AVScreenCapture](capi-avscreencapture-oh-avscreencapture.md) \*capture | 需要注册该回调的屏幕捕获对象。 |
| [OH\_AVScreenCapture\_OnUserSelected](capi-native-avscreen-capture-base-h.md#oh_avscreencapture_onuserselected) callback | 用户在界面确认后，通过该函数通知应用进行逻辑处理。 |
| void \*userData | 应用传入的控制块指针，在返回时携带给应用。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVSCREEN\_CAPTURE\_ErrCode](capi-native-avscreen-capture-errors-h.md#oh_avscreen_capture_errcode) | AV\_SCREEN\_CAPTURE\_ERR\_OK：执行成功。  AV\_SCREEN\_CAPTURE\_ERR\_INVALID\_VAL：输入参数capture为空指针。 |

### OH\_AVScreenCapture\_GetCaptureTypeSelected()

PhonePC/2in1TabletTV

```
1. OH_AVSCREEN_CAPTURE_ErrCode OH_AVScreenCapture_GetCaptureTypeSelected(OH_AVScreenCapture_UserSelectionInfo *selection, int32_t* type)
```

**描述**

获取用户在确认界面选择的屏幕捕获对象类型。在[OH\_AVScreenCapture\_OnUserSelected](capi-native-avscreen-capture-base-h.md#oh_avscreencapture_onuserselected)回调中使用，selection指针在回调结束后销毁。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVScreenCapture\_UserSelectionInfo](screencapture-oh-avscreencapture-userselectioninfo.md) \*selection | 指向OH\_AVScreenCapture\_UserSelectionInfo实例的指针。 |
| int32\_t\* type | 用户选择的捕获对象类型，0：代表屏幕，1：代表窗口。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVSCREEN\_CAPTURE\_ErrCode](capi-native-avscreen-capture-errors-h.md#oh_avscreen_capture_errcode) | AV\_SCREEN\_CAPTURE\_ERR\_OK：执行成功。  AV\_SCREEN\_CAPTURE\_ERR\_INVALID\_VAL：输入参数selection为空指针。 |

### OH\_AVScreenCapture\_GetDisplayIdSelected()

PhonePC/2in1TabletTV

```
1. OH_AVSCREEN_CAPTURE_ErrCode OH_AVScreenCapture_GetDisplayIdSelected(OH_AVScreenCapture_UserSelectionInfo *selection, uint64_t* displayId)
```

**描述**

获取确认页面，用户选择录制的屏幕ID。在[OH\_AVScreenCapture\_OnUserSelected](capi-native-avscreen-capture-base-h.md#oh_avscreencapture_onuserselected)回调中使用，selection指针在回调结束后销毁。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVScreenCapture\_UserSelectionInfo](screencapture-oh-avscreencapture-userselectioninfo.md) \*selection | 指向OH\_AVScreenCapture\_UserSelectionInfo实例的指针。 |
| uint64\_t\* displayId | 返回用户选择的屏幕ID。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVSCREEN\_CAPTURE\_ErrCode](capi-native-avscreen-capture-errors-h.md#oh_avscreen_capture_errcode) | AV\_SCREEN\_CAPTURE\_ERR\_OK：执行成功。  AV\_SCREEN\_CAPTURE\_ERR\_INVALID\_VAL：输入参数selection为空指针。 |

### OH\_AVScreenCapture\_StrategyForBFramesEncoding()

PhonePC/2in1TabletTV

```
1. OH_AVSCREEN_CAPTURE_ErrCode OH_AVScreenCapture_StrategyForBFramesEncoding(OH_AVScreenCapture_CaptureStrategy *strategy, bool value)
```

**描述**

向CaptureStrategy实例设置是否使能B帧编码，用于减小录制文件的大小。

B帧视频编码相关的约束和限制可以参考文档[B帧视频编码约束和限制](../harmonyos-guides/video-encoding-b-frame.md#约束和限制)。如果当前不符合B帧视频编码的约束和限制，则正常录制不含B帧的视频，不会返回错误。

**系统能力：** SystemCapability.Multimedia.Media.AVScreenCapture

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVScreenCapture\_CaptureStrategy](avscreencapture-oh-avscreencapture-capturestrategy.md) \*strategy | 指向OH\_AVScreenCapture\_CaptureStrategy对象的指针。 |
| bool value | 录屏文件是否使能B帧编码。  true表示录屏文件使能B帧编码，false表示录屏文件禁用B帧编码。  默认是false。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVSCREEN\_CAPTURE\_ErrCode](capi-native-avscreen-capture-errors-h.md#oh_avscreen_capture_errcode) | AV\_SCREEN\_CAPTURE\_ERR\_OK：执行成功。  AV\_SCREEN\_CAPTURE\_ERR\_INVALID\_VAL：输入参数strategy为空指针。 |

### OH\_AVScreenCapture\_StrategyForPickerPopUp()

PhonePC/2in1TabletTV

```
1. OH_AVSCREEN_CAPTURE_ErrCode OH_AVScreenCapture_StrategyForPickerPopUp(OH_AVScreenCapture_CaptureStrategy *strategy, bool value)
```

**描述**

设置是否弹出屏幕捕获Picker。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVScreenCapture\_CaptureStrategy](avscreencapture-oh-avscreencapture-capturestrategy.md) \*strategy | 指向OH\_AVScreenCapture\_CaptureStrategy对象的指针。 |
| bool value | 设置为false，代表APP已经指定了录屏内容，录屏启动后无需弹出Picker；设置为true代表录屏启动后统一弹出Picker；不设置，代表使用系统推荐行为。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVSCREEN\_CAPTURE\_ErrCode](capi-native-avscreen-capture-errors-h.md#oh_avscreen_capture_errcode) | AV\_SCREEN\_CAPTURE\_ERR\_OK：执行成功。  AV\_SCREEN\_CAPTURE\_ERR\_INVALID\_VAL：输入参数strategy为空指针或输入value为无效值。 |

### OH\_AVScreenCapture\_StrategyForFillMode()

PhonePC/2in1TabletTV

```
1. OH_AVSCREEN_CAPTURE_ErrCode OH_AVScreenCapture_StrategyForFillMode(OH_AVScreenCapture_CaptureStrategy *strategy, OH_AVScreenCapture_FillMode mode)
```

**描述**

设置捕获图像在目标区域的填充模式。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVScreenCapture\_CaptureStrategy](avscreencapture-oh-avscreencapture-capturestrategy.md) \*strategy | 指向OH\_AVScreenCapture\_CaptureStrategy对象的指针。 |
| [OH\_AVScreenCapture\_FillMode](capi-native-avscreen-capture-base-h.md#oh_avscreencapture_fillmode) mode | 捕获图像在输出图像上的填充模式。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVSCREEN\_CAPTURE\_ErrCode](capi-native-avscreen-capture-errors-h.md#oh_avscreen_capture_errcode) | AV\_SCREEN\_CAPTURE\_ERR\_OK：执行成功。  AV\_SCREEN\_CAPTURE\_ERR\_INVALID\_VAL：输入参数strategy为空指针。 |

### OH\_AVScreenCapture\_PresentPicker()

PhonePC/2in1TabletTV

```
1. OH_AVSCREEN_CAPTURE_ErrCode OH_AVScreenCapture_PresentPicker(struct OH_AVScreenCapture *capture)
```

**描述**

录屏开始后，调用该接口再次弹出picker，可动态更新录制源（窗口、屏幕）。更新录制源过程中，原录制流程不中断。

通过picker动态更新录制源后，可以按照新的录制源进行录制。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [struct OH\_AVScreenCapture](capi-avscreencapture-oh-avscreencapture.md) \*capture | 指向OH\_AVScreenCapture实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVSCREEN\_CAPTURE\_ErrCode](capi-native-avscreen-capture-errors-h.md#oh_avscreen_capture_errcode) | AV\_SCREEN\_CAPTURE\_ERR\_OK：执行成功。  AV\_SCREEN\_CAPTURE\_ERR\_INVALID\_VAL：输入参数capture为空指针。  AV\_SCREEN\_CAPTURE\_ERR\_OPERATE\_NOT\_PERMIT：不允许操作。 |

### OH\_AVScreenCapture\_SetCaptureAreaHighlight()

PhonePC/2in1TabletTV

```
1. OH_AVSCREEN_CAPTURE_ErrCode OH_AVScreenCapture_SetCaptureAreaHighlight(struct OH_AVScreenCapture *capture, OH_AVScreenCaptureHighlightConfig config)
```

**描述**

设置屏幕捕获区域高亮模式。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [struct OH\_AVScreenCapture](capi-avscreencapture-oh-avscreencapture.md) \*capture | 指向OH\_AVScreenCapture实例的指针。 |
| [OH\_AVScreenCaptureHighlightConfig](-avscreencapture-oh-avscreencapturehighlightconfig.md) config | 设置本次屏幕捕获的高亮参数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVSCREEN\_CAPTURE\_ErrCode](capi-native-avscreen-capture-errors-h.md#oh_avscreen_capture_errcode) | AV\_SCREEN\_CAPTURE\_ERR\_OK：执行成功。  AV\_SCREEN\_CAPTURE\_ERR\_INVALID\_VAL：输入参数capture为空指针或者config参数值无效。 |

### OH\_AVScreenCapture\_SetPickerMode()

PhonePC/2in1TabletTV

```
1. OH_AVSCREEN_CAPTURE_ErrCode OH_AVScreenCapture_SetPickerMode(struct OH_AVScreenCapture *capture, OH_CapturePickerMode pickerMode)
```

**描述**

设置Picker显示模式。定义picker中显示的内容类型，模式更改会在下一次调用[OH\_AVScreenCapture\_PresentPicker](capi-native-avscreen-capture-h.md#oh_avscreencapture_presentpicker) 函数时生效。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [struct OH\_AVScreenCapture](capi-avscreencapture-oh-avscreencapture.md) \*capture | 指向OH\_AVScreenCapture实例的指针。 |
| [OH\_CapturePickerMode](capi-native-avscreen-capture-base-h.md#oh_capturepickermode) pickerMode | Picker显示模式（请参阅OH\_CapturePickerMode枚举）。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVSCREEN\_CAPTURE\_ErrCode](capi-native-avscreen-capture-errors-h.md#oh_avscreen_capture_errcode) | AV\_SCREEN\_CAPTURE\_ERR\_OK：执行成功。  AV\_SCREEN\_CAPTURE\_ERR\_INVALID\_VAL：输入参数capture为空指针或者pickerMode参数值无效。  AV\_SCREEN\_CAPTURE\_ERR\_OPERATE\_NOT\_PERMIT：不允许操作。 |

### OH\_AVScreenCapture\_ExcludePickerWindows()

PhonePC/2in1TabletTV

```
1. OH_AVSCREEN_CAPTURE_ErrCode OH_AVScreenCapture_ExcludePickerWindows(struct OH_AVScreenCapture *capture, const int32_t *excludedWindowIDs, uint32_t windowCount)
```

**描述**

在Picker界面中隐藏指定的窗口。在picker界面显示前调用本接口，可对指定窗口进行过滤和隐藏。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [struct OH\_AVScreenCapture](capi-avscreencapture-oh-avscreencapture.md) \*capture | 指向OH\_AVScreenCapture实例的指针。 |
| const int32\_t \*excludedWindowIDs | 需要隐藏的窗口ID数组（已存在的窗口）。 |
| uint32\_t windowCount | 需要隐藏的窗口ID数组长度。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVSCREEN\_CAPTURE\_ErrCode](capi-native-avscreen-capture-errors-h.md#oh_avscreen_capture_errcode) | AV\_SCREEN\_CAPTURE\_ERR\_OK：执行成功。  AV\_SCREEN\_CAPTURE\_ERR\_INVALID\_VAL：输入参数capture为空指针或者窗口ID参数值无效。  AV\_SCREEN\_CAPTURE\_ERR\_OPERATE\_NOT\_PERMIT：不允许操作。 |
