---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/use-napi-about-crash
title: 使用Node-API接口产生的异常日志/崩溃分析
breadcrumb: 指南 > NDK开发 > 代码开发 > 使用Node-API实现ArkTS/JS与C/C++语言交互 > Node-API典型使用场景 > 使用Node-API接口产生的异常日志/崩溃分析
category: harmonyos-guides
scraped_at: 2026-04-28T07:54:11+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:5bdafd280ad935e9ade659071089f0a4cb3fc4d837bcc62df1885e550c08c8b4
---

以下维测手段多数依赖于ArkTS运行时的多线程检测能力，因此建议在调试前启用此功能。启用方法参考文档[分析CppCrash（进程崩溃）](ide-multi-thread-check.md)。

若无特殊说明，本章节描述的维测手段会在启用ArkTS运行时多线程检测开关的情况下，立即中断进程。

## 数据在使用时，与创建该数据时所使用的env不一致

### 各问题场景的关键日志

该维测手段主要包含以下两种场景：

1. 调用napi方法的入参napi\_env与创建napi数据结构时所使用的napi\_env不一致。

   **关键日志**

   param env not equal to its owner.
2. 调用napi方法的入参napi\_env与创建napi数据结构时所使用的napi\_env一致，但原始napi\_env已释放。

   **关键日志**

   1. 除线程安全函数相关方法外，关键日志如下：

      owner env has been destroyed, owner id: <owner id> , current env id: <current id>.
   2. 线程安全函数相关方法，关键日志如下：

      current tsfn was created by dead env, owner id: <owner id>, current env id: <current id>

该维测手段当前的覆盖范围如下：

1. napi\_get\_reference\_value
2. napi\_delete\_reference\*
3. napi\_queue\_async\_work
4. napi\_queue\_async\_work\_with\_qos
5. napi\_cancel\_async\_work
6. napi\_call\_threadsafe\_function\*
7. napi\_release\_threadsafe\_function\*

具有\*标志的接口，仅能触发第二种场景的维测信息，不含有\*标志的接口，能触发以上两种场景的维测信息。

### 案例及示例代码

注意

下面的代码仅用于构造异常场景，触发异常分支的DFX日志。在充分理解其意图前，请勿将其应用到业务场景中。

**基础工具类**

定义一个工具类，便于在后续构造两种异常场景。

