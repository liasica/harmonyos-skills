---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/use-napi-about-extension
title: 使用Node-API进行扩展能力功能开发
breadcrumb: 指南 > NDK开发 > 代码开发 > 使用Node-API实现ArkTS/JS与C/C++语言交互 > Node-API使用指导 > 使用Node-API进行扩展能力功能开发
category: harmonyos-guides
scraped_at: 2026-04-28T07:54:01+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:263fed354b4297075449be8ec6318f67bf962ce5d4e0ff3821ed69936d53a483
---

## 简介

[扩展能力](napi-data-types-interfaces.md#扩展能力)接口进一步扩展了Node-API的功能，提供了一些额外的接口，用于在Node-API模块中与ArkTS进行更灵活的交互和定制，这些接口可以用于创建自定义ArkTS对象等场景。

Node-API接口开发流程参考[使用Node-API实现跨语言交互开发流程](use-napi-process.md)，本文仅对接口对应C++及ArkTS相关代码进行展示。

本文cpp部分代码所需引用的头文件如下：

```
1. #include "napi/native_api.h"
2. #include <bits/alltypes.h>
3. #include <mutex>
4. #include <unordered_set>
5. #include <uv.h>
6. #include "hilog/log.h"
```

本文ArkTS侧示例代码所需的模块导入如下：

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';
2. import testNapi from 'libentry.so';
3. import { taskpool } from '@kit.ArkTS';
```

## 模块加载

### 接口描述

| 接口 | 描述 |
| --- | --- |
| napi\_load\_module | 用于在Node-API模块中将abc文件作为模块加载，返回模块的命名空间，适用于需要在运行时动态加载模块或资源的应用程序，从而实现灵活的扩展和定制。 |
| napi\_load\_module\_with\_info | 用于在Node-API中进行模块的加载，当模块加载出来之后，可以使用函数napi\_get\_property获取模块导出的变量，也可以使用napi\_get\_named\_property获取模块导出的函数，该函数可以在[新创建的ArkTS基础运行时环境](use-napi-ark-runtime.md)中使用。 |
| napi\_module\_register | 有些功能可能需要通过Node-API模块来实现以获得更好的性能，通过将这些功能实现为自定义模块并注册到ArkTS环境中，可以在一定程度上提高整体的性能。 |

### 使用示例

**napi\_load\_module**

[使用Node-API接口在主线程中进行模块加载](use-napi-load-module.md)

**napi\_load\_module\_with\_info**

[使用Node-API接口进行模块加载](use-napi-load-module-with-info.md)

**napi\_module\_register**

在ArkTS代码环境中使用Node-API模块编写的代码来实现特定的功能，可以将这部分功能封装成自定义模块，然后通过napi\_module\_register将其注册到ArkTS代码环境中，以实现功能的扩展和复用。

cpp部分代码

```
1. #include "napi/native_api.h"

3. // 此模块是一个Node-API的回调函数
4. static napi_value Add(napi_env env, napi_callback_info info)
5. {
6. // 接受传入两个参数
7. size_t requireArgc = 2;
8. size_t argc = 2;
9. napi_value args[2] = {nullptr};
10. napi_get_cb_info(env, info, &argc, args , nullptr, nullptr);

12. // 将传入的napi_value类型的参数转化为double类型
13. double valueLeft;
14. double valueRight;
15. napi_get_value_double(env, args[0], &valueLeft);
16. napi_get_value_double(env, args[1], &valueRight);

18. // 将转化后的double值相加并转成napi_value返回给ArkTS代码使用
19. napi_value sum;
20. napi_create_double(env, valueLeft + valueRight, &sum);

22. return sum;
23. }

25. // C++函数Init用于初始化插件，用于将ArkTS层的函数或属性与C++层的函数进行关联
26. EXTERN_C_START
27. static napi_value Init(napi_env env, napi_value exports)
28. {
29. // 通过napi_property_descriptor结构体，可以定义需要导出的属性，并在Node-API模块中使用。napi_define_properties将属性与实际的C++函数进行关联，使其可以被ArkTS层访问和调用
30. napi_property_descriptor desc[] = {
31. { "add", nullptr, Add, nullptr, nullptr, nullptr, napi_default, nullptr }
32. };
33. napi_define_properties(env, exports, sizeof(desc) / sizeof(desc[0]), desc);
34. return exports;
35. }
36. EXTERN_C_END

38. // 插件的初始化被定义在一个名为demoModule的结构体中，其中包含了模块的基本信息，比如模块的版本号、注册函数等
39. static napi_module demoModule = {
40. .nm_version =1,
41. .nm_flags = 0,
42. .nm_filename = nullptr,
43. .nm_register_func = Init,
44. .nm_modname = "entry",
45. .nm_priv = ((void*)0),
46. .reserved = { 0 },
47. };

49. // 在RegisterEntryModule函数中，使用napi_module_register函数注册并导出了这个插件
50. extern "C" __attribute__((constructor)) void RegisterEntryModule(void)
51. {
52. napi_module_register(&demoModule);
53. }
```

接口声明

```
1. export const add: (a: number, b: number) => number; // 模块加载
```

ArkTS侧示例代码

```
1. hilog.info(0x0000, 'testTag', 'Test Node-API 2 + 3 = %{public}d', testNapi.add(2, 3));
```

## ArkTS Object相关

### 接口描述

| 接口 | 描述 |
| --- | --- |
| napi\_create\_object\_with\_properties | 用于在Node-API模块中使用给定的napi\_property\_descriptor创建ArkTS Object。descriptor的键名必须为string，且不可转为number。 |
| napi\_create\_object\_with\_named\_properties | 用于在Node-API模块中使用给定的napi\_value和键名创建ArkTS Object。键名必须为string，且不可转为number。 |

### 使用示例

**napi\_create\_object\_with\_properties**

用给定的napi\_property\_descriptor作为属性去创建一个ArkTS对象，并且descriptor的键名必须为string，且不可转为number。

cpp部分代码

```
1. // ArkTS Object相关 napi_create_object_with_properties
2. static napi_value CreateObjectWithProperties(napi_env env, napi_callback_info info)
3. {
4. size_t argc = 1;
5. napi_value argv[1] = {nullptr};
6. // 获取解析传递的参数
7. napi_get_cb_info(env, info, &argc, argv, nullptr, nullptr);
8. // 声明了一个napi_property_descriptor数组desc，其中包含了一个名为"name"的属性，其值为传入的第一个参数argv[0]。
9. napi_property_descriptor desc[] = {
10. {"name", nullptr, nullptr, nullptr, nullptr, argv[0], napi_default_jsproperty, nullptr}};
11. napi_value object = nullptr;
12. // 调用napi_create_object_with_properties来创建一个新的ArkTS对象，并将属性值添加到该对象中。
13. napi_create_object_with_properties(env, &object, sizeof(desc) / sizeof(desc[0]), desc);
14. napi_valuetype valueType;
15. napi_typeof(env, object, &valueType);
16. if (valueType == napi_object) {
17. return object;
18. }
19. }
```

接口声明

```
1. export const createObjectWithProperties: (data: string) => {name:string}; // ArkTS Object相关 napi_create_object_with_properties
```

ArkTS侧示例代码

```
1. // ArkTS Object相关 napi_create_object_with_properties
2. let value1 = testNapi.createObjectWithProperties('createObject');
3. hilog.info(0x0000, 'testTag', 'Node-API napi_create_object_with_properties:%{public}s',
4. JSON.stringify(value1));
```

**napi\_create\_object\_with\_named\_properties**

用于使用给定的napi\_value和键名创建一个ArkTS对象，并且给定的键名必须为string，且不可转为number。

cpp部分代码

```
1. // ArkTS Object相关 napi_create_object_with_named_properties
2. static napi_value CreateObjectWithNameProperties(napi_env env, napi_callback_info info)
3. {
4. size_t argc = 1;
5. napi_value argv[1] = {nullptr};
6. // 获取解析传递的参数
7. napi_get_cb_info(env, info, &argc, argv, nullptr, nullptr);
8. napi_value obj = nullptr;
9. const char *key[] = {
10. "name",
11. };
12. const napi_value values[] = {
13. argv[0],
14. };
15. napi_property_descriptor desc[] = {{"name", nullptr, nullptr,
16. nullptr, nullptr, nullptr, napi_default, nullptr}};
17. napi_status status = napi_create_object_with_named_properties(
18. env, &obj, sizeof(desc) / sizeof(desc[0]), key, values
19. );
20. if (status != napi_ok) {
21. return nullptr;
22. }
23. return obj;
24. }
```

接口声明

```
1. export const createObjectWithNameProperties: (data: string) => undefined | { name: string }; // ArkTS Object相关 napi_create_object_with_named_properties
```

ArkTS侧示例代码

```
1. // ArkTS Object相关 napi_create_object_with_named_properties
2. let value2 = testNapi.createObjectWithNameProperties('ls');
3. try {
4. hilog.info(0x0000, 'testTag', 'Node-API napi_create_object_with_named_properties:%{public}s', JSON.stringify(value2));
5. } catch (error) {
6. hilog.error(0x0000, 'testTag', 'Node-API napi_create_object_with_named_properties: %{public}s', error.message);
7. }
```

## 运行指定abc文件

### 接口描述

| 接口 | 描述 |
| --- | --- |
| napi\_run\_script\_path | 用于在Node-API模块中运行指定abc文件。 |

### 使用示例

**napi\_run\_script\_path**

在Node-API模块中运行abc文件。

注意

在信号函数中调用不安全，直接调用可能导致栈溢出。

cpp部分代码

```
1. // 运行指定abc文件 napi_run_script_path
2. static napi_value RunScriptPath(napi_env env, napi_callback_info info)
3. {
4. napi_value value = nullptr;
5. // 注意：记得在应用rawfile目录下放置.abc文件
6. const char *scriptPath = "/entry/resources/rawfile/test.abc";
7. // 使用napi_run_script_path函数执行指定路径中的文件
8. napi_status status = napi_run_script_path(env, scriptPath, &value);
9. // 检查是否执行成功，如果失败，返回false
10. napi_value returnValue = nullptr;
11. if (value == nullptr || status != napi_ok) {
12. napi_get_boolean(env, false, &returnValue);
13. } else {
14. napi_get_boolean(env, true, &returnValue);
15. }
16. return returnValue;
17. }
```

接口声明

```
1. export const runScriptPath: () => boolean; // 运行指定abc文件 napi_run_script_path
```

ArkTS侧示例代码

```
1. // 运行指定abc文件 napi_run_script_path
2. try { // 在此处执行错误返回false，成功就返回true
3. hilog.info(0x0000, 'testTag', 'Test Node-API napi_run_script_path: %{public}s',
4. testNapi.runScriptPath());
5. // ···
6. } catch (error) {
7. hilog.error(0x0000, 'testTag', 'Test Node-API napi_run_script_path errorMessage: %{public}s',
8. error.message);
9. // ···
10. }
```

test.js代码，将JS代码编译为.abc文件，步骤如下：

1. 在SDK的ets/build-tools/ets-loader/bin/ark/build-win/bin目录下放置test.js文件
2. 执行命令如es2abc.exe test.js --output test.abc后便可生成test.abc文件

放入指定路径中：/entry/resources/rawfile

```
1. function add(a, b) {
2. return a + b;
3. }
4. add(1, 2);
```

## 异步工作对象加入队列并指定优先级

### 接口描述

| 接口 | 描述 |
| --- | --- |
| napi\_queue\_async\_work\_with\_qos | 用于将异步工作对象加入队列，让开发者能够根据QoS优先级来管理和调度异步工作的执行，从而更好地满足程序的性能和响应需求。 |

### 使用示例

**napi\_queue\_async\_work\_with\_qos**

将异步工作对象加到队列，由底层根据传入的qos优先级去调度执行。

## 给ArkTS对象绑定回调和回调所需的参数

### 接口描述

| 接口 | 描述 |
| --- | --- |
| napi\_coerce\_to\_native\_binding\_object | 用于给ArkTS对象绑定回调和回调所需的参数，其作用是为了给ArkTS对象携带Native信息。 |

### 使用示例

**napi\_coerce\_to\_native\_binding\_object**

用于给ArkTS Object绑定回调和回调所需的参数，给ArkTS Object携带Native信息。

cpp部分代码

```
1. #include <hilog/log.h>
2. #include <mutex>
3. #include <unordered_set>
4. #include "napi/native_api.h"

6. class Object {
7. public:
8. Object() = default;
9. ~Object() = default;

11. static Object* GetInstance()
12. {
13. Object* instance = new Object();
14. return instance;
15. }

17. static napi_value GetAddress(napi_env env, napi_callback_info info)
18. {
19. napi_value thisVar = nullptr;
20. napi_get_cb_info(env, info, nullptr, nullptr, &thisVar, nullptr);
21. if (thisVar == nullptr) {
22. return nullptr;
23. }
24. void* object = nullptr;
25. napi_unwrap(env, thisVar, &object);
26. if (object == nullptr) {
27. return nullptr;
28. }
29. uint64_t addressVal = reinterpret_cast<uint64_t>(object);
30. napi_value address = nullptr;
31. napi_create_bigint_uint64(env, addressVal, &address);
32. return address;
33. }

35. // 获取数组大小
36. static napi_value GetSetSize(napi_env env, napi_callback_info info)
37. {
38. napi_value thisVar = nullptr;
39. napi_get_cb_info(env, info, nullptr, nullptr, &thisVar, nullptr);
40. if (thisVar == nullptr) {
41. return nullptr;
42. }
43. void* object = nullptr;
44. napi_unwrap(env, thisVar, &object);
45. if (object == nullptr) {
46. return nullptr;
47. }
48. std::lock_guard<std::mutex> lock(reinterpret_cast<Object*>(object)->numberSetMutex_);
49. uint32_t setSize = reinterpret_cast<Object*>(object)->numberSet_.size();
50. napi_value napiSize = nullptr;
51. napi_create_uint32(env, setSize, &napiSize);
52. return napiSize;
53. }

55. // 往数组里插入元素
56. static napi_value Store(napi_env env, napi_callback_info info)
57. {
58. size_t argc = 1;
59. napi_value args[1] = {nullptr};
60. napi_value thisVar = nullptr;
61. napi_get_cb_info(env, info, &argc, args, &thisVar, nullptr);
62. if (argc != 1) {
63. napi_throw_error(env, nullptr, "Store args number must be one.");
64. return nullptr;
65. }
66. napi_valuetype type = napi_undefined;
67. napi_typeof(env, args[0], &type);
68. if (type != napi_number) {
69. napi_throw_error(env, nullptr, "Store args is not number.");
70. return nullptr;
71. }
72. if (thisVar == nullptr) {
73. return nullptr;
74. }
75. uint32_t value = 0;
76. napi_get_value_uint32(env, args[0], &value);
77. void* object = nullptr;
78. napi_unwrap(env, thisVar, &object);
79. if (object == nullptr) {
80. return nullptr;
81. }
82. std::lock_guard<std::mutex> lock(reinterpret_cast<Object*>(object)->numberSetMutex_);
83. reinterpret_cast<Object *>(object)-> numberSet_.insert(value);
84. return nullptr;
85. }

87. // 删除数组元素
88. static napi_value Erase(napi_env env, napi_callback_info info)
89. {
90. size_t argc = 1;
91. napi_value args[1] = {nullptr};
92. napi_value thisVar = nullptr;
93. napi_get_cb_info(env, info, &argc, args, &thisVar, nullptr);
94. if (argc != 1) {
95. napi_throw_error(env, nullptr, "Erase args number must be one.");
96. return nullptr;
97. }
98. napi_valuetype type = napi_undefined;
99. napi_typeof(env, args[0], &type);
100. if (type != napi_number) {
101. napi_throw_error(env, nullptr, "Erase args is not number.");
102. return nullptr;
103. }
104. if (thisVar == nullptr) {
105. return nullptr;
106. }
107. uint32_t value = 0;
108. napi_get_value_uint32(env, args[0], &value);
109. void* object = nullptr;
110. napi_unwrap(env, thisVar, &object);
111. if (object == nullptr) {
112. return nullptr;
113. }
114. std::lock_guard<std::mutex> lock(reinterpret_cast<Object*>(object)->numberSetMutex_);
115. reinterpret_cast<Object *>(object)->numberSet_.erase(value);
116. return nullptr;
117. }

119. // 清空数组
120. static napi_value Clear(napi_env env, napi_callback_info info)
121. {
122. napi_value thisVar = nullptr;
123. napi_get_cb_info(env, info, nullptr, nullptr, &thisVar, nullptr);
124. if (thisVar == nullptr) {
125. return nullptr;
126. }
127. void* object = nullptr;
128. napi_unwrap(env, thisVar, &object);
129. if (object == nullptr) {
130. return nullptr;
131. }
132. std::lock_guard<std::mutex> lock(reinterpret_cast<Object*>(object)->numberSetMutex_);
133. reinterpret_cast<Object *>(object)->numberSet_.clear();
134. return nullptr;
135. }

137. private:
138. Object(const Object &) = delete;
139. Object &operator=(const Object &) = delete;

141. std::unordered_set<uint32_t> numberSet_{};
142. std::mutex numberSetMutex_{};
143. };

145. void FinalizerCallback(napi_env env, void *data, void *hint)
146. {
147. return;
148. }

150. // 解绑回调，在序列化时调用，可在对象解绑时执行一些清理操作
151. void* DetachCallback(napi_env env, void *value, void *hint)
152. {
153. return value;
154. }

156. // 绑定回调，在反序列化时调用
157. napi_value AttachCallback(napi_env env, void* value, void* hint)
158. {
159. napi_value object = nullptr;
160. napi_create_object(env, &object);
161. napi_property_descriptor desc[] = {
162. {"getAddress", nullptr, Object::GetAddress, nullptr, nullptr, nullptr, napi_default, nullptr},
163. {"getSetSize", nullptr, Object::GetSetSize, nullptr, nullptr, nullptr, napi_default, nullptr},
164. {"store", nullptr, Object::Store, nullptr, nullptr, nullptr, napi_default, nullptr},
165. {"erase", nullptr, Object::Erase, nullptr, nullptr, nullptr, napi_default, nullptr},
166. {"clear", nullptr, Object::Clear, nullptr, nullptr, nullptr, napi_default, nullptr}};
167. napi_define_properties(env, object, sizeof(desc) / sizeof(desc[0]), desc);
168. // 将JS对象object和native对象value生命周期进行绑定
169. napi_status status = napi_wrap(env, object, value, FinalizerCallback, nullptr, nullptr);
170. if (status != napi_ok) {
171. OH_LOG_INFO(LOG_APP, "Node-API attachCallback is failed.");
172. }
173. // JS对象携带native信息
174. napi_coerce_to_native_binding_object(env, object, DetachCallback, AttachCallback, value, hint);
175. return object;
176. }

178. EXTERN_C_START
179. static napi_value Init(napi_env env, napi_value exports)
180. {
181. napi_property_descriptor desc[] = {
182. {"getAddress", nullptr, Object::GetAddress, nullptr, nullptr, nullptr, napi_default, nullptr},
183. {"getSetSize", nullptr, Object::GetSetSize, nullptr, nullptr, nullptr, napi_default, nullptr},
184. {"store", nullptr, Object::Store, nullptr, nullptr, nullptr, napi_default, nullptr},
185. {"erase", nullptr, Object::Erase, nullptr, nullptr, nullptr, napi_default, nullptr},
186. {"clear", nullptr, Object::Clear, nullptr, nullptr, nullptr, napi_default, nullptr}};
187. napi_define_properties(env, exports, sizeof(desc) / sizeof(desc[0]), desc);
188. auto object = Object::GetInstance();
189. napi_status status = napi_wrap(env, exports, reinterpret_cast<void*>(object), FinalizerCallback, nullptr, nullptr);
190. if (status != napi_ok) {
191. OH_LOG_INFO(LOG_APP, "Node-API napi_wrap is failed.");
192. }
193. napi_coerce_to_native_binding_object(env, exports, DetachCallback, AttachCallback, reinterpret_cast<void*>(object),
194. nullptr);
195. return exports;
196. }
197. EXTERN_C_END

199. static napi_module demoModule = {
200. .nm_version = 1,
201. .nm_flags = 0,
202. .nm_filename = nullptr,
203. .nm_register_func = Init,
204. .nm_modname = "entry",
205. .nm_priv = ((void*)0),
206. .reserved = { 0 },
207. };

209. extern "C" __attribute__((constructor)) void RegisterEntryModule(void)
210. {
211. napi_module_register(&demoModule);
212. }
```

接口声明

```
1. // 给ArkTS对象绑定回调和回调所需的参数 napi_coerce_to_native_binding_object
2. export const getAddress: () => number;

4. export const getSetSize: () => number;

6. export const store: (a: number) => void;

8. export const erase: (a: number) => void;

10. export const clear: () => void;
```

ArkTS侧示例代码

```
1. // index.ets
2. import testNapi from 'libentry.so';
3. import { taskpool } from '@kit.ArkTS';

5. @Concurrent
6. function getAddress() {
7. let address: number = testNapi.getAddress();
8. console.info("taskpool:: address is " + address);
9. }

11. @Concurrent
12. function store(a:number, b:number, c:number) {
13. let size:number = testNapi.getSetSize();
14. console.info("set size is " + size + " before store");
15. testNapi.store(a);
16. testNapi.store(b);
17. testNapi.store(c);
18. size = testNapi.getSetSize();
19. console.info("set size is " + size + " after store");
20. }

22. @Concurrent
23. function erase(a:number) {
24. let size:number = testNapi.getSetSize();
25. console.info("set size is " + size + " before erase");
26. testNapi.erase(a);
27. size = testNapi.getSetSize();
28. console.info("set size is " + size + " after erase");
29. }

31. @Concurrent
32. function clear() {
33. let size:number = testNapi.getSetSize();
34. console.info("set size is " + size + " before clear");
35. testNapi.clear();
36. size = testNapi.getSetSize();
37. console.info("set size is " + size + " after clear");
38. }

40. async function test01(): Promise<void> {
41. let address:number = testNapi.getAddress();
42. console.info("host thread address is " + address);

44. let task1 = new taskpool.Task(getAddress);
45. await taskpool.execute(task1);

47. let task2 = new taskpool.Task(store, 1, 2, 3);
48. await taskpool.execute(task2);

50. let task3 = new taskpool.Task(store, 4, 5, 6);
51. await taskpool.execute(task3);

53. let task4 = new taskpool.Task(erase, 3);
54. await taskpool.execute(task4);

56. let task5 = new taskpool.Task(erase, 5);
57. await taskpool.execute(task5);

59. let task6 = new taskpool.Task(clear);
60. await taskpool.execute(task6);
61. }

63. test01();
```

**注意事项**

对ArkTS对象A调用napi\_coerce\_to\_native\_binding\_object将开发者实现的detach/attach回调和native对象信息加到A上，再将A跨线程传递。跨线程传递需要对A进行序列化和反序列化。此处的序列化与反序列化是人为控制的，需要调用后文介绍的napi\_serialize、napi\_deserialize接口。过程如下图所示：在当前线程thread1序列化A得到数据data，序列化阶段执行detach回调。然后将data传给目标线程thread2，在thread2中反序列化data，执行attach回调，最终得到ArkTS对象A。此处的detach/attach是告知开发者序列化与反序列化执行完毕的回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/AMuorgvgTq-_iQiCC5arDg/zh-cn_image_0000002583479371.png?HW-CC-KV=V1&HW-CC-Date=20260427T235359Z&HW-CC-Expire=86400&HW-CC-Sign=B9A962641364FCCDF799437D8153F7BB7AA004D486431A0D064E19B990EC499A)

## 事件循环

### 接口描述

| 接口 | 描述 |
| --- | --- |
| napi\_run\_event\_loop | 触发底层的事件循环。 |
| napi\_stop\_event\_loop | 停止底层的事件循环。 |

### 使用示例

**napi\_run\_event\_loop、napi\_stop\_event\_loop**

[使用扩展的Node-API接口在异步线程中运行和停止事件循环](use-napi-event-loop.md)

## ArkTS基础运行时环境

### 接口描述

| 接口 | 描述 |
| --- | --- |
| napi\_create\_ark\_runtime | 创建基础运行时环境。 |
| napi\_destroy\_ark\_runtime | 销毁基础运行时环境。 |

### 使用示例

**napi\_create\_ark\_runtime、napi\_destroy\_ark\_runtime**

[使用Node-API接口创建ArkTS运行时环境](use-napi-ark-runtime.md)

## 序列化和反序列化

### 接口描述

| 接口 | 描述 |
| --- | --- |
| napi\_serialize | 将ArkTS对象转换为native数据。第一个参数env是接口执行的ArkTS环境；第二个参数object是待序列化的ArkTS对象；第三个参数transfer\_list是存放需要以transfer传递的arrayBuffer的array，如不涉及可传undefined；第四个参数clone\_list是存放需要克隆传递的Sendable对象的array，如不涉及可传undefined；第五个参数result是序列化结果。 |
| napi\_deserialize | 将native数据转为ArkTS对象。第一个参数env是接口执行的ArkTS环境；第二个参数buffer是序列化数据；第三个参数object是反序列化得到的结果。 |
| napi\_delete\_serialization\_data | 删除序列化数据。 |

### 使用示例

**napi\_serialize、napi\_deserialize、napi\_delete\_serialization\_data**

用于将ArkTS对象转换为native数据、将native数据转为ArkTS对象、删除序列化数据等操作。

cpp部分代码

```
1. // 序列化和反序列化
2. static napi_value AboutSerialize(napi_env env, napi_callback_info info)
3. {
4. // 获取传入的ts的一个对象作为参数
5. size_t argc = 1;
6. napi_value args[1] = {nullptr};
7. napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);
8. napi_value undefined = nullptr;
9. // 构造napi_serialize方法所需参数
10. napi_get_undefined(env, &undefined);
11. void *data = nullptr;
12. // 调用napi_serialize方法将ts对象转化为native数据
13. napi_status status = napi_serialize(env, args[0], undefined, undefined, &data);
14. if (status != napi_ok || data == nullptr) {
15. napi_throw_error(env, nullptr, "Node-API napi_serialize fail");
16. return nullptr;
17. }
18. // 构造napi_value类型的数据，用于接收将native数据转化为ts对象后的数据
19. napi_value result = nullptr;
20. napi_deserialize(env, data, &result);
21. napi_value number = nullptr;
22. // 获取native数据转化为ts对象后的数据中的numKey属性的值
23. napi_get_named_property(env, result, "numKey", &number);
24. // 判断获取到的属性值是否为number类型
25. napi_valuetype valuetype;
26. napi_typeof(env, number, &valuetype);
27. if (valuetype != napi_number) {
28. napi_throw_error(env, nullptr, "Node-API Wrong type of argument. Expects a number.");
29. return nullptr;
30. }
31. // 调用napi_delete_serialization_data方法删除序列化数据
32. napi_delete_serialization_data(env, data);
33. // 返回获取到的属性值
34. return number;
35. }
```

接口声明

```
1. export const aboutSerialize: (obj: {numKey:number}) => number | undefined; // 序列化和反序列化
```

ArkTS侧示例代码

```
1. class Obj {
2. numKey: number = 0;
3. }
```

```
1. // 序列化和反序列化
2. let obj: Obj = { numKey: 500 };
3. hilog.info(0x0000, 'testTag', ' Node-API aboutSerialize: %{public}d', testNapi.aboutSerialize(obj));
```

## 根据任务指定的优先级和入队方式进行处理异步线程向ArkTS线程投递的任务

### 接口描述

| 接口 | 描述 |
| --- | --- |
| napi\_call\_threadsafe\_function\_with\_priority | 将指定优先级和入队方式的任务投递到ArkTS主线程。 |

### 使用示例

**napi\_call\_threadsafe\_function\_with\_priority**

[使用Node-API接口从异步线程向ArkTS线程投递指定优先级和入队方式的的任务](use-call-threadsafe-function-with-priority.md)

## Sendable相关

### 接口描述

| 接口 | 描述 |
| --- | --- |
| napi\_is\_sendable | 判断给定ArkTS value是否是Sendable的。 |
| napi\_define\_sendable\_class | 创建一个sendable类。 |
| napi\_create\_sendable\_object\_with\_properties | 使用给定的napi\_property\_descriptor创建一个sendable对象。 |
| napi\_create\_sendable\_array | 创建一个sendable数组。 |
| napi\_create\_sendable\_array\_with\_length | 创建一个指定长度的sendable数组。 |
| napi\_create\_sendable\_arraybuffer | 创建一个sendable ArrayBuffer。 |
| napi\_create\_sendable\_typedarray | 创建一个sendable TypedArray。 |
| napi\_wrap\_sendable | 包裹一个native实例到ArkTS对象中。 |
| napi\_wrap\_sendable\_with\_size | 包裹一个native实例到ArkTS对象中并指定大小。 |
| napi\_unwrap\_sendable | 获取ArkTS对象包裹的native实例。 |
| napi\_remove\_wrap\_sendable | 移除并获取ArkTS对象包裹的native实例，移除后回调将不再触发，需手动delete释放内存。 |

### 使用示例

**napi\_is\_sendable**

判断给定ArkTS value是否是Sendable的。

cpp部分代码

```
1. // Sendable相关 napi_is_sendable
2. static napi_value IsSendable(napi_env env, napi_callback_info info)
3. {
4. size_t argc = 1;
5. napi_value args[1] = {nullptr};
6. napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);
7. bool isSendable = false;
8. napi_is_sendable(env, args[0], &isSendable);
9. napi_value result;
10. napi_get_boolean(env, isSendable, &result);
11. return result;
12. }
```

接口声明

```
1. export const isSendable: <T>(a: T) => boolean; // Sendable相关 napi_is_sendable
```

ArkTS侧示例代码

```
1. // Sendable相关 napi_is_sendable
2. let value = testNapi.isSendable('createObject');
3. hilog.info(0x0000, 'testTag', 'Node-API napi_is_sendable: %{public}s', JSON.stringify(value));
```

**napi\_define\_sendable\_class**

创建一个sendable类。

cpp部分代码

```
1. #include "napi/native_api.h"

