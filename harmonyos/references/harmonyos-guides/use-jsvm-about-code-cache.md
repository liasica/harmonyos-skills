---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/use-jsvm-about-code-cache
title: 使用code cache加速编译
breadcrumb: 指南 > NDK开发 > 代码开发 > 使用JSVM-API实现JS与C/C++语言交互 > JSVM-API典型使用场景指导 > JSVM-API调优&高性能使用示例 > 使用code cache加速编译
category: harmonyos-guides
scraped_at: 2026-04-28T07:54:27+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:88e2cce62679c8e66f9db922ad4851ac22fa7cba99fb93b93c6f9b20f9bb4630
---

##code cache简介

JSVM提供了生成并使用code cache加速编译过程的方法，其获取和使用分为下面几个部分：

* 首先使用compile系列接口编译得到JSVM\_Script
* 使用OH\_JSVM\_CreateCodeCache接口，传递编译完成后生成的JSVM\_Script
* 将OH\_JSVM\_CreateCodeCache生成的code cache保存，等待下一次编译时，作为参数传入compile系列接口

通过上述流程，将会在使用code cache的那次编译中，极大减少编译时间，其原理为将编译完成的script序列化，然后使用code cache编译时就不再需要重新解析/编译已经被序列化的函数，只需要进行一次反序列化即可，这样编译就简化为了一次数据读取。

##code cache校验规格说明

| 规格 | 规格说明 |
| --- | --- |
| 完整性校验 | 校验cache实际长度，是否与生成时一致 |
| 兼容性校验 | 校验生成cache的JSVM版本与编译选项是否与当前一致 |
| 一致性校验 | 校验生成cache的js源码，是否与当前输入源码长度一致 |

## 场景示例

下面的伪代码是一个典型的使用方法，其中第二次编译，如果cacheRejected为true，那么说明code cache被拒绝无法生效，运行时间会与无code cache时间相同；为false则这次运行将会极大加快。

其中使用到的JSVM-API可以参考 [JSVM数据类型与接口说明](jsvm-data-types-interfaces.md)，这里仅展示调用的步骤。

外层跨语言交互的部分可以参考 [使用JSVM-API实现JS与C/C++语言交互开发流程](use-jsvm-process.md)。

```
1. #include "napi/native_api.h"
2. #include "ark_runtime/jsvm.h"
3. #include <hilog/log.h>
4. #include <string>

6. JSVM_Value UseCodeCache(JSVM_Env env, JSVM_CallbackInfo info) {
7. // 编译参数准备
8. JSVM_Value jsSrc;
9. JSVM_Script script;
10. JSVM_Value result;
11. size_t length = 0;
12. const uint8_t* dataPtr = nullptr;
13. bool cacheRejected = true;
14. static std::string src = R"JS(
15. a = 65536;
16. b = 32768;
17. c = a + b;
18. )JS";

20. // 生成code cache
21. {
22. JSVM_HandleScope handleScope;
23. OH_JSVM_OpenHandleScope(env, &handleScope);

25. // 源码字符串转换为js字符串
26. OH_JSVM_CreateStringUtf8(env, src.c_str(), src.size(), &jsSrc);

28. // 编译js代码
29. OH_JSVM_CompileScript(env, jsSrc, nullptr, 0, true, nullptr, &script);

31. // 执行js代码
32. OH_JSVM_RunScript(env, script, &result);
33. int value = 0;
34. OH_JSVM_GetValueInt32(env, result, &value);
35. OH_LOG_INFO(LOG_APP, "first run result: %{public}d\n", value);

37. if (dataPtr == nullptr) {
38. // 将js源码编译出的脚本保存到cache, 可以避免重复编译, 带来性能提升
39. OH_JSVM_CreateCodeCache(env, script, &dataPtr, &length);
40. }

42. OH_JSVM_CloseHandleScope(env, handleScope);
43. }

45. // 使用code cache
46. {
47. JSVM_HandleScope handleScope;
48. OH_JSVM_OpenHandleScope(env, &handleScope);

50. // 源码字符串转换为js字符串
51. OH_JSVM_CreateStringUtf8(env, src.c_str(), src.size(), &jsSrc);

53. // 使用code cache编译js代码
54. OH_JSVM_CompileScript(env, jsSrc, dataPtr, length, true, &cacheRejected, &script);

56. // 执行js代码
57. OH_JSVM_RunScript(env, script, &result);
58. int value = 0;
59. OH_JSVM_GetValueInt32(env, result, &value);
60. OH_LOG_INFO(LOG_APP, "second run result: %{public}d\n", value);

62. OH_JSVM_CloseHandleScope(env, handleScope);
63. }
64. OH_LOG_INFO(LOG_APP, "cache rejected: %{public}d\n", cacheRejected);
65. return result;
66. }

68. // Register a callback.
69. static JSVM_CallbackStruct param[] = {
70. {.data = nullptr, .callback = UseCodeCache}
71. };
72. static JSVM_CallbackStruct *method = param;
73. // Register the C++ callback as a JSVM globalThis.UseCodeCache property for the JS to call.
74. static JSVM_PropertyDescriptor descriptor[] = {
75. {"UseCodeCache", nullptr, method++, nullptr, nullptr, nullptr, JSVM_DEFAULT},
76. };

78. // 样例测试js
79. const char* srcCallNative = R"JS(globalThis.UseCodeCache())JS";
```

预期的输出结果如下：

```
1. first run result: 98304
2. second run result: 98304
3. cache rejected: 0
```

## 注意事项

上述代码中使用了code cache进行编译：OH\_JSVM\_CompileScript(env, jsSrc, dataPtr, length, true, &cacheRejected, &script);

这个接口的传入参数中包含cacheRejected，用于接收实际编译过程中code cache是否被拒绝的状态，具体包括多种情况：

-code cache校验失败

-code cache校验成功

* 内存中存在编译缓存，code cache没有被校验

对于第一种情况，这个参数会被设置为true，而后两种情况都是false，因此需要注意即使reject为false，也不能说明code cache被接收了。
