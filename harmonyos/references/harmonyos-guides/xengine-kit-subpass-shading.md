---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/xengine-kit-subpass-shading
title: Subpass Shading
breadcrumb: 指南 > 图形 > XEngine Kit（GPU加速引擎服务） > Subpass Shading
category: harmonyos-guides
scraped_at: 2026-04-29T13:36:43+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:fb1c7060174d3da266fb2a6baae943bd2d0df6d4b18c53a8481d8292189108a9
---

随着游戏场景的复杂化，越来越多的光照效果被应用到游戏场景中，随之也带来大量的光照计算以及带宽消耗。目前通过Tile-Based Deferred Rendering（TBDR）和Forward+等方法可以解决大量光照的渲染时间消耗，但是大量带宽的占用问题还是没有解决，Subpass Shading能力主要减少计算过程中的读写从而减少带宽的占用。

下图说明Subpass Shading节省渲染通道1和Compute Pass从Device memory上面的一次读写带宽。

**图1** Forward+读取过程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/11/v3/TmTmi65LSH-CwFjhkNBDIg/zh-cn_image_0000002558605582.png?HW-CC-KV=V1&HW-CC-Date=20260429T053642Z&HW-CC-Expire=86400&HW-CC-Sign=F915CA4620F270943CB8E06D87336F78C066DE61E566037396CE2F90BCE205AB)

**图2** Subpass Shading读取过程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/6uegWU4-SVu0fr57SZ27Rg/zh-cn_image_0000002589325109.png?HW-CC-KV=V1&HW-CC-Date=20260429T053642Z&HW-CC-Expire=86400&HW-CC-Sign=E821450D18C8BF699B3E6583CBC3E24771D6A38FF90279C9FB930C00A600FCDB)

## 约束与限制

支持的设备类型：Phone，从5.0.2(14)版本开始，新增支持Tablet、PC/2in1设备，从5.1.0(18)版本开始新增支持TV设备。

## 接口说明

通过Vulkan扩展接口[VK\_HUAWEI\_subpass\_shading](https://registry.khronos.org/vulkan/specs/latest/man/html/VK_HUAWEI_subpass_shading.html)提供Subpass Shading API，该扩展支持在Subpass中使用Compute Shader，并在Compute Shader中使用SubpassLoad从Tile buffer中直接读取数据，可用于降低DDR带宽，适用于TBDR和Forward+管线。

Subpass Shading能力具体使用请参见[Demo（GPU加速引擎-Subpass Shading）](https://gitcode.com/harmonyos_samples/xengine-samplecode-subpass-shading-demo-cpp)。
