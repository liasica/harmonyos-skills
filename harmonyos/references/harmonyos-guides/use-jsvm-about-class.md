---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/use-jsvm-about-class
title: 使用JSVM-API接口进行class相关开发
breadcrumb: 指南 > NDK开发 > 代码开发 > 使用JSVM-API实现JS与C/C++语言交互 > JSVM-API使用指导 > 使用JSVM-API接口进行class相关开发
category: harmonyos-guides
scraped_at: 2026-04-28T07:54:18+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:d347cbd18f07dec5736ee7e93ea97007c0934e11e6f19093e63ee21e1802363a
---

## 简介

使用JSVM-API接口进行class相关开发，处理JavaScript中的类，例如定义类、构造实例等。

## 基本概念

在使用JSVM-API接口进行class相关开发时，需要理解以下基本概念：

* **类**：类是用于创建对象的模板。它提供了一种封装数据和行为的方式，以便于对数据进行处理和操作。类在JavaScript中是建立在原型（prototype）的基础上的，并且还引入了一些类独有的语法和语义。
* **实例**：实例是通过类创建具体的对象。类定义了对象的结构和行为，而实例则是类的具体表现。通过实例化类，我们可以访问类中定义的属性和方法，并且每个实例都具有自己的属性值。

## 接口说明

| 接口 | 功能说明 |
| --- | --- |
| OH\_JSVM\_NewInstance | 通过给定的构造函数，创建一个实例。 |
| OH\_JSVM\_GetNewTarget | 获取函数的元属性new.target。 |
| OH\_JSVM\_DefineClass | 用于在JavaScript中定义一个类，并与对应的C类进行封装和交互。它提供了创建类的构造函数、定义属性和方法的能力，支持C和JavaScript之间的数据交互。 |
| OH\_JSVM\_Wrap | 在JavaScript对象中封装原生实例。稍后可以使用OH\_JSVM\_Unwrap()解包原生实例。 |
| OH\_JSVM\_Unwrap | 解包先前封装在JavaScript对象中的原生实例。 |
| OH\_JSVM\_RemoveWrap | 解包先前封装在JavaScript对象中的原生实例，并释放封装。 |
| OH\_JSVM\_DefineClassWithOptions | 定义一个具有给定类名、构造函数、属性和回调处理程序、父类的JavaScript类，并根据传入了DefineClassOptions来决定是否需要为所定义的Class设置属性代理、预留internal-field槽位、为class作为函数进行调用时设置函数回调。 |

## 使用示例

JSVM-API接口开发流程参考[使用JSVM-API实现JS与C/C++语言交互开发流程](use-jsvm-process.md)，本文仅对接口对应C++相关代码进行展示。

### OH\_JSVM\_NewInstance

通过给定的构造函数，构建一个实例。

cpp部分代码

```
1. // hello.cpp
2. #include <string.h>
3. #include <fstream>

5. std::string ToString(JSVM_Env env, JSVM_Value val) {
6. JSVM_Value jsonString = nullptr;
7. JSVM_CALL(OH_JSVM_JsonStringify(env, val, &jsonString));
8. size_t totalLen = 0;
9. JSVM_CALL(OH_JSVM_GetValueStringUtf8(env, jsonString, nullptr, 0, &totalLen));
10. size_t needLen = totalLen + 1;
11. char* buff = new char[needLen];
12. std::memset(buff, 0, needLen);
13. JSVM_CALL(OH_JSVM_GetValueStringUtf8(env, jsonString, buff, needLen, &totalLen));
14. std::string str(buff);
15. delete[] buff;
16. return str;
17. }

19. // OH_JSVM_NewInstance的样例方法
20. static JSVM_Value NewInstance(JSVM_Env env, JSVM_CallbackInfo info) {
21. // 获取js侧传入的两个参数
22. size_t argc = 2;
23. JSVM_Value args[2] = {nullptr};
24. JSVM_CALL(OH_JSVM_GetCbInfo(env, info, &argc, args, nullptr, nullptr));
25. JSVM_Value result = nullptr;
26. // 调用OH_JSVM_NewInstance接口，实例化一个对象，将这个对象返回
27. JSVM_CALL(OH_JSVM_NewInstance(env, args[0], 1, &args[1], &result));
28. std::string str = ToString(env, result);
29. OH_LOG_INFO(LOG_APP, "NewInstance:%{public}s", str.c_str());
30. return nullptr;
31. }

33. // 通过给定的构造函数，构建一个实例。
34. // NewInstance注册回调
35. static JSVM_CallbackStruct param[] = {
36. {.data = nullptr, .callback = NewInstance},
37. };

39. static JSVM_CallbackStruct *method = param;

41. // NewInstance方法别名，供JS调用
42. static JSVM_PropertyDescriptor descriptor[] = {
43. {"newInstance", nullptr, method++, nullptr, nullptr, nullptr, JSVM_DEFAULT},
44. };
```

