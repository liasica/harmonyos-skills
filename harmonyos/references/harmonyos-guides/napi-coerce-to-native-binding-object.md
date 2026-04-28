---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/napi-coerce-to-native-binding-object
title: 自定义Native Transferable对象的多线程操作场景
breadcrumb: 指南 > 应用框架 > ArkTS（方舟编程语言） > ArkTS并发 > 应用多线程开发实践 > 应用多线程开发实践案例 > 自定义Native Transferable对象的多线程操作场景
category: harmonyos-guides
scraped_at: 2026-04-28T07:38:42+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:b6bd4db86e25998227a55a2f60280b608c4d7c4dda0b08d262b0c4e308a7bc28
---

在ArkTS应用开发中，有很多场景需要将ArkTS对象与Native对象进行绑定。ArkTS对象将数据写入Native对象，Native对象再将数据写入目的地。例如，将ArkTS对象中的数据写入C++数据库场景。

Native Transferable对象有两种模式：共享模式和转移模式。本示例将详细说明如何实现这两种模式。

1. Native实现各项功能。

   ```
   1. // napi_init.cpp
   2. #include <mutex>
   3. #include <unordered_set>
   4. #include "napi/native_api.h"
   5. #include <hilog/log.h>

   7. class CustomNativeObject {
   8. public:
   9. CustomNativeObject() {}
   10. ~CustomNativeObject() = default;
   11. static CustomNativeObject& GetInstance()
   12. {
   13. static CustomNativeObject instance;
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

   30. uint64_t addressVal = reinterpret_cast<uint64_t>(object);
   31. napi_value address = nullptr;
   32. napi_create_bigint_uint64(env, addressVal, &address);
   33. return address;
   34. }

   36. // 获取数组大小
   37. static napi_value GetSetSize(napi_env env, napi_callback_info info)
   38. {
   39. napi_value thisVar = nullptr;
   40. napi_get_cb_info(env, info, nullptr, nullptr, &thisVar, nullptr);
   41. if (thisVar == nullptr) {
   42. return nullptr;
   43. }
   44. void* object = nullptr;
   45. napi_unwrap(env, thisVar, &object);
   46. if (object == nullptr) {
   47. return nullptr;
   48. }
   49. CustomNativeObject* obj = static_cast<CustomNativeObject*>(object);
   50. std::lock_guard<std::mutex> lock(obj->numberSetMutex_);
   51. uint32_t setSize = reinterpret_cast<CustomNativeObject*>(object)->numberSet_.size();
   52. napi_value napiSize = nullptr;
   53. napi_create_uint32(env, setSize, &napiSize);
   54. return napiSize;
   55. }

   57. // 往数组里插入元素
   58. static napi_value Store(napi_env env, napi_callback_info info)
   59. {
   60. size_t argc = 1;
   61. napi_value args[1] = {nullptr};
   62. napi_value thisVar = nullptr;
   63. napi_get_cb_info(env, info, &argc, args, &thisVar, nullptr);
   64. if (argc != 1) {
   65. napi_throw_error(env, nullptr, "Store args number must be one.");
   66. return nullptr;
   67. }
   68. napi_valuetype type = napi_undefined;
   69. napi_typeof(env, args[0], &type);
   70. if (type != napi_number) {
   71. napi_throw_error(env, nullptr, "Store args is not number.");
   72. return nullptr;
   73. }
   74. if (thisVar == nullptr) {
   75. return nullptr;
   76. }

   78. void* object = nullptr;
   79. napi_unwrap(env, thisVar, &object);
   80. if (object == nullptr) {
   81. return nullptr;
   82. }

   84. uint32_t value = 0;
   85. napi_get_value_uint32(env, args[0], &value);
   86. CustomNativeObject* obj = static_cast<CustomNativeObject*>(object);
   87. std::lock_guard<std::mutex> lock(obj->numberSetMutex_);
   88. reinterpret_cast<CustomNativeObject *>(object)->numberSet_.insert(value);
   89. return nullptr;
   90. }

   92. // 删除数组元素
   93. static napi_value Erase(napi_env env, napi_callback_info info)
   94. {
   95. size_t argc = 1;
   96. napi_value args[1] = {nullptr};
   97. napi_value thisVar = nullptr;
   98. napi_get_cb_info(env, info, &argc, args, &thisVar, nullptr);
   99. if (argc != 1) {
   100. napi_throw_error(env, nullptr, "Erase args number must be one.");
   101. return nullptr;
   102. }
   103. napi_valuetype type = napi_undefined;
   104. napi_typeof(env, args[0], &type);
   105. if (type != napi_number) {
   106. napi_throw_error(env, nullptr, "Erase args is not number.");
   107. return nullptr;
   108. }
   109. if (thisVar == nullptr) {
   110. return nullptr;
   111. }

   113. void* object = nullptr;
   114. napi_unwrap(env, thisVar, &object);
   115. if (object == nullptr) {
   116. return nullptr;
   117. }

   119. uint32_t value = 0;
   120. napi_get_value_uint32(env, args[0], &value);

   122. CustomNativeObject* obj = static_cast<CustomNativeObject*>(object);
   123. std::lock_guard<std::mutex> lock(obj->numberSetMutex_);
   124. reinterpret_cast<CustomNativeObject *>(object)->numberSet_.erase(value);
   125. return nullptr;
   126. }

   128. // 清空数组
   129. static napi_value Clear(napi_env env, napi_callback_info info)
   130. {
   131. napi_value thisVar = nullptr;
   132. napi_get_cb_info(env, info, nullptr, nullptr, &thisVar, nullptr);
   133. if (thisVar == nullptr) {
   134. return nullptr;
   135. }
   136. void* object = nullptr;
   137. napi_unwrap(env, thisVar, &object);
   138. if (object == nullptr) {
   139. return nullptr;
   140. }
   141. CustomNativeObject* obj = static_cast<CustomNativeObject*>(object);
   142. std::lock_guard<std::mutex> lock(obj->numberSetMutex_);
   143. reinterpret_cast<CustomNativeObject *>(object)->numberSet_.clear();
   144. return nullptr;
   145. }

   147. // 设置传输模式
   148. static napi_value SetTransferDetached(napi_env env, napi_callback_info info)
   149. {
   150. size_t argc = 1;
   151. napi_value args[1];
   152. napi_value thisVar;
   153. napi_get_cb_info(env, info, &argc, args, &thisVar, nullptr);
   154. if (argc != 1) {
   155. napi_throw_error(env, nullptr, "SetTransferDetached args number must be one.");
   156. return nullptr;
   157. }

   159. if (thisVar == nullptr) {
   160. return nullptr;
   161. }

   163. napi_valuetype type = napi_undefined;
   164. napi_typeof(env, args[0], &type);
   165. if (type != napi_boolean) {
   166. napi_throw_error(env, nullptr, "SetTransferDetached args is not boolean.");
   167. return nullptr;
   168. }

   170. bool isDetached;
   171. napi_get_value_bool(env, args[0], &isDetached);

   173. void* object = nullptr;
   174. napi_unwrap(env, thisVar, &object);
   175. if (object == nullptr) {
   176. return nullptr;
   177. }
   178. CustomNativeObject* obj = static_cast<CustomNativeObject*>(object);
   179. std::lock_guard<std::mutex> lock(obj->numberSetMutex_);
   180. obj->isDetached_ = isDetached;
   181. return nullptr;
   182. }

   184. bool isDetached_ = false;

   186. private:
   187. CustomNativeObject(const CustomNativeObject &) = delete;
   188. CustomNativeObject &operator=(const CustomNativeObject &) = delete;

   190. std::unordered_set<uint32_t> numberSet_{};
   191. std::mutex numberSetMutex_{};
   192. };

   194. void FinalizeCallback(napi_env env, void *data, void *hint)
   195. {
   196. return;
   197. }

   199. // 解绑回调，在序列化时调用，可在对象解绑时执行一些清理操作
   200. void* DetachCallback(napi_env env, void *value, void *hint)
   201. {
   202. if (hint == nullptr) {
   203. return value;
   204. }
   205. napi_value jsObject = nullptr;
   206. napi_get_reference_value(env, reinterpret_cast<napi_ref>(hint), &jsObject);
   207. void* object = nullptr;
   208. if (static_cast<CustomNativeObject*>(value)->isDetached_) {
   209. napi_remove_wrap(env, jsObject, &object);
   210. }
   211. return value;
   212. }

   214. // 绑定回调，在反序列化时调用
   215. napi_value AttachCallback(napi_env env, void* value, void* hint)
   216. {
   217. napi_value object = nullptr;
   218. napi_create_object(env, &object);
   219. napi_property_descriptor desc[] = {
   220. {"getAddress", nullptr, CustomNativeObject::GetAddress, nullptr, nullptr, nullptr, napi_default, nullptr},
   221. {"getSetSize", nullptr, CustomNativeObject::GetSetSize, nullptr, nullptr, nullptr, napi_default, nullptr},
   222. {"store", nullptr, CustomNativeObject::Store, nullptr, nullptr, nullptr, napi_default, nullptr},
   223. {"erase", nullptr, CustomNativeObject::Erase, nullptr, nullptr, nullptr, napi_default, nullptr},
   224. {"clear", nullptr, CustomNativeObject::Clear, nullptr, nullptr, nullptr, napi_default, nullptr}};
   225. napi_define_properties(env, object, sizeof(desc) / sizeof(desc[0]), desc);
   226. // 将JS对象object和native对象value生命周期进行绑定
   227. napi_wrap(env, object, value, FinalizeCallback, nullptr, nullptr);
   228. // JS对象携带native信息
   229. napi_coerce_to_native_binding_object(env, object, DetachCallback, AttachCallback, value, nullptr);
   230. return object;
   231. }

   233. EXTERN_C_START
   234. static napi_value Init(napi_env env, napi_value exports)
   235. {
   236. napi_property_descriptor desc[] = {
   237. {"getAddress", nullptr, CustomNativeObject::GetAddress, nullptr, nullptr, nullptr, napi_default, nullptr},
   238. {"getSetSize", nullptr, CustomNativeObject::GetSetSize, nullptr, nullptr, nullptr, napi_default, nullptr},
   239. {"store", nullptr, CustomNativeObject::Store, nullptr, nullptr, nullptr, napi_default, nullptr},
   240. {"erase", nullptr, CustomNativeObject::Erase, nullptr, nullptr, nullptr, napi_default, nullptr},
   241. {"clear", nullptr, CustomNativeObject::Clear, nullptr, nullptr, nullptr, napi_default, nullptr},
   242. {"setTransferDetached", nullptr, CustomNativeObject::SetTransferDetached,
   243. nullptr, nullptr, nullptr, napi_default, nullptr}};
   244. napi_define_properties(env, exports, sizeof(desc) / sizeof(desc[0]), desc);
   245. auto &object = CustomNativeObject::GetInstance();
   246. napi_wrap(env, exports, reinterpret_cast<void*>(&object), FinalizeCallback, nullptr, nullptr);
   247. napi_ref exportsRef;
   248. napi_create_reference(env, exports, 1, &exportsRef);
   249. napi_coerce_to_native_binding_object(env, exports, DetachCallback,
   250. AttachCallback, reinterpret_cast<void*>(&object), exportsRef);
   251. return exports;
   252. }
   253. EXTERN_C_END

   255. static napi_module demoModule = {
   256. .nm_version = 1,
   257. .nm_flags = 0,
   258. .nm_filename = nullptr,
   259. .nm_register_func = Init,
   260. .nm_modname = "entry",
   261. .nm_priv = ((void*)0),
   262. .reserved = { 0 },
   263. };

   265. extern "C" __attribute__((constructor)) void RegisterEntryModule(void)
   266. {
   267. napi_module_register(&demoModule);
   268. }
   ```