```
1. #define CHECK(cond)                                                 \
2. do {                                                            \
3. if (!(cond)) {                                                 \
4. OH_LOG_FATAL(LOG_APP, "Failed to check `" #cond "`");   \
5. std::abort();                                           \
6. }                                                           \
7. } while(0)
8. #define CHECK_EQ(lhs, rhs) CHECK(lhs == rhs)
9. #define CHECK_NE(lhs, rhs) CHECK(lhs != rhs)
10. #define CHECK_NOT_NULL(val) CHECK(val != nullptr)

12. #define STRICT_NAPI_CALL(call)                                      \
13. do {                                                            \
14. napi_status ret = (call);                                   \
15. if (ret != napi_ok) {                                       \
16. OH_LOG_FATAL(LOG_APP, "Failed to execute `" #call "`, " \
17. "return code is: %{public}d", ret);                 \
18. std::abort();                                           \
19. }                                                           \
20. } while(0)

23. class CallbackInfo {
24. public:
25. CallbackInfo(napi_env env, napi_callback_info info)
26. : env_(env)
27. {
28. napi_get_cb_info(env, info, &argc_, nullptr, &thisVar_, &data_);
29. if (argc_ > 0) {
30. argv_ = new napi_value[argc_];
31. CHECK_NOT_NULL(argv_);
32. memset(argv_, 0, sizeof(argv_));
33. napi_get_cb_info(env, info, &argc_, argv_, nullptr, nullptr);
34. }
35. }
36. ~CallbackInfo()
37. {
38. if (argc_ > 0) {
39. delete[] argv_;
40. argv_ = nullptr;
41. }
42. }

44. inline size_t GetArgc() const { return argc_; }
45. inline napi_value* GetArgs() const { return argv_; }

47. inline napi_value GetArg(size_t index) const
48. {
49. if (index >= argc_) {
50. napi_value undefined = nullptr;
51. napi_get_undefined(env_, &undefined);
52. return undefined;
53. }
54. return argv_[index];
55. }
56. inline napi_value operator[](size_t index) const
57. {
58. return GetArg(index);
59. }

61. private:
62. napi_env env_ { nullptr };
63. size_t argc_ { 0 };
64. napi_value* argv_ { nullptr };
65. napi_value thisVar_ { nullptr };
66. void* data_ { nullptr };
67. };

69. // 构造相同（或不同）地址的napi_env，以便能触发不同的DFX信息
70. class EngineProxy {
71. public:
72. EngineProxy()
73. {
74. STRICT_NAPI_CALL(napi_create_ark_runtime(&env_));
75. // 5: 使napi_env地址复用更容易
76. for (int i = 0; i < 5; i++) {
77. RecreateOnce();
78. }
79. }

81. ~EngineProxy()
82. {
83. STRICT_NAPI_CALL(napi_destroy_ark_runtime(&env_));
84. }

86. inline bool RecreateSame()
87. {
88. return Recreate(true);
89. }

91. inline bool RecreateDiff()
92. {
93. return Recreate(false);
94. }

96. inline operator napi_env() const
97. {
98. return env_;
99. }

101. // 重新创建napi_env，直到地址与原始env相同（或不同）
102. bool Recreate(bool requireSame)
103. {
104. const char* recreateTypeTag = requireSame ? "same" : "different";
105. napi_env old = env_;
106. for (int i = 0; i < MAX_RETRY_TIMES; i++) {
107. if (RecreateOnce(old) == requireSame) {
108. OH_LOG_INFO(LOG_APP, "Succeed to recreate env with %{public}s pointer "
109. "address after retried %{public}d times.", recreateTypeTag, i);
110. return true;
111. }
112. }
113. OH_LOG_ERROR(LOG_APP, "Failed to recreate env with %{public}s pointer "
114. "address after retried %{public}d times.", recreateTypeTag, MAX_RETRY_TIMES);
115. return false;
116. }

118. private:
119. // 重新创建napi_env，返回新地址是否与原地址相同
120. bool RecreateOnce(napi_env old = nullptr)
121. {
122. STRICT_NAPI_CALL(napi_destroy_ark_runtime(&env_));
123. STRICT_NAPI_CALL(napi_create_ark_runtime(&env_));
124. return env_ == old;
125. }

127. napi_env env_ {nullptr};

129. constexpr static int MAX_RETRY_TIMES = 1 << 8;
130. };
```

**napi\_ref相关接口**

napi\_get\_reference\_value 和 napi\_delete\_reference 的示例代码

```
1. /*
2. * 接口声明 index.d.ts
3. * const triggerDFXGetRef: (samePtr: boolean) => void;
4. */
5. napi_value TriggerDFXGetRef(napi_env env, napi_callback_info cbinfo)
6. {
7. CallbackInfo info(env, cbinfo);
8. bool same = true;
9. STRICT_NAPI_CALL(napi_get_value_bool(env, info[0], &same));
10. std::thread([](bool same) {
11. EngineProxy localEnv;
12. napi_value obj = nullptr;
13. STRICT_NAPI_CALL(napi_create_object(localEnv, &obj));
14. napi_ref ref = nullptr;
15. // napi_create_reference为js对象创建了强引用，需要使用napi_delete_reference主动销毁，否则会导致js对象无法被回收，造成内存泄漏
16. napi_create_reference(localEnv, obj, 1, &ref);
17. if (!localEnv.Recreate(same)) {
18. if (ref != nullptr) {
19. napi_delete_reference(localEnv, ref);
20. }
21. return;
22. }
23. napi_value result = nullptr;
24. napi_get_reference_value(localEnv, ref, &result);
25. if (ref != nullptr) {
26. napi_delete_reference(localEnv, ref);
27. }
28. }, same).detach();
29. return nullptr;
30. }

32. /*
33. * 接口声明 index.d.ts
34. * const triggerDFXDelRef: () => void;
35. */
36. napi_value TriggerDFXDelRef(napi_env, napi_callback_info info)
37. {
38. std::thread([]() {
39. EngineProxy localEnv;
40. napi_value obj = nullptr;
41. STRICT_NAPI_CALL(napi_create_object(localEnv, &obj));
42. napi_ref ref = nullptr;
43. // 在使用完成后调用napi_delete_reference来释放引用，避免内存泄露
44. napi_create_reference(localEnv, obj, 1, &ref);
45. if (!localEnv.RecreateSame()) {
46. if (ref != nullptr) {
47. napi_delete_reference(localEnv, ref);
48. }
49. return;
50. };
51. if (ref != nullptr) {
52. napi_delete_reference(localEnv, ref);
53. }
54. }).detach();
55. return nullptr;
56. }
```

