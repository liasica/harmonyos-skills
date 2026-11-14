---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-overview-of-engineering-operator
title: AscendC算子工程开发概述
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > 自定义算子开发 > AscendC算子开发 > AscendC算子实现 > AscendC算子工程开发 > AscendC算子工程开发概述
category: harmonyos-guides
scraped_at: 2026-11-14T08:48:37+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:b583bcfa87814969259954fd24bd1e2978463cd5c0f4f32e71552228e37b3f15
---

工程化算子开发是指基于**自定义算子工程**完成算子实现、编译部署、单算子调用代码自动生成等一系列流程。

该开发流程是标准的开发流程，建议开发者按照该流程进行算子开发。该方式下，算子开发的代码会更规范、统一、易于维护；同时该方式考虑了单算子API调用、算子入图、AI框架调用等功能的集成，使得开发者易于借助DDK框架实现上述功能。

工程化算子开发流程如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/whyROTlPR6qEwC-jDTAhUg/zh-cn_image_0000002817507863.png?HW-CC-KV=V1&HW-CC-Date=20261114T004837Z&HW-CC-Expire=31536000000&HW-CC-Sign=BAC4E34F5C2216E644023B2D7E7030C25567992FE5D48C475BCA25EE7BA0263C)

1. 环境准备。

   1. CANN软件包安装请参考[环境准备](cannkit-environment-preparation.md)。
   2. [创建算子工程](cannkit-creating-an-operator-project.md)。基于鸿蒙CANN社区recipe仓的工程模板创建算子开发工程。
2. 算子实现。

   * [算子原型定义实现](cannkit-operator-prototype-definition.md)。通过原型定义来描述算子输入输出、属性等信息以及算子在AI处理器上相关实现信息，并关联tiling实现等函数。
   * Kernel侧算子实现和host侧tiling实现请参考[算子实现](cannkit-operator-implementation-overview.md)；工程化算子开发，支持开发者调用Tiling API基于DDK提供的编程框架进行tiling开发，kernel侧也提供对应的接口方便开发者获取tiling参数，具体内容请参考[Kernel侧算子实现](cannkit-operator-implementation-on-the.md)和[Host侧Tiling实现](cannkit-tiling-implementation-on-the-host.md)，由此而带来的额外约束也在上述章节说明。
3. [编译部署](cannkit-operator-project-compilation.md)。通过工程编译脚本完成算子的编译部署。
4. 算子调用。调用单算子API接口，基于C语言的API执行算子。
