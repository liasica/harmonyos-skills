---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/use-jsvm-execute_tasks
title: 使用JSVM-API接口进行任务队列相关开发
breadcrumb: 指南 > NDK开发 > 代码开发 > 使用JSVM-API实现JS与C/C++语言交互 > JSVM-API使用指导 > 使用JSVM-API接口进行任务队列相关开发
category: harmonyos-guides
scraped_at: 2026-04-28T07:54:15+08:00
doc_updated_at: 2026-04-17
content_hash: sha256:e313d1204920f0b4bd609fc84ae6847b3f57708fbccb23903225beea55c69c19
---

## 简介

在虚拟机内启动任务队列，检查队列中是否有待处理的微任务。任务队列可由外部事件循环执行。

## 基本概念

* **任务队列**：用于管理异步任务的调度和执行，确保任务按顺序处理。
* **微任务**：微任务是一种任务调度机制，主要用于处理那些需要尽快执行的较小任务，它们通常具有较高的优先级。

## 接口说明

| 接口 | 功能说明 |
| --- | --- |
| OH\_JSVM\_PumpMessageLoop | 启动任务队列的运行 |
| OH\_JSVM\_PerformMicrotaskCheckpoint | 执行任务队列里的微任务 |
| OH\_JSVM\_SetMicrotaskPolicy | 设置微任务执行策略 |

## 使用示例

JSVM-API接口开发流程参考[使用JSVM-API实现JS与C/C++语言交互开发流程](use-jsvm-process.md)，本文仅展示接口对应的C++相关代码。

权限要求：Wasm字节码需要应用拥有JIT权限才能执行，可参考[JSVM 申请JIT权限指导](jsvm-apply-jit-profile.md)申请对应权限。

运行限制：当前 JSVM 版本在坚盾守护模式下将禁用 WebAssembly 全部功能模块。开发者需针对此限制进行应用兼容性评估，具体技术规范详见[JSVM 坚盾守护模式](jsvm-secure-shield-mode.md)。

### OH\_JSVM\_PumpMessageLoop & OH\_JSVM\_PerformMicrotaskCheckpoint

启动任务队列，执行任务。

cpp部分代码：

