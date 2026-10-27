---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/ndk-development-faq-0003
title: Native侧SO库集成与加载方法常见问题
breadcrumb: FAQ > 应用框架开发 > NDK开发 > NDK开发 > 常见问题 > Native侧SO库集成与加载方法常见问题
category: harmonyos-faqs
scraped_at: 2026-10-28T07:46:55+08:00
doc_updated_at: 2026-10-27
content_hash: sha256:490286d9832b43d25c1bbdf2d16f8edf65402478f85de6c3f2e8e54abcd00a0f
---

**Q：Native工程中如何使用其他三方so库？**

**A**：

1. 将编译好的so库放到Native工程的entry/libs/arm64-v8a/目录下，并将so库对应的头文件放到entry/src/main/cpp目录层级下（可以在cpp目录下增加一个文件夹专门存放三方so库的头文件）。
2. 在CMakeLists.txt文件中链接so库。
3. 在Native侧 .cpp文件中引入头文件使用so库的相关能力。

示例如下：

在Native侧集成三方库Curl：

1. 将移植后的Curl的so库放到Native工程的entry/libs/目录下，并将移植后生成的、包含头文件的include目录放到entry/src/main/cpp目录下。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/KQmX_0AHSG-XK8XKupsJiA/zh-cn_image_0000002802039455.png)
2. 在CMakeLists.txt文件中链接Curl对应的so库。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/0cuQsMxITYyLqmm_TVIFtA/zh-cn_image_0000002772839700.png "点击放大")
3. 在Native侧.cpp文件中通过引入头文件curl.h来使用Curl的相关能力。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/SJbBX-TSRK6JyRtjNBA-Sw/zh-cn_image_0000002772679724.png)

参考链接：[在NDK工程中使用预构建库](../harmonyos-guides/build-with-ndk-prebuilts.md)。

**Q：ArkTS侧与Native侧分别如何动态加载SO库？**

**A**：解决措施：

1. ArkTS 可以通过动态 import 加载 so 库。
2. Native侧可以使用dlopen动态加载so库。参考代码如下：
3. ArkTS 通过动态 import 加载 so 库。添加异步函数，在异步函数中通过let testNapi = await import ("libentry.so")实现动态加载so库。

   ```ts
   import { hilog } from '@kit.PerformanceAnalysisKit';
   // import testNapi from 'libentry.so';

   @Entry
   @Component
   struct LoadSoLibrary {
     @State message: string = 'Hello World';

     build() {
       Row() {
         Column() {
           Text(this.message)
             .fontSize(50)
             .fontWeight(FontWeight.Bold)
             .onClick(async() => {
               let testNapi = await import("libentry.so")            // Load so library
               hilog.info(0x0000, 'testTag', 'Test NAPI 2 + 3 = %{public}d', testNapi.default.add(2, 3));   // Call library functions by default
               // hilog.info(0x0000, 'testTag', 'Test NAPI 2 + 3 = %{public}d', testNapi.add(2, 3));
             })
         }
         .width('100%')
       }
       .height('100%')
     }
   }
   ```
