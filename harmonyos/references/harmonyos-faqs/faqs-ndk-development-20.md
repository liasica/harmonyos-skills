---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-development-20
title: 在HarmonyOS工程中如何引用外部构建的so库
breadcrumb: FAQ > 应用框架开发 > NDK开发 > NDK开发 > 在HarmonyOS工程中如何引用外部构建的so库
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:57+08:00
doc_updated_at: 2026-08-13
content_hash: sha256:a8108ac3c56b0f76a29b828125b1bfcb1848f15a9772d1f70ad119f8a3778cad
---

## 问题现象

在工程中如何引用已经适配HarmonyOS的so库？

## 背景知识

参考官网[ArkTS侧引用三方so库](../harmonyos-guides/integrate-third-party-dlls.md#在arkts侧引用三方so库)的文档，通过配置模块动态依赖即可在工程中引用已经适配HarmonyOS的so库。

## 解决方案

* **非Native工程引用已经适配HarmonyOS的so库：**
  + 实现原理：
    - 将so库和对应的Native侧接口文件加入到工程中，在工程中配置so库对应的模块动态依赖，在ArkTS侧通过import引入依赖接口调用so库。
    - 但是需要注意该方案只能引用适配HarmonyOS的so库，因此在编译生成so库时需要实现功能函数并向Napi注册其Native侧接口，提供对应的Native侧接口文件index.d.ts和配置文件oh-package.json5。
  + 开发步骤：
    1. 将已经适配HarmonyOS的so库文件（假设so库为libxxx.so），置于entry/libs对应的架构目录下。
    2. 将libxxx.so的接口文件（index.d.ts）所在的文件夹拷贝到src/main/cpp/types下。
    3. 在模块级oh-package.json5中声明so库根目录路径。

       ```json
       {
         "name": "library",
         "version": "1.0.0",
         "description": "Please describe the basic information.",
         "main": "Index.ets",
         "author": "",
         "license": "Apache-2.0",
         "dependencies": {
           "libentry.so": "file:./src/main/cpp/types/libentry"
         }
       }
       ```
    4. 在ArkTS侧使用import引用oh-package.json5中声明的依赖并进行结果验证。

       ```ts
       import testNapi from 'libentry.so';

       function test() {
         console.info('纯ArkTS引用so库结果为：', testNapi.add(2, 3));
       }
       ```
    5. 工程关键部分结构。

       ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/9lVosYoCQQCALxOeqoTu6Q/zh-cn_image_0000002659138349.png)
  + 注意事项：

    在引用过程中除了将已经适配HarmonyOS的libxxx.so库文件置于entry/libs对应的架构目录下外，还需要将编译三方so库时配套产生的libc++\_shared.so库文件置于该目录下。

* **Native工程引用已经适配HarmonyOS的so库：**
  + 开发步骤。
    1. 将三方库生成的so文件拷贝到应用工程目录。

       为便于管理三方库，在应用工程的cpp目录新建一个thirdparty目录，将生成的so文件以及头文件拷贝到该目录下。

       如果该三方库二进制文件为so文件，还需要将so文件拷贝到工程目录的entry/libs/${OHOS\_ARCH}/目录下。
    2. 配置对应链接。

       配置链接只需要在cpp目录的CMakeLists.txt文件中添加对应target\_link\_libraries即可，动态库和静态库只需要填写一个：

       ```cmake
       # 配置动态库，静态库配置方式一样，将.so文件改成.a文件即可
       target_link_libraries(entry PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}/thirdparty/mytest/${OHOS_ARCH}/lib/libmytest.so)
       ```
    3. 配置头文件路径。

       配置链接只需要在cpp目录的CMakeLists.txt文件中添加对应target\_include\_directories：

       ```cmake
       target_include_directories(entry PRIVATE ${CMAKE_CURRENT_SOURCE_DIR}/thirdparty/mytest/${OHOS_ARCH}/include)
       ```
    4. 工程关键部分结构。

       假设xxx代表的是三方库名称，xxx文件夹下包含了arm64架构生成的二进制文件，架构目录下包含了该库的头文件(include)以及二进制文件(lib)。

       ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6a/v3/D7zxBHjSQEWOVvckNurIIA/zh-cn_image_0000002629058998.png "点击放大")
  + 注意事项。
    1. 应用在引用动态库的时候是通过soname来查找的，所以我们需要将名字为soname的库文件拷贝到entry/libs/${OHOS\_ARCH}/目录下。

       soname查看方法：llvm-readelf -d libxxx.so。
    2. 要正确的拷贝so文件。

       正确拷贝so文件后so文件大小应该与原库实体文件大小一致，so文件大小也可以通过llvm-readelf -d libxxx.so查询。

## 常见FAQ

Q：har包依赖so库时编译报错：

```txt
Only the following .so dependencies are allowed: external .so files located in libs/arm64-v8a or libs/x86_64 and internal .so files listed in CMakeLists.txt.
```

A：CMakeLists.txt中声明的so库名称与引用的so库名称不一致导致，需要检查CMakeLists.txt声明的so库名称。

Q：将已有的几个so库编译合并成一个so库时发生报错：

```txt
ERROR: Duplicated files found in module editsdk. This may cause unexpected errors at runtime. 
- D:\friendDemo\cantfindso\ohosApp\depend\editsdk\build\default\intermediates\cmake\default\obj\arm64-v8a\libeditsdk.so
- D:\friendDemo\cantfindso\ohosApp\depend\editsdk\libs\arm64-v8a\libeditsdk.so

* Try the following:
> Set .so file priorities with pickFirsts, pickLasts, or select option.
> Make sure each .so file name is unique.
> More info: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs-V5/faqs-compiling-and-building-109-V5

> hvigor ERROR: Failed :editsdk:default@ProcessLibs... 
> hvigor ERROR: BUILD FAILED in 3 s 795 ms
```

A：根据编译报错，结合CMakeLists.txt代码可知，目标生成的so库和已有so库重名导致编译错误。将目标so库的名字改成和已有so库不同的即可解决。

Q：工程中两个so内有同名同入参的函数，是否会导致调用关系错乱？

A：工程中两个so内有同名同入参的函数确实可能会导致调用关系错乱，建议添加命名空间区分来自不同库的内容，或者使用dlopen来加载指定的so，参考：[多so相互依赖场景下如何解耦](faqs-ndk-71.md)。

Q：使用dlopen动态加载自定义沙箱路径下的so失败是什么原因？

A：为保障用户隐私安全，dlopen具有命名空间隔离能力，应用可以加载的动态库受到命名空间的限制。一般应用只能够加载应用安装包目录/data/storage/el1/bundle下的动态库，以及系统内置对外开放的动态库。

若加载自定义路径动态库会报错：MUSL-LDSO bundlename E Open absolute\_path library: check ns accessible failed, pathname libxxx.so namespace moduleNs\_default。

参考：[通过调用dlopen的方式引用](../harmonyos-guides/integrate-third-party-dlls.md#通过调用dlopen的方式引用)。
