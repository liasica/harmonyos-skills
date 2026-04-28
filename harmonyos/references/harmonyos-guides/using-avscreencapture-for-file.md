---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/using-avscreencapture-for-file
title: 使用AVScreenCapture录屏写文件(C/C++)
breadcrumb: 指南 > 媒体 > Media Kit（媒体服务） > 媒体开发指导(C/C++) > 录制 > 使用AVScreenCapture录屏写文件(C/C++)
category: harmonyos-guides
scraped_at: 2026-04-28T07:46:31+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:471e6bd74ea1b166f4e41960eb670f9f6adaeb9883225b7250aac0fb4082f0ec
---

屏幕录制主要为主屏幕录屏功能。

开发者可以调用录屏（[AVScreenCapture](media-kit-intro.md#avscreencapture)）模块的C API接口，完成屏幕录制，采集设备内、麦克风等的音视频源数据。可以调用录屏模块获取音视频文件，然后通过文件的形式流转到其他模块进行播放或处理，达成文件形式分享屏幕内容的场景。

录屏模块和窗口（Window）、图形（Graphic）等模块协同完成整个视频采集的流程。

使用AVScreenCapture录制屏幕涉及到AVScreenCapture实例的创建、音视频采集参数的配置、采集的开始与停止、资源的释放等。

开始屏幕录制时正在通话中或者屏幕录制过程中来电，录屏将自动停止。因通话中断的录屏会上报OH\_SCREEN\_CAPTURE\_STATE\_STOPPED\_BY\_CALL状态。

屏幕录制过程中发生系统用户切换事件时，录屏将自动停止。因系统用户切换中断的录屏会上报OH\_SCREEN\_CAPTURE\_STATE\_STOPPED\_BY\_USER\_SWITCHES状态。

本开发指导将以完成一次屏幕数据录制的过程为例，向开发者讲解如何使用AVScreenCapture进行屏幕录制，详细的API声明请参考[AVScreenCapture API参考](../harmonyos-references/capi-avscreencapture.md)。

如果配置了采集麦克风音频数据，需对应配置麦克风权限ohos.permission.MICROPHONE和申请长时任务，配置方式请参见[向用户申请权限](request-user-authorization.md)、[申请长时任务](continuous-task.md)。

从API version 22开始，在PC/2in1设备上对应用进行录屏时，可通过申请权限**ohos.permission.TIMEOUT\_SCREENOFF\_DISABLE\_LOCK**，实现在屏幕熄灭但不锁屏的场景下，继续保持录制的效果，配置方式请参见[声明权限](declare-permissions.md)。

从API version 22开始，在PC/2in1设备上对应用进行录屏时，可通过申请权限**ohos.permission.CUSTOM\_SCREEN\_RECORDING**，实现在录制屏幕时不再弹出隐私告警弹窗。配置方式请参见[受限开放权限](restricted-permissions.md)。

## 开发步骤及注意事项

使用AVScreenCapture时要明确其状态的变化，在创建实例后，调用对应的方法可以进入指定的状态实现对应的行为。

在确定的状态下执行不合适的方法会导致AVScreenCapture发生错误，开发者需要在调用状态转换的方法前进行状态检查，避免程序运行异常。

**在 CMake 脚本中链接动态库**

```
1. target_link_libraries(entry PUBLIC libnative_avscreen_capture.so)
```

1. 添加头文件。

   ```
   1. #include "napi/native_api.h"
   2. #include <multimedia/player_framework/native_avscreen_capture.h>
   3. #include <multimedia/player_framework/native_avscreen_capture_base.h>
   4. #include <multimedia/player_framework/native_avscreen_capture_errors.h>
   5. #include <fcntl.h>
   6. #include <string>
   7. #include <unistd.h>
   ```
2. 创建AVScreenCapture实例capture。

   ```
   1. OH_AVScreenCapture* capture = OH_AVScreenCapture_Create();
   ```
3. 配置屏幕录制参数。

   创建AVScreenCapture实例capture后，可以设置屏幕录制所需要的参数。

   其中，录屏存文件时默认录制内录，麦克风可以动态开关，可以同时内外录制。

   同时，录屏存文件需要设置状态回调，感知录制状态。

   ```
   1. // 录屏时获取麦克风或者内录，内录参数必填，如果都设置了，内录和麦克风的参数设置需要一致。
   2. OH_AudioCaptureInfo micCapInfo = {
   3. .audioSampleRate = 48000,
   4. .audioChannels = 2,
   5. .audioSource = OH_MIC
   6. };

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

   19. OH_VideoCaptureInfo videoCapInfo = {
   20. .videoFrameWidth = 768,
   21. .videoFrameHeight = 1280,
   22. .videoSource = OH_VIDEO_SOURCE_SURFACE_RGBA
   23. };

   25. OH_VideoEncInfo videoEncInfo = {
   26. .videoCodec = OH_H264,
   27. .videoBitrate = 2000000,
   28. .videoFrameRate = 30
   29. };

   31. OH_AudioInfo audioInfo = {
   32. .innerCapInfo = innerCapInfo,
   33. .audioEncInfo = audioEncInfo
   34. };

   36. OH_VideoInfo videoInfo = {
   37. .videoCapInfo = videoCapInfo,
   38. .videoEncInfo = videoEncInfo
   39. };

   41. config = {
   42. .captureMode = OH_CAPTURE_HOME_SCREEN,
   43. .dataType = OH_CAPTURE_FILE,
   44. .audioInfo = audioInfo,
   45. .videoInfo = videoInfo,
   46. };

   48. OH_AVScreenCapture_Init(capture, config);
   ```
4. 调用StartScreenRecording()方法开始进行屏幕录制。

   ```
   1. OH_AVScreenCapture_StartScreenRecording(capture);
   ```
5. 调用StopScreenRecording()方法停止录制。

   ```
   1. OH_AVScreenCapture_StopScreenRecording(capture);
   ```
6. 调用Release()方法销毁实例，释放资源。

   ```
   1. OH_AVScreenCapture_Release(capture);
   ```

## 完整示例

下面展示了使用AVScreenCapture屏幕录制存文件的完整示例代码。

```
1. #include "napi/native_api.h"
2. #include <multimedia/player_framework/native_avscreen_capture.h>
3. #include <multimedia/player_framework/native_avscreen_capture_base.h>
4. #include <multimedia/player_framework/native_avscreen_capture_errors.h>
5. #include <fcntl.h>
6. #include <string>
7. #include <unistd.h>

9. int32_t outputFd;
10. struct OH_AVScreenCapture* capture;

12. void OnStateChange(struct OH_AVScreenCapture *capture, OH_AVScreenCaptureStateCode stateCode, void *userData) {
13. (void)capture;

15. if (stateCode == OH_SCREEN_CAPTURE_STATE_STARTED) {
16. // 处理状态变更。
17. }
18. if (stateCode == OH_SCREEN_CAPTURE_STATE_STOPPED_BY_CALL ||
19. stateCode == OH_SCREEN_CAPTURE_STATE_STOPPED_BY_USER_SWITCHES) {
20. // 录屏中断状态处理。
21. }
22. if (stateCode == OH_SCREEN_CAPTURE_STATE_INTERRUPTED_BY_OTHER) {
23. // 处理状态变更。
24. }
25. (void)userData;
26. }

28. // 获取录屏屏幕id的回调函数OnDisplaySelected()。
29. void OnDisplaySelected(struct OH_AVScreenCapture *capture, uint64_t displayId, void *userData) {
30. (void)capture;
31. (void)displayId;
32. (void)userData;
33. }

35. // 录屏内容变更回调函数OnCaptureContentChanged()。
36. void OnCaptureContentChanged(struct OH_AVScreenCapture *capture, OH_AVScreenCaptureContentChangedEvent event, OH_Rect *area, void *userData) {
37. (void)capture;
38. if (event == OH_SCREEN_CAPTURE_CONTENT_HIDE) {
39. // 处理录屏内容变为隐藏。
40. }
41. if (event == OH_SCREEN_CAPTURE_CONTENT_VISIBLE) {
42. // 处理录屏内容变为可见。
43. // 录屏内容变为可见时，可通过回调回传的area参数，获取窗口的位置信息。
44. }
45. if (event == OH_SCREEN_CAPTURE_CONTENT_UNAVAILABLE) {
46. // 处理录屏内容变为不可用，如录屏窗口关闭。
47. }
48. (void)area;
49. (void)userData;
50. }

52. // 手工确认页面用户选择结果的回调函数OnUserSelected()。
53. void OnUserSelected(OH_AVScreenCapture* capture, OH_AVScreenCapture_UserSelectionInfo* selections, void *userData) {
54. (void)capture;
55. (void)userData;
56. int* selectType = new int;
57. uint64_t* displayId = new uint64_t;

59. // 通过获取接口，拿到对应的选择类型和屏幕Id。OH_AVScreenCapture_UserSelectionInfo* selections仅在OnUserSelected回调中有效。
60. OH_AVSCREEN_CAPTURE_ErrCode errorSelectType = OH_AVScreenCapture_GetCaptureTypeSelected(selections, selectType);
61. OH_AVSCREEN_CAPTURE_ErrCode errorDisplayId = OH_AVScreenCapture_GetDisplayIdSelected(selections, displayId);

63. // 在使用完成后，对申请的内存进行释放
64. delete selectType, displayId;
65. }

67. // 开始录屏时调用StartScreenCapture。
68. static napi_value StartScreenCapture(napi_env env, napi_callback_info info) {
69. // 初始化录屏参数，传入配置信息OH_AVScreenCaptureConfig。
70. OH_AVScreenCaptureConfig config;
71. OH_AudioCaptureInfo micCapInfo = {
72. .audioSampleRate = 48000,
73. .audioChannels = 2,
74. .audioSource = OH_MIC
75. };

77. OH_AudioCaptureInfo innerCapInfo = {
78. .audioSampleRate = 48000,
79. .audioChannels = 2,
80. .audioSource = OH_ALL_PLAYBACK
81. };

83. OH_AudioEncInfo audioEncInfo = {
84. .audioBitrate = 48000,
85. .audioCodecformat = OH_AudioCodecFormat::OH_AAC_LC
86. };

88. OH_VideoCaptureInfo videoCapInfo = {
89. .videoFrameWidth = 768,
90. .videoFrameHeight = 1280,
91. .videoSource = OH_VIDEO_SOURCE_SURFACE_RGBA
92. };

94. OH_VideoEncInfo videoEncInfo = {
95. .videoCodec = OH_VideoCodecFormat::OH_H264,
96. .videoBitrate = 2000000,
97. .videoFrameRate = 30
98. };

100. OH_AudioInfo audioInfo = {
101. .micCapInfo = micCapInfo,
102. .innerCapInfo = innerCapInfo,
103. .audioEncInfo = audioEncInfo
104. };

106. OH_VideoInfo videoInfo = {
107. .videoCapInfo = videoCapInfo,
108. .videoEncInfo = videoEncInfo
109. };

111. config = {
112. .captureMode = OH_CAPTURE_HOME_SCREEN,
113. .dataType = OH_CAPTURE_FILE,
114. .audioInfo = audioInfo,
115. .videoInfo = videoInfo,
116. };

118. // 实例化ScreenCapture。
119. capture = OH_AVScreenCapture_Create();

121. OH_RecorderInfo recorderInfo;
122. const std::string SCREEN_CAPTURE_ROOT = "/data/storage/el2/base/files/";
123. outputFd = open((SCREEN_CAPTURE_ROOT + "screen01.mp4").c_str(), O_RDWR | O_CREAT, 0777);

125. // 处理打开失败或创建失败的情况，返回报错结果。
126. if (outputFd == -1) {
127. napi_value errCode;
128. napi_create_double(env, AV_SCREEN_CAPTURE_ERR_IO, &errCode);
129. return errCode;
130. }

132. std::string fileUrl = "fd://" + std::to_string(outputFd);
133. recorderInfo.url = const_cast<char *>(fileUrl.c_str());
134. recorderInfo.fileFormat = OH_ContainerFormatType::CFT_MPEG_4;
135. config.recorderInfo = recorderInfo;

137. // 设置状态回调。
138. OH_AVScreenCapture_SetStateCallback(capture, OnStateChange, nullptr);

140. // 可选，设置录屏内容变化回调。
141. OH_Rect* area = nullptr;
142. OH_AVScreenCapture_SetCaptureContentChangedCallback(capture, OnCaptureContentChanged, area);

144. // 可选，设置隐私窗口屏蔽模式。
145. int value = 0;
146. OH_AVScreenCapture_CaptureStrategy* strategy = OH_AVScreenCapture_CreateCaptureStrategy();
147. OH_AVScreenCapture_StrategyForPrivacyMaskMode(strategy, value);
148. OH_AVScreenCapture_SetCaptureStrategy(capture, strategy);

150. // 可选，设置录屏屏幕Id回调，必须在开始录屏前调用。
151. OH_AVScreenCapture_SetDisplayCallback(capture, OnDisplaySelected, nullptr);

153. // 可选 设置手工确认页面用户选择结果的回调，必须在开始录屏前调用。
154. OH_AVScreenCapture_SetSelectionCallback(capture, OnUserSelected, nullptr);

156. // 可选，设置光标显示开关，开始录屏前后均可调用。
157. OH_AVScreenCapture_ShowCursor(capture, false);

159. // 进行初始化操作。
160. int32_t retInit = OH_AVScreenCapture_Init(capture, config);

162. // 可选（API version 20开始支持）：可以根据需要设置区域坐标和大小，设置想要捕获的区域，如下方创建了一个从（0，0）为起点的长100，宽100的矩形区域。此接口也可以在开始录屏以后设置。
163. OH_Rect* region = new OH_Rect;
164. region->x = 0;
165. region->y = 0;
166. region->width = 100;
167. region->height = 100;
168. uint64_t regionDisplayId = 0; // 传入矩形区域所在的屏幕Id。
169. OH_AVScreenCapture_SetCaptureArea(capture, regionDisplayId, region);

171. // 对申请的内存进行释放。
172. delete region;

174. // 开始录屏。
175. int32_t retStart = OH_AVScreenCapture_StartScreenRecording(capture);

177. // 开始录屏失败的情况处理，返回报错结果。
178. if (retStart != AV_SCREEN_CAPTURE_ERR_OK) {
179. napi_value errCode;
180. napi_create_double(env, retStart, &errCode);
181. return errCode;
182. }

184. // 结束录屏见StopScreenCapture。

186. // 返回调用结果，示例仅返回随意值。
187. napi_value code;
188. napi_create_double(env, AV_SCREEN_CAPTURE_ERR_OK, &code);

190. return code;
191. }

193. // 结束录屏时调用StopScreenCapture。
194. static napi_value StopScreenCapture(napi_env env, napi_callback_info info) {
195. if (capture != nullptr) {
196. // 结束录屏。
197. int32_t retStop = OH_AVScreenCapture_StopScreenRecording(capture);

199. // 关闭文件访问
200. close(outputFd);

202. // 结束录屏失败的情况处理，返回报错结果。
203. if (retStop != AV_SCREEN_CAPTURE_ERR_OK) {
204. napi_value errCode;
205. napi_create_double(env, retStop, &errCode);
206. return errCode;
207. }

209. // 释放ScreenCapture。
210. int32_t retRelease = OH_AVScreenCapture_Release(capture);

212. // 释放ScreenCapture失败情况下处理，返回报错结果。
213. if (retRelease != AV_SCREEN_CAPTURE_ERR_OK) {
214. napi_value errCode;
215. napi_create_double(env, retRelease, &errCode);
216. return errCode;
217. }

219. capture = nullptr;
220. }

222. // 返回成功结果。
223. napi_value code;
224. napi_create_double(env, AV_SCREEN_CAPTURE_ERR_OK, &code);

226. return code;
227. }

229. EXTERN_C_START
230. static napi_value Init(napi_env env, napi_value exports) {
231. napi_property_descriptor desc[] = {
232. {"startScreenCapture", nullptr, StartScreenCapture, nullptr, nullptr, nullptr, napi_default, nullptr},
233. {"stopScreenCapture", nullptr, StopScreenCapture, nullptr, nullptr, nullptr, napi_default, nullptr}};
234. napi_define_properties(env, exports, sizeof(desc) / sizeof(desc[0]), desc);
235. return exports;
236. }
237. EXTERN_C_END

239. static napi_module demoModule = {
240. .nm_version = 1,
241. .nm_flags = 0,
242. .nm_filename = nullptr,
243. .nm_register_func = Init,
244. .nm_modname = "entry",
245. .nm_priv = ((void *)0),
246. .reserved = {0},
247. };

249. extern "C" __attribute__((constructor)) void RegisterEntryModule(void) { napi_module_register(&demoModule); }
```