3. static napi_value func(napi_env env, napi_callback_info info) {
4. napi_value val;
5. napi_create_string_utf8(env, "func result", NAPI_AUTO_LENGTH, &val);
6. return val;
7. }

9. static napi_value DefineSendableClass(napi_env env) {
10. napi_value str;
11. napi_create_string_utf8(env, "str", NAPI_AUTO_LENGTH, &str);

13. napi_property_descriptor props[] = {
14. {"staticStr", nullptr, nullptr, nullptr, nullptr, str,
15. static_cast<napi_property_attributes>(napi_static | napi_writable), nullptr},
16. {"staticFunc", nullptr, func, nullptr, nullptr, nullptr, napi_static, nullptr},
17. {"str", nullptr, nullptr, nullptr, nullptr, str, static_cast<napi_property_attributes>(1 << 9 | napi_writable),
18. nullptr},
19. {"func", nullptr, nullptr, nullptr, nullptr, nullptr,
20. static_cast<napi_property_attributes>(1 << 11 | napi_writable), nullptr},
21. };

23. napi_value sendableClass = nullptr;
24. napi_define_sendable_class(
25. env, "SendableClass", NAPI_AUTO_LENGTH,
26. [](napi_env env, napi_callback_info info) -> napi_value {
27. napi_value thisVar = nullptr;
28. napi_get_cb_info(env, info, nullptr, nullptr, &thisVar, nullptr);
29. napi_value str;
30. napi_create_string_utf8(env, "instance str", NAPI_AUTO_LENGTH, &str);
31. napi_property_descriptor props[] = {
32. {"str", nullptr, nullptr, nullptr, nullptr, str, napi_default, nullptr},
33. {"func", nullptr, func, nullptr, nullptr, nullptr, napi_default, nullptr},
34. };
35. napi_define_properties(env, thisVar, sizeof(props) / sizeof(props[0]), props);
36. return thisVar;
37. },
38. nullptr, sizeof(props) / sizeof(props[0]), props, nullptr, &sendableClass);

40. return sendableClass;
41. }

