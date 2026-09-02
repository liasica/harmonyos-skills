---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getdatatype
title: GetDataType
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > Tensor > GetDataType
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:40+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:a2a5af4fa8b716b1b63c380faaac41dd16e10aabb128684f2014a5e6be0e6748
---

## 函数功能

获取Tensor的数据类型。

## 函数原型

```cpp
ge::DataType GetDataType() const
```

## 参数说明

无

## 返回值

返回Tensor中的数据类型。

关于ge::DataType的定义，请参见[DataType](cannkit-ge-datatype.md)。

## 约束说明

无

## 调用示例

```cpp
StorageShape sh({1, 2, 3}, {1, 2, 3});
Tensor t = {sh, {}, {}, ge::DT_FLOAT, nullptr};
// ge::DT_FLOAT
auto dt = t.GetDataType();
```
