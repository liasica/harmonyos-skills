---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/use-napi-load-module-with-info
title: 使用Node-API接口进行模块加载
breadcrumb: 指南 > NDK开发 > 代码开发 > 使用Node-API实现ArkTS/JS与C/C++语言交互 > Node-API典型使用场景 > 使用Node-API接口进行模块加载
category: harmonyos-guides
scraped_at: 2026-04-29T13:44:06+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:02b689bbe90a40bc775268c52e86c39256afe81c64595268b011200d72e26fa1
---

Node-API中的napi\_load\_module\_with\_info接口的功能是进行模块的加载，当模块加载出来之后，可以使用函数napi\_get\_property获取模块导出的变量，也可以使用napi\_get\_named\_property获取模块导出的函数，该函数可以在[新创建的ArkTS基础运行时环境](use-napi-ark-runtime.md)中使用，即napi\_create\_ark\_runtime接口创建的运行时环境。

## 函数说明

```
1. napi_status napi_load_module_with_info(napi_env env, const char* path, const char* module_info, napi_value* result);
```

| 参数 | 说明 |
| --- | --- |
| env | 当前的虚拟机环境 |
| path | 加载的文件路径或者模块名 |
| module\_info | bundleName/moduleName的路径拼接 |
| result | 加载的模块 |

注意

1. bundleName表示AppScope/app.json5中配置的工程名。
2. moduleName指的是待加载模块所在的HAP下module.json5中配置的名字。

## napi\_load\_module\_with\_info支持的场景

| 场景 | 详细分类 | 说明 |
| --- | --- | --- |
| 本地工程模块 | 加载模块内文件路径 | 要求路径以moduleName开头 |
| 本地工程模块 | 加载HAR模块名 | - |
| 远程包 | 加载远程HAR模块名 | - |
| 远程包 | 加载ohpm包名 | - |
| API | 加载@ohos.或 @system. | - |
| 模块Native库 | 加载libNativeLibrary.so | - |

注意

1. 加载一个模块名，实际的行为是加载该模块的入口文件，一般为index.ets/ts。
2. 如果在HAR中加载另外一个HAR，需要确保module\_info的配置正确，尤其注意moduleName应为HAP的moduleName或者HSP的moduleName。
3. 如果在HAP/HSP中直接或间接使用了三方包，该三方包中使用napi\_load\_module\_with\_info接口加载其他模块A，则需要在HAP/HSP中也添加A的依赖。
4. 在信号函数中调用不安全，直接调用可能导致栈溢出。

## 异常场景

1. 在模块加载过程中，若出现包内未找到对应文件或build-profile.json5配置错误等问题，返回错误码napi\_generic\_failure，并打印报错日志。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/XSop2l3KRLe87AlSkbV2Jg/zh-cn_image_0000002558765874.png?HW-CC-KV=V1&HW-CC-Date=20260429T054405Z&HW-CC-Expire=86400&HW-CC-Sign=61561C8B09EB884D0CEAD1D899BD7CD1853A3044932194805424E6EA2CD4C381)
2. 系统侧发生非预期行为导致加载模块无法正常执行，将抛出cppcrash。

## 使用示例

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

1. 当前模块的build-profile.json5文件中需进行以下配置：

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
2. 使用napi\_load\_module\_with\_info加载Test文件，调用函数test以及获取变量value。

   注意

   开启useNormalizedOHMUrl后（即将工程目录中与entry同级别的应用级build-profile.json5文件中strictMode属性的useNormalizedOHMUrl字段配置为true），加载模块内文件路径时：

   1. bundleName不会影响最终加载逻辑，会智能通过module名索引进程内对应的hap，例如：工程的bundleName为com.example.application，实际入参时填写为 com.example.application1，模块也能正常加载。
   2. 路径需要以packageName开头，packageName指的是模块的oh-package.json5中配置的name字段。

   ```
   1. static napi_value loadModule(napi_env env, napi_callback_info info) {
   2. napi_value result;
   3. // 1. 使用napi_load_module_with_info加载Test文件中的模块
   4. napi_status status = napi_load_module_with_info(env, "entry/src/main/ets/Test", "com.example.application/entry", &result);
   5. if (status != napi_ok) {
   6. return nullptr;
   7. }

   9. napi_value testFn;
   10. // 2. 使用napi_get_named_property获取test函数
   11. napi_get_named_property(env, result, "test", &testFn);
   12. // 3. 使用napi_call_function调用函数test
   13. napi_call_function(env, result, testFn, 0, nullptr, nullptr);

   15. napi_value value;
   16. napi_value key;
   17. std::string keyStr = "value";
   18. napi_create_string_utf8(env, keyStr.c_str(), keyStr.size(), &key);
   19. // 4. 使用napi_get_property获取变量value
   20. napi_get_property(env, result, key, &value);
   21. return result;
   22. }
   ```

