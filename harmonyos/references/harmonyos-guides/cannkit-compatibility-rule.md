---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-compatibility-rule
title: 兼容性说明
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC昇腾到麒麟兼容性迁移指南 > 兼容性说明
category: harmonyos-guides
scraped_at: 2026-04-29T13:42:59+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:a5ba15085d4284264383f69b2da68ecfe43e9415122cb96972b78e7dec08d216
---

总体兼容性策略见表1 Ascend C API兼容策略，兼容性范围不包含编译器BuiltIn API、Ascend C内部实现接口等。若开发者希望在新平台运行其它平台开发的Ascend C程序，需要在新平台重新编译并运行，并可能需要根据迁移指导进行代码调整。

**图1** Ascend C API层次结构

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/vuRDt6NISc6RynsfcCTbQA/zh-cn_image_0000002589245603.png?HW-CC-KV=V1&HW-CC-Date=20260429T054258Z&HW-CC-Expire=86400&HW-CC-Sign=002227C2518AA5C5677320E96A8F814C04DD39D5049B11A33AAFA2F8E25DC7C0 "点击放大")

**表1** Ascend C API兼容策略

| API层级 | 兼容策略 |
| --- | --- |
| 高阶API | 高阶API在所有架构上均具备兼容性，但在涉及领域特性的部分存在不兼容情况。 |
| 基础API | 基础API分为可兼容的基础API和ISASI基础API；兼容的API在所有架构上均能兼容；ISASI API为体系架构相关的API，不保证跨架构版本的兼容性，例如CUBE侧的计算接口LoadData、Mmad等。 |
| 框架API | 框架API为软件实现API，跨架构版本兼容。 |
| 语言扩展C API | 不保证兼容。 |
| 编译器BuiltIn API | 不保证兼容。 |

**简要说明**

1. 为了保证兼容性，建议开发者在开发过程中尽量避免使用如下接口或编程方式，否则开发者需自行保证兼容性。

   * 非Ascend C公开接口、结构体，例如impl目录下的接口、结构体等；
   * 对芯片规格进行硬编码。例如：

     ```
     1. uint32_t MAX_UB_SIZE = 256 * 1024;
     2. // 建议获取方式：ascendcPlatform.GetCoreMemSize(platform_ascendc::CoreMemType::UB, MAX_UB_SIZE);
     3. // ...
     ```
   * 编译器BuiltIn API。例如：

     ```
     1. copy_gm_to_ubuf(input_1_local_ub, input_1, 0, 1, 8, 0, 0);
     ```
   * TilingKey编程。
2. 建议开发者使用如下接口或编程方式。

   * 兼容的API。
   * 若涉及特定领域扩展特性，在Device侧用[NPU\_ARCH编译宏](cannkit-migration-guidance-overview.md)进行隔离，在Host侧用[SocVersion](cannkit-getsocversion.md)进行隔离。
   * 使用[Tiling模板编程](https://www.hiascend.com/document/detail/zh/canncommercial/83RC1/opdevg/Ascendcopdevg/atlas_ascendc_10_00025.html)。
