---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-tensorplacement
title: TensorPlacement
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > TensorPlacement
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:41+08:00
doc_updated_at: 2026-06-27
content_hash: sha256:eb0e098a78d7a42ca92b30ec8cef33a3984336582c71e8ac33533dcfea9efa1c
---

Tensor存储位置的枚举值定义如下。

```cpp
enum TensorPlacement {
    kOnDeviceHbm, // < Tensor位于Device上的HBM内存
    kOnHost, // < Tensor位于Host
    kFollowing, // < Tensor位于Host，且数据紧跟在结构体后面
    kOnDeviceP2p, // < Tensor位于Device上的P2p内存，指的是HBM透到PCIE BAR空间上，可以让NPU跨PCIE能访问的地址空间
    kTensorPlacementEnd
};
```
