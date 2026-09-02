---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-ge-tensor-getplacement
title: GetPlacement
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > Tensor > GetPlacement
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:40+08:00
doc_updated_at: 2026-05-12
content_hash: sha256:f140c9136a7d362fad1aaf608960e4d65745760a6fdac0a6a8f4a8a37615f9f3
---

## 函数功能

获取tensor的placement。

## 函数原型

```cpp
TensorPlacement GetPlacement() const
```

## 参数说明

无

## 返回值

返回tensor的placement。

关于TensorPlacement类型的定义，请参见[TensorPlacement](cannkit-tensorplacement.md)。

## 约束说明

无

## 调用示例

```cpp
Tensor tensor{{{8, 3, 224, 224}, {16, 3, 224, 224}}, // shape
              {ge::FORMAT_ND, ge::FORMAT_FRACTAL_NZ, {}}, // format
              kFollowing, // placement
              ge::DT_FLOAT16, // dt
              nullptr};
auto placement = tensor.GetPlacement(); // kFollowing
```
