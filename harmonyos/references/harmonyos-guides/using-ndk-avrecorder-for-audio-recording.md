---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/using-ndk-avrecorder-for-audio-recording
title: 使用AVRecorder录制音频(C/C++)
breadcrumb: 指南 > 媒体 > Media Kit（媒体服务） > 媒体开发指导(C/C++) > 录制 > 使用AVRecorder录制音频(C/C++)
category: harmonyos-guides
scraped_at: 2026-04-28T07:46:31+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:448d192548690d2fc8080881cffb24755b95c0a181f380f1a86fe0c65de28bcc
---

AVRecorder支持开发音频或视频单独录制，集成了音频捕获，音频编码，视频编码，音视频封装功能，适用于实现简单音视频录制并直接得到本地媒体文件的场景。

本开发指导将以“开始录制-暂停录制-恢复录制-停止录制”的一次流程为示例，向开发者讲解如何使用AVRecorder进行音频录制。

在进行应用开发的过程中，开发者可以通过AVRecorder的state属性主动获取当前状态，或使用OH\_AVRecorder\_SetStateCallback方法注册回调监听状态变化。开发过程中应该严格遵循状态机要求，例如只能在started状态下调用pause()接口，只能在paused状态下调用resume()接口。

**图1** 录制状态变化示意图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/A6QS3jvFTlquRe0XVEBdwA/zh-cn_image_0000002552958596.png?HW-CC-KV=V1&HW-CC-Date=20260427T234629Z&HW-CC-Expire=86400&HW-CC-Sign=1625019FDB5D09E947D9FFB9535CC5C734D844DEF722D8690D7A742BB0D85E0B)

