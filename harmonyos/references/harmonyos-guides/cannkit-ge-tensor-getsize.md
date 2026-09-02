---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-ge-tensor-getsize
title: GetSize
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > Tensor > GetSize
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:40+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:c4ba80cf6a98e7d1940e15c877354ccab9f8a887fc9b7325f8756d761fa2d7d7
---

## 函数功能

获取Tensor数据的内存大小。

## 函数原型

```cpp
size_t GetSize() const
```

## 参数说明

无

## 返回值

内存大小，单位是字节。

## 约束说明

无

## 调用示例

```cpp
StorageShape sh({1, 2, 3}, {1, 2, 3});
Tensor t = {sh, {}, {}, ge::DT_FLOAT, nullptr};
auto td_size = t.GetSize(); // 1*2*3*sizeof(float) = 24;
```
