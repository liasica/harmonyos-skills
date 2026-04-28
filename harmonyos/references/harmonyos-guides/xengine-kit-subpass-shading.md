---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/xengine-kit-subpass-shading
title: Subpass Shading
breadcrumb: 指南 > 图形 > XEngine Kit（GPU加速引擎服务） > Subpass Shading
category: harmonyos-guides
scraped_at: 2026-04-28T07:47:54+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:de39cd51b787af4edb53279cf875913c430ef4d2d856846c411ae1787196ff89
---

随着游戏场景的复杂化，越来越多的光照效果被应用到游戏场景中，随之也带来大量的光照计算以及带宽消耗。目前通过Tile-Based Deferred Rendering（TBDR）和Forward+等方法可以解决大量光照的渲染时间消耗，但是大量带宽的占用问题还是没有解决，Subpass Shading能力主要减少计算过程中的读写从而减少带宽的占用。

下图说明Subpass Shading节省渲染通道1和Compute Pass从Device memory上面的一次读写带宽。

**图1** Forward+读取过程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/KKVeduoKQgywQwJiPGN3sA/zh-cn_image_0000002583478739.png?HW-CC-KV=V1&HW-CC-Date=20260427T234753Z&HW-CC-Expire=86400&HW-CC-Sign=E67A75A1177A441442A24A552F473529A888AEE0275894C80BA08F8F76E1DF59)

**图2** Subpass Shading读取过程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/NnDpv4l5RRe8GmXsgZzOpw/zh-cn_image_0000002552799090.png?HW-CC-KV=V1&HW-CC-Date=20260427T234753Z&HW-CC-Expire=86400&HW-CC-Sign=AB3C9188E82C5EA27B9219642809CBB7F276B3F69938DE26FA17EB04C3CC9E99)

## 约束与限制

支持的设备类型：Phone，从5.0.2(14)版本开始，新增支持Tablet、PC/2in1设备，从5.1.0(18)版本开始新增支持TV设备。

## 接口说明

通过Vulkan扩展接口[VK\_HUAWEI\_subpass\_shading](https://registry.khronos.org/vulkan/specs/latest/man/html/VK_HUAWEI_subpass_shading.html)提供Subpass Shading API，该扩展支持在Subpass中使用Compute Shader，并在Compute Shader中使用SubpassLoad从Tile buffer中直接读取数据，可用于降低DDR带宽，适用于TBDR和Forward+管线。

Subpass Shading能力具体使用请参见[Demo（GPU加速引擎-Subpass Shading）](https://gitcode.com/harmonyos_samples/xengine-samplecode-subpass-shading-demo-cpp)。