43. EXTERN_C_START
44. static napi_value Init(napi_env env, napi_value exports)
45. {
46. napi_property_descriptor desc[] = {};
47. napi_define_properties(env, exports, sizeof(desc) / sizeof(desc[0]), desc);
48. napi_value cons = DefineSendableClass(env);
49. napi_set_named_property(env, exports, "SendableClass", cons);
50. return exports;
51. }
52. EXTERN_C_END

54. static napi_module demoModule = {
55. .nm_version = 1,
56. .nm_flags = 0,
57. .nm_filename = nullptr,
58. .nm_register_func = Init,
59. .nm_modname = "entry",
60. .nm_priv = ((void*)0),
61. .reserved = { 0 },
62. };

64. extern "C" __attribute__((constructor)) void RegisterEntryModule(void)
65. {
66. napi_module_register(&demoModule);
67. }
```

接口声明

```
1. @Sendable
2. export class SendableClass {
3. static staticStr: string;
4. static staticFunc(): string;
5. str: string;
6. func(): string;
7. } // Sendable相关 napi_define_sendable_class
```

ArkTS侧示例代码

```
1. // Sendable相关 napi_define_sendable_class
2. let value = new testNapi.SendableClass();
3. hilog.info(0x0000, 'testTag', 'Node-API napi_define_sendable_class: %{public}s', value.str);
```

**napi\_create\_sendable\_object\_with\_properties**

使用给定的napi\_property\_descriptor创建一个sendable对象。

cpp部分代码

```
1. // Sendable相关 napi_create_sendable_object_with_properties
2. static napi_value GetSendableObject(napi_env env, napi_callback_info info)
3. {
4. napi_value val_true;
5. napi_get_boolean(env, true, &val_true);
6. napi_property_descriptor desc1[] = {
7. {"x", nullptr, nullptr, nullptr, nullptr, val_true, napi_default_jsproperty, nullptr},
8. };
9. napi_value obj;
10. napi_create_sendable_object_with_properties(env, 1, desc1, &obj);
11. return obj;
12. }
```

接口声明

```
1. export const getSendableObject: () => { x: true }; // Sendable相关 napi_create_sendable_object_with_properties
```

ArkTS侧示例代码

```
1. // Sendable相关 napi_create_sendable_object_with_properties
2. let value = testNapi.getSendableObject();
3. hilog.info(0x0000, 'testTag', 'Node-API napi_create_sendable_object_with_properties: %{public}s',
4. JSON.stringify(value));
```

**napi\_create\_sendable\_array**

创建一个sendable数组。

cpp部分代码

```
1. // Sendable相关 napi_create_sendable_array
2. static napi_value GetSendableArray(napi_env env, napi_callback_info info)
3. {
4. napi_value result = nullptr;
5. napi_create_sendable_array(env, &result);
6. return result;
7. }
```

接口声明

```
1. export const getSendableArray: () => []; // Sendable相关 napi_create_sendable_array
```

ArkTS侧示例代码

```
1. // Sendable相关 napi_create_sendable_array
2. let value = testNapi.getSendableArray();
3. hilog.info(0x0000, 'testTag', 'Node-API napi_create_sendable_array: %{public}s',
4. JSON.stringify(value));
```

**napi\_create\_sendable\_array\_with\_length**

创建一个指定长度的sendable数组。

cpp部分代码

```
1. // Sendable相关 napi_create_sendable_array_with_length
2. static napi_value GetSendableArrayWithLength(napi_env env, napi_callback_info info)
3. {
4. napi_value result = nullptr;
5. napi_create_sendable_array_with_length(env, 1, &result);
6. return result;
7. }
```

接口声明

```
1. // index.d.ts
2. export const getSendableArrayWithLength: () => [];
```

ArkTS侧示例代码

```
1. let value = testNapi.getSendableArrayWithLength();
2. hilog.info(0x0000, 'testTag', 'Node-API napi_create_sendable_array_with_length: %{public}s', JSON.stringify(value.length));
```

**napi\_create\_sendable\_arraybuffer**

创建一个sendable ArrayBuffer。

cpp部分代码

```
1. static napi_value GetSendableArrayBuffer(napi_env env, napi_callback_info info) {
2. static size_t LENGTH = 1024;
3. void *data;
4. napi_value result = nullptr;
5. napi_create_sendable_arraybuffer(env, LENGTH, &data, &result);
6. bool isArrayBuffer = false;
7. napi_is_arraybuffer(env, result, &isArrayBuffer);
8. OH_LOG_INFO(LOG_APP, "isArrayBuffer: %{public}d", isArrayBuffer);
9. return result;
10. }
```

接口声明

```
1. // index.d.ts
2. export const getSendableArrayBuffer: () => ArrayBuffer;
```

ArkTS侧示例代码

```
1. testNapi.getSendableArrayBuffer();
```

**napi\_create\_sendable\_typedarray**

创建一个sendable TypedArray。

cpp部分代码

```
1. static napi_value GetSendableTypedArray(napi_env env, napi_callback_info info) {
2. static size_t LENGTH = 1024;
3. static size_t OFFSET = 0;
4. void *data;
5. napi_value arraybuffer = nullptr;
6. napi_create_sendable_arraybuffer(env, LENGTH, &data, &arraybuffer);

8. napi_value result = nullptr;
9. napi_create_sendable_typedarray(env, napi_uint8_array, LENGTH, arraybuffer, OFFSET, &result);
10. bool isTypedArray = false;
11. napi_is_typedarray(env, result, &isTypedArray);
12. OH_LOG_INFO(LOG_APP, "isTypedArray: %{public}d", isTypedArray);
13. return result;
14. }
```

接口声明

```
1. // index.d.ts
2. export const getSendableTypedArray: () => void;
```

ArkTS侧示例代码

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';
2. import testNapi from 'libentry.so';

4. testNapi.getSendableTypedArray();
```

