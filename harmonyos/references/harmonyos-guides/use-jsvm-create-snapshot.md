---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/use-jsvm-create-snapshot
title: 使用JSVM-API接口进行虚拟机快照相关开发
breadcrumb: 指南 > NDK开发 > 代码开发 > 使用JSVM-API实现JS与C/C++语言交互 > JSVM-API使用指导 > 使用JSVM-API接口进行虚拟机快照相关开发
category: harmonyos-guides
scraped_at: 2026-04-28T07:54:15+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:99e59ea6b94bf6c5f25c86a4f7010d13e8b29322dec70053d0516ddca3557b70
---

## 简介

JavaScript虚拟机（JSVM）的快照创建功能，将当前运行时的JavaScript程序状态保存为一个快照文件，这个快照文件包含了当前的堆内存、执行上下文、函数闭包等信息。

## 基本概念

* **虚拟机启动快照**：虚拟机在某个特定时间点的状态快照，包含了当前虚拟机的所有内部状态和数据。通过创建一个启动快照，可以在之后的时间点恢复虚拟机到相同的状态。

创建和使用虚拟机启动快照可以简化一些复杂的编程任务，提高JSVM中虚拟机的管理和维护效率，增强程序的灵活性和稳定性。

## 接口说明

| 接口 | 功能说明 |
| --- | --- |
| OH\_JSVM\_CreateSnapshot | 用于创建虚拟机的启动快照 |
| OH\_JSVM\_CreateEnvFromSnapshot | 基于虚拟机的起始快照，创建一个新的环境 |

## 使用示例

### OH\_JSVM\_CreateSnapshot & OH\_JSVM\_CreateEnvFromSnapshot

用于创建和使用虚拟机的启动快照。

cpp部分代码：

**注意事项**: 需要在OH\_JSVM\_Init的时候，将JSVM对外部的依赖注册到initOptions.externalReferences中。

