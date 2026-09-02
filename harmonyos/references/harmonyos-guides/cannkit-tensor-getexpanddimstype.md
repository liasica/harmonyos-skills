---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-tensor-getexpanddimstype
title: GetExpandDimsType
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > Tensor > GetExpandDimsType
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:40+08:00
doc_updated_at: 2026-05-12
content_hash: sha256:2cd6061e3dddbcfb7c4cd1d70f9de496f71de6e7de6dc3dce01b98322287612f
---

## 函数功能

获取shape的补维规则。

## 函数原型

```cpp
ExpandDimsType GetExpandDimsType() const
```

## 参数说明

无

## 返回值

返回shape的补维规则。

关于ExpandDimsType类型的定义，请参见[ExpandDimsType](cannkit-expanddimstype-introduction.md)。

## 约束说明

无

## 调用示例

```cpp
Tensor tensor{{{8, 3, 224, 224}, {16, 3, 224, 224}}, // shape
              {ge::FORMAT_ND, ge::FORMAT_FRACTAL_NZ, {}}, // format
              kFollowing, // placement
              ge::DT_FLOAT16, // dt
              nullptr};
auto expand_dims_type = tensor.GetExpandDimsType(); // ExpandDimsType{}
```
