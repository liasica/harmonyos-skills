---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/avscreencapture-c-basic-process
title: AVScreenCapture录屏基础流程
breadcrumb: 指南 > 媒体 > Media Kit（媒体服务） > 媒体开发指导(C/C++) > 录制 > 使用AVScreenCapture录屏取码流(C/C++) > AVScreenCapture录屏基础流程
category: harmonyos-guides
scraped_at: 2026-04-28T07:46:32+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:a6bdc96679bef2eedb0bf16e82d689ed6423ac6b5faa46b4562632a4a3990da0
---

屏幕录制功能支持开发者获取屏幕数据，适用于屏幕录制、会议共享、直播等场景。开发者可通过调用[AVScreenCapture](media-kit-intro.md#avscreencapture)模块的C API，采集设备内外的音视频数据源。该模块需与窗口管理（Window）、图形处理（Graphic）等模块协同工作，以完成完整的视频采集流程。

从API version 22开始，在PC/2in1设备上录屏时新增如下能力：

* 支持在熄屏但不锁屏的情况下保持录制：需要申请权限**ohos.permission.TIMEOUT\_SCREENOFF\_DISABLE\_LOCK**。配置方式请参见[声明权限](declare-permissions.md)。
* 支持在录制屏幕时不再弹出隐私告警弹窗：需要申请权限**ohos.permission.CUSTOM\_SCREEN\_RECORDING**。配置方式请参见[受限开放权限](restricted-permissions.md)。

## 流程介绍

基础屏幕录制功能涉及到AVScreenCapture实例创建、音视频参数配置、回调设置、开始与停止、结果处理、资源释放等步骤。

在此基础上，开发者可以根据视频录制、直播等特定场景进行更高级的设置，详情参见[AVScreenCapture录屏自定义场景](avscreencapture-c-custom-scenarios.md)。

基础流程如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/HRzlayRGSMGFgAV89Ib4-g/zh-cn_image_0000002552958600.png?HW-CC-KV=V1&HW-CC-Date=20260427T234630Z&HW-CC-Expire=86400&HW-CC-Sign=64781B1D6454B7DEB433BCFEFF84631B3CA167D81C23136E37D057337BB3E492)

录屏采集的内容输出方式如下。

* 文件形式：保存为文件，该文件可以播放、分享等。
* 码流形式：该码流可根据场景进行不同的处理，例如将码流流转到其他模块，实现桌面共享、视频直播等。

## 约束与限制

* 使用AVScreenCapture时需明确其状态变化。创建实例后，调用方法可进入指定状态。在错误状态下执行方法会导致AVScreenCapture出错。开发者应在状态转换前进行检查以避免异常。
* 在录屏取码流场景中，屏幕录制启动时会弹出隐私保护弹框，包含“屏幕隐私保护”选项。勾选后，隐私信息（如横幅通知、控制中心、通话界面等）将被屏蔽。不同产品上的隐私信息可能有差异，以实际录制结果为准。

  隐私保护弹框：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/08/v3/GGtse8rjTtqxKgOvuReEpg/zh-cn_image_0000002583478601.png?HW-CC-KV=V1&HW-CC-Date=20260427T234630Z&HW-CC-Expire=86400&HW-CC-Sign=9CB57CBFA3E8E262B2A65EC4E293C6EF950A2A6C3FA4BFF6B97639D18C1915DC)

## 通用开发步骤

### 依赖导入

在CMake脚本中链接动态库：

```
1. target_link_libraries(entry PUBLIC libnative_avscreen_capture.so libnative_buffer.so libnative_media_core.so)
```

添加头文件：

```
1. #include "napi/native_api.h"
2. #include <multimedia/player_framework/native_avscreen_capture.h>
3. #include <multimedia/player_framework/native_avscreen_capture_base.h>
4. #include <multimedia/player_framework/native_avscreen_capture_errors.h>
5. #include <multimedia/player_framework/native_avbuffer.h>
6. #include <native_buffer/native_buffer.h>
7. #include <vector>
```

