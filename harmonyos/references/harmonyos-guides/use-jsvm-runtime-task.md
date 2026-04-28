---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/use-jsvm-runtime-task
title: 使用JSVM-API接口创建多个引擎执行JS代码并销毁
breadcrumb: 指南 > NDK开发 > 代码开发 > 使用JSVM-API实现JS与C/C++语言交互 > JSVM-API典型使用场景指导 > JSVM-API调优&高性能使用示例 > 使用JSVM-API接口创建多个引擎执行JS代码并销毁
category: harmonyos-guides
scraped_at: 2026-04-28T07:54:27+08:00
doc_updated_at: 2026-03-17
content_hash: sha256:5498bc244abd126ae9c56aa26713e6cf37340af55759765578beed90d61cb888
---

## 场景介绍

开发者通过createJsCore方法来创建一个新的JS运行时环境，并通过该方法获得一个CoreID。然后，通过evaluateJS方法使用CoreID对应的运行环境来运行JS代码，在JS代码中创建promise并异步执行函数。最后，使用releaseJsCore方法来销毁CoreID对应的运行环境。

## 使用示例

JSVM-API接口开发流程参考[使用JSVM-API实现JS与C/C++语言交互开发流程](use-jsvm-process.md)，本文仅对接口对应C++相关代码进行展示。

创建多个JS运行时环境并运行JS代码

