---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/use-napi-load-module
title: 使用Node-API接口在主线程中进行模块加载
breadcrumb: 指南 > NDK开发 > 代码开发 > 使用Node-API实现ArkTS/JS与C/C++语言交互 > Node-API典型使用场景 > 使用Node-API接口在主线程中进行模块加载
category: harmonyos-guides
scraped_at: 2026-04-28T07:54:09+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:e241c2b2772e6a8055dc767726306024b8597052fa7e0d65e06e5af595278712
---

## 场景介绍

Node-API中的napi\_load\_module接口的功能是在主线程中进行模块的加载，当模块加载出来之后，可以使用函数napi\_get\_property获取模块导出的变量，也可以使用napi\_get\_named\_property获取模块导出的函数。

## 函数说明

```
1. napi_status napi_load_module(napi_env env, const char* path, napi_value* result);
```

| 参数 | 说明 |
| --- | --- |
| env | 当前的虚拟机环境 |
| path | 加载的文件路径或者模块名 |
| result | 加载的模块 |

## 使用限制

* 禁止在非主线程当中使用该接口。
* 禁止在Init函数中使用该接口。
* 禁止在线程安全函数的回调函数当中进行文件路径的加载。
* 在信号函数中调用不安全，直接调用可能导致栈溢出。

建议使用[napi\_load\_module\_with\_info](use-napi-load-module-with-info.md)来进行模块加载，该接口支持了更多的场景。

## napi\_load\_module支持的场景

| 场景 | 详细分类 | 说明 |
| --- | --- | --- |
| 系统模块 | 加载@ohos.或 @system. | - |
| 本地工程模块 | 加载ets目录下文件中的模块 | 要求路径以ets开头 |
| 本地工程模块 | 加载模块内文件路径 | 要求路径以moduleName开头 |
| 本地工程模块 | 加载HAR模块名 | - |
| 本地工程模块 | 加载HSP模块名 | - |
| 远程包 | 加载远程HAR模块名 | - |
| 远程包 | 加载ohpm包名 | - |
| 模块Native库 | 加载Native模块(.so文件) | - |

* **加载系统模块**

  ```
  1. static napi_value loadModule(napi_env env, napi_callback_info info)
  2. {
  3. // 1. 使用napi_load_module加载模块@ohos.hilog
  4. napi_value result;
  5. napi_status status = napi_load_module(env, "@ohos.hilog", &result);
  6. if (status != napi_ok) {
  7. return nullptr;
  8. }

  10. // 2. 使用napi_get_named_property获取info函数
  11. napi_value infoFn;
  12. status = napi_get_named_property(env, result, "info", &infoFn);
  13. if (status != napi_ok) {
  14. return nullptr;
  15. }

  17. napi_value tag;
  18. std::string formatStr = "test";
  19. napi_create_string_utf8(env, formatStr.c_str(), formatStr.size(), &tag);

  21. napi_value outputString;
  22. std::string str = "Hello HarmonyOS";
  23. napi_create_string_utf8(env, str.c_str(), str.size(), &outputString);

  25. napi_value flag;
  26. napi_create_int32(env, 0, &flag);

  28. napi_value args[3] = {flag, tag, outputString};
  29. // 3. 使用napi_call_function调用info函数
  30. status = napi_call_function(env, result, infoFn, 3, args, nullptr);
  31. if (status != napi_ok) {
  32. return nullptr;
  33. }
  34. return result;
  35. }
  ```
* **加载ets目录下文件中的模块**

  当加载文件中的模块时，如以下ArkTS代码：

  ```
  1. let value = 123;
  2. function test() {
  3. console.info('Hello HarmonyOS');
  4. }
  5. export {value, test};
  ```

1. 需要在模块的build-profile.json5文件中进行以下配置：

   ```
   1. "buildOption": {
   2. "arkOptions" : {
   3. "runtimeOnly" : {
   4. "sources": [
   5. "./src/main/ets/Test.ets"
   6. ],
   7. "packages": [
   8. "library",
   9. "sharedlibrary",
   10. "@ohos/hypium",
   11. "@ohos/axios",
   12. "libentry7.so"
   13. ]
   14. }
   15. },
   ```