### 创建AVScreenCapture实例

实例化对象，通过[OH\_AVScreenCapture\_Create](../harmonyos-references/capi-native-avscreen-capture-h.md#oh_avscreencapture_create)创建[OH\_AVScreenCapture](../harmonyos-references/capi-avscreencapture-oh-avscreencapture.md)。

```
1. OH_AVScreenCapture* capture = OH_AVScreenCapture_Create();
```

### 配置音频采集参数

创建AVScreenCapture实例后，可设置屏幕录制所需要的音频参数[OH\_AudioInfo](../harmonyos-references/capi-avscreencapture-oh-audioinfo.md)，包括内录、麦克风音频[OH\_AudioCaptureInfo](../harmonyos-references/capi-avscreencapture-oh-audiocaptureinfo.md)和输出规格[OH\_AudioEncInfo](../harmonyos-references/capi-avscreencapture-oh-audioencinfo.md)。

如果配置了采集麦克风音频数据，需：

* 配置麦克风权限ohos.permission.MICROPHONE，配置方式请参见[向用户申请权限](request-user-authorization.md)。
* 申请长时任务，申请方式请参见[申请长时任务](continuous-task.md)。

录屏存文件时默认只开启内录。录制过程中，麦克风可以动态开启/关闭，开启后，可同时启动内外录制。

内录音频信息必须设置，麦克风音频信息可按实际场景按需设置。

```
1. // 录屏时获取麦克风，如果同时设置了内录和麦克风音频信息，两者参数设置需保持一致。
2. OH_AudioCaptureInfo micCapInfo = {
3. .audioSampleRate = 48000,
4. .audioChannels = 2,
5. .audioSource = OH_MIC
6. };
7. // 录屏时获取内录数据，内录参数必填。如果同时设置了内录和麦克风音频信息，两者参数设置需保持一致。
8. OH_AudioCaptureInfo innerCapInfo = {
9. .audioSampleRate = 48000,
10. .audioChannels = 2,
11. .audioSource = OH_ALL_PLAYBACK
12. };
13. // 录屏音频输出规格配置。audioBitrate保证输出文件的比特率为设置的预期比特率，和audioSampleRate无强关联。
14. OH_AudioEncInfo audioEncInfo = {
15. .audioBitrate = 48000,
16. .audioCodecformat = OH_AAC_LC
17. };
18. OH_AudioInfo audioInfo = {
19. .micCapInfo = micCapInfo,
20. .innerCapInfo = innerCapInfo,
21. .audioEncInfo = audioEncInfo
22. };
23. // 可以单独设置麦克风开关。
24. bool isMic = true;
25. OH_AVScreenCapture_SetMicrophoneEnabled(capture, isMic);
```

### 配置视频采集参数

录屏的视频采集信息[OH\_VideoInfo](../harmonyos-references/capi-avscreencapture-oh-videoinfo.md)包含录屏输入规格配置[OH\_VideoCaptureInfo](../harmonyos-references/capi-avscreencapture-oh-videocaptureinfo.md)和录屏输出规格配置[OH\_VideoEncInfo](../harmonyos-references/capi-avscreencapture-oh-videoencinfo.md)。

```
1. // 录屏输入规格配置。
2. OH_VideoCaptureInfo videoCapInfo = {
3. .videoFrameWidth = 768,
4. .videoFrameHeight = 1280,
5. .videoSource = OH_VIDEO_SOURCE_SURFACE_RGBA
6. };
7. // 录屏输出规格配置。
8. OH_VideoEncInfo videoEncInfo = {
9. .videoCodec = OH_H264,
10. .videoBitrate = 2000000,
11. .videoFrameRate = 30
12. };
13. OH_VideoInfo videoInfo = {
14. .videoCapInfo = videoCapInfo,
15. .videoEncInfo = videoEncInfo
16. };
```

### 初始化AVScreenCapture实例配置

AVScreenCapture实例的配置信息为[OH\_AVScreenCaptureConfig](../harmonyos-references/capi-avscreencapture-oh-avscreencaptureconfig.md)，包括录制数据格式[OH\_VideoInfo](../harmonyos-references/capi-avscreencapture-oh-videoinfo.md)、音视频采集参数[OH\_AudioInfo](../harmonyos-references/capi-avscreencapture-oh-audioinfo.md)、录屏模式[OH\_CaptureMode](../harmonyos-references/capi-native-avscreen-capture-base-h.md#oh_capturemode)等，录屏模式包含OH\_CAPTURE\_HOME\_SCREEN、OH\_CAPTURE\_SPECIFIED\_SCREEN、OH\_CAPTURE\_SPECIFIED\_WINDOW。

配置完成后通过[OH\_AVScreenCapture\_Init](../harmonyos-references/capi-native-avscreen-capture-h.md#oh_avscreencapture_init)将配置项设置到[OH\_AVScreenCapture](../harmonyos-references/capi-avscreencapture-oh-avscreencapture.md)中。

说明

在PC/2in1设备上，根据不同的录屏模式会有不同弹窗表现，详情见[PC/2in1弹窗模式配置说明](avscreencapture-c-basic-process.md#pc2in1弹窗模式配置说明)。

```
1. // 初始化录屏，传入配置信息OH_AVScreenCaptureConfig。
2. OH_AVScreenCaptureConfig config = {
3. .dataType = OH_ORIGINAL_STREAM,
4. .audioInfo = audioInfo,
5. .captureMode = OH_CAPTURE_HOME_SCREEN, // 录屏模式设置。
6. .videoInfo = videoInfo
7. };
8. OH_AVScreenCapture_Init(capture, config);
```

### 设置数据更新、状态切换、错误上报的回调

回调函数主要用来监听录屏过程中的错误发生、音视频流生成和录屏状态变更等事件，详细内容请参考：[错误回调](../harmonyos-references/capi-native-avscreen-capture-base-h.md#oh_avscreencaptureonerror)、[状态回调](../harmonyos-references/capi-native-avscreen-capture-h.md#oh_avscreencapture_setstatecallback)、[获取数据回调](../harmonyos-references/capi-native-avscreen-capture-h.md#oh_avscreencapture_setdatacallback)。

```
1. // 设置回调。
2. // 错误事件发生回调函数OnError()。
3. void OnError(OH_AVScreenCapture *capture, int32_t errorCode, void *userData) {
4. (void)capture;
5. // 应用根据错误码进行事件处理。
6. (void)errorCode;
7. (void)userData;
8. }

10. // 状态变更事件处理函数OnStateChange()。
11. void OnStateChange(struct OH_AVScreenCapture *capture, OH_AVScreenCaptureStateCode stateCode, void *userData) {
12. (void)capture;
13. if (stateCode == OH_AVScreenCaptureStateCode::OH_SCREEN_CAPTURE_STATE_CANCELED) { // 按照所需状态自行修改填写。
14. // 处理录屏状态变更。
15. }
16. (void)userData;
17. }

19. // 获取并处理音视频原始码流数据回调函数OnBufferAvailable()。
20. void OnBufferAvailable(OH_AVScreenCapture *capture, OH_AVBuffer *buffer, OH_AVScreenCaptureBufferType bufferType, int64_t timestamp, void *userData) {
21. // 处于录屏取码流状态。
22. }
23. int *userData = nullptr;// 用户自定义数据。
24. OH_AVScreenCapture_SetErrorCallback(capture, OnError, userData);
25. OH_AVScreenCapture_SetStateCallback(capture, OnStateChange, userData);
26. OH_AVScreenCapture_SetDataCallback(capture, OnBufferAvailable, userData);
```

### 启动录屏

启动录屏[OH\_AVScreenCapture\_StartScreenCapture](../harmonyos-references/capi-native-avscreen-capture-h.md#oh_avscreencapture_startscreencapture)后，开始采集原始码流，通过回调[OH\_AVScreenCapture\_OnBufferAvailable](../harmonyos-references/capi-native-avscreen-capture-base-h.md#oh_avscreencapture_onbufferavailable)来监听当前是否有码流的产生，通过回调[OH\_AVScreenCapture\_OnStateChange](../harmonyos-references/capi-native-avscreen-capture-base-h.md#oh_avscreencapture_onstatechange)来监听启动状态的变更。

在回调接口中，可以调用获取音频码流[OH\_AVScreenCapture\_AcquireAudioBuffer](../harmonyos-references/capi-native-avscreen-capture-h.md#oh_avscreencapture_acquireaudiobuffer)和获取视频码流[OH\_AVScreenCapture\_AcquireVideoBuffer](../harmonyos-references/capi-native-avscreen-capture-h.md#oh_avscreencapture_acquirevideobuffer)的接口来获取录屏的原始码流。

```
1. OH_AVScreenCapture_StartScreenCapture(capture);
```

### 处理录屏数据

根据音视频采集的参数不同，会生成不同数据流，包含视频流、内录的音频流、麦克风录制的音频流，开发者可根据场景进行不同的处理，如将码流流转到其他模块，实现共享桌面、视频直播等。

```
1. bool IsCaptureStreamRunning = true;
2. // 获取并处理音视频原始码流数据回调函数OnBufferAvailable()。
3. void OnBufferAvailable(OH_AVScreenCapture *capture, OH_AVBuffer *buffer, OH_AVScreenCaptureBufferType bufferType, int64_t timestamp, void *userData) {
4. // 处于录屏取码流状态。
5. if (IsCaptureStreamRunning) {
6. if (bufferType == OH_SCREEN_CAPTURE_BUFFERTYPE_VIDEO) {
7. // 视频buffer。
8. OH_NativeBuffer *nativeBuffer = OH_AVBuffer_GetNativeBuffer(buffer);
9. if (nativeBuffer != nullptr && capture != nullptr) {
10. // 获取buffer容量。
11. int bufferLen = OH_AVBuffer_GetCapacity(buffer);

13. // 获取buffer属性。
14. OH_AVCodecBufferAttr info;
15. OH_AVBuffer_GetBufferAttr(buffer, &info);

17. // 获取nativeBuffer配置。
18. OH_NativeBuffer_Config config;
19. OH_NativeBuffer_GetConfig(nativeBuffer, &config);

21. // 获取buffer地址。
22. uint8_t *buf = OH_AVBuffer_GetAddr(buffer);
23. if (buf == nullptr) {
24. return;
25. }
26. // 使用buffer数据。

28. // nativeBuffer的引用计数值减一，当引用计数值减为0，释放该资源。
29. OH_NativeBuffer_Unreference(nativeBuffer);
30. }
31. } else if (bufferType == OH_SCREEN_CAPTURE_BUFFERTYPE_AUDIO_INNER) {
32. // 内录buffer。
33. // 获取buffer属性。
34. OH_AVCodecBufferAttr info;
35. OH_AVBuffer_GetBufferAttr(buffer, &info);

37. // 获取buffer容量。
38. int bufferLen = OH_AVBuffer_GetCapacity(buffer);

40. // 获取buffer地址。
41. uint8_t *buf = OH_AVBuffer_GetAddr(buffer);
42. if (buf == nullptr) {
43. return;
44. }
45. // 使用buffer数据。
46. } else if (bufferType == OH_SCREEN_CAPTURE_BUFFERTYPE_AUDIO_MIC) {
47. // 麦克风buffer。
48. // 获取buffer容量。
49. int bufferLen = OH_AVBuffer_GetCapacity(buffer);

51. // 获取buffer地址。
52. uint8_t *buf = OH_AVBuffer_GetAddr(buffer);
53. if (buf == nullptr) {
54. return;
55. }
56. // 使用buffer数据。
57. }
58. }
59. }
```

### 停止录屏

调用[OH\_AVScreenCapture\_StopScreenCapture](../harmonyos-references/capi-native-avscreen-capture-h.md#oh_avscreencapture_stopscreencapture)后应用会停止录屏或屏幕共享，释放麦克风。

```
1. // 停止录屏。
2. OH_AVScreenCapture_StopScreenCapture(capture);
```

### 释放资源

调用[OH\_AVScreenCapture\_Release](../harmonyos-references/capi-native-avscreen-capture-h.md#oh_avscreencapture_release)释放创建的OH\_AVScreenCapture实例，需要在停止录屏后释放。

```
1. // 释放录屏资源。
2. OH_AVScreenCapture_Release(capture);
```

## PC/2in1弹窗模式配置说明

系统提供的录屏模式：[录制指定屏幕](avscreencapture-c-basic-process.md#录制指定屏幕)、[录制主屏幕](avscreencapture-c-basic-process.md#录制主屏幕)和[录制指定窗口](avscreencapture-c-basic-process.md#录制指定窗口推荐)。

录屏模式会使用到屏幕ID（displayId）和窗口ID（missionIds）。获取方式可参考：[获取displayid](../harmonyos-references/capi-oh-display-manager-h.md#oh_nativedisplaymanager_createalldisplays)、[获取missionIds](../harmonyos-references/arkts-apis-window-window.md#getwindowproperties9)。

### 录制指定屏幕

即[OH\_CAPTURE\_SPECIFIED\_SCREEN](../harmonyos-references/capi-native-avscreen-capture-base-h.md#oh_capturemode)模式。

在此模式下，启动录屏后，PC/2in1设备会弹出选择共享内容弹窗，并默认选中videoCapInfo.displayId参数对应的屏幕，如果传入的displayId对应的窗口不存在，则不做任何选中。

```
1. // 根据PC/2in1设备分辨率在config中配置录屏的宽度、高度。
2. config.videoInfo.videoCapInfo.videoFrameWidth = 2880;
3. config.videoInfo.videoCapInfo.videoFrameHeight = 1920;

5. // 设置录屏模式为OH_CAPTURE_SPECIFIED_SCREEN，传入屏幕Id。
6. config.captureMode = OH_CAPTURE_SPECIFIED_SCREEN;
7. config.videoInfo.videoCapInfo.displayId = 0;
```

如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0f/v3/6ZHl_MGVSKyw3VGjvrQmAw/zh-cn_image_0000002552798952.png?HW-CC-KV=V1&HW-CC-Date=20260427T234630Z&HW-CC-Expire=86400&HW-CC-Sign=9D9B7437DA34286F07180B79D771203795115034553970B48EFF809E3EF22194)

### 录制主屏幕

即[OH\_CAPTURE\_HOME\_SCREEN](../harmonyos-references/capi-native-avscreen-capture-base-h.md#oh_capturemode)模式。

在此模式下，启动录屏后，PC/2in1设备不会弹出选择录屏内容弹窗，会弹出隐私保护弹窗，同时配置的videoCapInfo.displayId参数不会生效，默认生效主屏的displayId。

```
1. // 根据PC/2in1设备分辨率在config中配置录屏的宽度、高度。
2. config.videoInfo.videoCapInfo.videoFrameWidth = 2880;
3. config.videoInfo.videoCapInfo.videoFrameHeight = 1920;

5. // 设置录屏模式为OH_CAPTURE_HOME_SCREEN，传入屏幕Id。
6. config.captureMode = OH_CAPTURE_HOME_SCREEN;
```

### 录制指定窗口（推荐）

即[OH\_CAPTURE\_SPECIFIED\_WINDOW](../harmonyos-references/capi-native-avscreen-capture-base-h.md#oh_capturemode)模式。

应用需根据PC/2in1设备分辨率配置录屏的高度和宽度值并传入屏幕Id。

若期望录制某个指定窗口，需要设置指定的窗口Id。该场景下，启动录屏后，会弹出选择共享内容弹窗，并默认选中指定的窗口。

```
1. // 根据PC/2in1设备分辨率在config中配置录屏的宽度、高度。
2. config.videoInfo.videoCapInfo.videoFrameWidth = 2880;
3. config.videoInfo.videoCapInfo.videoFrameHeight = 1920;

5. // 设置录屏模式为OH_CAPTURE_SPECIFIED_WINDOW，传入屏幕Id。
6. config.captureMode = OH_CAPTURE_SPECIFIED_WINDOW;
7. config.videoInfo.videoCapInfo.displayId = 0;

9. // (可选)若有期望录制的窗口，可传入单个窗口Id。
10. std::vector<int32_t> missionIds = {61}; // 表示弹出的Picker默认选中61号窗口。
11. config.videoInfo.videoCapInfo.missionIDs = &missionIds[0];
12. config.videoInfo.videoCapInfo.missionIDsLen = static_cast<int32_t>(missionIds.size());
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/sxeXgt0rQOSjEXOPaMv29w/zh-cn_image_0000002583438647.png?HW-CC-KV=V1&HW-CC-Date=20260427T234630Z&HW-CC-Expire=86400&HW-CC-Sign=9AC8C5DB3FC823DE2E344E9116DE742000DAA63484658C5C82976DD84536327D)

若期望同时录制多个窗口，需要传入期望录制的窗口Id列表。该场景下，不弹出选择共享内容弹窗，弹出隐私保护弹窗。

```
1. // 根据PC/2in1设备分辨率在config中配置录屏的宽度、高度。
2. config.videoInfo.videoCapInfo.videoFrameWidth = 2880;
3. config.videoInfo.videoCapInfo.videoFrameHeight = 1920;

5. // 设置录屏模式为OH_CAPTURE_SPECIFIED_WINDOW，传入屏幕Id。
6. config.captureMode = OH_CAPTURE_SPECIFIED_WINDOW;
7. config.videoInfo.videoCapInfo.displayId = 0;

9. // 传入多个窗口Id。
10. vector<int32_t> missionIds = {60, 61}; // 表示期望同时录制60、61号窗口。
11. config.videoInfo.videoCapInfo.missionIDs = &missionIds[0];
12. config.videoInfo.videoCapInfo.missionIDsLen = static_cast<int32_t>(missionIds.size());
```

## Phone/Tablet弹窗模式配置说明

从API version 23开始，支持在设备Phone/Tablet上通过策略控制是否弹出选择共享内容弹窗。

在PC/2in1设备上，是否弹出选择共享内容弹窗受录制模式控制，在Phone/Tablet设备上可以通过[OH\_AVScreenCapture\_StrategyForPickerPopUp](../harmonyos-references/capi-native-avscreen-capture-h.md#oh_avscreencapture_strategyforpickerpopup)配置选择共享内容弹窗模式，无需指定录制模式。

```
1. // 创建AVScreenCapture对象
2. OH_AVScreenCapture* capture = OH_AVScreenCapture_Create();

4. // 创建CaptureStrategy对象。
5. OH_AVScreenCapture_CaptureStrategy* strategy = OH_AVScreenCapture_CreateCaptureStrategy();

7. // 设置是否弹出屏幕捕获Picker。
8. // 设置为true，代表录屏启动后统一弹出Picker。
9. OH_AVScreenCapture_StrategyForPickerPopUp(strategy, true);

11. // 设置CaptureStrategy到AVScreenCapture实例。
12. OH_AVScreenCapture_SetCaptureStrategy(capture, strategy);

14. // 释放CaptureStrategy对象。
15. OH_AVScreenCapture_ReleaseCaptureStrategy(strategy);
```

## 更多资源

* API参考：详细的API描述请见[native\_avscreen\_capture.h](../harmonyos-references/capi-native-avscreen-capture-h.md)。
* 示例工程：该示例调用了媒体AVScreenCapture组件提供的接口能力，提供屏幕捕获的功能，详情见[录屏示例工程](https://gitcode.com/openharmony/applications_app_samples/tree/master/code/DocsSample/Media/ScreenCapture/ScreenCaptureSample)。