**样例JS**

```
1. const char *srcCallNative = R"JS(
2. function Fruit(name) {
3. this.name = name;
4. }
5. newInstance(Fruit, "apple");
6. )JS";
```

**执行结果**

在LOG中输出下面的结果：

```
1. NewInstance:{"name":"apple"}
```

### OH\_JSVM\_GetNewTarget

用于获取函数的元属性new.target值。在JavaScript中，new.target是一个特殊的元属性，用于检测函数或构造函数是否是通过 'new' 运算符被调用的。

### OH\_JSVM\_DefineClass

用于在JavaScript中定义一个类，并与对应的C类进行封装和交互。它提供了创建类的构造函数、定义属性和方法的能力，以及在C和JavaScript之间进行数据交互的支持。

cpp部分代码

```
1. // hello.cpp
2. #include <string>

4. JSVM_Value CreateInstance(JSVM_Env env, JSVM_CallbackInfo info) {
5. JSVM_Value newTarget;
6. // 获取构造函数的new.target值
7. JSVM_CALL(OH_JSVM_GetNewTarget(env, info, &newTarget));
8. OH_LOG_INFO(LOG_APP, "Create Instance");
9. OH_LOG_INFO(LOG_APP, "NAPI MyObject::New %{public}s", newTarget != nullptr ? "newTarget != nullptr" : "newTarget == nullptr");
10. JSVM_Value jsObject = nullptr;
11. JSVM_CALL(OH_JSVM_CreateObject(env, &jsObject));
12. JSVM_Value jsName = nullptr;
13. JSVM_CALL(OH_JSVM_CreateStringUtf8(env, "name", JSVM_AUTO_LENGTH, &jsName));
14. JSVM_Value jsValue = nullptr;
15. JSVM_CALL(OH_JSVM_CreateStringUtf8(env, "lilei", JSVM_AUTO_LENGTH, &jsValue));
16. JSVM_CALL(OH_JSVM_SetProperty(env, jsObject, jsName, jsValue));
17. return jsObject;
18. }

20. std::string ToString(JSVM_Env env, JSVM_Value val) {
21. JSVM_Value jsonString = nullptr;
22. JSVM_CALL(OH_JSVM_JsonStringify(env, val, &jsonString));
23. size_t totalLen = 0;
24. JSVM_CALL(OH_JSVM_GetValueStringUtf8(env, jsonString, nullptr, 0, &totalLen));
25. size_t needLen = totalLen + 1;
26. char* buff = new char[needLen];
27. std::memset(buff, 0, needLen);
28. JSVM_CALL(OH_JSVM_GetValueStringUtf8(env, jsonString, buff, needLen, &totalLen));
29. std::string str(buff);
30. delete[] buff;
31. return str;
32. }

34. // 封装c++中的自定义数据结构
35. JSVM_Value DefineClass(JSVM_Env env, JSVM_CallbackInfo info) {
36. JSVM_CallbackStruct param;
37. param.data = nullptr;
38. param.callback = CreateInstance;
39. JSVM_Value cons;
40. // 用于在JavaScript中定义一个类
41. JSVM_CALL(OH_JSVM_DefineClass(env, "MyObject", JSVM_AUTO_LENGTH, &param, 0, nullptr, &cons));
42. JSVM_Value instanceValue = nullptr;
43. // 作为class的构造函数调用
44. JSVM_CALL(OH_JSVM_NewInstance(env, cons, 0, nullptr, &instanceValue));
45. std::string str = ToString(env, instanceValue);
46. OH_LOG_INFO(LOG_APP, "NewInstance:%{public}s", str.c_str());

48. // 作为普通的函数调用
49. JSVM_Value global = nullptr;
50. JSVM_CALL(OH_JSVM_GetGlobal(env, &global));
51. JSVM_Value key;
52. JSVM_CALL(OH_JSVM_CreateStringUtf8(env, "Constructor", JSVM_AUTO_LENGTH, &key));
53. JSVM_CALL(OH_JSVM_SetProperty(env, global, key, cons));
54. JSVM_Value result = nullptr;
55. JSVM_CALL(OH_JSVM_CallFunction(env, global, cons, 0, nullptr, &result));
56. std::string buf = ToString(env, result);
57. OH_LOG_INFO(LOG_APP, "NewInstance:%{public}s", buf.c_str());
58. return nullptr;
59. }

61. // 注册DefineClass的方法
62. JSVM_CallbackStruct param[] = {
63. {.data = nullptr, .callback = DefineClass},
64. };

66. static JSVM_CallbackStruct *method = param;

68. // DefineClass方法别名，供JS调用
69. static JSVM_PropertyDescriptor descriptor[] = {
70. {"defineClass", nullptr, method++, nullptr, nullptr, nullptr, JSVM_DEFAULT},
71. };
```

