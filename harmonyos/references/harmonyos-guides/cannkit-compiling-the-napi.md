---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-compiling-the-napi
title: 配置项目NAPI
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > 端侧部署 > App集成 > 配置项目NAPI
category: harmonyos-guides
scraped_at: 2026-04-28T07:51:23+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:3ebcfb8a8f4a18b369761403108696aff0af836f7711bbb54b1eece54284db36
---

编译HAP时，NAPI层的so需要编译依赖NDK中的libneural\_network\_core.so和libhiai\_foundation.so。

## 头文件引用

按需引用[NNCore](../harmonyos-references/capi-neuralnetworkruntime.md)和[CANN Kit](../harmonyos-references/cannkit-hiai-aipp-param-8h.md)的头文件。

```
1. #include "neural_network_runtime/neural_network_core.h"
2. #include "CANNKit/hiai_options.h"
```

## 编写CMakeLists.txt

CMakeLists.txt示例代码如下。

```
1. # the minimum version of CMake.
2. cmake_minimum_required(VERSION 3.4.1)
3. project(CANNDemo)

5. set(NATIVERENDER_ROOT_PATH ${CMAKE_CURRENT_SOURCE_DIR})

7. include_directories(${NATIVERENDER_ROOT_PATH}
8. ${NATIVERENDER_ROOT_PATH}/include)

10. include_directories(${HMOS_SDK_NATIVE}/sysroot/usr/lib)
11. FIND_LIBRARY(cann-lib hiai_foundation)

13. add_library(entry SHARED Classification.cpp HIAIModelManager.cpp)

15. target_link_libraries(entry PUBLIC libace_napi.z.so
16. libhilog_ndk.z.so
17. librawfile.z.so
18. ${cann-lib}
19. libneural_network_core.so
20. )
```