4. Native侧使用dlopen动态加载so库。需要调用liba.so中的add函数。
   * 将liba.so文件放到libs/arm64-v8a/路径下。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/tqH1WgbeQNenA3Peeps6GA/zh-cn_image_0000002802119551.png)
   * 需要在ArkTS侧传递so库路径信息到Native侧。

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
                 let path = this.getUIContext().getHostContext()!.bundleCodeDir;     // Get project path
                 hilog.info(0x0000, 'testTag', 'Test NAPI 2 + 3 = %{public}d', testNapi.addByLibPath(2, 3, path + '/libs/arm64/liba.so'));   // Transfer parameter path information to the native side
               })
           }
           .width('100%')
         }
         .height('100%')
       }
     }
     ```
   * 在Native侧通过dlopen函数动态加载so库。

     ```c
     #include "napi/native_api.h" 
     #include <dlfcn.h> 
     typedef double (*FUNC_ADD)(int, int); 
     static napi_value AddByLibPath(napi_env env, napi_callback_info info) { 
         size_t requireArgc = 3; 
         size_t argc = 3; 
         napi_value args[3] = {nullptr}; 
         napi_get_cb_info(env, info, &argc, args, nullptr, nullptr); 
         double value0; 
         napi_get_value_double(env, args[0], &value0); 
         double value1; 
         napi_get_value_double(env, args[1], &value1); 
         char path[255]; 
         size_t size = 255; 
         napi_get_value_string_utf8(env, args[2], path, 255, &size); // Obtain dynamic library path information 
         void *handle = dlopen(path, RTLD_LAZY);                     // Open a dynamic link library, The path is "path".  
         dlerror(); 
         FUNC_ADD add_func = (FUNC_ADD)dlsym(handle, "add"); // Retrieve the function named "add" 
         if (dlerror()) { 
             return nullptr; 
         } 
         double res = add_func(value0, value1);              // Call add and pass the parameter information 
         dlclose(handle);                                    // Close the dynamic library 
         napi_value sum; 
         napi_create_double(env, res, &sum); 
         return sum; 
     } 
     // ...
     ```

**Q：如何在ArkTS侧引用其他三方so库？**

**A**：解决措施：在ArkTS中引用三方库so需要具备以下三个文件：xxx.so、Index.d.ts和oh-package.json5。其中，Index.d.ts和oh-package.json5在C++模板中自带，也可以手动创建。在需要调用的模块根目录下的oh-package.json5中声明so库的根目录路径。然后在代码中使用import语句引用oh-package.json5中声明的依赖名称。此方案仅适用于已经适配了Native的so库。因此，在编译生成so库时，需要实现功能函数并注册其Native侧接口，同时提供对应的Native侧接口声明文件Index.d.ts和配置文件oh-package.json5。

1. 将so文件移动到libs文件夹下对应架构的目录。如果在纯ArkTS工程中，还需将编译三方库时生成的libc++\\_xxx.so移动到该目录。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/35w98m8TRzWT3B3nxCoB_w/zh-cn_image_0000002802039461.png)
2. 在src/main/cpp/types目录下创建新目录，并将Index.d.ts和oh-package.json5文件移动到该目录下。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/Vz-9BGmoT0KwoFs-SVAkkQ/zh-cn_image_0000002772839704.png)
3. 在模块级的oh-package.json5文件中声明该 so 库的根目录路径。

   ```json
   "dependencies": {
     "libimportthirdpartylibraries.so": "file:./src/main/cpp/types/libimportthirdpartylibraries",
     "libapplication.so": "file:./src/main/cpp/types/libapplication"
   },
   ```
4. 在代码中引用并调用oh-package.json5中声明的依赖。

   ```ts
   import testNapi from 'libimportthirdpartylibraries.so';
   import myNapi from 'libapplication.so';

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
               console.info(`MyTest NAPI 2 + 3 = ${myNapi.add(2, 3)}`);
               console.info(`MyTest NAPI 2 - 3 = ${testNapi.sub(2, 3)}`);
             })
         }
         .width('100%')
       }
       .height('100%')
     }
   }
   ```

运行结果：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/LqaqFmbmSuWh7632XlBW0w/zh-cn_image_0000002772679730.png)

参考链接：[在ArkTS侧引用三方so库](../harmonyos-guides/integrate-third-party-dlls.md#在arkts侧引用三方so库)。

**Q：在Native侧如何集成三方SO库？**

**A**：开发过程可分为两个部分：

1. 系统编译生成so库。

   有关如何编译so库，请参考以下链接：[使用命令行CMake构建NDK工程](../harmonyos-guides/build-with-ndk-cmake.md)。
2. 系统集成SO库：
   * 方式一：直接集成。
   * 方式二：通过dlopen集成。

   参考代码如下：

1. 系统编译SO库：

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

   ```cmake
   # CMakeLists.txt
   cmake_minimum_required(VERSION 3.4.1)
   project(libSub)
   # Compile source code 
   add_library(nativeSub SHARED sub.cpp)
   ```
2. 系统集成SO库：
   * Native侧直接集成。

     将上步生成的so库置于entry/libs对应架构的目录下，将头文件放置到cpp目录下。修改CMakeLists.txt，将so库加入工程编译引用。在native侧引入头文件使用。

     ```cmake
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
   * Native侧通过dlopen方式集成。

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
