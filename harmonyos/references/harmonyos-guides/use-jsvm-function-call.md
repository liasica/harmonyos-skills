---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/use-jsvm-function-call
title: 使用JSVM-API接口进行函数创建和调用
breadcrumb: 指南 > NDK开发 > 代码开发 > 使用JSVM-API实现JS与C/C++语言交互 > JSVM-API使用指导 > 使用JSVM-API接口进行函数创建和调用
category: harmonyos-guides
scraped_at: 2026-04-28T07:54:16+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:036f7dc0b04bfe68b0800ec36cb063fab69be849e28269c7785b813a09630856
---

## 简介

函数调用允许开发者从JSVM模块中调用JavaScript函数，并传参，或者直接在JSVM模块中创建一个JavaScript函数。

## 基本概念

函数是一种重要的编程概念，用于执行特定任务，提升代码可读性与复用性，简化复杂操作，并实现代码的模块化和结构化，便于理解、维护和扩展。

## 接口说明

| 接口 | 功能说明 |
| --- | --- |
| OH\_JSVM\_GetCbInfo | 从给定的callback info中获取有关调用的详细信息，如参数和this指针。 |
| OH\_JSVM\_CallFunction | 在C/C++侧调用JavaScript方法。 |
| OH\_JSVM\_IsFunction | 判断对象是否为函数对象。 |
| OH\_JSVM\_CreateFunction | 用于创建JavaScript函数,用于从JavaScript环境中调用C/C++代码中的函数, 需要设置到一个JavaScript对象中才可以进行调用。 |

## 使用示例

JSVM-API接口开发流程参考[使用JSVM-API实现JS与C/C++语言交互开发流程](use-jsvm-process.md)，本文仅对接口对应C++相关代码进行展示。

### OH\_JSVM function整合测试

cpp测试全量代码，入口为TEST\_FUNC

```
1. #include "hilog/log.h"
2. #include "ark_runtime/jsvm.h"

4. #define LOG_DOMAIN 0x3200
5. #define LOG_TAG "APP"

7. #define CHECK_RET(cond) \
8. if ((cond)) { \
9. const JSVM_ExtendedErrorInfo* info; \
10. OH_JSVM_GetLastErrorInfo(env, &info); \
11. OH_LOG_ERROR(LOG_APP, "jsvm fail file: %{public}s line: %{public}d ret = %{public}d message = %{public}s", __FILE__, __LINE__, cond, info != nullptr ? info->errorMessage : ""); \
12. return -1;   \
13. }

15. #define CHECK(cond) \
16. if (!(cond)) { \
17. OH_LOG_ERROR(LOG_APP, "jsvm fail file: %{public}s line: %{public}d ret = %{public}d", __FILE__, __LINE__, cond); \
18. return -1;   \
19. }

21. JSVM_Value NativeCreateFunctionTest(JSVM_Env env, JSVM_CallbackInfo info) {
22. void *data = nullptr;
23. size_t argc = 1;
24. JSVM_Value argv[1] = {nullptr};
25. JSVM_Value thisArg;
26. // 获取callback 参数信息
27. JSVM_Status ret = OH_JSVM_GetCbInfo(env, info, &argc, &argv[0], &thisArg, &data);
28. if (ret != JSVM_OK) {
29. const JSVM_ExtendedErrorInfo* info;
30. OH_JSVM_GetLastErrorInfo(env, &info);
31. OH_LOG_ERROR(LOG_APP, "jsvm fail file: %{public}s line: %{public}d ret = %{public}d message = %{public}s", __FILE__, __LINE__, ret, info != nullptr ? info->errorMessage : "");
32. return nullptr;
33. }
34. char message[256];
35. OH_JSVM_GetValueStringLatin1(env, argv[0], message, 256, nullptr);
36. if (data == nullptr) {
37. OH_LOG_ERROR(LOG_APP, "jsvm: %{public}s; callback data null", message);
38. } else {
39. OH_LOG_INFO(LOG_APP, "jsvm: %{public}s; %{public}s", message, (char*)data);
40. }
41. return nullptr;
42. }

44. static int32_t TEST_FUNC() {
45. JSVM_InitOptions initOptions{};
46. JSVM_VM vm;
47. JSVM_Env env = nullptr;
48. JSVM_VMScope vmScope;
49. JSVM_EnvScope envScope;
50. JSVM_HandleScope handleScope;
51. JSVM_Value result;
52. static bool isVMInit = false;
53. if (!isVMInit) {
54. isVMInit = true;
55. // 单个进程只需初始化一次
56. OH_JSVM_Init(&initOptions);
57. }
58. CHECK_RET(OH_JSVM_CreateVM(nullptr, &vm));
59. CHECK_RET(OH_JSVM_CreateEnv(vm, 0, nullptr, &env));
60. CHECK_RET(OH_JSVM_OpenVMScope(vm, &vmScope));
61. CHECK_RET(OH_JSVM_OpenEnvScope(env, &envScope));
62. CHECK_RET(OH_JSVM_OpenHandleScope(env, &handleScope));

64. // 创建并检查函数
65. char hello[] = "Hello World!";
66. JSVM_CallbackStruct cb = {NativeCreateFunctionTest, (void*)hello};
67. JSVM_Value func;
68. CHECK_RET(OH_JSVM_CreateFunction(env, "", JSVM_AUTO_LENGTH, &cb, &func));
69. bool isFunction = false;
70. CHECK_RET(OH_JSVM_IsFunction(env, func, &isFunction));
71. CHECK(isFunction);

73. // 将函数设置到全局对象中
74. JSVM_Value global;
75. CHECK_RET(OH_JSVM_GetGlobal(env, &global));
76. JSVM_Value key;
77. CHECK_RET(OH_JSVM_CreateStringUtf8(env, "NativeFunc", JSVM_AUTO_LENGTH, &key));
78. CHECK_RET(OH_JSVM_SetProperty(env, global, key, func));

80. // 通过call 接口调用函数
81. JSVM_Value argv[1] = {nullptr};
82. OH_JSVM_CreateStringUtf8(env, "jsvm api call function", JSVM_AUTO_LENGTH, &argv[0]);
83. CHECK_RET(OH_JSVM_CallFunction(env, global, func, 1, argv, &result));

85. // 通过script调用函数
86. JSVM_Script script;
87. JSVM_Value jsSrc;
88. const char* srcCallNative = R"JS(NativeFunc('js source call function');)JS";
89. CHECK_RET(OH_JSVM_CreateStringUtf8(env, srcCallNative, JSVM_AUTO_LENGTH, &jsSrc));
90. CHECK_RET(OH_JSVM_CompileScript(env, jsSrc, nullptr, 0, true, nullptr, &script));
91. CHECK_RET(OH_JSVM_RunScript(env, script, &result));

93. CHECK_RET(OH_JSVM_CloseHandleScope(env, handleScope));
94. CHECK_RET(OH_JSVM_CloseEnvScope(env, envScope));
95. CHECK_RET(OH_JSVM_CloseVMScope(vm, vmScope));
96. CHECK_RET(OH_JSVM_DestroyEnv(env));
97. CHECK_RET(OH_JSVM_DestroyVM(vm));
98. return 0;
99. }
```

预期的输出

```
1. jsvm: jsvm api call function; Hello World!
2. jsvm: js source call function; Hello World!
```
