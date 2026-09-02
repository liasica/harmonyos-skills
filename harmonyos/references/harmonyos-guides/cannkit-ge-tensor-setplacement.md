---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-ge-tensor-setplacement
title: SetPlacement
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > Tensor > SetPlacement
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:40+08:00
doc_updated_at: 2026-05-12
content_hash: sha256:8526a64ff6181bd2612255c1e21cbfeefa96058f97822f8472ea10dd41a46385
---

## 函数功能

设置tensor的placement。

## 函数原型

```cpp
void SetPlacement(const TensorPlacement placement)
```

## 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| placement | 输入 | 需要设置的tensor的placement。  关于TensorPlacement类型的定义，请参见[TensorPlacement](cannkit-tensorplacement.md)。 |

## 返回值

无

## 约束说明

无

## 调用示例

```cpp
Tensor tensor{{{8, 3, 224, 224}, {16, 3, 224, 224}}, // shape
              {ge::FORMAT_ND, ge::FORMAT_FRACTAL_NZ, {}}, // format
              kFollowing, // placement
              ge::DT_FLOAT16, // dt
              nullptr};
tensor.SetPlacement(TensorPlacement::kOnDeviceHbm);
auto placement = tensor.GetPlacement(); // kOnDeviceHbm
```