2. 在ArkTS中声明接口。

   ```
   1. // Index.d.ts
   2. export const getAddress: () => number;
   3. export const getSetSize: () => number;
   4. export const store: (a: number) => void;
   5. export const erase: (a: number) => void;
   6. export const clear: () => void;
   7. export const setTransferDetached: (b : boolean) => number;
   ```
3. ArkTS对象调用Native侧实现的各项功能。

   在转移模式下，跨线程传递后，原来的ArkTS对象与Native对象解绑，因此不能继续访问。示例如下：

   ```
   1. import testNapi from 'libentry.so';
   2. import { taskpool } from '@kit.ArkTS';

   4. @Concurrent
   5. function getAddress() {
   6. let address: number = testNapi.getAddress();
   7. console.info('taskpool:: address is ' + address);
   8. }

   10. @Concurrent
   11. function store(a:number, b:number, c:number) {
   12. let size:number = testNapi.getSetSize();
   13. console.info('set size is ' + size + ' before store');
   14. testNapi.store(a);
   15. testNapi.store(b);
   16. testNapi.store(c);
   17. size = testNapi.getSetSize();
   18. console.info('set size is ' + size + ' after store');
   19. }

   21. @Concurrent
   22. function erase(a:number) {
   23. let size:number = testNapi.getSetSize();
   24. console.info('set size is ' + size + ' before erase');
   25. testNapi.erase(a);
   26. size = testNapi.getSetSize();
   27. console.info('set size is ' + size + ' after erase');
   28. }

   30. @Concurrent
   31. function clear() {
   32. let size:number = testNapi.getSetSize();
   33. console.info('set size is ' + size + ' before clear');
   34. testNapi.clear();
   35. size = testNapi.getSetSize();
   36. console.info('set size is ' + size + ' after clear');
   37. }

   39. // 转移模式
   40. async function test(): Promise<void> {
   41. // setTransferDetached 设置为true，表示传输方式为转移模式
   42. testNapi.setTransferDetached(true);
   43. let address:number = testNapi.getAddress();
   44. console.info('host thread address is ' + address);

   46. let task1 = new taskpool.Task(getAddress, testNapi);
   47. await taskpool.execute(task1);

   49. let task2 = new taskpool.Task(store, 1, 2, 3);
   50. await taskpool.execute(task2);

   52. let task3 = new taskpool.Task(store, 4, 5, 6);
   53. await taskpool.execute(task3);

   55. // 由于已经设置了转移模式，且testNapi已跨线程传递，所以主线程无法继续访问到Native对象的值
   56. let size:number = testNapi.getSetSize();
   57. // 输出的日志为“host thread size is undefined”
   58. console.info('host thread size is ' + size);

   60. let task4 = new taskpool.Task(erase, 3);
   61. await taskpool.execute(task4);

   63. let task5 = new taskpool.Task(erase, 5);
   64. await taskpool.execute(task5);

   66. let task6 = new taskpool.Task(clear);
   67. await taskpool.execute(task6);
   68. }

   70. @Entry
   71. @Component
   72. struct Index {
   73. @State message: string = 'Hello World';

   75. build() {
   76. Row() {
   77. Column() {
   78. Text(this.message)
   79. .fontSize($r('app.float.page_text_font_size'))
   80. .fontWeight(FontWeight.Bold)
   81. .onClick(() => {
   82. test();
   83. })
   84. }
   85. .width('100%')
   86. }
   87. .height('100%')
   88. }
   89. }
   ```

   在共享模式下，跨线程传递后，原来的ArkTS对象还可以继续访问Native对象。示例如下：

   ```
   1. // Index.ets
   2. import testNapi from 'libentry.so';
   3. import { taskpool } from '@kit.ArkTS';

   5. @Concurrent
   6. function getAddress() {
   7. let address: number = testNapi.getAddress();
   8. console.info('taskpool:: address is ' + address);
   9. }

   11. @Concurrent
   12. function store(a:number, b:number, c:number) {
   13. let size:number = testNapi.getSetSize();
   14. console.info('set size is ' + size + ' before store');
   15. testNapi.store(a);
   16. testNapi.store(b);
   17. testNapi.store(c);
   18. size = testNapi.getSetSize();
   19. console.info('set size is ' + size + ' after store');
   20. }

   22. @Concurrent
   23. function erase(a:number) {
   24. let size:number = testNapi.getSetSize();
   25. console.info('set size is ' + size + ' before erase');
   26. testNapi.erase(a);
   27. size = testNapi.getSetSize();
   28. console.info('set size is ' + size + ' after erase');
   29. }

   31. @Concurrent
   32. function clear() {
   33. let size:number = testNapi.getSetSize();
   34. console.info('set size is ' + size + ' before clear');
   35. testNapi.clear();
   36. size = testNapi.getSetSize();
   37. console.info('set size is ' + size + ' after clear');
   38. }

   40. // 共享模式
   41. async function test(): Promise<void> {
   42. let address:number = testNapi.getAddress();
   43. console.info('host thread address is ' + address);

   45. let task1 = new taskpool.Task(getAddress, testNapi);
   46. await taskpool.execute(task1);

   48. let task2 = new taskpool.Task(store, 1, 2, 3);
   49. await taskpool.execute(task2);

   51. let task3 = new taskpool.Task(store, 4, 5, 6);
   52. await taskpool.execute(task3);

   54. // 由于默认的传输模式为共享模式，testNapi跨线程传递后，主线程可以继续访问Native对象的值
   55. let size:number = testNapi.getSetSize();
   56. // 输出的日志为“host thread size is 6”
   57. console.info('host thread size is ' + size);

   59. let task4 = new taskpool.Task(erase, 3);
   60. await taskpool.execute(task4);

   62. let task5 = new taskpool.Task(erase, 5);
   63. await taskpool.execute(task5);

   65. let task6 = new taskpool.Task(clear);
   66. await taskpool.execute(task6);
   67. }

   69. @Entry
   70. @Component
   71. struct Index {
   72. @State message: string = 'Hello World';

   74. build() {
   75. Row() {
   76. Column() {
   77. Text(this.message)
   78. .fontSize($r('app.float.page_text_font_size'))
   79. .fontWeight(FontWeight.Bold)
   80. .onClick(() => {
   81. test();
   82. })
   83. }
   84. .width('100%')
   85. }
   86. .height('100%')
   87. }
   88. }
   ```
