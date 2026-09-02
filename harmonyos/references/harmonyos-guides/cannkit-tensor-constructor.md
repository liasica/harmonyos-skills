---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-tensor-constructor
title: 构造函数
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > Tensor > 构造函数
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:40+08:00
doc_updated_at: 2026-05-12
content_hash: sha256:35e80b4ce9bf443d22d1b548322d50f1710d52fa3b5198db26e11c8d95942929
---

## 函数功能

用于构造指定的Tensor对象。Tensor类用来描述一个tensor对象的信息以及行为，包含：shape信息、format信息、datatype信息以及tensor数据内容tensordata。

## 函数原型

```cpp
Tensor (const StorageShape &storage_shape, const StorageFormat &storage_format, const TensorPlacement placement, const ge::DataType data_type, TensorAddress addr)
Tensor(const StorageShape &storage_shape, const StorageFormat &storage_format, ge::DataType data_type)
```

## 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| storage\_shape | 输入 | 指定tensor的shape信息。 |
| storage\_format | 输入 | 指定tensor的format信息。 |
| placement | 输入 | 指定tensor的实际数据所存储的device位置。 |
| data\_type | 输入 | 指定tensor的datatype信息。 |
| addr | 输入 | 指定tensor的实际数据所存储的内存地址。 |

## 返回值

返回一个初始化的Tensor对象。

## 约束说明

无

## 调用示例

```cpp
Tensor tensor{{{8, 3, 224, 224}, {16, 3, 224, 224}}, // shape
              {ge::FORMAT_ND, ge::FORMAT_FRACTAL_NZ, {}}, // format
              kOnDeviceHbm, // placement
              ge::DT_FLOAT16, // dt
              nullptr};
```
