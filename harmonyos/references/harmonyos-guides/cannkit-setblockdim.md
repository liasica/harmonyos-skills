---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-setblockdim
title: SetBlockDim
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > TilingContext > SetBlockDim
category: harmonyos-guides
scraped_at: 2026-04-28T07:52:19+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:71ee70651751211d59a3404b97171c7dbe8e48284ed23a75e018f33f6f5baab5
---

## 函数功能

设置blockDim，即参与计算的Vector或者Cube核数。

## 函数原型

```
1. ge::graphStatus SetBlockDim(const uint32_t block_dim);
```

## 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| block\_dim | 输入 | blockDim是逻辑核的概念，取值范围为[1, 65535]。为了充分利用硬件资源，一般设置为物理核的核数或其倍数。对于耦合架构和分离架构，blockDim在运行时的意义和设置规则有一些区别，具体说明如下。  - 耦合架构：由于其Vector、Cube单元是集成在一起的，blockDim用于设置启动多个AICore核实例执行，不区分Vector、Cube。AI Core的核数可以通过GetCoreNumAiv或者GetCoreNumAic获取。  - 分离架构  - 针对仅包含Vector计算的算子，blockDim用于设置启动多少个Vector（AIV）实例执行，比如某款AI处理器上有40个Vector核，建议设置为40。  - 针对仅包含Cube计算的算子，blockDim用于设置启动多少个Cube（AIC）实例执行，比如某款AI处理器上有20个Cube核，建议设置为20。  - 针对Vector/Cube融合计算的算子，启动时，按照AIV和AIC组合启动，blockDim用于设置启动多少个组合执行，比如某款AI处理器上有40个Vector核和20个Cube核，一个组合是2个Vector核和1个Cube核，建议设置为20，此时会启动20个组合，即40个Vector核和20个Cube核。  **说明：** 该场景下，设置的blockDim逻辑核的核数不能超过物理核（2个Vector核和1个Cube核组合为1个物理核）的核数。  - AIC/AIV的核数分别通过GetCoreNumAic和GetCoreNumAiv接口获取。 |

## 返回值

设置成功时返回“ge::GRAPH\_SUCCESS”。

关于graphStatus的定义，请参见[ge::graphStatus](cannkit-gegraphstatus.md)。

## 约束说明

当前支持的Kirin9020和KirinX90系列处理器是分离架构。

## 调用示例

```
1. ge::graphStatus Tiling4XXX(TilingContext* context) {
2. auto ret = context->SetBlockDim(32);
3. // ...
4. }
```