**样例JS**

```
1. const char *srcCallNative = R"JS(
2. defineClass();
3. )JS";
```

**执行结果**

在LOG中输出下面的结果：

```
1. Create Instance

3. NAPI MyObject::New newTarget != nullptr

5. NewInstance:{"name":"lilei"}

7. Create Instance

9. NAPI MyObject::New newTarget == nullptr

11. NewInstance:{"name":"lilei"}
```

### OH\_JSVM\_Wrap

在JavaScript对象中封装原生实例。稍后可以使用OH\_JSVM\_Unwrap()解包原生实例

### OH\_JSVM\_Unwrap

解包JavaScript对象中先前封装的原生实例

### OH\_JSVM\_RemoveWrap

解包先前封装在JavaScript对象中的原生实例并释放封装

cpp部分代码

```
1. // hello.cpp
2. #include <string>

4. // OH_JSVM_GetNewTarget、OH_JSVM_DefineClass、OH_JSVM_Wrap、OH_JSVM_Unwrap、OH_JSVM_RemoveWrap的样例方法

6. // 自定义类结构体Object
7. struct Object {
8. std::string name;
9. int32_t age;
10. };

12. // 定义一个回调函数
13. static void DerefItem(JSVM_Env env, void *data, void *hint) {
14. OH_LOG_INFO(LOG_APP, "JSVM deref_item");
15. (void)hint;
16. }

18. static JSVM_Value WrapObject(JSVM_Env env, JSVM_CallbackInfo info) {
19. OH_LOG_INFO(LOG_APP, "JSVM wrap");
20. Object obj;
21. // 设置Object属性
22. obj.name = "lilei";
23. obj.age = 18;
24. Object *objPointer = &obj;
25. // 获取回调信息中的参数数量和将要被封装的值
26. size_t argc = 1;
27. JSVM_Value toWrap = nullptr;
28. JSVM_CALL(OH_JSVM_GetCbInfo(env, info, &argc, &toWrap, nullptr, nullptr));
29. // OH_JSVM_Wrap将自定义结构Object进行封装
30. JSVM_CALL(OH_JSVM_Wrap(env, toWrap, reinterpret_cast<void *>(objPointer), DerefItem, NULL, NULL));
31. Object *data;
32. // OH_JSVM_UnWrap解包先前封装在JavaScript对象中的原生实例
33. JSVM_CALL(OH_JSVM_Unwrap(env, toWrap, reinterpret_cast<void **>(&data)));
34. OH_LOG_INFO(LOG_APP, "JSVM name: %{public}s", data->name.c_str());
35. OH_LOG_INFO(LOG_APP, "JSVM age: %{public}d", data->age);
36. return nullptr;
37. }

39. static JSVM_Value RemoveWrap(JSVM_Env env, JSVM_CallbackInfo info) {
40. OH_LOG_INFO(LOG_APP, "JSVM removeWrap");
41. Object obj;
42. // 设置Object属性
43. obj.name = "lilei";
44. obj.age = 18;
45. Object *objPointer = &obj;
46. // 获取回调信息中的参数数量和将要被封装的值
47. size_t argc = 1;
48. JSVM_Value toWrap = nullptr;
49. JSVM_CALL(OH_JSVM_GetCbInfo(env, info, &argc, &toWrap, nullptr, nullptr));
50. // 将自定义结构Object封装
51. JSVM_CALL(OH_JSVM_Wrap(env, toWrap, reinterpret_cast<void *>(objPointer), DerefItem, NULL, NULL));
52. Object *data;
53. // 解包先前封装的object，并移除封装
54. JSVM_CALL(OH_JSVM_RemoveWrap(env, toWrap, reinterpret_cast<void **>(&objPointer)));
55. // 检查是否已被移除
56. JSVM_Status status = OH_JSVM_Unwrap(env, toWrap, reinterpret_cast<void **>(&data));
57. if (status != JSVM_OK) {
58. OH_LOG_INFO(LOG_APP, "JSVM OH_JSVM_RemoveWrap success");
59. }
60. return nullptr;
61. }

63. // WrapObject、RemoveWrap注册回调
64. static JSVM_CallbackStruct param[] = {
65. {.data = nullptr, .callback = WrapObject},
66. {.data = nullptr, .callback = RemoveWrap},
67. };
68. static JSVM_CallbackStruct *method = param;
69. // WrapObject、RemoveWrap方法别名，供JS调用
70. static JSVM_PropertyDescriptor descriptor[] = {
71. {"wrapObject", nullptr, method++, nullptr, nullptr, nullptr, JSVM_DEFAULT},
72. {"removeWrap", nullptr, method++, nullptr, nullptr, nullptr, JSVM_DEFAULT},
73. };
```

