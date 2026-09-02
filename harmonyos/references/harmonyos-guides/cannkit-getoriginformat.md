---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getoriginformat
title: GetOriginFormat
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > StorageFormat > GetOriginFormat
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:40+08:00
doc_updated_at: 2026-05-12
content_hash: sha256:769225a462abbfb94d72b03abcfe12f9821e719531e2ad098cc5dc1b8e122858
---

## 函数功能

获取原始format。

## 函数原型

```cpp
ge::Format GetOriginFormat() const
```

## 参数说明

无

## 返回值

原始format。

## 约束说明

无

## 调用示例

```cpp
ExpandDimsType dim_type("1100");
StorageFormat format(ge::Format::FORMAT_NCHW, ge::Format::FORMAT_C1HWNC0, dim_type);
auto origin_format = format.GetOriginFormat(); // Format::FORMAT_NCHW
```
