---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-72
title: 如何在一个模块中使用另一个模块中编译出来的so
breadcrumb: FAQ > 应用框架开发 > NDK开发 > NDK开发 > 如何在一个模块中使用另一个模块中编译出来的so
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:57+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:9d257baee02cee05c252be7e136c1131650fab79cfade9167a0d6fcc1199f44e
---

**问题场景**

在a module的Native侧集成b module编译出来的so，可以按照以下步骤操作：

1. 确保b module中的so文件已经成功编译，并且路径正确。

2. 在a module的`CMakeLists.txt`，添加对b module中so文件的引用。

例如，在CMakeLists.txt中添加如下内容：

```text
cmake
add_library(b SHARED IMPORTED)
set_target_properties(b PROPERTIES IMPORTED_LOCATION ${CMAKE_SOURCE_DIR}/path/to/b/libb.so)
target_link_libraries(a b)
```

3. 确保a module的构建脚本能够正确找到并链接b module的so文件。

通过以上步骤，a module就可以在Native侧成功集成b module编译出来的so文件。

**解决措施**

1. 纯CPP部分使用NDK编译成.so或.a文件，并放置在HAR或HSP中。
2. 依赖上述的HAR或HSP后，使用已链接的头文件方式，在链接时直接写库文件名即可。这样，纯C++的SO库实现了多模块共享。需要通过NAPI使用的模块，只需单独编写NAPI代码。NAPI封装后的功能也可以通过模块依赖的方式被其他模块使用。

**操作步骤**

1. 在HAR/HSP模块的build-profile.json5中，指定buildOption/nativeLib/headerPath为接口文件目录。

   ```json
   buildOption: { nativeLib: { headerPath: "src/main/cpp/include" } }
   ```
2. 调用方依赖HAR或HSP包。

   ```screen
   // oh-package.json dependencies: { curl: "1.0.0" }
   ```
3. 调用方配置CMake链接SO，格式为 packageName::soName。

   ```screen
   target_link_libraries(entry PUBLIC curl::curl)
   ```