**napi\_wrap\_sendable**

包裹一个native实例到ArkTS对象中。

cpp部分代码

```
1. #include "napi/native_api.h"

3. static napi_value WrapSendable(napi_env env, napi_callback_info info) {
4. napi_value val_true;
5. napi_get_boolean(env, true, &val_true);
6. napi_property_descriptor desc1[] = {
7. {"x", nullptr, nullptr, nullptr, nullptr, val_true, napi_default_jsproperty, nullptr},
8. };
9. napi_value obj;
10. napi_create_sendable_object_with_properties(env, 1, desc1, &obj);

12. const char* testStr = "test";
13. napi_wrap_sendable(env, obj, (void*)testStr, [](napi_env env, void* data, void* hint) {}, nullptr);

15. return nullptr;
16. }
```

接口声明

```
1. // index.d.ts
2. export const wrapSendable: () => void;
```

ArkTS侧示例代码

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';
2. import testNapi from 'libentry.so';

4. testNapi.wrapSendable();
```

**napi\_wrap\_sendable\_with\_size**

包裹一个native实例到ArkTS对象中并指定大小。

cpp部分代码

```
1. #include "napi/native_api.h"

3. static napi_value WrapSendableWithSize(napi_env env, napi_callback_info info) {
4. napi_value val_true;
5. napi_get_boolean(env, true, &val_true);
6. napi_property_descriptor desc1[] = {
7. {"x", nullptr, nullptr, nullptr, nullptr, val_true, napi_default_jsproperty, nullptr},
8. };
9. napi_value obj;
10. napi_create_sendable_object_with_properties(env, 1, desc1, &obj);

12. const char* testStr = "test";
13. napi_wrap_sendable_with_size(env, obj, (void*)testStr, [](napi_env env, void* data, void* hint) {}, nullptr, 100);

15. return nullptr;
16. }
```

接口声明

```
1. // index.d.ts
2. export const wrapSendableWithSize: () => void;
```

ArkTS侧示例代码

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';
2. import testNapi from 'libentry.so';

4. testNapi.wrapSendableWithSize();
```

