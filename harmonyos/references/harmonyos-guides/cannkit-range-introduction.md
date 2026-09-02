---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-range-introduction
title: 简介
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > Range > 简介
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:39+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:18b062954c6cfb464f0b9b9c7cd09afb931892f00d77c68971b2de62a00ce84d
---

Range类用于描述一个对象的上下界，包含两个信息：

```cpp
T *min_;
T *max_;
```

其中，min\_表示对象下界的指针，max\_表示对象上界的指针。开发者可以自行定义上下界的类型。
