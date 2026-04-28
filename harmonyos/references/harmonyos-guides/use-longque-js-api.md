---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/use-longque-js-api
title: Longque-JS-API使用指导
breadcrumb: 指南 > NDK开发 > 代码开发 > Longque-JS-API > Longque-JS-API使用指导
category: harmonyos-guides
scraped_at: 2026-04-28T07:54:28+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:82ce0eedbec0fa31c3a2ce040649a3fd53d3306883b7b29a278d7e583d73d8f4
---

Longque JS API 由 Longque JS Engine 提供，适用于在 HarmonyOS 平台构建稳定、高性能的应用。所有 API 均位于 \_\_Longque\_\_ 对象下。接口的版本可通过 \_\_Longque\_\_.version 获得，开发者可使用该版本进行特性判断。

**【注意】：Longque JS API 处于实验阶段，使用前请阅读本文档，评估其稳定性和兼容性。**

## 接口说明

| 接口 | 功能说明 |
| --- | --- |
| createDelegate | 创建委托 |

## 属性说明

| 属性 | 功能说明 |
| --- | --- |
| version | 用于表示 Longque JS API 的版本 |
| SKIP\_PROTOTYPE\_CHAIN | createDelegate 的属性过滤器，表示只委托自身属性，不考虑原型链 |
| SKIP\_PREFIX\_UNDERSCORE | createDelegate 的属性过滤器，表示过滤掉名字以 '\_' 开头的属性 |
| SKIP\_PREFIX\_DOLLAR | createDelegate 的属性过滤器，表示过滤掉名字以 '$' 开头的属性 |
| SKIP\_CONSTRUCTOR | createDelegate 的属性过滤器，表示过滤掉 'constructor' 属性 |

## createDelegate接口

接口引入版本 : 1

### 接口描述

| 接口 | 名称 | 说明 |
| --- | --- | --- |
| createDelegate | 创建委托 | 创建 underlyingObject 的委托对象，对委托对象的属性读写操作将映射至 underlyingObject。通过 initObject 指定初始委托对象，通过 propertyFilterFlags 指定属性过滤器。默认情况下，将映射 underlyingObject 及其原型链上所有可枚举的字符串键属性。 |

### 参数

(1) underlyingObject： 必选参数。表示被委托的底层对象。参数要求：

* underlyingObject 必须是对象，否则会抛出 TypeError 异常。
* 若 underlyingObject 是代理对象，将抛出 TypeError 异常。
* 若未指定 SKIP\_PROTOTYPE\_CHAIN 过滤器，且 underlyingObject 原型链上存在代理对象，则抛出 TypeError 异常。

(2) initObject：可选参数。表示初始委托对象。若传入 undefined，表示不指定初始对象，将由接口自动创建。参数要求：

* initObject 必须是对象，否则会抛出 TypeError 异常。
* 若 initObject 是代理对象，将抛出 TypeError 异常。
* 不能将委托对象作为 initObject，否则抛出 TypeError 异常。
* 若 initObject 是不可扩展的，则抛出 TypeError 异常。
* 若 initObject 中某些属性无法定义，将抛出 TypeError 异常，此时 initObject 中仅部分属性定义成功。

(3) propertyFilterFlags：可选参数。表示属性过滤器。如果传入的是 undefined，表示不指定过滤器。参数要求：

* 以下列出了当前支持的属性过滤器（未来可能扩展）。

```
1. __Longque__.SKIP_PROTOTYPE_CHAIN: 只委托 underlyingObject 自身属性，不考虑原型链
2. __Longque__.SKIP_PREFIX_UNDERSCORE: 过滤掉名字以 '_' 开头的属性
3. __Longque__.SKIP_PREFIX_DOLLAR: 过滤掉名字以 '$' 开头的属性
4. __Longque__.SKIP_CONSTRUCTOR: 过滤掉 'constructor' 属性
```

* 必须使用列出的过滤器，否则接口行为未定义，可能导致代码兼容性问题。
* 所有过滤器均为 number 类型，可用 | 运算符同时指定多个。
* 若 propertyFilterFlags 非 number 类型，抛出 TypeError 异常。

### 返回值

只有接口在不抛出异常的情况下，才会正确返回：

