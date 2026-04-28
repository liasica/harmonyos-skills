---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getplacement
title: GetPlacement
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > TensorData > GetPlacement
category: harmonyos-guides
scraped_at: 2026-04-28T07:52:13+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:aa9d1c15d08a7fa31a27c5b4fdc26c4d63225eb7f972e20fe0e898a316d4c16b
---

## 函数功能

获取tensor的placement，tensor数据所在的设备位置。

```
1. // tensor数据所在的设备位置
2. enum TensorPlacement {
3. kOnDeviceHbm,  // < Tensor位于Device上的HBM内存
4. kOnHost,       // < Tensor位于Host
5. kFollowing,    // < Tensor位于Host，且数据紧跟在结构体后面
6. kTensorPlacementEnd
7. };
```

## 函数原型

```
1. TensorPlacement GetPlacement() const
```

## 参数说明

无

## 返回值

tensor的placement。

关于TensorPlacement类型的定义，请参见[TensorPlacement](cannkit-tensorplacement.md)。

## 约束说明

无

## 调用示例

```
1. std::vector<int> a = {10};
2. auto addr = reinterpret_cast<void *>(a.data());
3. TensorData td(addr, HostAddrManager, 100U, kOnHost);
4. auto td_place = td.GetPlacement(); // kOnHost
```