2. 使用napi\_load\_module加载Test文件，调用函数test以及获取变量value：

   ```
   1. static napi_value loadModule(napi_env env, napi_callback_info info)
   2. {
   3. napi_value result;
   4. // 1. 使用napi_load_module加载Test文件中的模块
   5. napi_status status = napi_load_module(env, "ets/Test", &result);
   6. if (status != napi_ok) {
   7. return nullptr;
   8. }

   10. napi_value testFn;
   11. // 2. 使用napi_get_named_property获取test函数
   12. status = napi_get_named_property(env, result, "test", &testFn);
   13. if (status != napi_ok) {
   14. return nullptr;
   15. }
   16. // 3. 使用napi_call_function调用函数test
   17. status = napi_call_function(env, result, testFn, 0, nullptr, nullptr);
   18. if (status != napi_ok) {
   19. return nullptr;
   20. }

   22. napi_value value;
   23. napi_value key;
   24. std::string keyStr = "value";
   25. napi_create_string_utf8(env, keyStr.c_str(), keyStr.size(), &key);
   26. // 4. 使用napi_get_property获取变量value
   27. status = napi_get_property(env, result, key, &value);
   28. if (status != napi_ok) {
   29. return nullptr;
   30. }
   31. return result;
   32. }
   ```

* **加载模块内文件路径**

  当加载文件中的模块时，如以下ArkTS代码：

  ```
  1. //./src/main/ets/Test.ets
  2. let value = 123;
  3. function test() {
  4. console.info("Hello HarmonyOS");
  5. }
  6. export {value, test};
  ```

1. 需要当前模块的build-profile.json5文件中进行以下配置：

   ```
   1. {
   2. "buildOption" : {
   3. "arkOptions" : {
   4. "runtimeOnly" : {
   5. "sources": [
   6. "./src/main/ets/Test.ets"
   7. ]
   8. }
   9. }
   10. }
   11. }
   ```
2. 使用napi\_load\_module加载Test文件，调用函数test以及获取变量value：

   ```
   1. static napi_value loadModule(napi_env env, napi_callback_info info) {
   2. napi_value result;
   3. // 1. 使用napi_load_module加载Test文件中的模块
   4. napi_status status = napi_load_module(env, "entry/src/main/ets/Test", &result);
   5. if (status != napi_ok) {
   6. return nullptr;
   7. }

   9. napi_value testFn;
   10. // 2. 使用napi_get_named_property获取test函数
   11. status = napi_get_named_property(env, result, "test", &testFn);
   12. if (status != napi_ok) {
   13. return nullptr;
   14. }
   15. // 3. 使用napi_call_function调用函数test
   16. status = napi_call_function(env, result, testFn, 0, nullptr, nullptr);
   17. if (status != napi_ok) {
   18. return nullptr;
   19. }

   21. napi_value value;
   22. napi_value key;
   23. std::string keyStr = "value";
   24. napi_create_string_utf8(env, keyStr.c_str(), keyStr.size(), &key);
   25. // 4. 使用napi_get_property获取变量value
   26. status = napi_get_property(env, result, key, &value);
   27. if (status != napi_ok) {
   28. return nullptr;
   29. }
   30. return result;
   31. }
   ```

* **加载HAR模块名**

  HAR包Index.ets文件如下：

  ```
  1. //library Index.ets
  2. let value = 123;
  3. function test() {
  4. console.info("Hello HarmonyOS");
  5. }
  6. export {value, test};
  ```

1. 在当前模块下的oh-package.json5文件中配置dependencies项：

   ```
   1. {
   2. "dependencies": {
   3. "library": "file:../library"
   4. }
   5. }
   ```
2. 在使用library的模块中，对build-profile.json5进行配置：

   ```
   1. {
   2. "buildOption" : {
   3. "arkOptions" : {
   4. "runtimeOnly" : {
   5. "packages": [
   6. "library"
   7. ]
   8. }
   9. }
   10. }
   11. }
   ```
3. 用napi\_load\_module加载library，调用函数test以及获取变量value：

   ```
   1. static napi_value loadModule(napi_env env, napi_callback_info info) {
   2. napi_value result;
   3. // 1. 使用napi_load_module加载library
   4. napi_status status = napi_load_module(env, "library", &result);
   5. if (status != napi_ok) {
   6. return nullptr;
   7. }

   9. napi_value testFn;
   10. // 2. 使用napi_get_named_property获取test函数
   11. status = napi_get_named_property(env, result, "test", &testFn);
   12. if (status != napi_ok) {
   13. return nullptr;
   14. }
   15. // 3. 使用napi_call_function调用函数test
   16. status = napi_call_function(env, result, testFn, 0, nullptr, nullptr);
   17. if (status != napi_ok) {
   18. return nullptr;
   19. }

   21. napi_value value;
   22. napi_value key;
   23. std::string keyStr = "value";
   24. napi_create_string_utf8(env, keyStr.c_str(), keyStr.size(), &key);
   25. // 4. 使用napi_get_property获取变量value
   26. status = napi_get_property(env, result, key, &value);
   27. if (status != napi_ok) {
   28. return nullptr;
   29. }
   30. return result;
   31. }
   ```