```
1. // hello.cpp
2. #include "napi/native_api.h"
3. #include "ark_runtime/jsvm.h"
4. #include <hilog/log.h>
5. #include <fstream>

7. #define LOG_DOMAIN 0x0202
8. #define LOG_TAG "TEST_TAG"

10. static int g_aa = 0;

12. #define CHECK_RET(theCall)                                                                           \
13. do {                                                                                             \
14. JSVM_Status cond = theCall;                                                                  \
15. if ((cond) != JSVM_OK) {                                                                     \
16. const JSVM_ExtendedErrorInfo *info;                                                      \
17. OH_JSVM_GetLastErrorInfo(env, &info);                                                    \
18. OH_LOG_ERROR(LOG_APP,                                                                    \
19. "jsvm fail file: %{public}s line: %{public}d ret = %{public}d message = %{public}s", \
20. __FILE__,                                                                            \
21. __LINE__,                                                                            \
22. cond,                                                                                \
23. info != nullptr ? info->errorMessage : "");                                          \
24. return -1;                                                                               \
25. }                                                                                            \
26. } while (0)

28. #define CHECK(theCall)                                                                                              \
29. do {                                                                                                            \
30. JSVM_Status cond = theCall;                                                                                 \
31. if ((cond) != JSVM_OK) {                                                                                    \
32. OH_LOG_ERROR(                                                                                           \
33. LOG_APP, "jsvm fail file: %{public}s line: %{public}d ret = %{public}d", __FILE__, __LINE__, cond); \
34. return -1;                                                                                              \
35. }                                                                                                           \
36. } while (0)

38. // 用于调用theCall并检查其返回值是否为JSVM_OK。
39. // 如果不是，则调用GET_AND_THROW_LAST_ERROR处理错误并返回retVal。
40. #define JSVM_CALL_BASE(env, theCall, retVal)                                                         \
41. do {                                                                                             \
42. JSVM_Status cond = theCall;                                                                  \
43. if (cond != JSVM_OK) {                                                                       \
44. const JSVM_ExtendedErrorInfo *info;                                                      \
45. OH_JSVM_GetLastErrorInfo(env, &info);                                                    \
46. OH_LOG_ERROR(LOG_APP,                                                                    \
47. "jsvm fail file: %{public}s line: %{public}d ret = %{public}d message = %{public}s", \
48. __FILE__,                                                                            \
49. __LINE__,                                                                            \
50. cond,                                                                                \
51. info != nullptr ? info->errorMessage : "");                                          \
52. return retVal;                                                                           \
53. }                                                                                            \
54. } while (0)

56. // JSVM_CALL_BASE的简化版本，返回nullptr
57. #define JSVM_CALL(theCall) JSVM_CALL_BASE(env, theCall, nullptr)

59. static const int MAX_BUFFER_SIZE = 128;
60. // CreateHelloString()函数需绑定到JSVM虚拟机, 用于OH_JSVM_CreateSnapshot虚拟机快照的正常创建
61. static JSVM_Value CreateHelloString(JSVM_Env env, JSVM_CallbackInfo info)
62. {
63. JSVM_Value outPut;
64. OH_JSVM_CreateStringUtf8(env, "Hello world!", JSVM_AUTO_LENGTH, &outPut);
65. return outPut;
66. }
67. // 提供外部引用的方式以便JavaScript环境可以调用绑定的函数
68. static JSVM_CallbackStruct helloCb = {CreateHelloString, nullptr};

70. static intptr_t externals[] = {
71. (intptr_t)&helloCb,
72. 0,
73. };

75. static JSVM_Value RunVMScript(JSVM_Env env, std::string &src)
76. {
77. // 打开handleScope作用域
78. JSVM_HandleScope handleScope;
79. OH_JSVM_OpenHandleScope(env, &handleScope);
80. JSVM_Value jsStr = nullptr;
81. OH_JSVM_CreateStringUtf8(env, src.c_str(), src.size(), &jsStr);
82. // 编译JavaScript代码
83. JSVM_Script script;
84. OH_JSVM_CompileScript(env, jsStr, nullptr, 0, true, nullptr, &script);
85. // 执行JavaScript代码
86. JSVM_Value result = nullptr;
87. OH_JSVM_RunScript(env, script, &result);
88. // 关闭handleScope作用域
89. OH_JSVM_CloseHandleScope(env, handleScope);
90. return result;
91. }
92. // OH_JSVM_CreateSnapshot的样例方法
93. static void CreateVMSnapshot()
94. {
95. // 创建JavaScript虚拟机实例,打开虚拟机作用域
96. JSVM_VM vm;
97. JSVM_CreateVMOptions vmOptions;
98. memset(&vmOptions, 0, sizeof(vmOptions));
99. // isForSnapshotting设置该虚拟机是否用于创建快照
100. vmOptions.isForSnapshotting = true;
101. OH_JSVM_CreateVM(&vmOptions, &vm);
102. JSVM_VMScope vmScope;
103. OH_JSVM_OpenVMScope(vm, &vmScope);
104. // 创建JavaScript环境,打开环境作用域
105. JSVM_Env env;
106. // 将native函数注册成JavaScript可调用的方法
107. JSVM_PropertyDescriptor descriptor[] = {
108. {"createHelloString", nullptr, &helloCb, nullptr, nullptr, nullptr, JSVM_DEFAULT},
109. };
110. OH_JSVM_CreateEnv(vm, 1, descriptor, &env);
111. JSVM_EnvScope envScope;
112. OH_JSVM_OpenEnvScope(env, &envScope);
113. // 使用OH_JSVM_CreateSnapshot创建虚拟机的启动快照
114. const char *blobData = nullptr;
115. size_t blobSize = 0;
116. JSVM_Env envs[1] = {env};
117. OH_JSVM_CreateSnapshot(vm, 1, envs, &blobData, &blobSize);
118. // 将snapshot保存到文件中
119. // 保存快照数据，/data/storage/el2/base/files/test_blob.bin为沙箱路径
120. // 以包名为com.example.jsvm为例，实际文件会保存到/data/app/el2/100/base/com.example.jsvm/files/test_blob.bin
121. std::ofstream file(
122. "/data/storage/el2/base/files/test_blob.bin", std::ios::out | std::ios::binary | std::ios::trunc);
123. file.write(blobData, blobSize);
124. file.close();
125. // 关闭并销毁环境和虚拟机
126. OH_JSVM_CloseEnvScope(env, envScope);
127. OH_JSVM_DestroyEnv(env);
128. OH_JSVM_CloseVMScope(vm, vmScope);
129. OH_JSVM_DestroyVM(vm);
130. }

132. static void RunVMSnapshot()
133. {
134. // blobData的生命周期不能短于vm的生命周期
135. // 从文件中读取snapshot
136. std::vector<char> blobData;
137. std::ifstream file("/data/storage/el2/base/files/test_blob.bin", std::ios::in | std::ios::binary | std::ios::ate);
138. size_t blobSize = file.tellg();
139. blobData.resize(blobSize);
140. file.seekg(0, std::ios::beg);
141. file.read(blobData.data(), blobSize);
142. file.close();
143. OH_LOG_INFO(LOG_APP, "Test JSVM RunVMSnapshot read file blobSize = : %{public}ld", blobSize);
144. // 使用快照数据创建虚拟机实例
145. JSVM_VM vm;
146. JSVM_CreateVMOptions vmOptions;
147. memset(&vmOptions, 0, sizeof(vmOptions));
148. vmOptions.snapshotBlobData = blobData.data();
149. vmOptions.snapshotBlobSize = blobSize;
150. OH_JSVM_CreateVM(&vmOptions, &vm);
151. JSVM_VMScope vmScope;
152. OH_JSVM_OpenVMScope(vm, &vmScope);
153. // 从快照中创建环境env
154. JSVM_Env env;
155. OH_JSVM_CreateEnvFromSnapshot(vm, 0, &env);
156. JSVM_EnvScope envScope;
157. OH_JSVM_OpenEnvScope(env, &envScope);
158. // 执行js脚本，快照记录的env中定义了createHelloString()
159. std::string src = "createHelloString()";
160. JSVM_Value result = RunVMScript(env, src);
161. // 环境关闭前检查脚本运行结果
162. char str[MAX_BUFFER_SIZE];
163. OH_JSVM_GetValueStringUtf8(env, result, str, MAX_BUFFER_SIZE, nullptr);
164. if (strcmp(str, "Hello world!") != 0) {
165. OH_LOG_ERROR(LOG_APP, "jsvm fail file: %{public}s line: %{public}d", __FILE__, __LINE__);
166. }
167. // 关闭并销毁环境和虚拟机
168. OH_JSVM_CloseEnvScope(env, envScope);
169. OH_JSVM_DestroyEnv(env);
170. OH_JSVM_CloseVMScope(vm, vmScope);
171. OH_JSVM_DestroyVM(vm);
172. return;
173. }

175. static JSVM_Value AdjustExternalMemory(JSVM_Env env, JSVM_CallbackInfo info)
176. {
177. // 在创建虚拟机快照时，如果存在对外部的依赖，需要在OH_JSVM_Init时，将外部依赖注册到initOptions.externalReferences中
178. // 创建虚拟机快照并将快照保存到文件中
179. CreateVMSnapshot();
180. // snapshot可以记录下特定的js执行环境，可以跨进程通过snapshot快速还原出js执行上下文环境
181. RunVMSnapshot();
182. JSVM_Value result = nullptr;
183. OH_JSVM_CreateInt32(env, 0, &result);
184. return result;
185. }

187. static JSVM_CallbackStruct param[] = {
188. {.data = nullptr, .callback = AdjustExternalMemory},
189. };
190. static JSVM_CallbackStruct *method = param;
191. // AdjustExternalMemory方法别名，供JS调用
192. static JSVM_PropertyDescriptor descriptor[] = {
193. {"adjustExternalMemory", nullptr, method, nullptr, nullptr, nullptr, JSVM_DEFAULT},
194. };

196. // 样例测试JS
197. const char *srcCallNative = R"JS(adjustExternalMemory();)JS";

199. static int32_t TestJSVM()
200. {
201. JSVM_InitOptions initOptions = {0};
202. JSVM_VM vm;
203. JSVM_Env env = nullptr;
204. JSVM_VMScope vmScope;
205. JSVM_EnvScope envScope;
206. JSVM_HandleScope handleScope;
207. JSVM_Value result;
208. // 初始化JavaScript引擎实例
209. if (g_aa == 0) {
210. g_aa++;
211. initOptions.externalReferences = externals;
212. int argc = 0;
213. char **argv = nullptr;
214. initOptions.argc = &argc;
215. initOptions.argv = argv;
216. CHECK(OH_JSVM_Init(&initOptions));
217. }
218. // 创建JSVM环境
219. CHECK(OH_JSVM_CreateVM(nullptr, &vm));
220. CHECK(OH_JSVM_CreateEnv(vm, sizeof(descriptor) / sizeof(descriptor[0]), descriptor, &env));
221. CHECK(OH_JSVM_OpenVMScope(vm, &vmScope));
222. CHECK_RET(OH_JSVM_OpenEnvScope(env, &envScope));
223. CHECK_RET(OH_JSVM_OpenHandleScope(env, &handleScope));

225. // 通过script调用测试函数
226. JSVM_Script script;
227. JSVM_Value jsSrc;
228. CHECK_RET(OH_JSVM_CreateStringUtf8(env, srcCallNative, JSVM_AUTO_LENGTH, &jsSrc));
229. CHECK_RET(OH_JSVM_CompileScript(env, jsSrc, nullptr, 0, true, nullptr, &script));
230. CHECK_RET(OH_JSVM_RunScript(env, script, &result));

232. // 销毁JSVM环境
233. CHECK_RET(OH_JSVM_CloseHandleScope(env, handleScope));
234. CHECK_RET(OH_JSVM_CloseEnvScope(env, envScope));
235. CHECK(OH_JSVM_CloseVMScope(vm, vmScope));
236. CHECK(OH_JSVM_DestroyEnv(env));
237. CHECK(OH_JSVM_DestroyVM(vm));
238. return 0;
239. }

241. static napi_value RunTest(napi_env env, napi_callback_info info)
242. {
243. TestJSVM();
244. return nullptr;
245. }

247. EXTERN_C_START
248. static napi_value Init(napi_env env, napi_value exports)
249. {
250. OH_LOG_INFO(LOG_APP, "JSVM Init");
251. napi_property_descriptor desc[] = {
252. {"runTest", nullptr, RunTest, nullptr, nullptr, nullptr, napi_default, nullptr},
253. };

255. napi_define_properties(env, exports, sizeof(desc) / sizeof(desc[0]), desc);
256. return exports;
257. }
258. EXTERN_C_END

260. static napi_module demoModule = {
261. .nm_version = 1,
262. .nm_flags = 0,
263. .nm_filename = nullptr,
264. .nm_register_func = Init,
265. .nm_modname = "entry",
266. .nm_priv = ((void *)0),
267. .reserved = {0},
268. };

270. extern "C" __attribute__((constructor)) void RegisterEntryModule(void) { napi_module_register(&demoModule); }
```

