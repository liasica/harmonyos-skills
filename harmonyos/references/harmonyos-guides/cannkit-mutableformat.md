---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-mutableformat
title: MutableFormat
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > Tensor > MutableFormat
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:40+08:00
doc_updated_at: 2026-05-12
content_hash: sha256:6d88b537261617ae76254f8f46bf2f3e318926c3069103c04d5faeca20514b69
---

## 函数功能

获取Tensor的format，包含运行时format和原始format。

## 函数原型

```cpp
StorageFormat &MutableFormat()
```

## 参数说明

无

## 返回值

format引用。

关于StorageFormat类型的定义，请参见[StorageFormat](cannkit-storageformat-constructor.md)。

## 约束说明

无

## 调用示例

```cpp
Tensor tensor{{{8, 3, 224, 224}, {16, 3, 224, 224}}, // shape
              {ge::FORMAT_ND, ge::FORMAT_FRACTAL_NZ, {}}, // format
              kFollowing, // placement
              ge::DT_FLOAT16, // dt
              nullptr};
auto fmt = tensor.MutableFormat();
```
