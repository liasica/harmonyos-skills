---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getblockdim
title: GetBlockDim
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > TilingContext > GetBlockDim
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:41+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:f229b2004175186bf16fc238463d9153b380e2919c55b8ff38b62bfbb868b615
---

## 函数功能

获取blockDim，即参与计算的Vector或者Cube核数。blockDim的详细概念和设置方式请参考[SetBlockDim](cannkit-setblockdim.md)。

## 函数原型

```cpp
uint32_t GetBlockDim() const;
```

## 参数说明

无

## 返回值

返回blockDim。

## 约束说明

无

## 调用示例

```cpp
ge::graphStatus Tiling4XXX(TilingContext* context) {
  auto block_dim = context->GetBlockDim();
  // ...
}
```
