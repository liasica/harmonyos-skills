---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-tensorplacement
title: TensorPlacement
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > TensorPlacement
category: harmonyos-guides
scraped_at: 2026-04-28T07:52:24+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:9f9d8a0714be2f965ea531b19badb027b2a6ec2e086bd9dbc5a09ad76ce8830a
---

```
1. enum TensorPlacement {
2. kOnDeviceHbm,  // < Tensor位于Device上的HBM内存
3. kOnHost,       // < Tensor位于Host
4. kFollowing,    // < Tensor位于Host，且数据紧跟在结构体后面
5. kOnDeviceP2p,  // < Tensor位于Device上的P2p内存, 指的是HBM透到PCIE BAR空间上,可以让NPU跨PCIE能访问的地址空间
6. kTensorPlacementEnd
7. };
```
