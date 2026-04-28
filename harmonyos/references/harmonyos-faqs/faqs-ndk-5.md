---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-5
title: 在Native侧如何集成三方SO库
breadcrumb: FAQ > 应用框架开发 > NDK开发 > NDK开发 > 在Native侧如何集成三方SO库
category: harmonyos-faqs
scraped_at: 2026-04-28T08:24:29+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:26de715577592d672dc4a41246e8c210e06704d1150b43e67c96629d0d1ca862
---

开发过程可分为两个部分：

1. 系统编译生成so库。

   有关如何编译so库，请参考以下链接：

   [使用命令行CMake构建NDK工程](../harmonyos-guides/build-with-ndk-cmake.md)
2. 系统集成SO库
   * 方式一：直接集成
   * 方式二：通过dlopen集成

参考代码如下：

1. 系统编译SO库

   ```
   1. // sub.h
   2. extern "C" {
   3. double sub(double a, double b);
   4. }
   ```

   [sub.h](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/Ndk/ndk1/IntegrateThirdPartySO1/src/main/cpp/sub.h#L10-L13)

   ```
   1. // sub.cpp
   2. #include <iostream>
   3. #include "sub.h"
   4. double sub(double a, double b)
   5. {
   6. return a - b;
   7. }
   ```

   [sub.cpp](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/Ndk/ndk1/IntegrateThirdPartySO1/src/main/cpp/sub.cpp#L10-L16)

   ```
   1. # CMakeLists.txt
   2. cmake_minimum_required(VERSION 3.4.1)
   3. project(libSub)
   4. # Compile source code
   5. add_library(nativeSub SHARED sub.cpp)
   ```

   [CMakeLists.txt](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/Ndk/ndk1/IntegrateThirdPartySO1/src/main/cpp/CMakeLists.txt#L3-L7)
2. 系统集成SO库
   * Native侧直接集成

     将上步生成的so库置于entry/libs对应架构的目录下，将头文件放置到cpp目录下。修改CMakeLists.txt，将so库加入工程编译引用。在native侧引入头文件使用。

     ```
     1. # CMakeLists.txt
     2. # the minimum version of CMake.
     3. cmake_minimum_required(VERSION 3.5.0)
     4. project(ndk1)

     6. set(NATIVERENDER_ROOT_PATH ${CMAKE_CURRENT_SOURCE_DIR})

     8. if(DEFINED PACKAGE_FIND_FILE)
     9. include(${PACKAGE_FIND_FILE})
     10. endif()

     12. include_directories(${NATIVERENDER_ROOT_PATH}
     13. ${NATIVERENDER_ROOT_PATH}/include)

     15. add_library(entry SHARED napi_init.cpp)
     16. target_link_libraries(entry PUBLIC libace_napi.z.so  libhilog_ndk.z.so)
     17. target_link_libraries(entry PUBLIC ${NATIVERENDER_ROOT_PATH}/../../../libs/arm64-v8a/libnativeSub.so)
     ```

     [CMakeLists.txt](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/Ndk/ndk1/IntegrateThirdPartySO/src/main/cpp/CMakeLists.txt#L3-L19)

     ```
     1. #include "sub.h"

     3. static napi_value Sub(napi_env env, napi_callback_info info)
     4. {
     5. size_t requireArgc = 2;
     6. size_t argc = 2;
     7. napi_value args[2] = {nullptr};
     8. napi_get_cb_info(env, info, &argc, args , nullptr, nullptr);
     9. napi_valuetype valuetype0;
     10. napi_typeof(env, args[0], &valuetype0);
     11. napi_valuetype valuetype1;
     12. napi_typeof(env, args[1], &valuetype1);
     13. double value0;
     14. napi_get_value_double(env, args[0], &value0);
     15. double value1;
     16. napi_get_value_double(env, args[1], &value1);
     17. napi_value sum;
     18. napi_create_double(env, sub(value0, value1), &sum);
     19. return sum;
     20. }
     ```

     [sub.cpp](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/Ndk/ndk1/IntegrateThirdPartySO/src/main/cpp/sub.cpp#L11-L30)
   * Native侧通过dlopen方式集成

     将上步生成的so库置于entry/libs目录下，通过ArkTS侧传递沙箱路径到native侧，然后直接在native侧使用dlopen方式调用。注意：该方式引用的so库源码在编译时必须使用extern "C" {}包裹起来，即函数必须是使用C编译模式编译的。

     ```
     1. import { hilog } from '@kit.PerformanceAnalysisKit';
     2. import testNapi from 'libentry.so';

     4. @Entry
     5. @Component
     6. struct Index {
     7. @State message: string = 'Hello World';

     9. build() {
     10. Row() {
     11. Column() {
     12. Text(this.message)
     13. .fontSize(50)
     14. .fontWeight(FontWeight.Bold)
     15. .onClick(() => {
     16. let path = this.getUIContext().getHostContext()!.bundleCodeDir; // Get project path
     17. hilog.info(0x0000, 'testTag', 'Test NAPI 2 + 3 = %{public}d', testNapi.subSobyDlOpenSo(2, 3, path + '/libs/arm64/libnativeSub.so')); // Transfer parameter path information to the native side
     18. })
     19. }
     20. .width('100%')
     21. }
     22. .height('100%')
     23. }
     24. }
     ```

     [Index.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/Ndk/ndk1/IntegrateThirdPartySO/src/main/ets/pages/Index.ets#L5-L28)

     ```
     1. #include <dlfcn.h>
     2. typedef double (*Sub)(double, double);
     3. static napi_value SubSobyDlOpenSo(napi_env env, napi_callback_info info) {
     4. size_t requireArgc = 3;
     5. size_t argc = 3;
     6. napi_value args[3] = {nullptr};
     7. napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);
     8. double value0;
     9. napi_get_value_double(env, args[0], &value0);
     10. double value1;
     11. napi_get_value_double(env, args[1], &value1);
     12. char* path = new char[1024];
     13. size_t size = 1024;
     14. napi_get_value_string_utf8(env, args[2], path, 255, &size); // Obtain dynamic library path information
     15. void *handle = dlopen(path, RTLD_LAZY);                     // Open the dynamic link library with path as path
     16. napi_value result;
     17. Sub sub_func = (Sub)dlsym(handle, "sub");                   // Get the function named sub
     18. napi_create_double(env, sub_func(value0, value1), &result);
     19. dlclose(handle);                                            // Finally, close the dynamic library
     20. return result;
     21. }
     ```

     [napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/Ndk/ndk1/IntegrateThirdPartySO/src/main/cpp/napi_init.cpp#L7-L27)
