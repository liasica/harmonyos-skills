---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-60
title: 在CMakeLists文件中如何获取模块版本信息
breadcrumb: FAQ > 应用框架开发 > NDK开发 > NDK开发 > 在CMakeLists文件中如何获取模块版本信息
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:57+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:ae4c750c20bc4b516a8142399f50b81e06e0c8b44ef836f3146b24c614baa285
---

**问题现象**

有一个har模块，在 oh-package.json5 中配置了版本 1.0.0。模块内部有C++代码，其中某一个文件会根据版本变化，因此不同版本参与编译的都是不同的文件。通过CMAKE\_VERSION变量可以获取CMake的版本信息，但获取不到har的版本信息，如何在CMakeLists中获取当前har模块oh-package.json5中的version版本号，以匹配不同的cpp文件。

**解决措施**

可以尝试通过转JSON字符串与版本号比较的方式解决。

```text
cmake_minimum_required(VERSION 3.4.1)
project(CmakeModuleInfo)

set(JSON_FILE_PATH ${CMAKE_CURRENT_SOURCE_DIR}/../../../oh-package.json5)
file(READ ${JSON_FILE_PATH} JSON_STRING)
message("json string:${JSON_STRING}")
if("${JSON_STRING}" MATCHES "1.0.0")
set(SRC_LIST napi_init.cpp)
else()
set(SRC_LIST hello.cpp)
endif()
message("src_file:${SRC_LIST}")

set(NATIVERENDER_ROOT_PATH ${CMAKE_CURRENT_SOURCE_DIR})
include_directories(${NATIVERENDER_ROOT_PATH}
                    ${NATIVERENDER_ROOT_PATH}/include)

add_library(entry SHARED ${SRC_LIST})
target_link_libraries(entry PUBLIC libace_napi.z.so)
```