* 若未指定初始委托对象，返回新创建的委托对象。
* 若已指定初始委托对象，返回该初始委托对象。

### 注意事项

(1) 委托对象的属性顺序可能与 for-in、Object.keys 方法的结果不一致，请勿依赖属性顺序。

(2) 委托对象的实现是引擎内部机制。请勿依赖在委托对象上调用 Object.getOwnPropertyDescriptor、getOwnPropertyDescriptors、Reflect.getOwnPropertyDescriptor 等接口的返回结果。

### 使用示例

本示例展示了在 JSVM 中使用 Longque JS API 的方式，JSVM-API 接口开发流程参考[使用JSVM-API实现JS与C/C++语言交互开发流程](use-jsvm-process.md)，本文仅对接口对应C++相关代码进行展示。

cpp部分代码：

```
1. // 待执行的js代码
2. static const char *STR_TASK = R"JS(
3. function createDelegateTest() {
4. var myobj = {
5. 42: 0,
6. x: 1,
7. _y: 2,
8. $z:3
9. };

11. var proto = {
12. foo: 'foo'
13. };
14. Object.setPrototypeOf(myobj, proto);

16. var d1 = __Longque__.createDelegate(myobj, undefined);
17. consoleinfo(JSON.stringify(d1)); // {"42":0,"x":1,"_y":2,"$z":3,"foo":"foo"}

19. const propertyFilterFlags = __Longque__.SKIP_PREFIX_UNDERSCORE | __Longque__.SKIP_PREFIX_DOLLAR;
20. var d2 = __Longque__.createDelegate(myobj, undefined, propertyFilterFlags);
21. consoleinfo(JSON.stringify(d2)); // {"42":0,"x":1,"foo":"foo"}

23. d2[42] = 100;

25. const newFilter = propertyFilterFlags | __Longque__.SKIP_PROTOTYPE_CHAIN;
26. var d3 = __Longque__.createDelegate(myobj, undefined, newFilter);
27. consoleinfo(JSON.stringify(d3)); // {"42":100,"x":1}
28. }
29. createDelegateTest();
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
61. // 创建JavaScript虚拟机实例，打开虚拟机作用域
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

82. // 关闭并销毁环境和虚拟机
83. CHECK_RET(OH_JSVM_CloseHandleScope(env, handlescope));
84. CHECK_RET(OH_JSVM_CloseEnvScope(env, envScope));
85. CHECK(OH_JSVM_DestroyEnv(env));
86. CHECK(OH_JSVM_CloseVMScope(vm, vm_scope));
87. CHECK(OH_JSVM_DestroyVM(vm));
88. return 0;
89. }
```

预期的输出：

```
1. JSVM API TEST: {"42":0,"x":1,"_y":2,"$z":3,"foo":"foo"}
2. JSVM API TEST: {"42":0,"x":1,"foo":"foo"}
3. JSVM API TEST: {"42":100,"x":1}
```

### 性能测试示例

本示例用于测试使用Longque JS API前后的性能。

cpp部分代码：

