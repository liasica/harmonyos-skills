---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getoriginformat
title: GetOriginFormat
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > StorageFormat > GetOriginFormat
category: harmonyos-guides
scraped_at: 2026-04-28T07:52:10+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:304405a50a3234351de721630db58f98ea6002bf39c02c36a00d9a2bd876e161
---

## 函数功能

获取原始format。

## 函数原型

```
1. ge::Format GetOriginFormat() const
```

## 参数说明

无

## 返回值

原始format。

## 约束说明

无

## 调用示例

```
1. ExpandDimsType dim_type("1100");
2. StorageFormat format(ge::Format::FORMAT_NCHW, ge::Format::FORMAT_C1HWNC0, dim_type);
3. auto origin_format = format.GetOriginFormat();  // Format::FORMAT_NCHW
```
