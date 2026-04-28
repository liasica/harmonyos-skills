---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/using-ndk-avrecorder-for-video-recording
title: 使用AVRecorder录制视频(C/C++)
breadcrumb: 指南 > 媒体 > Media Kit（媒体服务） > 媒体开发指导(C/C++) > 录制 > 使用AVRecorder录制视频(C/C++)
category: harmonyos-guides
scraped_at: 2026-04-28T07:46:31+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:ddcc20449cb0706c149aa95640cc44b101b6d35ac6f060bc3a82b9d6cd0baee6
---

AVRecorder支持开发音视频录制，集成了音频捕获，音频编码，视频编码，音视频封装功能，适用于实现简单视频录制并直接得到本地媒体文件的场景。

本开发指导将以“开始录制-暂停录制-恢复录制-停止录制”的一次流程为示例，向开发者讲解如何使用AVRecorder进行视频录制。

在进行应用开发的过程中，开发者可以通过AVRecorder的state属性主动获取当前状态，或使用OH\_AVRecorder\_SetStateCallback方法注册回调监听状态变化。开发过程中应严格遵循状态机要求，例如只能在started状态下调用pause()接口，只能在paused状态下调用resume()接口。

**图1** 录制状态变化示意图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/7i39j5XYQhioMYi0hefgdA/zh-cn_image_0000002583438645.png?HW-CC-KV=V1&HW-CC-Date=20260427T234629Z&HW-CC-Expire=86400&HW-CC-Sign=78C7AD6DE7F55C36372564CDDE779CD4C86DAD70664171732CC69BCD6AC28AC9)

