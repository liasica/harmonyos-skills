---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-typedcontinuousvector-introduction
title: 简介
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > TypedContinuousVector > 简介
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:41+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:96d8b4fe839ac9ee66c3e7c0e0fd90819a394999f1b6466f4a121faa02227266
---

本类继承自ContinuousVector类，与ContinuousVector类不同的是MutableData和GetData返回的是指定类型的地址，而不是void \*。因此称为Typed。