* **加载HSP模块名**

  HSP包Index.ets文件如下：

  ```
  1. //sharedlibrary Index.ets
  2. let value = 123;
  3. function test() {
  4. console.info("Hello HarmonyOS");
  5. }
  6. export {value, test};
  ```

1. 在当前模块下的oh-package.json5文件中配置dependencies项：

   ```
   1. {
   2. "dependencies": {
   3. "sharedlibrary": "file:../sharedlibrary"
   4. }
   5. }
   ```
2. 在使用library的模块中，对build-profile.json5进行配置：

   ```
   1. {
   2. "buildOption" : {
   3. "arkOptions" : {
   4. "runtimeOnly" : {
   5. "packages": [
   6. "sharedlibrary"
   7. ]
   8. }
   9. }
   10. }
   11. }
   ```
3. 用napi\_load\_module加载sharedlibrary，调用函数test以及获取变量value：

   ```
   1. static napi_value loadModule(napi_env env, napi_callback_info info) {
   2. napi_value result;
   3. // 1. 使用napi_load_module加载sharedlibrary
   4. napi_status status = napi_load_module(env, "sharedlibrary", &result);
   5. if (status != napi_ok) {
   6. return nullptr;
   7. }

   9. napi_value testFn;
   10. // 2. 使用napi_get_named_property获取test函数
   11. status = napi_get_named_property(env, result, "test", &testFn);
   12. if (status != napi_ok) {
   13. return nullptr;
   14. }
   15. // 3. 使用napi_call_function调用函数test
   16. status = napi_call_function(env, result, testFn, 0, nullptr, nullptr);
   17. if (status != napi_ok) {
   18. return nullptr;
   19. }

   21. napi_value value;
   22. napi_value key;
   23. std::string keyStr = "value";
   24. napi_create_string_utf8(env, keyStr.c_str(), keyStr.size(), &key);
   25. // 4. 使用napi_get_property获取变量value
   26. status = napi_get_property(env, result, key, &value);
   27. if (status != napi_ok) {
   28. return nullptr;
   29. }
   30. return result;
   31. }
   ```

* **加载远程HAR模块名**

1. 在当前模块下的oh-package.json5文件中配置dependencies项：

   ```
   1. {
   2. "dependencies": {
   3. "@ohos/hypium": "1.0.16"
   4. }
   5. }
   ```
2. 在使用@ohos/hypium的模块中，对build-profile.json5进行配置：

   ```
   1. {
   2. "buildOption" : {
   3. "arkOptions" : {
   4. "runtimeOnly" : {
   5. "packages": [
   6. "@ohos/hypium"
   7. ]
   8. }
   9. }
   10. }
   11. }
   ```
3. 用napi\_load\_module加载@ohos/hypium，获取DEFAULT变量：

   ```
   1. static napi_value loadModule(napi_env env, napi_callback_info info) {
   2. napi_value result;
   3. // 1. 使用napi_load_module加载@ohos/hypium
   4. napi_status status = napi_load_module(env, "@ohos/hypium", &result);
   5. if (status != napi_ok) {
   6. return nullptr;
   7. }

   9. napi_value key;
   10. std::string keyStr = "DEFAULT";
   11. napi_create_string_utf8(env, keyStr.c_str(), keyStr.size(), &key);
   12. // 2. 使用napi_get_property获取DEFAULT变量
   13. napi_value defaultValue;
   14. status = napi_get_property(env, result, key, &defaultValue);
   15. if (status != napi_ok) {
   16. return nullptr;
   17. }
   18. return result;
   19. }
   ```

* **加载ohpm包名**

1. 在当前模块下的oh-package.json5文件中配置dependencies项：

   ```
   1. {
   2. "dependencies": {
   3. "@ohos/axios": "2.2.4",
   4. }
   5. }
   ```
2. 在使用@ohos/axios的模块中，对build-profile.json5进行配置：

   ```
   1. {
   2. "buildOption" : {
   3. "arkOptions" : {
   4. "runtimeOnly" : {
   5. "packages": [
   6. "@ohos/axios"
   7. ]
   8. }
   9. }
   10. }
   11. }
   ```
