---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/pipwindow-native
title: 使用NDK接口实现画中画功能开发（C/C++）
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > 窗口管理 > 在应用程序中使用画中画功能 > 使用NDK接口实现画中画功能开发（C/C++）
category: harmonyos-guides
scraped_at: 2026-04-28T07:40:44+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:56536a2ae17f9e936d02e73aaf855f71614441cd1f462ddba6def7710925fe82
---

本文以视频播放为例，介绍通过NDK接口实现画中画功能的基本开发步骤。

说明

* 从API version 20开始，支持使用NDK接口实现画中画功能开发。
* 支持在Phone、PC/2in1、Tablet设备使用NDK接口实现画中画功能开发。

## 约束与限制

* 画中画窗口中画面的呈现不通过传入XComponent Controller实现，而是通过渲染surfaceId（在开启画中画回调中获取）对应的组件实现。
* 与typeNode实现方式相同，系统不缓存页面。如需进行页面操作，应用需要开启画中画生命周期监听，在对应周期内进行对应操作。
* 不支持设置自动拉起画中画。

## 开发步骤

示例中的视频播放器简易实现逻辑如下：

1. 通过OH\_PictureInPicture\_CreatePipConfig创建画中画参数配置器，并通过OH\_PictureInPicture\_SetPipMainWindowId、OH\_PictureInPicture\_SetPipTemplateType、OH\_PictureInPicture\_SetPipRect、OH\_PictureInPicture\_SetPipControlGroup、OH\_PictureInPicture\_SetPipNapiEnv接口在画中画参数配置器中设置初始配置信息。
2. 创建画中画控制器，后续可根据返回的控制器标识controllerId注册生命周期事件以及控制事件回调。通过OH\_PictureInPicture\_CreatePip接口创建画中画控制器实例，并缓存对应的控制器标识。建议在创建完成后立即调用OH\_PictureInPicture\_DestroyPipConfig销毁画中画参数配置器，以免发生内存泄漏。
3. 通过OH\_PictureInPicture\_RegisterStartPipCallback接口注册启动画中画回调，并根据返回的surfaceId渲染视频画面。同时应用可以按需注册其他需要监听的事件回调。
4. 通过OH\_PictureInPicture\_StartPip启动画中画。
5. 通过OH\_PictureInPicture\_UpdatePipContentSize更新媒体源尺寸信息。
6. 通过OH\_PictureInPicture\_StopPip关闭画中画。
7. 通过OH\_PictureInPicture\_UnregisterStartPipCallback解注册画中画启动回调，避免内存泄漏。同时应用可以按需解注册其他已注册的事件回调。

以上步骤涉及的各文件及示例可见下文。

Node-API模块注册，具体使用请参考[Native API在应用工程中的使用指导](napi-guidelines.md)。

本文件仅作为参考示例，异常处理及错误码打印由开发者按需处理。

