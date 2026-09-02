---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getaddr
title: GetAddr
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > TensorData > GetAddr
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:40+08:00
doc_updated_at: 2026-06-27
content_hash: sha256:3ebd87a324b0579217ecd3f96d9ccdeab63c71209196e29ed070a2fc6b4d7d42
---

## 函数功能

获取tensor数据地址。若存在manager函数，则由manager函数给出地址。

## 函数原型

```cpp
TensorAddress GetAddr() const
```

## 参数说明

无

## 返回值

tensor地址。

## 约束说明

无

## 调用示例

```cpp
auto addr0 = reinterpret_cast<void *>(0x10);
TensorData td(addr0, nullptr);
auto addr1 = td.GetAddr(); // 0x10
```