```
1. #include <chrono>
2. #include <string.h>

4. static int g_aa = 0;

6. // 待执行的js代码
7. static const char *STR_TASK = R"JS(
8. // wasm 字节码 (以add 模块为例)
9. // 以下 wasmBuffer 对应的 wasm 字节码文本格式如下所示，只包含了一个函数 add
10. // (module
11. //   (func $add (param $lhs i32) (param $rhs i32) (result i32)
12. //     local.get $lhs
13. //     local.get $rhs
14. //     i32.add
15. //   )
16. //   (export "add" (func $add))
17. // )
18. var wasmBytes = new Uint8Array([0x00, 0x61, 0x73, 0x6d, 0x01, 0x00, 0x00, 0x00, 0x01, 0x07, 0x01,
19. 0x60, 0x02, 0x7f, 0x7f, 0x01, 0x7f, 0x03, 0x02, 0x01, 0x00, 0x07,
20. 0x07, 0x01, 0x03, 0x61, 0x64, 0x64, 0x00, 0x00, 0x0a, 0x09, 0x01,
21. 0x07, 0x00, 0x20, 0x00, 0x20, 0x01, 0x6a, 0x0b]);

23. var p = WebAssembly.instantiate(wasmBytes, {});
24. p.then((result) => {
25. consoleinfo("Called with instance " + result);
26. });
27. p.finally(() => {
28. consoleinfo("Called Finally");
29. });
30. )JS";

32. // 保证js代码中的打印信息可以正常输出
33. static JSVM_Value ConsoleInfo(JSVM_Env env, JSVM_CallbackInfo info) {
34. size_t argc = 1;
35. JSVM_Value args[1];
36. char log[256] = "";
37. size_t logLength = 0;
38. JSVM_CALL(OH_JSVM_GetCbInfo(env, info, &argc, args, NULL, NULL));

40. OH_JSVM_GetValueStringUtf8(env, args[0], log, 255, &logLength);
41. log[255] = 0;
42. OH_LOG_INFO(LOG_APP, "JSVM API TEST: %{public}s", log);
43. return nullptr;
44. }

46. // 注册consoleinfo的方法
47. JSVM_CallbackStruct param[] = {
48. {.data = nullptr, .callback = ConsoleInfo},
49. };
50. JSVM_PropertyDescriptor descriptor[] = {
51. {"consoleinfo", NULL, &param[0], NULL, NULL, NULL, JSVM_DEFAULT},
52. };

54. static int32_t TestJSVM() {
55. JSVM_InitOptions init_options;
56. memset(&init_options, 0, sizeof(init_options));
57. if (g_aa == 0) {
58. OH_JSVM_Init(&init_options);
59. g_aa++;
60. }
61. // 创建JavaScript虚拟机实例,打开虚拟机作用域
62. JSVM_VM vm;
63. JSVM_CreateVMOptions options;
64. memset(&options, 0, sizeof(options));
65. CHECK(OH_JSVM_CreateVM(&options, &vm));
66. JSVM_VMScope vm_scope;
67. CHECK(OH_JSVM_OpenVMScope(vm, &vm_scope));

69. JSVM_Env env;
70. CHECK(OH_JSVM_CreateEnv(vm, sizeof(descriptor) / sizeof(descriptor[0]), descriptor, &env));
71. JSVM_EnvScope envScope;
72. CHECK_RET(OH_JSVM_OpenEnvScope(env, &envScope));
73. JSVM_HandleScope handlescope;
74. CHECK_RET(OH_JSVM_OpenHandleScope(env, &handlescope));
75. JSVM_Value sourcecodevalue;
76. CHECK_RET(OH_JSVM_CreateStringUtf8(env, STR_TASK, strlen(STR_TASK), &sourcecodevalue));
77. JSVM_Script script;
78. CHECK_RET(OH_JSVM_CompileScript(env, sourcecodevalue, nullptr, 0, true, nullptr, &script));
79. JSVM_Value result;
80. CHECK_RET(OH_JSVM_RunScript(env, script, &result));
81. bool rst = false;
82. auto start = std::chrono::system_clock::now();
83. while (true) {
84. // 如果任务队列中没有任务启动，则rst设置为false
85. CHECK_RET(OH_JSVM_PumpMessageLoop(vm, &rst));
86. CHECK_RET(OH_JSVM_PerformMicrotaskCheckpoint(vm));
87. // 定时退出
88. auto now = std::chrono::system_clock::now();
89. auto cost = std::chrono::duration_cast<std::chrono::milliseconds>(now - start).count();
90. if (cost > 100) {
91. break;
92. }
93. }

95. // 关闭并销毁环境和虚拟机
96. CHECK_RET(OH_JSVM_CloseHandleScope(env, handlescope));
97. CHECK_RET(OH_JSVM_CloseEnvScope(env, envScope));
98. CHECK(OH_JSVM_DestroyEnv(env));
99. CHECK(OH_JSVM_CloseVMScope(vm, vm_scope));
100. CHECK(OH_JSVM_DestroyVM(vm));
101. return 0;
102. }
```

预期输出结果：

```
1. JSVM API TEST: Called with instance [object Object]
2. JSVM API TEST: Called Finally
```

### OH\_JSVM\_SetMicrotaskPolicy

修改微任务执行策略，通过该接口，用户可以将策略设置为 JSVM\_MicrotaskPolicy::JSVM\_MICROTASK\_EXPLICIT 或 JSVM\_MicrotaskPolicy::JSVM\_MICROTASK\_AUTO。默认模式下，微任务的执行策略为 JSVM\_MicrotaskPolicy::JSVM\_MICROTASK\_AUTO。

微任务策略：

* JSVM\_MicrotaskPolicy::JSVM\_MICROTASK\_EXPLICIT ： 微任务在用户调用 OH\_JSVM\_PerformMicrotaskCheckpoint 后执行
* JSVM\_MicrotaskPolicy::JSVM\_MICROTASK\_AUTO： 微任务在 JS 调用栈为空时自动执行

cpp 部分代码

