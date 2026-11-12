---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-programmingapi-basic-apis
title: 基础API
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > 自定义算子开发 > AscendC算子开发 > 基本概念 > 编程API > 基础API
category: harmonyos-guides
scraped_at: 2026-11-12T09:52:41+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:c4774ca1961a82074c30b42bc6acc3adf6a10de1af80557e0bf14fbf2f96a147
---

## 数据搬运

数据搬运接口，包括[普通数据搬运](https://www.hiascend.com/document/detail/zh/CANNCommunityEdition/latest/API/ascendcopapi/docs/zh/api/api_list.md)、[随路格式转换](https://www.hiascend.com/document/detail/zh/CANNCommunityEdition/latest/API/ascendcopapi/docs/zh/api/api_list.md)。

* 普通数据搬运接口，适用于连续和不连续数据搬运。
* 随路格式转换接口，适用于在搬运时进行格式转换。

## 内存管理与同步控制

AscendC编程范式，把算子核内的处理程序，分成多个流水任务，通过队列(Queue)完成**任务间通信和同步**，并通过统一的**资源管理**模块(Pipe)来统一管理内存、事件等资源。

AscendC提供一组内存管理与同步控制API，开发者使用这一组API即可完成任务间同步和内存管理。

核心的API包括：

* AllocTensor：从Queue中分配Tensor，Tensor所占大小为InitBuffer时设置的每块内存长度。
* FreeTensor：释放Queue中的指定Tensor，供Queue后续使用。
* EnQue：将Tensor添加到队列Queue。
* DeQue：将Tensor从队列Queue中取出，用于后续处理。
