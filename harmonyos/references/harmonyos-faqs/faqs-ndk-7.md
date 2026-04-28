---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-7
title: 如何导出C++自定义类，导出后如何在ArkTS侧进行类方法调用
breadcrumb: FAQ > 应用框架开发 > NDK开发 > NDK开发 > 如何导出C++自定义类，导出后如何在ArkTS侧进行类方法调用
category: harmonyos-faqs
scraped_at: 2026-04-28T08:24:29+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:02e39dcf8cd1864828c433c1ddf2e82c1e2c44221e0b44942eb139b9210837c3
---

可以通过 napi\_define\_class 建立 ArkTS 类与 C++ 侧的映射关系，并将对应的对象挂载到 export 上导出。在 index.d.ts 文件中定义 ArkTS 侧类接口，实现对类的调用。

参考代码如下：

C++侧定义类。

```
1. // MyDemo.h Define C++classes
2. class MyDemo {
3. public:
4. MyDemo(std::string m_name);
5. MyDemo();
6. ~MyDemo();
7. std::string name;
8. int add(int a, int b);
9. int sub(int a, int b);
10. };
```

[MyDemo.h](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/Ndk/ndk1/nativeClass/src/main/cpp/MyDemo.h#L13-L22)

在hello.cpp中完成ArkTS类与C++的映射，并将其挂载到export上。

```
1. // ArkTS Object Constructor
2. static napi_value JsConstructor(napi_env env, napi_callback_info info) {
3. // Create Napi object
4. napi_value jDemo = nullptr;
5. size_t argc = 0;
6. napi_value args[1] = {0};
7. // Get constructor input parameters
8. napi_get_cb_info(env, info, &argc, args, &jDemo, nullptr);
9. // Parameters passed in args [0] js
10. char name[50];
11. size_t result = 0;
12. napi_get_value_string_utf8(env, args[0], name, sizeof(name) + 1, &result);
13. // Create C++objects
14. MyDemo *cDemo = new MyDemo(name);
15. OH_LOG_INFO(LOG_APP, "%{public}s", (cDemo->name).c_str());
16. // Set the JS object name attribute
17. napi_set_named_property(env, jDemo, "name", args[0]);
18. // Binding JS objects with C++objects
19. napi_wrap(
20. env, jDemo, cDemo,
21. // Define callback function for recycling JS objects, used to destroy C++objects and prevent memory leaks
22. [](napi_env env, void *finalize_data, void *finalize_hint) {
23. MyDemo *cDemo = (MyDemo *)finalize_data;
24. delete cDemo;
25. cDemo = nullptr;
26. },
27. nullptr, nullptr);
28. return jDemo;
29. }
30. // ArkTS object add function
31. static napi_value JsAdd(napi_env env, napi_callback_info info) {
32. size_t argc = 2;
33. napi_value args[2] = {nullptr};
34. napi_value jDemo = nullptr;
35. napi_get_cb_info(env, info, &argc, args, &jDemo, nullptr);
36. MyDemo *cDemo = nullptr;
37. // Convert ArkTS object to c object
38. napi_unwrap(env, jDemo, (void **)&cDemo);
39. // Get parameters passed by ArkTS
40. int value0;
41. napi_get_value_int32(env, args[0], &value0);
42. int value1;
43. napi_get_value_int32(env, args[1], &value1);
44. int cResult = cDemo->add(value0, value1);
45. napi_value jResult;
46. napi_create_int32(env, cResult, &jResult);
47. return jResult;
48. }
49. // ArkTS object sub function
50. static napi_value JsSub(napi_env env, napi_callback_info info) {
51. size_t argc = 2;
52. napi_value args[2] = {nullptr};
53. napi_value jDemo = nullptr;
54. napi_get_cb_info(env, info, &argc, args, &jDemo, nullptr);
55. MyDemo *cDemo = nullptr;
56. // Convert ArkTS object to c object
57. napi_unwrap(env, jDemo, (void **)&cDemo);
58. // Get parameters passed by ArkTS
59. int value0;
60. napi_get_value_int32(env, args[0], &value0);
61. int value1;
62. napi_get_value_int32(env, args[1], &value1);
63. int cResult = cDemo->sub(value0, value1);
64. napi_value jResult;
65. napi_create_int32(env, cResult, &jResult);
66. return jResult;
67. }
68. static napi_value Add(napi_env env, napi_callback_info info) {
69. size_t requireArgc = 2;
70. size_t argc = 2;
71. napi_value args[2] = {nullptr};
72. napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);
73. napi_valuetype valuetype0;
74. napi_typeof(env, args[0], &valuetype0);
75. napi_valuetype valuetype1;
76. napi_typeof(env, args[1], &valuetype1);
77. int value0;
78. napi_get_value_int32(env, args[0], &value0);
79. int value1;
80. napi_get_value_int32(env, args[1], &value1);
81. MyDemo *demo = new MyDemo();
82. // Call functions in so to perform operations
83. int result = demo->add(value0, value1);
84. napi_value sum;
85. napi_create_int32(env, result, &sum);
86. delete demo;
87. return sum;
88. }
89. static napi_value Sub(napi_env env, napi_callback_info info) {
90. size_t argc = 2;
91. napi_value args[2] = {nullptr};
92. napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);
93. napi_valuetype valuetype0;
94. napi_typeof(env, args[0], &valuetype0);
95. napi_valuetype valuetype1;
96. napi_typeof(env, args[1], &valuetype1);
97. int value0;
98. napi_get_value_int32(env, args[0], &value0);
99. int value1;
100. napi_get_value_int32(env, args[1], &value1);
101. MyDemo *demo = new MyDemo();
102. // Call functions in so to perform operations
103. int result = demo->sub(value0, value1);
104. napi_value num;
105. napi_create_int32(env, result, &num);
106. delete demo;
107. return num;
108. }

110. EXTERN_C_START
111. static napi_value Init(napi_env env, napi_value exports) {
112. // Define the methods that modules need to be exposed externally
113. napi_property_descriptor desc[] = {{"add", nullptr, Add, nullptr, nullptr, nullptr, napi_default, nullptr},
114. {"sub", nullptr, Sub, nullptr, nullptr, nullptr, napi_default, nullptr}};
115. napi_define_properties(env, exports, sizeof(desc) / sizeof(desc[0]), desc);
116. // Establish the mapping relationship between ArkTS class and C++side through napi_fine_class, and then mount the corresponding object onto export
117. napi_property_descriptor classProp[] = {{"add", nullptr, JsAdd, nullptr, nullptr, nullptr, napi_default, nullptr},
118. {"sub", nullptr, JsSub, nullptr, nullptr, nullptr, napi_default, nullptr}};
119. napi_value jDemo = nullptr;
120. const char *jDemoName = "MyDemo";
121. // Establish an association between ArkTS constructor and C++methods, specifying 2 props
122. napi_define_class(env, jDemoName, sizeof(jDemoName), JsConstructor, nullptr,
123. sizeof(classProp) / sizeof(classProp[0]), classProp, &jDemo);
124. napi_set_named_property(env, exports, jDemoName, jDemo);
125. return exports;
126. }
127. EXTERN_C_END
```

[hello.cpp](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/Ndk/ndk1/nativeClass/src/main/cpp/hello.cpp#L9-L135)

在index.d.ts文件中定义ArkTS类。

```
1. declare namespace testNapi {
2. const add: (a: number, b: number) => number;
3. const sub: (a: number, b: number) => number;
4. // Defining the ArkTS Interface
5. class MyDemo {
6. constructor(name:string)
7. name: string
8. add(a: number, b: number): number
9. sub(a: number, b: number): number
10. }
11. }
12. export default testNapi;
```

[Index.d.ts](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/Ndk/ndk1/nativeClass/src/main/cpp/types/libentry/Index.d.ts#L5-L16)

在ArkTS侧实现调用。

```
1. import testNapi from 'libentry.so';
2. // ...
3. // ...
4. new testNapi.MyDemo('abc');
5. hilog.info(0x0000, 'testTag', 'Test NAPI 2 + 3 = %{public}d', testNapi.add(2, 3));
6. hilog.info(0x0000, 'testTag', 'Test NAPI 2 - 3 = %{public}d', testNapi.sub(2, 3));
7. // ...
```

[MyDemo.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/Ndk/ndk1/nativeClass/src/main/ets/pages/MyDemo.ets#L6-L14)
