---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getplacement
title: GetPlacement
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > TensorData > GetPlacement
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:40+08:00
doc_updated_at: 2026-05-12
content_hash: sha256:ed639398c7597f6622ebc5dff73dec1ae9cbc8857573bb82a62aae8e11b571b2
---

## 函数功能

获取tensor的placement，tensor数据所在的设备位置。

```cpp
// tensor数据所在的设备位置
enum TensorPlacement {
  kOnDeviceHbm, // < Tensor位于Device上的HBM内存
  kOnHost, // < Tensor位于Host
  kFollowing, // < Tensor位于Host，且数据紧跟在结构体后面
  kTensorPlacementEnd
};
```

## 函数原型

```cpp
TensorPlacement GetPlacement() const
```

## 参数说明

无

## 返回值

tensor的placement。

关于TensorPlacement类型的定义，请参见[TensorPlacement](cannkit-tensorplacement.md)。

## 约束说明

无

## 调用示例

```cpp
std::vector<int> a = {10};
auto addr = reinterpret_cast<void *>(a.data());
TensorData td(addr, HostAddrManager, 100U, kOnHost);
auto td_place = td.GetPlacement(); // kOnHost
```