* **加载源码HAR模块**

HAR包Index.ets文件如下：

```
1. //library Index.ets
2. let value = 123;
3. function test() {
4. console.info("Hello HarmonyOS");
5. }
6. export {value, test};
```

1. 在oh-package.json5文件中配置dependencies项：

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
3. 使用napi\_load\_module\_with\_info加载library，调用函数test以及获取变量value：

   ```
   1. static napi_value loadModule(napi_env env, napi_callback_info info) {
   2. napi_value result;
   3. // 1. 使用napi_load_module_with_info加载library
   4. napi_status status = napi_load_module_with_info(env, "library", "com.example.application/entry", &result);
   5. if (status != napi_ok) {
   6. return nullptr;
   7. }

   9. napi_value testFn;
   10. // 2. 使用napi_get_named_property获取test函数
   11. napi_get_named_property(env, result, "test", &testFn);
   12. // 3. 使用napi_call_function调用函数test
   13. status = napi_call_function(env, result, testFn, 0, nullptr, nullptr);
   14. if (status != napi_ok) {
   15. return nullptr;
   16. }

   18. napi_value value;
   19. napi_value key;
   20. std::string keyStr = "value";
   21. napi_create_string_utf8(env, keyStr.c_str(), keyStr.size(), &key);
   22. // 4. 使用napi_get_property获取变量value
   23. status = napi_get_property(env, result, key, &value);
   24. if (status != napi_ok) {
   25. return nullptr;
   26. }
   27. return result;
   28. }
   ```

* **加载源码HSP模块**

HSP包Index.ets文件如下：

```
1. //hsp Index.ets
2. let value = 123;
3. function test() {
4. console.info("Hello World");
5. }
6. export {value, test};
```

1. 在oh-package.json5文件中配置dependencies项：

   ```
   1. {
   2. "dependencies": {
   3. "hsp": "file:../hsp"
   4. }
   5. }
   ```
2. 在使用hsp的模块中，对build-profile.json5进行配置：

   ```
   1. {
   2. "buildOption" : {
   3. "arkOptions" : {
   4. "runtimeOnly" : {
   5. "packages": [
   6. "hsp"
   7. ]
   8. }
   9. }
   10. }
   11. }
   ```
