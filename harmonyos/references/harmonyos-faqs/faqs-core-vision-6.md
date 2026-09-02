---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-core-vision-6
title: 如何判断skeletonDetection（骨骼点检测）能否使用设备的NPU运行
breadcrumb: FAQ > AI功能开发 > 机器学习 > 基础视觉（Core Vision） > 如何判断skeletonDetection（骨骼点检测）能否使用设备的NPU运行
category: harmonyos-faqs
scraped_at: 2026-09-02T14:55:00+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:9770b3e07e4eddcf30e4ca45a5b5d4bce292157bb6d822fce5b7247986f4fb00
---

## 问题现象

某些设备没有NPU导致骨骼点检测运行较慢。如何提前判断骨骼点检测能否使用设备的NPU运行？

## 背景知识

* [骨骼点检测](../harmonyos-guides/core-vision-skeleton-detection.md)：人体骨骼关键点检测，主要检测人体的一些关键点，通过关键点描述人体骨骼信息。具体应用主要集中在智能视频监控，病人监护系统，人机交互，虚拟现实，人体动画，智能家居，智能安防，运动员辅助训练等等。
* [CANN Kit简介](../harmonyos-guides/cannkit-introduction.md)：CANN（Compute Architecture for Neural Networks）是华为面向AI推出的端云一致的异构计算架构。CANN Kit通过协同调度设备的NPU（神经网络处理单元）、CPU等硬件资源，实现高效的设备端智能计算性能优化。

## 解决方案

* 当设备没有NPU时，骨骼点检测会使用CPU进行推理，导致时间较长。CPU推理导致时间延长属于正常现象。
* 若希望提前判断[skeletonDetection（骨骼点检测）](../harmonyos-references/core-vision-skeleton-detection-api.md)API能否使用设备的NPU运行，进而再根据结果做下一步处理，可以使用CANN Kit的[HMS\_HiAI\_GetVersion()](../harmonyos-references/cannkit.md#hms_hiai_getversion)方法进行判断：

  通过返回模板hiaiversion A1A2A3.X1X2X3.Y1Y2Y3.Z1Z2Z3指定X1是否为0来区分是否支持NPU。若X1为0，则表示不支持NPU；若X1为非0，则表示支持NPU。

步骤如下：

1. [创建项目](../harmonyos-guides/cannkit-creating-a-project.md)。
2. [配置项目NAPI](../harmonyos-guides/cannkit-compiling-the-napi.md)：
   * 引入CANNKit/hiai\_helper.h头文件，实现判断设备NPU的方法IsNpuDevice。工程目录“\entry\src\main\cpp\napi\_init.cpp”文件示例参考如下：

     ```cpp
     /*
      * Copyright (c) Huawei Technologies Co., Ltd. 2026. All rights reserved.
      */

     #include "napi/native_api.h"
     #include <hilog/log.h>
     #include <cstring>
     #include "CANNKit/hiai_helper.h"

     static napi_value IsNpuDevice(napi_env env, napi_callback_info info)
     {
         const char *hiaiVersion = HMS_HiAI_GetVersion();
         napi_value result;
         napi_get_boolean(env, true, &result);
         if (hiaiVersion == nullptr || strlen(hiaiVersion) != 15) { /* 15: hiaiVersion返回的字符串长度 */
             OH_LOG_ERROR(LOG_APP, "HiAI version is null or not supported");
             napi_get_boolean(env, false, &result);
         } else if (hiaiVersion[4] == '0') { /* 返回的hiaiVersion字符串A1A2A3.X1X2X3.Y1Y2Y3.Z1Z2Z3中X1为0表示不支持NPU */
             OH_LOG_INFO(LOG_APP, "NPU is not supported");
             napi_get_boolean(env, false, &result);
         }
         return result;
     }

     EXTERN_C_START
     static napi_value Init(napi_env env, napi_value exports)
     {
         napi_property_descriptor desc[] = {
             {"isNpuDevice", nullptr, IsNpuDevice, nullptr, nullptr, nullptr, napi_default, nullptr}};
         napi_define_properties(env, exports, sizeof(desc) / sizeof(desc[0]), desc);
         return exports;
     }
     EXTERN_C_END

     static napi_module demoModule = {
         .nm_version = 1,
         .nm_flags = 0,
         .nm_filename = nullptr,
         .nm_register_func = Init,
         .nm_modname = "entry",
         .nm_priv = ((void *)0),
         .reserved = {0},
     };

     extern "C" __attribute__((constructor)) void RegisterEntryModule(void) { napi_module_register(&demoModule); }
     ```
   * 编写CMakeLists.txt。工程目录“\entry\src\main\cpp\CMakeLists.txt”文件示例参考如下：

     ```txt
     # the minimum version of CMake.
     cmake_minimum_required(VERSION 3.5.0)
     project(SkeletonDetectionNpuDemo)

     set(NATIVERENDER_ROOT_PATH ${CMAKE_CURRENT_SOURCE_DIR})

     include_directories(${NATIVERENDER_ROOT_PATH}
                         ${NATIVERENDER_ROOT_PATH}/include)

     include_directories(${HMOS_SDK_NATIVE}/sysroot/usr/lib)
     FIND_LIBRARY(cann_lib hiai_foundation)

     add_library(entry SHARED napi_init.cpp)

     target_link_libraries(entry PUBLIC libace_napi.z.so
         libhilog_ndk.z.so
         librawfile.z.so
         ${cann_lib}
         )
     ```
   * 导出cpp接口。工程目录“\entry\src\main\cpp\types\libentry\Index.d.ts”文件示例参考如下：

     ```ts
     export const isNpuDevice : () => boolean;
     ```
3. 在ArkTS中调用判断是否支持NPU的接口。

   工程目录“\entry\src\main\ets\pages\Index.ets”文件示例参考如下：

   ```ts
   import { hilog } from '@kit.PerformanceAnalysisKit';
   import testNapi from 'libentry.so';

   const DOMAIN = 0x0000;

   @Entry
   @Component
   struct Index {
     @State text: string = '请检查';
     private isNpuDevice: boolean = false;

     build() {
       Row() {
         Column() {
           Button('请点击检查是否支持NPU')
             .onClick(() => {
               this.isNpuDevice = testNapi.isNpuDevice(); // 调用接口检查是否支持NPU
               hilog.info(DOMAIN, 'testTag', 'If support NPU: %{public}s', this.isNpuDevice);
               this.text = this.isNpuDevice ? '支持' : '不支持';
             })
             .margin(20)
           Text(this.text)
         }
         .width('100%')
       }
       .height('100%')
     }
   }
   ```
