---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-computenodeinfo-introduction
title: 简介
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > ComputeNodeInfo > 简介
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:38+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:4ebb96b3a915ebff79e969a594d8c6a054c5ae4d6bec7081fd6c380d7a743bd5
---

ComputeNodeInfo类主要的目的在于将算子的相关编译信息进行序列化保存，以便可以在图执行阶段能够高效地获取这些信息。

ComputeNodeInfo的内存空间是平铺式的，内存依次存放ComputeNodeInfo自身的数据成员、算子IR定义输入个数的Anchor信息、实际输入个数和输出个数的编译阶段的Tensor描述信息以及IR定义的属性信息。