**napi\_async\_work相关接口**

napi\_queue\_async\_work、napi\_queue\_async\_work\_with\_qos 和 napi\_cancel\_async\_work 的示例代码

```
1. /*
2. * 宏 EXPAND_ASYNC_WORK_CASE 将为 op 提供如下变量
3. * @variable napi_env localEnv
4. * @variable napi_async_work work
5. */
6. #define EXPAND_ASYNC_WORK_CASE(name, op)                                           \
7. napi_value name(napi_env env, napi_callback_info cbinfo)                           \
8. {                                                                                  \
9. CallbackInfo info(env, cbinfo);                                                \
10. bool same = true;                                                              \
11. STRICT_NAPI_CALL(napi_get_value_bool(env, info[0], &same));                    \
12. std::thread([](bool same) {                                                    \
13. EngineProxy localEnv;                                                      \
14. napi_async_work work = nullptr;                                            \
15. {                                                                          \
16. napi_value taskName = nullptr;                                         \
17. napi_create_string_utf8(localEnv, #name, NAPI_AUTO_LENGTH, &taskName); \
18. /* 不建议使用空的 execute 回调创建 napi_async_work */                    \
19. /* 此处可能出现内存泄漏，仅为复现 dfx 维测 */                            \
20. napi_create_async_work(localEnv, nullptr, taskName,                    \
21. [](napi_env, void*) {}, [](napi_env, napi_status, void* ) {},      \
22. nullptr, &work);                                                   \
23. if (!localEnv.Recreate(same)) {                                        \
24. if (work != nullptr) {                                             \
25. napi_delete_async_work(localEnv, work);                        \
26. }                                                                  \
27. return;                                                            \
28. }                                                                      \
29. }                                                                          \
30. (op);                                                                      \
31. if (work != nullptr) {                                                     \
32. napi_delete_async_work(localEnv, work);                                \
33. }                                                                          \
34. }, same).detach();                                                             \
35. return nullptr;                                                                \
36. }

38. /*
39. * 接口声明 index.d.ts
40. * const triggerDFXQueueWork: (samePtr: boolean) => void;
41. * const triggerDFXQueueWorkWithQos: (samePtr: boolean) => void;
42. * const triggerDFXCancelWork: (samePtr: boolean) => void;
43. */
44. EXPAND_ASYNC_WORK_CASE(TriggerDFXQueueWork,
45. napi_queue_async_work(localEnv, work))
46. EXPAND_ASYNC_WORK_CASE(TriggerDFXQueueWorkWithQos,
47. napi_queue_async_work_with_qos(localEnv, work, napi_qos_default))
48. EXPAND_ASYNC_WORK_CASE(TriggerDFXCancelWork,
49. napi_cancel_async_work(localEnv, work))

51. #undef EXPAND_ASYNC_WORK_CASE
```

**napi\_threadsafe\_function相关接口**

napi\_call\_threadsafe\_function 和 napi\_release\_threadsafe\_function 的示例代码

