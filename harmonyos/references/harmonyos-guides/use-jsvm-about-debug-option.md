---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/use-jsvm-about-debug-option
title: 使用JSVM-API接口进行debug操作
breadcrumb: 指南 > NDK开发 > 代码开发 > 使用JSVM-API实现JS与C/C++语言交互 > JSVM-API使用指导 > 使用JSVM-API接口进行debug操作
category: harmonyos-guides
scraped_at: 2026-04-28T07:54:18+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:4d5301ab30be9ad3bd6b1d093170642342cd3e2ba3bdd5600ca0a0ad7e2cad5a
---

## 简介

JSVM-API中提供接口，可以启用/禁用特定JSVM\_Env下的指定debug选项。目前支持的debug选项有JSVM\_SCOPE\_CHECK。

## debug选项介绍

debug选项皆为JSVM\_DebugOption类型。

### JSVM\_SCOPE\_CHECK

* 开发者在开发时，可能会出现在HandleScope结束后，调用上一次HandleScope内的JSVM\_Value类型变量，导致程序崩溃。JSVM\_SCOPE\_CHECK为scope校验手段，校验当前调用的JSVM\_Value类型变量是否超出HandleScope作用域，如果超出，则抛出错误“Run in wrong HandleScope”。
* 开启该debug选项后，若JSVM-API创建了JSVM\_Value，则在hilog中有“ADD\_VAL\_TO\_SCOPE\_CHECK in function: [函数名]”输出，例如“ADD\_VAL\_TO\_SCOPE\_CHECK in function: OH\_JSVM\_GetBoolean”。若JSVM-API使用了JSVM\_Value，则在hilog中有“CHECK\_SCOPE in function: [函数名]”输出，表示对使用的JSVM\_Value进行了HandleScope校验，例如“CHECK\_SCOPE in function: OH\_JSVM\_IsBoolean”。

## 接口说明

| 接口 | 功能说明 |
| --- | --- |
| OH\_JSVM\_SetDebugOption | 启用/禁用特定JSVM\_Env的指定debug选项。传入的debug选项参数debugOption必须为JSVM\_DebugOption类型，布尔值参数isEnabled用于控制是否开启该debug选项。此API仅供debug时使用，开启后可能会带来性能下降。 |

## 使用示例

JSVM-API接口开发流程参考[使用JSVM-API实现JS与C/C++语言交互开发流程](use-jsvm-process.md)，本文仅对接口对应C++相关代码进行展示。

### JSVM\_DebugOption

仅需替换[使用JSVM-API实现JS与C/C++语言交互开发流程](use-jsvm-process.md)示例代码中的“TestJSVM()”函数即可运行。

* 在正确的HandleScope内调用JSVM\_Value类型变量。

```
1. static int32_t TestJSVM()
2. {
3. JSVM_InitOptions initOptions = {0};
4. JSVM_VM vm;
5. JSVM_Env env = nullptr;
6. JSVM_VMScope vmScope;
7. JSVM_EnvScope envScope;
8. JSVM_HandleScope handleScope;

10. // 初始化JavaScript引擎实例
11. if (g_aa == 0) {
12. g_aa++;
13. CHECK(OH_JSVM_Init(&initOptions));
14. }
15. // 创建JSVM环境
16. CHECK(OH_JSVM_CreateVM(nullptr, &vm));
17. CHECK(OH_JSVM_CreateEnv(vm, sizeof(descriptor) / sizeof(descriptor[0]), descriptor, &env));
18. // 打开JSVM_SCOPE_CHECK校验选项
19. CHECK(OH_JSVM_SetDebugOption(env, JSVM_SCOPE_CHECK, true));
20. CHECK(OH_JSVM_OpenVMScope(vm, &vmScope));
21. CHECK_RET(OH_JSVM_OpenEnvScope(env, &envScope));
22. // 打开HandleScope
23. CHECK_RET(OH_JSVM_OpenHandleScope(env, &handleScope));

25. // 通过script调用测试函数
26. JSVM_Script script;
27. JSVM_Value jsSrc, result;
28. CHECK_RET(OH_JSVM_CreateStringUtf8(env, srcCallNative, JSVM_AUTO_LENGTH, &jsSrc));
29. CHECK_RET(OH_JSVM_CompileScript(env, jsSrc, nullptr, 0, true, nullptr, &script));
30. CHECK_RET(OH_JSVM_RunScript(env, script, &result));

32. bool boolResult = true;
33. // OH_JSVM_IsBoolean接口调用JSVM_Value类型变量result
34. JSVM_Status status = OH_JSVM_IsBoolean(env, result, &boolResult);
35. if (status != JSVM_OK) {
36. OH_LOG_ERROR(LOG_APP, "JSVM OH_JSVM_IsBoolean: failed");
37. } else {
38. OH_LOG_INFO(LOG_APP, "JSVM OH_JSVM_IsBoolean: success: %{public}d", boolResult);
39. }

41. // 销毁JSVM环境
42. // 关闭HandleScope
43. CHECK_RET(OH_JSVM_CloseHandleScope(env, handleScope));
44. CHECK_RET(OH_JSVM_CloseEnvScope(env, envScope));
45. CHECK(OH_JSVM_CloseVMScope(vm, vmScope));
46. // 关闭JSVM_SCOPE_CHECK校验选项
47. CHECK(OH_JSVM_SetDebugOption(env, JSVM_SCOPE_CHECK, false));
48. CHECK(OH_JSVM_DestroyEnv(env));
49. CHECK(OH_JSVM_DestroyVM(vm));
50. return 0;
51. }
```

