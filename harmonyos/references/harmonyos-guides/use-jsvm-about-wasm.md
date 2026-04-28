---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/use-jsvm-about-wasm
title: 使用JSVM-API接口进行WebAssembly模块相关开发
breadcrumb: 指南 > NDK开发 > 代码开发 > 使用JSVM-API实现JS与C/C++语言交互 > JSVM-API使用指导 > 使用JSVM-API接口进行WebAssembly模块相关开发
category: harmonyos-guides
scraped_at: 2026-04-28T07:54:16+08:00
doc_updated_at: 2026-03-17
content_hash: sha256:4da0fe162e1692366fbf3d58b6fbed62ffa98513c9b125bc1761c8a54c670004
---

## 简介

JSVM-API WebAssembly 接口提供了 WebAssembly 字节码编译、WebAssembly 函数优化、WebAssembly cache 序列化和反序列化的能力。

权限要求：WebAssembly相关接口需要应用拥有JIT权限才能执行，可参考[JSVM 申请JIT权限指导](jsvm-apply-jit-profile.md)申请对应权限。

运行限制：当前 JSVM 版本在坚盾守护模式下将禁用 WebAssembly 全部功能模块。开发者需针对此限制进行应用兼容性评估，具体技术规范详见[JSVM 坚盾守护模式](jsvm-secure-shield-mode.md)。

## 基本概念

* **wasm module**：表示一个 WebAssembly 模块，(WebAssembly 简称为wasm)，通过OH\_JSVM\_CompileWasmModule可以将wasm字节码或wasm cache创建为wasm module。通过 OH\_JSVM\_IsWasmModuleObject 接口可以判断一个 JSVM\_Value 是否是一个 wasm module。
* **wasm function**：表示 wasm module 中定义的函数，wasm function 在导出后被外部代码使用。OH\_JSVM\_CompileWasmFunction 接口提供了将 wasm function 编译为优化后的机器码的能力，方便开发者对指定 wasm function 提前编译和函数粒度的并行编译。
* **wasm cache**：对 wasm module 中的机器码进行序列化，生成的数据被称为 wasm cache。wasm cache 的创建和释放接口分别为 OH\_JSVM\_CreateWasmCache 和 OH\_JSVM\_ReleaseCache (对应的 cacheType 为 JSVM\_CACHE\_TYPE\_WASM)。

## 接口说明

| 接口 | 功能说明 |
| --- | --- |
| OH\_JSVM\_CompileWasmModule | 将 wasm 字节码同步编译为 wasm module。如果提供了 cache 参数，先尝试将 cache 反序列化为 wasm module，反序列化失败后再执行编译。如果没有 JIT 权限支持，则打印一行日志提示开发者。 |
| OH\_JSVM\_CompileWasmFunction | 将 wasm module 中指定编号的函数编译为优化后的机器码，目前只使能了最高的优化等级，函数编号的合法性由接口调用者保证。如果没有 JIT 权限支持，则打印一行日志提示开发者。 |
| OH\_JSVM\_IsWasmModuleObject | 判断传入的值是否是wasm module。 |
| OH\_JSVM\_CreateWasmCache | 将 wasm module 中的机器码序列化为 wasm cache，如果 wasm module 不包含机器码，会导致序列化失败。如果没有 JIT 权限支持，则打印一行日志提示开发者。 |
| OH\_JSVM\_ReleaseCache | 释放由 JSVM 接口生成的 cache。传入的 cacheType 和 cacheData 必须匹配，否则会产生未定义行为。 |

## code cache 校验规格说明

| 规格 | 规格说明 |
| --- | --- |
| 完整性校验 | 由用户保证 |
| 兼容性校验 | 校验生成 cache 的 JSVM 版本与编译选项是否与当前一致 |
| 一致性校验 | 由用户保证 |

## 使用示例

参考 [使用JSVM-API实现JS与C/C++语言交互开发流程](use-jsvm-process.md) 了解 JSVM-API 接口开发流程。本文仅展示接口对应的 C++ 代码。

cpp 部分代码：