```
1. // napi_init.cpp
2. #include "napi/native_api.h"
3. #include <cstddef>
4. #include <cstdint>
5. #include <cstdio>
6. #include <string>
7. #include "window_manager/oh_window_pip.h"
8. #include "hilog/log.h"
9. #include "js_native_api.h"
10. #include "napi/native_api.h"
11. #include <cstdio>
12. #include "rawfile/raw_file_manager.h"

14. #define LOG_MSG_TAG "PiPMain"
15. #define LOG(format, ...) ((void)OH_LOG_Print(LOG_APP, LOG_INFO, 0xFF00, LOG_MSG_TAG, format, ##__VA_ARGS__))
16. napi_ref jsCallback;
17. napi_env env_;

19. napi_ref jsLifecycleCallback;
20. napi_env lifeEnv_;
21. int32_t g_minValue = 0;
22. int32_t g_maxValue = 255;

24. inline bool ConvertFromJsNumber(napi_env env, napi_value jsValue, int32_t& value)
25. {
26. return napi_get_value_int32(env, jsValue, &value) == napi_ok;
27. }

29. inline bool ConvertFromJsNumber(napi_env env, napi_value jsValue, uint32_t& value)
30. {
31. return napi_get_value_uint32(env, jsValue, &value) == napi_ok;
32. }

34. inline bool ConvertFromJsNumber(napi_env env, napi_value jsValue, int64_t& value)
35. {
36. return napi_get_value_int64(env, jsValue, &value) == napi_ok;
37. }

39. inline bool ConvertFromJsNumber(napi_env env, napi_value jsValue, uint64_t& value)
40. {
41. int64_t num;
42. auto res = napi_get_value_int64(env, jsValue, &num);
43. if (res == napi_ok) {
44. value = static_cast<uint64_t>(num);
45. }
46. return res == napi_ok;
47. }

49. inline bool ConvertFromJsNumber(napi_env env, napi_value jsValue, double& value)
50. {
51. return napi_get_value_double(env, jsValue, &value) == napi_ok;
52. }

54. inline bool ConvertFromJsNumber(napi_env env, napi_value jsValue, bool& value)
55. {
56. return napi_get_value_bool(env, jsValue, &value) == napi_ok;
57. }

59. inline bool ConvertFromJsNumber(napi_env env, napi_value jsValue, unsigned char& value)
60. {
61. int32_t num;
62. if (napi_get_value_int32(env, jsValue, &num) != napi_ok) {
63. return false;
64. }
65. if (num < g_minValue || num > g_maxValue) {
66. return false; // 越界无效
67. }
68. value = static_cast<unsigned char>(num);
69. return true;
70. }

72. template<class T>
73. bool ConvertFromJsValue(napi_env env, napi_value jsValue, T& value)
74. {
75. if (jsValue == nullptr) {
76. return false;
77. }
78. using ValueType = std::remove_cv_t<std::remove_reference_t<T>>;
79. if constexpr (std::is_same_v<ValueType, bool>) {
80. return napi_get_value_bool(env, jsValue, &value) == napi_ok;
81. } else if constexpr (std::is_arithmetic_v<ValueType>) {
82. return ConvertFromJsNumber(env, jsValue, value);
83. } else if constexpr (std::is_same_v<ValueType, std::string>) {
84. size_t len = 0;
85. if (napi_get_value_string_utf8(env, jsValue, nullptr, 0, &len) != napi_ok) {
86. return false;
87. }
88. auto buffer = std::make_unique<char[]>(len + 1);
89. size_t strLength = 0;
90. if (napi_get_value_string_utf8(env, jsValue, buffer.get(), len + 1, &strLength) == napi_ok) {
91. value = buffer.get();
92. return true;
93. }
94. return false;
95. } else if constexpr (std::is_enum_v<ValueType>) {
96. std::make_signed_t<ValueType> numberValue = 0;
97. if (!ConvertFromJsNumber(env, jsValue, numberValue)) {
98. return false;
99. }
100. value = static_cast<ValueType>(numberValue);
101. return true;
102. }
103. return false;
104. }

106. void PipStartPipCallback(uint32_t controllerId, uint8_t requestId, uint64_t surfaceId)
107. {
108. if (jsCallback) {
109. napi_value global = nullptr;
110. napi_get_global(env_, &global);
111. size_t argc = 1;
112. std::string tStr = std::to_string(surfaceId);
113. const char* cStr = tStr.c_str();
114. size_t length = strlen(cStr);
115. napi_value str;
116. napi_status status = napi_create_string_utf8(env_, cStr, length, &str);
117. napi_value argv[1] = {str};
118. napi_value jsCallbackValue;

120. napi_value result = nullptr;
121. if (!jsCallback) {
122. LOG("js callback is invalid");
123. }
124. napi_get_reference_value(env_, jsCallback, &jsCallbackValue);
125. napi_call_function(env_, global, jsCallbackValue, argc, argv, &result);
126. }
127. }

129. void LifecycleCallback(uint32_t controllerId, PictureInPicture_PipState state, int32_t errcode)
130. {
131. if (jsLifecycleCallback) {
132. napi_value global = nullptr;
133. napi_get_global(lifeEnv_, &global);
134. size_t argc = 1;
135. napi_value pipState = nullptr;
136. napi_create_int32(lifeEnv_, static_cast<int32_t> (state), &pipState);
137. napi_value argv[1] = {pipState};
138. napi_value jsCallbackValue;

140. napi_value result = nullptr;
141. if (!jsCallback) {
142. LOG("js callback is invalid");
143. }
144. napi_get_reference_value(lifeEnv_, jsLifecycleCallback, &jsCallbackValue);
145. napi_call_function(lifeEnv_, global, jsCallbackValue, argc, argv, &result);
146. }
147. }

149. class PiPManager {
150. public:
151. static napi_value CreatePip(napi_env env, napi_callback_info info);
152. static napi_value StartPip(napi_env env, napi_callback_info info);
153. static napi_value RegisterStartPip(napi_env env, napi_callback_info info);
154. static napi_value DeletePip(napi_env env, napi_callback_info info);
155. static napi_value StopPip(napi_env env, napi_callback_info info);
156. static napi_value RegisterLifecycleListener(napi_env env, napi_callback_info info);
157. static void getElement(napi_env &env, uint32_t size, napi_value &controlGroupValue,
158. PictureInPicture_PipControlGroup controlGroup[]);
159. };

161. napi_value PiPManager::CreatePip(napi_env env, napi_callback_info info)
162. {
163. size_t argc = 1;
164. napi_value argv[1] = {nullptr};
165. napi_get_cb_info(env, info, &argc, argv, nullptr, nullptr);
166. napi_value config = argv[0];

168. napi_value mainWindowIdValue = nullptr;
169. napi_value pipTemplateTypeValue = nullptr;
170. napi_value widthValue = nullptr;
171. napi_value heightValue = nullptr;
172. napi_value controlGroupValue = nullptr;
173. napi_value pipControllerIdValue = nullptr;

175. uint32_t controllerId = -1;
176. uint32_t mainWindowId = -1;
177. PictureInPicture_PipTemplateType pipTemplateType = PictureInPicture_PipTemplateType::VIDEO_PLAY;
178. uint32_t width = -1;
179. uint32_t height = -1;

181. napi_get_named_property(env, config, "mainWindowId", &mainWindowIdValue);
182. napi_get_named_property(env, config, "pipTemplateType", &pipTemplateTypeValue);
183. napi_get_named_property(env, config, "width", &widthValue);
184. napi_get_named_property(env, config, "height", &heightValue);
185. napi_get_named_property(env, config, "controlGroup", &controlGroupValue);
186. napi_get_named_property(env, config, "pipControllerId", &pipControllerIdValue);

188. ConvertFromJsValue(env, mainWindowIdValue, mainWindowId);
189. ConvertFromJsValue(env, pipTemplateTypeValue, pipTemplateType);
190. ConvertFromJsValue(env, widthValue, width);
191. ConvertFromJsValue(env, heightValue, height);
192. ConvertFromJsValue(env, pipControllerIdValue, controllerId);

194. uint32_t size = 0;
195. napi_get_array_length(env, controlGroupValue, &size);
196. PictureInPicture_PipControlGroup controlGroup[size];

198. PiPManager::getElement(env, size, controlGroupValue, controlGroup);

200. napi_value result = nullptr;
201. PictureInPicture_PipConfig pipConfig;
202. OH_PictureInPicture_CreatePipConfig(&pipConfig);
203. OH_PictureInPicture_SetPipMainWindowId(pipConfig, mainWindowId);
204. OH_PictureInPicture_SetPipTemplateType(pipConfig, pipTemplateType);
205. OH_PictureInPicture_SetPipRect(pipConfig, width, height);
206. OH_PictureInPicture_SetPipControlGroup(pipConfig, controlGroup, size);
207. OH_PictureInPicture_SetPipNapiEnv(pipConfig, env);
208. int32_t res = OH_PictureInPicture_CreatePip(pipConfig, &controllerId);
209. OH_PictureInPicture_DestroyPipConfig(&pipConfig);
210. napi_create_uint32(env, controllerId, &result);
211. return result;
212. }

214. void PiPManager::getElement(napi_env &env, uint32_t size, napi_value &controlGroupValue,
215. PictureInPicture_PipControlGroup controlGroup[])
216. {
217. for (uint32_t i = 0; i < size; i++) {
218. napi_value getElementValue = nullptr;
219. napi_get_element(env, controlGroupValue, i, &getElementValue);
220. PictureInPicture_PipControlGroup controlType;
221. if (ConvertFromJsValue(env, getElementValue, controlType)) {
222. controlGroup[i] = controlType;
223. }
224. LOG("controlType: %{public}d", controlType);
225. }
226. }

228. napi_value PiPManager::StartPip(napi_env env, napi_callback_info info)
229. {
230. size_t argc = 1;
231. napi_value argv[1] = {nullptr};
232. napi_get_cb_info(env, info, &argc, argv, nullptr, nullptr);
233. napi_value controlIdValue = argv[0];
234. uint32_t controlId = -1;
235. ConvertFromJsValue(env, controlIdValue, controlId);
236. napi_value resultValue = nullptr;
237. int32_t result = OH_PictureInPicture_StartPip(controlId);
238. napi_create_uint32(env, result, &resultValue);
239. return resultValue;
240. }

242. napi_value PiPManager::RegisterStartPip(napi_env env, napi_callback_info info)
243. {
244. size_t argc = 2;
245. napi_value argv[2] = {nullptr};
246. napi_get_cb_info(env, info, &argc, argv, nullptr, nullptr);
247. napi_value controllerIdValue = argv[0];
248. uint32_t controlId = -1;
249. napi_status status = napi_create_reference(env, argv[1], 1, &jsCallback);
250. env_ = env;
251. ConvertFromJsValue(env, controllerIdValue, controlId);
252. napi_value resultValue = nullptr;
253. int32_t result = OH_PictureInPicture_RegisterStartPipCallback(controlId, PipStartPipCallback);
254. napi_create_uint32(env, result, &resultValue);
255. return resultValue;
256. }

258. napi_value PiPManager::DeletePip(napi_env env, napi_callback_info info)
259. {
260. size_t argc = 1;
261. napi_value argv[1] = {nullptr};
262. napi_get_cb_info(env, info, &argc, argv, nullptr, nullptr);
263. uint32_t controlId = -1;
264. ConvertFromJsValue(env, argv[0], controlId);
265. napi_value resultValue = nullptr;
266. int32_t result = OH_PictureInPicture_DeletePip(controlId);
267. napi_create_uint32(env, result, &resultValue);
268. return resultValue;
269. }

271. napi_value PiPManager::StopPip(napi_env env, napi_callback_info info)
272. {
273. size_t argc = 1;
274. napi_value argv[1] = {nullptr};
275. napi_get_cb_info(env, info, &argc, argv, nullptr, nullptr);
276. uint32_t controlId = -1;
277. napi_value resultValue = nullptr;

279. ConvertFromJsValue(env, argv[0], controlId);
280. uint32_t result = OH_PictureInPicture_StopPip(controlId);
281. napi_create_uint32(env, result, &resultValue);
282. return resultValue;
283. }

285. napi_value PiPManager::RegisterLifecycleListener(napi_env env, napi_callback_info info)
286. {
287. size_t argc = 2;
288. napi_value argv[2] = {nullptr};
289. napi_get_cb_info(env, info, &argc, argv, nullptr, nullptr);
290. uint32_t controlId = -1;
291. napi_status status = napi_create_reference(env, argv[1], 1, &jsLifecycleCallback);
292. lifeEnv_ = env;
293. if (status != napi_ok) {
294. LOG("register failed %{public}d", status);
295. }
296. ConvertFromJsValue(env, argv[0], controlId);

298. napi_value resultValue = nullptr;
299. int32_t result = OH_PictureInPicture_RegisterLifecycleListener(controlId, LifecycleCallback);
300. napi_create_uint32(env, result, &resultValue);
301. return resultValue;
302. }

304. EXTERN_C_START
305. static napi_value Init(napi_env env, napi_value exports)
306. {
307. napi_property_descriptor desc[] = {
308. {"createPip", nullptr, PiPManager::CreatePip, nullptr, nullptr, nullptr, napi_default, nullptr},
309. {"startPip", nullptr, PiPManager::StartPip, nullptr, nullptr, nullptr, napi_default, nullptr},
310. {"registerStartPip", nullptr, PiPManager::RegisterStartPip, nullptr, nullptr, nullptr, napi_default, nullptr},
311. {"deletePip", nullptr, PiPManager::DeletePip, nullptr, nullptr, nullptr, napi_default, nullptr},
312. {"stopPip", nullptr, PiPManager::StopPip, nullptr, nullptr, nullptr, napi_default, nullptr},
313. {"registerLifecycleListener", nullptr, PiPManager::RegisterLifecycleListener,
314. nullptr, nullptr, nullptr, napi_default, nullptr},
315. };
316. napi_define_properties(env, exports, sizeof(desc) / sizeof(desc[0]), desc);
317. return exports;
318. }
319. EXTERN_C_END

321. static napi_module demoModule = {
322. .nm_version = 1,
323. .nm_flags = 0,
324. .nm_filename = nullptr,
325. .nm_register_func = Init,
326. .nm_modname = "entry",
327. .nm_priv = ((void*)0),
328. .reserved = { 0 },
329. };
330. extern "C" __attribute__((constructor)) void RegisterEntryModule(void)
331. {
332. napi_module_register(&demoModule);
333. }
```

