---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-tensordesc-getformat
title: GetFormat
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > TensorDesc > GetFormat
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:42+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:65f948a04cce75237782c4e1e5a27431d0bdc3cad89e3957d5d3003823621282
---

## 函数功能

获取TensorDesc所描述的Tensor的Format。

## 函数原型

```cpp
Format GetFormat() const;
```

## 参数说明

无

## 返回值

| 类型 | 描述 |
| --- | --- |
| [Format](cannkit-ge-format.md) | TensorDesc所描述的Tensor的format信息。 |

## 异常处理

无

## 约束说明

由于返回的Format信息为值拷贝，因此修改返回的Format信息，不影响TensorDesc中已有的Format信息。
