---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-compiling-the-napi
title: 配置项目NAPI
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > 端侧部署 > App集成 > 配置项目NAPI
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:34+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:f16a9e6ef272faa072acd1ed5b1b86d2f2814bc1c822c4d4805a402897bbcdf7
---

编译HAP时，NAPI层的so需要编译依赖NDK中的libneural\_network\_core.so和libhiai\_foundation.so。

## 头文件引用

按需引用[NNCore](../harmonyos-references/capi-neuralnetworkruntime.md)和[CANN Kit](../harmonyos-references/cannkit-hiai-aipp-param-8h.md)的头文件。

```cpp
#include "neural_network_runtime/neural_network_core.h"
#include "CANNKit/hiai_options.h"
```

## 编写CMakeLists.txt

CMakeLists.txt示例代码如下。

```make
# the minimum version of CMake.
cmake_minimum_required(VERSION 3.4.1)
project(CANNDemo)

set(NATIVERENDER_ROOT_PATH ${CMAKE_CURRENT_SOURCE_DIR})

include_directories(${NATIVERENDER_ROOT_PATH}
                    ${NATIVERENDER_ROOT_PATH}/include)

include_directories(${HMOS_SDK_NATIVE}/sysroot/usr/lib)
FIND_LIBRARY(cann-lib hiai_foundation)

add_library(entry SHARED Classification.cpp HIAIModelManager.cpp)

target_link_libraries(entry PUBLIC libace_napi.z.so
    libhilog_ndk.z.so
    librawfile.z.so
    ${cann-lib}
    libneural_network_core.so
    )
```