Node-API接口声明。

```
1. // Index.d.ts
2. export enum PiPControlGroup {
3. VIDEO_PLAY_VIDEO_PREVIOUS_NEXT = 101,
4. VIDEO_PLAY_FAST_FORWARD_BACKWARD = 102,
5. VIDEO_CALL_MICROPHONE_SWITCH = 201,
6. VIDEO_CALL_HANG_UP_BUTTON = 202,
7. VIDEO_CALL_CAMERA_SWITCH = 203,
8. VIDEO_CALL_MUTE_SWITCH = 204,
9. VIDEO_MEETING_HANG_UP_BUTTON = 301,
10. VIDEO_MEETING_CAMERA_SWITCH = 302,
11. VIDEO_MEETING_MUTE_SWITCH = 303,
12. VIDEO_MEETING_MICROPHONE_SWITCH = 304,
13. VIDEO_LIVE_VIDEO_PLAY_PAUSE = 401,
14. VIDEO_LIVE_MUTE_SWITCH = 402,
15. }
16. export interface PiPConfig {
17. mainWindowId: number;
18. pipTemplateType: number;
19. width: number;
20. height: number;
21. controlGroup: Array<PiPControlGroup>;
22. }
23. export declare const createPip: (config: PiPConfig) => number;
24. export declare const startPip: (controllerId: number) => number;
25. export declare const registerStartPip: (controllerId: number, jsCallback: Function) => number;
26. export declare const deletePip: (controllerId: number) => number;
27. export declare const stopPip: (controllerId: number) => number;
28. export declare const registerLifecycleListener: (controllerId: number, jsCallback: Function) => number;
```

