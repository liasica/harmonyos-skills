---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-tbuf-overview
title: 简介
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > AscendC API > 基础API > 内存管理与同步控制 > TBuf > 简介
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:37+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:d6f54d5b944d3b274f72f014a24657db8450bd09f154edabce10076aa66fdd2c
---

使用AscendC编程的过程中，可能会用到一些临时变量。这些临时变量占用的内存可以使用TBuf数据结构来管理，存储位置通过模板参数来设置，可以设置为不同的TPosition逻辑位置。

TBuf占用的存储空间通过TPipe进行管理，开发者可以通过[InitBuffer](cannkit-tpipe-initbuffer.md)接口为TBuf进行内存初始化操作，之后即可通过[Get](cannkit-tbuf-get.md)获取指定长度的Tensor参与计算。

使用[InitBuffer](cannkit-tpipe-initbuffer.md)为TBuf分配内存和为Queue分配内存有以下差异：

* 为TBuf分配的内存空间只能参与计算，无法执行Queue队列的入队出队操作。
* 调用一次内存初始化接口，TPipe只会为TBuf分配一块内存，为Queue队列可以通过参数设置申请多块内存。如果要使用多个临时变量，需要定义多个TBuf数据结构，对每个TBuf数据结构分别调用[InitBuffer](cannkit-tpipe-initbuffer.md)接口进行内存初始化。
* TBuf获取的Tensor无需释放。
