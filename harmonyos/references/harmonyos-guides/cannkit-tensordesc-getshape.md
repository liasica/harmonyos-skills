---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-tensordesc-getshape
title: GetShape
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > TensorDesc > GetShape
category: harmonyos-guides
scraped_at: 2026-04-28T07:52:57+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:edc1fe721ae063d726d576a6866dbecc48b91cafbaa34b3d374731c6a59acd55
---

## 函数功能

获取TensorDesc所描述Tensor的Shape。

## 函数原型

```
1. Shape GetShape() const;
```

## 参数说明

无

## 返回值

| 类型 | 描述 |
| --- | --- |
| [Shape](cannkit-shape-construction-and-destructor.md) | TensorDesc描述的shape。 |

## 异常处理

无

## 约束说明

由于返回的Shape信息为值拷贝，因此修改返回的Shape信息，不影响TensorDesc中已有的Shape信息。
