---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-multi-hap-hsp-practice
title: 性能/内存优化：多HAP/HSP工程编译优化实践
breadcrumb: 指南 > 构建应用 > 提升构建效率 > 实践说明 > 性能/内存优化：多HAP/HSP工程编译优化实践
category: harmonyos-guides
scraped_at: 2026-09-02T15:00:27+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:11d882a8b575dee43125f8a02d664dc0fe234b5616dc256a7ef73b16beacef9c
---

## 概述

在包含多个HAP/HSP模块的工程中，执行构建（Build Hap(s)）时，会针对每个模块单独启动编译任务，每个编译任务都会对该模块的依赖模块进行语法检查、转换等编译流程。如果不同的HAP/HSP依赖相同的HAR模块，重复的编译检查会导致编译耗时增加、占用内存升高。

本文介绍几种常用的优化方案，通过控制编译构建的启动方式，合理调整模块类型，启用一些常用配置，可以在部分场景下有效降低编译构建耗时和内存占用。

## 优化方案一：控制编译构建启动方式

通过选择合适的构建和运行启动方式，避免编译所有的HAP/HSP，仅编译受影响的模块及其依赖。

* 构建（Build）启动优化

  修改单个模块后，可以通过Build Hap(s)和Make Module进行构建，两者的差异如下。

  | 启动方式 | 行为描述 | 适用场景 | 资源消耗 |
  | --- | --- | --- | --- |
  | Build Hap(s) | 编译打包所有HAP模块及其依赖。 | 需要生成所有HAP/HSP安装包进行真机安装时。 | 高（编译全部HAP） |
  | Make Module | 仅编译打包当前模块及其依赖。 | 日常开发中，仅修改了单个模块代码，需快速验证逻辑时。 | 低（编译单个模块） |

  因此，修改单模块后，建议通过Make Module进行构建，这样可以在多HAP/HSP场景下减少单次修改所编译的安装包数量，从而降低耗时和内存占用。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/99/v3/-r02JIQtQYWNHXs4LDb8Ug/zh-cn_image_0000002701663412.png)
* 运行（Run）启动优化

  通过推包运行的方式启动编译构建，可以降低某些场景下的耗时和内存占用。例如频繁增量修改某个HSP模块，如果不涉及修改其导出接口，可以优先选择运行该HSP模块，从而避免重新编译和打包其他未修改的HAP/HSP模块。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/WhgepNfqRq-IEoJ4x_FFDw/zh-cn_image_0000002731542607.png)

## 优化方案二：HSP改造为HAR

HAP和HSP、HSP之间可能依赖相同的HAR，导致编译、包体积都会有重复的部分。如果模块不需要按需加载特性，将HSP改造为HAR，可以降低编译耗时及内存占用，减小包体积。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/lsJXTBpeRw-4NW877leiIQ/zh-cn_image_0000002731382639.png "点击放大")

### 改造原则

1. 自顶向下改造
   * 执行命令`ohpm list -r`分析工程的依赖链路。
   * 按照自顶向下的顺序，从依赖链路的顶端HSP开始改造。
   * 原因：如果从底层HSP开始改造为HAR，上层的HSP可能引入重复的HAR依赖，导致构建时间不减反增。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/9NyTs_muQpuHOkKiKw7E0w/zh-cn_image_0000002731542605.png "点击放大")
2. 适用对象
   * 工程中不需要使用按需加载特性的HSP模块。

### 改造步骤

参考[HSP转HAR指导](hsp-to-har.md)。

### 常见问题

1. 同名资源文件冲突覆盖

   **问题现象**

   在单HAP项目架构中，多个HSP改造为HAR后，其资源文件会合并到entry模块中。如果不同HSP模块存在同名资源，会根据全局依赖配置的先后顺序执行覆盖逻辑，可能导致资源丢失或错误。

   **解决方案**

   资源命名规范化，为各模块的资源文件增加唯一标识。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/wqkfbEC6QDeQ_VEfR-AgSg/zh-cn_image_0000002731382637.png "点击放大")
2. Worker线程加载路径变更

   **问题现象**

   如果HSP模块中使用了Worker线程，改造为HAR后，由于模块类型变化，Worker的加载路径规则可能发生变化。

   **解决方案**

   根据[Stage模型下的文件路径规则](worker-introduction.md#stage模型下的文件路径规则)调整Worker的加载方式。

## 优化方案三：性能/内存优化常用配置

此外，还有一些针对编译构建效率的配置，可以帮助进一步减少构建耗时和内存，提升使用体验。在hvigor-config.json5中添加以下字段，关于字段的详细介绍请参考[实验特性](ide-hvigor-experimental-properties.md)。

```json5
"properties": {
  "hvigor.task.schedule.optimization": true,   // 开启任务调度优化，通过优先执行CompileArkTs及其依赖的任务，能够尽早启动编译任务CompileArkTs，从而减少构建时间
  "ohos.arkCompile.noEmitJs": true,    // 优化编译中间产物生成，ArkTS代码编译时，不会再生成中间态的js代码，从而减少编译时间和内存占用。
  "ohos.arkCompile.singleFileEmit": true     // 优化编译产物写入，ArkTS代码编译时，在单文件解析完成后会写入磁盘，可以降低编译过程的峰值内存。
}
```
