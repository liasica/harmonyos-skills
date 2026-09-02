---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-5
title: 在Native侧如何集成三方SO库
breadcrumb: FAQ > 应用框架开发 > NDK开发 > NDK开发 > 在Native侧如何集成三方SO库
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:56+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:d05e70091f8a9843429b699304d8a9e0a366d69f62cb5aba7f7798d6ab51abe2
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

   ```cpp
   // sub.h 
   extern "C" {
   double sub(double a, double b); 
   }
   ```

   ```cpp
   // sub.cpp 
   #include <iostream> 
   #include "sub.h" 
   double sub(double a, double b) 
   { 
       return a - b; 
   }
   ```

   ```text
   # CMakeLists.txt
   cmake_minimum_required(VERSION 3.4.1)
   project(libSub)
   # Compile source code 
   add_library(nativeSub SHARED sub.cpp)
   ```
2. 系统集成SO库
   * Native侧直接集成

     将上步生成的so库置于entry/libs对应架构的目录下，将头文件放置到cpp目录下。修改CMakeLists.txt，将so库加入工程编译引用。在native侧引入头文件使用。

     ```text
     # CMakeLists.txt
     # the minimum version of CMake.
     cmake_minimum_required(VERSION 3.5.0)
     project(ndk1)

     set(NATIVERENDER_ROOT_PATH ${CMAKE_CURRENT_SOURCE_DIR})

     if(DEFINED PACKAGE_FIND_FILE)
         include(${PACKAGE_FIND_FILE})
     endif()

     include_directories(${NATIVERENDER_ROOT_PATH}
                         ${NATIVERENDER_ROOT_PATH}/include)

     add_library(entry SHARED napi_init.cpp)
     target_link_libraries(entry PUBLIC libace_napi.z.so  libhilog_ndk.z.so)
     target_link_libraries(entry PUBLIC ${NATIVERENDER_ROOT_PATH}/../../../libs/arm64-v8a/libnativeSub.so)
     ```

     ```cpp
     #include "sub.h"

     static napi_value Sub(napi_env env, napi_callback_info info)
     {
         size_t requireArgc = 2;
         size_t argc = 2;
         napi_value args[2] = {nullptr};
         napi_get_cb_info(env, info, &argc, args , nullptr, nullptr);
         napi_valuetype valuetype0;
         napi_typeof(env, args[0], &valuetype0);
         napi_valuetype valuetype1;
         napi_typeof(env, args[1], &valuetype1);
         double value0;
         napi_get_value_double(env, args[0], &value0);
         double value1;
         napi_get_value_double(env, args[1], &value1);
         napi_value sum;
         napi_create_double(env, sub(value0, value1), &sum);
         return sum;
     }
     ```
   * Native侧通过dlopen方式集成

     将上步生成的so库置于entry/libs目录下，通过ArkTS侧传递沙箱路径到native侧，然后直接在native侧使用dlopen方式调用。注意：该方式引用的so库源码在编译时必须使用extern "C" {}包裹起来，即函数必须是使用C编译模式编译的。

     ```ts
     import { hilog } from '@kit.PerformanceAnalysisKit';
     import testNapi from 'libentry.so';

     @Entry
     @Component
     struct Index {
       @State message: string = 'Hello World';

       build() {
         Row() {
           Column() {
             Text(this.message)
               .fontSize(50)
               .fontWeight(FontWeight.Bold)
               .onClick(() => {
                 let path = this.getUIContext().getHostContext()!.bundleCodeDir; // Get project path
                 hilog.info(0x0000, 'testTag', 'Test NAPI 2 + 3 = %{public}d', testNapi.subSobyDlOpenSo(2, 3, path + '/libs/arm64/libnativeSub.so')); // Transfer parameter path information to the native side
               })
           }
           .width('100%')
         }
         .height('100%')
       }
     }
     ```

     ```cpp
     #include <dlfcn.h>
     typedef double (*Sub)(double, double);
     static napi_value SubSobyDlOpenSo(napi_env env, napi_callback_info info) {
         size_t requireArgc = 3;
         size_t argc = 3;
         napi_value args[3] = {nullptr};
         napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);
         double value0;
         napi_get_value_double(env, args[0], &value0);    
         double value1;
         napi_get_value_double(env, args[1], &value1);
         char* path = new char[1024];
         size_t size = 1024;
         napi_get_value_string_utf8(env, args[2], path, 255, &size); // Obtain dynamic library path information
         void *handle = dlopen(path, RTLD_LAZY);                     // Open the dynamic link library with path as path
         napi_value result;
         Sub sub_func = (Sub)dlsym(handle, "sub");                   // Get the function named sub
         napi_create_double(env, sub_func(value0, value1), &result);
         dlclose(handle);                                            // Finally, close the dynamic library
         return result;
     }
     ```