**napi\_unwrap\_sendable**

获取ArkTS对象包裹的native实例。

cpp部分代码

```
1. #include "napi/native_api.h"

3. static napi_value UnwrapSendable(napi_env env, napi_callback_info info) {
4. napi_value val_true;
5. napi_get_boolean(env, true, &val_true);
6. napi_property_descriptor desc1[] = {
7. {"x", nullptr, nullptr, nullptr, nullptr, val_true, napi_default_jsproperty, nullptr},
8. };
9. napi_value obj;
10. napi_create_sendable_object_with_properties(env, 1, desc1, &obj);

12. const char* testStr = "test";
13. napi_wrap_sendable(env, obj, (void*)testStr, [](napi_env env, void* data, void* hint) {}, nullptr);

15. char* tmpTestStr = nullptr;
16. napi_unwrap_sendable(env, obj, (void**)&tmpTestStr);
17. OH_LOG_INFO(LOG_APP, "native value is %{public}s", tmpTestStr);

19. return nullptr;
20. }
```

接口声明

```
1. // index.d.ts
2. export const unwrapSendable: () => void;
```

ArkTS侧示例代码

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';
2. import testNapi from 'libentry.so';

4. testNapi.unwrapSendable();
```

**napi\_remove\_wrap\_sendable**

移除并获取ArkTS对象包裹的native实例，移除后回调将不再触发，需手动delete释放内存。

cpp部分代码

```
1. #include "napi/native_api.h"

