---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-33
title: 如何通过AKI三方库实现ArkTS与C/C++之间的跨语言调用
breadcrumb: FAQ > 应用框架开发 > NDK开发 > NDK开发 > 如何通过AKI三方库实现ArkTS与C/C++之间的跨语言调用
category: harmonyos-faqs
scraped_at: 2026-04-29T14:15:51+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:61dc1c065678ba1414db3068a3c97d3dfc5810ba1a953dc6dfde115185716954
---

ArkTS与C/C++之间交互，涉及到跨语言调用中数据转换，以及跨线程交互等内容。沿用Node-API标准实现，支持的Node-API接口可参见[Node-API支持的数据类型和接口](../harmonyos-guides/napi-data-types-interfaces.md)。

当前可以通过AKI三方库实现跨语言调用。AKI针对OpenHarmony上提供ArkTS与C/C++跨语言互调的场景提供解决方案，提供了极简语法糖使用方式，一行代码完成ArkTS与C/C++的无障碍跨语言互调，所见即所得。同时开发者无需关心Node-API的线程安全问题、Native对象GC问题，为开发者屏蔽Node-API内部复杂逻辑。

1. OHPM HAR包依赖：

   在指定路径下（例如：项目根路径/entry），输入以下命令安装ohpm har包依赖。

   ```
   1. cd entry
   2. ohpm install @ohos/aki
   ```

   在CMakeLists.txt中添加依赖，假设编译的动态库名为libhello.so。

   ```
   1. # ...

   3. # 1. Set the AKI root path
   4. set(AKI_ROOT_PATH ${CMAKE_CURRENT_SOURCE_DIR}/../../../oh_modules/@ohos/aki)
   5. set(CMAKE_MODULE_PATH ${AKI_ROOT_PATH})
   6. find_package(Aki REQUIRED)

   8. # ...

   10. add_library(entry SHARED napi_init.cpp)
   11. # 2. To link the binary dependencies & header file, you need to make sure that the target (e.g. entry) is the same as the target in the add_library() method
   12. target_link_libraries(entry PUBLIC Aki::libjsbind)
   ```

   [CMakeLists.txt](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/Ndk/ndk1/nativeAki/src/main/cpp/CMakeLists.txt#L3-L27)

   在右上角同步工程。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/IK8JOxziQn6iH747Tv2aRg/zh-cn_image_0000002229604253.png?HW-CC-KV=V1&HW-CC-Date=20260429T061550Z&HW-CC-Expire=86400&HW-CC-Sign=F5631516E48BC9D95D40A7E8278D968AE04D0586BA5771C4AB9F63A4124DF69A)
2. 在napi\_init.cpp文件中定义业务，并将业务接口导出给 ArkTS。

   ```
   1. #include <aki/jsbind.h>
   2. #include <string>
   3. // 1、User defined business
   4. std::string SayHello(std::string msg){  return msg + " too.";}

   6. // 2、Export business interface
   7. // Step 1: Register the AKI plugin
   8. JSBIND_ADDON(entry) // Register AKI plugin name: This is the compiled *. so name, following the same rules as Node API

   10. // Step 2: Register FFI Features
   11. JSBIND_GLOBAL()
   12. {
   13. JSBIND_FUNCTION(SayHello);
   14. }
   ```

   [napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/Ndk/ndk1/nativeAki/src/main/cpp/napi_init.cpp#L5-L18)

注册的AKI插件名需与模块级 oh-package.json5 文件中 dependencies 标签下的 “lib<AKI插件名>” 字段名称一致。例如，libentry.so。

1. 在“src/main/cpp/types/libentry/index.d.ts”中导出 .so 文件的接口。

   export const SayHello: (msg: string) => string;
2. 在ArkTS文件中调用.so文件中的接口。

   ```
   1. import aki from 'libentry.so' // *. so compiled from the project

   3. @Entry
   4. @Component
   5. struct Index {
   6. @State message: string = 'Hello World';

   8. build() {
   9. Row() {
   10. Column() {
   11. Text(this.message)
   12. .fontSize(50)
   13. .fontWeight(FontWeight.Bold)
   14. .onClick(() => {
   15. console.info(aki.SayHello("hello world")); // 调用.so文件中的代码接口
   16. })
   17. }
   18. .width('100%')
   19. }
   20. .height('100%')
   21. }
   22. }
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/Ndk/ndk1/nativeAki/src/main/ets/pages/Index.ets#L5-L26)

**参考链接**

[AKI 项目介绍](https://gitcode.com/openharmony-sig/aki)
