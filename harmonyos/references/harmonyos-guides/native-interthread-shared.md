---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/native-interthread-shared
title: C++线程间数据共享场景
breadcrumb: 指南 > 应用框架 > ArkTS（方舟编程语言） > ArkTS并发 > 应用多线程开发实践 > 应用多线程开发实践案例 > C++线程间数据共享场景
category: harmonyos-guides
scraped_at: 2026-04-28T07:38:41+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:07196fa8fb67dc6e222483f23b5397557a7cbeee35c064d196fa1f08deaa6474
---

在C++层进行多线程并发计算时，需要在每个C++线程上创建ArkTS执行环境，直接调用API。这样可以避免在非UI主线程回调时等待UI主线程的API调用结果。同时，还需要在C++线程之间共享和操作Sendable对象。

为了支持此类场景，C++线程需要能够创建并调用ArkTS，同时支持对Sendable对象进行多线程共享和操作。

## 在C++线程上调用ArkTS能力

使用Node-API接口在C++线程中创建ArkTS运行环境并调用的方法，可以参考[使用Node-API接口创建ArkTS运行时环境](use-napi-ark-runtime.md)。

核心代码片段如下所示：

ArkTS文件定义。

```
1. @Sendable
2. export class SendableObjTest {
3. static newSendable() {
4. return 1024;
5. }
6. }
```

实现Native加载ArkTS模块的能力。

```
1. #include <thread>

3. #include "napi/native_api.h"

5. static void* g_serializationData = nullptr;
6. static void* CreateEnvAndSendSendable(void*)
7. {
8. // 1. 创建基础运行环境
9. napi_env env = nullptr;
10. napi_status ret = napi_create_ark_runtime(&env);
11. if (ret != napi_ok) {
12. std::abort();
13. }
14. // 2. 加载自定义模块，假定SendableObjTest中提供创建sendable对象的方法newSendable
15. napi_value test = nullptr;
16. ret = napi_load_module_with_info(
17. env, "entry/src/main/ets/pages/SendableObjTest", "com.example.myapplication/entry", &test);
18. if (ret != napi_ok) {
19. std::abort();
20. }
21. napi_value sendableObjTest = nullptr;
22. ret = napi_get_named_property(env, test, "SendableObjTest", &sendableObjTest);
23. if (ret != napi_ok) {
24. std::abort();
25. }
26. // 3. 使用ArkTS中的newSendable，假设sendableObjTest中有一个函数newSendable能返回sendable对象
27. napi_value newSendable = nullptr;
28. ret = napi_get_named_property(env, sendableObjTest, "newSendable", &newSendable);
29. if (ret != napi_ok) {
30. std::abort();
31. }
32. // 4. 调用newSendable函数返回新创建的sendable对象，并保存在result中
33. napi_value result = nullptr;
34. ret = napi_call_function(env, sendableObjTest, newSendable, 0, nullptr, &result);
35. if (ret != napi_ok) {
36. std::abort();
37. }
38. // 5. 序列化sendable对象
39. napi_value undefined;
40. napi_get_undefined(env, &undefined);
41. ret = napi_serialize(env, result, undefined, undefined, &g_serializationData);
42. if (ret != napi_ok) {
43. std::abort();
44. }
45. return nullptr;
46. }
```

主要步骤包括：创建执行环境、加载模块、查找并调用模块函数（或直接通过Node-API接口创建Sendable对象），最后销毁执行环境。加载模块的详细信息，请参见[使用Node-API接口进行模块加载](use-napi-load-module-with-info.md)。查找并调用函数及更多Node-API接口能力，请参见[Node-API](../harmonyos-references/napi.md)。

## 在C++线程之间操作Sendable共享对象

在C++中调用ArkTS能力后，需要通过序列化和反序列化跨线程传递。napi\_value不是多线程安全的，不能直接在多线程之间操作和共享。

下面代码例子说明了如何序列化和反序列化传递对象，注意因为Sendable共享对象是引用传递，所以序列化不会产生另外一份拷贝数据，而是直接传递对象引用到反序列化线程，所以在性能上相比非Sendable对象的序列化和反序列化更为高效。

ArkTS文件定义。

```
1. @Sendable
2. export class SendableObjTest {
3. static newSendable() {
4. return 1024;
5. }
6. }
```

在Native中实现两个线程的序列化和反序列化Sendable的逻辑。