3. static napi_value RemoveWrapSendable(napi_env env, napi_callback_info info) {
4. napi_value val_true;
5. napi_get_boolean(env, true, &val_true);
6. napi_property_descriptor desc1[] = {
7. {"x", nullptr, nullptr, nullptr, nullptr, val_true, napi_default_jsproperty, nullptr},
8. };
9. napi_value obj;
10. napi_create_sendable_object_with_properties(env, 1, desc1, &obj);

12. const char* testStr = "test";
13. napi_wrap_sendable(env, obj, (void*)testStr, [](napi_env env, void* data, void* hint) {}, nullptr);

15. char* tmpTestStr = nullptr;
16. napi_remove_wrap_sendable(env, obj, (void**)&tmpTestStr);
17. OH_LOG_INFO(LOG_APP, "native value is %{public}s", tmpTestStr);

19. return nullptr;
20. }
```

接口声明

```
1. // index.d.ts
2. export const removeWrapSendable: () => void;
```

ArkTS侧示例代码

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';
2. import testNapi from 'libentry.so';

4. testNapi.removeWrapSendable();
```

以上代码如果要在native cpp中打印日志，需在CMakeLists.txt文件中添加以下配置信息（并添加头文件：#include "hilog/log.h"）：

```
1. // CMakeLists.txt
2. target_compile_definitions(entry PRIVATE LOG_DOMAIN=0xd0d0 LOG_TAG="testTag")
3. target_link_libraries(entry PUBLIC libace_napi.z.so libhilog_ndk.z.so)
```

