---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/xengine-kit-subpass-shading
title: Subpass Shading
breadcrumb: 指南 > 图形 > XEngine Kit（GPU加速引擎服务） > Subpass Shading
category: harmonyos-guides
scraped_at: 2026-09-05T06:15:00+08:00
doc_updated_at: 2026-08-03
content_hash: sha256:b02913d9676f8cabb42c0b774c5821ce97fb7a61bcaf897e3894d89e9aa7e2e8
---

随着游戏场景的复杂化，越来越多的光照效果被应用到游戏场景中，随之也带来大量的光照计算以及带宽消耗。目前通过Tile-Based Deferred Rendering（TBDR）和Forward+等方法可以解决大量光照的渲染时间消耗，但是大量带宽的占用问题还是没有解决，Subpass Shading（子通道着色）能力主要减少计算过程中的读写从而减少带宽的占用。

下图说明Subpass Shading节省渲染通道1和Compute Pass从Device memory上面的一次读写带宽。

**图1** Forward+读取过程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9/v3/HdDkzirUTuOxkDpvEXvReA/zh-cn_image_0000002742123901.png)

**图2** Subpass Shading读取过程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/lcspDEIaRJK0guQsx-XWHw/zh-cn_image_0000002712244994.png)

## 约束与限制

支持的设备类型：Phone，从5.0.2(14)版本开始，新增支持Tablet、PC/2in1设备，从5.1.0(18)版本开始新增支持TV设备。

## 接口说明

通过Vulkan扩展接口[VK\_HUAWEI\_subpass\_shading](https://registry.khronos.org/vulkan/specs/latest/man/html/VK_HUAWEI_subpass_shading.html)提供Subpass Shading API，该扩展支持在Subpass中使用Compute Shader，并在Compute Shader中使用SubpassLoad从Tile buffer中直接读取数据，可用于降低DDR带宽，适用于TBDR和Forward+管线。

Subpass Shading能力具体使用请参见[Demo（GPU加速引擎-Subpass Shading）](https://gitcode.com/harmonyos_samples/xengine-samplecode-subpass-shading-demo-cpp)。
