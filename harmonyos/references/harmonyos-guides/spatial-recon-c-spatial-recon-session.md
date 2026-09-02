---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/spatial-recon-c-spatial-recon-session
title: 管理Spatial Recon会话
breadcrumb: 指南 > 图形 > Spatial Recon Kit（空间建模服务） > 管理Spatial Recon会话
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:22+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:1ca2929224d5395f38d995543c1752f92ec3279a7a29219b28d8d595242a55af
---

## 概要

从6.1.0(23)开始，对于任何需要使用空间重建能力的应用，都需要创建一个会话[HMS\_SpatialRecon\_Session](../harmonyos-references/capi-spatialrecon-hms-spatialrecon-session.md)，用于管理SpatialRecon Kit的系统状态。该会话需要应用开发者使用本Kit提供的API创建，并在相关任务结束后使用本Kit提供的API手动销毁。

由于空间重建能力会消耗大量系统资源，并非所有设备都支持重建。推荐先通过[HMS\_SpatialRecon\_IsSupport](../harmonyos-references/capi-spatial-recon-interface-h.md#hms_spatialrecon_issupport)接口来查询当前设备是否支持该特性。

## 检查当前设备是否支持重建

1. 引入头文件。

   ```cpp
   #include "spatial/spatial_recon_interface.h"
   ```
2. 调用接口，根据返回值判断当前设备是否支持使用该特性。

   ```cpp
   HMS_SpatialReconStatus ret = HMS_SpatialRecon_IsSupport(SPATIAL_RECON_MODEL_TYPE_GS);
   ```

   如果当前设备支持此特性，会返回SPATIAL\_RECON\_STATUS\_SUCCESS，否则会返回SPATIAL\_RECON\_STATUS\_DEVICE\_NOT\_SUPPORT。

## 引入Spatial Recon Kit

1. 引入头文件。

   ```cpp
   #include "spatial/spatial_recon_interface.h"
   ```
2. 编写CMakeLists.txt。

   ```cpp
   find_library(
       # Sets the name of the path variable.
       spatialrecon-lib
       # Specifies the name of the NDK library that
       # you want CMake to locate.
       libspatial_recon_ndk.z.so
   )

   target_link_libraries(entry PUBLIC
       ${spatialrecon-lib}
   )
   ```

## 创建Spatial Recon Kit会话

当需要使用空间重建能力时，应调用[HMS\_SpatialRecon\_CreateSession](../harmonyos-references/capi-spatial-recon-interface-h.md#hms_spatialrecon_createsession)函数创建一个Spatial Recon Kit会话。

在创建时，需要指定一个工作目录，用于存放重建过程中的必要数据。此工作目录必须是已经存在的目录，且必须是应用文件目录的子目录。

```cpp
HMS_SpatialRecon_Session* spatialReconSession = nullptr;

const char* workPath = "/data/storage/el1/base/spatial_recon_files/"; // 指定工作目录为 /data/storage/el[1-5]/base/的子目录。开发者可视情况选取不同的加密等级。

HMS_SpatialReconStatus ret = HMS_SpatialRecon_CreateSession(SPATIAL_RECON_MODEL_TYPE_GS, workPath, &spatialReconSession);
```

创建会话成功后，会返回SPATIAL\_RECON\_STATUS\_SUCCESS，否则返回SPATIAL\_RECON\_STATUS\_FAILED。

## 销毁Spatial Recon Kit会话

在空间重建session的所有相关任务完成后，开发者可以调用[HMS\_SpatialRecon\_DestroySession](../harmonyos-references/capi-spatial-recon-interface-h.md#hms_spatialrecon_destroysession)函数销毁当前的Spatial Recon Kit会话。

和C/C++的裸指针行为类似，Spatial Recon Kit不保证session具备并发能力，开发者应在确认session相关任务执行完毕，再销毁session。

```cpp
HMS_SpatialRecon_DestroySession(spatialReconSession);
```

请注意，如果某session正在执行任务（如重建、保存）时要求销毁，会导致未定义行为。一旦调用了此函数销毁session，则不应该对此session进行任何操作，否则结果是未定义的。
