---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-gettensordata
title: GetTensorData
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > Tensor > GetTensorData
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:40+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:6e7d49450f52255b3a3b327e1e2cd2b4695874369b9a00d4fe95ce7ae3b31564
---

## 函数功能

获取tensor中的数据，返回只读的TensorData类型对象。

## 函数原型

```cpp
const TensorData &GetTensorData() const
```

## 参数说明

无

## 返回值

只读的tensor data引用。

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