状态的详细说明请参考[AVRecorderState](../harmonyos-references/arkts-apis-media-t.md#avrecorderstate9)。

## 申请权限

在开发此功能前，开发者应根据实际需求申请相关权限：

* 当需要使用麦克风时，需要申请**ohos.permission.MICROPHONE**麦克风权限。申请方式请参考：[向用户申请授权](request-user-authorization.md)。
* 当需要使用相机拍摄时，需要申请**ohos.permission.CAMERA**相机权限。申请方式请参考：[向用户申请授权](request-user-authorization.md)。
* 当需要从图库读取图片或视频文件时，请优先使用媒体库[Picker选择媒体资源](photoaccesshelper-photoviewpicker.md)。
* 当需要保存图片或视频文件至图库时，请优先使用[安全控件保存媒体资源](photoaccesshelper-savebutton.md)。

说明

仅应用需要克隆、备份或同步用户公共目录的图片、视频类文件时，可申请ohos.permission.READ\_IMAGEVIDEO、ohos.permission.WRITE\_IMAGEVIDEO权限来读写音视频文件，申请方式请参考[申请受控权限](declare-permissions-in-acl.md)，通过AGC审核后才能使用。为避免应用的上架申请被驳回，开发者应优先使用Picker/控件等替代方案，仅少量符合[特殊场景](restricted-permissions.md#ohospermissionread_imagevideo)的应用被允许申请受限权限。

## 开发步骤及注意事项

说明

AVRecorder只负责视频数据的处理，需要与视频数据采集模块配合才能完成视频录制。视频数据采集模块需要通过Surface将视频数据传递给AVRecorder进行数据处理。当前常用的数据采集模块为相机模块，具体请参考[相机-录像](native-camera-recording.md)。

文件的创建与存储，请参考[应用文件访问与管理](app-file-access.md)，默认存储在应用的沙箱路径之下，如需存储至图库，请使用[安全控件保存媒体资源](photoaccesshelper-savebutton.md)对沙箱内文件进行存储。

开发者通过引入[avrecorder.h](../harmonyos-references/capi-avrecorder-h.md)、[avrecorder\_base.h](../harmonyos-references/capi-avrecorder-base-h.md)和[native\_averrors.h](../harmonyos-references/capi-native-averrors-h.md)头文件，使用视频录制相关API。

AVRecorder详细的API说明请参考[AVRecorder API参考](../harmonyos-references/capi-avrecorder.md)。

在CMake脚本中链接动态库。

```
1. target_link_libraries(entry PUBLIC libavrecorder.so)
```

使用[OH\_AVFormat](../harmonyos-references/capi-native-avformat-h.md)相关接口时，需引入如下头文件。

```
1. #include <multimedia/player_framework/native_avformat.h>
```

并在CMake脚本中链接如下动态库。

```
1. target_link_libraries(entry PUBLIC libnative_media_core.so)
```

开发者使用系统日志能力时，需引入如下头文件。

```
1. #include <hilog/log.h>
```

并需要在CMake脚本中链接如下动态库。

```
1. target_link_libraries(entry PUBLIC libhilog_ndk.z.so)
```

1. 创建AVRecorder实例，实例创建完成进入idle状态。

   ```
   1. #include <multimedia/player_framework/avrecorder.h>
   2. #include <multimedia/player_framework/avrecorder_base.h>

   4. static struct OH_AVRecorder *g_avRecorder = nullptr;
   5. g_avRecorder = OH_AVRecorder_Create();
   ```
2. 设置业务需要的监听事件，监听状态变化及错误上报。

   | 事件类型 | 说明 |
   | --- | --- |
   | OnStateChange | 监听AVRecorder的状态改变。 |
   | OnError | 监听AVRecorder的错误信息。 |
   | OnUri | 监听AVRecorder生成媒体文件。 |

   ```
   1. // 设置状态回调。
   2. void OnStateChange(OH_AVRecorder *recorder, OH_AVRecorder_State state,
   3. OH_AVRecorder_StateChangeReason reason, void *userData) {
   4. (void)recorder;
   5. (void)userData;

   7. // 将reason转换为字符串表示。
   8. const char *reasonStr = (reason == OH_AVRecorder_StateChangeReason::AVRECORDER_USER) ? "USER" :
   9. (reason == OH_AVRecorder_StateChangeReason::AVRECORDER_BACKGROUND) ? "BACKGROUND" : "UNKNOWN";

   11. if (state == OH_AVRecorder_State::AVRECORDER_IDLE) {
   12. OH_LOG_INFO(LOG_APP, "==NDKDemo== Recorder OnStateChange IDLE, reason: %{public}s", reasonStr);
   13. // 处理状态变更。
   14. }
   15. if (state == OH_AVRecorder_State::PREPARED) {
   16. OH_LOG_INFO(LOG_APP, "==NDKDemo== Recorder OnStateChange PREPARED, reason: %{public}s", reasonStr);
   17. // 处理状态变更。
   18. }
   19. if (state == OH_AVRecorder_State::STARTED) {
   20. OH_LOG_INFO(LOG_APP, "==NDKDemo== Recorder OnStateChange STARTED, reason: %{public}s", reasonStr);
   21. // 处理状态变更。
   22. }
   23. if (state == OH_AVRecorder_State::PAUSED) {
   24. OH_LOG_INFO(LOG_APP, "==NDKDemo== Recorder OnStateChange PAUSED, reason: %{public}s", reasonStr);
   25. // 处理状态变更。
   26. }
   27. if (state == OH_AVRecorder_State::STOPPED) {
   28. OH_LOG_INFO(LOG_APP, "==NDKDemo== Recorder OnStateChange STOPPED, reason: %{public}s", reasonStr);
   29. // 处理状态变更。
   30. }
   31. if (state == OH_AVRecorder_State::RELEASED) {
   32. OH_LOG_INFO(LOG_APP, "==NDKDemo== Recorder OnStateChange RELEASED, reason: %{public}s", reasonStr);
   33. // 处理状态变更。
   34. }
   35. if (state == OH_AVRecorder_State::ERROR) {
   36. OH_LOG_INFO(LOG_APP, "==NDKDemo== Recorder OnStateChange ERROR, reason: %{public}s", reasonStr);
   37. // 处理状态变更。
   38. }
   39. }

   41. // 设置错误回调。
   42. void OnError(OH_AVRecorder *recorder, int32_t errorCode, const char *errorMsg, void *userData) {
   43. (void)recorder;
   44. (void)userData;
   45. OH_LOG_INFO(LOG_APP, "==NDKDemo== Recorder OnError errorCode: %{public}d, error message: %{public}s",
   46. errorCode, errorMsg);
   47. }

   49. // 设置生成媒体文件回调（fileGenerationMode选择AUTO_CREATE时设置）。
   50. void OnUri(OH_AVRecorder *recorder, OH_MediaAsset *asset, void *userData) {
   51. (void)recorder;
   52. (void)userData;
   53. if (asset != nullptr) {
   54. auto changeRequest = OH_MediaAssetChangeRequest_Create(asset);
   55. if (changeRequest == nullptr) {
   56. OH_LOG_ERROR(LOG_APP, "==NDKDemo== changeRequest is null!");
   57. return;
   58. }
   59. MediaLibrary_ImageFileType imageFileType = MEDIA_LIBRARY_IMAGE_JPEG; // 待媒体库提供可用的VIDEO接口。
   60. uint32_t result = OH_MediaAssetChangeRequest_SaveCameraPhoto(changeRequest, imageFileType);
   61. OH_LOG_INFO(LOG_APP, "result of OH_MediaAssetChangeRequest_SaveCameraPhoto: %d", result);

   63. uint32_t resultChange = OH_MediaAccessHelper_ApplyChanges(changeRequest);
   64. OH_LOG_INFO(LOG_APP, "result of OH_MediaAccessHelper_ApplyChanges: %d", resultChange);

   66. OH_MediaAsset_Release(asset);
   67. OH_MediaAssetChangeRequest_Release(changeRequest);
   68. } else {
   69. OH_LOG_ERROR(LOG_APP, "Received null media asset!");
   70. }
   71. }
   ```
3. 配置视频录制参数，调用OH\_AVRecorder\_Prepare()接口，此时进入prepared状态。

   说明

   配置参数需要注意：

   * 配置参数之前需要确保完成对应权限的申请，请参考[申请权限](using-ndk-avrecorder-for-video-recording.md#申请权限)。
   * prepare接口的入参OH\_AVRecorder\_Config中设置的音视频相关的配置参数，如示例代码所示。
   * 需要使用支持的[录制规格](media-kit-intro.md#支持的格式)，视频比特率、分辨率、帧率以实际硬件设备支持的范围为准。
   * 录制输出的url地址（即示例里avConfig中的url），形式为fd://xx (fd number)。需要调用基础文件操作接口实现应用文件访问能力，获取方式参考[应用文件访问与管理](native-fileio-guidelines.md)。

   ```
   1. void SetConfig(OH_AVRecorder_Config &config)
   2. {
   3. config.audioSourceType = AVRECORDER_MIC;
   4. config.videoSourceType = AVRECORDER_SURFACE_ES;

   6. // 设置媒体属性。
   7. config.profile.audioBitrate = 96000;
   8. config.profile.audioChannels = 2;
   9. config.profile.audioCodec = AVRECORDER_AUDIO_AAC;
   10. config.profile.audioSampleRate = 48000;

   12. config.profile.videoBitrate = 2000000;
   13. config.profile.videoFrameWidth = 1280;
   14. config.profile.videoFrameHeight = 720;
   15. config.profile.videoFrameRate = 30;
   16. config.profile.videoCodec = AVRECORDER_VIDEO_AVC;
   17. config.profile.isHdr = false;
   18. config.profile.enableTemporalScale = false;

   20. config.profile.fileFormat = AVRECORDER_CFT_MPEG_4;
   21. config.fileGenerationMode = AVRECORDER_APP_CREATE;

   23. config.metadata.videoOrientation = new char[2]; // 开发者需要自行释放申请的内存。
   24. if (config.metadata.videoOrientation != nullptr) {
   25. strcpy(config.metadata.videoOrientation, "0"); // 视频旋转角度，支持0、90、180、270。
   26. }
   27. OH_LOG_INFO(LOG_APP, "==NDKDemo== videoOrientation: %{public}s", config.metadata.videoOrientation);

   29. config.metadata.location.latitude = 27.791863;
   30. config.metadata.location.longitude = 64.574687;
   31. }

   33. // 准备录制。
   34. static napi_value PrepareAVRecorder(napi_env env, napi_callback_info info)
   35. {
   36. (void)info;
   37. OH_LOG_INFO(LOG_APP, "==NDKDemo== PrepareAVRecorder in!");
   38. g_avRecorder = OH_AVRecorder_Create();
   39. OH_LOG_INFO(LOG_APP, "==NDKDemo== AVRecorder Create ok! g_avRecorder: %{public}p", g_avRecorder);
   40. if (g_avRecorder == nullptr) {
   41. OH_LOG_ERROR(LOG_APP, "==NDKDemo== AVRecorder Create failed!");
   42. }
   43. OH_AVRecorder_Config *config = new OH_AVRecorder_Config(); // 开发者需要自行释放申请的内存。

   45. SetConfig(*config);

   47. // 1.设置URL（fileGenerationMode选择APP_CREATE时设置）。
   48. const std::string AVRECORDER_ROOT = "/data/storage/el2/base/files/";
   49. int32_t outputFd = open((AVRECORDER_ROOT + "avrecorder01.mp4").c_str(), O_RDWR | O_CREAT, 0777); // 设置文件名。
   50. std::string fileUrl = "fd://" + std::to_string(outputFd);
   51. config->url = const_cast<char *>(fileUrl.c_str());
   52. OH_LOG_INFO(LOG_APP, "config.url is: %s", const_cast<char *>(fileUrl.c_str()));

   54. // 2.设置回调。
   55. // 状态回调。
   56. OH_AVRecorder_SetStateCallback(g_avRecorder, OnStateChange, nullptr);

   58. // 错误回调。
   59. OH_AVRecorder_SetErrorCallback(g_avRecorder, OnError, nullptr);

   61. // 生成媒体文件回调（fileGenerationMode选择AUTO_CREATE时设置）。
   62. OH_AVErrCode ret = OH_AVRecorder_SetUriCallback(g_avRecorder, OnUri, nullptr);
   63. if (ret == AV_ERR_OK) {
   64. OH_LOG_INFO(LOG_APP, "==NDKDemo==  OH_AVRecorder_SetUriCallback succeed!");
   65. } else {
   66. OH_LOG_ERROR(LOG_APP, "==NDKDemo==  Failed to set URI callback, error code: %d", ret);
   67. }

   69. // 3.调用prepare接口。
   70. int result = OH_AVRecorder_Prepare(g_avRecorder, config);
   71. if (result != AV_ERR_OK) {
   72. OH_LOG_ERROR(LOG_APP, "==NDKDemo== AVRecorder Prepare failed %{public}d", result);
   73. }

   75. // 4.释放内存。
   76. delete config->metadata.videoOrientation;
   77. delete config;
   78. config = nullptr;

   80. napi_value res;
   81. napi_create_int32(env, result, &res);
   82. return res;
   83. }
   ```
4. 获取视频录制需要的SurfaceID，初始化视频数据输入源。该步骤需要在输入源模块完成，以相机为例，需要创建录像输出流，包括创建Camera对象、获取相机列表、创建相机输入流等，相机详细步骤请参考[相机-录像方案](native-camera-recording.md)。

   调用getInputSurface()接口，接口的返回值SurfaceID用于传递给视频数据输入源模块。常用的输入源模块为相机，以下示例代码中，仅展示获取SurfaceID的步骤。

   输入源模块通过SurfaceID可以获取到Surface，通过Surface可以将视频数据流传递给AVRecorder，由AVRecorder再进行视频数据的处理。

   ```
   1. // 获取surfaceID。
   2. OHNativeWindow *window = nullptr;
   3. int resultCode = OH_AVRecorder_GetInputSurface(g_avRecorder, &window);
   4. uint64_t surfaceId = 0;
   5. if (resultCode == AV_ERR_OK && window != nullptr) {
   6. OH_NativeWindow_GetSurfaceId(window, &surfaceId);
   7. }
   ```
5. 初始化视频数据输入源。该步骤需要在输入源模块完成，以相机为例，需要创建录像输出流，包括创建Camera对象、获取相机列表、创建相机输入流等，相机详细步骤请参考[相机-录像方案](native-camera-recording.md)。
6. 开始录制，启动输入源输入视频数据，例如相机模块调用OH\_VideoOutput\_Start()接口启动相机录制。然后调用OH\_AVRecorder\_Start()接口，此时AVRecorder进入started状态。

   ```
   1. OH_AVRecorder_Start(g_avRecorder);
   ```
7. 暂停录制，调用OH\_AVRecorder\_Pause()接口，此时AVRecorder进入paused状态，同时暂停输入源输入数据。例如相机模块调用OH\_VideoOutput\_Stop()停止相机视频数据输入。

   ```
   1. OH_AVRecorder_Pause(g_avRecorder);
   ```
8. 恢复录制，调用OH\_AVRecorder\_Resume()接口，此时再次进入started状态。

   ```
   1. OH_AVRecorder_Resume(g_avRecorder);
   ```
9. 停止录制，调用OH\_AVRecorder\_Stop()接口，此时进入stopped状态，同时停止相机录制。

   ```
   1. OH_AVRecorder_Stop(g_avRecorder);
   ```
10. 重置资源，调用OH\_AVRecorder\_Reset()重新进入idle状态，允许重新配置录制参数。

    ```
    1. OH_AVRecorder_Reset(g_avRecorder);
    ```
11. 销毁实例，调用OH\_AVRecorder\_Release()进入released状态，退出录制，释放视频数据输入源相关资源，例如相机资源。

    ```
    1. OH_AVRecorder_Release(g_avRecorder);
    ```

## 完整示例

参考以下示例，包括“创建录制实例-准备录制-开始录制-暂停录制-恢复录制-停止录制-重置录制状态-释放录制资源”的完整流程。

```
1. #include <unistd.h>
2. #include <fcntl.h>
3. #include "hilog/log.h"
4. #include <multimedia/player_framework/avrecorder.h>
5. #include <multimedia/player_framework/avrecorder_base.h>
6. #include <multimedia/media_library/media_asset_change_request_capi.h>
7. #include <multimedia/media_library/media_access_helper_capi.h>
8. #include <multimedia/media_library/media_asset_capi.h>

10. static struct OH_AVRecorder *g_avRecorder = nullptr;
11. static int32_t g_outputFd;

13. // 设置状态回调。
14. void OnStateChange(OH_AVRecorder *recorder, OH_AVRecorder_State state,
15. OH_AVRecorder_StateChangeReason reason, void *userData)
16. {
17. (void)recorder;
18. (void)userData;

20. // 将reason转换为字符串表示。
21. const char *reasonStr = (reason == OH_AVRecorder_StateChangeReason::AVRECORDER_USER) ? "USER" :
22. (reason == OH_AVRecorder_StateChangeReason::AVRECORDER_BACKGROUND) ? "BACKGROUND" : "UNKNOWN";

24. if (state == OH_AVRecorder_State::AVRECORDER_IDLE) {
25. OH_LOG_INFO(LOG_APP, "==NDKDemo== Recorder OnStateChange IDLE, reason: %{public}s", reasonStr);
26. // 处理状态变更。
27. }
28. if (state == OH_AVRecorder_State::AVRECORDER_PREPARED) {
29. OH_LOG_INFO(LOG_APP, "==NDKDemo== Recorder OnStateChange PREPARED, reason: %{public}s", reasonStr);
30. // 处理状态变更。
31. }
32. if (state == OH_AVRecorder_State::AVRECORDER_STARTED) {
33. OH_LOG_INFO(LOG_APP, "==NDKDemo== Recorder OnStateChange STARTED, reason: %{public}s", reasonStr);
34. // 处理状态变更。
35. }
36. if (state == OH_AVRecorder_State::AVRECORDER_PAUSED) {
37. OH_LOG_INFO(LOG_APP, "==NDKDemo== Recorder OnStateChange PAUSED, reason: %{public}s", reasonStr);
38. // 处理状态变更。
39. }
40. if (state == OH_AVRecorder_State::AVRECORDER_STOPPED) {
41. OH_LOG_INFO(LOG_APP, "==NDKDemo== Recorder OnStateChange STOPPED, reason: %{public}s", reasonStr);
42. // 处理状态变更。
43. }
44. if (state == OH_AVRecorder_State::AVRECORDER_RELEASED) {
45. OH_LOG_INFO(LOG_APP, "==NDKDemo== Recorder OnStateChange RELEASED, reason: %{public}s", reasonStr);
46. // 处理状态变更。
47. }
48. if (state == OH_AVRecorder_State::AVRECORDER_ERROR) {
49. OH_LOG_INFO(LOG_APP, "==NDKDemo== Recorder OnStateChange ERROR, reason: %{public}s", reasonStr);
50. // 处理状态变更。
51. }
52. }

54. // 设置错误回调。
55. void OnError(OH_AVRecorder *recorder, int32_t errorCode, const char *errorMsg, void *userData)
56. {
57. (void)recorder;
58. (void)userData;
59. OH_LOG_INFO(LOG_APP, "==NDKDemo== Recorder OnError errorCode: %{public}d, error message: %{public}s",
60. errorCode, errorMsg);
61. }

63. // 设置生成媒体文件回调（fileGenerationMode选择AUTO_CREATE时设置）。
64. void OnUri(OH_AVRecorder *recorder, OH_MediaAsset *asset, void *userData)
65. {
66. (void)recorder;
67. (void)userData;
68. OH_LOG_INFO(LOG_APP, "==NDKDemo== OnUri in!");
69. if (asset != nullptr) {
70. auto changeRequest = OH_MediaAssetChangeRequest_Create(asset);
71. if (changeRequest == nullptr) {
72. OH_LOG_ERROR(LOG_APP, "==NDKDemo== changeRequest is null!");
73. return;
74. }
75. MediaLibrary_ImageFileType imageFileType = MEDIA_LIBRARY_IMAGE_JPEG; // 待媒体库提供可用的VIDEO接口。
76. uint32_t result = OH_MediaAssetChangeRequest_SaveCameraPhoto(changeRequest, imageFileType);
77. OH_LOG_INFO(LOG_APP, "result of OH_MediaAssetChangeRequest_SaveCameraPhoto: %d", result);

79. uint32_t resultChange = OH_MediaAccessHelper_ApplyChanges(changeRequest);
80. OH_LOG_INFO(LOG_APP, "result of OH_MediaAccessHelper_ApplyChanges: %d", resultChange);

82. OH_MediaAsset_Release(asset);
83. OH_MediaAssetChangeRequest_Release(changeRequest);
84. } else {
85. OH_LOG_ERROR(LOG_APP, "Received null media asset!");
86. }
87. OH_LOG_INFO(LOG_APP, "==NDKDemo== OnUri out!");
88. }

90. void SetConfig(OH_AVRecorder_Config &config)
91. {
92. config.audioSourceType = AVRECORDER_MIC;
93. config.videoSourceType = AVRECORDER_SURFACE_ES;

95. // 设置媒体属性。
96. config.profile.audioBitrate = 96000;
97. config.profile.audioChannels = 2;
98. config.profile.audioCodec = AVRECORDER_AUDIO_AAC;
99. config.profile.audioSampleRate = 48000;

101. config.profile.videoBitrate = 2000000;
102. config.profile.videoFrameWidth = 1280;
103. config.profile.videoFrameHeight = 720;
104. config.profile.videoFrameRate = 30;
105. config.profile.videoCodec = AVRECORDER_VIDEO_AVC;
106. config.profile.isHdr = false;
107. config.profile.enableTemporalScale = false;

109. config.profile.fileFormat = AVRECORDER_CFT_MPEG_4;
110. config.fileGenerationMode = AVRECORDER_APP_CREATE;

112. config.metadata.videoOrientation = new char[2]; // 开发者需要自行释放申请的内存。
113. if (config.metadata.videoOrientation != nullptr) {
114. strcpy(config.metadata.videoOrientation, "0"); // 视频旋转角度，支持0、90、180、270。
115. }
116. OH_LOG_INFO(LOG_APP, "==NDKDemo== videoOrientation: %{public}s", config.metadata.videoOrientation);

118. config.metadata.location.latitude = 27.791863;
119. config.metadata.location.longitude = 64.574687;
120. }

122. // 1.准备录制。
123. static napi_value PrepareAVRecorder(napi_env env, napi_callback_info info)
124. {
125. (void)info;
126. OH_LOG_INFO(LOG_APP, "==NDKDemo== PrepareAVRecorder in!");
127. g_avRecorder = OH_AVRecorder_Create();
128. OH_LOG_INFO(LOG_APP, "==NDKDemo== AVRecorder Create ok! g_avRecorder: %{public}p", g_avRecorder);
129. if (g_avRecorder == nullptr) {
130. OH_LOG_ERROR(LOG_APP, "==NDKDemo== AVRecorder Create failed!");
131. }
132. OH_AVRecorder_Config *config = new OH_AVRecorder_Config(); // 开发者需要自行释放申请的内存。

134. SetConfig(*config);

136. // 1.1设置URL（fileGenerationMode选择APP_CREATE时设置）。
137. const std::string AVRECORDER_ROOT = "/data/storage/el2/base/files/";
138. g_outputFd = open((AVRECORDER_ROOT + "avrecorder01.mp4").c_str(), O_RDWR | O_CREAT, 0777); // 设置文件名。
139. std::string fileUrl = "fd://" + std::to_string(g_outputFd);
140. config->url = const_cast<char *>(fileUrl.c_str());

142. // 1.2设置回调。
143. // 状态回调。
144. OH_AVRecorder_SetStateCallback(g_avRecorder, OnStateChange, nullptr);

146. // 错误回调。
147. OH_AVRecorder_SetErrorCallback(g_avRecorder, OnError, nullptr);

149. // 生成媒体文件回调（fileGenerationMode选择AUTO_CREATE时设置）。
150. OH_AVErrCode ret = OH_AVRecorder_SetUriCallback(g_avRecorder, OnUri, nullptr);
151. if (ret == AV_ERR_OK) {
152. OH_LOG_INFO(LOG_APP, "==NDKDemo==  OH_AVRecorder_SetUriCallback succeed!");
153. } else {
154. OH_LOG_ERROR(LOG_APP, "==NDKDemo==  Failed to set URI callback, error code: %d", ret);
155. }

157. // 1.3调用prepare接口。
158. int result = OH_AVRecorder_Prepare(g_avRecorder, config);
159. if (result != AV_ERR_OK) {
160. OH_LOG_ERROR(LOG_APP, "==NDKDemo== AVRecorder Prepare failed %{public}d", result);
161. }

163. // 1.4释放内存。
164. delete config->metadata.videoOrientation;
165. delete config;
166. config = nullptr;

168. napi_value res;
169. napi_create_int32(env, result, &res);
170. return res;
171. }

173. // 2.启动相机。
174. static napi_value PrepareCamera(napi_env env, napi_callback_info info)
175. {
176. OH_LOG_INFO(LOG_APP, "==NDKDemo== AVRecorder PrepareCamera");
177. (void)info;

179. OHNativeWindow *window = nullptr;
180. int resultCode = OH_AVRecorder_GetInputSurface(g_avRecorder, &window);
181. if (resultCode != AV_ERR_OK || window == nullptr) {
182. OH_LOG_INFO(LOG_APP, "==NDKDemo== AVRecorder OH_AVRecorder_GetInputSurface failed!");
183. napi_value errorResult;
184. napi_create_int32(env, -1, &errorResult); // -1表示错误
185. return errorResult;
186. }
187. uint64_t surfaceId = 0;
188. OH_NativeWindow_GetSurfaceId(window, &surfaceId);

190. // 将surfaceId传入数据采集模块，具体请参考相机模块。

192. int result = 0;
193. napi_value res;
194. napi_create_int32(env, result, &res);
195. return res;
196. }

198. // 3.开始录制。
199. static napi_value StartAVRecorder(napi_env env, napi_callback_info info)
200. {
201. (void)info;
202. int result = OH_AVRecorder_Start(g_avRecorder);
203. if (result != AV_ERR_OK) {
204. OH_LOG_ERROR(LOG_APP, "==NDKDemo== AVRecorder Start failed %{public}d", result);
205. }
206. napi_value res;
207. napi_create_int32(env, result, &res);
208. return res;
209. }

211. // 4.暂停录制。
212. static napi_value PauseAVRecorder(napi_env env, napi_callback_info info)
213. {
214. (void)info;
215. int result = OH_AVRecorder_Pause(g_avRecorder);
216. if (result != AV_ERR_OK) {
217. OH_LOG_ERROR(LOG_APP, "==NDKDemo== AVRecorder Pause failed %{public}d", result);
218. }
219. napi_value res;
220. napi_create_int32(env, result, &res);
221. return res;
222. }

224. // 5.恢复录制。
225. static napi_value ResumeAVRecorder(napi_env env, napi_callback_info info)
226. {
227. (void)info;
228. int result = OH_AVRecorder_Resume(g_avRecorder);
229. if (result != AV_ERR_OK) {
230. OH_LOG_ERROR(LOG_APP, "==NDKDemo== AVRecorder Resume failed %{public}d", result);
231. }
232. napi_value res;
233. napi_create_int32(env, result, &res);
234. return res;
235. }

237. // 6.停止录制。
238. static napi_value StopAVRecorder(napi_env env, napi_callback_info info)
239. {
240. (void)info;
241. int result = OH_AVRecorder_Stop(g_avRecorder);
242. if (result != AV_ERR_OK) {
243. OH_LOG_ERROR(LOG_APP, "==NDKDemo== AVRecorder Stop failed %{public}d", result);
244. }
245. close(g_outputFd);
246. napi_value res;
247. napi_create_int32(env, result, &res);
248. return res;
249. }

251. // 7.重置录制状态。
252. static napi_value ResetAVRecorder(napi_env env, napi_callback_info info)
253. {
254. (void)info;
255. // 检查g_avRecorder是否有效。
256. if (g_avRecorder == nullptr) {
257. OH_LOG_ERROR(LOG_APP, "==NDKDemo== g_avRecorder is nullptr!");
258. napi_value res;
259. napi_create_int32(env, AV_ERR_INVALID_VAL, &res);
260. return res;
261. }

263. int result = OH_AVRecorder_Reset(g_avRecorder);
264. if (result != AV_ERR_OK) {
265. OH_LOG_ERROR(LOG_APP, "==NDKDemo== AVRecorder Reset failed %{public}d", result);
266. }
267. napi_value res;
268. napi_create_int32(env, result, &res);
269. return res;
270. }

272. // 8.释放录制资源。
273. static napi_value ReleaseAVRecorder(napi_env env, napi_callback_info info)
274. {
275. (void)info;
276. // 检查g_avRecorder是否有效。
277. if (g_avRecorder == nullptr) {
278. OH_LOG_ERROR(LOG_APP, "==NDKDemo== g_avRecorder is nullptr!");
279. napi_value res;
280. napi_create_int32(env, AV_ERR_INVALID_VAL, &res);
281. return res;
282. }

284. int result = OH_AVRecorder_Release(g_avRecorder);
285. g_avRecorder = nullptr;   // 释放录制资源后，需要显式地将g_avRecorder指针置空。

287. if (result != AV_ERR_OK) {
288. OH_LOG_ERROR(LOG_APP, "==NDKDemo== AVRecorder Release failed %{public}d", result);
289. }
290. napi_value res;
291. napi_create_int32(env, result, &res);
292. return res;
293. }
```
