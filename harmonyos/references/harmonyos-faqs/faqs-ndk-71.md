---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-71
title: 多so相互依赖场景下如何解耦
breadcrumb: FAQ > 应用框架开发 > NDK开发 > NDK开发 > 多so相互依赖场景下如何解耦
category: harmonyos-faqs
scraped_at: 2026-04-29T14:16:00+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:35e53f67b1b03dccf3bbbf6edf728c66d8c575c628c43c60bd72bc37977140ff
---

**问题现象**

A模块包含a.so，B模块包含b.so。a.so调用b.so的函数，b.so也调用a.so的函数。按照正常编译步骤，无论先编译哪个so，都会编译失败。

**解决措施**

通过dlopen和dlsym接口进行SO编译依赖解耦，将隐式依赖转换为显式依赖。具体示例代码如下：

1. 修改代码和CMakeLists.txt文件，利用Native侧dlopen方法编译出liba.so和libb.so。生成的.so文件位于build/default/intermediates/cmake/default/obj目录下。

   （注意一定要用extern "C" {}括起来、不然不能识别到对应的函数导致编译出错）

   ```
   1. // a.cpp
   2. extern "C" {     // Be sure to enclose it with extern 'C' {}
   3. #include "a.h"
   4. #include <dlfcn.h>
   5. #include "stdio.h"
   6. typedef int (*FUNC_SUB)(int, int);
   7. int add(int a, int b) { return a + b; }
   8. int getb(char *path, int a, int b) {       // Path:The sandbox path for passing So files from ArkTS side (note that the path should be passed from ArkTS side, otherwise it may not be found, and the specific code will be listed later)
   9. void *handle = dlopen(path, RTLD_LAZY);  // Open the dynamic link library with path as path
   10. if (!handle) {
   11. return 0;
   12. }
   13. FUNC_SUB sub_func = (FUNC_SUB)dlsym(handle, "sub"); // Get the function named sub
   14. int res = sub_func(a, b);                           // caller function
   15. dlclose(handle);                                    // Close dynamic link library
   16. return res;
   17. }
   18. }
   ```

   [a.cpp](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/Ndk/ndk1/demoso/src/main/cpp/a.cpp#L10-L27)

   ```
   1. // a.h
   2. extern "C" {
   3. #ifndef DemoSO_a_H
   4. #define DemoSO_a_H
   5. int add(int a, int b);
   6. int getb(char *path, int a, int b);
   7. #endif // DemoSO_a_H
   8. }
   ```

   [a.h](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/Ndk/ndk1/demoso/src/main/cpp/a.h#L10-L17)

   ```
   1. // b.cpp
   2. extern "C" {     // Be sure to enclose it with extern 'C' {}
   3. #include "b.h"
   4. #include <dlfcn.h>
   5. #include "stdio.h"
   6. typedef int (*FUNC_ADD)(int, int);
   7. int sub(int a, int b) { return a - b; }
   8. int geta(char *path, int a, int b) {    // Path: The sandbox path for passing So files from ArkTS side (note that the path should be passed from ArkTS side, otherwise it may not be found, and the specific code will be listed later)
   9. void *handle = dlopen(path, RTLD_LAZY);    // Open the dynamic link library with path as path
   10. if (!handle) {
   11. return 0;
   12. }
   13. FUNC_ADD add_func = (FUNC_ADD)dlsym(handle, "add");      // Get the function named sub
   14. int res = add_func(a, b);                                // caller function
   15. dlclose(handle);                                         // Close dynamic link library
   16. return res;
   17. }
   18. }
   ```

   [b.cpp](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/Ndk/ndk1/demoso/src/main/cpp/b.cpp#L10-L27)

   ```
   1. // b.h
   2. extern "C" {
   3. #ifndef DemoSO_b_H
   4. #define DemoSO_b_H
   5. int sub(int a, int b);
   6. int geta(char *path, int a, int b);
   7. #endif // DemoSO_b_H
   8. }
   ```

   [b.h](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/Ndk/ndk1/demoso/src/main/cpp/b.h#L10-L17)

   ```
   1. # CMakeLists.txt
   2. cmake_minimum_required(VERSION 3.4.1)
   3. project(liba)
   4. # Compile library liba.so
   5. add_library(a SHARED a.cpp)
   6. target_link_libraries(a PUBLIC libace_napi.z.so libhilog_ndk.z.so)
   7. project(libb)
   8. # Compile library libb.so
   9. add_library(b SHARED b.cpp)
   10. target_link_libraries(b PUBLIC libace_napi.z.so libhilog_ndk.z.so)
   ```

   [CMakeLists1.txt](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/Ndk/ndk1/demoso/src/main/cpp/CMakeLists1.txt#L3-L12)
2. 将生成的.so文件（相对路径：build/default/intermediates/cmake/default/obj）移动到libs目录。

   移动完成后，目录结构如下：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/d3y2neuORbqzQs92cW12YA/zh-cn_image_0000002194158924.png?HW-CC-KV=V1&HW-CC-Date=20260429T061559Z&HW-CC-Expire=86400&HW-CC-Sign=3F266471974F3368B64C9D54CFA096A365A43FCD12A56E13798B5FDF65458FB8 "点击放大")
3. 修改CMakeLists.txt文件，将编译生成的.so文件引入到工程中。

   ```
   1. # CMakeLists.txt
   2. cmake_minimum_required(VERSION 3.4.1)
   3. project(DemoSO)
   4. set(NATIVERENDER_ROOT_PATH ${CMAKE_CURRENT_SOURCE_DIR})
   5. include_directories(${NATIVERENDER_ROOT_PATH}
   6. ${NATIVERENDER_ROOT_PATH}/include)
   7. # Add libdemoso. so file
   8. add_library(demoso SHARED hello.cpp)
   9. # Add dependency libraries liba.so and libb.so. Please note to include the path, otherwise the corresponding SO library cannot be found
   10. target_link_libraries(demoso PUBLIC libace_napi.z.so ${CMAKE_CURRENT_SOURCE_DIR}/../../../libs/${OHOS_ARCH}/liba.so ${CMAKE_CURRENT_SOURCE_DIR}/../../../libs/${OHOS_ARCH}/libb.so)
   ```

   [CMakeLists.txt](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/Ndk/ndk1/demoso/src/main/cpp/CMakeLists.txt#L3-L12)

   ```
   1. // index.ets
   2. import testNapi from 'libdemoso.so';
   3. import { hilog } from '@kit.PerformanceAnalysisKit';

   5. @Entry
   6. @Component
   7. struct Index {
   8. @State message: string = 'Hello World';
   9. private path: string = '';

   11. build() {
   12. Row() {
   13. Column() {
   14. Text(this.message)
   15. .fontSize(50)
   16. .fontWeight(FontWeight.Bold)
   17. .onClick(() => {
   18. this.path = this.getUIContext().getHostContext()!.bundleCodeDir;   // get path
   19. hilog.info(0x0000, 'testTag', 'Test NAPI 5 + 3 = %{public}d', testNapi.add(5, 3, this.path + '/libs/arm64/liba.so'));  // Call the native side function
   20. hilog.info(0x0000, 'testTag', 'Test NAPI 5 - 3 = %{public}d', testNapi.sub(5, 3, this.path + '/libs/arm64/libb.so'));
   21. })
   22. }
   23. .width('100%')
   24. }
   25. .height('100%')
   26. }
   27. }
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/Ndk/ndk1/demoso/src/main/ets/pages/Index.ets#L5-L31)

   ```
   1. // index.d.ts
   2. export const add: (a: number, b: number, path: string) => number;
   3. export const sub: (a: number, b: number, path: string) => number;
   ```

   [Index.d.ts](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/Ndk/ndk1/demoso/src/main/cpp/types/libdemoso/Index.d.ts#L5-L7)

   ```
   1. // hello.cpp
   2. #include "a.h"
   3. #include "b.h"
   4. #include "napi/native_api.h"

   6. static napi_value Add(napi_env env, napi_callback_info info) {
   7. size_t requireArgc = 3;
   8. size_t argc = 3;
   9. napi_value args[3] = {nullptr};
   10. napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);
   11. napi_valuetype valuetype0;
   12. napi_typeof(env, args[0], &valuetype0);
   13. napi_valuetype valuetype1;
   14. napi_typeof(env, args[1], &valuetype1);
   15. napi_valuetype valuetype2;
   16. napi_typeof(env, args[2], &valuetype2);
   17. int value0;
   18. napi_get_value_int32(env, args[0], &value0);
   19. int value1;
   20. napi_get_value_int32(env, args[1], &value1);
   21. char path[255];
   22. size_t size = 255;
   23. napi_get_value_string_utf8(env, args[2], path, 255, &size);
   24. int res = geta(path, value0, value1);                    // Call the function and pass the sandbox path
   25. napi_value sum;
   26. napi_create_int32(env, res, &sum);
   27. return sum;
   28. }
   29. static napi_value Sub(napi_env env, napi_callback_info info) {
   30. size_t requireArgc = 3;
   31. size_t argc = 3;
   32. napi_value args[3] = {nullptr};
   33. napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);
   34. napi_valuetype valuetype0;
   35. napi_typeof(env, args[0], &valuetype0);
   36. napi_valuetype valuetype1;
   37. napi_typeof(env, args[1], &valuetype1);
   38. napi_valuetype valuetype2;
   39. napi_typeof(env, args[2], &valuetype2);
   40. int value0;
   41. napi_get_value_int32(env, args[0], &value0);
   42. int value1;
   43. napi_get_value_int32(env, args[1], &value1);
   44. char path[255];
   45. size_t size = 255;
   46. napi_get_value_string_utf8(env, args[2], path, 255, &size);
   47. int res = getb(path, value0, value1);                 // Call the function and pass the sandbox path
   48. napi_value sum;
   49. napi_create_int32(env, res, &sum);
   50. return sum;
   51. }
   52. EXTERN_C_START
   53. static napi_value Init(napi_env env, napi_value exports) {
   54. napi_property_descriptor desc[] = {{"add", nullptr, Add, nullptr, nullptr, nullptr, napi_default, nullptr},
   55. {"sub", nullptr, Sub, nullptr, nullptr, nullptr, napi_default, nullptr}};
   56. napi_define_properties(env, exports, sizeof(desc) / sizeof(desc[0]), desc);
   57. return exports;
   58. }
   59. EXTERN_C_END

   61. static napi_module demoModule = {
   62. .nm_version = 1,
   63. .nm_flags = 0,
   64. .nm_filename = nullptr,
   65. .nm_register_func = Init,
   66. .nm_modname = "demoso",
   67. .nm_priv = ((void *)0),
   68. .reserved = {0},
   69. };
   70. extern "C" __attribute__((constructor)) void RegisterDemosoModule(void) { napi_module_register(&demoModule); }
   ```

   [hello.cpp](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/Ndk/ndk1/demoso/src/main/cpp/hello.cpp#L5-L74)