CMakeLists.txt文件，用于生成对应的库文件。

```
1. # CMakeLists.txt
2. # the minimum version of CMake.
3. cmake_minimum_required(VERSION 3.5.0)
4. set(CMAKE_CXX_STANDARD 17)
5. set(CMAKE_CXX_STANDARD_REQUIRED ON)
6. project(MyApplication)
7. set(NATIVERENDER_ROOT_PATH ${CMAKE_CURRENT_SOURCE_DIR})
8. if(DEFINED PACKAGE_FIND_FILE)
9. include(${PACKAGE_FIND_FILE})
10. endif()
11. include_directories(${NATIVERENDER_ROOT_PATH}
12. ${NATIVERENDER_ROOT_PATH}/include)
13. add_library(entry SHARED napi_init.cpp)
14. target_link_libraries(entry PUBLIC libace_napi.z.so libace_ndk.z.so libnative_window_manager.so libhilog_ndk.z.so)
```

EntryAbility文件示例。

```
1. // entryability/EntryAbility.ets
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { AbilityConstant, ConfigurationConstant, UIAbility, Want } from '@kit.AbilityKit';
4. import { window } from '@kit.ArkUI';
5. import { PipManager } from '../nodefree/PipManager';
6. import { Logger } from '../util/LogUtil';

8. export default class EntryAbility extends UIAbility {
9. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
10. AppStorage.setOrCreate('UIAbilityContext', this.context);
11. this.context.getApplicationContext().setColorMode(ConfigurationConstant.ColorMode.COLOR_MODE_NOT_SET);
12. }

14. onDestroy(): void {
15. Logger.info('testTag', '%{public}s', 'Ability onDestroy');
16. }

18. onWindowStageCreate(windowStage: window.WindowStage): void {
19. // Main window is created, set main page for this ability
20. Logger.info('testTag', '%{public}s', 'Ability onWindowStageCreate');
21. let windowClass: window.Window | undefined = undefined;
22. let windowClassId: number = -1;

24. windowStage.getMainWindow().then((window) => {
25. if (window == null) {
26. Logger.error('Failed to obtaining the window. Cause: The data is empty');
27. return;
28. }
29. windowClass = window;
30. windowClass.setUIContent('pages/Index');
31. windowClassId = windowClass.getWindowProperties().id;
32. AppStorage.setOrCreate('windowId', windowClassId);
33. Logger.info('Succeeded in obtaining the window')

35. let ctx = window.getUIContext();
36. AppStorage.setOrCreate('UIContext', ctx);
37. // 通过主窗口UIContext创建typeNode节点
38. PipManager.getInstance().makeTypeNode(ctx);
39. }).catch((err: BusinessError) => {
40. Logger.error(`Failed to obtaining the window. Cause code: ${err.code}, message: ${err.message}`);
41. });
42. windowStage.loadContent('pages/Index', (err) => {
43. if (err.code) {
44. Logger.error('testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err));
45. return;
46. }
47. Logger.info('testTag', 'Succeeded in loading the content.');
48. });
49. }
50. onWindowStageDestroy(): void {
51. // Main window is destroyed, release UI related resources
52. Logger.info('testTag', '%{public}s', 'Ability onWindowStageDestroy');
53. }

55. onForeground(): void {
56. // Ability has brought to foreground
57. Logger.info('testTag', '%{public}s', 'Ability onForeground');
58. }

60. onBackground(): void {
61. // Ability has back to background
62. Logger.info('testTag', '%{public}s', 'Ability onBackground');
63. }
64. }
```

