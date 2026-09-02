---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getshapesize
title: GetShapeSize
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > Tensor > GetShapeSize
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:40+08:00
doc_updated_at: 2026-06-27
content_hash: sha256:89493d67de21dcdcc108370fdec20f368224f5ab7370f525bb9200ca1be93578
---

## 函数功能

获取当前Tensor运行时的shape大小，即此Tensor中包含的元素的数量。

## 函数原型

```cpp
int64_t GetShapeSize() const
```

## 参数说明

无。

## 返回值

返回执行时shape的大小。

## 约束说明

无

## 调用示例

```cpp
Tensor tensor{{{8, 3, 224, 224}, {16, 3, 224, 224}}, // shape
              {ge::FORMAT_ND, ge::FORMAT_FRACTAL_NZ, {}}, // format
              kOnDeviceHbm, // placement
              ge::DT_FLOAT16, // dt
              nullptr};
auto shape_size = tensor.GetShapeSize(); // 16*3*224*224
```