状态的详细说明请参考[AVRecorderState](../harmonyos-references/arkts-apis-media-t.md#avrecorderstate9)。

## 申请权限

在开发此功能前，开发者应根据实际需求申请相关权限：

* 当需要使用麦克风时，需要申请**ohos.permission.MICROPHONE**麦克风权限。申请方式请参考：[向用户申请授权](request-user-authorization.md)。
* 当需要读取和保存音频文件时，请优先使用[AudioViewPicker音频选择器对象](../harmonyos-references/js-apis-file-picker.md#audioviewpicker)。

说明

仅应用需要克隆、备份或同步用户公共目录的音频类文件时，可申请ohos.permission.READ\_AUDIO、ohos.permission.WRITE\_AUDIO权限来读写音频文件，申请方式请参考[申请受控权限](declare-permissions-in-acl.md)，通过AGC审核后才能使用。为避免应用的上架申请被驳回，开发者应优先使用Picker/控件等替代方案，仅少量符合[特殊场景](restricted-permissions.md#ohospermissionread_audio)的应用被允许申请受限权限。

## 开发步骤及注意事项

选择只录音频时，与视频相关的所有参数（如videoFrameWidth和videoFrameHeight）均不需要配置。同理，选择只录视频不录音频时，与音频相关的所有参数（如audioBitrate和audioChannels）均不需要配置。

开发者通过引入[avrecorder.h](../harmonyos-references/capi-avrecorder-h.md)、[avrecorder\_base.h](../harmonyos-references/capi-avrecorder-base-h.md)和[native\_averrors.h](../harmonyos-references/capi-native-averrors-h.md)头文件，使用视频录制相关API。

AVRecorder详细的API说明请参考[AVRecorder API参考](../harmonyos-references/capi-avrecorder.md)。

在 CMake 脚本中链接动态库。

```
1. target_link_libraries(entry PUBLIC libavrecorder.so)
```

使用[OH\_AVFormat](../harmonyos-references/capi-native-avformat-h.md)相关接口时，需引入如下头文件。

```
1. #include <multimedia/player_framework/native_avformat.h>
```

并在 CMake 脚本中链接如下动态库。

```
1. target_link_libraries(entry PUBLIC libnative_media_core.so)
```

开发者使用系统日志能力时，需引入如下头文件。

```
1. #include <hilog/log.h>
```

并需要在 CMake 脚本中链接如下动态库。

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
   15. if (state == OH_AVRecorder_State::AVRECORDER_PREPARED) {
   16. OH_LOG_INFO(LOG_APP, "==NDKDemo== Recorder OnStateChange PREPARED, reason: %{public}s", reasonStr);
   17. // 处理状态变更。
   18. }
   19. if (state == OH_AVRecorder_State::AVRECORDER_STARTED) {
   20. OH_LOG_INFO(LOG_APP, "==NDKDemo== Recorder OnStateChange STARTED, reason: %{public}s", reasonStr);
   21. // 处理状态变更。
   22. }
   23. if (state == OH_AVRecorder_State::AVRECORDER_PAUSED) {
   24. OH_LOG_INFO(LOG_APP, "==NDKDemo== Recorder OnStateChange PAUSED, reason: %{public}s", reasonStr);
   25. // 处理状态变更。
   26. }
   27. if (state == OH_AVRecorder_State::AVRECORDER_STOPPED) {
   28. OH_LOG_INFO(LOG_APP, "==NDKDemo== Recorder OnStateChange STOPPED, reason: %{public}s", reasonStr);
   29. // 处理状态变更。
   30. }
   31. if (state == OH_AVRecorder_State::AVRECORDER_RELEASED) {
   32. OH_LOG_INFO(LOG_APP, "==NDKDemo== Recorder OnStateChange RELEASED, reason: %{public}s", reasonStr);
   33. // 处理状态变更。
   34. }
   35. if (state == OH_AVRecorder_State::AVRECORDER_ERROR) {
   36. OH_LOG_INFO(LOG_APP, "==NDKDemo== Recorder OnStateChange ERROR, reason: %{public}s", reasonStr);
   37. // 处理状态变更。
   38. }
   39. }

   41. // 设置错误回调。
   42. void OnError(OH_AVRecorder *recorder, int32_t errorCode, const char *errorMsg, void *userData)
   43. {
   44. (void)recorder;
   45. (void)userData;
   46. OH_LOG_INFO(LOG_APP, "==NDKDemo== Recorder OnError errorCode: %{public}d, error message: %{public}s",
   47. errorCode, errorMsg);
   48. }

   50. // 设置生成媒体文件回调（fileGenerationMode选择AUTO_CREATE时设置）。
   51. void OnUri(OH_AVRecorder *recorder, OH_MediaAsset *asset, void *userData)
   52. {
   53. (void)recorder;
   54. (void)userData;
   55. OH_LOG_INFO(LOG_APP, "==NDKDemo== OnUri in!");
   56. if (asset != nullptr) {
   57. auto changeRequest = OH_MediaAssetChangeRequest_Create(asset);
   58. if (changeRequest == nullptr) {
   59. OH_LOG_ERROR(LOG_APP, "==NDKDemo== changeRequest is null!");
   60. return;
   61. }
   62. MediaLibrary_ImageFileType imageFileType = MEDIA_LIBRARY_IMAGE_JPEG; // 待媒体库提供可用的VIDEO接口。
   63. uint32_t result = OH_MediaAssetChangeRequest_SaveCameraPhoto(changeRequest, imageFileType);
   64. OH_LOG_INFO(LOG_APP, "result of OH_MediaAssetChangeRequest_SaveCameraPhoto: %d", result);

   66. uint32_t resultChange = OH_MediaAccessHelper_ApplyChanges(changeRequest);
   67. OH_LOG_INFO(LOG_APP, "result of OH_MediaAccessHelper_ApplyChanges: %d", resultChange);

   69. OH_MediaAsset_Release(asset);
   70. OH_MediaAssetChangeRequest_Release(changeRequest);
   71. } else {
   72. OH_LOG_ERROR(LOG_APP, "Received null media asset!");
   73. }
   74. OH_LOG_INFO(LOG_APP, "==NDKDemo== OnUri out!");
   75. }
   ```
3. 配置音频录制参数，调用OH\_AVRecorder\_Prepare()接口，此时进入prepared状态。

   说明

   配置参数需要注意：

   * 配置参数之前需要确保完成对应权限的申请，请参考[申请权限](using-ndk-avrecorder-for-audio-recording.md#申请权限)。
   * prepare接口的入参OH\_AVRecorder\_Config中设置音频相关的配置参数，如示例代码所示。
   * 录制输出的url地址（即示例里avConfig中的url），形式为fd://xx (fd number)。需要调用基础文件操作接口实现应用文件访问能力，获取方式参考[应用文件访问与管理](native-fileio-guidelines.md)。

   ```
   1. void SetConfig(OH_AVRecorder_Config &config)
   2. {
   3. config.audioSourceType = AVRECORDER_MIC;

   5. // 设置媒体属性。
   6. config.profile.audioBitrate = 100000;
   7. config.profile.audioChannels = 2;
   8. config.profile.audioCodec = AVRECORDER_AUDIO_AAC;
   9. config.profile.audioSampleRate = 48000;

   11. config.profile.fileFormat = AVRECORDER_CFT_MPEG_4A;
   12. config.fileGenerationMode = AVRECORDER_APP_CREATE;
   13. }

   15. // 准备录制。
   16. static napi_value PrepareAVRecorder(napi_env env, napi_callback_info info)
   17. {
   18. (void)info;
   19. OH_LOG_INFO(LOG_APP, "==NDKDemo== PrepareAVRecorder in!");
   20. g_avRecorder = OH_AVRecorder_Create();
   21. OH_LOG_INFO(LOG_APP, "==NDKDemo== AVRecorder Create ok! g_avRecorder: %{public}p", g_avRecorder);
   22. if (g_avRecorder == nullptr) {
   23. OH_LOG_ERROR(LOG_APP, "==NDKDemo== AVRecorder Create failed!");
   24. }
   25. OH_AVRecorder_Config *config = new OH_AVRecorder_Config();

   27. SetConfig(*config);

   29. // 1.设置URL（fileGenerationMode选择APP_CREATE时设置）。
   30. const std::string AVRECORDER_ROOT = "/data/storage/el2/base/files/";
   31. int32_t outputFd = open((AVRECORDER_ROOT + "avrecorder01.mp3").c_str(), O_RDWR | O_CREAT, 0777); // 设置文件名。
   32. std::string fileUrl = "fd://" + std::to_string(outputFd);
   33. config->url = const_cast<char *>(fileUrl.c_str());
   34. OH_LOG_INFO(LOG_APP, "config.url is: %s", const_cast<char *>(fileUrl.c_str()));

   36. // 2.设置回调。
   37. // 状态回调。
   38. OH_AVRecorder_SetStateCallback(g_avRecorder, OnStateChange, nullptr);

   40. // 错误回调。
   41. OH_AVRecorder_SetErrorCallback(g_avRecorder, OnError, nullptr);

   43. // 生成媒体文件回调（fileGenerationMode选择AUTO_CREATE时设置）。
   44. OH_LOG_INFO(LOG_APP, "==NDKDemo== OH_AVRecorder_SetUriCallback in!");
   45. OH_AVErrCode ret = OH_AVRecorder_SetUriCallback(g_avRecorder, OnUri, nullptr);
   46. OH_LOG_INFO(LOG_APP, "==NDKDemo== OH_AVRecorder_SetUriCallback out!");
   47. if (ret == AV_ERR_OK) {
   48. OH_LOG_INFO(LOG_APP, "==NDKDemo== OH_AVRecorder_SetUriCallback succeed!");
   49. } else {
   50. OH_LOG_ERROR(LOG_APP, "==NDKDemo== Failed to set URI callback, error code: %d", ret);
   51. }

   53. // 3.调用prepare接口。
   54. int result = OH_AVRecorder_Prepare(g_avRecorder, config);
   55. if (result != AV_ERR_OK) {
   56. OH_LOG_ERROR(LOG_APP, "==NDKDemo== AVRecorder Prepare failed %{public}d", result);
   57. }

   59. napi_value res;
   60. napi_create_int32(env, result, &res);
   61. return res;
   62. }
   ```
4. 开始录制，调用OH\_AVRecorder\_Start()接口，此时AVRecorder进入started状态。

   ```
   1. OH_AVRecorder_Start(g_avRecorder);
   ```
5. 暂停录制，调用OH\_AVRecorder\_Pause()接口，此时AVRecorder进入paused状态，同时暂停输入源输入数据。

   ```
   1. OH_AVRecorder_Pause(g_avRecorder);
   ```
6. 恢复录制，调用OH\_AVRecorder\_Resume()接口，此时再次进入started状态。

   ```
   1. OH_AVRecorder_Resume(g_avRecorder);
   ```
7. 停止录制，调用OH\_AVRecorder\_Stop()接口，此时进入stopped状态。

   ```
   1. OH_AVRecorder_Stop(g_avRecorder);
   ```
8. 重置资源，调用OH\_AVRecorder\_Reset()重新进入idle状态，允许重新配置录制参数。

   ```
   1. OH_AVRecorder_Reset(g_avRecorder);
   ```
9. 销毁实例，调用OH\_AVRecorder\_Release()进入released状态，退出录制。

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
15. OH_AVRecorder_StateChangeReason reason, void *userData) {
16. (void)recorder;
17. (void)userData;

19. // 将reason转换为字符串表示。
20. const char *reasonStr = (reason == OH_AVRecorder_StateChangeReason::AVRECORDER_USER) ? "USER" :
21. (reason == OH_AVRecorder_StateChangeReason::AVRECORDER_BACKGROUND) ? "BACKGROUND" : "UNKNOWN";

23. if (state == OH_AVRecorder_State::AVRECORDER_IDLE) {
24. OH_LOG_INFO(LOG_APP, "==NDKDemo== Recorder OnStateChange IDLE, reason: %{public}s", reasonStr);
25. // 处理状态变更。
26. }
27. if (state == OH_AVRecorder_State::AVRECORDER_PREPARED) {
28. OH_LOG_INFO(LOG_APP, "==NDKDemo== Recorder OnStateChange PREPARED, reason: %{public}s", reasonStr);
29. // 处理状态变更。
30. }
31. if (state == OH_AVRecorder_State::AVRECORDER_STARTED) {
32. OH_LOG_INFO(LOG_APP, "==NDKDemo== Recorder OnStateChange STARTED, reason: %{public}s", reasonStr);
33. // 处理状态变更。
34. }
35. if (state == OH_AVRecorder_State::AVRECORDER_PAUSED) {
36. OH_LOG_INFO(LOG_APP, "==NDKDemo== Recorder OnStateChange PAUSED, reason: %{public}s", reasonStr);
37. // 处理状态变更。
38. }
39. if (state == OH_AVRecorder_State::AVRECORDER_STOPPED) {
40. OH_LOG_INFO(LOG_APP, "==NDKDemo== Recorder OnStateChange STOPPED, reason: %{public}s", reasonStr);
41. // 处理状态变更。
42. }
43. if (state == OH_AVRecorder_State::AVRECORDER_RELEASED) {
44. OH_LOG_INFO(LOG_APP, "==NDKDemo== Recorder OnStateChange RELEASED, reason: %{public}s", reasonStr);
45. // 处理状态变更。
46. }
47. if (state == OH_AVRecorder_State::AVRECORDER_ERROR) {
48. OH_LOG_INFO(LOG_APP, "==NDKDemo== Recorder OnStateChange ERROR, reason: %{public}s", reasonStr);
49. // 处理状态变更。
50. }
51. }

53. // 设置错误回调。
54. void OnError(OH_AVRecorder *recorder, int32_t errorCode, const char *errorMsg, void *userData)
55. {
56. (void)recorder;
57. (void)userData;
58. OH_LOG_INFO(LOG_APP, "==NDKDemo== Recorder OnError errorCode: %{public}d, error message: %{public}s",
59. errorCode, errorMsg);
60. }

62. // 设置生成媒体文件回调（fileGenerationMode选择AUTO_CREATE时设置）。
63. void OnUri(OH_AVRecorder *recorder, OH_MediaAsset *asset, void *userData)
64. {
65. (void)recorder;
66. (void)userData;
67. OH_LOG_INFO(LOG_APP, "==NDKDemo== OnUri in!");
68. if (asset != nullptr) {
69. auto changeRequest = OH_MediaAssetChangeRequest_Create(asset);
70. if (changeRequest == nullptr) {
71. OH_LOG_ERROR(LOG_APP, "==NDKDemo== changeRequest is null!");
72. return;
73. }
74. MediaLibrary_ImageFileType imageFileType = MEDIA_LIBRARY_IMAGE_JPEG; // 待媒体库提供可用的VIDEO接口。
75. uint32_t result = OH_MediaAssetChangeRequest_SaveCameraPhoto(changeRequest, imageFileType);
76. OH_LOG_INFO(LOG_APP, "result of OH_MediaAssetChangeRequest_SaveCameraPhoto: %d", result);

78. uint32_t resultChange = OH_MediaAccessHelper_ApplyChanges(changeRequest);
79. OH_LOG_INFO(LOG_APP, "result of OH_MediaAccessHelper_ApplyChanges: %d", resultChange);

81. OH_MediaAsset_Release(asset);
82. OH_MediaAssetChangeRequest_Release(changeRequest);
83. } else {
84. OH_LOG_ERROR(LOG_APP, "Received null media asset!");
85. }
86. OH_LOG_INFO(LOG_APP, "==NDKDemo== OnUri out!");
87. }

89. void SetConfig(OH_AVRecorder_Config &config)
90. {
91. config.audioSourceType = AVRECORDER_MIC;

93. // 设置媒体属性。
94. config.profile.audioBitrate = 96000;
95. config.profile.audioChannels = 2;
96. config.profile.audioCodec = AVRECORDER_AUDIO_AAC;
97. config.profile.audioSampleRate = 48000;

99. config.profile.fileFormat = AVRECORDER_CFT_MPEG_4;
100. config.fileGenerationMode = AVRECORDER_APP_CREATE;

102. config.metadata.location.latitude = 27.791863;
103. config.metadata.location.longitude = 64.574687;
104. }

106. // 1.准备录制。
107. static napi_value PrepareAVRecorder(napi_env env, napi_callback_info info)
108. {
109. (void)info;
110. OH_LOG_INFO(LOG_APP, "==NDKDemo== PrepareAVRecorder in!");
111. g_avRecorder = OH_AVRecorder_Create();
112. OH_LOG_INFO(LOG_APP, "==NDKDemo== AVRecorder Create ok! g_avRecorder: %{public}p", g_avRecorder);
113. if (g_avRecorder == nullptr) {
114. OH_LOG_ERROR(LOG_APP, "==NDKDemo== AVRecorder Create failed!");
115. }
116. OH_AVRecorder_Config *config = new OH_AVRecorder_Config();

118. SetConfig(*config);

120. // 1.1设置URL（fileGenerationMode选择APP_CREATE时设置）。
121. const std::string AVRECORDER_ROOT = "/data/storage/el2/base/files/";
122. g_outputFd = open((AVRECORDER_ROOT + "avrecorder01.mp3").c_str(), O_RDWR | O_CREAT, 0777); // 设置文件名。
123. std::string fileUrl = "fd://" + std::to_string(g_outputFd);
124. config->url = const_cast<char *>(fileUrl.c_str());
125. OH_LOG_INFO(LOG_APP, "config.url is: %s", const_cast<char *>(fileUrl.c_str()));

127. // 1.2设置回调。
128. // 状态回调。
129. OH_AVRecorder_SetStateCallback(g_avRecorder, OnStateChange, nullptr);

131. // 错误回调。
132. OH_AVRecorder_SetErrorCallback(g_avRecorder, OnError, nullptr);

134. // 生成媒体文件回调（fileGenerationMode选择AUTO_CREATE时设置）。
135. OH_AVErrCode ret = OH_AVRecorder_SetUriCallback(g_avRecorder, OnUri, nullptr);
136. if (ret == AV_ERR_OK) {
137. OH_LOG_INFO(LOG_APP, "==NDKDemo==  OH_AVRecorder_SetUriCallback succeed!");
138. } else {
139. OH_LOG_ERROR(LOG_APP, "==NDKDemo==  Failed to set URI callback, error code: %d", ret);
140. }

142. // 1.3调用prepare接口。
143. int result = OH_AVRecorder_Prepare(g_avRecorder, config);
144. if (result != AV_ERR_OK) {
145. OH_LOG_ERROR(LOG_APP, "==NDKDemo== AVRecorder Prepare failed %{public}d", result);
146. }

148. napi_value res;
149. napi_create_int32(env, result, &res);
150. return res;
151. }

153. // 2.开始录制。
154. static napi_value StartAVRecorder(napi_env env, napi_callback_info info)
155. {
156. (void)info;
157. OH_LOG_INFO(LOG_APP, "==NDKDemo== g_avRecorder start: %{public}p", g_avRecorder);
158. int result = OH_AVRecorder_Start(g_avRecorder);
159. if (result != AV_ERR_OK) {
160. OH_LOG_ERROR(LOG_APP, "==NDKDemo== AVRecorder Start failed %{public}d", result);
161. }
162. napi_value res;
163. napi_create_int32(env, result, &res);
164. return res;
165. }

167. // 3.暂停录制。
168. static napi_value PauseAVRecorder(napi_env env, napi_callback_info info)
169. {
170. (void)info;
171. int result = OH_AVRecorder_Pause(g_avRecorder);
172. if (result != AV_ERR_OK) {
173. OH_LOG_ERROR(LOG_APP, "==NDKDemo== AVRecorder Pause failed %{public}d", result);
174. }
175. napi_value res;
176. napi_create_int32(env, result, &res);
177. return res;
178. }

180. // 4.恢复录制。
181. static napi_value ResumeAVRecorder(napi_env env, napi_callback_info info)
182. {
183. (void)info;
184. int result = OH_AVRecorder_Resume(g_avRecorder);
185. if (result != AV_ERR_OK) {
186. OH_LOG_ERROR(LOG_APP, "==NDKDemo== AVRecorder Resume failed %{public}d", result);
187. }
188. napi_value res;
189. napi_create_int32(env, result, &res);
190. return res;
191. }

193. // 5.停止录制。
194. static napi_value StopAVRecorder(napi_env env, napi_callback_info info)
195. {
196. (void)info;
197. int result = OH_AVRecorder_Stop(g_avRecorder);
198. if (result != AV_ERR_OK) {
199. OH_LOG_ERROR(LOG_APP, "==NDKDemo== AVRecorder Stop failed %{public}d", result);
200. }
201. close(g_outputFd);
202. napi_value res;
203. napi_create_int32(env, result, &res);
204. return res;
205. }

207. // 6.重置录制状态。
208. static napi_value ResetAVRecorder(napi_env env, napi_callback_info info)
209. {
210. (void)info;
211. // 检查g_avRecorder是否有效。
212. if (g_avRecorder == nullptr) {
213. OH_LOG_ERROR(LOG_APP, "==NDKDemo== g_avRecorder is nullptr!");
214. napi_value res;
215. napi_create_int32(env, AV_ERR_INVALID_VAL, &res);
216. return res;
217. }

219. int result = OH_AVRecorder_Reset(g_avRecorder);
220. if (result != AV_ERR_OK) {
221. OH_LOG_ERROR(LOG_APP, "==NDKDemo== AVRecorder Reset failed %{public}d", result);
222. }
223. napi_value res;
224. napi_create_int32(env, result, &res);
225. return res;
226. }

228. // 7.释放录制资源。
229. static napi_value ReleaseAVRecorder(napi_env env, napi_callback_info info)
230. {
231. (void)info;
232. // 检查g_avRecorder是否有效。
233. if (g_avRecorder == nullptr) {
234. OH_LOG_ERROR(LOG_APP, "==NDKDemo== g_avRecorder is nullptr!");
235. napi_value res;
236. napi_create_int32(env, AV_ERR_INVALID_VAL, &res);
237. return res;
238. }

240. int result = OH_AVRecorder_Release(g_avRecorder);
241. g_avRecorder = nullptr;   // 释放录制资源后，需要显式地将g_avRecorder指针置空。

243. if (result != AV_ERR_OK) {
244. OH_LOG_ERROR(LOG_APP, "==NDKDemo== AVRecorder Release failed %{public}d", result);
245. }
246. napi_value res;
247. napi_create_int32(env, result, &res);
248. return res;
249. }
```
