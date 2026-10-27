---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/ndk-development-faq-0007
title: 如何通过AKI三方库实现ArkTS调用C/C++
breadcrumb: FAQ > 应用框架开发 > NDK开发 > NDK开发 > 常见问题 > 如何通过AKI三方库实现ArkTS调用C/C++
category: harmonyos-faqs
scraped_at: 2026-10-28T07:46:56+08:00
doc_updated_at: 2026-10-27
content_hash: sha256:4c4d1b4a8ef3768c8aebe82f3c62f8b6d9b3146928917556b06b69a86c308577
---

**Q：如何通过AKI三方库实现ArkTS调用C/C++？**

**A**：ArkTS与C/C++之间交互，涉及到跨语言调用中数据转换，以及跨线程交互等内容。沿用Node-API标准实现，支持的Node-API接口可参见[Node-API支持的数据类型和接口](../harmonyos-guides/napi-data-types-interfaces.md)。

当前可以通过AKI三方库实现跨语言调用。AKI针对OpenHarmony上提供ArkTS与C/C++跨语言互调的场景提供解决方案，提供了极简语法糖使用方式，一行代码完成ArkTS与C/C++的无障碍跨语言互调，所见即所得。AKI降低了线程安全与GC的使用门槛，但跨线程场景仍需遵循约束。

1. OHPM HAR包依赖：

   在指定路径下（例如：项目根路径/entry），输入以下命令安装ohpm har包依赖。

   ```bash
   cd entry 
   ohpm install @ohos/aki
   ```

   在CMakeLists.txt中添加依赖，假设编译的动态库名为libentry.so。

   ```screen
   # ...

   # 1. Set the AKI root path
   set(AKI_ROOT_PATH ${CMAKE_CURRENT_SOURCE_DIR}/../../../oh_modules/@ohos/aki)
   set(CMAKE_MODULE_PATH ${AKI_ROOT_PATH})
   find_package(Aki REQUIRED)

   # ...

   add_library(entry SHARED napi_init.cpp)
   # 2. To link the binary dependencies & header file, you need to make sure that the target (e.g. entry) is the same as the target in the add_library() method
   target_link_libraries(entry PUBLIC Aki::libjsbind)
   ```

   在右上角同步工程。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/QMbhx9GGQPmR65kCu1x7rg/zh-cn_image_0000002774068822.png "点击放大")
2. 在napi\_init.cpp文件中定义业务，并将业务接口导出给ArkTS：

   ```cpp
   #include <aki/jsbind.h> 
   #include <string>
   // 1、User defined business 
   std::string SayHello(std::string msg){  return msg + " too.";}  

   // 2、Export business interface
   // Step 1: Register the AKI plugin
   JSBIND_ADDON(entry) // Register AKI plugin name: This is the compiled *. so name, following the same rules as Node API

   // Step 2: Register FFI Features
   JSBIND_GLOBAL() 
   { 
     JSBIND_FUNCTION(SayHello); 
   }
   ```

   注册的AKI插件名需与模块级oh-package.json5文件中dependencies标签下的"lib<AKI插件名>"字段名称一致。例如，libentry.so。
3. 在"src/main/cpp/types/libentry/index.d.ts"中导出.so文件的接口：

   ```ts
   export const SayHello: (msg: string) => string;
   ```
4. 在ArkTS文件中调用.so文件中的接口：

   ```screen
   import aki from 'libentry.so' // *. so compiled from the project

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
               console.info(aki.SayHello("hello world")); // 调用.so文件中的代码接口
             })
         }
         .width('100%')
       }
       .height('100%')
     }
   }
   ```

   参考链接：[AKI项目介绍](https://gitcode.com/openharmony-sig/aki)。

   **说明** 

   一个APP中多模块引入aki时必须保持版本一致，否则运行时符号表不一致会导致crash。

**Q：封装C++接口时选择NAPI还是AKI？**

**A**：推荐使用AKI（@ohos/aki）。AKI是基于NAPI封装的极简语法糖三方库，底层仍为NAPI，但通过声明式绑定大幅减少样板代码，一行代码即可完成函数/类绑定，自动处理类型转换、Promise桥接和异步Worker，且支持与现有NAPI代码混用。NAPI与AKI的对比如下：

| 对比维度 | NAPI（Node-API） | AKI（@ohos/aki） |
| --- | --- | --- |
| 定位 | 系统跨语言调用接口 | 基于NAPI封装的极简语法糖三方库 |
| 代码量 | 样板代码多，需手动编写napi\_get\_cb\_info等 | 一行代码完成绑定，大幅减少样板代码 |
| 学习成本 | 较高，需熟悉NAPI全套API | 较低，声明式绑定，开发体验简洁 |
| 类型转换 | 手动处理每种类型的转换 | 自动类型转换（基本类型、string、ArrayBuffer、对象、回调等） |
| 类绑定 | 需手动napi\_define\_class+属性描述符 | JSBIND\_CLASS一行绑定，支持成员函数、成员属性、继承、枚举 |
| Promise支持 | 需手动创建napi\_create\_promise | aki::Promise一键返回Promise |
| 异步/跨线程 | 需手动napi\_create\_async\_work | 内置AsyncWorker+TaskRunner跨线程调度 |
| 线程安全函数 | 需手动napi\_create\_threadsafe\_function | 内置线程安全函数，解决多线程回调竞态 |
| 与NAPI混用 | - | 支持与现有NAPI代码混用 |
| 底层控制力 | 可精细控制每一步 | 适中，底层仍是NAPI，复杂场景可回退NAPI |
| 稳定性 | 系统级接口，长期稳定 | 三方库，需关注版本维护 |