ArkTS侧示例代码：

```
1. import napitest from 'libentry.so';

3. @Entry
4. @Component
5. struct Index {
6. @State message: string = 'Hello World';

8. build() {
9. Row() {
10. Column() {
11. Text(this.message)
12. .fontSize(50)
13. .fontWeight(FontWeight.Bold)
14. .onClick(() => {
15. // runtest
16. napitest.runTest();
17. })
18. }
19. .width('100%')
20. }
21. .height('100%')
22. }
23. }
```

执行结果

在LOG中输出：

```
1. Test JSVM RunVMSnapshot read file blobSize = : 300064
```

多次点击屏幕,LOG中输出:

```
1. Test JSVM RunVMSnapshot read file blobSize = : 300176
2. Test JSVM RunVMSnapshot read file blobSize = : 300064
3. Test JSVM RunVMSnapshot read file blobSize = : 300160
4. Test JSVM RunVMSnapshot read file blobSize = : 300032
5. Test JSVM RunVMSnapshot read file blobSize = : 300176
6. Test JSVM RunVMSnapshot read file blobSize = : 300048
```

上述执行结果是因为在读取快照文件时，blobSize 的值来源于快照文件的大小（通过 file.tellg() 获取）。快照文件的大小直接决定了 blobSize 的值，所以会输出不同的值。