```
1. #include <thread>

3. #include "napi/native_api.h"

5. static void* g_serializationData = nullptr;
6. static void* CreateEnvAndSendSendable(void*)
7. {
8. // 1. 创建基础运行环境
9. napi_env env = nullptr;
10. napi_status ret = napi_create_ark_runtime(&env);
11. if (ret != napi_ok) {
12. std::abort();
13. }
14. // 2. 加载自定义模块，假定SendableObjTest中提供创建sendable对象的方法newSendable
15. napi_value test = nullptr;
16. ret = napi_load_module_with_info(
17. env, "entry/src/main/ets/pages/SendableObjTest", "com.example.myapplication/entry", &test);
18. if (ret != napi_ok) {
19. std::abort();
20. }
21. napi_value sendableObjTest = nullptr;
22. ret = napi_get_named_property(env, test, "SendableObjTest", &sendableObjTest);
23. if (ret != napi_ok) {
24. std::abort();
25. }
26. // 3. 使用ArkTS中的newSendable，假设sendableObjTest中有一个函数newSendable能返回sendable对象
27. napi_value newSendable = nullptr;
28. ret = napi_get_named_property(env, sendableObjTest, "newSendable", &newSendable);
29. if (ret != napi_ok) {
30. std::abort();
31. }
32. // 4. 调用newSendable函数返回新创建的sendable对象，并保存在result中
33. napi_value result = nullptr;
34. ret = napi_call_function(env, sendableObjTest, newSendable, 0, nullptr, &result);
35. if (ret != napi_ok) {
36. std::abort();
37. }
38. // 5. 序列化sendable对象
39. napi_value undefined;
40. napi_get_undefined(env, &undefined);
41. ret = napi_serialize(env, result, undefined, undefined, &g_serializationData);
42. if (ret != napi_ok) {
43. std::abort();
44. }
45. return nullptr;
46. }

48. static void* CreateEnvAndReceiveSendable(void*)
49. {
50. // 1. 创建基础运行环境
51. napi_env env = nullptr;
52. napi_status ret = napi_create_ark_runtime(&env);
53. if (ret != napi_ok) {
54. std::abort();
55. }
56. // 2. 反序列化获取sendable共享对象，结果保存在result中，这个result就可以通过napi接口进行各种操作了
57. napi_value result = nullptr;
58. ret = napi_deserialize(env, g_serializationData, &result);
59. if (ret != napi_ok) {
60. std::abort();
61. }
62. // 3. 删除序列化数据
63. ret = napi_delete_serialization_data(env, g_serializationData);
64. if (ret != napi_ok) {
65. std::abort();
66. }
67. napi_valuetype valuetype0;
68. napi_typeof(env, result, &valuetype0);
69. if (valuetype0 != napi_number) {
70. std::abort();
71. }
72. int value0;
73. napi_get_value_int32(env, result, &value0);
74. // 1024是判断ArkTS返回的结果是否正确
75. if (value0 != 1024) {
76. std::abort();
77. }
78. return nullptr;
79. }

81. static napi_value TestSendSendable([[maybe_unused]] napi_env env, [[maybe_unused]] napi_callback_info info)
82. {
83. std::thread t1(CreateEnvAndSendSendable, nullptr);
84. t1.join();
85. std::thread t2(CreateEnvAndReceiveSendable, nullptr);
86. t2.join();
87. return nullptr;
88. }

90. EXTERN_C_START
91. static napi_value Init(napi_env env, napi_value exports)
92. {
93. napi_property_descriptor desc[] = { { "testSendSendable", nullptr, TestSendSendable, nullptr, nullptr, nullptr,
94. napi_default, nullptr } };
95. napi_define_properties(env, exports, sizeof(desc) / sizeof(desc[0]), desc);
96. return exports;
97. }
98. EXTERN_C_END

100. static napi_module demoModule = {
101. .nm_version = 1,
102. .nm_flags = 0,
103. .nm_filename = nullptr,
104. .nm_register_func = Init,
105. .nm_modname = "entry",
106. .nm_priv = ((void*)0),
107. .reserved = { 0 },
108. };

110. extern "C" __attribute__((constructor)) void RegisterEntryModule(void)
111. {
112. napi_module_register(&demoModule);
113. }
```

```
1. export const testSendSendable: () => void;
```

UI主线程发起调用。

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';
2. import testNapi from 'libentry.so';
3. import { SendableObjTest } from './SendableObjTest'

5. @Entry
6. @Component
7. struct Index {
8. @State message: string = 'Hello World';

10. build() {
11. Row() {
12. Column() {
13. Text(this.message)
14. .fontSize(50)
15. .fontWeight(FontWeight.Bold)
16. .onClick(() => {
17. SendableObjTest.newSendable()
18. hilog.info(0x0000, 'testTag', 'Test send Sendable begin');
19. testNapi.testSendSendable();
20. hilog.info(0x0000, 'testTag', 'Test send Sendable end');
21. this.message = 'success';
22. })
23. }
24. .width('100%')
25. }
26. .height('100%')
27. }
28. }
```

整个过程主要包括的逻辑实现为：

1. 在UI主线程中创建ArkTS运行环境，并发起一个C++子线程创建Sendable对象，保存到result中，然后将result引用的Sendable对象序列化到全局序列化数据serializationData中。
2. 当这些流程完成后，发起另外一个C++子线程，并在这个新的线程中创建ArkTS运行环境。然后再通过反序列化接口从serializationData中反序列化出UI主线程创建的Sendable对象，并保存到result中，从而实现了Sendable对象的跨C++线程传递。反序列化完成后，需要销毁反序列化数据避免内存泄露。这时UI主线程和子线程都同时持有这个Sendable共享对象，即可通过Node-API进行对象操作，比如读写或者传递到ArkTS层等。

   说明

   操作对象需要符合Sendable对象的规则，具体可见[Sendable使用规则与约束](sendable-constraints.md)。
