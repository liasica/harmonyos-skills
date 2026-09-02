---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-shape-introduction
title: 简介
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > Shape > 简介
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:40+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:693a47262b452656c39cdf39a0cb931149d2e20ee8f86f81da152a97b6b968be
---

Shape结构体用于描述一个tensor的shape，包含两个信息：

```cpp
size_t dim_num_;
int64_t dims_[kMaxDimNum];
```

其中，dim\_num\_表示shape的维数，dims\_数组表示tensor具体的shape。