3. 用napi\_load\_module加载@ohos/axios，获取VERSION变量：

   ```
   1. static napi_value loadModule(napi_env env, napi_callback_info info) {
   2. napi_value result;
   3. // 1. 使用napi_load_module加载@ohos/axios
   4. napi_status status = napi_load_module(env, "@ohos/axios", &result);
   5. if (status != napi_ok) {
   6. return nullptr;
   7. }

   9. napi_value key;
   10. std::string keyStr = "VERSION";
   11. napi_create_string_utf8(env, keyStr.c_str(), keyStr.size(), &key);
   12. // 2. 使用napi_get_property获取VERSION
   13. napi_value defaultValue;
   14. status = napi_get_property(env, result, key, &defaultValue);
   15. if (status != napi_ok) {
   16. return nullptr;
   17. }
   18. return result;
   19. }
   ```

* **加载Native库**

  libentry.so的index.d.ts文件如下：

  ```
  1. //index.d.ts
  2. export const add: (a: number, b: number) => number;
  ```

1. 在当前模块下的oh-package.json5文件中配置dependencies项：

   ```
   1. {
   2. "dependencies": {
   3. "libentry.so": "file:../src/main/cpp/types/libentry"
   4. }
   5. }
   ```
2. 在使用libentry.so的模块中，对build-profile.json5进行配置：

   ```
   1. {
   2. "buildOption" : {
   3. "arkOptions" : {
   4. "runtimeOnly" : {
   5. "packages": [
   6. "libentry.so"
   7. ]
   8. }
   9. }
   10. }
   11. }
   ```
3. 用napi\_load\_module加载libentry.so，调用函数add：

   ```
   1. static napi_value loadModule(napi_env env, napi_callback_info info) {
   2. napi_value result;
   3. // 1. 使用napi_load_module加载libentry.so
   4. napi_status status = napi_load_module(env, "libentry.so", &result);
   5. if (status != napi_ok) {
   6. return nullptr;
   7. }

   9. napi_value addFn;
   10. // 2. 使用napi_get_named_property获取add函数
   11. status = napi_get_named_property(env, result, "add", &addFn);
   12. if (status != napi_ok) {
   13. return nullptr;
   14. }

   16. napi_value a;
   17. napi_value b;
   18. napi_create_int32(env, 2, &a);
   19. napi_create_int32(env, 3, &b);
   20. napi_value args[2] = {a, b};
   21. // 3. 使用napi_call_function调用函数add
   22. napi_value returnValue;
   23. status = napi_call_function(env, result, addFn, 2, args, &returnValue);
   24. if (status != napi_ok) {
   25. return nullptr;
   26. }
   27. return result;
   28. }
   ```

* **HAR加载HAR模块名**

  场景为har1加载har2，har2中的Index.ets文件如下：

  ```
  1. //har2 Index.ets
  2. let value = 123;
  3. function test() {
  4. console.info("Hello HarmonyOS");
  5. }
  6. export {value, test};
  ```

1. 在har1中的oh-package.json5文件中配置dependencies项：

   ```
   1. {
   2. "dependencies": {
   3. "har2": "file:../har2"
   4. }
   5. }
   ```
2. 在har1的build-profile.json5文件中进行配置：

   ```
   1. {
   2. "buildOption" : {
   3. "arkOptions" : {
   4. "runtimeOnly" : {
   5. "packages": [
   6. "har2"
   7. ]
   8. }
   9. }
   10. }
   11. }
   ```
3. 在har1中用napi\_load\_module加载har2，调用函数test以及获取变量value：

   ```
   1. static napi_value loadModule(napi_env env, napi_callback_info info) {
   2. napi_value result;
   3. // 1. 使用napi_load_module加载har2
   4. napi_status status = napi_load_module(env, "har2", &result);
   5. if (status != napi_ok) {
   6. return nullptr;
   7. }

   9. napi_value testFn;
   10. // 2. 使用napi_get_named_property获取test函数
   11. status = napi_get_named_property(env, result, "test", &testFn);
   12. if (status != napi_ok) {
   13. return nullptr;
   14. }
   15. // 3. 使用napi_call_function调用函数test
   16. status = napi_call_function(env, result, testFn, 0, nullptr, nullptr);
   17. if (status != napi_ok) {
   18. return nullptr;
   19. }

   21. napi_value value;
   22. napi_value key;
   23. std::string keyStr = "value";
   24. napi_create_string_utf8(env, keyStr.c_str(), keyStr.size(), &key);
   25. // 4. 使用napi_get_property获取变量value
   26. status = napi_get_property(env, result, key, &value);
   27. if (status != napi_ok) {
   28. return nullptr;
   29. }
   30. return result;
   31. }
   ```