示例中的视频播放需要使用AVPlayer，具体实现可参考[视频播放](video-playback.md)。

```
1. // model/AVPlayer.ets
2. // 视频播放器简单实现
3. import media from '@ohos.multimedia.media';
4. import common from '@ohos.app.ability.common';
5. import { BusinessError } from '@ohos.base';
6. import resourceManager from '@ohos.resourceManager';
7. import { Logger } from '../util/LogUtil';

9. export class AVPlayer {
10. public avPlayer?: media.AVPlayer;
11. private count: number = 0;
12. private surfaceID: string; // surfaceID用于播放画面显示，具体的值需要通过XComponent接口获取，相关文档链接见上面XComponent创建方法
13. public jumpNext: boolean = false;
14. public type: number = 0; // 用于区分主界面的player还是pip界面的player
15. public state_: string = ''
16. public playStatus: boolean = true;

18. constructor(surfaceID: string, type: number) {
19. this.surfaceID = surfaceID;
20. this.type = type
21. }

23. setSurfaceId(id: string) {
24. if (this.avPlayer) {
25. this.surfaceID = id;
26. this.avPlayer.surfaceId = id;
27. }
28. }

30. updatePlayStatus(status: boolean) {
31. this.playStatus = status;
32. }
33. // 注册avplayer回调函数
34. setAVPlayerCallback() {
35. // seek操作结果回调函数
36. this.avPlayer?.on('seekDone', (seekDoneTime: number) => {
37. Logger.info(`PipMain AVPlayer seek succeeded, seek time is ${seekDoneTime}`);
38. })
39. // error回调监听函数,当avPlayer在操作过程中出现错误时调用reset接口触发重置流程
40. this.avPlayer?.on('error', (err: BusinessError) => {
41. Logger.error(`PipMain Invoke avPlayer failed, code is ${err.code}, message is ${err.message}`);
42. this.avPlayer?.reset(); // 调用reset重置资源，触发idle状态
43. })
44. // 状态机变化回调函数
45. this.avPlayer?.on('stateChange', async (state, reason) => {
46. if (!this.avPlayer) {
47. return;
48. }
49. this.state_ = state;
50. switch (state) {
51. case 'idle': // 成功调用reset接口后触发该状态机上报
52. Logger.info('AVPlayer state idle called.');
53. if (!this.jumpNext) {
54. this.avPlayer.release(); // 调用release接口销毁实例对象
55. } else {
56. let uiContext: UIContext = AppStorage.get('UIAbilityContext') as UIContext;
57. let context = uiContext.getHostContext() as common.UIAbilityContext;
58. let fileDescriptor: resourceManager.RawFileDescriptor;
59. fileDescriptor = await context.resourceManager.getRawFd('640x360.mp4');
60. // 为fdSrc赋值触发initialized状态机上报
61. this.avPlayer.fdSrc = fileDescriptor;
62. }
63. break;
64. case 'initialized': // avplayer 设置播放源后触发该状态上报
65. Logger.info('initialized called.');
66. this.avPlayer.surfaceId = this.surfaceID; // 设置显示画面，当播放的资源为纯音频时无需设置
67. this.avPlayer.prepare().then(() => {
68. Logger.info('AVPlayer prepare succeeded.');
69. }, (err: BusinessError) => {
70. Logger.error(`Invoke prepare failed, code is ${err.code}, message is ${err.message}`);
71. });
72. break;
73. case 'prepared': // prepare调用成功后上报该状态机
74. Logger.info('AVPlayer state prepared called.');
75. this.avPlayer.play(); // 调用播放接口开始播放
76. break;
77. case 'playing': // play成功调用后触发该状态机上报
78. Logger.info('AVPlayer state playing called.');
79. this.jumpNext = false;
80. this.count++;
81. break;
82. case 'paused': // pause成功调用后触发该状态机上报
83. Logger.info('AVPlayer state paused called.');
84. // this.avPlayer.play(); // 再次播放接口开始播放
85. break;
86. case 'completed': // 播放结束后触发该状态机上报
87. Logger.info('AVPlayer state completed called.');
88. this.playNext();
89. ; //调用播放结束接口
90. break;
91. case 'stopped': // stop接口成功调用后触发该状态机上报
92. Logger.info('AVPlayer state stopped called.');
93. this.avPlayer.reset(); // 调用reset接口初始化avplayer状态
94. break;
95. case 'released':
96. Logger.info('AVPlayer state released called.');
97. break;
98. default:
99. Logger.info('AVPlayer state unknown called.');
100. break;
101. }
102. })
103. this.avPlayer?.on('videoSizeChange', (width: number, height: number) => {
104. Logger.info('videoSizeChange width:' + width + ' height:' + height);
105. let context = AppStorage.get('UIAbilityContext') as common.UIAbilityContext;
106. })
107. }

109. // 以下demo为使用资源管理接口获取打包在HAP内的媒体资源文件并通过fdSrc属性进行播放示例
110. async avPlayerFdSrc() {
111. // 创建avPlayer实例对象
112. Logger.info('avPlayerFdSrc');
113. this.avPlayer = await media.createAVPlayer();

115. // 创建状态机变化回调函数
116. this.setAVPlayerCallback();
117. // 通过UIAbilityContext的resourceManager成员的getRawFd接口获取媒体资源播放地址
118. // 返回类型为{fd,offset,length},fd为HAP包fd地址，offset为媒体资源偏移量，length为播放长度

120. let context = AppStorage.get('UIAbilityContext') as common.UIAbilityContext;
121. let fileDescriptor = await context.resourceManager.getRawFd('640x360.mp4');
122. Logger.info('getRawFd');
123. // 为fdSrc赋值触发initialized状态机上报
124. this.avPlayer.fdSrc = fileDescriptor;
125. }

127. async playNext() {
128. if (this.avPlayer === null) {
129. return;
130. }
131. this.jumpNext = true;
132. this.avPlayer?.stop();
133. }

135. play() {
136. if (this.state_ === 'paused') {
137. this.avPlayer?.play();
138. }
139. }

141. pause() {
142. if (this.state_ === 'playing') {
143. this.avPlayer?.pause();
144. }
145. }

147. stopAvPlayer() {
148. Logger.info('stopAvPlayer>>>')
149. if (!this.avPlayer) {
150. return;
151. }
152. this.avPlayer.stop();
153. Logger.info('stopping>>>');
154. this.avPlayer.reset();
155. }
156. }
```