```
1. #include <map>
2. #include <mutex>
3. #include <deque>
4. using namespace std;
5. // 定义map管理每个独立vm环境
6. static map<int, JSVM_VM *> g_vmMap;
7. static map<int, JSVM_Env *> g_envMap;
8. static map<int, JSVM_CallbackStruct *> g_callBackStructMap;
9. static uint32_t ENVTAG_NUMBER = 0;
10. static std::mutex envMapLock;
11. static int g_aa = 0;

13. #define CHECK_COND(cond)                                                                                               \
14. do {                                                                                                               \
15. if (!(cond)) {                                                                                                 \
16. OH_LOG_ERROR(LOG_APP, "jsvm fail file: %{public}s line: %{public}d ret = false", __FILE__, __LINE__);      \
17. return -1;                                                                                                 \
18. }                                                                                                              \
19. } while (0)

21. class Task {
22. public:
23. virtual ~Task() = default;
24. virtual void Run() = 0;
25. };
26. static map<int, deque<Task *>> g_taskQueueMap;

28. // 自定义ConsoleInfo方法
29. static JSVM_Value ConsoleInfo(JSVM_Env env, JSVM_CallbackInfo info) {
30. size_t argc = 1;
31. JSVM_Value args[1];
32. char log[256] = "";
33. size_t log_length = 0;
34. JSVM_CALL(OH_JSVM_GetCbInfo(env, info, &argc, args, NULL, NULL));

36. JSVM_CALL(OH_JSVM_GetValueStringUtf8(env, args[0], log, 255, &log_length));
37. log[255] = 0;
38. OH_LOG_INFO(LOG_APP, "JSVM API TEST: %{public}s", log);
39. return nullptr;
40. }

42. // 自定义创建Promise方法用以在JS代码中创建Promise
43. static JSVM_Value CreatePromise(JSVM_Env env, JSVM_CallbackInfo info) {
44. OH_LOG_INFO(LOG_APP, "JSVM API TEST: CreatePromise start");
45. int envID = -1;
46. // 通过当前env获取envID
47. for (auto it = g_envMap.begin(); it != g_envMap.end(); ++it) {
48. if (*it->second == env) {
49. envID = it->first;
50. break;
51. }
52. }
53. if (envID == -1) {
54. OH_LOG_ERROR(LOG_APP, "JSVM API TEST: CreatePromise envID failed");
55. return nullptr;
56. }
57. JSVM_Value promise;
58. JSVM_Deferred deferred;
59. JSVM_CALL(OH_JSVM_CreatePromise(env, &deferred, &promise));
60. // 设计ReadTask类用以将promise对象的deferred加入执行队列
61. class ReadTask : public Task {
62. public:
63. ReadTask(JSVM_Env env, JSVM_Deferred deferred, int envNum) : env_(env), envID_(envNum), deferred_(deferred) {}
64. void Run() override {
65. // string str = "TEST RUN OH_JSVM_ResolveDeferred";
66. int envID = 0;
67. for (auto it = g_envMap.begin(); it != g_envMap.end(); ++it) {
68. if (*it->second == env_) {
69. envID = it->first;
70. break;
71. }
72. }
73. OH_LOG_INFO(LOG_APP, "JSVM API TEST: CreatePromise %{public}d", envID);
74. JSVM_Value result;
75. if (OH_JSVM_CreateInt32(env_, envID, &result) != JSVM_OK) {
76. return;
77. }
78. if (OH_JSVM_ResolveDeferred(env_, deferred_, result) != JSVM_OK) {
79. return;
80. }
81. }

83. private:
84. JSVM_Env env_;
85. int envID_;
86. JSVM_Deferred deferred_;
87. };
88. g_taskQueueMap[envID].push_back(new ReadTask(env, deferred, envID));
89. OH_LOG_INFO(LOG_APP, "JSVM API TEST: CreatePromise end");
90. return promise;
91. }

93. // 自定义Add方法
94. static JSVM_Value Add(JSVM_Env env, JSVM_CallbackInfo info) {
95. size_t argc = 2;
96. JSVM_Value args[2];
97. JSVM_CALL(OH_JSVM_GetCbInfo(env, info, &argc, args, NULL, NULL));
98. double num1 = 0, num2 = 0;
99. JSVM_CALL(OH_JSVM_GetValueDouble(env, args[0], &num1));
100. JSVM_CALL(OH_JSVM_GetValueDouble(env, args[1], &num2));
101. JSVM_Value sum = nullptr;
102. JSVM_CALL(OH_JSVM_CreateDouble(env, num1 + num2, &sum));
103. return sum;
104. }

106. // 自定义AssertEqual方法
107. static JSVM_Value AssertEqual(JSVM_Env env, JSVM_CallbackInfo info) {
108. size_t argc = 2;
109. JSVM_Value args[2];
110. JSVM_CALL(OH_JSVM_GetCbInfo(env, info, &argc, args, NULL, NULL));

112. bool isStrictEquals = false;
113. JSVM_CALL(OH_JSVM_StrictEquals(env, args[0], args[1], &isStrictEquals));

115. if (isStrictEquals) {
116. OH_LOG_INFO(LOG_APP, "JSVM API TEST RESULT: PASS");
117. } else {
118. OH_LOG_INFO(LOG_APP, "JSVM API TEST RESULT: FAILED");
119. }
120. return nullptr;
121. }

123. static int fromOHStringValue(JSVM_Env &env, JSVM_Value &value, std::string &result) {
124. size_t size = 0;
125. CHECK_RET(OH_JSVM_GetValueStringUtf8(env, value, nullptr, 0, &size));
126. char *resultStr = new char[size + 1];
127. CHECK_RET(OH_JSVM_GetValueStringUtf8(env, value, resultStr, size + 1, &size));
128. result = resultStr;
129. delete[] resultStr;
130. return 0;
131. }

133. // 提供创建JSVM运行环境的对外接口并返回对应唯一ID
134. static int CreateJsCore(uint32_t *result) {
135. OH_LOG_INFO(LOG_APP, "JSVM CreateJsCore START");
136. g_taskQueueMap[ENVTAG_NUMBER] = deque<Task *>{};

138. if (g_aa == 0) {
139. JSVM_InitOptions init_options;
140. memset(&init_options, 0, sizeof(init_options));
141. CHECK(OH_JSVM_Init(&init_options));
142. g_aa++;
143. }
144. std::lock_guard<std::mutex> lock_guard(envMapLock);

146. // 虚拟机实例
147. g_vmMap[ENVTAG_NUMBER] = new JSVM_VM;
148. JSVM_CreateVMOptions options;
149. JSVM_VMScope vmScope;
150. memset(&options, 0, sizeof(options));
151. CHECK(OH_JSVM_CreateVM(&options, g_vmMap[ENVTAG_NUMBER]));
152. CHECK(OH_JSVM_OpenVMScope(*g_vmMap[ENVTAG_NUMBER], &vmScope));

154. // 新环境
155. g_envMap[ENVTAG_NUMBER] = new JSVM_Env;
156. g_callBackStructMap[ENVTAG_NUMBER] = new JSVM_CallbackStruct[4];

158. // 注册用户提供的本地函数的回调函数指针和数据，通过JSVM-API暴露给js
159. for (int i = 0; i < 4; i++) {
160. g_callBackStructMap[ENVTAG_NUMBER][i].data = nullptr;
161. }
162. g_callBackStructMap[ENVTAG_NUMBER][0].callback = ConsoleInfo;
163. g_callBackStructMap[ENVTAG_NUMBER][1].callback = Add;
164. g_callBackStructMap[ENVTAG_NUMBER][2].callback = AssertEqual;
165. g_callBackStructMap[ENVTAG_NUMBER][3].callback = CreatePromise;
166. JSVM_PropertyDescriptor descriptors[] = {
167. {"consoleinfo", NULL, &g_callBackStructMap[ENVTAG_NUMBER][0], NULL, NULL, NULL, JSVM_DEFAULT},
168. {"add", NULL, &g_callBackStructMap[ENVTAG_NUMBER][1], NULL, NULL, NULL, JSVM_DEFAULT},
169. {"assertEqual", NULL, &g_callBackStructMap[ENVTAG_NUMBER][2], NULL, NULL, NULL, JSVM_DEFAULT},
170. {"createPromise", NULL, &g_callBackStructMap[ENVTAG_NUMBER][3], NULL, NULL, NULL, JSVM_DEFAULT},
171. };
172. CHECK(OH_JSVM_CreateEnv(*g_vmMap[ENVTAG_NUMBER], sizeof(descriptors) / sizeof(descriptors[0]), descriptors,
173. g_envMap[ENVTAG_NUMBER]));
174. CHECK(OH_JSVM_CloseVMScope(*g_vmMap[ENVTAG_NUMBER], vmScope));

176. OH_LOG_INFO(LOG_APP, "JSVM CreateJsCore END");
177. *result = ENVTAG_NUMBER;
178. ENVTAG_NUMBER++;
179. return 0;
180. }

182. // 对外提供释放JSVM环境接口，通过envId释放对应环境
183. static int ReleaseJsCore(uint32_t coreEnvId) {
184. std::lock_guard<std::mutex> lock_guard(envMapLock);

186. OH_LOG_INFO(LOG_APP, "JSVM ReleaseJsCore START");
187. CHECK_COND(g_envMap.count(coreEnvId) != 0 && g_envMap[coreEnvId] != nullptr);

189. CHECK(OH_JSVM_DestroyEnv(*g_envMap[coreEnvId]));
190. g_envMap[coreEnvId] = nullptr;
191. g_envMap.erase(coreEnvId);
192. CHECK(OH_JSVM_DestroyVM(*g_vmMap[coreEnvId]));
193. g_vmMap[coreEnvId] = nullptr;
194. g_vmMap.erase(coreEnvId);
195. delete[] g_callBackStructMap[coreEnvId];
196. g_callBackStructMap[coreEnvId] = nullptr;
197. g_callBackStructMap.erase(coreEnvId);
198. g_taskQueueMap.erase(coreEnvId);

200. OH_LOG_INFO(LOG_APP, "JSVM ReleaseJsCore END");
201. return 0;
202. }

204. static std::mutex mutexLock;
205. // 对外提供执行JS代码接口，通过coreID在对应的JSVM环境中执行JS代码
206. static int EvaluateJS(uint32_t envId, const char *source, std::string &res) {
207. OH_LOG_INFO(LOG_APP, "JSVM EvaluateJS START");

209. CHECK_COND(g_envMap.count(envId) != 0 && g_envMap[envId] != nullptr);

211. JSVM_Env env = *g_envMap[envId];
212. JSVM_VM vm = *g_vmMap[envId];
213. JSVM_VMScope vmScope;
214. JSVM_EnvScope envScope;
215. JSVM_HandleScope handleScope;
216. JSVM_Value result;

218. std::lock_guard<std::mutex> lock_guard(mutexLock);
219. {
220. // 创建JSVM环境
221. CHECK_RET(OH_JSVM_OpenVMScope(vm, &vmScope));
222. CHECK_RET(OH_JSVM_OpenEnvScope(*g_envMap[envId], &envScope));
223. CHECK_RET(OH_JSVM_OpenHandleScope(*g_envMap[envId], &handleScope));

225. // 通过script调用测试函数
226. JSVM_Script script;
227. JSVM_Value jsSrc;
228. CHECK_RET(OH_JSVM_CreateStringUtf8(env, source, JSVM_AUTO_LENGTH, &jsSrc));
229. CHECK_RET(OH_JSVM_CompileScript(env, jsSrc, nullptr, 0, true, nullptr, &script));
230. CHECK_RET(OH_JSVM_RunScript(env, script, &result));

232. JSVM_ValueType type;
233. CHECK_RET(OH_JSVM_Typeof(env, result, &type));
234. OH_LOG_INFO(LOG_APP, "JSVM API TEST type: %{public}d", type);
235. // Execute tasks in the current env event queue
236. while (!g_taskQueueMap[envId].empty()) {
237. auto task = g_taskQueueMap[envId].front();
238. g_taskQueueMap[envId].pop_front();
239. task->Run();
240. delete task;
241. }

243. if (type == JSVM_STRING) {
244. CHECK_COND(fromOHStringValue(env, result, res) != -1);
245. } else if (type == JSVM_BOOLEAN) {
246. bool ret = false;
247. CHECK_RET(OH_JSVM_GetValueBool(env, result, &ret));
248. ret ? res = "true" : res = "false";
249. } else if (type == JSVM_NUMBER) {
250. int32_t num = 0;
251. CHECK_RET(OH_JSVM_GetValueInt32(env, result, &num));
252. res = std::to_string(num);
253. } else if (type == JSVM_OBJECT) {
254. JSVM_Value objResult;
255. CHECK_RET(OH_JSVM_JsonStringify(env, result, &objResult));
256. CHECK_COND(fromOHStringValue(env, objResult, res) != -1);
257. }
258. }
259. {
260. bool aal = false;
261. CHECK_RET(OH_JSVM_PumpMessageLoop(*g_vmMap[envId], &aal));
262. CHECK_RET(OH_JSVM_PerformMicrotaskCheckpoint(*g_vmMap[envId]));
263. CHECK_RET(OH_JSVM_CloseHandleScope(*g_envMap[envId], handleScope));
264. CHECK_RET(OH_JSVM_CloseEnvScope(*g_envMap[envId], envScope));
265. CHECK_RET(OH_JSVM_CloseVMScope(*g_vmMap[envId], vmScope));
266. }
267. OH_LOG_INFO(LOG_APP, "JSVM EvaluateJS END");
268. return 0;
269. }

271. static int32_t TestJSVM() {
272. const char source1[] = "{\
273. let a = \"hello World\";\
274. consoleinfo(a);\
275. const mPromise = createPromise();\
276. mPromise.then((result) => {\
277. assertEqual(result, 0);\
278. });\
279. a;\
280. };";

282. const char source2[] = "{\
283. let a = \"second hello\";\
284. consoleinfo(a);\
285. let b = add(99, 1);\
286. assertEqual(100, b);\
287. assertEqual(add(99, 1), 100);\
288. createPromise().then((result) => {\
289. assertEqual(result, 1);\
290. });\
291. a;\
292. };";

294. // 创建首个运行环境，并绑定TS回调
295. uint32_t coreId1 = 0;
296. CHECK_COND(CreateJsCore(&coreId1) == 0);
297. OH_LOG_INFO(LOG_APP, "TEST coreId: %{public}d", coreId1);
298. // 在首个运行环境中执行JS代码
299. std::string result1;
300. CHECK_COND(EvaluateJS(coreId1, source1, result1) == 0);
301. OH_LOG_INFO(LOG_APP, "TEST evaluateJS: %{public}s", result1.c_str());

303. // 创建第二个运行环境，并绑定TS回调
304. uint32_t coreId2 = 0;
305. CHECK_COND(CreateJsCore(&coreId2) == 0);
306. OH_LOG_INFO(LOG_APP, "TEST coreId: %{public}d", coreId2);
307. // 在第二个运行环境中执行JS代码
308. std::string result2;
309. CHECK_COND(EvaluateJS(coreId2, source2, result2) == 0);
310. OH_LOG_INFO(LOG_APP, "TEST evaluateJS: %{public}s", result2.c_str());

312. // 释放首个运行环境
313. CHECK_COND(ReleaseJsCore(coreId1) == 0);
314. // 释放第二个运行环境
315. CHECK_COND(ReleaseJsCore(coreId2) == 0);
316. OH_LOG_INFO(LOG_APP, "Test NAPI end");

318. return 0;
319. }
```

