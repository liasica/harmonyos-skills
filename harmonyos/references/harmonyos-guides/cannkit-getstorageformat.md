---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getstorageformat
title: GetStorageFormat
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > StorageFormat > GetStorageFormat
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:40+08:00
doc_updated_at: 2026-05-12
content_hash: sha256:a2433fd34720286f149d3c06afa80a115a572f512546996b0bbd2d3e537a15e8
---

## 函数功能

获取运行时format。

## 函数原型

```cpp
ge::Format GetStorageFormat() const
```

## 参数说明

无

## 返回值

运行时format。

## 约束说明

无

## 调用示例

```cpp
ExpandDimsType dim_type("1100");
StorageFormat format(ge::Format::FORMAT_NCHW, ge::Format::FORMAT_C1HWNC0, dim_type);
auto storage_format = format.GetStorageFormat(); // Format::FORMAT_C1HWNC0
```