3. 使用napi\_load\_module\_with\_info加载hsp，调用函数test以及获取变量value：

   ```
   1. static napi_value loadModule(napi_env env, napi_callback_info info) {
   2. napi_value result;
   3. // 1. 使用napi_load_module_with_info加载hsp
   4. napi_status status = napi_load_module_with_info(env, "hsp", "com.example.application/entry", &result);
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

1. 在oh-package.json5文件中配置dependencies项：

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
3. 使用napi\_load\_module\_with\_info加载@ohos/hypium，获取DEFAULT变量：

   ```
   1. static napi_value loadModule(napi_env env, napi_callback_info info) {
   2. napi_value result;
   3. // 1. 使用napi_load_module_with_info加载@ohos/hypium
   4. napi_status status = napi_load_module_with_info(env, "@ohos/hypium", "com.example.application/entry", &result);
   5. if (status != napi_ok) {
   6. return nullptr;
   7. }

   9. napi_value key;
   10. std::string keyStr = "DEFAULT";
   11. napi_create_string_utf8(env, keyStr.c_str(), keyStr.size(), &key);
   12. // 2. 使用napi_get_property获取DEFAULT变量
   13. napi_value defaultValue;
   14. napi_get_property(env, result, key, &defaultValue);
   15. return result;
   16. }
   ```

* **加载ohpm包名**

1. 在oh-package.json5文件中配置dependencies项：

   ```
   1. {
   2. "dependencies": {
   3. "json5": "^2.2.3"
   4. }
   5. }
   ```
2. 在使用json5的模块中，对build-profile.json5进行配置：

   ```
   1. {
   2. "buildOption" : {
   3. "arkOptions" : {
   4. "runtimeOnly" : {
   5. "packages": [
   6. "json5"
   7. ]
   8. }
   9. }
   10. }
   11. }
   ```
3. 用napi\_load\_module\_with\_info加载json5，调用函数stringify：

   ```
   1. static napi_value loadModule(napi_env env, napi_callback_info info) {
   2. napi_value result;
   3. // 1. 使用napi_load_module_with_info加载json5
   4. napi_status status = napi_load_module_with_info(env, "json5", "com.example.application/entry", &result);
   5. if (status != napi_ok) {
   6. return nullptr;
   7. }

   9. napi_value key;
   10. std::string keyStr = "default";
   11. napi_create_string_utf8(env, keyStr.c_str(), keyStr.size(), &key);
   12. // 2. 使用napi_get_property获取default对象
   13. napi_value defaultValue;
   14. napi_get_property(env, result, key, &defaultValue);

   16. napi_value stringifyFn;
   17. // 3. 使用napi_get_named_property获取stringify函数
   18. napi_get_named_property(env, defaultValue, "stringify", &stringifyFn);
   19. // 4. 使用napi_call_function调用函数stringify
   20. napi_value argStr;
   21. std::string text = "call json5 stringify";
   22. napi_create_string_utf8(env, text.c_str(), text.size(), &argStr);
   23. napi_value args[1] = {argStr};

   25. napi_value returnValue;
   26. napi_call_function(env, defaultValue, stringifyFn, 1, args, &returnValue);
   27. return result;
   28. }
   ```

* **加载API模块**

```
1. static napi_value loadModule(napi_env env, napi_callback_info info) {
2. // 1. 使用napi_load_module_with_info加载模块@ohos.hilog
3. napi_value result;
4. napi_status status = napi_load_module_with_info(env, "@ohos.hilog", nullptr, &result);
5. if (status != napi_ok) {
6. return nullptr;
7. }

9. // 2. 使用napi_get_named_property获取info函数
10. napi_value infoFn;
11. status = napi_get_named_property(env, result, "info", &infoFn);
12. if (status != napi_ok) {
13. return nullptr;
14. }

16. napi_value tag;
17. std::string formatStr = "test";
18. napi_create_string_utf8(env, formatStr.c_str(), formatStr.size(), &tag);

20. napi_value outputString;
21. std::string str = "Hello HarmonyOS";
22. napi_create_string_utf8(env, str.c_str(), str.size(), &outputString);

24. napi_value flag;
25. napi_create_int32(env, 0, &flag);

27. napi_value args[3] = {flag, tag, outputString};
28. // 3. 使用napi_call_function调用info函数
29. status = napi_call_function(env, result, infoFn, 3, args, nullptr);
30. if (status != napi_ok) {
31. return nullptr;
32. }
33. return result;
34. }
```

* **加载Native库**

libentry.so的index.d.ts文件如下：

```
1. //index.d.ts
2. export const add: (a: number, b: number) => number;
```

1. 在oh-package.json5文件中配置dependencies项：

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
3. 用napi\_load\_module\_with\_info加载libentry.so，调用函数add：

   ```
   1. static constexpr int INT_NUM_2 = 2; // int类型数值2
   2. static constexpr int INT_NUM_3 = 3; // int类型数值3

   4. static napi_value loadModule(napi_env env, napi_callback_info info) {
   5. napi_value result;
   6. // 1. 使用napi_load_module_with_info加载libentry.so
   7. napi_status status = napi_load_module_with_info(env, "libentry.so", "com.example.application/entry", &result);
   8. if (status != napi_ok) {
   9. return nullptr;
   10. }

   12. napi_value addFn;
   13. // 2. 使用napi_get_named_property获取add函数
   14. napi_get_named_property(env, result, "add", &addFn);

   16. napi_value a;
   17. napi_value b;
   18. napi_create_int32(env, INT_NUM_2, &a);
   19. napi_create_int32(env, INT_NUM_3, &b);
   20. napi_value args[2] = {a, b};
   21. // 3. 使用napi_call_function调用函数add
   22. napi_value returnValue;
   23. napi_call_function(env, result, addFn, INT_NUM_2, args, &returnValue);
   24. return result;
   25. }
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
3. 在har1中使用napi\_load\_module\_with\_info加载har2，调用test函数并获取value变量：

   ```
   1. static napi_value loadModule(napi_env env, napi_callback_info info) {
   2. napi_value result;
   3. // 1. 使用napi_load_module_with_info加载har2，注意这里的moduleName为模块所在HAP包的moduleName
   4. napi_status status = napi_load_module_with_info(env, "har2", "com.example.application/entry", &result);
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