应用界面布局文件，用于演示画中画基本功能。

```
1. // pages/Index.ets
2. // 应用首页
3. import { router } from '@kit.ArkUI';

5. @Entry
6. @Component
7. struct Index {
8. pathStack: NavPathStack = new NavPathStack();

10. build() {
11. Navigation(this.pathStack) {
12. Scroll() {
13. Flex({ direction: FlexDirection.Column }) {
14. // ...
15. this.featureButton('使用NDK接口实现画中画（C++）', this.ndkImplement);
16. }
17. }
18. }
19. .hideBackButton(true)
20. .titleMode(NavigationTitleMode.Mini)
21. .backgroundColor('#FFF1F3F5')
22. .mode(NavigationMode.Stack)
23. .title('画中画SampleCode')
24. }

26. @Builder
27. featureButton(buttonText: string, callbackOnClick: () => void) {
28. Button({ type: ButtonType.Normal }) {
29. Row() {
30. Column() {
31. Text(buttonText)
32. .fontSize(24)
33. .fontWeight(FontWeight.Bold)
34. .fontColor('#000000')
35. Rect()
36. .radius(1)
37. .fill('#0A59F7')
38. .height(2)
39. .width(30)
40. }
41. .width('100%')
42. .alignItems(HorizontalAlign.Start)
43. }
44. .width('100%')
45. }
46. .width('90%')
47. .padding('5%')
48. .margin({ top: '3%', bottom: '2%', right: '3%' })
49. .backgroundColor('#FFFFFF')
50. .borderRadius(20)
51. .onClick(callbackOnClick)
52. }

54. // ...
55. private ndkImplement = () => {
56. this.getUIContext().getRouter().pushUrl({ url: 'pages/NDKImplementPage' }, router.RouterMode.Standard)
57. }
58. }
```