```
1. // 待执行的js代码
2. static const char *STR_TASK = R"JS(
3. // 原始js代码
4. function base(underlying) {
5. var obj = {};
6. var tryDefineProperty = function (key) {
7. if (key.indexOf('_') === 0 || key.indexOf('$') === 0 || key === 'constructor') {
8. return false;
9. }
10. Object.defineProperty(obj, key, {
11. configurable: true,
12. enumerable: true,
13. get: function get() {
14. return underlying[key];
15. },
16. set: function set(value) {
17. return (underlying[key] = value);
18. },
19. });
20. return true;
21. };
22. for (var key in underlying) {
23. if (!tryDefineProperty(key)) {
24. continue;
25. }
26. }
27. return obj;
28. }

30. // 使用Longque JSVM API之后的代码
31. function opt(underlying) {
32. var delegate = __Longque__.createDelegate(
33. underlying,
34. undefined,
35. __Longque__.SKIP_PREFIX_UNDERSCORE |
36. __Longque__.SKIP_PREFIX_DOLLAR |
37. __Longque__.SKIP_CONSTRUCTOR,
38. );
39. return delegate;
40. }

42. // 性能测试
43. function doTest(tag, func, underlying, times) {
44. const begin = Date.now();
45. var obj = null;
46. for (var i = 0; i < times; ++i) {
47. obj = func(underlying);
48. }
49. const end = Date.now();
50. consoleinfo(`[${tag}] Time cost: ${(end - begin).toFixed(0)} ms`);
51. return obj;
52. }

54. function testEntry() {
55. var underlying = {
56. x: 1,
57. y: 2,
58. foo: 'foo',
59. _bar: '_bar',
60. _hi: '_hi',
61. $test: '$test',
62. constructor: 'ctor',
63. pi: 3.14,
64. };
65. for (var i = 0; i < 100; ++i) {
66. underlying[`key_${i}`] = i;
67. }
68. const n = 10000;
69. // 测试原js代码的运行时间
70. doTest('base', base, underlying, n);
71. // 测试使用Longque JSVM API之后的运行时间
72. doTest('opt', opt, underlying, n);
73. }

75. testEntry();
76. )JS";

78. // 保证js代码中的打印信息可以正常输出
79. static JSVM_Value ConsoleInfo(JSVM_Env env, JSVM_CallbackInfo info) {
80. size_t argc = 1;
81. JSVM_Value args[1];
82. char log[256] = "";
83. size_t logLength = 0;
84. JSVM_CALL(OH_JSVM_GetCbInfo(env, info, &argc, args, NULL, NULL));

86. OH_JSVM_GetValueStringUtf8(env, args[0], log, 255, &logLength);
87. log[255] = 0;
88. OH_LOG_INFO(LOG_APP, "JSVM API TEST: %{public}s", log);
89. return nullptr;
90. }

92. // 注册consoleinfo的方法
93. JSVM_CallbackStruct param[] = {
94. {.data = nullptr, .callback = ConsoleInfo},
95. };
96. JSVM_PropertyDescriptor descriptor[] = {
97. {"consoleinfo", NULL, &param[0], NULL, NULL, NULL, JSVM_DEFAULT},
98. };

100. static int32_t TestJSVM() {
101. JSVM_InitOptions init_options;
102. memset(&init_options, 0, sizeof(init_options));
103. if (g_aa == 0) {
104. OH_JSVM_Init(&init_options);
105. g_aa++;
106. }
107. // 创建JavaScript虚拟机实例，打开虚拟机作用域
108. JSVM_VM vm;
109. JSVM_CreateVMOptions options;
110. memset(&options, 0, sizeof(options));
111. CHECK(OH_JSVM_CreateVM(&options, &vm));
112. JSVM_VMScope vm_scope;
113. CHECK(OH_JSVM_OpenVMScope(vm, &vm_scope));

115. JSVM_Env env;
116. CHECK(OH_JSVM_CreateEnv(vm, sizeof(descriptor) / sizeof(descriptor[0]), descriptor, &env));
117. JSVM_EnvScope envScope;
118. CHECK_RET(OH_JSVM_OpenEnvScope(env, &envScope));
119. JSVM_HandleScope handlescope;
120. CHECK_RET(OH_JSVM_OpenHandleScope(env, &handlescope));
121. JSVM_Value sourcecodevalue;
122. CHECK_RET(OH_JSVM_CreateStringUtf8(env, STR_TASK, strlen(STR_TASK), &sourcecodevalue));
123. JSVM_Script script;
124. CHECK_RET(OH_JSVM_CompileScript(env, sourcecodevalue, nullptr, 0, true, nullptr, &script));
125. JSVM_Value result;
126. CHECK_RET(OH_JSVM_RunScript(env, script, &result));

128. // 关闭并销毁环境和虚拟机
129. CHECK_RET(OH_JSVM_CloseHandleScope(env, handlescope));
130. CHECK_RET(OH_JSVM_CloseEnvScope(env, envScope));
131. CHECK(OH_JSVM_DestroyEnv(env));
132. CHECK(OH_JSVM_CloseVMScope(vm, vm_scope));
133. CHECK(OH_JSVM_DestroyVM(vm));
134. return 0;
135. }
```

某次测试的输出：

```
1. JSVM API TEST: [base] Time cost: 414 ms
2. JSVM API TEST: [opt] Time cost: 148 ms
```
