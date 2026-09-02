---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-mutabletensordata
title: MutableTensorData
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > Tensor > MutableTensorData
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:41+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:336069084774f7f04ee84e27caa0a0bd0fcfec0ad01e1f8e8e769da94cbd38e1
---

## 函数功能

获取tensor中的数据。

## 函数原型

```cpp
TensorData &MutableTensorData()
```

## 参数说明

无

## 返回值

可写的tensor data引用。

关于TensorData类型的定义，请参见[TensorData](cannkit-construction-and-destructor-functions.md)。

## 约束说明

无

## 调用示例

```cpp
Tensor t = {{}, {}, {}, {}, nullptr};
const Tensor &ct = t;
std::vector<int> a = {10};
t.MutableTensorData() = TensorData{reinterpret_cast<void *>(a.data()), nullptr}; // 设置新tensordata
auto td = t.GetTensorData(); // TensorData{a, nullptr}
```
