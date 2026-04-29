---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-overview-of-engineering-operator
title: 工程化算子开发概述
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > 自定义算子开发 > 算子实现 > 工程化算子开发 > 工程化算子开发概述
category: harmonyos-guides
scraped_at: 2026-04-29T13:41:08+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:4c4301c0b1e27717b14a37493e3e6cc030eae38cf2134243d7aa514d4c890f98
---

工程化算子开发是指基于自动生成的**自定义算子工程**完成算子实现、编译部署、单算子调用代码自动生成等一系列流程。

该开发流程是标准的开发流程，建议开发者按照该流程进行算子开发。该方式下，算子开发的代码会更规范、统一、易于维护；同时该方式考虑了单算子API调用、算子入图、AI框架调用等功能的集成，使得开发者易于借助DDK框架实现上述功能。

工程化算子开发流程如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/AcNQjPhgQ0OKrHmuNnn8Fw/zh-cn_image_0000002558765748.png?HW-CC-KV=V1&HW-CC-Date=20260429T054107Z&HW-CC-Expire=86400&HW-CC-Sign=A9E93306971ED6395B0FB72142CCDE562571B8393FAA049222687E514596E5A9)

1. 环境准备。

   1. DDK软件安装请参考[环境准备](cannkit-environment-preparation.md)。
   2. [创建算子工程](cannkit-creating-an-operator-project.md)。使用msOpGen工具创建算子开发工程。
2. 算子实现。

   * [算子原型定义实现](cannkit-operator-prototype-definition.md)。通过原型定义来描述算子输入输出、属性等信息以及算子在AI处理器上相关实现信息，并关联tiling实现等函数。
   * Kernel侧算子实现和host侧tiling实现请参考[算子实现](cannkit-operator-implementation-overview.md)；工程化算子开发，支持开发者调用Tiling API基于DDK提供的编程框架进行tiling开发，kernel侧也提供对应的接口方便开发者获取tiling参数，具体内容请参考[Kernel侧算子实现](cannkit-operator-implementation-on-the.md)和[Host侧Tiling实现](cannkit-tiling-implementation-on-the-host.md)，由此而带来的额外约束也在上述章节说明。
3. [编译部署](cannkit-operator-project-compilation.md)。通过工程编译脚本完成算子的编译部署。
4. 算子调用。调用单算子API接口，基于C语言的API执行算子。
