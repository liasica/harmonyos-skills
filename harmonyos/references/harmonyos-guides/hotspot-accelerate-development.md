---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hotspot-accelerate-development
title: 启用热点加速
breadcrumb: 指南 > 系统 > 基础功能 > Linx Kit（灵犀加速库） > 启用热点加速
category: harmonyos-guides
scraped_at: 2026-09-05T06:14:34+08:00
doc_updated_at: 2026-09-01
content_hash: sha256:810e54c7fcd95309459681356ada7ff619a27a8544fc4ec4b13c83966d3f50c1
---

Linx Kit提供实现热点加速优化的API接口，通过对线程执行过程中的热点代码模式进行针对性优化，提升线程执行效率。该功能主要用于优化特定线程的性能表现，适用于需要提升线程执行效率的场景。

## 热点加速模块介绍

以某场景为例，可以看到其CPU上的负载重点线程（逻辑线程和渲染线程），均具有帧粒度的周期性：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/ntSaZqkZTYCPK9MIDJJ4oQ/zh-cn_image_0000002742123547.png)

开发者确定对应源码位置后，在具有周期性的热点流程入口和出口位置分别调用本接口，本热点加速模块便可记录程序运行行为，例如分支跳转等关键信息，将其保存，并在下一帧进行重放，达到提升线程执行效率的效果。

## 开发步骤

在需要优化线程性能的场景下，开发者可以通过调用Linx Kit提供的热点加速API来提升线程执行效率。下面是热点加速优化模块的主要开发步骤：

1. 在正式调用前，开发者应使用性能分析工具，定位进程中的热点函数/流程，以便后续进行优化。
2. 在CMake脚本中链接相关动态库。

   ```cmake
    find_library(linxkit-lib liblinx.so)
    target_link_libraries(entry PUBLIC ${linxkit-lib})
   ```
3. 确定热点流程的源码位置后，需在该流程的入口和出口分别调用[HMS\_LINX\_HotspotAccelerateBegin](../harmonyos-references/capi-linx-hotspot-h.md#hms_linx_hotspotacceleratebegin)和[HMS\_LINX\_HotspotAccelerateEnd](../harmonyos-references/capi-linx-hotspot-h.md#hms_linx_hotspotaccelerateend)接口，以记录并重放关键行为。
4. 可将热点函数/流程划分为多个context，仅对最重要的context实施加速策略，从而降低主存访问开销。

以下是启用热点加速的完整代码步骤：

1. 引入头文件。

   ```
   #include "LinxKit/linx_hotspot.h"
   ```
2. 在应用进程创建时调用[HMS\_LINX\_HotspotAccelerateInit](../harmonyos-references/capi-linx-hotspot-h.md#hms_linx_hotspotaccelerateinit)，初始化热点加速模块。

   ```
   int32_t ret = HMS_LINX_HotspotAccelerateInit();
   if (ret != 0) {
       (void)OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_ID, "linxkit_test", "LinxKit init error: %{public}d", ret);
   }
   ```
3. 调用[HMS\_LINX\_HotspotAccelerateBegin](../harmonyos-references/capi-linx-hotspot-h.md#hms_linx_hotspotacceleratebegin)开始热点加速。ctx初始化为0，后续由热点加速API自动分配一个有效ctx。

   ```
   uint32_t ctx = g_ctx;
   int32_t ret = HMS_LINX_HotspotAccelerateBegin(&ctx);
   g_ctx = ctx;
   if (ret != 0) {
       (void)OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_ID, "linxkit_test", "LinxKit acc begin error: %{public}d", ret);
   }
   ```
4. 确保在不需要加速时调用[HMS\_LINX\_HotspotAccelerateEnd](../harmonyos-references/capi-linx-hotspot-h.md#hms_linx_hotspotaccelerateend)停止热点加速，释放资源。

   ```
   ret = HMS_LINX_HotspotAccelerateEnd(ctx);
   if (ret != 0) {
       (void)OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_ID, "linxkit_test", "LinxKit acc end error: %{public}d", ret);
   }
   ```