```
1. /*
2. * 宏 EXPAND_THREADSAFE_FUNCTION_CASE 将为 op 提供如下变量
3. * @variable napi_env localEnv
4. * @variable napi_threadsafe_function tsfn
5. */
6. #define EXPAND_THREADSAFE_FUNCTION_CASE(name, op)                                       \
7. napi_value name(napi_env, napi_callback_info info) {                                \
8. std::thread([]() {                                                              \
9. EngineProxy localEnv;                                                       \
10. napi_threadsafe_function tsfn = nullptr;                                    \
11. {                                                                           \
12. napi_value taskName = nullptr;                                          \
13. napi_create_string_utf8(localEnv, "Test", NAPI_AUTO_LENGTH, &taskName); \
14. // napi_create_threadsafe_function创建线程安全函数，任务执行完成后，      \
15. // 需调用napi_release_threadsafe_function释放
16. napi_create_threadsafe_function(                                        \
17. localEnv, nullptr, nullptr, taskName, 0, 1, nullptr,                \
18. [](napi_env, void *, void *) {}, nullptr,                           \
19. [](napi_env, napi_value, void *, void *) {}, &tsfn);                \
20. if (status != napi_ok) {                                                \
21. OH_INFO_ERROR(LOG_APP,"napi_create_threadsafe_function failed");    \
22. return nullptr;                                                     \
23. }                                                                       \
24. if (!localEnv.RecreateSame()) {                                         \
25. return;                                                             \
26. };                                                                      \
27. }                                                                           \
28. (op);                                                                       \
29. }).detach();                                                                    \
30. return nullptr;                                                                 \
31. }

33. /*
34. * 接口声明 index.d.ts
35. * const triggerDFXTsfnCall: () => void;
36. * const triggerDFXTsfnRelease: () => void;
37. */
38. EXPAND_THREADSAFE_FUNCTION_CASE(TriggerDFXTsfnCall,
39. napi_call_threadsafe_function(tsfn, nullptr, napi_tsfn_nonblocking))
40. EXPAND_THREADSAFE_FUNCTION_CASE(TriggerDFXTsfnRelease,
41. napi_release_threadsafe_function(tsfn, napi_tsfn_release))

43. #undef EXPAND_THREADSAFE_FUNCTION_CASE
```

## 跨线程调用

### 覆盖范围及关键日志

大多数napi接口都不是多线程安全的，因此为这些错误用法额外增加了定位手段。

若无特殊说明，本章节描述的维测手段会在启用ArkTS运行时多线程检测开关后，立即中断进程。

**关键日志**

current napi interface cannot run in multi-thread, thread id: <env tid>, current thread id: <current tid>

该维测手段覆盖范围如下：

1. napi\_add\_env\_cleanup\_hook\*
2. napi\_remove\_env\_cleanup\_hook\*
3. napi\_add\_async\_cleanup\_hook
4. napi\_set\_instance\_data
5. napi\_get\_instance\_data

\*：具有该标志的接口，在维测触发的情况下，仅打印带有调用栈信息的ERROR日志，并不会中断进程。

### 案例及示例代码

注意

下面的代码仅用于构造异常场景，触发异常分支的DFX日志。在充分理解其意图前，请勿将其应用到业务场景中。

**env\_cleanup\_hook相关接口**

napi\_add\_env\_cleanup\_hook 和 napi\_remove\_env\_cleanup\_hook 的示例代码

