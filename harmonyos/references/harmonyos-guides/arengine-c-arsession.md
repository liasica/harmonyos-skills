---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arengine-c-arsession
title: 管理AR会话（C/C++）
breadcrumb: 指南 > 图形 > AR Engine（AR引擎服务） > 管理AR会话 > 管理AR会话（C/C++）
category: harmonyos-guides
scraped_at: 2026-04-28T07:46:48+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:14f204fc3adc6900610488629783ed623393b2ef60cced45a1180d29ea37378c
---

本章节给出了关键开发步骤，完整代码可以参考[示例代码](https://gitcode.com/harmonyos_samples/arengine_-sample-code_-clientdemo_cpp)。

## 约束与限制

管理AR会话支持部分Phone、部分Tablet设备。并且从6.1.0(23)版本开始，新增支持TV设备。请参考[硬件要求](arengine-preparations.md#硬件要求)判断设备是否支持。

## 引入AR Engine

1. 引入头文件。

   ```
   1. #include "ar/ar_engine_core.h"
   ```
2. 编写CMakeLists.txt。

   ```
   1. find_library(
   2. # Sets the name of the path variable.
   3. arengine-lib
   4. # Specifies the name of the NDK library that
   5. # you want CMake to locate.
   6. libarengine_ndk.z.so
   7. )

   9. target_link_libraries(entry PUBLIC
   10. ${arengine-lib}
   11. )
   ```

## 创建AR会话

应用开始时，调用[HMS\_AREngine\_ARSession\_Create](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arsession_create)函数创建一个AR会话。

```
1. AREngine_ARSession *arSession = nullptr;
2. HMS_AREngine_ARSession_Create(nullptr, nullptr, &arSession);
```

## 自定义配置AR会话

创建一个[AREngine\_ARConfig](../harmonyos-references/arengine-capi-arengine.md#arengine_arconfig)对象来配置当前AR会话。如缺省，则使用默认配置，具体配置可参考[HMS\_AREngine\_ARConfig\_Create](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arconfig_create)。

```
1. // 创建一个拥有合理默认配置的配置对象。
2. AREngine_ARConfig *arConfig = nullptr;
3. HMS_AREngine_ARConfig_Create(arSession, &arConfig);

5. // 此处配置arConfig。

7. // 配置AREngine_ARSession会话。
8. HMS_AREngine_ARSession_Configure(arSession, arConfig);

10. // 释放指定的配置对象的内存空间。
11. HMS_AREngine_ARConfig_Destroy(arConfig);
```

具体可配置项，请参考[AR Engine API参考](../harmonyos-references/arengine-capi-arengine.md)。

## 销毁AR会话

应用结束时，调用[HMS\_AREngine\_ARSession\_Destroy](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arsession_destroy)函数销毁当前的AR会话。

```
1. HMS_AREngine_ARSession_Destroy(arSession);
```
