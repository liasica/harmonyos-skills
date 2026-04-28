---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getstorageformat
title: GetStorageFormat
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > StorageFormat > GetStorageFormat
category: harmonyos-guides
scraped_at: 2026-04-28T07:52:10+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:b43e2ca2b708a2e808881ccd3e3eb1608c6be5b7f1037b3fc8fb83093e6d0207
---

## 函数功能

获取运行时format。

## 函数原型

```
1. ge::Format GetStorageFormat() const
```

## 参数说明

无

## 返回值

运行时format。

## 约束说明

无

## 调用示例

```
1. ExpandDimsType dim_type("1100");
2. StorageFormat format(ge::Format::FORMAT_NCHW, ge::Format::FORMAT_C1HWNC0, dim_type);
3. auto storage_format = format.GetStorageFormat();  // Format::FORMAT_C1HWNC0
```
