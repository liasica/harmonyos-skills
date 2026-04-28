---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-api-overview
title: 接口概述
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > 自定义算子开发 > 基本概念 > 编程API > 接口概述
category: harmonyos-guides
scraped_at: 2026-04-28T07:51:27+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:8cb5815716a3d2b9d8d5f3d814e82542f6b07ff5d7342764b8359665de0850c0
---

AscendC算子采用标准C++语法和一组类库API进行编程，开发者可以根据自己的需求选择合适的API。AscendC编程类库API示意图如下所示，AscendC API的操作数都是Tensor类型：GlobalTensor和LocalTensor；类库API分为基础API和高阶API。

* **基础API：** 实现对硬件能力的抽象，开放芯片的能力，保证完备性和兼容性。标注为ISASI（Instruction Set Architecture Special Interface，硬件体系结构相关的接口）类别的API，不能保证跨硬件版本兼容。
* **高阶API：** 实现一些常用的计算算法，用于提高编程开发效率，通常会调用多种基础API实现。高阶API包括数学库、Matmul、Softmax等API。高阶API可以保证兼容性。

**图1** AscendC编程类库API示意图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/19ul7FocRJe_E5pK1B6g7w/zh-cn_image_0000002583439283.png?HW-CC-KV=V1&HW-CC-Date=20260427T235126Z&HW-CC-Expire=86400&HW-CC-Sign=7806EAE22E0466A9F955220A4ECC2E01EDE5C26A7609ABBE4A950E2736502EE9)

对于基础API，主要分为以下几类：

* **计算API**，包括标量计算API、向量计算API、矩阵计算API，分别实现调用Scalar计算单元、Vector计算单元、Cube计算单元执行计算的功能。
* **数据搬运API**，计算API基于Local Memory数据进行计算，所以数据需要先从Global Memory搬运至Local Memory，再使用计算API完成计算，最后从Local Memory搬出至Global Memory。执行搬运过程的接口称之为数据搬运API，比如[DataCopy](cannkit-common-data-movement.md)接口。
* **内存管理API**，用于分配管理内存，比如AllocTensor、FreeTensor接口。
* **同步控制API**，完成任务间的通信和同步，比如EnQue、DeQue接口。不同的API指令间有可能存在依赖关系，从[硬件架构抽象](cannkit-hardware-architecture-abstraction.md)可知，不同的指令异步并行执行，为了保证不同指令队列间的指令按照正确的逻辑关系执行，需要向不同的组件发送同步指令。同步控制API内部即完成这个发送同步指令的过程，开发者无需关注内部实现逻辑，使用简单的API接口即可完成。
* **ISASI(Instruction Set Architecture Special API)，** 硬件体系结构相关的API，该类接口不能保证跨硬件版本兼容。

对于基础API中的**计算API，** 根据对数据操作方法的不同，分为以下**几种计算方式：**

* **整个tensor参与计算**：通过运算符重载的方式实现，支持“+, -, \*, /, |, &, <, >, <=, >=, ==, !=”，实现计算的简化表达。例如：

  dst=src1+src2
* **tensor前n个数据计算**：针对源操作数的连续n个数据进行计算并连续写入目的操作数，解决一维tensor的连续计算问题。例如：

  Add(dst, src1, src2, n);

下图以矢量加法为例，展示了几种计算方式的特点。

**图2** 计算API几种计算方式的特点

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/bnepHZeqSnmc2OgvAwX4zw/zh-cn_image_0000002552959238.png?HW-CC-KV=V1&HW-CC-Date=20260427T235126Z&HW-CC-Expire=86400&HW-CC-Sign=2692445E548D28F29828EEC6CC52A7A7B475EFCB3DAAE5433E697EB77741FB3E)

说明

AscendC API所在头文件目录为：

* 基础API：${DDK\_INSTALL\_PATH}/tools/tools\_ascendc/include/tikcpp/tikcfw/kernel\_operator.h。
* 高阶API：${DDK\_INSTALL\_PATH}/tools/tools\_ascendc/include/tikcpp/tikcfw/lib，其中${DDK\_INSTALL\_PATH}表示DDK软件安装目录。（目录头文件中包含的接口如果未在资料中声明，属于间接调用接口，开发者无需关注）