```
1. // OH_JSVM_SetMicrotaskPolicy的样例方法
2. static int SetMicrotaskPolicy(JSVM_VM vm, JSVM_Env env) {
3. // 默认或将策略设置为 JSVM_MICROTASK_AUTO 的行为
4. const char *scriptEvalMicrotask = R"JS(
5. evaluateMicrotask = false;
6. Promise.resolve().then(()=>{
7. evaluateMicrotask = true;
8. });
9. )JS";
10. JSVM_Script script;
11. JSVM_Value jsSrc;
12. JSVM_Value result;
13. CHECK_RET(OH_JSVM_CreateStringUtf8(env, scriptEvalMicrotask, JSVM_AUTO_LENGTH, &jsSrc));
14. CHECK_RET(OH_JSVM_CompileScript(env, jsSrc, nullptr, 0, true, nullptr, &script));
15. CHECK_RET(OH_JSVM_RunScript(env, script, &result));
16. JSVM_Value global;
17. CHECK_RET(OH_JSVM_GetGlobal(env, &global));
18. JSVM_Value hasEvaluateMicrotask;
19. CHECK_RET(OH_JSVM_GetNamedProperty(env, global, "evaluateMicrotask", &hasEvaluateMicrotask));
20. bool val = false;
21. CHECK_RET(OH_JSVM_GetValueBool(env, hasEvaluateMicrotask, &val));

23. OH_LOG_INFO(LOG_APP, "Policy :JSVM_MICROTASK_AUTO, evaluateMicrotask : %{public}d", val);

25. // 策略设置为 JSVM_MICROTASK_EXPLICIT 的行为
26. CHECK_RET(OH_JSVM_SetMicrotaskPolicy(vm, JSVM_MicrotaskPolicy::JSVM_MICROTASK_EXPLICIT));
27. CHECK_RET(OH_JSVM_RunScript(env, script, &result));
28. CHECK_RET(OH_JSVM_GetNamedProperty(env, global, "evaluateMicrotask", &hasEvaluateMicrotask));
29. CHECK_RET(OH_JSVM_GetValueBool(env, hasEvaluateMicrotask, &val));
30. OH_LOG_INFO(
31. LOG_APP,
32. "Policy: JSVM_MICROTASK_AUTO, evaluateMicrotask before calling OH_JSVM_PerformMicrotaskCheckpoint: %{public}d",
33. val);

35. CHECK_RET(OH_JSVM_PerformMicrotaskCheckpoint(vm));
36. CHECK_RET(OH_JSVM_GetNamedProperty(env, global, "evaluateMicrotask", &hasEvaluateMicrotask));
37. CHECK_RET(OH_JSVM_GetValueBool(env, hasEvaluateMicrotask, &val));
38. OH_LOG_INFO(
39. LOG_APP,
40. "Policy: JSVM_MICROTASK_AUTO, evaluateMicrotask after calling OH_JSVM_PerformMicrotaskCheckpoint: %{public}d",
41. val);

43. return 0;
44. }

46. static void RunDemo(JSVM_VM vm, JSVM_Env env) {
47. if (SetMicrotaskPolicy(vm, env) != 0) {
48. OH_LOG_INFO(LOG_APP, "Run Microtask Policy failed");
49. }
50. }

52. static int32_t TestJSVM() {
53. JSVM_InitOptions initOptions = {0};
54. JSVM_VM vm;
55. JSVM_Env env = nullptr;
56. JSVM_VMScope vmScope;
57. JSVM_EnvScope envScope;
58. JSVM_HandleScope handleScope;
59. JSVM_Value result;
60. // 初始化JavaScript引擎实例
61. if (g_aa == 0) {
62. g_aa++;
63. CHECK(OH_JSVM_Init(&initOptions));
64. }
65. // 创建JSVM环境
66. CHECK(OH_JSVM_CreateVM(nullptr, &vm));
67. CHECK(OH_JSVM_CreateEnv(vm, 0, nullptr, &env));
68. CHECK(OH_JSVM_OpenVMScope(vm, &vmScope));
69. CHECK_RET(OH_JSVM_OpenEnvScope(env, &envScope));
70. CHECK_RET(OH_JSVM_OpenHandleScope(env, &handleScope));

72. // 通过script调用测试函数
73. RunDemo(vm, env);

75. // 销毁JSVM环境
76. CHECK_RET(OH_JSVM_CloseHandleScope(env, handleScope));
77. CHECK_RET(OH_JSVM_CloseEnvScope(env, envScope));
78. CHECK(OH_JSVM_CloseVMScope(vm, vmScope));
79. CHECK(OH_JSVM_DestroyEnv(env));
80. CHECK(OH_JSVM_DestroyVM(vm));
81. return 0;
82. }
```

预期输出结果：

```
1. Policy :JSVM_MICROTASK_AUTO, evaluateMicrotask : 1
2. Policy :JSVM_MICROTASK_AUTO, evaluateMicrotask before calling OH_JSVM_PerformMicrotaskCheckpoint: 0
3. Policy :JSVM_MICROTASK_AUTO, evaluateMicrotask after calling OH_JSVM_PerformMicrotaskCheckpoint: 1
```
