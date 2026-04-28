---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-60
title: 在CMakeLists文件中如何获取模块版本信息
breadcrumb: FAQ > 应用框架开发 > NDK开发 > NDK开发 > 在CMakeLists文件中如何获取模块版本信息
category: harmonyos-faqs
scraped_at: 2026-04-28T08:24:40+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:b5d09680033246b3610c007002cc7fb02c3784293e70b4d3a00823d8fb333d7e
---

**问题现象**

有一个har模块，在 oh-package.json5 中配置了版本 1.0.0。模块内部有C++代码，其中某一个文件会根据版本变化，因此不同版本参与编译的都是不同的文件。通过CMAKE\_VERSION变量可以获取CMake的版本信息，但获取不到har的版本信息，如何在CMakeLists中获取当前har模块oh-package.json5中的version版本号，以匹配不同的cpp文件。

**解决措施**

可以尝试通过转JSON字符串与版本号比较的方式解决。

```
1. cmake_minimum_required(VERSION 3.4.1)
2. project(CmakeModuleInfo)

4. set(JSON_FILE_PATH ${CMAKE_CURRENT_SOURCE_DIR}/../../../oh-package.json5)
5. file(READ ${JSON_FILE_PATH} JSON_STRING)
6. message("json string:${JSON_STRING}")
7. if("${JSON_STRING}" MATCHES "1.0.0")
8. set(SRC_LIST napi_init.cpp)
9. else()
10. set(SRC_LIST hello.cpp)
11. endif()
12. message("src_file:${SRC_LIST}")

14. set(NATIVERENDER_ROOT_PATH ${CMAKE_CURRENT_SOURCE_DIR})
15. include_directories(${NATIVERENDER_ROOT_PATH}
16. ${NATIVERENDER_ROOT_PATH}/include)

18. add_library(entry SHARED ${SRC_LIST})
19. target_link_libraries(entry PUBLIC libace_napi.z.so)
```

[CMakeLists.txt](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/Ndk/Ndk2/CMakeGetModuleVersion/src/main/cpp/CMakeLists.txt#L4-L22)