```
1. // hello.cpp
2. #include "napi/native_api.h"
3. #include "ark_runtime/jsvm.h"
4. #include <hilog/log.h>
5. #include <vector>

7. #ifndef CHECK_STATUS
8. #define CHECK_STATUS(cond)                           \
9. do {                                             \
10. if (!(cond)) {                               \
11. OH_LOG_ERROR(LOG_APP, "CHECK FAILED");   \
12. }                                            \
13. } while (0)
14. #endif

16. // 判断一个 JSVM_Value 是否是 wasm module
17. static bool IsWasmModuleObject(JSVM_Env env, JSVM_Value value) {
18. bool result = false;
19. JSVM_Status status = OH_JSVM_IsWasmModuleObject(env, value, &result);
20. CHECK_STATUS(status == JSVM_OK);
21. return result;
22. }

24. // 由 C 字符串创建 JSVM string
25. static JSVM_Value CreateString(JSVM_Env env, const char *str) {
26. JSVM_Value jsvmStr;
27. JSVM_Status status = OH_JSVM_CreateStringUtf8(env, str, JSVM_AUTO_LENGTH, &jsvmStr);
28. CHECK_STATUS(status == JSVM_OK);
29. return jsvmStr;
30. }

32. // 由 C int32_t 创建 JSVM number
33. static JSVM_Value CreateInt32(JSVM_Env env, int32_t val) {
34. JSVM_Value jsvmInt32;
35. JSVM_Status status = OH_JSVM_CreateInt32(env, val, &jsvmInt32);
36. CHECK_STATUS(status == JSVM_OK);
37. return jsvmInt32;
38. }

40. // 对 wasm module 进行实例化
41. static JSVM_Value InstantiateWasmModule(JSVM_Env env, JSVM_Value wasmModule) {
42. JSVM_Status status = JSVM_OK;
43. JSVM_Value globalThis;
44. status = OH_JSVM_GetGlobal(env, &globalThis);
45. CHECK_STATUS(status == JSVM_OK);

47. JSVM_Value webAssembly;
48. status = OH_JSVM_GetProperty(env, globalThis, CreateString(env, "WebAssembly"), &webAssembly);
49. CHECK_STATUS(status == JSVM_OK);

51. JSVM_Value webAssemblyInstance;
52. status = OH_JSVM_GetProperty(env, webAssembly, CreateString(env, "Instance"), &webAssemblyInstance);
53. CHECK_STATUS(status == JSVM_OK);

55. JSVM_Value instance;
56. JSVM_Value argv[] = {wasmModule};
57. status = OH_JSVM_NewInstance(env, webAssemblyInstance, 1, argv, &instance);
58. CHECK_STATUS(status == JSVM_OK);
59. return instance;
60. }

62. // 获取 wasm 字节码 (add 模块)
63. static std::vector<uint8_t> GetAddWasmBuffer() {
64. /* 以下 wasmBuffer 对应的 wasm 字节码文本格式如下所示，只包含了一个函数 add
65. (module
66. (func $add (param $lhs i32) (param $rhs i32) (result i32)
67. local.get $lhs
68. local.get $rhs
69. i32.add
70. )
71. (export "add" (func $add))
72. )
73. */
74. std::vector<uint8_t> wasmBuffer = {0x00, 0x61, 0x73, 0x6d, 0x01, 0x00, 0x00, 0x00, 0x01, 0x07, 0x01,
75. 0x60, 0x02, 0x7f, 0x7f, 0x01, 0x7f, 0x03, 0x02, 0x01, 0x00, 0x07,
76. 0x07, 0x01, 0x03, 0x61, 0x64, 0x64, 0x00, 0x00, 0x0a, 0x09, 0x01,
77. 0x07, 0x00, 0x20, 0x00, 0x20, 0x01, 0x6a, 0x0b};
78. return wasmBuffer;
79. }

81. // 验证 wasm instance 功能 (add 模块)
82. static void VerifyAddWasmInstance(JSVM_Env env, JSVM_Value wasmInstance) {
83. JSVM_Status status = JSVM_OK;
84. // 从 wasm instance 获取 exports.add 函数
85. JSVM_Value exports;
86. status = OH_JSVM_GetProperty(env, wasmInstance, CreateString(env, "exports"), &exports);
87. CHECK_STATUS(status == JSVM_OK);

89. JSVM_Value add;
90. status = OH_JSVM_GetProperty(env, exports, CreateString(env, "add"), &add);
91. CHECK_STATUS(status == JSVM_OK);

93. // 执行 exports.add(1, 2)，期望得到结果 3
94. JSVM_Value undefined;
95. OH_JSVM_GetUndefined(env, &undefined);
96. JSVM_Value one = CreateInt32(env, 1);
97. JSVM_Value two = CreateInt32(env, 2);
98. JSVM_Value argv[] = {one, two};
99. JSVM_Value result;
100. status = OH_JSVM_CallFunction(env, undefined, add, 2, argv, &result);
101. CHECK_STATUS(status == JSVM_OK);
102. int32_t resultInt32 = 0;
103. OH_JSVM_GetValueInt32(env, result, &resultInt32);
104. CHECK_STATUS(resultInt32 == 3);
105. }

107. // WebAssembly demo 主函数
108. static JSVM_Value WasmDemo(JSVM_Env env, JSVM_CallbackInfo info) {
109. JSVM_Status status = JSVM_OK;
110. std::vector<uint8_t> wasmBuffer = GetAddWasmBuffer();
111. uint8_t *wasmBytecode = wasmBuffer.data();
112. size_t wasmBytecodeLength = wasmBuffer.size();
113. JSVM_Value wasmModule;
114. // 根据 wasm 字节码得到 wasm module
115. status = OH_JSVM_CompileWasmModule(env, wasmBytecode, wasmBytecodeLength, NULL, 0, NULL, &wasmModule);
116. CHECK_STATUS(status == JSVM_OK);
117. CHECK_STATUS(IsWasmModuleObject(env, wasmModule));

119. // 对当前 wasm module 中定义的第一个函数 (即 add) 执行编译优化
120. int32_t functionIndex = 0;
121. // 注意：当前只支持 high level optimization，即传入 JSVM_WASM_OPT_BASELINE 和传入 JSVM_WASM_OPT_HIGH 效果是一样的
122. status = OH_JSVM_CompileWasmFunction(env, wasmModule, functionIndex, JSVM_WASM_OPT_HIGH);
123. CHECK_STATUS(status == JSVM_OK);
124. // 对编译得到的 wasm module 进行实例化
125. JSVM_Value wasmInstance = InstantiateWasmModule(env, wasmModule);
126. // 对实例化的 wasm instance 中的函数进行功能验证
127. VerifyAddWasmInstance(env, wasmInstance);

129. // 创建 wasm cache
130. const uint8_t *wasmCacheData = NULL;
131. size_t wasmCacheLength = 0;
132. status = OH_JSVM_CreateWasmCache(env, wasmModule, &wasmCacheData, &wasmCacheLength);
133. CHECK_STATUS(status == JSVM_OK);
134. // 期望 wasm cache 创建成功
135. CHECK_STATUS(wasmCacheData != NULL);
136. CHECK_STATUS(wasmCacheLength > 0);

138. // 通过将 wasm cache 赋值来模拟 cache 持久化，实际使用场景可能将 wasm cache 保存到文件
139. std::vector<uint8_t> cacheBuffer(wasmCacheData, wasmCacheData + wasmCacheLength);

141. // cache 一旦保存完成后，需要显式释放，以免发生内存泄露
142. // 注意：传入的 JSVM_CacheType 必须匹配
143. status = OH_JSVM_ReleaseCache(env, wasmCacheData, JSVM_CACHE_TYPE_WASM);
144. CHECK_STATUS(status == JSVM_OK);

146. // 使用 wasm code 反序列化来生成 wasm module
147. bool cacheRejected = false;
148. JSVM_Value wasmModule2;
149. status = OH_JSVM_CompileWasmModule(env, wasmBytecode, wasmBytecodeLength, cacheBuffer.data(), cacheBuffer.size(),
150. &cacheRejected, &wasmModule2);

152. // 传入的 wasm cache 如果是匹配的，且内部校验通过 (如版本)，则会接受 cache
153. CHECK_STATUS(!cacheRejected);
154. CHECK_STATUS(IsWasmModuleObject(env, wasmModule2));

156. // 对反序列化得到的 wasmModule2 进行同样的操作：函数编译、实例化、验证功能，期望也都是通过的
157. status = OH_JSVM_CompileWasmFunction(env, wasmModule2, functionIndex, JSVM_WASM_OPT_HIGH);
158. CHECK_STATUS(status == JSVM_OK);

160. JSVM_Value wasmInstance2 = InstantiateWasmModule(env, wasmModule2);
161. VerifyAddWasmInstance(env, wasmInstance2);

163. JSVM_Value result;
164. OH_JSVM_GetBoolean(env, true, &result);
165. return result;
166. }

168. // WasmDemo 方法注册回调
169. static JSVM_CallbackStruct param[] = {
170. {.data = nullptr, .callback = WasmDemo}
171. };
172. static JSVM_CallbackStruct *method = param;
173. // 将 C++ callback WasmDemo 函数注册为 JSVM globalThis.wasmDemo 属性，供 JS 侧调用
174. static JSVM_PropertyDescriptor descriptor[] = {
175. {"wasmDemo", nullptr, method++, nullptr, nullptr, nullptr, JSVM_DEFAULT},
176. };

178. // 样例测试js
179. const char *srcCallNative = R"JS(wasmDemo())JS";
```

预期输出：无报错
