---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-continuousvectorvector-introduction
title: 简介
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > ContinuousVectorVector > 简介
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:39+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:1441b1826b42b89f114585548086176ef2323bf7c237de56c64e83c93e71fb94
---

在内存中开辟一块连续的空间，用于存储数据的描述信息以及实际的数据元素，元素类型为ContinuousVector结构。不支持动态扩容。

本类的描述信息包括：用于存放数据的内存空间的总容量capacity\_、当前存放的实际元素数量size\_及各个数据元素相对于ContinuousVectorVector结构首地址的偏移量offset\_。