```
1. // pages/NDKImplementIndexPage.ets
2. // 画中画功能演示界面
3. import testNapi, {PiPConfig} from 'libentry.so';
4. import { PiPWindow } from '@kit.ArkUI';
5. import { AVPlayer } from '../model/NDKAVPlayer';
6. import { Logger } from '../util/LogUtil';

8. const TAG = 'PipMain';
9. export enum PiPControlGroup {
10. VIDEO_PLAY_VIDEO_PREVIOUS_NEXT = 101,
11. VIDEO_PLAY_FAST_FORWARD_BACKWARD = 102,
12. VIDEO_CALL_MICROPHONE_SWITCH = 201,
13. VIDEO_CALL_HANG_UP_BUTTON = 202,
14. VIDEO_CALL_CAMERA_SWITCH = 203,
15. VIDEO_CALL_MUTE_SWITCH = 204,
16. VIDEO_MEETING_HANG_UP_BUTTON = 301,
17. VIDEO_MEETING_CAMERA_SWITCH = 302,
18. VIDEO_MEETING_MUTE_SWITCH = 303,
19. VIDEO_MEETING_MICROPHONE_SWITCH = 304,
20. VIDEO_LIVE_VIDEO_PLAY_PAUSE = 401,
21. VIDEO_LIVE_MUTE_SWITCH = 402,
22. }

24. @Entry
25. @Component
26. struct NDKImplementIndexPage {
27. @State message: string = 'Hello World';
28. mXComponentController: XComponentController | null = new XComponentController();
29. private controllerId: number = -1;
30. private contentWidth: number = 1920;
31. private contentHeight: number = 1080;
32. private pipType: PiPWindow.PiPTemplateType = PiPWindow.PiPTemplateType.VIDEO_PLAY;
33. private pipControlGroups: Array<PiPControlGroup> = [];
34. player?: AVPlayer;
35. surfaceId = '';

37. changeSurface = (surfaceId: string) => {
38. if(this.player) {
39. this.player.setSurfaceId(surfaceId);
40. return;
41. }
42. Logger.info(`[${TAG}] change surface failed`);
43. }

45. private onStateChange = (state: PiPWindow.PiPState) => {
46. switch(state) {
47. case PiPWindow.PiPState.ABOUT_TO_START:
48. Logger.info(`[${TAG}] ABOUT_TO_START`);
49. break;
50. case PiPWindow.PiPState.STARTED:
51. Logger.info(`[${TAG}] STARTED`);
52. break;
53. case PiPWindow.PiPState.ABOUT_TO_STOP:
54. Logger.info(`[${TAG}] ABOUT_TO_STOP`);
55. break;
56. case PiPWindow.PiPState.STOPPED:
57. if (this.mXComponentController) {
58. this.changeSurface(this.mXComponentController?.getXComponentSurfaceId());
59. }
60. Logger.info(`[${TAG}] STOPPED`);
61. break;
62. case PiPWindow.PiPState.ABOUT_TO_RESTORE:
63. this.changeSurface(this.surfaceId);
64. Logger.info(`[${TAG}] ABOUT_TO_RESTORE`);
65. break;
66. case PiPWindow.PiPState.ERROR:
67. Logger.info(`[${TAG}] ERROR`);
68. break;
69. default:
70. break;
71. }
72. }

75. build() {
76. RelativeContainer() {
77. Row({ space: 20 }) {

79. Button('更换模板')
80. .bindMenu([
81. {
82. value: '视频',
83. action: () => {
84. this.pipType = PiPWindow.PiPTemplateType.VIDEO_PLAY;
85. this.pipControlGroups = [PiPControlGroup.VIDEO_PLAY_VIDEO_PREVIOUS_NEXT];
86. }
87. },
88. {
89. value: '通话',
90. action: () => {
91. this.pipType = PiPWindow.PiPTemplateType.VIDEO_CALL;
92. this.pipControlGroups = [PiPControlGroup.VIDEO_CALL_HANG_UP_BUTTON,
93. PiPControlGroup.VIDEO_CALL_CAMERA_SWITCH, PiPControlGroup.VIDEO_CALL_MICROPHONE_SWITCH];
94. }
95. },
96. {
97. value: '会议',
98. action: () => {
99. this.pipType = PiPWindow.PiPTemplateType.VIDEO_MEETING;
100. this.pipControlGroups = [PiPControlGroup.VIDEO_MEETING_MICROPHONE_SWITCH,
101. PiPControlGroup.VIDEO_MEETING_HANG_UP_BUTTON,
102. PiPControlGroup.VIDEO_MEETING_CAMERA_SWITCH];
103. }
104. },
105. {
106. value: '直播',
107. action: () => {
108. this.pipType = PiPWindow.PiPTemplateType.VIDEO_LIVE;
109. this.pipControlGroups = [PiPControlGroup.VIDEO_LIVE_VIDEO_PLAY_PAUSE,
110. PiPControlGroup.VIDEO_LIVE_MUTE_SWITCH];
111. }
112. }
113. ])
114. }
115. .size({ width: '100%', height: 60 })
116. .backgroundColor('#DDDDDD')
117. .justifyContent(FlexAlign.SpaceAround)
118. .alignRules({
119. top: { anchor: '__container__', align: VerticalAlign.Top },
120. middle: { anchor: '__container__', align: HorizontalAlign.Center }
121. })
122. .id('pip_type_control')
123. XComponent({
124. type: XComponentType.SURFACE,
125. controller: this.mXComponentController
126. })
127. .onLoad(() => {
128. if (this.mXComponentController) {
129. this.surfaceId = this.mXComponentController.getXComponentSurfaceId();
130. }
131. this.player = new AVPlayer(this.surfaceId, 1);
132. this.player.avPlayerFdSrc();
133. })
134. .onDestroy(() => {
135. Logger.info(`[${TAG}] XComponent onDestroy`);
136. })
137. .size({ width: '100%', height: '800px' })
138. .margin({ top: 10 })
139. .backgroundColor('#888888')
140. .alignRules({
141. bottom: { anchor: '__container__', align: VerticalAlign.Center },
142. middle: { anchor: '__container__', align: HorizontalAlign.Center }
143. })
144. .id('x_component')
145. .size({ width: '100%', height: '800px' })
146. Row({ space: 0 }) {
147. Button('创建画中画')
148. .onClick(() => {
149. let windowId: number | undefined = AppStorage.get('windowId');
150. let config: PiPConfig = {
151. mainWindowId: windowId as number,
152. pipTemplateType: this.pipType,
153. width: this.contentWidth,
154. height: this.contentHeight,
155. controlGroup: this.pipControlGroups
156. }
157. this.controllerId = testNapi.createPip(config);
158. testNapi.registerStartPip(this.controllerId, this.changeSurface);
159. testNapi.registerLifecycleListener(this.controllerId, this.onStateChange);
160. })
161. Button('开启画中画')
162. .onClick(() => {
163. testNapi.startPip(this.controllerId);
164. })
165. }
166. .size({ width: '100%', height: 60 })
167. .alignRules({
168. top: { anchor: 'x_component', align: VerticalAlign.Bottom },
169. left: { anchor: '__container__', align: HorizontalAlign.Start }
170. })
171. .id('pip_control')
172. Row({ space: 0 }) {
173. Button('关闭画中画')
174. .onClick(() => {
175. testNapi.stopPip(this.controllerId);
176. })
177. Button('删除控制器')
178. .onClick(() => {
179. testNapi.deletePip(this.controllerId);
180. })
181. }
182. .size({ width: '100%', height: 60 })
183. .alignRules({
184. top: { anchor: 'pip_control', align: VerticalAlign.Bottom },
185. left: { anchor: '__container__', align: HorizontalAlign.Start }
186. })
187. }
188. .size({ width: '100%', height: '100%' })
189. }
190. }
```

以上示例代码对应的示意图如下所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/lKcKhRPITaicoJEVDWPo4g/zh-cn_image_0000002583478181.gif?HW-CC-KV=V1&HW-CC-Date=20260427T234042Z&HW-CC-Expire=86400&HW-CC-Sign=093B028720E6AF695CAA3F7C01E5422D8E7322AC46B278AC2ADE91CB33DA1AE3)
