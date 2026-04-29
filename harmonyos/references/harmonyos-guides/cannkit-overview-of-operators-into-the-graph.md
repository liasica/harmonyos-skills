---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-overview-of-operators-into-the-graph
title: 算子入图概述
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > 自定义算子开发 > 算子部署 > 算子入图（GE图）开发 > 算子入图概述
category: harmonyos-guides
scraped_at: 2026-04-29T13:41:14+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:80b1fa00e22f8ffa0429482d04f194c9dce584ef2fadc8a0fde726b5eac1da18
---

图模式是神经网络模型的一种运行模式，在图模式下开发者首先将模型的计算过程构造成一张图，然后通过GE将图下发到Kirin硬件执行。相对于单个算子依次下发的方式，图模式下，GE可以通过计算图优化、多流并行、内存复用、模型下沉等技术手段，加速模型执行效率，减少模型内存占用。

算子入图的开发流程如下图所示，算子工程创建完成后，基于工程代码框架完成算子原型定义、Kernel侧算子实现、Host侧Tiling实现并完成算子入图开发，通过工程编译脚本完成算子的编译部署，之后即可基于图IR执行算子，比如单算子模型执行或者IR构图的方式调用自定义算子。该开发流程以[工程化算子开发](cannkit-overview-of-engineering-operator.md)为基础，除了需要提供[算子实现](cannkit-operator-prototype-definition.md)中的算子实现文件外，还需要额外交付算子入图的代码文件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/zs8cmK0fQYeZrdWNHfh03w/zh-cn_image_0000002558765752.png?HW-CC-KV=V1&HW-CC-Date=20260429T054113Z&HW-CC-Expire=86400&HW-CC-Sign=C0D76596129B123AB146F4EB1B7B94416CBD72F68D9E6369D6CAF313C34C494D)

1. 环境准备。

   1. DDK软件安装请参考[环境准备](cannkit-environment-preparation.md)。
   2. [创建算子工程](cannkit-creating-an-operator-project.md)。使用msOpGen工具创建算子开发工程。
2. 算子实现。

   * [算子原型定义实现](cannkit-operator-prototype-definition.md)。通过原型定义来描述算子输入输出、属性等信息以及算子在AI处理器上相关实现信息，并关联Tiling实现等函数。
   * Kernel侧算子实现和Host侧Tiling实现请参考[算子实现](cannkit-operator-implementation-overview.md)；工程化算子开发，支持开发者调用Tiling API基于DDK提供的编程框架进行Tiling开发，Kernel侧也提供对应的接口方便开发者获取Tiling参数，具体内容请参考[Kernel侧算子实现](cannkit-operator-implementation-on-the.md)和[Host侧Tiling实现](cannkit-tiling-implementation-on-the-host.md)，由此而带来的额外约束也在上述章节说明。
3. [开发流程](cannkit-development-process.md)。算子入图场景下，需要提供shape推导等算子入图适配函数的实现。
4. [算子编译安装](cannkit-operator-project-compilation.md)。通过工程编译脚本完成算子的编译安装。
5. [图编译和图执行](cannkit-graph-compilation-and-execution.md)。基于图IR执行算子，比如单算子模型执行或者IR构图的方式调用自定义算子。

   说明

   HarmonyOS Next暂不支持图编译与图执行，仅支持通过[AI框架算子适配](cannkit-overview-of-ai-framework-operator.md)方式集成算子。