预计的输出结果：

```
1. JSVM CreateJsCore START
2. JSVM CreateJsCore END
3. TEST coreId: 0
4. JSVM EvaluateJS START
5. JSVM API TEST: hello World
6. JSVM API TEST: CreatePromise start
7. JSVM API TEST: CreatePromise end
8. JSVM API TEST type: 4
9. JSVM API TEST: CreatePromise 0
10. JSVM API TEST RESULT: PASS
11. JSVM EvaluateJS END
12. TEST evaluateJS: hello World
13. JSVM CreateJsCore START
14. JSVM CreateJsCore END
15. TEST coreId: 1
16. JSVM EvaluateJS START
17. JSVM API TEST: second hello
18. JSVM API TEST RESULT: PASS
19. JSVM API TEST RESULT: PASS
20. JSVM API TEST: CreatePromise start
21. JSVM API TEST: CreatePromise end
22. JSVM API TEST type: 4
23. JSVM API TEST: CreatePromise 1
24. JSVM API TEST RESULT: PASS
25. JSVM EvaluateJS END
26. TEST evaluateJS: second hello
27. JSVM ReleaseJsCore START
28. JSVM ReleaseJsCore END
29. JSVM ReleaseJsCore START
30. JSVM ReleaseJsCore END
31. Test NAPI end
```