**样例JS**

```
1. const char *srcCallNative = R"JS(
2. class Obj {};
3. wrapObject(new Obj());
4. removeWrap(new Obj());
5. )JS";
```

**执行结果**

在LOG中输出下面的结果：

```
1. JSVM wrap

3. JSVM name: lilei

5. JSVM age: 18

7. JSVM removeWrap

9. JSVM OH_JSVM_RemoveWrap success

11. JSVM deref_item
```

### OH\_JSVM\_DefineClassWithOptions

**Note:**

传入的父类class必须是通过OH\_JSVM\_DefineClass系列接口创建出来的，否则被视为无效参数，返回JSVM\_INVALID\_ARG错误码。

目前支持以下的DefineClassOptions:

* JSVM\_DEFINE\_CLASS\_NORMAL: 按正常模式创建Class。默认缺省状态为JSVM\_DEFINE\_CLASS\_NORMAL状态。
* JSVM\_DEFINE\_CLASS\_WITH\_COUNT: 为所创建的Class预留interfield槽位。
* JSVM\_DEFINE\_CLASS\_WITH\_PROPERTY\_HANDLER: 为所创建的Class设置监听拦截属性以及设置作为函数调用时回调函数。

cpp部分代码

```
1. #include <string>
2. #include <memory>
3. static JSVM_PropertyHandlerConfigurationStruct propertyCfg{
4. nullptr, nullptr, nullptr, nullptr, nullptr, nullptr, nullptr, nullptr, nullptr, nullptr
5. };

7. static bool g_call_as_function_flag = false;
8. static bool g_set_named_property_flag = false;
9. static bool g_call_as_constructor_flag = false;
10. static bool g_properties_flag = false;

12. static JSVM_Value SetNamedPropertyCbInfo2(JSVM_Env env, JSVM_Value name, JSVM_Value property, JSVM_Value thisArg,
13. JSVM_Value data)
14. {
15. g_set_named_property_flag = true;
16. return property;
17. }

19. static JSVM_Value Add(JSVM_Env env, JSVM_CallbackInfo info) {
20. g_properties_flag = true;
21. size_t argc = 2;
22. JSVM_Value args[2];
23. OH_JSVM_GetCbInfo(env, info, &argc, args, NULL, NULL);
24. double num1 = 0;
25. double num2 = 0;
26. OH_JSVM_GetValueDouble(env, args[0], &num1);
27. OH_JSVM_GetValueDouble(env, args[1], &num2);
28. JSVM_Value sum = nullptr;
29. OH_JSVM_CreateDouble(env, num1 + num2, &sum);
30. return sum;
31. }

33. std::string ToString(JSVM_Env jsvm_env, JSVM_Value val)
34. {
35. JSVM_Value js_string;
36. OH_JSVM_CoerceToString(jsvm_env, val, &js_string);
37. size_t length = 0;
38. OH_JSVM_GetValueStringUtf8(jsvm_env, js_string, NULL, 0, &length);
39. size_t capacity = length + 1;
40. auto buffer = std::make_unique<char[]>(capacity);
41. size_t copy_length = 0;
42. OH_JSVM_GetValueStringUtf8(jsvm_env, js_string, buffer.get(), capacity, &copy_length);
43. std::string str(buffer.get());
44. return str;
45. }

47. JSVM_Value Run(JSVM_Env env, const char *s)
48. {
49. // 1. 将const char*转换成JS_String。
50. JSVM_Value str;
51. JSVM_CALL(OH_JSVM_CreateStringUtf8(env, s, JSVM_AUTO_LENGTH, &str));
52. // 2. 将JS_String转换成JS_Script。
53. JSVM_Script script;
54. OH_JSVM_CompileScript(env, str, nullptr, JSVM_AUTO_LENGTH,   false, nullptr, &script);
55. // 3. 执行JS_Script。
56. JSVM_Value result = nullptr;
57. OH_JSVM_RunScript(env, script, &result);
58. return result;
59. }

61. static JSVM_Value TestDefineClassWithOptions(JSVM_Env env, JSVM_CallbackInfo info)
62. {
63. g_call_as_function_flag = false;
64. g_set_named_property_flag = false;
65. g_call_as_constructor_flag = false;
66. g_properties_flag = false;
67. // 1. Define parent-class.
68. JSVM_Value parentClass = nullptr;
69. JSVM_CallbackStruct parentClassConstructor;
70. parentClassConstructor.data = nullptr;
71. parentClassConstructor.callback = [](JSVM_Env env, JSVM_CallbackInfo info) -> JSVM_Value {
72. JSVM_Value thisVar = nullptr;
73. OH_JSVM_GetCbInfo(env, info, nullptr, nullptr, &thisVar, nullptr);
74. return thisVar;
75. };
76. JSVM_Value fooVal;
77. OH_JSVM_CreateStringUtf8(env, "bar", JSVM_AUTO_LENGTH, &fooVal);
78. JSVM_PropertyDescriptor des[2];
79. des[0] = {
80. .utf8name = "foo",
81. .value = fooVal,
82. };
83. JSVM_CallbackStruct parentProperties[] = {
84. {.callback = Add, .data = nullptr},
85. };
86. des[1] = {
87. .utf8name = "add",
88. .method = &parentProperties[0],
89. };
90. JSVM_DefineClassOptions options[1];
91. options[0].id = JSVM_DEFINE_CLASS_WITH_COUNT;
92. options[0].content.num = 3;
93. JSVM_CALL(OH_JSVM_DefineClassWithOptions(env, "parentClass", JSVM_AUTO_LENGTH, &parentClassConstructor, 2, des,
94. nullptr, 1, options, &parentClass));

96. // 2. Define sub-class.
97. JSVM_Value subClass = nullptr;
98. JSVM_CallbackStruct subClassConstructor;
99. subClassConstructor.data = nullptr;
100. subClassConstructor.callback = [](JSVM_Env env, JSVM_CallbackInfo info) -> JSVM_Value {
101. JSVM_Value thisVar = nullptr;
102. g_call_as_constructor_flag = true;
103. OH_JSVM_GetCbInfo(env, info, nullptr, nullptr, &thisVar, nullptr);
104. return thisVar;
105. };
106. JSVM_DefineClassOptions subOptions[2];
107. JSVM_CallbackStruct callAsFuncParam;
108. callAsFuncParam.data = nullptr;
109. callAsFuncParam.callback = [](JSVM_Env env, JSVM_CallbackInfo info) -> JSVM_Value {
110. JSVM_Value thisVar = nullptr;
111. g_call_as_function_flag = true;
112. OH_JSVM_GetCbInfo(env, info, nullptr, nullptr, &thisVar, nullptr);
113. return thisVar;
114. };
115. propertyCfg.genericNamedPropertySetterCallback = SetNamedPropertyCbInfo2;
116. JSVM_PropertyHandler propertyHandler = {
117. .propertyHandlerCfg = &propertyCfg,
118. .callAsFunctionCallback = &callAsFuncParam,
119. };
120. subOptions[0].id = JSVM_DEFINE_CLASS_WITH_COUNT;
121. subOptions[0].content.num = 4;
122. subOptions[1].id = JSVM_DEFINE_CLASS_WITH_PROPERTY_HANDLER;
123. subOptions[1].content.ptr = &propertyHandler;
124. JSVM_CALL(OH_JSVM_DefineClassWithOptions(env, "subClass", JSVM_AUTO_LENGTH, &subClassConstructor, 0, nullptr,
125. parentClass, 2, subOptions, &subClass));
126. // 3. Verify the validity of 'constructor'.
127. JSVM_Value subInstance;
128. JSVM_CALL(OH_JSVM_NewInstance(env, subClass, 0, nullptr, &subInstance));

130. JSVM_Value globalVal;
131. OH_JSVM_GetGlobal(env, &globalVal);
132. OH_JSVM_SetNamedProperty(env, globalVal, "obj", subInstance);

134. // 4. Verify the validity of 'parentClass'.
135. JSVM_Value subRes = nullptr;
136. JSVM_CALL(OH_JSVM_GetNamedProperty(env, subInstance, "foo", &subRes));
137. if (ToString(env, subRes).compare("bar") != 0) {
138. OH_LOG_ERROR(LOG_APP, "Run OH_JSVM_DefineClassWithOptions: Failed");
139. }
140. // 5. Verify the validity of 'properties'.
141. Run(env, "obj.add(3, 4);");
142. // 6. Verify the validity of 'options'.
143. Run(env, "obj()");
144. Run(env, "obj.x = 123;");
145. if (g_call_as_function_flag &&
146. g_set_named_property_flag &&
147. g_call_as_constructor_flag &&
148. g_properties_flag) {
149. OH_LOG_INFO(LOG_APP, "Run OH_JSVM_DefineClassWithOptions: Success");
150. } else {
151. OH_LOG_ERROR(LOG_APP, "Run OH_JSVM_DefineClassWithOptions: Failed");
152. }
153. JSVM_Value checked;
154. OH_JSVM_GetBoolean(env, true, &checked);
155. return checked;
156. }

158. static JSVM_CallbackStruct param[] = {
159. {.data = nullptr, .callback = TestDefineClassWithOptions},
160. };
161. static JSVM_CallbackStruct *method = param;

163. static JSVM_PropertyDescriptor descriptor[] = {
164. {"testDefineClassWithOptions", nullptr, method++, nullptr, nullptr, nullptr, JSVM_DEFAULT},
165. };
```

**样例JS**

```
1. const char *srcCallNative = R"JS(testDefineClassWithOptions();)JS";
```

**执行结果**

在LOG中输出下面的结果：

```
1. Run OH_JSVM_DefineClassWithOptions: Success
```