## napi\_wrap接口增强

### 接口描述

| 接口 | 描述 |
| --- | --- |
| napi\_wrap\_enhance | 在ArkTS对象上绑定一个native对象实例并指定实例大小，运行时会统计传入的实例大小并将其累加，当累计大小达到GC触发阈值时，运行时会启动垃圾回收流程。开发者可以指定绑定的回调函数是否异步执行，如果是异步执行，回调函数必须保证是线程安全的。 |

### 使用示例

**napi\_wrap\_enhance**

在ArkTS对象上绑定一个native对象实例并指定实例大小，运行时会统计传入的实例大小并将其累加，当累计大小达到GC触发阈值时，运行时会启动垃圾回收流程。开发者可以指定绑定的回调函数是否异步执行，如果是异步执行，回调函数必须保证是线程安全的。

cpp部分代码

```
1. #include "napi/native_api.h"

3. static napi_value TestNapiWrapEnhance(napi_env env, napi_callback_info info)
4. {
5. napi_value testClass = nullptr;
6. napi_define_class(
7. env, "TestClass", NAPI_AUTO_LENGTH,
8. [](napi_env env, napi_callback_info info) -> napi_value {
9. napi_value thisVar = nullptr;
10. napi_get_cb_info(env, info, nullptr, nullptr, &thisVar, nullptr);
11. return thisVar;
12. },
13. nullptr, 0, nullptr, &testClass);

15. napi_value obj = nullptr;
16. napi_new_instance(env, testClass, 0, nullptr, &obj);
17. const char* testStr = "test";
18. napi_ref wrappedRef = nullptr;
19. napi_wrap_enhance(env, obj, (void*)testStr, [](napi_env env, void* data, void* hint) {}, false, nullptr, sizeof(testStr), &wrappedRef);
20. return nullptr;
21. }
```