```
1. static void EnvCleanUpCallback(void *arg) {
2. char* data = reinterpret_cast<char *>(arg);
3. delete data;
4. }

6. /*
7. * 接口声明 index.d.ts
8. * const triggerDFXClnAddXT: () => void;
9. */
10. napi_value TriggerDFXClnAddXT(napi_env env, napi_callback_info info)
11. {
12. char* data = new char;
13. CHECK_NOT_NULL(data);
14. *data = '\0';
15. std::thread([](napi_env env, char* data) {
16. napi_add_env_cleanup_hook(env, EnvCleanUpCallback, reinterpret_cast<void *>(data));
17. }, env, data).join();
18. napi_remove_env_cleanup_hook(env, EnvCleanUpCallback, reinterpret_cast<void *>(data));
19. delete data;
20. return nullptr;
21. }

23. /*
24. * 接口声明 index.d.ts
25. * const triggerDFXClnAddMT: () => void;
26. */
27. napi_value TriggerDFXClnAddMT(napi_env env, napi_callback_info info)
28. {
29. char* data = new char;
30. CHECK_NOT_NULL(data);
31. *data = '\0';
32. napi_add_env_cleanup_hook(env, EnvCleanUpCallback, reinterpret_cast<void *>(data));
33. napi_add_env_cleanup_hook(env, EnvCleanUpCallback, reinterpret_cast<void *>(data));
34. napi_remove_env_cleanup_hook(env, EnvCleanUpCallback, reinterpret_cast<void *>(data));
35. delete data;
36. return nullptr;
37. }

39. /*
40. * 接口声明 index.d.ts
41. * const triggerDFXClnRmXT: () => void;
42. */
43. napi_value TriggerDFXClnRmXT(napi_env env, napi_callback_info info)
44. {
45. char* data = new char;
46. CHECK_NOT_NULL(data);
47. *data = '\0';
48. napi_add_env_cleanup_hook(env, EnvCleanUpCallback, reinterpret_cast<void *>(data));
49. std::thread([](napi_env env, char* data) {
50. napi_remove_env_cleanup_hook(env, EnvCleanUpCallback, reinterpret_cast<void *>(data));
51. delete data;
52. }, env, data).join();
53. return nullptr;
54. }

56. /*
57. * 接口声明 index.d.ts
58. * const triggerDFXClnRmMT: () => void;
59. */
60. napi_value TriggerDFXClnRmMT(napi_env env, napi_callback_info info)
61. {
62. char* data = new char;
63. CHECK_NOT_NULL(data);
64. *data = '\0';
65. napi_add_env_cleanup_hook(env, EnvCleanUpCallback, reinterpret_cast<void *>(data));
66. napi_remove_env_cleanup_hook(env, EnvCleanUpCallback, reinterpret_cast<void *>(data));
67. // 解注册使用的参数与注册时的一致性，比重复解注册更值得关注
68. napi_remove_env_cleanup_hook(env, EnvCleanUpCallback, reinterpret_cast<void *>(data));
69. delete data;
70. return nullptr;
71. }
```

**async\_cleanup\_hook相关接口**

napi\_add\_async\_cleanup\_hook示例代码

```
1. static void AsyncCleanupCallback(napi_async_cleanup_hook_handle handle, void *)
2. {
3. napi_remove_async_cleanup_hook(handle);
4. }

6. /*
7. * 接口声明 index.d.ts
8. * const triggerDFXAsyncAddXT: () => void;
9. */
10. napi_value TriggerDFXAsyncAddXT(napi_env env, napi_callback_info info)
11. {
12. std::thread([](napi_env env) {
13. napi_add_async_cleanup_hook(env, AsyncCleanupCallback, nullptr, nullptr);
14. }, env).join();
15. return nullptr;
16. }
```

**instance\_data相关接口**

napi\_set\_instance\_data、napi\_get\_instance\_data示例代码

```
1. /*
2. * 接口声明 index.d.ts
3. * const triggerDFXInsSetXT: () => void;
4. */
5. napi_value TriggerDFXInsSetXT(napi_env env, napi_callback_info info)
6. {
7. std::thread([](napi_env env) {
8. napi_set_instance_data(env, nullptr, [](napi_env, void *, void *) {}, nullptr);
9. }, env).join();
10. return nullptr;
11. }

13. /*
14. * 接口声明 index.d.ts
15. * const triggerDFXInsGetXT: () => void;
16. */
17. napi_value TriggerDFXInsGetXT(napi_env env, napi_callback_info info)
18. {
19. std::thread([](napi_env env) {
20. void *data = nullptr;
21. napi_get_instance_data(env, &data);
22. }, env).join();
23. return nullptr;
24. }
```