**执行结果**

hilog中有以下结果输出：

```
1. ADD_VAL_TO_SCOPE_CHECK in function: NewString
2. CHECK_SCOPE in function: OH_JSVM_CompileScript
3. ADD_VAL_TO_SCOPE_CHECK in function: OH_JSVM_GetCbInfo
4. ADD_VAL_TO_SCOPE_CHECK in function: OH_JSVM_GetCbInfo
5. ADD_VAL_TO_SCOPE_CHECK in function: OH_JSVM_GetCbInfo
6. CHECK_SCOPE in function: OH_JSVM_StrictEquals
7. CHECK_SCOPE in function: OH_JSVM_StrictEquals
8. JSVM OH_JSVM_StrictEquals: success: 0
9. ADD_VAL_TO_SCOPE_CHECK in function: OH_JSVM_GetBoolean
10. ADD_VAL_TO_SCOPE_CHECK in function: OH_JSVM_RunScript
11. CHECK_SCOPE in function: OH_JSVM_IsBoolean
12. JSVM OH_JSVM_IsBoolean: success: 1
```

* 在错误的HandleScope内调用JSVM\_Value类型变量。

```
1. static int32_t TestJSVM()
2. {
3. JSVM_InitOptions initOptions = {0};
4. JSVM_VM vm;
5. JSVM_Env env = nullptr;
6. JSVM_VMScope vmScope;
7. JSVM_EnvScope envScope;
8. JSVM_HandleScope handleScope;

10. // 初始化JavaScript引擎实例
11. if (g_aa == 0) {
12. g_aa++;
13. CHECK(OH_JSVM_Init(&initOptions));
14. }
15. // 创建JSVM环境
16. CHECK(OH_JSVM_CreateVM(nullptr, &vm));
17. CHECK(OH_JSVM_CreateEnv(vm, sizeof(descriptor) / sizeof(descriptor[0]), descriptor, &env));
18. // 打开JSVM_SCOPE_CHECK校验选项
19. CHECK(OH_JSVM_SetDebugOption(env, JSVM_SCOPE_CHECK, true));
20. CHECK(OH_JSVM_OpenVMScope(vm, &vmScope));
21. CHECK_RET(OH_JSVM_OpenEnvScope(env, &envScope));
22. // 打开HandleScope
23. CHECK_RET(OH_JSVM_OpenHandleScope(env, &handleScope));

25. // 通过script调用测试函数
26. JSVM_Script script;
27. JSVM_Value jsSrc, result;
28. CHECK_RET(OH_JSVM_CreateStringUtf8(env, srcCallNative, JSVM_AUTO_LENGTH, &jsSrc));
29. CHECK_RET(OH_JSVM_CompileScript(env, jsSrc, nullptr, 0, true, nullptr, &script));
30. CHECK_RET(OH_JSVM_RunScript(env, script, &result));

32. bool boolResult = true;

34. // 销毁JSVM环境
35. // 关闭HandleScope
36. CHECK_RET(OH_JSVM_CloseHandleScope(env, handleScope));
37. // OH_JSVM_IsBoolean接口在错误的HandleScope调用JSVM_Value类型变量result
38. JSVM_Status status = OH_JSVM_IsBoolean(env, result, &boolResult);
39. CHECK_RET(OH_JSVM_CloseEnvScope(env, envScope));
40. CHECK(OH_JSVM_CloseVMScope(vm, vmScope));
41. // 关闭JSVM_SCOPE_CHECK校验选项
42. CHECK(OH_JSVM_SetDebugOption(env, JSVM_SCOPE_CHECK, false));
43. CHECK(OH_JSVM_DestroyEnv(env));
44. CHECK(OH_JSVM_DestroyVM(vm));
45. return 0;
46. }
```

**执行结果**

程序崩溃，有cppcrash日志生成，在hilog中可以检索到类似以下的信息：

```
1. JSVM Fatal Error Position : "../../../../../../../arkcompiler/jsvm/src/js_native_api_v8.cpp":4537
2. JSVM Fatal Error Message : "Run in wrong HandleScope"
```