接口声明

```
1. // index.d.ts
2. export const testNapiWrapEnhance: () => void;
```

ArkTS侧示例代码

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';
2. import testNapi from 'libentry.so';

4. testNapi.testNapiWrapEnhance();
```

## napi提供多上下文环境能力

### 接口描述

| 接口 | 描述 |
| --- | --- |
| napi\_create\_ark\_context | 创建基础运行时上下文环境。 |
| napi\_switch\_ark\_context | 切换到指定的运行时上下文环境。 |
| napi\_destroy\_ark\_context | 销毁基础运行时上下文环境。 |

### 使用示例

**napi\_create\_ark\_context、napi\_switch\_ark\_context、napi\_destroy\_ark\_context**

[使用扩展的Node-API接口创建、切换和销毁上下文环境](use-napi-about-context.md)

## napi提供通过指针访问ArkTS String内存数据的功能

### 接口描述

| 接口 | 描述 |
| --- | --- |
| napi\_get\_buffer\_string\_utf16\_in\_critical\_scope | 获取以Utf16编码的ArkTS String的内存数据缓冲区 |

### 使用示例

**napi\_get\_buffer\_string\_utf16\_in\_critical\_scope**

[使用扩展的Node-API接口创建和销毁临界区作用域及访问字符串内容](use-napi-about-critical.md)

## napi实现临界区作用域

### 接口描述

| 接口 | 描述 |
| --- | --- |
| napi\_open\_critical\_scope | 打开临界区作用域 |
| napi\_close\_critical\_scope | 关闭临界区作用域 |

### 使用示例

**napi\_open\_critical\_scope、napi\_close\_critical\_scope**

[使用扩展的Node-API接口创建和销毁临界区作用域及访问字符串内容](use-napi-about-critical.md)

## napi支持创建轻量级的强引用对象

### 接口描述

| 接口 | 描述 |
| --- | --- |
| napi\_create\_strong\_reference | 创建指向ArkTS对象的强引用 |
| napi\_delete\_strong\_reference | 删除强引用 |
| napi\_get\_strong\_reference\_value | 根据强引用对象获取其关联的ArkTS对象值 |

### 使用示例

**napi\_create\_strong\_reference、napi\_delete\_strong\_reference、napi\_get\_value\_strong\_reference**

[使用扩展的Node-API接口创建、销毁和使用强引用对象](use-napi-about-strong-reference.md)

## napi支持创建Sendable的强引用

### 接口描述

| 接口 | 描述 |
| --- | --- |
| napi\_create\_strong\_sendable\_reference | 创建指向Sendable ArkTS对象的Sendable强引用。 |
| napi\_delete\_strong\_sendable\_reference | 删除Sendable强引用。 |
| napi\_get\_strong\_sendable\_reference\_value | 根据Sendable强引用获取其关联的ArkTS对象值。 |

### 使用示例

**napi\_create\_strong\_sendable\_reference、napi\_delete\_strong\_sendable\_reference、napi\_get\_strong\_sendable\_reference\_value**

[使用扩展的Node-API接口创建、销毁和使用Sendable强引用](use-napi-about-sendable-reference.md)

## napi支持抛出错误对象的code属性类型为number的ArkTS Error

### 接口描述

| 接口 | 描述 |
| --- | --- |
| napi\_throw\_business\_error | 抛出带文本信息的ArkTS Error，其错误对象的code属性类型为number。 |

### 使用示例

**napi\_throw\_business\_error**

[使用扩展的Node-API接口抛出ArkTS异常](use-napi-about-error.md)
